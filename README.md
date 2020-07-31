# firstPython
API Which interacts for questions and answers


Below Set of URLS will interact with Genie and just return what you asked/what it answered (As a baby level) and returns All questions/answers it faced so far


URL:/genie/question
Method: Post
Request Param:
{
"question":"What is your Name?"
"timeQuestioned":"07-31-20 19:05"
"message":"success"
}

URL: /genie/answer
Method: Post
Request Param:
{
"answer":"What is your Name?"
"timeQuestioned":"07-31-20 19:05"
"message":"success"
}

URL: /genie/getQuestions
Method: GET
{
"questions":"questions asked so far"
"message":"success"
}

URL: /genie/getAnswers
Method: GET
{
"answers":"answers told so far"
"message":"success"
}
