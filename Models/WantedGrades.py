from typing import Dict

from Models.Grade import Grade


class WantedGrade(Grade):
	@staticmethod
	def from_json(data: dict) -> "WantedGrade":
		return WantedGrade(data)

	def set_grade(self, subject: str, grade: float):
		self._grades[subject] = max(grade, 0)

	def set_grades(self, grades: Dict[str, float]):
		for subject, grade in grades.items():
			self.set_grade(subject, grade)
