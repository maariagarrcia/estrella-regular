# Este programa dibuja poligonos estrellados según la definición de estos que
# figura en la wikipedia y no estrellas.
# Los poligonos trellados se pueden dibujar de un solo trazo sin levantar el
# el lapiz. Esto significa que con un solo trazo se pueden visitar todos los
# vértices del poligono reglar sin dejar ninguno sin visitar.




####
# I M P O R T S
####

# Import turtle: se usa para crear dibujos sencillos, en una
# ventana distinta a la ventana de IDLE.
import turtle 
   
####
# F U N C I O N E S
####

def mcd(x,y):
    # Funcion para calcular el maximo comun divisor de dos 
    # numeros enteros por el algoritmo de euclides. 
    # Funciun necesaria para calcular el angulo de rotacion 
    while (y != 0):
        x, y = y, x % y
    return x
   
    
def calcular_angulo(puntas):
    # Bucle el angulo de rotacion
    for a in range(puntas// 2, 1, -1):
        if mcd(puntas, a) == 1:
            return 360.0 / puntas * a

    return  # Esto devuele nulo ya que no se especifica un      valor a devolver

def dibujar_poligono_estrellado(puntas, lado=150):
    # Dibujar una poligono estrellado regular (con todos los angulo iguales)
    # # dado el numero de puntas de dicho polígno

    # Bucle para buscar el angulo de rotacion
    angle = calcular_angulo(puntas)

    # Mínimo  una estrella tiene que tener 4 puntas
    if not angle:
        print("No se puede dibujar un poligono estrellado de " +
              str(puntas) + " vértices")
        print("Pruebe con un número de vertices distinto y siempre mayor que 4...")
        return

    # Especifica el color del trazo del dibujo
    turtle.pencolor("pink")

    # Cambia la forma del "cursor de dibujo" a un triangulo
    turtle.shape("triangle")

    # Especifica el color del "cursor de dibujo"
    turtle.color("pink")

    # Indica que queremos que la figura que vamos a dibujar se rellene en color amarillo
    turtle.begin_fill()

    # Bucle que dibujar la figura arista a arista
    for _ in range(puntas):
        # Dibujamos una de las aristas cuya longitud es "lado" avanzando hacia donde
        # apunta la tortuga (cursor de dibujo)
        turtle.forward(lado)

        # Rotamos el cursor de dibujo un angulo que depende del número de puntas
        # y que hemos calculado previamente.
        turtle.left(angle)

    # Indicamos que ya hemos finalizado el trazado de la figura que empezamos
    # con begin_fill() y que ya se puede rellenar
    turtle.fillcolor("yellow")
    turtle.end_fill()
    return   

####
# I N I C I O   P R O G R A M A
####

# Devolvemos la funcion con el parametro a elegir
dibujar_poligono_estrellado(6)





