import csv              
#on va definire 3 fonctions une pour creeer la liste qui va contenire les datas et une pour definir le format xml
def read_students():
    #On genere la liste des students de GINF2
    #on pourra faire la meme chose pour les autres filiere dans le dir 'CSV_FILES'
    path='/Users/AISSAME/Mega/GINF2/XML_Project/Q1/CSV_FILES/lesGINF2.csv'
    file = open(path)
    csv_f = csv.reader(file)   
    previousFil = ''
        #dans cette variable on va stocker la colonne qui continet la filiere dont on va distinguee les etudiants

    index = 0
    filieres = []
    data = [[]]
    for row in csv_f: 
        if row[4] != previousFil:
            previousFil = row[4]
            filieres.append(previousFil)
            index += 1
            data.append([])
        data[index].append(row)
    file.close()
    return [data,filieres]

def student_xml(row):
    return """<student>
    \t<cne>%s</cne>
    \t<dateofbirth>%s</dateofbirth>
    \t<firstname>%s</firstname>
    \t<lastname>%s</lastname>
    \t<filiere>%s</filiere>
    \t<phone>%s</phone>
    \t<email>%s</email>
\t</student>\n""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
#la 3eme fct est pour generer finalement le fichier xml
def generate_students_xml():
    index = 0
    data = read_students()
    student_data = data[0]
    filieres = data[1]

    for fil in student_data:
        if fil != []:
            xml_file = open('students_' + filieres[index] + '.xml', 'w')
            xml_file.write('')
            xml_file.close()
            xml_file = open('students_' + filieres[index] + '.xml', 'a')
            xml_file.write('<stud_' + filieres[index] + '>\n')
            for student in fil:
                if student != []:
                    xml_file.write('\t')
                    xml_file.write(student_xml(student))
            xml_file.write('\n</stud_' + filieres[index] + '>')
            xml_file.close()
            index+=1
            

generate_students_xml()