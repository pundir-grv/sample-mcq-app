from config import constants
import mysql.connector
  
dataBase = mysql.connector.connect(
  host = constants.dbData["host"],
  port = constants.dbData["port"],
  user = constants.dbData["user"],
  passwd = constants.dbData["password"],
  database = constants.dbData["name"]
)
 
cursorObject = dataBase.cursor()

def getQuestionFromDb(id):
    sql = "SELECT question,option1,option2,option3,option4 from mcq where question_id = %s"
    val = [id]
    cursorObject.execute(sql, val)
    return cursorObject.fetchall()[0]

def getAnswer(id):
    sql = "SELECT answer from mcq where question_id = %s"
    val = [id]
    cursorObject.execute(sql, val)
    return cursorObject.fetchall()[0][0]

def getTotalQuestions():
    sql = "SELECT count(question_id) from mcq"
    cursorObject.execute(sql)
    return cursorObject.fetchall()[0][0]





