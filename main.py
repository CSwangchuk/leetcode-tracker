from helpers import add_problems, summary, topic_breakdown, view_all, search, delete_problem, edit_problem, is_valid
# this is the main menu of the tracker 
def menu():
    while True:
        print("")
        print("*** LeetCode Tracker ***")
        print("""
    1.Add a new problem
    2.View Summary
    3.View Topic Breakdown
    4.View All Problems
    5.Search by Title
    6.Delete Problem
    7.Edit Problem
    8.Quit""")
        print("")

        choice = input("Please enter your choice: ")

        if choice == "1":
            title = input("What is the title of the problem : ")
            difficulty = input("What is the difficulty (Easy / Medium / Hard): ")
            if not is_valid(difficulty, ["Easy", "Medium", "Hard"]):
                print("Invalid difficulty, please try again")
            else:
                topic = input("What topic is the problem related to : ")
                date_solved = input("When did you solve this problem: ")
                add_problems(title, difficulty, topic, date_solved)
                print("The problem has been added!")
        elif choice == "2":
            summaries = summary()
            print("=== Summary ===")
            for key,value in summaries.items():
                print(f"{key}: {value}")
        elif choice == "3":
            ans = topic_breakdown()
            print("=== Topic Breakdown ===")
            for key,value in ans.items():
                print(f"{key}: {value}")
        elif choice =="4":
            view_all()
        elif choice =="5":
            user_input= input("Please input the title of the problem : ")
            ans = search(user_input)
            for i,elem in enumerate(ans):
                print(f"{i+1}.")
                for key,value in elem.items():
                    print(f"{key}: {value}")
                print("")
            if not ans:
                print("No title found by that name, please try a vaild title")
        elif choice == "6":
            user_choice = input("Please enter the title of the problem you want to delete : ")
            delete_problem(user_choice)
        elif choice == "7":
            ask = input("Enter the title of the problem you would like to edit : ")
            print("What would you like to edit? (title / difficulty / topic / date_solved)")
            target = input("Enter field: ")   
            valid_fields = ["title", "difficulty", "topic", "date_solved"]
            if not is_valid(target,valid_fields):
                print("Invalid field, please try again")
            else:
                if target == "difficulty":
                    change = input ("What is the new change : ")
                    if not is_valid(change,["Easy","Medium","Hard"]):
                        print("Invalid difficulty option,please try again")
                    else:
                        edit_problem(ask,target, change)
                else:
                    change = input ("What is the new change : ")
                    edit_problem(ask,target, change)
        elif choice =="8":
            print("Thank you for using the tracker, Goodbye")
            break
        else:
            print("invalid input, please try again with a valid input")


menu()

            

