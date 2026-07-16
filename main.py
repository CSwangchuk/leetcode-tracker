import json
import os 
def save_problems(problems):
    with open("problems.json", "w") as f:
        json.dump(problems,f)

def load_problems():
    if os.path.exists("problems.json"):
        with open("problems.json", "r") as f:
            data = json.load(f)
            return data
    else:
        return []
def add_problems(title,difficulty,topic,date_solved):
    my_problems = load_problems()
    new_problem = {
        "title": title,
        "difficulty": difficulty,
        "topic": topic,
        "date_solved": date_solved
    }
    my_problems.append(new_problem)
    save_problems(my_problems)
def summary():
    problems = load_problems()
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for problem in problems:
        if problem["difficulty"].lower() == "easy":
            counts["Easy"] += 1
        elif problem["difficulty"].lower() == "medium":
            counts["Medium"] += 1
        else:
            counts["Hard"] += 1
    return counts

def topic_breakdown():
    problems = load_problems()
    topic_counts  = {}
    for problem in problems:
        topic = problem["topic"]
        if topic in topic_counts:
            topic_counts[topic]+=1
        else:
            topic_counts[topic]=1
    return topic_counts



def menu():
    while True:
        print("""
        1.Add a new problem
        2.View Summary
        3.View Topic Breakdown
        4.Quit""")

        choice = input("Please enter your choice: ")

        if choice=="1":
            title = input("What is the title of the problem : ")
            difficulty = input("What is the difficulty level of the problem: ")
            topic = input("What topic is the problem related to : ")
            date_solved = input("When did you solve this problem")
            add_problems(title,difficulty,topic,date_solved)
            print("The problem has been added!")
        elif choice == "2":
            summaries = summary()
            print(summaries)
        elif choice == "3":
            ans = topic_breakdown()
            print(ans)
        elif choice =="4":
            print("Thank you for using the tracker, Goodbye")
            break
        else:
            print("invalid input, please try again with a valid input")
            

menu()