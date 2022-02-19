from typing import List


class Guest:
    def __init__(self, index: int, next_: "Guest" = None):
        self.index = index
        self.next_ = next_


class Solution:
    def guest_sum(self, guest: Guest):
        count = 0

        while True:
            if guest.next_:
                count += 1
                guest = guest.next_
                continue
            break

        return count

    def maximumInvitations(self, favorite: List[int]) -> int:
        handled_guests = {}
        head_guest = Guest(0)
        next_guest = head_guest

        while True:
            if next_guest in handled_guests:
                break

            handled_guests[next_guest.index] = True
            fav = favorite[next_guest.index]
            guest = Guest(fav)
            next_guest.next_ = guest
            next_guest = guest

        return self.guest_sum(head_guest)


if __name__ == '__main__':
    tests = [
        [[2, 2, 1, 2], 3],
        [[1, 2, 0], 3],
        [[3, 0, 1, 4, 1], 4]
    ]
