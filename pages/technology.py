class Technologies:
    def __init__(self,page):
        self.page=page
        ##-----Technologies-EComm options(locators and stored as list)----
        self.tech=page.locator('(//a[text()="Technologies"])[1]')
        self.tech_eC=page.locator('//strong[text()="eCommerce Development"]')

        self.TE1=page.locator('//a[text()="Magento Development"]')
        self.TE2=page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.TE3=page.locator('(//a[text()="Big Commerce"])[1]')
        self.TE4=page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.TE5=page.locator('(//a[contains(text(),"Nop")])[1]')
        self.TE6=page.locator('(//a[text()="Laravel Development"])[1]')
        self.TE7=page.locator('(//a[text()="Drupal Development"])[1]')
        self.TE8=page.locator('(//a[text()="Joomla Development"])[1]')
        self.TE9=page.locator('(//a[text()="Express JS Development"])[1]')
        self.TE10=page.locator('(//a[text()="Opencart Development"])[1]')
        self.TE11=page.locator('(//a[text()="WordPress Development"])[1]')
        self.TE12=page.locator('(//a[text()="Shopify Development"])[1]')
        self.TE13=page.locator('(//a[text()="Node JS Development"])[1]')
        self.TE14=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.TE15=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.TE16=page.locator('(//a[text()="Wix Development"])[1]')
        self.TE17=page.locator('(//a[text()="React JS Development"])[1]')

        self.TeComm_list=[self.TE1,self.TE2,self.TE3,self.TE4,self.TE5,self.TE6,self.TE7,self.TE8,self.TE9,self.TE10,self.TE11,self.TE12,self.TE13,self.TE14,self.TE15,self.TE16,self.TE17]

##-----Technologies-MobileApp options(locators and stored as list)----

        self.tech=page.locator('(//a[text()="Technologies"])[1]')
        self.tech_Mob=page.locator('//strong[text()="Mobile App Development"]')
        
        self.TM1=page.locator('(//a[contains(text(),"React ")])[2]')
        self.TM2=page.locator('(//a[contains(text(),"Xamarin ")])[1]')
        self.TM3=page.locator('(//a[contains(text(),"Flutter ")])[1]') 
        self.TM4=page.locator('(//a[contains(text(),"Swift ")])[1]')
        self.TM5=page.locator('(//a[contains(text(),"Enterprise ")])[1]')
        self.TM6=page.locator('(//a[contains(text(),"Kotlin ")])[1]')
        self.TM7=page.locator('(//a[contains(text(),"Ionic ")])[1]')
        self.TM8=page.locator('(//a[contains(text(),"Appointment ")])[1]')

        self.TMob_list=[self.TM1,self.TM2,self.TM3,self.TM4,self.TM5,self.TM6,self.TM7,self.TM8]

##-----Technologies-ArtificialIntelligence options(locators and stored as list)----

        self.tech=page.locator('(//a[text()="Technologies"])[1]')
        self.artInt=page.locator('//strong[text()="Artificial Intelligence"]')

##-----Methods to perform actions(Technologies-EComm options)

    def click_Ecom_option(self):
        for i in self.TeComm_list:
            self.tech.hover()
            self.tech_eC.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Technologies-ArtificialIntelligence options)

    def click_MobileApp_option(self):
        for i in self.TMob_list:
            self.tech.hover()
            self.tech_Mob.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

##-----Methods to perform actions(Technologies-EComm options)
    
    def click_artInt(self):
        self.tech.hover()
        self.artInt.click()
        self.page.wait_for_load_state("load")
        self.page.go_back()