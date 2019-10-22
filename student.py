"""
Date           : 2019.07.16
School 	       : Semyung Computer High School
Team           : SemyungSe~myung
Member :       : Seoyun Kim, Hyunjun Yun, Seungjun Lee
File name      : student.py
Used Editor    : PyCharm, Vim
Python Version : 2.7.6
"""




def inputscore(subject_name):
    score = raw_input(subject_name + ' Score :')
    while 1:
        try:
            i_score = int(score)
            break
        except:
            score = raw_input('type casting error\n ' + subject_name + ' score (number only):')	# If the entered character is not an integer, 
												# print a warning statement with it
    return i_score

def same_name():
	if(inc != 0)
		for k in range(0,len(stu)):
			if(stu_name == stu[k]):
      	                  print("no same  name") 
			  break
		     	else:
			     pass






stu = []			# stu = student
kor_scores = []		# kor = korean
eng_scores = []		# eng = english
math_scores = []
tot_scores = []		# tot = total
kor_sum = 0
eng_sum = 0
math_sum = 0
max_scores = 0
max_idx = 0		# idc = A Random Variable
inc = 0			# inc = A Random Variable
data = 0		# Use in f.write

while (1):
    stu_name = raw_input('Plz Input A Student Name : ')
    if (stu_name != 'Q' and stu_name != 'q'):
        stu.append(stu_name)	
	k=0
	if(inc != 0):
		for k in range(0,len(stu)):
			if(stu_name == stu[k]):
				print("no same name")
				break
			else:
			 	pass
        kor_scores.append(inputscore("Korean"))						# Input scores in 'kor_scores' list
        eng_scores.append(inputscore("English"))					# Input scores in 'eng_scores' list
        math_scores.append(inputscore("Mathmatics"))					# Input scores in 'math_scores' list
        tot_scores.append(kor_scores[inc] + eng_scores[inc] + math_scores[inc])		# Input total scores in 'tot_scores' list
        inc += 1
    else:
        if (len(stu) > 0):
            for idx in range(len(stu)):
                if (tot_scores[idx] > max_scores):		#Sum array's value
                    max_scores = tot_scores[idx]
                    max_idx = idx
                kor_sum = kor_sum + kor_scores[idx];
                eng_sum = eng_sum + eng_scores[idx];
                math_sum = math_sum + math_scores[idx];
            kor_avg = kor_sum / len(stu)			# Divide average the number of students
            eng_avg = eng_sum / len(stu)
            math_avg = math_sum / len(stu)
	
            print("\n\n\n")
            print("Korean Avg : " + str(kor_avg))
            print("English Avg : " + str(eng_avg))
            print("Mathmatics Avg : " + str(math_avg))
            print("Best student : " + str(stu[max_idx]) + ", Total score : " + str(tot_scores[max_idx]))
	    print("Student's name and score data is saved!")
            
	    f = open('student_data.txt', 'w')	# Open student_data.txt 
            for i in range(len(stu)):		# Write on the txt file
                data = "%d. Student : %s Korean : %d English : %d Math : %d\n"% (i+1,stu[i], kor_scores[i], eng_scores[i], math_scores[i])
                f.write(data)

            break
        else:
            print("ERROR! Plz do it again.")
            break
f.close()
