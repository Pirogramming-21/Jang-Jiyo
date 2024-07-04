# 예외 처리 함수
# 1. 잘못된 데이터 개수 입력
class WrongInputNum(Exception):
   pass
# 2. 이미 존재하는 이름
class ExistName(Exception):
   pass
# 3. 입력 점수 값이 양의 정수가 아님
class NegativeScore(Exception):
   pass
# 4. 저장된 학생 정보 없음
class NoStudentData(Exception):
   pass
# 5. 저장되어 있는 학생의 학점이 부여되지 않음
class NoGrade(Exception):
   pass
# 6. 존재하지 않는 이름
class NoExistName(Exception):
   pass

# 학생 정보를 저장할 리스트
studentList = []

##############  menu 1
def Menu1(name, midScore, finalScore) :
   # 사전에 학생 정보 저장하는 코딩
   student = [name, midScore, finalScore]
   studentList.append(student)

##############  menu 2
def Menu2() :
   # 학점 부여 하는 코딩
   for student in studentList:
      if len(student) != 4:
         avgScore = (student[1] + student[2]) / 2
         if avgScore >= 90:
            student.append('A')
         elif avgScore >= 80:
            student.append('B')
         elif avgScore >= 70:
            student.append('C')
         else:
            student.append('D')

##############  menu 3
def Menu3() :
   # 출력 코딩
   print("--------------------------")
   print("name  mid  final  grade")
   print("--------------------------")
   for i in range(len(studentList)):
      print(f"{studentList[i][0]}   {studentList[i][1]}    {studentList[i][2]}      {studentList[i][3]}")

##############  menu 4
def Menu4(targetName):
   # 학생 정보 삭제하는 코딩
   for student in studentList:
      if student[0] == targetName:
         studentList.remove(student)

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
   choice = input("Choose menu 1, 2, 3, 4, 5 : ")
   if choice == "1":
      # 학생 정보 입력받기
      # 예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
      try:
         inputLine = input("Enter name mid-score final-score : ")
         data = inputLine.split()
         name = data[0]
         # 데이터 입력 갯수 예외 처리
         if len(data) != 3:
            raise WrongInputNum("Num of data is not 3!")
         # 이미 존재하는 이름 예외 처리
         for student in studentList:
            if name == student[0]:
               raise ExistName("Already exis name!")
         # 입력 점수 값 양의 정수 아닐 경우 예외처리
         midScore, finalScore = map(int, data[1:])
         if midScore <= 0 or finalScore <= 0:
            raise NegativeScore("Score is not positive integer!")
      except ValueError:
         print("Score is not integer!")
      except NegativeScore as e:
         print(e)
      except WrongInputNum as e:
         print(e)
      except ExistName as e:
         print(e)
      # 예외사항이 아닌 입력인 경우 1번 함수 호출
      else:
         Menu1(name, midScore, finalScore)

   elif choice == "2" :
      # 예외사항 처리(저장된 학생 정보의 유무)
      try:
         if len(studentList) == 0:
            raise NoStudentData("No Student data!")
      except NoStudentData as e:
         print(e)
      # 예외사항이 아닌 경우 2번 함수 호출
      else:
         Menu2()
         # "Grading to all students." 출력
         print("Granding to all studnets.")

   elif choice == "3" :
      # 예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
      try:
         if len(studentList) == 0:
            raise NoStudentData("No Student data!")
         for student in studentList:
            if len(student) != 4:
               raise NoGrade("There is a student who didn't get grade.")
      except NoStudentData as e:
         print(e)
      except NoGrade as e:
         print(e)
      # 예외사항이 아닌 경우 3번 함수 호출
      else:
         Menu3()

   elif choice == "4" :
      # 예외사항 처리(저장된 학생 정보의 유무)
      try:
         if len(studentList) == 0:
            raise NoStudentData("No Student data!")
      except NoStudentData as e:
         print(e)
      # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
      else:
         # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
         name = input("Enter the name to delete : ")
         try:
            flag = 0
            for student in studentList:
               if student[0] == name:
                  flag = 1
                  break
            if flag == 0:
               raise NoExistName("Not exist name!")
         except NoExistName as e:
            print(e)
         # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
         else:
            Menu4(name)
            print(f"{name} student information is deleted.")

   elif choice == "5" :
      # 프로그램 종료 메세지 출력
      print("Exit Program!")
      # 반복문 종료
      break

   else :
      # "Wrong number. Choose again." 출력
      print("Wrong number. Choose again.")