from cliente import menu_cliente
from bibliotecario import menu_bibliotecario
from biblioteca import Biblioteca

def menu_principal():
    biblioteca = Biblioteca()

    while True:
        try:
            opc = int(input("1 - Menu do Bibliotecário\n"
                            "2 - Menu do Cliente\n"
                            "3 - Sair\n"
                            "Digite a opção que deseja: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opc == 1:
            menu_bibliotecario(biblioteca)
        elif opc == 2:
            menu_cliente(biblioteca)
        elif opc == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção não implementada ou inválida.")

if __name__ == "__main__":
    menu_principal()
