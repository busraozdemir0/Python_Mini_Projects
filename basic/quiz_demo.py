# Basit bir quiz-answer uygulaması


class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    
    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):  #gönderilen indekse göre ilgili soruyu alır ve ekranda gösterir
        question=self.getQuestion()
        print(f"Soru {self.questionIndex+1}: {question.text}")

        for q in question.choices:
            print("-"+q)
        
        answer=input("Cevap: ")
        self.quess(answer)
        self.loadQuestion()
    
    def quess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1

    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
 
    def showScore(self):
        print("Score: ",self.score)

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex+1

        if questionNumber>totalQuestion:
            print("Quiz bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))


q1=Question("En iyi programlama dili hangisidir?",["c#","python","javaScript","java"],"c#")
q2=Question("En popüler programlama dili hangisidir?",["python","c#","java","javaScript"],"java")
q3=Question("En çok kazandıran programlama dili hangisidir?",["c#","javaScript","java","python"],"javascript")
q4=Question("Android uygulama geliştirmeye yönelik uygun programlama dili hangisidir?",["java","c#","javaScript","python"],"java")  
q5=Question("OOP adı geçince ilk bilinen programlama dili hangisidir?",["c#","javaScript","java","python"],"c#")  
q6=Question("En kolay programlama dili hangisidir?",["c#","javaScript","python","java"],"python")  
questions=[q1,q2,q3,q4,q5,q6]

quiz=Quiz(questions)

quiz.loadQuestion()


