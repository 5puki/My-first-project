#This project will be a test to my begginer skills in creating the "Quiz Game" with my own understanding for everything that I have learnt until this point

#-----------------------------
def new_game():
    player_guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print("-----------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i, end=" ")
            print()
        choice = input("Select the letter in front of your answer?: ")
        choice = choice.upper()
        player_guesses.append(choice)

        correct_guess += see_answers(questions.get(key), choice)
        question_num += 1

    see_result(correct_guess, player_guesses)
#-----------------------------
def see_answers(answer, choice):
    if answer == choice:
        print("YOU ARE CORRECT!")
        return 1
    else:
        print("YOU ARE WRONG LIKE JOEY!")
        return 0
#-----------------------------
def see_result(correct_guess, player_guesses):
    print("-----------------------------")
    print("Lets see how Joey has scored!")
    print("-----------------------------")

    print("Correct Answers", end=" ")
    for key in questions:
        print(questions.get(key), end=" ")
    print()

    print("Joey's Guesses", end=" ")
    for i in player_guesses:
        print(i, end=" ")
    print()

    result = int((correct_guess/len(questions))*100)
    print("Joey has scored "+str(result)+"%")
#-----------------------------
def play_again():
    another_one = input("Would you like to play again with Joey? Yes/No: ")
    another_one = another_one.upper()
    while another_one == "YES":
        return True
    else:
        return False
#-----------------------------

questions = {"You put this in your coffee? It's White? It's heavier than milk?": "J",
             "You put this in your sandwich? It's White? It's made from Eggs? ": "H",
             "You put this on a hamburger?": "A"}

options = [["A. Spoon", "B. Your hands", "C. Your face", "D. Paper", "E. Snow", "F. Ghost", "G. Rock", "H. Dog", "I. The Earth", "J. Cream"],
           ["A. Salami", "B. Anchovies", "C. Jam", "D. Paper", "E. Snow", "F. Ghost", "G. Chickens", "H. Mayonnaise"],
           ["A. Ketchup", "B. Relish"]]

print("************************")
print("Welcome to the Pyramid!")
print("************************")
print()
print("Our contestant and the star of popular show Days Of Our Lives, Joey Tribbiani will be answering some questions for us!")
new_game()

while play_again():
    new_game()

print("Goodnight Joey!")