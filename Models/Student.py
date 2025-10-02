import uuid
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


class Student:
	def __init__(self, first_name: str, second_name: str, last_name: str, group: UUID, bd: datetime, uid: UUID = None):
		if uid is None:
			uid = uuid.uuid4()
		self.__uid = uid
		self.__first_name = first_name.title()
		self.__second_name = second_name.title()
		self.__last_name = last_name.title()
		self.__group = group
		self.__bd = bd

	def __str__(self) -> str:
		return str(self.to_json())

	@property
	def uid(self) -> UUID:
		return self.__uid

	@property
	def full_name(self) -> str:
		return f"{self.__last_name} {self.__first_name} {self.__second_name}"

	@property
	def group(self) -> UUID:
		return self.__group

	@property
	def bd(self) -> datetime:
		return self.__bd

	@group.setter
	def group(self, group: UUID) -> None:
		self.group = group

	@staticmethod
	def from_json(uid: UUID, data: dict) -> "Student":
		return Student(
			str(data["first_name"]),
			str(data["second_name"]),
			str(data["last_name"]),
			UUID(data["group"]),
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
