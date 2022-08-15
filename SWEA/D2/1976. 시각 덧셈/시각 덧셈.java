import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int h1 = sc.nextInt();
			int m1 = sc.nextInt();
			int h2 = sc.nextInt();
			int m2 = sc.nextInt();
			
			int[] result = new int[2];
			
			result[1] = (m1 + m2) % 60;
			if (m1 + m2 >= 60)
				result[0]++;
			
			result[0] += (h1 + h2);
			if (result[0] > 12) {
				result[0] %= 12;
				if (result[0] == 0)
					result[0] += 12;
			}
			
			System.out.printf("#%d %d %d%n", tc, result[0], result[1]);
		}
	}

}