import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # 1. Open demo login page
        await page.goto('https://the-internet.herokuapp.com/login')

        # 2. Fill the username and password
        await page.fill('#username', 'tomsmith')
        await page.fill('#password', 'SuperSecretPassword!')

        # 3. Click the login button
        await page.click('button[type="submit"]')

        # 4. Wait for navigation to complete
        await page.wait_for_selector('.flash.success')

        # 5. Take a screenshot as proof
        await page.screenshot(path='login_success.png')

        await browser.close()

asyncio.run(run())
