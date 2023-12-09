from collections import Counter
from functools import cmp_to_key
import bisect


def card_value(c):
    try:
        c_num = int(c)
    except ValueError:
        if c == "T":
            c_num = 10
        elif c == "J":
            c_num = 11
        elif c == "Q":
            c_num = 12
        elif c == "K":
            c_num = 13
        elif c == "A":
            c_num = 14
        else:
            raise ValueError(f"Unknown card {c}")
    return c_num


def compare_card(c1, c2) -> int:
    c1_num = card_value(c1)
    c2_num = card_value(c2)

    if c1_num == c2_num:
        return 0
    elif c1_num > c2_num:
        return 1
    else:
        return -1


def type(hand):
    max_same = max(hand["counts"].values())

    if max_same == 5:
        return 7
    elif max_same == 4:
        return 6
    elif max_same == 3:
        if 2 in hand["counts"].values():
            return 5
        return 4
    elif max_same == 2:
        num_pairs = Counter(hand["counts"].values())[2]
        if num_pairs == 2:
            return 3
        return 2
    else:
        return 1


def compare_hand(h1, h2) -> int:
    if h1["type"] == h2["type"]:
        for c1, c2 in zip(h1["cards"], h2["cards"]):
            if compare_card(c1, c2) != 0:
                return compare_card(c1, c2)

    return h1["type"] - h2["type"]


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = file.read().splitlines()

    hands = []
    for line in lines:
        cards_str, bid_str = line.split()
        cards = [c for c in cards_str]
        bid = int(bid_str)

        hand = {"cards": cards, "bid": bid}
        hand["raw"] = line
        hand["counts"] = Counter(hand["cards"])
        hand["type"] = type(hand)
        bisect.insort(hands, hand, key=cmp_to_key(compare_hand))

    type = None
    total = 0
    for i, hand in enumerate(hands):
        rank = i+1
        if hand["type"] != type:
            print("")
            type = hand["type"]
        value = rank * hand["bid"]
        print(f"{hand} || {rank} (rank) * {hand['bid']} (bid) = {value}")
        total += value

    print(total)
