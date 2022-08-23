//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("src/swea_d2/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			int[] checked = new int[10];
			
			int result = 0;
			int cnt = 1;
			int sum = 0;
			while (sum != 45 || checked[0] == 0) {
				for (String num : String.valueOf(n * cnt).split("")) {
					int i = Integer.parseInt(num);
					
					if (checked[i] == 0) {
						checked[i] = 1;
						sum += i;
					}
				}
				
				cnt++;
				result += n;
			}
			
			System.out.printf("#%d %d%n", tc, result);
		}
	}

}