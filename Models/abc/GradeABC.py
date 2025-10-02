from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Self

from Models.abc.JsonSerializableABC import JsonSerializableABC


@dataclass
class GradeABC(JsonSerializableABC, ABC):
	_grades: Dict[str, float]

	def get_grade(self, subject: str) -> float:
		return self._grades.get(subject, 0.0)

	@abstractmethod
	def avg_grade(self) -> float:
		return sum(self._grades.values()) / len(self._grades)

	@classmethod
	def from_json(cls, json_data: dict) -> Self:
		_grades = json_data

	@abstractmethod
	def to_json(self) -> dict:
		return self._grades
