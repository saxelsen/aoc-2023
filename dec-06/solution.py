import math

def hold_times(time: int, distance_to_beat: int) -> tuple[int, int]:
    lower_hold_limit = (time - math.sqrt(time**2 - 4*distance_to_beat))/2
    upper_hold_limit = (time + math.sqrt(time**2 - 4*distance_to_beat))/2
    return math.floor(lower_hold_limit + 1), math.ceil(upper_hold_limit - 1)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()

    time_title, time_str = lines[0].split(":")
    times = [int(time) for time in time_str.split()]

    distance_title, distance_str = lines[1].split(":")
    distances = [int(distance) for distance in distance_str.split()]

    permutations = 1
    for time, distance in zip(times, distances):
        hold_range = hold_times(time, distance)
        ways_to_win = hold_range[1] + 1 - hold_range[0]
        permutations *= ways_to_win
    print(permutations)
