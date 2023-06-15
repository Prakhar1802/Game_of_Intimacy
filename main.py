import random
import time
from Flames import Flame_fun
import win32com.client
from data import Past_questions, Life_questions, Relationship_questions, Intimacy_questions, About_questions, \
    Random_questions


def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def name_loader():
    name = input("Name:")
    return name


def Intro():
    speak("Welcome to the game of Intimacy")
    print("Welcome to the game of Intimacy\n")


def Greeting(name11, name21):
    print(f"\nHello {name11} and {name21}, I am Friday. NPC(Non Player Character), "
          f"Let's find the relationship of you guys using Flames")
    speak(f"Hello {name11} and {name21}, I am Friday, a NPC(Non Player Character)."
          f" Let's find the relationship of you guys, using flames")


def flame_answer(name12, name21):
    answer = Flame_fun(name12, name21)
    print(f"The Relationship between {name12} and {name21} is:{answer}")
    speak(f"The Relationship between {name12} and {name21} is:{answer}")


def Rules():
    speak("Rules of the game.")
    print("Rules of the game\n1.There are 10 questions related to your category choice\n"
          "2.You are allowed to pass two question\n"
          "3.You get the point when the opponent is fully satisfied and give you point\n4.Who get maximum points is "
          "gonna win\n\n")
    speak("There are 10 questions, related to your category choice. You are allowed to pass two questions."
          "You get the point, when the opponent is fully satisfied and give you point. Who get maximum points."
          " is gonna win")


def question_choose(play_player, choice):
    for i in range(1, 10):
        question = random.choice(choice)
        print(f"{play_player}'s question number{i}:{question}")
        speak(f"{play_player}'s question number{i}.:{question}")
        time.sleep(2)
        nxt = input("Are you satisfied?\ny/n\t>>")
        if "n" or "N" in nxt:
            speak(f"{play_player}, not good")
        elif "y" or "Y" in nxt:
            speak("Perfect")
        else:
            print("Invalid input!!!!")
            speak("Invalid input.")


def Player_category_choice(player_1):
    speak("Choose your category to play")
    category_choice = int(
        input("Choose your category.....\nPress 1 for Past\nPress 2 for Relationship\nPress 3 for "
              "Random\nPress 4 for About\nPress 5 for Intimacy\nPress 6 for Life\n>>"))
    if category_choice == 1:
        choice_1 = Past_questions
        print(f"{player_1} choose Past....")
        speak(f"{player_1} choose Past. let's dig something in past guys.")
        question_choose(player_1, choice_1)

    elif category_choice == 2:
        choice_1 = Relationship_questions
        print(f"{player_1} choose Relationship....")
        speak(f"{player_1} choose Relationship. Get Ready for being emotional.")
        question_choose(player_1, choice_1)

    elif category_choice == 3:
        choice_1 = Random_questions
        print(f"{player_1} choose Random....")
        speak(f"{player_1} choose Random. Let's talk random guys.")
        question_choose(player_1, choice_1)

    elif category_choice == 4:
        choice_1 = About_questions
        print(f"{player_1} choose About....")
        speak(f"{player_1} choose About. let's know about{player_1}.")
        question_choose(player_1, choice_1)

    elif category_choice == 5:
        choice_1 = Intimacy_questions
        print(f"{player_1} choose Intimacy....")
        speak(f"{player_1} choose Intimacy. Let's get touchy.")
        question_choose(player_1, choice_1)

    elif category_choice == 6:
        choice_1 = Life_questions
        print(f"{player_1} choose Life....")
        speak(f"{player_1} choose life. Get Ready to know about life guys.")
        question_choose(player_1, choice_1)

    else:
        print("Invalid input!!!!")
        speak("Invalid input.")


def SPS(name2, name4):
    speak(f"{name2} and {name4} Let's get start the fun!!!!")
    print("Let's get start the fun!!!!")
    time.sleep(1)
    print("Play stone paper and scissor and answer the question to continue the game")
    speak("First, You guys play stone paper and scissor to continue the game")
    time.sleep(1)


def Player_Choice():
    speak("Choose with whom you want to play the Intimacy.")
    People_category = input("Choose with whom you play the Intimacy\n1.Press P/p for Parents\n2.Press C/c for "
                            "couples\n3.Press F/f for friends\n>>")

    if People_category == "P" or People_category == "p":
        print("Enter the players name")
        speak("Enter the players name")
        name1 = name_loader()
        name2 = name_loader()
        Greeting(name1, name2)
        player_name = input(f"Who want to give answer first {name1} or {name2}?\n Enter the name:")
        Rules()
        Player_category_choice(player_name)

    elif People_category == "C" or People_category == "c":
        print("Enter the players name")
        speak("Enter the players name")
        name1 = name_loader()
        name2 = name_loader()
        Greeting(name1, name2)
        time.sleep(2)
        flame_answer(name1, name2)
        SPS(name1, name2)
        Staring_Player = input("First name of Stone, Paper and Scissor winner :")
        Rules()
        Player_category_choice(Staring_Player)

    elif People_category == "F" or People_category == "f":
        print("Enter the players name")
        speak("Enter the players name")
        name1 = name_loader()
        name2 = name_loader()
        Greeting(name1, name2)
        time.sleep(2)
        flame_answer(name1, name2)
        SPS(name1, name2)
        Staring_Player = input("First name of Stone, Paper and Scissor winner :")
        Rules()
        Player_category_choice(Staring_Player)

    else:
        print("Invalid input!!!!")
        speak("Invalid input.")


if __name__ == '__main__':
    Intro()
    Player_Choice()
