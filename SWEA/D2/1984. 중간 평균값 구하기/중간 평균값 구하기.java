import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int tc = 1; tc <= t; tc++) {
			int[] nums = new int[10];
			for (int i = 0; i < 10; i++) {
				nums[i] = sc.nextInt();
			}
			
			Arrays.sort(nums);
			int[] temp = Arrays.copyOfRange(nums, 1, nums.length - 1);
			
			float total = 0;
			for (int n : temp) {
				total += n;
			}
			
			int avg = Math.round(total / temp.length);
			
			System.out.printf("#%d %d%n", tc, avg);
		}
	}

}