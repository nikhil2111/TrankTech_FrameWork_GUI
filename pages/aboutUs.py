class AboutUs():
    def __init__(self,page):
        self.page=page
        self.about=page.locator('(//a[text()="About us"])[1]')
        self.selectFrm=page.locator('//a[@aria-hidden="false" and .//img[@alt="Selected Firms"]]')
        self.goodFrm=page.locator('//a[@aria-hidden="false" and .//img[@alt="Good Firms"]]')
        self.develop4U=page.locator('//a[@aria-hidden="false" and .//img[@alt="Develop4U"]]')
        self.clutch=page.locator('//a[@aria-hidden="false" and .//img[@alt="Clutch"]]')
        self.semFrm=page.locator('//a[@aria-hidden="false" and .//img[@alt="Sem Firms"]]')
        self.softDev=page.locator('//a[@aria-hidden="false" and .//img[@alt="Top Software developers"]]')
        self.trustPilot=page.locator('//a[@aria-hidden="false" and .//img[@alt="Trust Pilot"]]')
        self.techRev=page.locator('//a[@aria-hidden="false" and .//img[@alt="Tech Reviewer"]]')
        
        self.about_List=[self.selectFrm,self.goodFrm,self.develop4U,self.clutch,self.semFrm,self.softDev,self.trustPilot,self.techRev]


    def click_AboutUs(self):
        self.about.click()
        for i in self.about_List:
            self.about.click()
            if i.is_visible():
                with self.page.context.expect_page() as new_page_info:
                    i.click()
                new_tab=new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()