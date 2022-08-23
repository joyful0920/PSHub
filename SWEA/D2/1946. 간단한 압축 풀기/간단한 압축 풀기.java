//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("src/swea_d2/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = Integer.parseInt(sc.nextLine());
		for (int tc = 1; tc <= t; tc++) {
			int n = Integer.parseInt(sc.nextLine());
			System.out.printf("#%d%n", tc);
			
			int cnt = 0;
			for (int i = 0; i < n; i++) {
				String s = sc.nextLine();
				char ci = s.charAt(0);
				int ki = Integer.parseInt(s.substring(2));
				
				for (int j = ki; j > 0; j--) {
					if (cnt == 10) {
						cnt = 0;
						System.out.println();		
					}
					
					cnt += 1;
					System.out.print(ci);
				}
			}
			System.out.println();
		}
	}

}