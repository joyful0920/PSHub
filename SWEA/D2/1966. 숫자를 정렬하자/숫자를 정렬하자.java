// import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			
			int[] nums = new int[n];
			for (int i = 0; i < n; i++) {
				nums[i] = sc.nextInt();
			}
			
			Arrays.sort(nums);
			
			System.out.printf("#%d ", tc);
			for (int i = 0; i < n; i++) {
				System.out.print(nums[i] + " ");
			}
			System.out.println();
		}
	}

}