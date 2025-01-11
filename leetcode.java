import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class leetcode {
        public static int singleNumber(int[] nums) {
        Map<Integer, Integer> dict = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            dict.put(nums[i], dict.getOrDefault(nums[i],0)+1);
        }

        for (Map.Entry<Integer, Integer> entry: dict.entrySet()) {
            if (entry.getKey() == 1) {
                return entry.getKey();
            }
        }

        return 0;

        // time complexity is O(n) because of the for loop;
    }
    // search insert position
    // Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
	// You must write an algorithm with O(log n) runtime complexity.
    public static int searchInsert(int[] nums, int target) {
        // use binary search
        int left = 0;
        int right = nums.length -1;
        int mid = (left + (right - left)) /2;
        while (left < right) {
            if (nums[mid] == target) {
                return mid;
            } else if (nums[left] < target) {
                left = mid +1; 
            } else {
                right = mid -1;
            }
        }
        return left;
    }
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
        int[] nums = {4,1,2,1,2};
        // System.out.println(twoSum(nums, 9));
        // System.out.println(searchInsert(nums, 5));
        singleNumber(nums);
    }
}