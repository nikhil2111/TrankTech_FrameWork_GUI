class ContactUs():
    def __init__(self,page):
##-----ContactUs Form (locators)----
        self.page=page
        self.contact=page.locator('(//a[text()="Contact us"])[1]')
        self.un=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.umail=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.send_button=page.locator('(//button[text()="Send OTP"])[2]')
        self.otp=page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.comp=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.serv=page.locator('(//select[@name="service"])[2]')
        self.ph=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.msg=page.locator('(//textarea[@placeholder="Message"])[2]')


##-----Methods to perform actions(ContactUs Form options)
    def contact_FormFill(self):
        self.contact.click()
        self.un.fill("Tester")
        self.umail.fill("tester@mailinator.com")
        self.page.once("dialog",lambda dialog:dialog.accept())
        self.send_button.click()
        self.page.wait_for_timeout(5000)
        self.otp.fill("123456")
        self.comp.fill("Quality_tech")
        self.serv.select_option("App Development")
        self.ph.fill("9898989898")
        self.msg.fill("I am Quality Eng")



