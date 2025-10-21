'Quiz'


def trivQ():
    question = ["What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\n(d) Rome\n",
                "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n",
                "What is the largest planet in our solar system?\n(a) Earth\n(b) Mars\n(c) Jupiter\n(d) Saturn\n"]

    print(question[0])

    ipunt_srt = input("your awnser is: ")

    if ipunt_srt.lower() == 'c':
        print("Correct!")
    else:
        print("incorect, the correct awser is (c) Paris.")
    SystemExit

    print("\n", question[1])

    ipunt2 = input("your awnser is: ")

    if ipunt2.lower() == "b":
        print("Correct!")
    elif int(ipunt2) == 4:
        print("While this this is true, we please advise you to use the given options to respond to our questions accordingly sur as : a b c and d")
    else:
        print("False")
    SystemExit

    print(question[2])

    input4 = input("you awnser is: ")

    if input4 == 'c':
        print("Congratulations, thats right, you have  completed the quiz!")
    else:
        print("You awser is ", input4,
              "That is false, the correct awnser was c. Good luck next time")
    SystemExit
