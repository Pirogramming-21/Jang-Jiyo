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
def Menu1(name, mid-score, final-score) :
   # 사전에 학생 정보 저장하는 코딩
   student = [name, mid-score, final-score]
   studentList.append(student)

##############  menu 2
def Menu2() :
   # 학점 부여 하는 코딩
   for student in studentList:
      if len(student) != 4:
         avg-score = (student[1] + student[2]) / 2
         if avg-score >= 90:
            student[3] = 'A'
         else if avg-score >= 80:
            student[3] = 'B'
         else if avg-score >= 70:
            student[3] = 'C'
         else:
            student[3] = 'D'

##############  menu 3
def Menu3() :
   # 출력 코딩
   print("--------------------------")
   print("name  mid  final  grade")
   print("--------------------------")
   for student in studentList:
      print(f"{student[0]}  {studnet[1]}  {student[2]}  {student[3]}")

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
         input_line = input("Enter name mid-score final-score : ")
         data = input_line.split()
         name = data[0]
         # 데이터 입력 갯수 예외 처리
         if len(data) != 3:
            raise WrongInputNum("Invalid Number of Data Inputs")
         # 이미 존재하는 이름 예외 처리
         for student in studentList:
            if name == student[0]:
               raise ExistName("Name that already Exists")
         # 입력 점수 값 양의 정수 아닐 경우 예외처리
         id-score, final-score = map(int, data[1:])
         if mid-score <= 0 or final-score <= 0:
            raise NegativeScore("Negative Score Value")
      except ValueError:
         print("Non-Integer Score Value")
      except NegativeScore as e:
         print(e)
      except WrongInputNum as e:
         print(e)
      except ExistName as e:
         print(e)
      # 예외사항이 아닌 입력인 경우 1번 함수 호출
      else:
         Menu1(name, mid-score, final-score)

   elif choice == "2" :
      # 예외사항 처리(저장된 학생 정보의 유무)
      try:
         if len(studnetList) == 0:
            raise NoStudentData("No Student Data Saved")
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
         if len(studnetList) == 0:
            raise NoStudentData("No Student Data Saved")
         for student in studentList:
            if len(student) != 4:
               raise NoGrade("Student not Granted Credit")
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
         if len(studnetList) == 0:
            raise NoStudentData("No Student Data Saved")
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
            menu4(name)
            print(f"{name} student information is deleted.")

   elif choice == "5" :
      #프로그램 종료 메세지 출력
      #반복문 종료

   else :
      #"Wrong number. Choose again." 출력