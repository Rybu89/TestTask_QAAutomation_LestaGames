from ParsingWiki.web_driver.driver import Webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import string
import re


class WikiPage(Webdriver):

    def get_record_text(self, locator):
        """ Метод получения текста из элемента.
                Принимает:
                    locator - локатор элемента (Str).
        """

        return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.XPATH, locator))).text

    def get_record_all_attribute(self, elements_locator, name_attribute):
        """ Метод получения списка значений атрибутов элементов.
                Принимает:
                    elements_locator - локатор элементов (Str);
                    name_attribute - имя атрибута элементов.
                Возвращает:
                    list_value_attribute - список значений атрибута указанных элементов (List).
        """

        list_elements = WebDriverWait(self.browser, 10)\
            .until(ec.presence_of_all_elements_located((By.XPATH, elements_locator)))
        list_value_attribute = []
        n = 0
        for _ in list_elements:
            list_value_attribute.append(list_elements[n].get_attribute(name_attribute))
            n += 1
        return list_value_attribute

    def get_value_websites(self, entry_number):
        """ Метод получения текста содержащегося в поле/элементе столбца «Websites».
            Принимает:
               entry_number - порядковый номер строки в таблице (Int).
            Возвращает:
               - текст содержащийся в поле/элементе (Str).
        """

        websites_value_locator = f"//table[contains(@class, " \
                                 f"'wikitable sortable jquery-tablesorter')][1]/tbody/tr[{entry_number}]/td[1]/a"
        return self.get_record_text(websites_value_locator)

    def get_value_popularity(self, entry_number):
        """ Метод получения текста содержащегося в поле/элементе столбца «Popularity».
            Принимает:
               entry_number - порядковый номер строки в таблице (Int).
            Возвращает:
               - текст содержащийся в поле/элементе (List).
        """
        popularity_value_locator = f"//table[contains(@class, " \
                                   f"'wikitable sortable jquery-tablesorter')][1]/tbody/tr[{entry_number}]/td[2]"
        popularity_value = self.get_record_text(popularity_value_locator)
        for punctuation in string.punctuation:
            popularity_value = popularity_value.replace(punctuation, '')
        value = re.findall(r'\b\d+\b', popularity_value)
        return value

    def get_value_frontend(self, entry_number):
        """ Метод получения значений содержащихся в поле/элементе столбца «Front-end (Client-side)».
            Принимает:
               entry_number - порядковый номер строки в таблице (Int).
            Возвращает:
               - список значений содержащихся в поле/элементе (List).
        """

        frontend_value_locator = f"//table[contains(@class, " \
                                 f"'wikitable sortable jquery-tablesorter')][1]/tbody/tr[{entry_number}]/td[3]/a"
        return self.get_record_all_attribute(frontend_value_locator, 'title')

    def get_value_backend(self, entry_number):
        """ Метод получения значений содержащихся в поле/элементе столбца «Back-end (Server-side)».
            Принимает:
               entry_number - порядковый номер строки в таблице (Int).
            Возвращает:
               - список значений содержащихся в поле/элементе (List).
        """

        backend_value_locator = f"//table[contains(@class, " \
                                f"'wikitable sortable jquery-tablesorter')][1]/tbody/tr[{entry_number}]/td[4]/a"
        return self.get_record_all_attribute(backend_value_locator, 'title')

    def get_value_database(self, entry_number):
        """ Метод получения значений содержащихся в поле/элементе столбца «Database».
            Принимает:
               entry_number - порядковый номер строки в таблице (Int).
            Возвращает:
               - список значений содержащихся в поле/элементе (List).
        """

        database_value_locator = f"//table[contains(@class, " \
                                 f"'wikitable sortable jquery-tablesorter')][1]/tbody/tr[{entry_number}]/td[5]/a"
        return self.get_record_all_attribute(database_value_locator, 'title')

    def get_value_notes(self, entry_number):
        """ Метод получения текста содержащегося в поле/элементе столбца «Notes».
            Принимает:
               entry_number - порядковый номер строки в таблице (Int).
            Возвращает:
               - текст содержащийся в поле/элементе (Str).
        """

        notes_value_locator = f"//table[contains(@class, " \
                              f"'wikitable sortable jquery-tablesorter')][1]/tbody/tr[{entry_number}]/td[6]"
        return self.get_record_text(notes_value_locator)

    def get_number_of_entries(self):
        """ Метод получения всех элементов столбца «Websites» == количество записей из таблицы «Programming
            languages used in most popular websites».
                Возвращает:
                    - список полей/элементов (WebElement).
        """

        return WebDriverWait(self.browser, 10). \
            until(ec.presence_of_all_elements_located(
            (By.XPATH, "//table[contains(@class, 'wikitable sortable jquery-tablesorter')][1]/tbody/tr/td[1]/a")))
