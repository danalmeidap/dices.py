from enum import Enum


class ElevenToNineteen(Enum):
	Eleven = 1
	Twelve = 2
	Thirteen = 3
	Fourteen = 4
	Fifteen = 5
	Sixteen = 6
	Seventeen = 7
	Eighteen = 8
	Nineteen = 9

	def __str__(self) -> str:
		return self.name
