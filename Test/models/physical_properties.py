"""Базовый класс, описывающий сущность человека, его стандартные физические свойства"""


class PhysicalProperties(HumanBaseModel):
    """Класс, описывающий физические свойства человека, наследуемый от базового класса HumanBaseModel"""

    def __init__(self, gender=None, height=None, weight=None, eye_color=None, hair_color=None, blood_type=None, **kwargs):
        """
        Инициализирует атрибуты физического состояния человека
        Параметры упорядочены по значимости:
        gender -> height -> weight -> eye_color -> hair_color -> blood_type
        """
        super().__init__(**kwargs)  # Инициализируем базовые атрибуты из HumanBaseModel
        self.gender = gender            # Пол
        self.height = height            # Рост
        self.weight = weight            # Вес
        self.eye_color = eye_color      # Цвет глаз
        self.hair_color = hair_color    # Цвет волос
        self.blood_type = blood_type    # Группа крови

    def describe_physical(self):
        """Возвращает строковое описание физических характеристик человека"""
        return (f"Пол: {self.gender}, Рост: {self.height} см, Вес: {self.weight} кг, "
                f"Цвет глаз: {self.eye_color}, Цвет волос: {self.hair_color}, Группа крови: {self.blood_type}")

# Пример использования:
human_physical = PhysicalProperties(
    first_name="Иван",
    last_name="Иванов",
    middle_name="Иванович",
    race="европеоид",
    nationality="русский",
    place_of_birth="Москва",
    date_of_birth="01.01.1990",
    gender="мужской",
    height=180,
    weight=75,
    eye_color="карие",
    hair_color="черные",
    blood_type="O+"
)