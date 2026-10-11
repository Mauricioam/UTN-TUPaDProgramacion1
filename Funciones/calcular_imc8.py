
def calcular_imc(weigth,height):
        if(weigth > 0 and height > 0):
            result = weigth / (height*height)
            return (f"El IMC es igual a {result:.2f}")
        else:
            return ("Error: el valor no puede ser 0")


