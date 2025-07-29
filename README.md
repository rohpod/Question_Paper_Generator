# QUESTION PAPER GENERATOR

## It generates questions.

This is a program that outputs the questions in the order desired by the user.

The program uses a text file with the questions in the format:
"subject" | "difficulty" | "question"

Upon a successful run:
1. The program accesses the data in the given text.
2. The program asks the user for questions from a single subject or multiple subjects.
3. The program asks the user for the subjects of the questions to include.
4. The program asks the user for the number of "easy" questions.
5. The program asks the user for the number of "medium" questions.
6. The program asks the user for the number of "hard" questions.
7. The program shuffles and outputs the questions.

_Note:_ If the user inputs more a higher number of questions than present in the file, then the maximum number of questions from the file are generated.