import pytest
from ParsingWiki.data_constructor.data import DataClassCollections

dat = DataClassCollections()

class Tests:
    test_date = [
        (int(10 ** 7)),
        (int(1.5 * 10 ** 7)),
        (int(5 * 10 ** 7)),
        (int(10 ** 8)),
        (int(5 * 10 ** 8)),
        (int(10 ** 9)),
        (int(1.5 * 10 ** 9)),
    ]

    @pytest.mark.parametrize('data', test_date)
    def test_check_popularity(self, from_parsing_tests, from_tests, data):
        """ Проверяет, что в таблице «Programming languages used in most popular websites» в столбце «Popularity(unique
         visitors per month)» нет строк, значение которых меньше передаваемых.
                Принимает:
                    test_date - список проверяемых значений (list).
        """

        class_collection = dat.create_a_collection_of_classes()
        class_names = list(class_collection)
        n = 0
        for _ in class_names:
            get_name_class = class_names[n]
            get_class = class_collection[get_name_class]
            get_popularity_value = get_class.popularity[0]
            convert_popularity_value = int(get_popularity_value)
            assert convert_popularity_value > data, f"{get_name_class}(Frontend:|Backend:) has {get_popularity_value}" \
                                                    f" unique visitors per month. (Expected more than {data})"
            n += 1
