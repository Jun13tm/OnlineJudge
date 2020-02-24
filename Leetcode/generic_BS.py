#!/usr/bin/python
# -*- coding: utf-8 -*-
def BS(li, target):
    front, end = 0, len(li) - 1
    while front <= end:
        mid = (front + end) // 2
        if li[mid] == target:
            return mid
        elif li[mid] > target:
            end = mid - 1
        else:
            front = mid + 1
    # loop ends naturally，target not found
    return -1 

if __name__ == "__main__":
    test = [1, 2, 6, 7, 8]
    target = 8
    print(BS(test, target))

    test = [1, 2, 6, 7, 8]
    target = 9
    print(BS(test, target))