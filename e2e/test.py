

def test_login(page):
    page.goto("https://www.saucedemo.com/")
    
    page.fill('#user-name', 'standard_user')
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    inventory_container = page.locator("[data-test='inventory-container']")
    expect(inventory_container).to_be_visible()


def test_login_incorrecto(page):
    page.goto("https://www.saucedemo.com/")
    
    page.fill('#user-name', 'test')
    page.fill("#password", "error")
    page.click("#login-button")
    error_message = page.locator("[data-test='error']")
    assert error_message.is_visible()