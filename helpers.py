import json
import os 
# these are the helper methods for the tracker 

# this method saves the problems in the json file 
# overwrites the files if not used correctly
def save_problems(problems):
    with open("problems.json", "w") as f:
        json.dump(problems, f, indent=4)

#this method reads the json file and returns the content in it 
def load_problems():
    if os.path.exists("problems.json"):
        with open("problems.json", "r") as f:
            content = f.read()
            if content.strip() == "":
                return []
            else:
                data = json.loads(content)
                return data
    else:
        return []
    
# this method adds the problem to the json file 
def add_problems(title,difficulty,topic,date_solved):
    my_problems = load_problems()
    if not is_valid(difficulty,["Easy","Medium","Hard"]):
        print("Invalid difficulty, please enter Easy, Medium, or Hard")
        return
    new_problem = {
        "title": title,
        "difficulty": difficulty,
        "topic": topic,
        "date_solved": date_solved
    }
    my_problems.append(new_problem)
    save_problems(my_problems)

# returns the number of problems having various difficulty level
# uses dictionary
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

# returns the number of problems having similar topic, counts how many problems have the same topic 
# uses dictionary(frequency mapping/key-value)
def topic_breakdown():
    problems = load_problems()
    topic_counts  = {}
    for problem in problems:
        topic = problem["topic"].lower()
        if topic in topic_counts:
            topic_counts[topic]+=1
        else:
            topic_counts[topic]=1
    return topic_counts

# prints all the problems in the json file
def view_all():
    index = 1
    problems = load_problems()
    for problem in problems:
        print(f"{index}.")
        for key,value in problem.items():
            print(f"{key}: {value}")
        
        print("")
        index+=1

# searches for the problem by the title, partial and full searches both work 
def search(target):
    problems = load_problems()
    matches = []
    for problem in problems:
        if target.lower() in problem["title"].lower():
            matches.append(problem)
    return matches
  
# deletes a problem from the json file(overwrites the json file without the specific problem)
def delete_problem(target):
    problems = load_problems()
    new_problem = []
    org_len = len(problems)
    for problem in problems:
        if target.lower() != problem["title"].lower():
            new_problem.append(problem)
    new_len = len(new_problem)
    if new_len<org_len:
        print(f"{target} has been deleted")
        save_problems(new_problem)
    else:
        print(f"No problem with the title '{target}' was found")

# lets user make further edits to the problem 
# (checks for the title since title is the only differentiating factor)
# (if title matches enters in the problem and goes to the target and makes the changes )
def edit_problem(problem_title,target,change):
    problems = load_problems()
    changed = False
    if not is_valid(target,["title", "difficulty", "topic", "date_solved"]):
        print("Invalid option please try again")
        return
    if target == "difficulty" and not is_valid(change, ["Easy", "Medium", "Hard"]):
        print("Invalid difficulty, please enter Easy, Medium, or Hard")
        return
    for problem in problems:
        if problem_title.lower()== problem["title"].lower():
            problem[target] = change
            changed = True
    if changed:
        save_problems(problems)
        print("Change has been made")
    else:
        print("Nothing has changed")

def is_valid(value,valid_options):
    return value in valid_options



