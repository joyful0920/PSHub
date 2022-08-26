//import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = Integer.parseInt(sc.nextLine());
		for (int tc = 1; tc <= t; tc++) {
			int n = Integer.parseInt(sc.nextLine());
			
			ArrayList<Integer>[] farm = new ArrayList[n];
			for (int i = 0; i < n; i++) {
				farm[i] = new ArrayList<Integer>();
				for (String num : sc.nextLine().split("")) {
					farm[i].add(Integer.parseInt(num));
				}
			}
			
			int result = 0;
			int m = n / 2;
			for (int i = 0; i < n - m; i++) {
				for (int j = m - i; j < n - m + i; j++) {
					result += farm[i].get(j);
				}
			}
			for (int i = n - 1; i >= n - m; i--) {
				for (int j = i - m; j < n + m - i; j++) {
					result += farm[i].get(j);
				}
			}
			
			System.out.printf("#%d %d%n", tc, result);
		}
	}
}