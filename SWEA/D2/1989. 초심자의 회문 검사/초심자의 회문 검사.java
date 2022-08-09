import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = Integer.parseInt(sc.nextLine());
		
		for (int tc = 1; tc <= t; tc++) {
			String word = sc.nextLine();
			StringBuffer sb = new StringBuffer(word);
			
			if (word.equals(sb.reverse().toString()))
				System.out.printf("#%d 1%n", tc);
			else
				System.out.printf("#%d 0%n", tc);
		}
	}

}
