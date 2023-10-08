# Define una variable de cada tipo de primitivo
entero = 42
flotante = 3.14
cadena = "Hola, soy una cadena"
booleano = True

# Concatena las variables aplicando la conversión correcta
resultado_concatenacion = str(entero) + str(flotante) + cadena + str(booleano)

# Límite de los enteros y flotantes en Python
limite_enteros = 2**31 - 1  # El límite de enteros en Python es 2^31 - 1
limite_flotantes = 1.8e308  # Límite de flotantes positivos en Python

# Fórmula para la suma de los primeros n números pares
def suma_pares(n):
    return n * (n + 1)

# Tomamos n como la variable de tipo entero
n = entero
resultado_suma_pares = suma_pares(n)

# Imprimir los resultados
print("Resultado de la concatenación:", resultado_concatenacion)
print("Límite de enteros en Python:", limite_enteros)
print("Límite de flotantes en Python:", limite_flotantes)
print(f"Suma de los primeros {n} números pares:", resultado_suma_pares)
