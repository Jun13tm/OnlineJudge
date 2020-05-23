'''
	• Complexity: 
		○ O(num_moves) - constant time operation for each move
	• Topics: 
		○ system_design
直接看代码，有几个edge cases要handle:
	1. board太大，构建会TLE，用set()存被occupied的coordinates instead
	2. 蛇要前进的为止刚好是蛇的尾巴，这种情况不算触碰身体，因为等蛇头移动以后，蛇尾会离开那个位置
	3. 常规移动时需要先把尾巴的位置remove出occupied set，再重新把头的位置add进occupied set。避免某个位置没有成功没mark
	4. 食物出现在蛇身上是没问题的，不影响游戏
	5. 蛇向上行的时候按下会被Collide with body给handle掉，不需要额外handle
	6. 如果食物吃完了，设置当前食物的坐标为(-1, -1)
'''
from collections import deque

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height should be greater than 0")
        self.width = width
        self.height = height
        # given board can be extremely big, for example: 10000*10000 - one of the test case, causing TLE
        # therefore, use set((x,y)) to mark occupied locations instead
        # self.board = [[0 for _ in range(width)] for _ in range(height)] - discarded
        self.occupied = set()
        self.foods = food
        self.score = 0
        self.body = deque()
        self.directions = {'U':(-1, 0), 'L':(0, -1), 'R':(0, 1), 'D':(1, 0)}
        
        self.body.append((0, 0))
        self.occupied.add((0, 0))
        
    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x, y = self.body[-1]
        dx, dy = x + self.directions[direction][0], y + self.directions[direction][1]
        if len(self.foods) > 0:
            food = self.foods[0]
        else:
            # no food
            food = [-1, -1]
        # if collides with border
        if not 0 <= dx < self.height or not 0 <= dy < self.width:
            return -1
        # if collides with body, edge case: tail moves first, then head moves, i.e ok if (dx,dy) = tail coordinates
        elif (dx, dy) in self.occupied and self.body[0] != (dx, dy):
            return -1
        # if eats food
        elif dx == food[0] and dy == food[1]:
            self.body.append((dx, dy))
            self.occupied.add((dx, dy))
            self.foods.pop(0)
            self.score += 1
            return self.score
        # regular move, edge case: unmark tail first, then mark head location as occupied
        else:
            popped_x, popped_y = self.body.popleft()
            self.occupied.remove((popped_x, popped_y))
            self.body.append((dx, dy))
            self.occupied.add((dx, dy))

            return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)