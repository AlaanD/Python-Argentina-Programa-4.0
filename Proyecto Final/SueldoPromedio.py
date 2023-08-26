"""
El empleado llamado Juan cobró 300 dólares por mes desde enero a junio,
500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre.
En base al escenario propuesto, se le solicita a los estudiantes que creen un
pequeño programa que calcule el sueldo promedio del empleado Juan.
Además, se debe indicar sí Juan se encuentra cobrando un sueldo bajo,
normal o mejor de lo normal, considerando las siguientes pautas:

a. Sueldo bajo: por debajo de 300 dólares.
b. Sueldo normal:  entre 300 a 900.
c. Sueldo mejor de lo normal: más de 900 dólares.

Tip: se debe utilizar estructuras condicionales.
"""

class SueldoPromedio:
    
    def calcularPromedio(sueldo_pri_6m, sueldo_sig_4m, sueldo_ult_2m):
        total = sueldo_pri_6m + sueldo_sig_4m + sueldo_ult_2m
        resultado = total / 12
        return round(resultado, 2)

    def calcularRangoSalario(promedio):
        if(promedio < 300):
            return "bajo"
        elif(promedio >= 300 and promedio <= 900):
            return "normal"
        return "mejor de lo normal"

    sueldo_pri_6m = 300 * 6
    sueldo_sig_4m = 500 * 4
    sueldo_ult_2m = 700 * 2

    promedio = calcularPromedio(sueldo_pri_6m, sueldo_sig_4m, sueldo_ult_2m)
    rango = calcularRangoSalario(promedio)

    print("El salario promedio de Juan es " + str(promedio))
    print("Juan se encuentra cobrando un salario " + rango)