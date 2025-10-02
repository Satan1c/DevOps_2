from Models.abc.GradeABC import GradeABC


class Grade(GradeABC):
	def __str__(self) -> str:
		return str(self.to_json())

	@staticmethod
	def from_json(data: dict) -> "Grade":
		return Grade(data)

	def avg_grade(self) -> float:
		return super().avg_grade()

	def to_json(self) -> dict:
		return super().to_json()
