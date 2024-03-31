import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(storage_state="src/auth.json")
    page = await context.new_page()
    await page.goto("https://testwebsite.com")
    await page.get_by_role("button", name="My Dashboard").click()
    await page.locator(".status-cell > .multiselect-container > .multiselect > .multiselect__select").first.click()
    await page.locator("#client-table-1078866").get_by_text("Applied").first.click()
    await page.get_by_role("button", name="Yes").click()
    await page.get_by_text("cancel").click()
    await page.get_by_text("cancel", exact=True).click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
