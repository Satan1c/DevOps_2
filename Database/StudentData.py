from dataclasses import dataclass

from Models.WantedGrades import WantedGrade
from Models.Grade import Grade
from Models.Student import Student

@dataclass
class StudentData:
	student: Student = None
	_grades: Grade = None
	_wanted_grades: WantedGrade = None

	def __str__(self):
		return f"{self.student}, Grades: {self.grades}, Wanted Grades: {self.wanted_grades}"

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
