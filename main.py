from flask import Flask
from flask import request
import json
import configparser
import time
app = Flask(__name__)
Config = configparser.ConfigParser()
Config._interpolation = configparser.ExtendedInterpolation()

@app.route('/genie/')
def hello_world():
    return 'Hello World!'

@app.route('/genie/getQuestions',methods = ['GET'])
def getQuestion():
    d = {}
    d["questions"]=getProperty("Questions","questionData")
    d["message"] = "success"
    return json.dumps(d),200

@app.route('/genie/question',methods = ['POST'])
def acknowledgeAskedQuestion():
    d = {}

    json_str = json.dumps(request.get_json())


    resp = json.loads(json_str)

    question =resp['query']
    print(question)
    d["question"] =question
    d["timeQuestioned"] = time.strftime('%-m:%-d:%Y %Z on %b %d, %Y')
    d["message"] = "success"
    writeValueIntoProperty("Questions", "questiondata", question)
    return json.dumps(d),200

@app.route('/genie/answer',methods = ['POST'])
def acknowledgeAnsweredQuestion():
    d = {}

    json_str = json.dumps(request.get_json())

    resp = json.loads(json_str)
    answer = resp['query']
    d["answer"] =answer
    d["timeAnswered"] = time.strftime('%-m:%-d:%Y %Z on %b %d, %Y')
    d["message"] = "success"
    writeValueIntoProperty("Answers","answerData",answer)
    return json.dumps(d),200

@app.route('/genie/getAnswers',methods = ['GET'])
def getAnswer():
    d = {}

    d["message"] = "success"

    d["answers"]=getProperty("Answers","answerData")
    return json.dumps(d),200

def writeValueIntoProperty(key,value,newvalue):
    Config.read("properties.ini")
    sectionObj= Config[key]
    existval=getProperty(key,value)
    sectionObj[value] = existval+"\n"+newvalue
    with open('properties.ini', 'w') as conf:
        Config.write(conf)



def getProperty(key,value):
    Config.read("properties.ini")
    return Config.get(key, value)


if __name__=="__main__":
       app.run(host=None,port=8001,debug=True)
