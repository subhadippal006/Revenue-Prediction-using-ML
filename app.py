import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Models/model_pickle.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('predict.html')

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
        

    return render_template('predict.html', prediction_text='Revenue will  {}'.format(res_val))

if __name__ == "__main__":
    app.run()
