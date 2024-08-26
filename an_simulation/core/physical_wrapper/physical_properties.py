from human_base import HumanBaseModel

class PhysicalProperties(HumanBaseModel):
    """
    Класс, описывающий физические свойства человека. Наследуется от HumanBaseModel и включает детализированную информацию о физическом состоянии и внешности человека.

    Атрибуты:
    ----------
    height : float
        Рост человека в сантиметрах.
    weight : float
        Вес человека в килограммах.
    eye_color : str
        Цвет глаз (например, карие, голубые, зеленые и т.д.).
    hair_color : str
        Цвет волос (например, черные, каштановые, светлые и т.д.).
    blood_type : str
        Группа крови человека (например, O, A, B, AB и их резус-фактор).
    skin_color : str
        Цвет кожи (например, светлая, темная, оливковая).
    body_type : str
        Тип телосложения (например, эктоморф, мезоморф, эндоморф).
    fitness_level : str
        Уровень физической подготовки (например, атлет, средний, низкий).
    handedness : str
        Руководство человека (левша, правша, амбидекстр).
    facial_hair : str
        Наличие и тип лицевых волос (например, борода, усы, бакенбарды).
    tattoos : str
        Описание татуировок (если есть).
    scars : str
        Описание шрамов (если есть).
    posture : str
        Осанка человека (например, прямая, сутулая).
    shoe_size : float
        Размер обуви.
    voice_pitch : str
        Тембр голоса (например, высокий, средний, низкий).
    """

    def __init__(self, height: float = None, weight: float = None, eye_color: str = None,
                 hair_color: str = None, blood_type: str = None, skin_color: str = None,
                 body_type: str = None, fitness_level: str = None, handedness: str = None,
                 facial_hair: str = None, tattoos: str = None, scars: str = None,
                 posture: str = None, shoe_size: float = None, voice_pitch: str = None, **kwargs):
    """
        Инициализирует физические свойства человека.

        :param height: Рост человека (в сантиметрах).
        :param weight: Вес человека (в килограммах).
        :param eye_color: Цвет глаз (карие, голубые, зеленые и т.д.).
        :param hair_color: Цвет волос (черные, каштановые, светлые и т.д.).
        :param blood_type: Группа крови человека (O, A, B, AB и их резус-фактор).
        :param skin_color: Цвет кожи (светлая, темная, оливковая).
        :param body_type: Тип телосложения (эктоморф, мезоморф, эндоморф).
        :param fitness_level: Уровень физической подготовки (атлет, средний, низкий).
        :param handedness: Руководство человека (левша, правша, амбидекстр).
        :param facial_hair: Лицевые волосы (борода, усы, бакенбарды).
        :param tattoos: Татуировки (описание).
        :param scars: Шрамы (описание).
        :param posture: Осанка (прямая, сутулая).
        :param shoe_size: Размер обуви.
        :param voice_pitch: Тембр голоса (высокий, средний, низкий).
        :param kwargs: Дополнительные параметры, передаваемые базовому классу.
    """

    super().__init__(**kwargs)
        self.height = height