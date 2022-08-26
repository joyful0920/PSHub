//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		while (t >= 1) {
			t--;
			int tc = sc.nextInt();
			
			int[] cnts = new int[101];
			for (int i = 0; i < 1000; i++) {
				cnts[sc.nextInt()]++;
			}
			
			int max_cnts = Integer.MIN_VALUE;
			int result = 0;
			for (int i = 0; i <= 100; i++)
				if (cnts[i] >= max_cnts) {
					max_cnts = cnts[i];
					result = i;
				}
			
			System.out.printf("#%d %d%n", tc, result);
		}
	}
}