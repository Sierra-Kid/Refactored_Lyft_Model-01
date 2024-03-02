# from abc import ABC

# from car import Car


# class SternmanEngine(Car, ABC):
#     def __init__(self, last_service_date, warning_light_is_on):
#         super().__init__(last_service_date)
#         self.warning_light_is_on = warning_light_is_on

#     def engine_should_be_serviced(self):
#         if self.warning_light_is_on:
#             return True
#         else:
#             return False


from typing import List
from models import Car

class SternmanEngine:
    def __init__(self):
        pass

    def get_cars(self) -> List[Car]:
        return [
            Car(name="Toyota", model="Camry", year=2020),
            Car(name="Honda", model="Civic", year=2019),
            Car(name="Ford", model="Mustang", year=2018),
        ]