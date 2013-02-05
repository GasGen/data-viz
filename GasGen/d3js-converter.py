#OpenWorm CSV to JSON
#author: Gaston Gentile

import gspread, csv, json, getpass, os

'''Para inicio de sesion automatico borrar variables user & pwd
y escibrilos entre comillas en la variable gc.
To automatic sign in, remove user & pwd variables, and write
them between quotes in gc variable respectively'''

os.system('clear')

#FIRST STEP
def start():
    print 'Convert CSV to JSON'
    user = raw_input("Gmail user: ")
    pwd = getpass.getpass("Gmail Password: ")
    gc = gspread.login(user,pwd)
    docurl = raw_input("Spreadsheet url: ")
    sh = gc.open_by_url(docurl)#apertura del documento/Open Doc.
    worksheet = sh.worksheet("Single Neurons")#Seleccion de la hoja/Sheet selection.

    #allsheet = worksheet.get_all_values()Toma todos los valores de la hoja/Take all the values of the sheet.

    #colb, cold, colf toma los valores de las columnas (b,d,f)/ Take values of columns (b,d,f)
    colb = worksheet.col_values(2)
    cold = worksheet.col_values(4)
    colf = worksheet.col_values(6)

    #parse = str(allsheet)Convierte los datos a string/Parse data to string.

    #Convierte valores de columnas en strings/Parse columns values in to string.
    parseb = str(colb)
    parsed = str(cold)
    parsef = str(colf)

    #Guarda el CSV separado por columnas/Save the CSV separate by columns
    colbwrite = open('colb.csv', 'w')
    coldwrite = open('cold.csv', 'w')
    colfwrite = open('colf.csv', 'w')
    escribirb = colbwrite.write(parseb)
    colbwrite.close()
    escribird = coldwrite.write(parsed)
    coldwrite.close()
    escribirf = colfwrite.write(parsef)
    colfwrite.close()

#SECOND STEP - EXPERIMENTAL
def convert():
    #Abre columna b, elimina comas y espacios./Open column b and delet commas and spaces.

    coma = ","

    fb = open('colb.csv','r')
    leer = fb.read()

    eliminado = leer.replace(coma, "")
    espacios = eliminado.replace(' ','')

    fb.close()
    fb = open('colb.csv','w')
    fb.write(espacios)
    fb.close()

    #Abre columna d, elimina comas y espacios./Open column b and delet commas and spaces.

    coma = ","

    fd = open('cold.csv','r')
    leer = fd.read()

    eliminado = leer.replace(coma, "")
    espacios = eliminado.replace(' ','')

    fd.close()
    fd = open('cold.csv','w')
    fd.write(espacios)
    fd.close()

    #Abre columna f, elimina comas y espacios./Open column b and delet commas and spaces.   

    coma = ","

    ff = open('colf.csv','r')
    leer = ff.read()

    eliminado = leer.replace(coma, "")
    espacios = eliminado.replace(' ','')

    ff.close()
    ff = open('colf.csv','w')
    ff.write(espacios)
    ff.close()


    #Index para tomar valores de las celdas / Index for take values of cells
    loop = 1
    celd = 3 #El valor es tres, porque es el primer dato que aparece/The value is third because is the first data.

    head = "{\n""\"name\":\"NeuroNetwork\",\n"
    foot = "\n}\n]"*302 #302 porque es al cantidad de childrens / 302 because are the numbers of childrens.


    fb = open('colb.csv','r')

    fd = open('cold.csv', 'r')

    ff = open('colf.csv', 'r')

    celegans = open('celegans.json','w')

    celegans.write(head)

    #Las vueltas del bucle es igual a la cantidad de celulas / The laps of loop are equal to numbers of cells.
    while loop <= 302:

        #Los datos se encuentran en posiciones impares, con esta porcion de codigo, utilizamos solo esas posiciones. / The data is only in odd positions, with this portion of code, use only them.
        if celd%2 == 0:
            celd = celd + 1

        #Columna b / Column b
        for line in fb.readlines():
            if "\'" in line:
                cellb = line.split('\'')[celd]
        #Columna d / Column d   
        for line in fd.readlines():
            if "\'" in line:
                celld= line.split('\'')[celd]
        #Columna f / Column f
        for line in ff.readlines():
            if "\'" in line:
                cellf = line.split('\'')[celd]

        chld = "\"children\": [\n{\n\"name\":\""+cellb+"\",\n\"Neurotransmitter\":\""+celld+"\",\n\"Receptor\":\""+cellf+"\",\n\"size\":\"1400\",\n"

        #Escribe el children / Write the children
        celegans.write(chld)
        #Cuenta las vueltas del bucle / Loop count.
        loop = loop + 1
        #Celda a utilizar en la proxima vuelta / Celd to use in the next lap.
        celd = celd + 1 

    #Escribe el pie del archivo json/ Write the foot of the json file
    celegans.write(foot)
    #Cierra el archivo json / Close the json file.
    celegans.close()

    fb.close()

    print "\nWORKS!, celegans.json was generated!\n"

start()
convert()