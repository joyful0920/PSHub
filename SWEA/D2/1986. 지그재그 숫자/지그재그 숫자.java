import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc= 1; tc <= t; tc++) {
			int n = sc.nextInt();
			if (n % 2 == 0) {
				int result = -(n / 2);
				System.out.printf("#%d %d%n", tc, result);
			} else {
				int result = n - ((n - 1) / 2);
				System.out.printf("#%d %d%n", tc, result);
			}
		}
	}

}