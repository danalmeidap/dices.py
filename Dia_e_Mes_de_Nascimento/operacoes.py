from models.dia_da_semana import DiaDaSemana
from models.meses import Meses
from datetime import datetime


def formata_data(data: str) -> str:
    try:
        aniversario: datetime = datetime.strptime(data, '%d/%m/%Y')
        dia_semana: DiaDaSemana = DiaDaSemana(aniversario.weekday())
        mes: Meses = Meses(aniversario.month)
    except ValueError:
        return "Por favor, digite a data com o formato (dd/mm/aaaa)"
    return f"Você nasceu em {aniversario.day} de {mes} de {aniversario.year}. Era um(a) {dia_semana}"
