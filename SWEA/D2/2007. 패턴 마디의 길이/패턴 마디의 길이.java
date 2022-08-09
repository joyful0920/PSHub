import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = Integer.parseInt(sc.nextLine());
		for (int tc = 1; tc <= t; tc++) {
			String s = sc.nextLine();
			
			for (int i = 1; i <= 10; i++) {
				if (s.substring(0, i).equals(s.substring(i, i + i))) {
					System.out.printf("#%d %d%n", tc, i);
					break;
				}
			}
		}
	}

}