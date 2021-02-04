import random
import sys
file  = open("test.txt","w+")
file.write("What is the longest river in Russia and Europe ?  Volga \n")
file.write("What is the capital city of Armenia ?  Yerevan \n")
file.write("5+5 ? 10 \n")
file.write("15*2= ?  30 \n")
x = random.randint(1,4);
file.close()
count = 0
question = ""
answer = ""
f = open("test.txt","r")
f1 = f.readlines()
for line in f1:
    count +=1
    if(count == x):
        question = line[:line.index('?')]
        answer = line[line.index('?')+1:].strip()

print(question)
str = '-'*len(answer)
print(str)
flag = False
for line in sys.stdin:
    for var in line.split():
        for i in range(len(var)):
            for k in range(len(answer)):
                if(var[i] == answer[k]):
                    str = str[:k]+var[i]+str[k+1:];
        print(str);
        if (var == answer or str == answer):
            print("Congrats!")
            flag = True

    if(flag):
        break
file.close()
