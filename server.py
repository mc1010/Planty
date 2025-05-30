from flask import Flask, request, jsonify
from predict import predict
print("Lancement du fichier server.py")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    if 'image' not in request.files:
        return jsonify({'error': 'Image manquante'}), 400

    image = request.files['image'].read()
    label, confidence = predict(image)

    return jsonify({
        'status': 'success',
        'prediction': label,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
