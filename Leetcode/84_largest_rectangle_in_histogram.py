'''
84: Largest Rectangle in Histogram Hard
	• Complexity:
		○ O(n); O(n)
	• Topics:
		○ stack
Example:
	heights: [6, 7, 5, 2, 4, 5, 9, 3]
	indices: [0, 1, 2, 3, 4, 5, 6, 7]

这个Algorithm确实比较niche，遇到比stack最后一个柱子要高或一样高的，push进stack。到矮的，pop直到
stack最后一个柱子比现在遇到的这个要矮，再push现在这个柱子进stack。pop过程之中，可以constant时间
计算以被pop出来的这个柱子的height为高的rectangle最大的面积是多少（有点绕，建议用上面这个example
走一遍。）
why this works? 因为stack保持了increasing heights。假设当前的index为i，被pop出来的柱子index
为j，那么j与i之间所有的柱子（如果有），一定比heights[j]这个柱子要高，那么计算以heights[j]为高的
最大面积时，j与i之间的差值，全部要计入长度。for example，i = 7， j = 5，计算的面积应该是 5 x 2 
（即，index 5~6为长）。而j以左的柱子一定比j要矮，忽略。
在Loop完以后清理stack时，stack倒数第二个pair一定是最小的heights，所以用height * len(heights)
去计算area即可。
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        # append -1 for empty comparison, (height, index)
        stack = [(-1, -1)]
        for i in range(len(heights)):
            if heights[i] < stack[-1][0]:
                while stack[-1][0] > heights[i]:
                    height, idx = stack.pop()
                    # tricky part, check comments
                    area = height * (i - stack[-1][1] - 1)
                    largest = max(largest, area)
            stack.append((heights[i], i))
        print(stack)
        # pop rest of the stack
        while len(stack) > 2:
            height, idx = stack.pop()
            area = height * (len(heights) - stack[-1][1] - 1)
            largest = max(largest, area)
        # last element is global min
        height, idx = stack.pop()
        largest = max(largest, height * len(heights))
        return largest