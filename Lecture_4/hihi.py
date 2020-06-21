import random

#function for judging number
#code for judging number
larger = 1
smaller = 2
equal = 0
def compare(userInp,Ans):
    if(userInp < Ans):
        return larger
    elif(userInp > Ans):
        return smaller
    return equal

#get user input
userInp = int(input("Enter a number: "))
#get a random number
correctAns = random.randint(0,10) 
#initialize count variable
count = 1
#judging user answer
while(userInp != correctAns and count < 3):
    if(compare(userInp,correctAns) == larger):
        print("Sai! số random lớn hơn {0}".format(userInp))
        userInp = int(input("Xin nhập lại: "))
        count += 1
    else: 
        print("Sai! số random nhỏ hơn {0}".format(userInp))
        userInp = int(input("Xin nhập lại: "))
        count += 1
#if count == 3, the user loses, but if count < 3, the user wins
if(count == 3):
    print("Bạn đã thua! số đúng là {0}".format(correctAns))
else:
    print("Bạn đã thắng! số đúng là {0}".format(correctAns))