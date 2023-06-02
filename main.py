from flask import Flask,render_template,jsonify,request
from project_app.utils import MedicalInsurance

app=Flask(__name__)

@app.route('/')
def home_api():
    print("We are in Home API")

    return render_template('index.html')

@app.route("/prediction",methods=['GET','POST'])
def prediction():

    if request.method=="GET":
        age= int(request.args.get("age"))
        sex = (request.args.get("sex"))
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        med_ins=MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges=med_ins.get_prediction()

        return render_template('index.html',prediction=charges)
    else:
        age= int(request.form.get("age"))
        sex = (request.form.get("sex"))
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        med_ins=MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges=med_ins.get_prediction()

        return render_template('index.html',prediction=charges)
        
if __name__=="__main__":
     app.run(host='0.0.0.0',port=5000,debug=True)
             
