from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result/', methods=['GET','POST'])
def result():
    Name = request.form.get('name')
    Sex_Upon_Outcome = request.form.get('sex_upon_outcome')
    # Age_days = int(request.form.get('age_days'))
    Sex = request.form.get('sex')
    cfa_breed = request.form.get('cfa_breed')
    # coat_pattern = request.form.get('coat_pattern')
    pattern = request.form.get('pattern')
    Cat_Kitten_Neonatal = request.form.get('cat_kitten_neonatal')

    # value = [Name,Age_days,Sex,cfa_breed,coat_pattern,pattern,Cat_Kitten_Neonatal,Sex_Upon_Outcome]
    value = [[Name,Sex,cfa_breed,pattern,Cat_Kitten_Neonatal,Sex_Upon_Outcome]]
    columns = ['Name','Sex','cfa_breed','pattern','Cat_Kitten_Neonatal','Sex_Upon_Outcome']
    result = pd.DataFrame(value, columns=columns)

    pred = model.predict(result)

    return render_template('result.html', pred=pred)
    # return Sex

if __name__ == '__main__':
    app.run(debug=True)