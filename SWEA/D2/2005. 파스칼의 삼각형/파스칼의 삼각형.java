import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			int[][] arr = new int[n][n];
			
			System.out.printf("#%d%n", tc);
			for (int i = 0; i < n; i++) {
				if (i == 0) { 
					arr[0][0] = 1;
					System.out.println("1");
				}
				else {
					for (int j = 0; j < i + 1; j++)  {
						if (j == 0) {
							arr[i][j] = 1;
							System.out.print("1 ");
						} else if (j == i) {
							arr[i][j] = 1;
							System.out.printf("1%n");
						}
						else {
							arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
							System.out.printf("%d ", arr[i][j]);
						}
					}
				}
			}
		}
	}

}
