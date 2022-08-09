import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		int[] nums = new int[10];
		for (int i = 0; i < t; i++) {
			for (int j = 0; j < nums.length; j++) {
				nums[j] = sc.nextInt();
			}
			
			int max_num = 0;
			for (int j = 0; j < nums.length; j++) {
				if (nums[j] > max_num) {
					max_num = nums[j];
				}
			}
			
			System.out.printf("#%d %d%n", i + 1, max_num);
		}
	}

}
