# exQuizzIt: a quizz program that takes a file with questions and answers, quizzes the user with those questions, and shows a final score at the end.

# Assumptions:
# Every line of the Q&A file is formatted as: The question?|||The answer
# The maximum score is 100, and each question is worth the same amount of points.

""" OUTPUT EXAMPLE:
What is the name of the QA file? quiz1.txt
Question: how many years did it take to build the panama canal?
Your Answer: 10
correct!
what color is the sky?
Enter response: gray
incorrect!
You got 1 out of 2 correct.
Your percentage grade: 50.0%
"""

QA_file_name = input("What is the name of your Questions and Answers file? ")
