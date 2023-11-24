from ParsingWiki.web_driver.driver import Webdriver
import pytest

driver = Webdriver()
@pytest.fixture(scope="module")
def from_parsing_tests():
    """ Для тестов использующих webdriver selenium. """

    print('\n ENTER')
    yield
    # закрытие драйвера
    driver.browser.quit()
    print('\n EXIT')


@pytest.fixture()
def from_tests():
    """ Для обозначения тестов. """

    print('\n START TEST')
    yield
    print('\n FINISH TEST')


