from typing import Dict

from Models.Grade import Grade


class WantedGrade(Grade):
	@classmethod
	def from_json(cls, json_data: dict) -> "WantedGrade":
		return WantedGrade(json_data)

	def set_grade(self, subject: str, grade: float):
		self._grades[subject] = max(grade, 0)

	def set_grades(self, grades: Dict[str, float]):
		for subject, grade in grades.items():
			self.set_grade(subject, grade)
