def BS(li, target):
    low, high = 0, len(li) - 1
    while high >= low:
        mid = int((high + low) / 2)

        if li[mid] == target:
            return mid
        elif li[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


li = [1,2,6,7,9]
target = 9

print (BS(li, target))