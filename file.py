import random
import sys

file = open("test.txt", "w+")
file.write("What is the longest river in Russia and Europe ?  Volga \n")
file.write("What is the capital city of Armenia ?  Yerevan \n")
file.write("5+5 ? 10 \n")
file.write("15*2= ?  30 \n")
x = random.randint(1, 4);
file.close()
count = 0
question = ""
answer = ""
f = open("test.txt", "r")
f1 = f.readlines()
for line in f1:
    count += 1
    if (count == x):
        question = line[:line.index('?')]
        answer = line[line.index('?') + 1:].strip()

print(question)
str = '-' * len(answer)
print(str)

#if we enter only 1 char

while str != answer:
    var = input("enter answer")
    if(len(var) > 1):
        var = input("Reenter answer")
    for j in range(len(answer)):
        if (var == answer[j]):
            str = str[:j] + var + str[j + 1:]
    print(str)
print("Congrats!")
file.close()
