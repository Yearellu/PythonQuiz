def intro():
    print("Welcome to this completly Normal Quiz, but before we start lets get to know each other.")

    input_name = input("\n Enter your name: ")
    input_age = input("\n Enter your age: ")
    input_sex = input("\n Are you a male or a female: ")

    print("\n")

    if input_sex != "female" and input_sex != "male" :
        SystemExit

    def greetings(name):
        print("Hello " + name)
        

    def age(age):
        print("Your age is", age)
        

    def sex(sex):
        if input_sex == "male":
            print("You are a", input_sex)
            
        elif input_sex == "female":
            print("You are a", input_sex)
            
        else:
            print("You did not enter your proper gender")
            SystemExit

    greetings(input_name)
    print("\n")
    age(input_age)
    print("\n")
    sex(input_sex)
    print("\n")

    list = [input_name, input_age, input_sex]
    print(list)

