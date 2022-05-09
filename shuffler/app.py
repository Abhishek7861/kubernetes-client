# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import task_executor as taskExecutor

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/start-job', methods=['POST'])
def hello_world():
    taskExecutor.triggerJob("Hello World")
    return 'Job scheduled with id: dummy'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(port=8000)
