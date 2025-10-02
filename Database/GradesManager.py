import json
from uuid import UUID

from Database.abc.DataManagerABC import DataManagerABC
from Models.Grade import Grade


class GradesManager(DataManagerABC):
	def __init__(self, path: str):
		super().__init__("Grade-", path)

	def load(self, uid: str, path: str) -> None:
		self.objects[uid] = Grade.from_json(json.load(open(path)))

	def add_grade(self, uid: str, grade: Grade) -> None:
		self.objects[uid] = grade

	def get_grade(self, uid: str) -> Grade:
		return self.objects.get(uid)
