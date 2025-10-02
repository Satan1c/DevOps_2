from abc import ABC, abstractmethod
from typing import Self


class JsonSerializableABC(ABC):
	@abstractmethod
	def to_json(self) -> dict:
		pass

	@classmethod
	def from_json(cls, json_data: dict) -> Self:
		pass
