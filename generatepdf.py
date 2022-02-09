from fpdf import FPDF
import xml.etree.ElementTree as ET
from os import walk
import math
import random

def availableFil():
    _, _, filenames = next(walk('./'))

    def onlyFilieres(file):
        if 'students' in file:
            if 'xml' in file:
                return True
            else:
                return False
        else:
            return False

    filiereFilter = filter(onlyFilieres,filenames)
    filieres = []

    for filiere in filiereFilter:
        filieres.append(filiere.split('_')[1].split('.')[0])
    return filieres

def availablemods():
    _, _, filenames = next(walk('./'))

    def onlymodules(file):
        if 'modules' in file:
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

def createStudentCard(cne):
    pdf = FPDF()
    pdf.add_page() 
    availableNote = availableFil()
    for fil in availableNote:
        students = ET.parse('students_' + fil + '.xml').getroot()
        searchRes = students.find('.//student[cne="' + str(cne) + '"].')
        if not searchRes is None:
            for child in searchRes:
                pdf.set_font("Arial", size = 20) 
                pdf.cell(50, 10, txt = child.tag + ': ', ln = 0, align = 'L') 
                pdf.set_font("Arial", size = 14) 
                pdf.cell(100, 10, txt = child.text, ln = 1, align = 'L') 


    pdf.output('carte_' + str(cne) + '.pdf')


def availableNotes():
    _, _, filenames = next(walk('./'))

    def onlyFilieres(file):
        if 'notes' in file:
            if 'xml' in file:
                return True
            else:
                return False
        else:
            return False

    filiereFilter = filter(onlyFilieres,filenames)
    filieres = []

    for filiere in filiereFilter:
        filieres.append(filiere.split('_')[1].split('.')[0])
    return filieres


def createStudentReleve(cne):
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A3')
    pdf.add_page() 
    availableNote = availableNotes()
    for fil in availableNote:
        notes = ET.parse('notes_' + fil + '.xml').getroot()
        searchRes = notes.find('.//student[cne="' + str(cne) + '"].')
        if not searchRes is None:
            for child in searchRes:
                if child.tag == 'cne':
                    pdf.set_font("Arial", size = 20) 
                    pdf.cell(50, 10, txt = 'CNE: ', ln = 0, align = 'L') 
                    pdf.set_font("Arial", size = 14) 
                    pdf.cell(100, 10, txt = child.text, ln = 1, align = 'L')
                    notesEl = []
                    elements = []
                if child.tag == 'module':
                    for el in child:
                        if el.tag == 'name':
                            pdf.set_font("Arial", size = 18) 
                            pdf.cell(50, 15, txt =  'Module: ', ln = 0, align = 'L') 
                            pdf.set_font("Arial", size = 12) 
                            pdf.cell(100, 15, txt = el.text, ln = 1, align = 'L')
                        if el.tag == 'note':
                            for element in elements:
                                pdf.set_font("Arial", size = 14) 
                                if len(element) > 8:
                                    element = element[0:8] + '...'
                                pdf.cell(297/len(elements), 15, txt =  element, ln = 0, align = 'L')  
                            pdf.cell(50, 8, txt =  ' ', ln = 1, align = 'L')
                            for note in notesEl:
                                pdf.set_font("Arial", size = 14)
                                pdf.cell(297/len(elements), 15, txt =  note, ln = 0, align = 'L') 
                            pdf.cell(50, 15, txt =  ' ', ln = 1, align = 'L') 
                            pdf.set_font("Arial", size = 18) 
                            pdf.cell(50, 15, txt =  'Note: ', ln = 0, align = 'L') 
                            pdf.set_font("Arial", size = 14) 
                            pdf.cell(100, 15, txt = el.text, ln = 1, align = 'L')
                            pdf.cell(50, 15, txt =  ' ', ln = 1, align = 'L') 
                            notesEl = []
                            elements = []
                        else:
                            elements.append(el.tag)
                            notesEl.append(el.text)
    pdf.output('releve_' + str(cne) + '.pdf')


