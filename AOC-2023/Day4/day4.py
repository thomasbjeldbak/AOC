import re

with open("input.txt", 'r') as file:
    lines = file.readlines()


def card_points():
    points = 0

    for line in lines:
        match = re.match(r'Card\s+(\d+):\s*(.+?)\s*\|\s*(.+)', line)
        if match:
            winning_numbers = list(map(int, match.group(2).split()))
            numbers = list(map(int, match.group(3).split()))

            points_on_card = 0

            for number in numbers:
                if number in winning_numbers:
                    points_on_card = 1 if points_on_card == 0 else points_on_card * 2

            points += points_on_card

    return points


def actual_points():
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]
    return sum(cards)


print(f"Part 1: {card_points()}")
print(f"Part 2: {actual_points()}")
