import numpy as np
import pandas as pd
import os
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Models/model_pickle.pkl', 'rb'))
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER



@app.route('/')
def home():
 full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
 return render_template("predict.html", user_image = full_filename)

@app.route('/Alliance')
def Alliance():
    return render_template('Alliance.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ["Administrative","Administrative_Duration","Informational","Informational_Duration","ProductRelated","ProductRelated_Duration","BounceRates","ExitRates","PageValues","SpecialDay","Month","OperatingSystems",
                      "Browser","Region","TrafficType","VisitorType","Weekend"]
    
    df = pd.DataFrame(features_value, columns=features_name)
    Revenue = model.predict(df)
        
    if Revenue == 1:
        res_val = "be generated"
    else:
        res_val = "not be generated "
        
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')

    return render_template('predict.html', prediction_text='Revenue will  {}'.format(res_val), user_image = full_filename)




if __name__ == "__main__":
    app.run()
