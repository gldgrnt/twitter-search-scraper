class css_property_change:
    def __init__(self, driver, locator, css_property):
        # Setup props
        self.driver = driver
        self.locator = locator
        self.css_property = css_property

        # Find initial value
        self.initial_css_property_value = self.driver.find_element(*self.locator).value_of_css_property(self.css_property)


    def __call__(self, driver):
        element = driver.find_element(*self.locator)

        # Check if property has changed
        return element.value_of_css_property(self.css_property) != self.initial_css_property_value