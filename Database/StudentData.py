from dataclasses import dataclass

from Models.Grade import Grade
from Models.Student import Student
from Models.WantedGrades import WantedGrade
from Models.abc.JsonSerializableABC import JsonSerializableABC


@dataclass
class StudentData(JsonSerializableABC):
	student: Student = None
	_grades: Grade = None
	_wanted_grades: WantedGrade = None

	def __str__(self) -> str:
		return str(self.to_json())

	@property
	def grades(self) -> Grade:
		if self._grades is None:
			self._grades = Grade({})
		return self._grades

	@grades.setter
	def grades(self, grades: Grade) -> None:
		self._grades = grades

	@property
	def wanted_grades(self) -> WantedGrade:
		if self._wanted_grades is None:
			self._wanted_grades = WantedGrade({})
		return self._wanted_grades

	@wanted_grades.setter
	def wanted_grades(self, grades: WantedGrade) -> None:
		self._wanted_grades = grades

	def to_json(self) -> dict:
		return {
			"student": self.student.to_json() if self.student else "{}",
			"grades": self.grades.to_json() if self.grades else "{}",
			"wanted_grades": self.wanted_grades.to_json() if self.wanted_grades else "{}"
		}
