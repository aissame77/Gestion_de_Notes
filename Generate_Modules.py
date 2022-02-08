import csv              
#Generate_Modules
#Modules_AP1
#Eleves_

def read_modules():
    path='/Users/AISSAME/Mega/GINF2/XML_Project/Q1/CSV_FILES/modules.csv'
    file = open(path)
    csv_file = csv.reader(file)   
    filier_prec = ''
    index = 0
    filieres = []
    data = [[]]
    for row in csv_file: 
        if row[len(row) - 1] != filier_prec:
            filier_prec = row[len(row) - 1]
            filieres.append(filier_prec)
            index += 1
            data.append([])
        data[index].append(row)
    file.close()
    return [data,filieres]

def module_xml(row):
    module = "<module>\n\t<name>" + row[0] + "</name>\n"
    for i in range(1,len(row) - 1,1):
        module += "\t<elementname" + str(i) + ">" + row[i] + "</elementname" + str(i) + ">\n"
    module += "\t<dept_attachement>" + row[len(row) - 1] + "</dept_attachement>\n</module>\n"
    return module

def generate_module_xml():
    index = 0
    data = read_modules()
    module_data = data[0]
    filieres = data[1]
    for fil in module_data:
        if fil != []:
            xml_file = open('modules_' + filieres[index] + '.xml', 'w')
            xml_file.write('')
            xml_file.close()
            xml_file = open('modules_' + filieres[index] + '.xml', 'a')
            xml_file.write('<mod_' + filieres[index] + '>\n')
            for module in fil:
                if module != []:
                    xml_file.write('\t')
                    xml_file.write(module_xml(module))

            xml_file.write('\n</mod_' + filieres[index] + '>')
            index+=1
            xml_file.close()

generate_module_xml()