import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        Stack<Character> stack = new stack<Character>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{')
                stack.push(c);
            else {
                if (!stack.empty() && map.get(c) == stack.peek())
                    stack.pop();
                else
                    return false;
            }
        }
        if (stack.empty()) 
            return false;
        return true;
    }
}