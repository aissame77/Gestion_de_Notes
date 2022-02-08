import csv              

def read_profs():
    path='/Users/AISSAME/Mega/GINF2/XML_Project/Q1/CSV_FILES/profs.csv'
    file = open(path)
    csv_file = csv.reader(file)   
    filiere_prec = ''
    #dans cette variable on va stocker la colonne qui continet la filiere dont on va distinguee les etudiants
    index = 0
    dept = []
    data = [[]]
    for row in csv_file: 
        if row[3] != filiere_prec:
            filiere_prec = row[3]
            dept.append(filiere_prec)
            index += 1
            data.append([])
        data[index].append(row)
    file.close()
    return [data,dept]
#definition de format xml des donnees
def prof_xml(row):
    return """<prof>
    \t<cin>%s</cin>
    \t<firstname>%s</firstname>
    \t<lastname>%s</lastname>
    \t<dept_attachement>%s</dept_attachement>
    \t<phone>%s</phone>
    \t<email>%s</email>
\t</prof>\n""" % (row[0], row[1], row[2], row[3], row[4], row[5])
#generation de prof en format xml
def generate_prof_xml():
    index = 0
    data = read_profs()
    prof_data = data[0]
    depts = data[1]

    for dept in prof_data:
        if dept != []:
            xml_file = open('profs_' + depts[index] + '.xml', 'w')
            xml_file.write('')
            xml_file.close()
            xml_file = open('profs_' + depts[index] + '.xml', 'a')
            xml_file.write('<prof_' + depts[index] + '>\n')
            for prof in dept:
                if prof != []:
                    xml_file.write('\t')
                    xml_file.write(prof_xml(prof))
            xml_file.write('\n</prof_' + depts[index] + '>')
            index+=1
            xml_file.close()

generate_prof_xml()



