import json
from uuid import UUID

from Database.abc.DataManagerABC import DataManagerABC
from Models.WantedGrades import WantedGrade


class WantedGradesManager(DataManagerABC):
	def __init__(self, path: str):
		super().__init__("WantedGrade-", path)

	def load(self, uid: str, path: str) -> None:
		self.objects[uid] = WantedGrade.from_json(json.load(open(path)))

	def add_wanted_grade(self, uid: str, grade: WantedGrade) -> None:
		self.objects[uid] = grade

	def get_wanted_grade(self, uid: str) -> WantedGrade:
		return self.objects.get(uid)
