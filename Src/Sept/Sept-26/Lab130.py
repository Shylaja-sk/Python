'''
******************** https://spring.io/projects/spring-boot - to get Spring boot where we can build the REST API's

Task
find the difference between SOAP btw REST with example

*****https://medium.com/@timothysmccann/building-restful-apis-with-flask-a-comprehensive-guide-3d68b4fe9368 - FLASK Restful API

*****  https://www.tutorialspoint.com/flask/index.htm --- Learn flask


'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '{"name":"Shylaja"}'
if __name__ == '__main__':
    app.run(debug=True)

