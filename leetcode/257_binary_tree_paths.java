import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
 * = left; this.right = right; } }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        // DFS with stack
        Stack<Pair<TreeNode, String>> stack = new Stack<Pair<TreeNode, String>>();
        stack.push(new Pair<TreeNode, String>(root, ""));
        List<String> ret = new ArrayList<String>();

        if (root == null)
            return ret;

        while (!stack.isEmpty()) {
            Pair<TreeNode, String> pair = stack.pop();
            TreeNode node = pair.getKey();
            String string = pair.getValue();
            // If leaf
            if (node.left == null && node.right == null)
                ret.add(string + String.valueOf(node.val));
            if (node.right != null)
                stack.push(new Pair<TreeNode, String>(node.right, string + String.valueOf(node.val) + "->"));
            if (node.left != null)
                stack.push(new Pair<TreeNode, String>(node.left, string + String.valueOf(node.val) + "->"));
        }
        return ret;
    }
}