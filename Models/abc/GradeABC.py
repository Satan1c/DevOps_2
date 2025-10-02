from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class GradeABC(ABC):
	_grades: Dict[str, float]

	def get_grade(self, subject: str) -> float:
		return self._grades.get(subject, 0.0)

	@abstractmethod
	def avg_grade(self) -> float:
		return sum(self._grades.values()) / len(self._grades)

	@staticmethod
	def from_json(data: dict) -> None:
		_grades = data

	@abstractmethod
	def to_json(self) -> dict:
		return self._grades
