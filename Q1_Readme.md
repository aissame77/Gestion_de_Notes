1- Objectif: Conversion de l’ensemble des fichiers Excel au Format XML
- We have chosen to use Python as our scripting language in order to generate our data.
- At first as we have four main classes we are going to need a script that generates the xml files for our classes
those are: Modules, Students, Notes, and Profs.
- Each of those scrips contain three functions:
  + 1st one is to read the data from the csv file and creates a new list that contains the data+ filiere.
  + 2nd one is to define the xml format.
  + 3rd is to generate the aimed xml file using the data provided and respecting the format
- The only package imported used for this question is CSV.
- There is a file 'CSV_FILES ' that contains all the csvs that we have used for this project; which we have randemly generated using excel and a list of arabic names.
- The only real csv file used is the list of our class 'GINF2', please if you are using this make sure to respect the personal data.
- To generate marks (notes) we have imported the folwing packages: 
    + ElementTree: navigation and access to elements
    + re
    + random: to generate random marks and associate them with students
    + os
  We select the modules available so we can be specific to generate which marks that is why we have created a fct to detect and show the avialable modules
- You will find all the generated xml files in 'Generated_xml' but you can generate it by chaningg the 'path' variable in each script.
