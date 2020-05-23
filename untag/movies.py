def sol(li, k):
    # Always exist a valid pair

    k -= 30
    # tup: (length, index)
    li = [(li[i], i) for i in range(len(li))]
    li.sort()
    # max sum
    ma = -1
    # max length of single movie
    # longest = -1
    # valid pairs; be prepared for the edgest case 100,30,30 <= 130
    pair = None

    # two pointers
    # nested for-loop
    ## return index of the valid tuple (movie) -1 if not found
    def search(start, li, target):  
        for i in range(start, len(li)):
            if li[i][0] > target:
                if i == start:
                    return -1
                else:
                    return i - 1
        return len(li) - 1

    for i in range(len(li)):
        if li[i][0] > k / 2 or i == len(li) - 1:
            break
        idx = search(i + 1, li, k - li[i][0])
        if idx == -1:
            break
        su = li[i][0] + li[idx][0]
        if su > ma:
            ma = su
            #longest = li[idx][0]
            pair = [li[i][1], li[idx][1]]
        #if su == ma: # currently ignoring the edgest case
        #    #longest = li[idx][0]
        #    pair = [li[i][1], li[idx][1]]
    return pair

#li = [90, 75, 60, 120, 150, 125, 135, 80]
#d = 245 # looking for 215
li = []


print (sol(li, d))