def test_landing_page(driver, live_server):
    driver.get(live_server.url)
    assert 'hangman' in driver.page_source.lower()
    assert driver.find_element_by_css_selector('[data-test="log-in"]')
