from enum import Enum


class DiaDaSemana(Enum):
    Segunda_Feira = 0
    Terca_Feira = 1
    Quarta_Feira = 2
    Quinta_Feira = 3
    Sexta_Feira = 4
    Sabado = 5
    Domingo = 6

    def __str__(self):
        return self.name
