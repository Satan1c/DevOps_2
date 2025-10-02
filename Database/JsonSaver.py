import json

from Database.abc.DataSaverABC import DataSaverABC


class JsonSaver(DataSaverABC):
	data: dict = {}

	def add(self, data: dict) -> None:
		self.data.update(data)

	def clear(self) -> None:
		self.data.clear()

	def save(self, path: str) -> None:
		with open(path + ".json", 'w') as f:
			json.dump(self.data, f, indent=4, ensure_ascii=False)
