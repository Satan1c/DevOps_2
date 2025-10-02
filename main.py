import os
import uuid
from datetime import datetime
from typing import Dict

from Database.DbManager import DbManager
from Models.Grade import Grade
from Models.Student import Student
from Models.WantedGrades import WantedGrade

storage = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Storage")

groups: Dict[str, uuid.UUID] = {"ПДМ-51": uuid.uuid4()}

db = DbManager(storage)
db.load()

group_id: uuid.UUID = groups["ПДМ-51"]
student_id: uuid.UUID = uuid.uuid4()
db.save_student(
	Student(
		"Олександр", "Геннадійович", "Федотов",
		group_id,
		datetime.fromisoformat("2003-03-12"),
		student_id
	)
)

db.save_grades(student_id, Grade({
	"Математика": 65.0,
	"Фізика": 60.0,
	"Програмування": 100.0
}))
db.save_wanted_grades(student_id, WantedGrade({
	"Математика": 75.0,
	"Фізика": 65.0,
	"Програмування": 100.0
}))

student = db.get_student(student_id)
print(student.student)
print(student.student.full_name)
print(student.grades)
print(student.grades.avg_grade())
print(student.wanted_grades)
print(student.wanted_grades.avg_grade())
