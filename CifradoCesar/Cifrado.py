texto = "Esta cadena esta sin codificar"
desplazar = 3
convertir = ""
cadena1 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZABC"
cadena2 = "abcdefghijklmnñopqrstuvwxyzabc"
inicial = "p"
for x in texto:
    if x in cadena1:

        convertir += cadena1[cadena1.index(x) + desplazar % (len(cadena1))]

    elif x in cadena2:

        convertir += cadena2[cadena2.index(x) + desplazar % (len(cadena2))]

    else:

        convertir += x

print(inicial + convertir.replace(" ", ""))


