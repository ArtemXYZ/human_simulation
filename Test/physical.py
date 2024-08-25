from human_base import HumanBaseModel

class PhysicalProperties(HumanBaseModel):
    def __init__(self, height=None, weight=None, eye_color=None, hair_color=None, blood_type=None, **kwargs):
        super().__init__(**kwargs)
        self.height = height
        self.weight = weight
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.blood_type = blood_type