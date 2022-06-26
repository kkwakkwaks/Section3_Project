import pandas as pd
import csv

file = open('cat_data.csv','r')
reader = csv.reader(file)

# DB생성
import sqlite3
con = sqlite3.connect('cat_dataDB.db')
cur = con.cursor()

# table생성
cur.execute('''
CREATE TABLE cat_data(
    Name INTEGER, 
    Sex_upon_Outcome VARCHAR(30),
    Adopt INTEGER,
    Age_days INTEGER, 
    Sex VARCHAR(30),        
    cfa_breed INTEGER,
    coat_pattern VARCHAR(30), 
    pattern INTEGER,
    Cat_Kitten_Neonatal VARCHAR(30)
)
''')


for row in reader:
    Name = (row[1])
    Sex_upon_Outcome = (row[2])
    Adopt = (row[3])
    Age_days = (row[4])
    Sex = (row[5])
    cfa_breed = (row[6])
    coat_pattern = (row[7])
    pattern = (row[8])
    Cat_Kitten_Neonatal = (row[9])
    


    ist = 'INSERT INTO cat_data(Name,Sex_upon_Outcome, Adopt,Age_days,Sex,cfa_breed,coat_pattern,pattern,Cat_Kitten_Neonatal) VALUES(?,?,?,?,?,?,?,?,?);'
    cur.execute(ist,(Name,Sex_upon_Outcome, Adopt,Age_days,Sex,cfa_breed,coat_pattern,pattern,Cat_Kitten_Neonatal))

cur.execute('''DELETE FROM cat_data
WHERE rowid=1;''')


con.commit()

cur.close()
con.close()