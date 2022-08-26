//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = Integer.parseInt(sc.nextLine());
		for (int tc = 1; tc <= t; tc++) {
			String target = sc.nextLine();
			
			String first = "";
			for (int i = 0; i < target.length(); i++) {
				first += "0";
			}
			
			int cnt = 0;
			StringBuilder now = new StringBuilder(first);
			
			for (int i = 0; i < target.length(); i++) {
				if (now.charAt(i) != target.charAt(i)) {
					cnt++;
					char temp = target.charAt(i);
					
					for (int j = i; j < target.length(); j++) {
						now.setCharAt(j, temp);
					}
				}
				
				if (now.equals(target) == true)
					break;
			}
			
			System.out.printf("#%d %d%n", tc, cnt);
		}
	}
}