estado_civil = "as"

match estado_civil:
        case "C":
            print("Casado")
        case "S":
            print("Solteiro")
        case "V":
            print("Viúvo")
        case "D":
            print("Divorciado")
        case _:
            print("Estado Civil Indefinido")