import re

with open("input.txt", 'r') as file:
    lines = file.readlines()


def max_and_sum_of_valid_games():
    valid_game_ids_sum = 0

    for line in lines:
        match_game = re.match(r'Game (\d+):', line)
        game_id = int(match_game.group(1))

        game_max_blue = 0
        game_max_green = 0
        game_max_red = 0

        blue_matches = list(map(int, re.findall(r'(\d+) blue', line)))
        green_matches = list(map(int, re.findall(r'(\d+) green', line)))
        red_matches = list(map(int, re.findall(r'(\d+) red', line)))

        if blue_matches:
            game_max_blue = max(game_max_blue, max(blue_matches))
        if green_matches:
            game_max_green = max(game_max_green, max(green_matches))
        if red_matches:
            game_max_red = max(game_max_red, max(red_matches))

        if game_max_red <= 12 and game_max_green <= 13 and game_max_blue <= 14:
            valid_game_ids_sum += game_id

    return valid_game_ids_sum


print(f"Part 1: {max_and_sum_of_valid_games()}")


def min_and_sum_of_games():

    total_power = 0

    for line in lines:
        blue_matches = list(map(int, re.findall(r'(\d+) blue', line)))
        green_matches = list(map(int, re.findall(r'(\d+) green', line)))
        red_matches = list(map(int, re.findall(r'(\d+) red', line)))

        min_blue = max(blue_matches) if blue_matches else 0
        min_green = max(green_matches) if green_matches else 0
        min_red = max(red_matches) if red_matches else 0

        total_power += min_blue * min_green * min_red

    return total_power


print(f"Part 2: {min_and_sum_of_games()}")
