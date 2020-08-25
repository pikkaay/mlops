from flask import Flask, jsonify, request
from healthcheck import HealthCheck
import logging


app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.DEBUG,
	format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app.logger.info('Model is loaded')

health = HealthCheck(app, "/hcheck")


def howami():
	return True, 'Im doing good'

health.add_check(howami) 


@app.route('/classifier', methods=['POST'])
def predict():
	app.logger.info('predicting request')
	text = request.json["text"]
	return jsonify({'prediction': 'success', 'text':text})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000', debug=True)
