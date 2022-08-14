import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		String[] grades = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"};
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			int[][] points = new int[n][3];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < 3; j++) {
					points[i][j] = sc.nextInt();
				}
			}
			
			Double[] students = new Double[n];
			double target = 0;
			for (int i = 0; i < n; i++) {
				students[i] = points[i][0] * 0.35 + points[i][1] * 0.45 + points[i][2] * 0.20;
				if (i == k - 1) {
					target = students[i];
				}
			}
			
			Arrays.sort(students, Collections.reverseOrder());
			int idx = 0;
			for (int i = 0; i < n; i++) {
				if (students[i] == target)
					idx = i;
			}
			
			System.out.printf("#%d %s%n", tc, grades[idx / (n / 10)]);
		}
			
	}

}