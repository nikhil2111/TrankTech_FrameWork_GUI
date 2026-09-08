
class Blog:
    def __init__(self,page):
        self.page=page
        self.blog=page.locator('(//a[text()="Blog"])[1]')
        self.blog1=page.locator('(//a[text()="App Development"])[1]')
        self.blog2=page.locator('(//a[text()="Web Development"])[1]')
        self.blog3=page.locator('(//a[text()="Software Development"])[1]')
        self.blog4=page.locator('(//a[text()="Digital Marketing"])[1]')
        self.blog5=page.locator('(//a[text()="Email Marketing"])[1]')
        self.blog6=page.locator('(//a[text()="Artificial Intelligence"])[2]')
        self.blog7=page.locator('(//a[text()="UI UX Design"])[1]')
        self.blog8=page.locator('//a[text()="Content Marketing"]')
        self.blog9=page.locator('(//a[text()="CRM Development"])[3]')
        self.blog10=page.locator('(//a[text()="ECommerce Development"])[5]')
        self.blog11=page.locator('(//a[text()="Graphic Design"])[3]')
        self.blog12=page.locator('//a[text()="Software & IT Company"]')

        self.blog_list=[self.blog1,self.blog2,self.blog3,self.blog4,self.blog5,self.blog6,self.blog7,self.blog8,self.blog9,self.blog10,self.blog11,self.blog12]

##-----Blogs-WebDevelopment options (locators and stored as list)----
        self.bCMS=page.locator('//a[text()="CMS Website Development"]')
        self.beCom=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.beComNewWindow=page.locator('//a[text()="Website Development Delhi"]')
        self.bCustom=page.locator('//a[text()="Custom Web Portal Development"]')
        
        self.W_List=[self.bCMS,self.bCustom]

##-----Blogs - UI UX Design options(locators and stored as list)----
        self.ux1=page.locator('//a[text()="Mobile App Design"]')
        self.ux2=page.locator('//a[text()="Responsive Web Design"]')
        self.ux3=page.locator('//a[text()="Brand Identity Design"]')
        self.ux_List=[self.ux1,self.ux2,self.ux3]

##-----Blog - App Development options(locators and stored as list)----
        self.app1=page.locator('//a[text()="iOS App Development"]')
        self.app2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.app2_NewWindow1=page.locator('//a[text()="Android App Development Delhi"]')
        self.app2_NewWindow2=page.locator('//a[text()="App Development Delhi"]')
        self.app3=page.locator('//a[text()="Hybrid Mobile App Development"]')
        self.app4=page.locator('//a[text()="Cross-Platform App Development"]')
        self.app5=page.locator('//a[text()="Progressive Web App Development"]')
        self.app_List=[self.app1,self.app3,self.app4,self.app5]
        self.app_NewWin_List=[self.app2_NewWindow1,self.app2_NewWindow2]

##-----Portfolio - App Development options(locators and stored as list)----
        self.app1=page.locator('//a[text()="iOS App Development"]')
        self.app2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.app2_NewWindow1=page.locator('(//a[text()="Android App Development"])[2]')
        self.app2_NewWindow2=page.locator('(//a[text()="App Development"])[2]')
        self.app3=page.locator('//a[text()="Hybrid Mobile App Development"]')
        self.app4=page.locator('//a[text()="Cross-Platform App Development"]')
        self.app5=page.locator('//a[text()="Progressive Web App Development"]')
        self.app_List=[self.app1,self.app3,self.app4,self.app5]
        
##-----Blog - Graphic Design options(locators and stored as list)----
        self.graph1=page.locator('//a[text()="Logo Design"]')
        self.graph2=page.locator('//a[text()="Banner Design"]')
        self.graph3=page.locator('//a[text()="Packaging Design"]')
        self.graph4=page.locator('//a[text()="Business cards Design"]')
        self.graph_List=[self.graph1,self.graph2,self.graph3,self.graph4]



##-----Methods to perform actions(Blogs options)
    def click_blog_option(self):
        for i in self.blog_list:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Blogs-Web Development options)
    def click_blog_webDev(self):
        for i in self.W_List:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        self.beCom.click()
        with self.page.context.expect_page() as new_page_info:
            self.beComNewWindow.click()
        new_tab = new_page_info.value
        new_tab.wait_for_load_state("load")
        new_tab.close()
        

##-----Methods to perform actions(Blog - UI UX Design options)
    def click_ux(self):
        for i in self.ux_List:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Blog - App Development options)
    def click_App(self):
        for i in self.app_List:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def click_App_NewWin(self):
        self.app2.click()
        for i in self.app_NewWin_List:
            with self.page.context.expect_page() as new_page_info:
                i.click()
            new_tab=new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()

##-----Methods to perform actions(Blog - Graphic Design options)
    def click_Bgraph(self):
        for i in self.graph_List:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        self.page.go_back()  