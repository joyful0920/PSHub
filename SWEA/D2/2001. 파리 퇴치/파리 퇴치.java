import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[][] arr = new int[n][n];
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			int max_sum = 0;
			for (int i = 0; i < n - m + 1; i++) {
				for (int j = 0; j < n - m + 1; j++) {
					int temp = 0;
					for (int x = i; x < i + m; x++) {
						for (int y = j; y < j + m; y++) {
							temp += arr[x][y];
						}
					}
					if (temp > max_sum)
						max_sum = temp;
				}
			}
			
			System.out.printf("#%d %d%n", tc, max_sum);
		}
	}

}
