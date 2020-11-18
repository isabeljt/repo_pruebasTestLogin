"""
These tests cover DuckDuckGo searches.
"""

from pages.main import ProductStoreMainPage
# from pages.search import DuckDuckGoSearchPage


def test_basic_productStore_Login(browser):
  main_page = ProductStoreMainPage(browser)
 # result_page = DuckDuckGoResultPage(browser)
 # PHRASE = "panda"

  # Given the Product Store home page is displayed
  main_page.load()

  # When the user pulse loginButton
  main_page.login()

"""
  # Then the search result title contains "panda"
  assert PHRASE in result_page.title()

  # And the search result query is "panda"
  assert PHRASE == result_page.search_input_value()

  # And the search result links pertain to "panda"
  titles = result_page.result_link_titles()
  matches = [t for t in titles if PHRASE.lower() in t.lower()]
  assert len(matches) > 0
"""
