from abc import ABC, abstractmethod


class DataSaverABC(ABC):
	@abstractmethod
	def add(self, data: dict) -> None:
		pass

	@abstractmethod
	def clear(self) -> None:
		pass

	@abstractmethod
	def save(self, path: str) -> None:
		pass
