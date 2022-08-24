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
			
			int speed = 0;
			int result = 0;
			
			for (int i = 1; i <= n; i++) {
				int co1 = sc.nextInt();
				int co2 = 0;
				
				if (co1 == 0)
					co2 = 0;
				else {
					co2 = sc.nextInt();
					if (co1 == 1)
						speed += co2;
					else {
						if (speed > co2)
							speed -= co2;
						else
							speed = 0;
					}
				}
				
				result += speed;
			}
			
			System.out.printf("#%d %d%n", tc, result);
		}
	}

}