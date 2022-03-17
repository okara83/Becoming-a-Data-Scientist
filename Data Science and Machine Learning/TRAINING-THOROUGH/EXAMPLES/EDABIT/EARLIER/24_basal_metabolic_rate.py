"""
Basal metabolic rate
Create a funktion that takes a dict with the size, the weight in kg, the age, how much sport the person does and whether the person is male or female

dict = {"gender": "male",
            "size": 180,
             "weight": 80,
             "age": 20,
             "sport": 3}
Return the basal metabolic rate of the person rounded to one decimal place. The formula is: BMR for Men = 66.47 + (13.75 weight) + (5.003 size) − (6.755 * age)

BMR for Women = 655.1 + (9.563 weight) + (1.85 size) − (4.676 * age)

Once you’ve calculated your BMR, this is then put into the Harris Benedict Formula , which calculates your total calorie intake required to maintain your current weight. This is as follows:

Little/no exercise(1): BMR * 1.2 = Total Calorie Need

Light exercise(2): BMR * 1.375 = Total Calorie Need

Moderate exercise (3): BMR * 1.55 = Total Calorie Need

Very active (4): BMR * 1.725 = Total Calorie Need

Extra active (5): BMR * 1.9 = Total Calorie Need

BMR({"gender": "female",
         "size": 170,
         "weight": 65,
         "age": 25,
         "sport": 5}) →  2801.2
Notes
"""
def BMR(person): 
    
    if person["gender"] == "male":
        BMR = 66.47 + person["size"]*5.003 +person["weight"]*13.75 - person["age"]*6.755
    elif person["gender"] == "female":
        BMR = 655.1 + person["size"]*1.85 +person["weight"]*9.563 - person["age"]*4.676
       
    if person["sport"] == 1:
        return round(BMR*1.2 , 1)
    elif person["sport"] == 2:
        return round(BMR*1.375 , 1)    
    elif person["sport"] == 3:
        return round(BMR*1.55 , 1)
    elif person["sport"] == 4:
        return round(BMR*1.725 , 1)   
    elif person["sport"] == 5:
        return round(BMR*1.9 , 1)    
    
BMR({"gender": "female",
         "size": 170,
         "weight": 65,
         "age": 25,
         "sport": 5}) #→  2801.2  