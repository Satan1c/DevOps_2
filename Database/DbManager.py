import os
from typing import List
from uuid import UUID

from Database.GradesManager import GradesManager
from Database.GroupsManager import GroupsManager
from Database.StudentData import StudentData
from Database.StudentsManager import StudentsManager
from Database.WantedGradesManager import WantedGradesManager
from Database.abc.DataManagerABC import DataManagerABC


class DbManager:
	def __init__(self, path: str):
		self.path = path
		self.groups_manager: GroupsManager = GroupsManager()
		self.students_manager: StudentsManager = StudentsManager(path)
		self.grades_manager: GradesManager = GradesManager(path)
		self.wanted_grades_manager: WantedGradesManager = WantedGradesManager(path)

		self.__managers: List[DataManagerABC] = [
			self.students_manager,
			self.grades_manager,
			self.wanted_grades_manager
		]

	def load(self) -> None:
		for root, dirs, files in os.walk(self.path):
			for group in dirs:
				group_id = group[6:]
				self.groups_manager.add_group(group_id)
				for r, d, f in os.walk(os.path.join(root, group)):
					for file in f:
						for manager in self.__managers:
							if manager.is_valid(file):
								name = '-'.join(file.split('-')[1:])
								uid = name[:-5]
								manager.load(uid, os.path.join(r, file))

	def get_student_data(self, uid: str) -> StudentData:
		return StudentData(
			self.students_manager.get_student(uid),
			self.grades_manager.get_grade(uid),
			self.wanted_grades_manager.get_wanted_grade(uid),
		)

	def save(self):
		for group, students in self.groups_manager.groups.items():
			group_path = os.path.join(self.path, f"Group-{group}")
			if not os.path.exists(group_path):
				os.makedirs(group_path)
			for student in students:
				for manager in self.__managers:
					manager.save_json(group, student)

