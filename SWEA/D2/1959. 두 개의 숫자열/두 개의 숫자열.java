//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int[] a = new int[n];
			int[] b = new int[m];
			for (int i = 0; i < n; i++) {
				a[i] = sc.nextInt();
			}
			for (int i = 0; i < m; i++) {
				b[i] = sc.nextInt();
			}
			
			int result = Integer.MIN_VALUE;
			for (int i = 0; i < Math.abs(m - n) + 1; i++) {
				int temp = 0;
				for (int j = 0; j < Math.min(n, m); j++) {
					if (n < m) 
						temp += a[j] * b[i + j];
					else
						temp += a[i + j] * b[j];
				}
				if (temp > result)
					result = temp;
			}
			
			System.out.printf("#%d %d%n", tc,  result);
		}

	}

}