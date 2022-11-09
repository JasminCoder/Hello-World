# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo" )


# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print("Hola,", name )	# con una coma
print("Hola, "+name )	# con un +



# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print("Hola", name )	# con una coma
#print("Hola"+name)	    # con una +	-- este debería arrojar un error!

#BONUS NINJA: descubre cómo resolver el error de arriba, sin cambiar el signo + a una coma
print("Hola "+ str(name))



# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer "+str(fave_food1)+" y "+str(fave_food2))    # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}")              # con una cadena f



#Almacena dos de tus comidas favoritas en variables y luego úsalas para imprimir la cadena “Amo comer {{comida_uno}} y {{comida_dos}}.” 
#con el método format (#4a)

comida_uno = "pastel"
comida_dos = "chocolate"
print("Amo comer "+str(comida_uno)+" y "+str(comida_dos))


#Almacena dos de tus comidas favoritas en variables y luego úsalas para imprimir la cadena “Amo comer {{comida_uno}} y {{comida_dos}}.” 
#con cadenas “f” (#4b)

print(f"Amo comer {comida_uno} y {comida_dos}")



#BONUS NINJA: Toma unos minutos para jugar con otros métodos de cadena ¡para saber qué hay allá afuera!

#operador +
nombre = "Juana "
apellido = "De Arco"
nombre_completo = nombre + apellido
print(nombre_completo)



#multiplicar: crear varias copias de una cadena
var1 = "Hola " * 3
var2 = "Mundo"
print(var1 + var2)


#cortar: cortar partes del principio o final de una cadena
mensaje8 = "Hola mundo"
mensaje8a = mensaje8[1:8]
print(mensaje8a)


#minusculas: convertir una cadena a caracteres en minuscula / de minusculas a mayusculas, cambiar .lower() por .upper()
x = "HOLA MUNDO"
xa = x.lower()
print(xa)