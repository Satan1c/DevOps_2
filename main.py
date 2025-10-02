import os
import uuid
from datetime import datetime
from typing import Dict

from Database.DbManager import DbManager
from Models.Grade import Grade
from Models.Student import Student
from Models.WantedGrades import WantedGrade

storage = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Storage")
if not os.path.exists(storage):
	os.mkdir(storage)

groups: Dict[str, uuid.UUID] = {"ПДМ-51": uuid.uuid4()}

db = DbManager(storage)
db.load()

group_id: str = str(groups["ПДМ-51"])
student_id: str = str(uuid.uuid4())

db.groups_manager.add_student(group_id, student_id)
db.students_manager.add_student(
	Student(
		"Олександр",
		"Геннадійович",
		"Федотов",
		group_id,
		datetime.fromisoformat("2003-09-12"),
		student_id
	)
)

db.grades_manager.add_grade(
	student_id,
	Grade(
		{
			"Математика": 3,
			"Фізика": 3,
			"Программування": 5
		},
	)
)
db.wanted_grades_manager.add_wanted_grade(
	student_id,
	WantedGrade(
		{
			"Математика": 4,
			"Фізика": 4,
			"Программування": 5
		},
	)
)

db.save()
