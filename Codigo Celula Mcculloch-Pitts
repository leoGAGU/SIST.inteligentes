
# Definir la función de la célula McCulloch-Pitts
def mcculloch_pitts(x, w, theta):
    """
    Función que implementa la célula McCulloch-Pitts.

    Args:
    x: Lista o arreglo de valores de entrada.
    w: Lista o arreglo de pesos sinápticos.
    theta: Umbral de activación.

    Returns:
    Un valor binario que indica la salida de la célula.
    """
    # Calcular la suma ponderada de las entradas
    z = sum([x[i]*w[i] for i in range(len(x))])

    # Aplicar la función escalón
    if z >= theta:
        return 1
    else:
        return 0

# Definir las tablas de verdad para las compuertas lógicas AND, OR y NOT
X_and = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_and = [0, 0, 0, 1]

X_or = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_or = [0, 1, 1, 1]

X_not = [[0], [1]]
y_not = [1, 0]

# Entrenar la célula McCulloch-Pitts para las tablas de verdad de las compuertas AND, OR y NOT
w_and = [1, 1]
theta_and = 1.5

w_or = [1, 1]
theta_or = 0.5

w_not = [-1]
theta_not = -0.5

# Probar la célula McCulloch-Pitts con las entradas de las tablas de verdad de las compuertas AND, OR y NOT
print(f"AND: {[mcculloch_pitts(X_and[i], w_and, theta_and) for i in range(len(X_and))]}")
print(f"OR: {[mcculloch_pitts(X_or[i], w_or, theta_or) for i in range(len(X_or))]}")
print(f"NOT: {[mcculloch_pitts(X_not[i], w_not, theta_not) for i in range(len(X_not))]}")
