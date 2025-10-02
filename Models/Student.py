import uuid
from datetime import datetime
from uuid import UUID

from Models.abc.JsonSerializableABC import JsonSerializableABC


class Student(JsonSerializableABC):
	def __init__(self, first_name: str, second_name: str, last_name: str, group: str, bd: datetime, uid: str = None):
		if uid is None:
			uid = str(uuid.uuid4())
		self.__uid = uid
		self.__first_name = first_name.title()
		self.__second_name = second_name.title()
		self.__last_name = last_name.title()
		self.__group = group
		self.__bd = bd

	def __str__(self) -> str:
		return str(self.to_json())

	@property
	def uid(self) -> str:
		return self.__uid

	@property
	def full_name(self) -> str:
		return f"{self.__last_name} {self.__first_name} {self.__second_name}"

	@property
	def group(self) -> str:
		return self.__group

	@property
	def bd(self) -> datetime:
		return self.__bd

	@group.setter
	def group(self, group: str) -> None:
		self.group = group

	@staticmethod
	def from_json(uid: str, data: dict) -> "Student":
		return Student(
			data["first_name"],
			data["second_name"],
			data["last_name"],
			data["group"],
			datetime.fromisoformat(data["bd"]),
			uid
		)

	def to_json(self) -> dict:
		return {
			"first_name": self.__first_name,
			"second_name": self.__second_name,
			"last_name": self.__last_name,
			"group": str(self.group),
			"bd": datetime.isoformat(self.bd),
		}
