# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = 90*365 #- (90//4)
weeks = 90*52 #- (90//4)//7
months = 90*12
x = days - (int(age)*365)
y = weeks - (int(age)*52)
z = months - (int(age)*12)
print(f"You have {x} days, {y} weeks, and {z} months left.")
