from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='/var/log/my_flask_app_foo.log',level=logging.INFO)

@app.route('/')
def index():
    random_number = request.headers.get('X-Random-Number')
    app.logger.info(f'Received random number: {random_number}')
    return render_template('index.html', random_number=random_number)

@app.route('/foo')
def bar():
    random_number = request.headers.get('X-Random-Number')
    app.logger.info(f'Received random number: {random_number}')
    return render_template('foo.html', random_number=random_number)

if __name__ == '__main__':
    app.run('0.0.0.0',port=80,debug=True)
