import json

f=open('questions.json')
questions = json.load(f)
f.close()

student = input('Enter Your name:')
mark = 0

for element in questions:
    q = element["q"]
    a = element["a"]
    ans = input(q+'=')
    if ans == a:
        mark = mark + 1

print('your mark is: {}'.format(mark))

f=open('students.txt','a')
f.write(student+" = "+str(mark)+"\n")
f.close()
