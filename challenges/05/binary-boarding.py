def find_seat_position(word_piece, whole_range):
    least, most = whole_range

    for char in word_piece:
        if char in ['F', 'L']:
            least, most = (least, most - int((most - least) / 2) - 1)
        else:
            least, most = least + int((most - least) / 2) + 1, most

    return least


def find_seat_row(word):
    return find_seat_position(word[:7], [0, 127])


def find_seat_column(word):
    return find_seat_position(word[7:], [0, 7])


def calculate_seat_id(row, column):
    return (row * 8) + column


with open('inputs.txt', 'r') as file:
    lines = list(file)

    seat_ids = [
        calculate_seat_id(
            find_seat_row(list(line.strip())),
            find_seat_column(list(line.strip())),
        )
        for line in lines
    ]

    print(max(seat_ids))

    all_possible_seat_ids = [i for i in range(min(seat_ids), max(seat_ids))]
    missing_seat_id = list(set(all_possible_seat_ids) - set(seat_ids)).pop()

    print(missing_seat_id)

