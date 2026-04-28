 # 1. Abrir web
def test_login(page):
    page.goto("https://www.saucedemo.com/")

    # 2. Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # 3. Añadir 2 productos al carrito
    page.click("#add-to-cart-sauce-labs-fleece-jacket")
    page.click("#add-to-cart-sauce-labs-bike-light")

    # 4. Verificar cantidad de productos en el carrito
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.text_content() == "2" 

    