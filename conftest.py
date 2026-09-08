
from pathlib import Path
import re
import shutil

import pytest
from playwright.sync_api import sync_playwright
import pytest_html

from config import BASE_URL

@pytest.fixture(scope="session")
def browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)

    yield browser

    browser.close()
    p.stop()


@pytest.fixture
def page(request, browser):
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")

    yield page

    video = page.video
    context.close()

    if video:
        source = Path(video.path())
        safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.nodeid)
        destination = videos_dir / f"{safe_name}.webm"
        shutil.move(str(source), str(destination))

        report = getattr(request.node, "_call_report", None)
        if report:
            report.extras.append(pytest_html.extras.video(str(destination)))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call":
        item._call_report = report
        report.extra = extra

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extra.append(pytest_html.extras.image(str(file_name)))

        report.extra = extra