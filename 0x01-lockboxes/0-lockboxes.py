#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    b_keys = set()
    b_unopened = set()
    for j in range(2):
        for i in range(len(boxes)):
            if i == 0:
                b_keys.update(boxes[0])
            else:
                if i in b_keys:
                    b_keys.update(boxes[i])
                elif j == 1:
                    b_unopened.update([i])
    return len(b_keys & b_unopened) == len(b_unopened)


if __name__ == "__main__":
    canUnlockAll([[1], [0]])
