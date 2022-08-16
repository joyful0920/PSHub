//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();

			int[][] nums = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					nums[i][j] = sc.nextInt();
				}
			}

			System.out.printf("#%d%n", tc);

			for (int m = 0; m < n; m++) {
				for (int i = n - 1; i >= 0; i--) {
					System.out.print(nums[i][m]);
				}
				System.out.print(" ");

				for (int j = n - 1; j >= 0; j--) {
					System.out.print(nums[n - m - 1][j]);
				}
				System.out.print(" ");

				for (int i = 0; i < n; i++) {
					System.out.print(nums[i][n - m - 1]);
				}
				System.out.println();
			}
		}
	}

}
