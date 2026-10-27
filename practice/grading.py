#Grade student based on their score 
def grade(input):
    if(input>=90 and input<=100):
        print("Grade A")
    if(input>=80 and input<=89):
        print("Grade B")
    if(input>=70 and input<=79):
        print("Grade C")
    if(input>=60 and input<=69):
        print("Grade D")
    if(input>=0 and input<=59):
        print("Grade F")

grade(int(input("Enter input to find grade")))