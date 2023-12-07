with open('input.txt') as f:
    cards = [line.strip().split() for line in f.readlines()]

card_strength = 'AKQJT98765432'
card_strength_2 = 'AKQT98765432J'


def calc_strength_part1(hand: str, strength_str=card_strength):
    label_counts = [hand.count(s) for s in hand]
    label_rank = [strength_str.index(s) for s in hand]
    # 1 Five of a kind
    if 5 in label_counts:
        strength = 1
        # 2 Four of a kind
    elif 4 in label_counts:
        strength = 2
    # 3 Full house
    elif 3 in label_counts and 2 in label_counts:
        strength = 3
    # 4 Three of a kind
    elif 3 in label_counts:
        strength = 4
    # 5 Two pair
    elif label_counts.count(2) == 4:
        strength = 5
        # 6 One pair
    elif 2 in label_counts:
        strength = 6
    # 7 High card
    elif label_counts.count(1) == 5:
        strength = 7

    return strength, label_rank


def calc_strength_part2(hand: str, strength_str=card_strength_2):
    # strength=0
    label_counts = [hand.count(s) for s in hand]
    label_rank = [strength_str.index(s) for s in hand]

    Js = hand.count('J')

    # 1 Five of a kind
    if 5 - Js in label_counts or Js == 5:
        strength = 1
        # 2 Four of a kind
    elif (4 - Js in label_counts and Js != 2) or Js == 3 or (Js == 2 and label_counts.count(2) == 4):
        strength = 2
        # 3 Full house
    elif (3 in label_counts and 2 in label_counts) or (Js in range(1, 3) and label_counts.count(2) == 4):
        strength = 3
        # 4 Three of a kin
    elif 3 - Js in label_counts or Js == 2:
        strength = 4
        # 5 Two pair
    elif label_counts.count(2) == 4 or (Js == 1 and 2 in label_counts):
        strength = 5
    # 6 One pair,
    elif 2 in label_counts or Js == 1:
        strength = 6
    # 7 High card
    elif label_counts.count(1) == 5 and Js == 0:
        strength = 7

    return strength, label_rank


for i, hand in enumerate(cards):
    strength, ranks = calc_strength_part2(hand[0])  # calc_strength_part2(hand[0])
    cards[i].append(strength)
    cards[i].append(ranks)

cards = sorted(cards, key=lambda x: (x[2], x[3]), reverse=True)

print(sum([r * int(hand[1]) for r, hand in enumerate(cards, 1)]))