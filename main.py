import pickle
from flask import Flask,render_template,request

#create object of flask

app = Flask(__name__,template_folder='templets')


# Un dump the model

model = pickle.load(open('model.pkl','rb'))

#rul
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def  predict():
    prediction = model.predict([[int(request.form.get('temprature'))]])
    output = round(prediction[0],2)
    print(output)
    return render_template('index.html',prediction_text=f'Total revenue genarated in Rs. {output}')


if __name__ =='__main__':
    app.run(debug=True)