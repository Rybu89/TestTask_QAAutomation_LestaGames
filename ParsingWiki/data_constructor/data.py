from dataclasses import make_dataclass
from ParsingWiki.page.wiki_page import WikiPage


ad = WikiPage()

class DataClassCollections:
    def create_a_collection_of_classes(self):
        """ Метод создания коллекции объектов класса.
                Возвращает:
                    - словарь состоящий из сгенерированных классов (dict)."""

        number_of_entries = ad.get_number_of_entries()
        n = 1
        creator_of_class_collections = {}
        for e in number_of_entries:
            name_class = ad.get_value_websites(n)
            name_key = ad.get_value_websites(n)
            class_creator = make_dataclass(name_class, [
                ("websites", str),
                ("popularity", list),
                ("frontend", list),
                ("backend", list),
                ("notes", str)]
                 )
            new_class = class_creator(
                websites=ad.get_value_websites(n),
                popularity=ad.get_value_popularity(n),
                frontend=ad.get_value_frontend(n),
                backend=ad.get_value_backend(n),
                notes=ad.get_value_notes(n)
            )
            creator_of_class_collections[name_key] = new_class
            n += 1
        return creator_of_class_collections



