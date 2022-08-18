//import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			
			ArrayList<Integer>[] dp = new ArrayList[n];
			for (int i = 0; i < n; i++) {
				dp[i] = new ArrayList<Integer>();
				for (int j = 0; j <= i; j++) {
					dp[i].add(1);
				}
			}
			
			for (int i = 2; i < n; i++) {
				for (int j = 1; j < i; j++) {
					dp[i].set(j, dp[i - 1].get(j - 1) + dp[i - 1].get(j));
				}
			}
			
			System.out.printf("#%d%n", tc);
			for (int i = 0; i < n; i++) {
				for (int j = 0; j <= i; j++) {
					System.out.printf("%d ", dp[i].get(j));
				}
				System.out.println();
			}
			
		}
	}

}