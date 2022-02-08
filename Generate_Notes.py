import xml.etree.ElementTree as ET
import re
import random
from os import walk

def availablemods():
    _, _, filenames = next(walk('./'))

    def onlymodules(file):
        if 'students' in file:
            if 'xml' in file:
                return True
            else:
                return False
        else:
            return False

    moduleFilter = filter(onlymodules,filenames)
    modules = []

    for module in moduleFilter:
        modules.append(module.split('_')[1].split('.')[0])
    return modules

def read_students(level):
    students = ET.parse('students_' + level.upper() + '.xml').getroot()
    cne = ''
    filiere = ''
    studentData = []
    codes = []
    pattern = re.compile("elementname")
    for student in students:
        cne = student.findall('cne')[0].text
        filiere = student.findall('filiere')[0].text
        modFil = ''
        if 'AP' not in filiere:
            modFil = re.sub('\d$', '', filiere)
        else:
            modFil = filiere
        modules = ET.parse('modules_' + modFil + '.xml').getroot()
        markstudent = []
        for module in modules:
            avg = 0
            els = 0
            mark = {}
            for element in module:
                if element.tag == 'name':
                    mark['module'] = element.text
                if pattern.match(element.tag):
                    mark[element.text] = round(random.uniform(0, 20), 2)
                    avg+= mark[element.text]
                    els+=1
            mark['notemod'] = round(avg/els, 2)
            markstudent.append(mark)
        studentData.append(markstudent)
        codes.append(cne)
    return [studentData,codes,filiere]

def Generate_marks():
    availablemodules = availablemods()
    if len(availablemodules) != 0:
        level = input('Enytrer la filiere pour generer les notes:\n- Select from: ' + str(availablemodules).split('[')[1].split(']')[0] + '\n\t>> ')
        data = read_students(level)
        studentData = data[0]
        codes = data[1]
        filiere = data[2]
        note = "<note>\n"
        for i in range (0,len(studentData),1):
            note += "\t<student>\n"
            note += "\t\t<cne>" + codes[i] + "</cne>\n"
            for module in studentData[i]:
                for key in module:
                    if key == "module":
                        note += "\t\t<module>\n\t\t\t<name>" + module['module'] + "</name>\n"
                    elif key == "notemod":
                        note += "\t\t\t<note>" + str(module['notemod']) + "</note>\n" + "\t\t</module>\n"
                    else:
                        note += "\t\t\t<" + key.replace(" ", "_") + ">" + str(module[key]) + "</" + key.replace(" ", "_") + ">\n"
            note +="\t</student>\n"
        note += "</note>\n"

        xml_file = open('notes_' + filiere + '.xml', 'w')
        xml_file.write(note)
    else:
        print(' Please try running generatemod.py')

Generate_marks()