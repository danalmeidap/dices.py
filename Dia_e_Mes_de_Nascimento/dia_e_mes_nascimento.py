from operacoes import formata_data


def main() -> None:
    data_aniversario: str = str(input('Por favor, digite seu aniversário(dd/mm/aaaa): '))
    print(formata_data(data_aniversario))


if __name__ == "__main__":
    main()
