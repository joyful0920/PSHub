import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			int[] nums = new int[n];
			
			for (int i = 0; i < n; i++) {
				nums[i] = sc.nextInt();
			}
			
			long result = 0;
			int max_num = 0;
			for (int i = n - 1; i >= 0; i--) {
				if(nums[i] > max_num)
					max_num = nums[i];
				result += max_num - nums[i];
			}
			
			System.out.printf("#%d %d%n", tc, result);
		}
	}

}
