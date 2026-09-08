class vertical:
    def __init__(self,page):
        self.page=page
##------ Vertical-Trading options(locators and stored as list)
        self.vert=page.locator('(//a[text()="Verticals"])[1]')
        self.VT=page.locator('//strong[text()="Trading"]')
        self.VT_ST=page.locator('(//a[text()="Stock Trading"])[1]')
        self.VT_PT=page.locator('(//a[text()="Paper Trading"])[1]')
        self.VT_CFD=page.locator('(//a[text()="CFD Trading"])[1]')
        self.VT_TA=page.locator('//a[contains(text(),"Trading App")]')
        self.VT_AT=page.locator('(//a[text()="Algo Trading"])[1]')
        self.VT_CT=page.locator('(//a[contains(text(),"Custom")])[1]')
        self.VT_WPT=page.locator('(//a[text()="Web Portal Trading"])[1]')

        self.Vtrade_list=[self.VT_ST,self.VT_PT,self.VT_CFD,self.VT_TA,self.VT_AT,self.VT_CT,self.VT_WPT]

##----  Vertical-Retail and Ecommerence options (locators and stored as list)
        self.vert=page.locator('(//a[text()="Verticals"])[1]')
        self.VR=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.VR1 = page.locator('(//a[contains(text(),"eCommerce")])[1]')
        self.VR2 = page.locator('(//a[contains(text(),"eCommerce")])[2]')

        self.eCom_list=[self.VR1,self.VR2]

##-------Vertical-Healthcare options (locators and stored as list)

        self.vert=page.locator('(//a[text()="Verticals"])[1]')
        self.VH=page.locator('//strong[text()="Healthcare"]')
        self.VH1 = page.locator('(//a[contains(text(),"Diet ")])[1]')
        self.VH2 = page.locator('(//a[text()="Health tracking App"])[1]')

        self.VHealth_list=[self.VH1,self.VH2]

##-------Vertical-Fintech options (locators and stored as list)
        self.vert=page.locator('(//a[text()="Verticals"])[1]')
        self.VF=page.locator('//strong[text()="Fintech"]')   
        self.VF1 = page.locator('(//a[contains(text(),"Pos ")])[1]')
        self.VF2 = page.locator('(//a[text()="Crypto"])[1]')

        self.VFintech_list=[self.VF1,self.VF2]

##-----Vertical-Custom App options(locators and stored as list)----
        self.vert=page.locator('(//a[text()="Verticals"])[1]')
        self.VC=page.locator('//strong[text()="Custom App"]')    
        self.VC1 = page.locator('(//a[contains(text(),"Desktop ")])[1]')
        self.VC2 = page.locator('(//a[text()="HRM Development"])[1]')
        self.VC3 = page.locator('(//a[text()="Travel"])[1]')
        self.VC4 = page.locator('(//a[text()="Dating App Development"])[1]')
        self.VC5 = page.locator('(//a[text()="CRM Development USA"])[1]')
        self.VC6 = page.locator('(//a[text()="CRM Development"])[1]')
        self.VC7 = page.locator('(//a[text()="ERP App Development"])[1]')
        self.VC8 = page.locator('(//a[text()="E-Learning"])[1]')
        self.VC9 = page.locator('(//a[text()="Real Estate"])[1]')

        self.VCustom_list=[self.VC1,self.VC2,self.VC3,self.VC4,self.VC5,self.VC6,self.VC7,self.VC8,self.VC9]


##-----Methods to perform actions(Vertical-Trading options)
    def click_trading_option(self):
        for i in self.Vtrade_list:
            self.vert.hover()
            self.VT.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Vertical-Retail and Ecommerence options)
    def click_Ecom_option(self):
        for i in self.eCom_list:
            self.vert.hover()
            self.VR.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Vertical-Healthcare options)
    def click_health_option(self):
        for i in self.VHealth_list:
            self.vert.hover()
            self.VH.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Vertical-Fintech options)
    def click_fintect_option(self):
        for i in self.VFintech_list:
            self.vert.hover()
            self.VF.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Vertical-Custom options)
    def click_custom_option(self):
        for i in self.VCustom_list:
            self.vert.hover()
            self.VC.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()