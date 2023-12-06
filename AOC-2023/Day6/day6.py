part1_times = [47, 70, 75, 66]
part1_distances = [282, 1079, 1147, 1062]

part2_times = [47707566]
part2_distances = [282107911471062]


# Part 1
def race(times, distances):
    total_ways = 1

    for time, distance in zip(times, distances):
        ways = 0
        for hold_time in range(time):
            speed = hold_time
            remaining_time = time - hold_time
            total_distance = speed * remaining_time
            if total_distance > distance:
                ways += 1

        total_ways *= ways

    return total_ways


print(f"Part 1: {race(part1_times, part1_distances)}")
print(f"Part 2: {race(part2_times, part2_distances)}")
