"This program helps to find the BMI of a person."


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI = round(weight / height ** 2)
 
  if(BMI < 18.5):
   print(f"Your bmi is {BMI}, you are underweight.")

  elif(BMI < 25):
   print(f"Your bmi is {BMI}, you are normalweight.")

  elif(BMI < 30):
   print(f"Your bmi is {BMI}, you are overweight.")

  elif(BMI < 35):
   print(f"Your bmi is {BMI}, you are obese.")

  else:
   print(f"Your bmi is {BMI}, you are clinically obese.")
