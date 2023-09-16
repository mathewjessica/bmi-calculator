#I am going to be building a BMI calculator. 
#But what makes this one special? It's unique becuase it gives you suggestions on how you can 
#reach a healthy BMI

name = str(input("What is your name?"))
print("Hello", name,"today we're gonna help calculate your BMI!")

weight = float(input("Your weight in lbs: "))
height = float(input("Your height in inches: "))

BMI = (weight * 703)/(height * height)
print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name , "you are in the Underweight category")
    elif(BMI <= 24.9):
        print(name , "you are in the Normal weight category")
    elif(BMI < 29.9):
        print(name , "you are in the Overweight category")
    elif(BMI < 34.9):
        print(name , "you are in the Obese catgoery")
    elif(BMI < 39.9):
        print(name , "you are in the Serverly Obese catogory")
    else:
        print(name , "you are in the Morbidly Obese catgory")
#I'm done!