from flask import Flask, request
from db import getQuestionFromDb, getAnswer, getTotalQuestions
import random


app = Flask(__name__)

@app.route('/')
def homePage():
    msg = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>MCQ Questions</title>
        </head>
        <body>
            <h1>Sample flask based app to demonstrate read write operation in mysql</h1>
            
            <h2><a href="/getQuestion">New Question</a></h2>
        </body>
    </html>
    """
    return msg


@app.route('/getQuestion')
def getQuestion():
    count = getTotalQuestions()
    id = random.randrange(1,count+1)
    question = getQuestionFromDb(id)
    msg = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>MCQ Questions</title>
        </head>
        <body>
            <form action="/answer" method="post">
                <h2>{question}</h2>
                <input type="hidden" name="question" value="{question_id}">
                <input type="radio" id="option1" name="option" value="{option1}">
                <label for="option1">{option1}</label><br>
                <input type="radio" id="option2" name="option" value="{option2}">
                <label for="option2">{option2}</label><br>
                <input type="radio" id="option3" name="option" value="{option3}">
                <label for="option3">{option3}</label><br>
                <input type="radio" id="option4" name="option" value="{option4}">
                <label for="option4">{option4}</label><br>
                
                <input type="submit" value="Submit">
            </form>
            
        </body>
    </html>
    """.format(question_id=id,question=question[0],option1=question[1],option2=question[2],option3=question[3],option4=question[4])

    return msg

@app.route('/answer', methods=['POST'])
def checkAnswer():
    choice = request.form.get("option")
    id = request.form.get("question")
    correctAnswer = getAnswer(id)
    if correctAnswer == choice:
        label = "Correct Answer."
    else:
        label = "Wrong Answer, Answer: {}".format(correctAnswer) 
    message = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>MCQ Questions</title>
        </head>
        <body>
            
            <h2>{label}</h2><br>
            <h2><a href="/getQuestion">New Question</a></h2>
            
        </body>
    </html>
    """.format(label=label)
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)