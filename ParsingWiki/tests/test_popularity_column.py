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
        class_names = list(class_collection)
        n = 0
        for _ in class_names:
            get_name_class = class_names[n]
            get_class = class_collection[get_name_class]
            get_popularity_value = get_class.popularity[0]
            convert_popularity_value = int(get_popularity_value)
            # print(get_class)
            frontend_name = get_class.frontend
            backend_name = get_class.backend
            assert convert_popularity_value > data_for, \
                f"{get_name_class}(Frontend:{frontend_name}|Backend:{backend_name}) has {get_popularity_value}" \
                                                    f" unique visitors per month. (Expected more than {data_for})"
            n += 1
