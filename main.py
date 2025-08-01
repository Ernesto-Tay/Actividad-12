estudiantes = {}
while True:
    print("\n\nManejo de estudiantes")
    while True:
        est_cant = input("¿Cuántos estudiantes quiere ingresar?: ")
        if est_cant.isdigit():
            est_cant = int(est_cant)
            if est_cant <=0:
                print("Ingrese una cantidad positiva")
            else:
                break
        else:
            print("Ingrese un número entero")

    for i in range(est_cant):
        while True:
            try:
                print(f"----- ESTUDIANTE {i+1} -----")
                nombre = input("Ingrese el nombre del estudiante: ")
                nota_cant = int(input("Ingrese la cantidad de notas a ingresar: "))
                if nota_cant <=0:
                    print("La cantidad de notas debe ser positiva y mayor a 0")

            except ValueError:
                print("Ingrese un número entero en la cantidad de notas")
            except Exception as e:
                print("Error inesperado: ",e)

        notas = []
        total = 0
        promedio = 0
        for i in range(nota_cant):
            while True:
                try:
                    nota = int(input(f"Ingrese la nota {i+1}: "))
                    if nota <=0 or nota>100:
                        print("La nota debe estar entre 0 y 100")
                    else:
                        total += nota
                        break
                except ValueError:
                    print("Ingrese números enteros")
                except Exception as e:
                    print("Error inesperado: ",e)





