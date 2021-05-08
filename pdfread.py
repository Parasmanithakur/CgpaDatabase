
# importing required modules
import PyPDF2
import sqlite3
import re
conn = sqlite3.connect('cgpa.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE ece (name TEXT NOT NULL , cgpa FLOAT,idn TEXT UNIQUE PRIMARY KEY)''');


pdfname =input("Enter pdf name")

pdfFileObj = open(pdfname, 'rb')

# creating a pdf Reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)
j=0
data=dict()
ece=list()
for i in range(pdfReader.numPages):
     pageObj = pdfReader.getPage(i)
     
     str1=str(pageObj.extractText())# extracting text from page
     
     j=0
     str1=str1.strip()
     gpa=re.findall(r'CGPAEGP[0-9]+([0-9].[0-9]+)',str1)
     for sgpa in gpa:
       cgpa=sgpa
       
     Enroll=re.findall(r'Degree:([A-za-z]+[0-9]+[A-za-z]+[0-9]+)' ,str1)
     if not (Enroll):
       Enroll=re.findall(r'Degree:([A-za-z]+[0-9]+)',str1)     
     ece.append(cgpa)
     ece.append(Enroll)  
     name=re.findall(r'Technology([A-za-z]+\s[A-za-z]*?)',str1)
     name=str(name[0])
     Enroll=str(Enroll[0])
     cgpa=float(cgpa)
     cur.execute('''INSERT OR REPLACE INTO ece(name,cgpa,idn)
        VALUES ( ?, ?,? )''', ( name,cgpa,Enroll) )
     conn.commit()
cur.close()
# closing the pdf file object
pdfFileObj.close()