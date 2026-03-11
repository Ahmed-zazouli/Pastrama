import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get absolute path to the local HTML file
        file_path = f"file://{os.path.abspath('dar-el-kaid/index.html')}"

        # Go to the local page
        await page.goto(file_path)

        # Wait a bit for images to load
        await page.wait_for_timeout(2000)

        # Take screenshot
        screenshot_path = "/home/jules/verification/dar-el-kaid.png"
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
