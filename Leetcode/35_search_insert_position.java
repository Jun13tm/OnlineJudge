class Solution {
    public static int binarySearch(int[] nums, int target) {
        if (nums.length == 1) {
            if (nums[0] < target) 
                return 1;
            return 0;
        }
        // General case
        int mid = nums.length / 2;
        if (target == nums[mid]) 
            return mid;
        else if (target > nums[mid]) 
            // Should include mid, in case len == 2
            return Solution.binarySearch(Arrays.copyOfRange(nums, mid, nums.length), target) + mid;
        else 
            return Solution.binarySearch(Arrays.copyOfRange(nums, 0, mid), target);  
    }
    
    public int searchInsert(int[] nums, int target) {
        if (nums.length == 0) return 0;
        return Solution.binarySearch(nums, target);
    }
}