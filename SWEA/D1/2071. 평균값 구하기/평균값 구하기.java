import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int i = 1; i <= t; i++) {
			int[] nums = new int[10];
			for (int j = 0; j < 10; j++) {
				nums[j] = sc.nextInt();
			}
			
			float sum = 0, avg = 0;
			for (int j : nums) {
				sum += j;
			}
			
			avg = sum / 10;
			System.out.printf("#%d %d%n", i, Math.round(avg));
		}
	}

}