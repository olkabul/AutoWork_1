class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.admin_link_text = "Admin"
        self.logout_id = "logout-link"

    def click_admin(self):
        self.driver.find_element_by_link_text(self.admin_link_text).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_id).click()