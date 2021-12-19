####
# I M P O R T S
####



####
# F U N C I O N E S
####
def dibujar_estrella(puntas,lado=150):
    # Import turtle: se usa para crear dibujos sencillos, en una
    # ventana distinta a la ventana  de IDLE.
    import turtle 
    
    turtle.pencolor("pink")
    turtle.shape("triangle")
    turtle.fillcolor("yellow")
    turtle.color("pink")
    turtle.begin_fill()
    
    # Dibujar una estrella regular dado el numero de puntas
    def mcd(x,y):
        # Funciun para calcular el maximo comun divisor de dos 
        # numeros enteros por el algoritmo de euclides. 
        # Funciun necesaria para calcular el angulo de rotacion 
        while (y != 0):
            x, y = y, x % y
        return x
   
    # Miinimo  una estrella tiene que tener 4 puntas
    if puntas <= 4:
        print("La estrella tiene que tener 4 puntas minimo. Inserte una mayor")
        return 

    for a in range(puntas // 2, 1, -1):
        # Bucle para buscar el a ngulo de rotacion
        if mcd(puntas, a) == 1:
            angle = 360.0 / puntas * a
            break

    
    # Dibujar los  traz.
    for _ in range(puntas):
        # Dibujamos el lado
        turtle.forward(lado)
        # Rotamos el cursor
        turtle.left(angle)
    turtle.end_fill()
    return
    
dibujar_estrella(10)


