from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='app.log',level=logging.INFO)

@app.route('/')
def index():
    random_number = request.headers.get('X-Random-Number')
    app.logger.info(f'Received random number: {random_number}')
    return render_template('index.html', random_number=random_number)

@app.route('/bar')
def bar():
    random_number = request.headers.get('X-Random-Number')
    app.logger.info(f'Received random number: {random_number}')
    return render_template('bar.html', random_number=random_number)

if __name__ == '__main__':
    app.run('0.0.0.0',port=80,debug=True)
