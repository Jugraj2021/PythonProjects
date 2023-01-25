name = input('Name: ')
age = int(input('Age: '))
gender = input('Enter M for male or F for female: ')
weight = float(input('Enter your weight in pounds: '))
height = float(input('Lastly, enter your height in inches: '))

# round(float, 2)
bmi = round(((weight/height**2)*703),2)

if bmi < 16:
  print(f'Oh NO, You are severly underweight. (Your BMI is {bmi})!!!')
elif bmi >= 16 and bmi < 18.5:
  print(f'NOoooo, You are underweight!!!. (Your BMI is {bmi})')
elif bmi >= 18.5 and bmi < 25:
  print(f'Ohkk Good, You are Healthy :). (Your BMI is {bmi})')
elif bmi >= 25 and bmi < 30:
  print(f'Man, You are Overweight, do gym ;). (Your BMI is {bmi})')
else:
  print(f'Damn, You are obese, try fasting... (Your BMI is {bmi})')


# Nutrition Calculation

print()
foods = {'Milk':100, 'Egg':155, 'Rice':130,'Lentils':113,'Vegetables':85,'Meat':143}

print('Your nutrition caclculation::')
calorie = {}
total_calories = 0
for i in foods.keys():
  calorie[i] = float(input(f'Quantity for the food {i}: '))
  total_calories += ((foods[i]/100)*calorie[i])
    
print("Your total calorie intake is ",total_calorie)

if age >= 0 and age < 2:
  if total_calories >= 800:
    print(f'You are properly nourished as the recommneded calories for you is\
    800 and  your calorie intake is {total_calories}')
  else:
    print(f'You are malnourished as the recommneded calories for you is\
    800 and  your calorie intake is {total_calories}')
elif age >=2 and age < 4:
  if total_calories >= 1400:
    print(f'You are properly nourished as the recommneded calories for you is\
    1400 and  your calorie intake is {total_calories}')
  else:
    print(f'You are malnourished as the recommneded calories for you is\
    1400 and  your calorie intake is {total_calories}')
elif age >=4 and age < 8:
  if total_calories >= 1800:
    print(f'You are properly nourished as the recommneded calories for you is\
    1800 and  your calorie intake is {total_calories}')
  else:
    print(f'You are malnourished as the recommneded calories for you is\
    1800 and  your calorie intake is {total_calories}')
else:
  print('Sorry, you are not a child!! Can\'t use it')
  


