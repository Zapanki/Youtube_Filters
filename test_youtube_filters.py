import time

import pytest
from selenium.webdriver.common.by import By


base_url = 'https://www.youtube.com/'
expected_success_url = "https://www.youtube.com/"


@pytest.mark.parametrize("name", [
    ("ufc"),
    ("soccer")
])
@pytest.mark.youtube_test
def test_youtube_search(browser, name):
    browser.get(base_url)
    browser.find_element(By.NAME, "search_query").click()
    browser.implicitly_wait(3)
    browser.find_element(By.NAME, "search_query").send_keys(name)
    browser.implicitly_wait(3)
    browser.find_element(By.ID, "search-icon-legacy").click()
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, ".style-scope.ytd-search-sub-menu-renderer .yt-spec-touch-feedback-shape__fill").click()
    browser.find_element(By.CLASS_NAME, "style-scope ytd-search-filter-renderer").click()
    browser.implicitly_wait(3)
    browser.find_element(By.ID, "guide-icon").click()
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, "ytd-mini-guide-renderer [role='tab']:nth-of-type(3) #icon").click()
    browser.find_element(By.ID, "logo-icon").click()
    browser.implicitly_wait(3)
    assert expected_success_url==browser.current_url
    browser.refresh()
