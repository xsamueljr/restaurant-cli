from auth import is_password_correct
from db_handler import DBHandler, PlateNotFound


def main() -> None:
    db_handler = DBHandler()
    for i in [
        "1. Crear plato",
        "2. Listar platos",
        "3. Actualizar plato",
        "4. Eliminar plato",
        "5. Salir"
    ]:
        print(i)

    print("Elige")
    while True:
        try:
            option = int(input("> "))
        except ValueError:
            print("No es un número")
            continue

        if option not in range(1, 6):
            print("Opción inválida")
            continue

        if option == 5:
            return

        if option in {1, 3, 4}:
            password = input("Contraseña: ")
            if not is_password_correct(password):
                print("Contraseña incorrecta")
                continue

        if option == 1:
            name = input("Nombre: ")
            print("Creando plato...")
            db_handler.create_plate(name)
            print("Plato creado")

        elif option == 2:
            print("Listando platos...")

            plates = db_handler.list_plates()
            if not plates:
                print("No hay platos")
                continue

            for plate in db_handler.list_plates():
                print(plate)

        elif option == 3:
            old_name = input("Nombre actual: ")
            new_name = input("Nuevo nombre: ")
            print("Actualizando plato...")
            try:
                db_handler.update_plate(old_name, new_name)
            except PlateNotFound:
                print("Plato no encontrado")
                continue
            print("Plato actualizado")

        elif option == 4:
            name = input("Nombre: ")
            print("Eliminando plato...")
            try:
                db_handler.delete_plate(name)
            except PlateNotFound:
                print("Plato no encontrado")
                continue
            print("Plato eliminado")


if __name__ == '__main__':
    main()
