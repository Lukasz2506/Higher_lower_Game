# 100 Days of code, Dr Angela Yu,
# Higher, Lower Game project
# Student: Łukasz Świątek Brzeziński
# My own workshop (my assumption was to omit choice function application. 



from art import logo, vs
import random 



print(logo) #display game name


def guess_values(data): #gives list contains two random indexes from your list
    '''takes a list contains of dictionaries
    and gives a new random list with only two dictionaries.
    '''
    random_number1 = 0
    random_number2 = 0
    while random_number1 == random_number2:
        random_number1 = random.randint(0, len(data) - 1)
        random_number2 = random.randint(0, len(data) - 1)
    return [data[random_number1], data[random_number2]]


#A Characters

data = [
    {"name" : "Robert Lewandowski",
     "followers_no" : 999999,
     "describtion" : "Footballer",
     "country" : "Poland",},
    
  {"name" : "Garcian Rostocki",
     "followers_no" : 100,
     "describtion" : "Comic",
     "country" : "Poland",},

    {"name" : "Kurt Cobain",
     "followers_no" : 1500000,
     "describtion" : "Musician",
     "country" : "USA",},

    {"name" : "Marcin Surowiec",
     "followers_no" : 1500,
     "describtion" : "Buschcraftowy",
     "country" : "Poland",},

    ]





print("???WHO IS MOST FAMOUS???\n")

def game():
    score = 0
    game_loop = True

    while game_loop:

        attr_list = guess_values(data) #gives two random indexes from data list

        guy1 = attr_list[0]["name"] #Charater name from dict for the first argument from an attr_list 
        followers1 = attr_list[0]["followers_no"] #Charater followers_no from dict for the first argument from an attr_list
        describtion1 = attr_list[0]["describtion"] #Charater describtion from dict for the first argument from an attr_list
        country1 = attr_list[0]["country"] #Charater country from dict for the first argument from an attr_list
        print("\n")
        print(f"----- Character A: {guy1}, {describtion1}, {country1} -----")

        print(vs)

     
        guy2 = attr_list[1]["name"]
        followers2 = attr_list[1]["followers_no"] 
        describtion2 = attr_list[1]["describtion"]
        country2 = attr_list[1]["country"]

        print("\n")
        print(f"----- Against character B: {guy2}, {describtion2}, {country2} -----\n")

        guess_who = input(f"  ☺️Guess which of them has more followers on ☺\n   instagram {guy1} vs {guy2}? >>> ").title()

        if guess_who == guy1:
            if followers1 > followers2:
                print("😁😁😁 Well done. You're right!!! 😁😁😁")
                score += 1
                print(f"Your Score is {score}.")
            else:
                print("😭😭😭 Oh no! You're wrong. You lose!!! 😭😭😭")
                print(f"Your Score is {score}.")
                game_loop = False
        elif guess_who == guy2:
            if followers2 > followers1:
                print("😁😁😁 Well done. You're right!!! 😁😁😁")
                score += 1
                print(f"Your Score is {score}.")
            else:
                print("😭😭😭 Oh no! You're wrong. You lose!!! 😭😭😭")
                print(f"Your Score is {score}.")
                game_loop = False
        else:
            print("This choice is not possible. Choose one of the Character.")
game()