def createFilReleve():
    availableNote = availableNotes()
    cne = ''
    notesEl = []
    elements = []
    fil = input('entrez une filiere:\n-les choix sont: ' + str(availableNote).split('[')[1].split(']')[0] + '\n\t>>').upper()
    while True:
        if fil not in availableNote:
            fil = input('entrez une filiere:\n-les choix sont: ' + str(availableNote).split('[')[1].split(']')[0] + '\n\t>>').upper()
            break
        else:
            break

    notes = ET.parse('notes_' + fil + '.xml').getroot()
    searchRes = notes.findall('student')

    for student in searchRes:
        pdf = FPDF(orientation = 'P', unit = 'mm', format='A3')
        pdf.add_page() 
        if not searchRes is None:
            for child in student:
                if child.tag == 'cne':
                    pdf.set_font("Arial", size = 20) 
                    pdf.cell(50, 10, txt = 'CNE: ', ln = 0, align = 'L') 
                    pdf.set_font("Arial", size = 14) 
                    pdf.cell(100, 10, txt = child.text, ln = 1, align = 'L')
                    cne = child.text
                    createStudentReleve(cne)
    
def createAffichage():
    availableNote = availableNotes()
    fil = input('entrez une filiere:\n-les choix sont: ' + str(availableNote).split('[')[1].split(']')[0] + '\n\t>>').upper()
    while True:
        if fil not in availableNote:
            fil = input('entrez une filiere:\n-les choix sont: ' + str(availableNote).split('[')[1].split(']')[0] + '\n\t>>').upper()
            break
        else:
            break

    notes = ET.parse('notes_' + fil + '.xml').getroot()
    searchRes = notes.findall('student')

    pdf = FPDF(orientation = 'P', unit = 'mm', format='A3')
    A3 = 297
    pdf.add_page() 

    headers = []

    for child in searchRes[0]:
        if child.tag == 'cne':
            headers.append('CNE')
        if child.tag == 'module':
            for el in child:
                if el.tag == 'name':
                    headers.append(el.text)

    headers.append('Moyenne')
    margin = 5
    pdf.set_margins(margin,15,margin)
    pdf.set_font("Arial", size = 12) 
    pdf.cell(A3, 10,' ', ln = 1, align = 'L') 
    width = (A3/len(headers)) - margin/2
    
    for hr in headers:
        pdf.set_font("Arial", size = 15) 
        if len(hr) > 7:
            hr = hr[0:7] + '...'
        pdf.cell(width, 10, txt = hr, ln = 0, align = 'L') 

    pdf.cell(A3, 10, txt = ' ', ln = 1, align = 'L')
    pdf.set_font("Arial", size = 10) 

    modMoy=[0 for i in range(len(headers) - 2)]
    index = 0

    for student in searchRes:
        if not searchRes is None:
            stMoy = 0
            pdf.set_font("Arial", size = 10)
            for child in student:
                if child.tag == 'cne':
                    pdf.cell(width, 10, txt = child.text, ln = 0, align = 'L')
                if child.tag == 'module':
                    for el in child:
                        if el.tag == 'note':
                            pdf.cell(width, 10, txt = el.text, ln = 0, align = 'L')
                            stMoy+= float(el.text)
                            modMoy[index % len(modMoy)]+=float(el.text)
                            index+=1
            pdf.set_font("Arial", size = 15)
            pdf.cell(width, 10, txt = str(round(stMoy/((len(headers)) - 2),2)) , ln = 1, align = 'L')


    modMoy = [ x/(index // len(modMoy)) for x in modMoy]

    pdf.set_font("Arial", size = 15) 
    pdf.cell(width, 10, txt = 'Moyenne', ln = 0, align = 'L') 

    for moy in modMoy:
        pdf.cell(width, 10, txt = str(round(moy,2)), ln = 0, align = 'L') 

    pdf.output('affichage_' + fil + '.pdf')

def createAttReu(cne):
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A3')
    pdf.add_page() 
    availableNote = availableNotes()

    global stMoy
    global modCount
    global state

    stMoy = 0
    modCount = 0
    state = True

    for fil in availableNote:
        notes = ET.parse('notes_' + fil + '.xml').getroot()
        searchRes = notes.find('.//student[cne="' + str(cne) + '"].')

        if not searchRes is None:
            for child in searchRes:
                if child.tag == 'cne':
                   cne = child.text
                if child.tag == 'module':
                    modCount+=1
                    for el in child:
                        if el.tag == 'note':
                            stMoy+=float(el.text)
                            
      #  print(cne,stMoy,modCount)

        if 'AP1' in fil or 'AP2' in fil:
            if stMoy/modCount < 10:
                state = False
        else:
            if stMoy/modCount < 12:
                state = False

    if state:
        pdf.set_font("Arial", size = 25) 
        pdf.cell(35, 20, txt = cne, ln = 1, align = 'c') 
        pdf.set_font("Arial", size = 20) 
        pdf.cell(35, 10, txt = 'Vous avez valide votre annee felicitations', ln = 1, align = 'c') 

    pdf.output('attestation_' + str(cne) + '.pdf')

def emploi(days):
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page() 
    availablemodules = availablemods()
    level = ''
    if len(availablemodules) != 0:
        level = input('enter desired level to generate schedule for:\n-Available choices are: ' + str(availablemodules).split('[')[1].split(']')[0] + '\n\t>> ').upper()
        while True:
            if level not in availablemodules:
                print('please enter a valid module')
                level = input('enter desired level to generate schedule for:\n-Available choices are: ' + str(availablemodules).split('[')[1].split(']')[0] + '\n\t>> ').upper()
            else:
                break

    module_xml = ET.parse('modules_' + level + '.xml').getroot()

    modules = module_xml.findall('module')
    elements = []

    for module in modules:
        for child in module:
            if child.tag != 'name' and child.tag != 'dept_attachement':
                elements.append(child.text)

    emp =  []
    randomEl = ''

    for i in range(days):
        emp.append([])
        for j in range(0,random.randint(2,4)):
            emp[i].append('')
            randomEl = elements[random.randint(0,len(elements) - 1)]
            if emp[i][j - 1] == randomEl:
                randomEl = elements[(elements.index(randomEl) + 1 ) % len(elements)]
                emp[i][j] = randomEl
            else:
                emp[i][j] = randomEl
    
    pdf.set_font("Arial", 'B', size = 23)
    pdf.cell(190, 40, 'Emploi ' + level, 0, 1, 'C')

    pdf.set_font("Arial", size = 15) 
    pdf.cell(35, 10, txt = ' ', ln = 0, align = 'L')
    pdf.cell(35, 10, txt = '9:00-10:30', ln = 0, align = 'L')
    pdf.cell(35, 10, txt = '10:45-12:15', ln = 0, align = 'L')
    pdf.cell(35, 10, txt = '1:30-3:00', ln = 0, align = 'L')
    pdf.cell(35, 10, txt = '3:15-4:45', ln = 0, align = 'L')   
    pdf.cell(35, 10, txt = ' ', ln = 1, align = 'L')     
    for day in emp:
        pdf.cell(35, 10, txt = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi'][emp.index(day) % 5], ln = 0, align = 'L')
        for el in day:
            if len(el) > 8:
                el = el[0:8] + '...';
            pdf.cell(35, 10, txt = el, ln = 0, align = 'L')
        pdf.cell(35, 10, txt = ' ', ln = 1, align = 'L')    

    pdf.output('emploi_' + str(level) + '.pdf')

    #print(emp)

def main():
    #studentCNE = input('entrez le CNE:\n\t>>')
    #createStudentCard(studentCNE)
    #createStudentReleve(studentCNE)
    #createFilReleve()
    #createAffichage()
    #createAttReu(studentCNE)
    emploi(5)

main()