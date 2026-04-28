

def test_login(page):
    page.goto("https://www.saucedemo.com/")
    
    page.fill('#user-name', 'standard_user')
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    inventory_container = page.locator("#inventory_container").first
    assert inventory_container.is_visible()


def test_login_incorrecto(page):
    page.goto("https://www.saucedemo.com/")
    
    page.fill('#user-name', 'test')
    page.fill("#password", "error")
    page.click("#login-button")
    error_message = page.locator("[data-test='error']")
    assert error_message.is_visible()