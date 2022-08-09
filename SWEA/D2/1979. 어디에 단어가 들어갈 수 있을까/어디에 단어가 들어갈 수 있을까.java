import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int i = 1; i <= t; i++) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			int[][] arr = new int[n][n];
			
			for (int x = 0; x < n; x++) {
				for (int y = 0; y < n; y++) {
					arr[x][y] = sc.nextInt();
				}
			}
			
			int result = 0;
			for (int x = 0; x < n; x++) {
				for (int y = 0; y <= n - k; y++) {
					int cnt = 0;
					for (int z = 0; z < k; z++) {
						if (arr[x][y + z] == 0) {
							break;
						}
						cnt += 1;
					}
					
					if (cnt == k) {
						if (y == 0 || (y > 0 && arr[x][y - 1] == 0)) {
							if (y + k == n || (y + k < n && arr[x][y + k] == 0)) {
								result += 1;
							}
						}
					}
				}
				
			}
			for (int y = 0; y < n; y++) {
				for (int x = 0; x <= n - k; x++) {
					int cnt = 0;
					for (int z = 0; z < k; z++) {
						if (arr[x + z][y] == 0) {
							break;
						}
						cnt += 1;
					}
					
					if (cnt == k) {
						if (x == 0 || (x > 0 && arr[x - 1][y] == 0)) {
							if (x + k == n || (x + k < n && arr[x + k][y] == 0)) {
								result += 1;
							}
						}
					}
				}
				
			}
			
			System.out.printf("#%d %d%n", i, result);
		}
	}

}
