import pytest
from ParsingWiki.data_constructor.data import DataClassCollections

data = DataClassCollections()

class TestPopularityColumn:
    test_date = [
        (int(10 ** 7)),
        (int(1.5 * 10 ** 7)),
        (int(5 * 10 ** 7)),
        (int(10 ** 8)),
        (int(5 * 10 ** 8)),
        (int(10 ** 9)),
        (int(1.5 * 10 ** 9)),
    ]

    @pytest.mark.parametrize('data_for', test_date)
    def test_check_popularity(self, from_parsing_tests, from_tests, data_for):
        """ Проверяет, что в таблице «Programming languages used in most popular websites» в столбце «Popularity(unique
         visitors per month)» нет строк, значение которых меньше передаваемых.
                Принимает:
                    test_date - список проверяемых значений (list).
        """

        class_collection = data.create_a_collection_of_classes()
        result_of_check = []
        for element in list(class_collection):
            get_popularity_value = int(class_collection[element].popularity[0])

            if get_popularity_value < data_for:
                result_of_check.append(f"{element}(Frontend: {class_collection[element].frontend} |Backend: {class_collection[element].backend}) has "
                              f"{get_popularity_value/1000000} millions  "
                              f"unique visitors per month. (Expected more than {data_for/1000000} millions.)")

        assert len(result_of_check) == 0, print(result_of_check)

