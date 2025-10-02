import os
from abc import ABC, abstractmethod
from uuid import UUID

from Database.JsonSaver import JsonSaver
from Models.abc.JsonSerializableABC import JsonSerializableABC


class DataManagerABC(JsonSaver):
	def __init__(self, prefix: str, path: str):
		super().__init__()
		self.prefix = prefix
		self.path = path
		self.objects: dict[str, JsonSerializableABC] = {}

	def is_valid(self, name: str) -> bool:
		return name.startswith(self.prefix)

	@abstractmethod
	def load(self, uid: str, path: str) -> None:
		pass

	def save_json(self, group, uid) -> None:
		super().add(self.objects.get(uid).to_json())
		super().save(os.path.join(self.path, f"Group-{group}", f"{self.prefix}{uid}"))
		super().clear()

