import re


def extract_key_values(key_values_str):
    key_values = key_values_str.split()
    return [key_value.split(':')[0] for key_value in key_values], [key_value.split(':')[1] for key_value in key_values]


def validate_presence_of(required_fields, passport_fields):
    return all(required_field in passport_fields for required_field in required_fields)


def validate_passport(required_fields, passport_data):
    passport_keys, passport_values = extract_key_values(passport_data)
    passport = dict(zip(passport_keys, passport_values))

    return validate_presence_of(required_fields, passport_keys) \
        and validate_byr(passport['byr']) \
        and validate_iyr(passport['iyr']) \
        and validate_eyr(passport['eyr']) \
        and validate_hgt(passport['hgt']) \
        and validate_hcl(passport['hcl']) \
        and validate_ecl(passport['ecl']) \
        and validate_pid(passport['pid'])


def validate_byr(value):
    return 1920 <= int(value) <= 2002


def validate_iyr(value):
    return 2010 <= int(value) <= 2020


def validate_eyr(value):
    return 2020 <= int(value) <= 2030


def validate_hgt(value):
    if 'cm' in value:
        return 150 <= int(value.strip('cm')) <= 193
    elif 'in' in value:
        return 59 <= int(value.strip('in')) <= 76
    else:
        return False


def validate_hcl(value):
    return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)


def validate_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(value):
    return value.isdigit() and len(value) == 9


with open('inputs.txt', 'r') as file:
    content = file.read().split('\n\n')

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passports_with_required_fields = [
        key_values_str
        for key_values_str in content
        if validate_presence_of(required_fields, extract_key_values(key_values_str)[0])
    ]

    print(len(passports_with_required_fields))

    valid_passports = [
        key_values_str
        for key_values_str in content
        if validate_passport(required_fields, key_values_str)
    ]

    print(len(valid_passports))

