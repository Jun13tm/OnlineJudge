# Commands
- codefind "question number"
- codekey "company_name, topic, difficulty" 
- codenote
- template (in current directory)

# Keys
- star(bookmarked)
- easy/medium/hard
- topics
- facebook

# Topics
- array
- math
- stack
- two_pointers
- overflow
- string
- linkedlist
- interval
- sort
- dp

# Algorithm Tips
## Two Pointers
- 快慢指针 <br>
Q26: 快指针负责explore，慢指针负责修改。<br/>
Q28: 1号指针找到第一个match后，2号指针负责loop needle。<br/>
Q??: 在linkedlist相关题中，用慢指针确定mid node的位置。<br/>
- 前后指针 <br>
Q9: 前指针指向index 0，后指针指向index len-1，用while i < j来loop整个list/string. <br>

## Linkedlist
- Always use a dummy node (so head doesn't need to be handled specifically) <br>
- while curr vs. while curr.next <br>
请考虑算法如何handle最后几个Node，两者没有很大的区别。<br>
Q82: sol1 vs. sol2 <br>


# Python Tips
## Logrithm
- math.log(a, Base) <br>
Q67: decimal -> binary <br/>

## String and list
- str.join(list): require list to only contain strings <br>
Q67: decimal -> binary (good example) <br/>

## For-loop
- for i in reversed(range(5)) <br>
-> 4, 3, 2, 1, 0
- 