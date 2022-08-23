//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int[] coins = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int money = sc.nextInt();
			int[] cnts = new int[8];
			
			for (int i = 0; i < 8; i++) {
				if (money >= coins[i]) {
					cnts[i] = money / coins[i];
					money %= coins[i];
				}
			}
			
			System.out.printf("#%d%n", tc);
			for (int cnt : cnts) {
				System.out.print(cnt + " ");
			}
			System.out.println();
			
		}
	}

}