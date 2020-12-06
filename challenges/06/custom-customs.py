import functools


def calculate_questions(group_answers):
    answers_by_person = group_answers.split('\n')

    return set("".join(answers_by_person))


def find_answered_by_everyone(group_answers):
    answers_by_person = group_answers.split('\n')
    persons_count = len(answers_by_person)
    all_answers = "".join(answers_by_person)
    answers_count = [[letter, all_answers.count(letter)] for letter in set(all_answers)]
    answered_by_everyone = [answer_count[0] for answer_count in answers_count if answer_count[1] == persons_count]

    return answered_by_everyone


with open('inputs.txt', 'r') as file:
    content = file.read().split('\n\n')
    answered_questions = [len(list(calculate_questions(group_answers))) for group_answers in content]

    print(functools.reduce(lambda a, b: a + b, answered_questions))

    answered_by_everyone = [len(find_answered_by_everyone(group_answers)) for group_answers in content]
    print(functools.reduce(lambda a, b: a + b, answered_by_everyone))
