//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("src/swea_d2/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int[] numbers = {2, 3, 5, 7, 11};
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int[] cnts = new int[5];
			int n = sc.nextInt();
			
			for (int i = 0; i < 5; i++) {
				while (n % numbers[i] == 0 && n > 0) {
					cnts[i]++;
					n /= numbers[i];
				}
			}
			
			System.out.printf("#%d ", tc);
			for (int i = 0; i < 5; i++) {
				System.out.print(cnts[i] + " ");
			}
			System.out.println();
		}
	}

}