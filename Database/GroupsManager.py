from typing import Dict, List
from uuid import UUID


class GroupsManager:
	def __init__(self):
		self.groups: Dict[str, List[str]] = {}

	def add_group(self, group_id: str) -> None:
		if group_id not in self.groups:
			self.groups[group_id] = []

	def add_student(self, group_id: str, student_id: str) -> None:
		self.add_group(group_id)
		self.groups[group_id].append(student_id)
