# Este programa dibuja poligonos estrellados según la definición de estos que
# figura en la wikipedia y no estrellas.
# Los poligonos trellados se pueden dibujar de un solo trazo sin levantar el
# el lapiz. Esto significa que con un solo trazo se pueden visitar todos los
# vértices del poligono reglar sin dejar ninguno sin visitar.

####
# F U N C I O N E S
####


####
# I M P O R T S
####

# Import turtle: se usa para crear dibujos sencillos, en una
# ventana distinta a la ventana de IDLE.
import turtle 
    turtle.pencolor("pink")
    turtle.shape("triangle")
    turtle.fillcolor("yellow")
    turtle.color("pink")
    turtle.begin_fill()

    # Dibujar una estrella regular dado el numero de puntas
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

    def dibujar_poligono_estrellado():
       

####
# I N I C I O   P R O G R A M A
####

# Devolvemos la funcion con el parametro a elegir
dibujar_poligono_estrellado(5)





