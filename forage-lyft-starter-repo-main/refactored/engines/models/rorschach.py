# from datetime import datetime

# from engines.willoughby_engine import WilloughbyEngine


# class Rorschach(WilloughbyEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False

class Rorschach:
    def __init__(self, name: str, model: str, year: int):
        self.name = name
        self.model = model
        self.year = year