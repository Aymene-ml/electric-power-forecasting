import pickle
from flask import Flask, request, jsonify,app,url_for,render_template
from preprocessing import *
# Initialize Flask app
app = Flask(__name__)

# Load the model
with open('model.pkl','rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    try:
        data = request.json['data']
        print(data)
        print('Date received')
        df = process_time_series_data(data)
        print('data processed')
        input_sample = df_to_X_single_sample(df,window_size=5)
        print('input get ready')
        print('model predicting...')
        output = model.predict(input_sample)[0]
        
        print(f'output:{output}')
        return jsonify({'output':round(output,3)}),200
    except Exception as e:
        return jsonify({'error':str(e)}), 400    
    
if __name__ == '__main__':
    app.run(debug=True)   
