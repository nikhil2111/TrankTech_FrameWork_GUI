class Portfolio():
    def __init__(self,page):
        self.page=page
        self.port=page.locator('//a[text()="Portfolio"]')
        self.ics=page.locator('(//a[text()="View More"])[1]')
        self.wings=page.locator('(//a[text()="View More"])[2]')
        self.arena=page.locator('(//a[text()="View More"])[3]')
        self.home=page.locator('(//a[text()="View More"])[4]')
        self.club=page.locator('(//a[text()="View More"])[5]')
        self.cords=page.locator('(//a[text()="View More"])[6]')
        self.port_List=[self.ics,self.wings,self.arena,self.home,self.club,self.cords]

##-----Portfolio - Web Development options(locators and stored as list)----
        self.web1=page.locator('//a[text()="CMS Website Development"]')
        # self.web2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        # self.web2_NewWindow=page.locator('//a[text()="Website Development"]')
        self.web3=page.locator('//a[text()="Custom Web Portal Development"]')
        self.webDev_List=[self.web1,self.web3]

##-----Portfolio - UI UX Design options(locators and stored as list)----
        self.ux1=page.locator('//a[text()="Mobile App Design"]')
        self.ux2=page.locator('//a[text()="Responsive Web Design"]')
        self.ux3=page.locator('//a[text()="Brand Identity Design"]')
        self.ux_List=[self.ux1,self.ux2,self.ux3]

##-----Portfolio - App Development options(locators and stored as list)----
        self.app1=page.locator('//a[text()="iOS App Development"]')
        # self.app2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        #self.app2_NewWindow1=page.locator('(//a[text()="Android App Development"])[2]')
        #self.app2_NewWindow2=page.locator('(//a[text()="App Development"])[2]')
        self.app3=page.locator('//a[text()="Hybrid Mobile App Development"]')
        self.app4=page.locator('//a[text()="Cross-Platform App Development"]')
        self.app5=page.locator('//a[text()="Progressive Web App Development"]')
        self.app_List=[self.app1,self.app3,self.app4,self.app5]

##-----Portfolio - Graphic Design options(locators and stored as list)----
        self.graph1=page.locator('//a[text()="Logo Design"]')
        self.graph2=page.locator('//a[text()="Banner Design"]')
        self.graph3=page.locator('//a[text()="Packaging Design"]')
        self.graph4=page.locator('//a[text()="Business cards Design"]')
        self.graph_List=[self.graph1,self.graph2,self.graph3,self.graph4]

##----Method to handle Portfolio options with newpage
    def click_PortNewWindow(self):
        for i in self.port_List:
            self.port.click()
            if i.get_attribute("target") == "_blank":
                with self.page.context.expect_page() as new_page_info:
                    i.click()
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()
            else:
                i.click()

##-----Methods to perform actions(Portfolio - Web Development options)
    def click_webDev(self):
        for i in self.webDev_List:
            self.port.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Portfolio - UI UX Design options)
    def click_ux(self):
        for i in self.ux_List:
            self.port.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Portfolio - App Development options)
    def click_App(self):
        for i in self.app_List:
            self.port.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Portfolio - Graphic Design options)
    def click_graph(self):
        for i in self.graph_List:
            self.port.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()