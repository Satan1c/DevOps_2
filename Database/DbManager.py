import json
import os
from typing import Dict
from uuid import UUID

from Database.StudentData import StudentData
from Models.Grade import Grade
from Models.Student import Student
from Models.WantedGrades import WantedGrade


class DbManager:
	def __init__(self, path: str):
		self.path = path
		self.groups: Dict[UUID, Dict[UUID, StudentData]] = {}

	def load(self):
		for root, dirs, files in os.walk(self.path):
			for group in dirs:
				group_id = UUID(group[6:])
				self.groups[group_id] = {}
				for r, d, f in os.walk(os.path.join(root, group)):
					for file in f:
						name = '-'.join(file.split('-')[1:])
						uid = UUID(name[:-5])
						if uid not in self.groups[group_id]:
							self.groups[group_id][uid] = StudentData()

						if file.startswith("Student-"):
							self.groups[group_id][uid].student = Student.from_json(uid, json.load(open(os.path.join(r, file))))
						elif file.startswith("Grades-"):
							self.groups[group_id][uid].grades = Grade.from_json(json.load(open(os.path.join(r, file))))
						elif file.startswith("WantedGrades-"):
							self.groups[group_id][uid].wanted_grades = WantedGrade.from_json(json.load(open(os.path.join(r, file))))

	def get_student(self, uid: UUID) -> StudentData | None:
		for group_id, students in self.groups.items():
			if uid in students:
				return students[uid]
		return None

	def get_group_student(self, group: UUID, student: UUID) -> StudentData | None:
		if group not in self.groups:
			return None
		if student in self.groups[group]:
			return self.groups[group][student]
		return None

	def get_group_students(self, group: UUID) -> list[StudentData]:
		if group not in self.groups:
			return []
		return list(self.groups[group].values())

	def save_student(self, student: Student) -> None:
		if student.group not in self.groups:
			self.groups[student.group] = {}
		if student.uid not in self.groups[student.group]:
			self.groups[student.group][student.uid] = StudentData()
		self.groups[student.group][student.uid].student = student
		group_path = os.path.join(self.path, f"Group-{student.group}")
		if not os.path.exists(group_path):
			os.makedirs(group_path)
		student_path = os.path.join(group_path, f"Student-{student.uid}.json")
		with open(student_path, "w") as f:
			json.dump(student.to_json(), f, indent=4, ensure_ascii=False)

	def delete_student(self, uid: UUID) -> None:
		for group_id, students in self.groups.items():
			if uid in students:
				self.groups[uid].pop(uid, None)
		for root, dirs, files in os.walk(self.path):
			for file in files:
				if file == f"Student-{uid}.json":
					os.remove(os.path.join(root, file))

	def delete_group_student(self, group: UUID, student: UUID) -> None:
		if group in self.groups:
			self.groups[group].pop(student, None)
		group_path = os.path.join(self.path, f"Group-{group}")
		if not os.path.exists(group_path):
			return
		student_path = os.path.join(group_path, f"Student-{student}.json")
		if not os.path.exists(student_path):
			return
		os.remove(student_path)

	def delete_group(self, group: UUID) -> None:
		if group in self.groups:
			self.groups.pop(group, None)
		group_path = os.path.join(self.path, f"Group-{group}")
		if not os.path.exists(group_path):
			return
		os.rmdir(group_path)

	def save_grades(self, uid: UUID, grades: Grade) -> None:
		if self.save_grades_data(uid, "Grades-", grades.to_json()):
			student_data = self.get_student(uid)
			student_data.grades = grades

	def save_wanted_grades(self, uid: UUID, wanted_grades: WantedGrade) -> None:
		if self.save_grades_data(uid, "WantedGrades-", wanted_grades.to_json()):
			student_data = self.get_student(uid)
			student_data.wanted_grades = wanted_grades

	def save_grades_data(self, uid: UUID, prefix: str, data: dict) -> bool:
		student_data = self.get_student(uid)
		if not student_data:
			return False
		group_path = os.path.join(self.path, f"Group-{student_data.student.group}")
		if not os.path.exists(group_path):
			os.makedirs(group_path)
		wanted_grades_path = os.path.join(group_path, f"{prefix}{uid}.json")
		with open(wanted_grades_path, "w") as f:
			json.dump(data, f, indent=4, ensure_ascii=False)
		return True

	def get_grades(self, uid: UUID) -> Grade:
		student_data = self.get_student(uid)
		if not student_data or not student_data.grades:
			return Grade({})
		return student_data.grades

	def get_wanted_grades(self, uid: UUID) -> WantedGrade:
		student_data = self.get_student(uid)
		if not student_data or not student_data.wanted_grades:
			return WantedGrade({})
		return student_data.wanted_grades