import pickle
from flask import Flask, request, jsonify,app,url_for,render_template
from preprocessing import *
# Initialize Flask app
app = Flask(__name__)

# Load the model
with open('gb_regressor_model.pkl','rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    try:
        data = request.json['data']
        df = process_time_series_data(data)
        input_sample = df_to_X_single_sample(df,window_size=5)
        output = model.predict(input_sample)[0]
        return jsonify({'output':round(output,3)}),200
    except Exception as e:
        return jsonify({'error':str(e)}), 400    

@app.route('/predict',methods=['POST'])
def predict():
    date_list = [request.form[f'date{i}'] for i in range(1,6)]
    time_list = [request.form[f'time{i}'] for i in range(1,6)]
    global_active_power_list = [float(request.form[f'global_active_power{i}']) for i in range(1, 6)]
    global_reactive_power_list = [float(request.form[f'global_reactive_power{i}']) for i in range(1, 6)]
    voltage_list = [float(request.form[f'voltage{i}']) for i in range(1, 6)]
    global_intensity_list = [float(request.form[f'global_intensity{i}']) for i in range(1, 6)]
    sub_metering_1_list = [float(request.form[f'sub_metering_1{i}']) for i in range(1, 6)]
    sub_metering_2_list = [float(request.form[f'sub_metering_2{i}']) for i in range(1, 6)]
    sub_metering_3_list = [float(request.form[f'sub_metering_3{i}']) for i in range(1, 6)]
    data = process_input_data(date_list,time_list,global_active_power_list,global_reactive_power_list,voltage_list,global_intensity_list,sub_metering_1_list,sub_metering_2_list,sub_metering_3_list)
    df = process_time_series_data(data)
    input_sample = df_to_X_single_sample(df,5)
    output = round(model.predict(input_sample)[0],3)
    return render_template('home.html',prediction_text=f'The consumed power for the next hour prediction is {output}')
if __name__ == '__main__':
    app.run(debug=True)   
