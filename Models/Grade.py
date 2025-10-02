from Models.abc.GradeABC import GradeABC


class Grade(GradeABC):
	def __str__(self) -> str:
		return str(self.to_json())

	@classmethod
	def from_json(cls, json_data: dict) -> "Grade":
		return Grade(json_data)

	def avg_grade(self) -> float:
		return super().avg_grade()

	def to_json(self) -> dict:
		return super().to_json()
