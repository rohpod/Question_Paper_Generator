import random

def main():
    print("Welcome to the Question Paper Generator!")
    
    # Opening the file
    filename = "example.txt"
    questions = openfile(filename)
    if not questions:
        return
    
    # Display available subjects
    subs = sorted(set(q["sub"] for q in questions))
    print(f"\nAvailable Subjects: {', '.join(subs)}")
    
    # User choice for single-subject or mixed-subjects
    sub_choice = input("Do you want mixed questions from different subjects? (yes/no): ").strip().lower()
    if sub_choice not in ["yes", "no"]:
        print("Invalid choice.")
        return
    
    if sub_choice == "no":
        # User choice for single-subject
        selected_sub = input(f"Enter the subject (choose from {', '.join(subs)}): ").strip().lower()
        if selected_sub not in subs:
            print("Invalid choice.")
            return
        selected_sub = [selected_sub]
    else:
        # User choice for mixed-subjects
        selected_sub = input("Enter subjects (comma-separated): ").split(',')
        selected_sub = [sub.strip().lower() for sub in selected_sub if sub.strip() in subs]
        if not selected_sub:
            print("No valid subjects selected.")
            return
    
    # User input for question counts by level
    try:
        num_easy = int(input("How many Easy questions do you want? "))
        num_med = int(input("How many Medium questions do you want? "))
        num_hard = int(input("How many Hard questions do you want? "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return
    
    # Generate question paper
    question_paper = generate_question_paper(questions, num_easy, num_med, num_hard, selected_sub)
    
    if not question_paper:
        print("No questions match your criteria.")
        return
    
    # Display the question paper
    print("\nGenerated Question Paper:\n")
    i = 1
    for  question in question_paper:
        print(f"{i}. {question['question']} ({question['sub']}, {question['level']})")
        i += 1


# Opening the file containing questions
def openfile(filename):
    questions = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    sub, level, question = line.strip().split('|')
                    questions.append({"sub": sub.strip().lower(), "level": level.strip().lower(), "question": question.strip().lower()})
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    return questions


# Filter questions by subject and level
def filter_questions(questions, selected_sub, level):
    filtered = [
        q for q in questions
        if q["sub"] in selected_sub and q["level"].lower() == level.lower()
    ]
    return filtered


# Generating a question paper with user specifications
def generate_question_paper(questions, num_easy, num_med, num_hard, selected_sub):
    easy_questions = filter_questions(questions, selected_sub, "Easy")
    medium_questions = filter_questions(questions, selected_sub, "Medium")
    hard_questions = filter_questions(questions, selected_sub, "Hard")
    
    if num_easy > len(easy_questions):
        print(f"Not enough Easy questions available. Using {len(easy_questions)} instead of {num_easy}.")
        num_easy = len(easy_questions)
    if num_med > len(medium_questions):
        print(f"Not enough Medium questions available. Using {len(medium_questions)} instead of {num_med}.")
        num_med = len(medium_questions)
    if num_hard > len(hard_questions):
        print(f"Not enough Hard questions available. Using {len(hard_questions)} instead of {num_hard}.")
        num_hard = len(hard_questions)
    
    selected_easy = random.sample(easy_questions, num_easy)
    selected_medium = random.sample(medium_questions, num_med)
    selected_hard = random.sample(hard_questions, num_hard)
    
    question_paper = selected_easy + selected_medium + selected_hard
    random.shuffle(question_paper)
    return question_paper


if __name__ == "__main__":
    main()