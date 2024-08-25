"""
Базовый класс. Содержит первичные идентификаторы человека без детализации, только самые главные.
"""


class HumanBaseModel:

    # Атрибут класса:
    # -

    def __init__(self, surname: str = None, first_name: str = None, middle_name: str = None,
                 date_of_birth: int = None, birthplace: str = None, nationality: str = None, race: str = None):
        """
        Базовый класс. Содержит первичные идентификаторы человека без детализации, только самые главные. \
        Все атрибуты опциональны и могут быть None, что позволяет гибко работать с классом в разных ситуациях,
        когда может отсутствовать информация.

        :param surname: 1. Фамилия (last_name)
        :param first_name: 2. Имя (first_name)
        :param middle_name: 3. Отчество (middle_name)
        :param date_of_birth: 4. Дата рождения (year of birth)
        :param birthplace: 5. Место рождения (place of birth)
        :param nationality: 6. Национальность (nationality)
        :param race: 7. Раса (race)
        """

        self.surname = surname  # 1.
        self.first_name = first_name  # 2.
        self.middle_name = middle_name  # 3.
        self.date_of_birth = date_of_birth  # 4.
        self.birthplace = birthplace  # 5.
        self.nationality = nationality  # 6.
        self.race = race or self.determine_race_by_nationality(nationality)  # 7.

    def determine_race_by_nationality(self, nationality: str) -> str:
        """
        Определяет расу на основе национальности.

        :param nationality: Национальность человека.
        :return: Название расы.
        """
        race_mapping = {
            "русский": "европеоид",
            "немец": "европеоид",
            "японец": "азиат",
            "китаец": "азиат",
            "негр": "негроид",
            "араб": "кавказоид",
            # Можно расширить маппинг на другие национальности
        }
        return race_mapping.get(nationality.lower(), "неопределённая раса")

    def describe(self):
        """Возвращает строковое описание основных характеристик человека"""

        return (f'Фамилия: {self.surname}, Имя: {self.first_name}, Отчество: {self.middle_name}, '
                f'Дата рождения: {self.date_of_birth}, Место рождения: {self.birthplace}, '
                f'Национальность: {self.nationality}, Раса: {self.race}.')


# Пример вызова:
# artem = HumanBaseModel('Познышев', 'Артем', 'Александрович', '21.08.1989',
# 'Россиия, г.Орск, Оренбургской области', 'Русский')
# print(artem.describe())