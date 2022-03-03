print('Welcome to AskPython Quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions = 4

if answer.lower()=='yes':
    answer = input('Question 1: Who is your favourite as a python developer?')
    if answer.lower() == 'hunny':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


    answer = input('Question 2: What is your Favourite programming language?')
    if answer.lower() == 'python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 3: Do you follow hunnypd16@github? ')
    if answer.lower() == 'yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 4: What is the name of your favourite website for learning Python?')
    if answer.lower() == 'hunnyd016.blogspot.com':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thankyou for Playing this small quiz game, you attempted', score, "questions correctly!")
mark = (score / total_questions) * 100
print('Marks obtained:', mark)
print('BYE!')
