import json
from uuid import UUID

from Database.abc.DataManagerABC import DataManagerABC
from Models.Student import Student


class StudentsManager(DataManagerABC):
	def __init__(self, path: str):
		super().__init__("Student-", path)

	def load(self, uid: str, path: str) -> None:
		self.objects[uid] = Student.from_json(uid, json.load(open(path)))

	def add_student(self, student: Student) -> None:
		self.objects[student.uid] = student

	def get_student(self, uid: str) -> Student:
		return self.objects.get(uid)
