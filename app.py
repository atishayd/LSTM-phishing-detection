from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

model = tf.keras.models.load_model("lstm_model.keras")

with open('tokenizer.pkl', 'rb') as f:
    tk = pickle.load(f)

def preprocess(text):
    sequences = tk.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequences, padding='post', maxlen=150)
    return padded_sequence  

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.data.decode("utf-8") 
        input_data = preprocess(text)
        prediction = model.predict(input_data)[0][0] 
        result = {"prediction": float(prediction)}
    except Exception as e:
        result = {"error": str(e)} 

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
