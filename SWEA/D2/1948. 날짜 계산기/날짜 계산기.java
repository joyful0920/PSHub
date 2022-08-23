//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("src/swea_d2/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int[] days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int[] dates = new int[4];
			
			for (int i = 0; i < 4; i++) {
				dates[i] = sc.nextInt();
			}
			
			int result = 0;
			for (int i = dates[0]; i < dates[2]; i++) {
				result += days[i];
			}
			
			result = result - dates[1] + dates[3] + 1;
			System.out.printf("#%d %d%n", tc, result);
		}
		
	}

}
