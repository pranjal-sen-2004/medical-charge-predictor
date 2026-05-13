print("FILE IS RUNNING")
from flask import Flask,jsonify,render_template,request
import pickle
import pandas as pd

application=Flask(__name__)
app=application

try:
    print("Loading model...")
    lasso_model = pickle.load(open('lasso.pkl','rb'))
    print("Model loaded")

    print("Loading scaler...")
    scaler = pickle.load(open('scaler.pkl','rb'))
    print("Scaler loaded")

except Exception as e:
    print("ERROR OCCURRED:", e)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":
        age=int(request.form.get('age'))
        sex=int(request.form.get('sex'))
        bmi=float(request.form.get('bmi'))
        smoker=int(request.form.get('smoker'))
        children=int(request.form.get('children'))
        region=int(request.form.get('region'))

        transformed_data=scaler.transform([[age,sex,bmi,children,smoker,region]])
        result=lasso_model.predict(transformed_data)

        return render_template('predict.html',results=result[0])
    else:
        return render_template('predict.html')

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host="127.0.0.1", port=5000, debug=True)
