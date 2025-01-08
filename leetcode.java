import java.util.Arrays;

class leetcode {
    public static int[] twoSum(int[] nums, int target) {
        for (int i =0; i < nums.length; i++) {
            for (int j =i+1; j < nums.length;j++) {
                if (nums[i] + nums[j] == target) {
                    int[] result = new int[]{i,j};
                    Arrays.toString(result);
                    return result;
                    
                }
            }
        }
        return new int[]{};
        
    }

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        System.out.println(twoSum(nums, 9));
    }
}