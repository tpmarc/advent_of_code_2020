def extract_policy(text):
    least_most, letter = text.split(' ')
    least, most = least_most.split('-')

    return {'least': int(least), 'most': int(most), 'letter': letter}


def extract_password_policy(text):
    parts = text.split(':')
    policy = extract_policy(parts[0].strip())
    password = parts[1].strip()

    return {'policy': policy, 'password': password}


def validate_password_by_count(policy, password):
    letter_count = password.count(policy['letter'])

    return policy['least'] <= letter_count <= policy['most']


def validate_password_by_position(policy, password):
    letter_least = password[policy['least'] - 1]
    letter_most = password[policy['most'] - 1]

    return letter_least != letter_most and (letter_least == policy['letter'] or letter_most == policy['letter'])


with open('inputs.txt', 'r') as file:
    lines = list(file)

    valid_passwords_by_count = [
        extract_password_policy(line)
        for line in lines
        if validate_password_by_count(
            extract_password_policy(line)['policy'], extract_password_policy(line)['password']
        )
    ]

    print(len(valid_passwords_by_count))

    valid_passwords_by_position = [
        extract_password_policy(line)
        for line in lines
        if validate_password_by_position(
            extract_password_policy(line)['policy'], extract_password_policy(line)['password']
        )
    ]

    print(len(valid_passwords_by_position))
