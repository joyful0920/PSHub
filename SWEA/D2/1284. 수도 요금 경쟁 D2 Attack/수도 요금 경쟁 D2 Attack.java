//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//			System.setIn(new FileInputStream("src/input.txt"));
			Scanner sc = new Scanner(System.in);
			
			int t = sc.nextInt();
			for (int tc = 1; tc <= t; tc++) {
				int p = sc.nextInt();
				int q = sc.nextInt();
				int r = sc.nextInt();
				int s = sc.nextInt();
				int w = sc.nextInt();
				
				int a = p * w;
				int b = q;
				
				if (w > r)
					b += (w - r) * s;
				
				int result = (a > b) ? b : a;
				
				System.out.printf("#%d %d%n", tc, result);
			}
			
	}
}