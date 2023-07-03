"""
CP1401 2021-1 Assignment 2
Program 2 - Market Garden Simulator 
Student Name: <Sally Pang Shue Yan>
Date started: <30 Dec 2021>

Pseudocode:

Import random from system

Define value of RAINFALL_MAX, RAINFALL_MIN, RAINFALL_PLANT_DIE
Define original plants list

Funtion main
    display the welcome speech
    display original plants list

    WHILE True
        count number of plant in plants list using len()
        display detail instruction
        display choice and get input from user

        IF choice is q
            the system will break from the loop

        calling all three functions in order to check the conditions

    once the function break from the loop,
    display ending speech including the count day and number of plant that user ended with.

Function determine choice
    IF choice is w
        count day must +1 each time it come in to this choice
        randomly pick a number between RAINFALL_MAX and RAINFALL_MIN
        display the random number

        IF random number less than RAINFALL_PLANT_DIE
            from the plants list randomly pick one plant
            delete the randomly picked plant
            display which plant has died

        ELSE
            FOR plant in plants
                calculate the food amount for each plant
                display the food amount for each plant
                sum up all the food amount values

    ELIF choice is a
        get a new plant name from user

            while the name of new plant already in the current plants list 
                display You already have the plant
                ask for a new plant name from user

            calculate plant price by calculating the length of new plant name

            IF total food amount less than plant price
                display the new plant name and plant price saying with the current total food amount user is not able to purchase the new plant

            ELSE
                add the new plant in the plants list
                calculate the new total food amount

    return count day and total food amount in order to update the values to the main function


Function displaying plants
    IF choice is d
        display all plants from the plants list

    return choice making sure all plants including the new plants are in the list


Function invalid choice
    IF choice is not a, w, d, q
        display invalid choice

    return choice make sure the system checks the conditions


call the main function 

"""



import random 

RAINFALL_MAX = 100
RAINFALL_MIN = 0
RAINFALL_PLANT_DIE = 30

plants = ["Parsley", "Sage", "Rosemary", "Thyme"] #original plant list


def main():
    
    '''Ensure count_day & total_food_amount start counting from 0.'''
    
    count_day = 0 
    total_food_amount = 0

    print('''Welcome to the Market Garden Simulator
Plants cost and generate food according to their name length (e.g., Sage plants cost 4). 
You can buy new plants with the food your garden generates. 
You get up to 100 mm of rain per day. Not all plants can survive with less than 30. 
Let's hope it rains... a lot! 
You start with these plants:''')
    print(*plants, sep=", ", end=",") #listing all plants from the list 
    print()
    while True:
        
        plant_number = len(plants) #count number of plant in plants list
        print(f"After {count_day} days, you have {plant_number} plants and your total food is {total_food_amount}.")
        choice = str(input("(W)ait \n(D)isplay plants \n(A)dd new plant \n(Q)uit \nChoose: ")).lower() 

        if choice == "q":
            break; 

        '''Define all functions to keep the system/ value eg. plants in list, count day updated.'''
        
        invalid_choice(choice) 
        count_day, total_food_amount, = determine_choice(choice, count_day, total_food_amount)
        choice = displaying_plants(choice)


    '''Display exit speech.'''
    
    print(f"You finished with {plant_number}.")
    print(f"After {count_day} days, you have {plant_number} plants and your total food is {total_food_amount}.")
    print("Thank you for simulating. Now go and enjoy a real garden.")


def determine_choice(choice, count_day, total_food_amount):
    
    '''Display a random number as the Rainfall value.'''
    
    if choice == "w":
        count_day += 1 #one entry in this choice, count day will increase by 1 
        rainfall_guess = random.randint(RAINFALL_MIN, RAINFALL_MAX) 
        print(f"Rainfall: {rainfall_guess}mm")

        if rainfall_guess < RAINFALL_PLANT_DIE:
            random_plant_index = random.randint(0, len(plants) - 1) #choosing a random plant from the plants list 
            print(f"Sadly, your {plants[random_plant_index]} plants has died.")
            del plants[random_plant_index] #delete a random plant from the plants list 
            rainfall, food_amount = food(plants, rainfall_guess, total_food_amount)
        
        else:
            rainfall, food_amount = food(plants, rainfall_guess, total_food_amount)
        
        total_food_amount += food_amount

    elif choice == "a":

        '''Get new plant as input from user then check the condition to proceed to the next step.'''
        
        new_plant = str(input("Enter plant name: ")).lower().title()
        
        while new_plant == "" or new_plant in plants:
            if new_plant == "":
                print("Invalid plant name")
            elif new_plant in plants:
                print(f"You already have a {new_plant} plant.")
            new_plant = str(input("Enter plant name: ")).lower().title()

        plant_price = len(new_plant) #calculate the length of new plant name as the plant price 
        if total_food_amount < plant_price: 
            print(f"{new_plant} would cost {plant_price} food. With only {total_food_amount}, you can't afford it.")
        else:
            plants.append(new_plant) #insert the new plant name in the plants list 
            total_food_amount = total_food_amount - plant_price 

    return count_day, total_food_amount  


def displaying_plants(choice):
    
    '''Display plants list including the new plants (if there is).'''
    
    if choice == "d": 
        print(*plants, sep=", ", end = ",\n") 

    return choice 


def invalid_choice(choice):
    
    '''Determine the invalid choice. '''
    
    if choice != "a" and choice != "w" and choice != "d" and choice != "q":
        print("Inavlid choice")

    return choice 

def food(plants, rainfall_guess, total_food_amount):
    
    '''Calculate the food amount for each plant in the plants list then sum all the values of food amount.'''
    
    total_food_amount = 0
    
    for plant in plants:
        if plant == plants[-1]:
            food_amount = int(random.uniform(0.5 * rainfall_guess, rainfall_guess) / 100 * len(plant))
            print(plant, "produced", food_amount, end=",\n")
        else:
            food_amount = int(random.uniform(0.5 * rainfall_guess, rainfall_guess) / 100 * len(plant))
            print(plant, "produced", food_amount, end=", ")
        total_food_amount += food_amount

    return rainfall_guess, total_food_amount

main() 



