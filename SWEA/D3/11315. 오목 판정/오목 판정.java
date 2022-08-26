//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = Integer.parseInt(sc.nextLine());
		for (int tc = 1; tc <= t; tc++) {
			int n = Integer.parseInt(sc.nextLine());
			
			String[] omok = new String[n];
			for (int i = 0; i < n; i++) {
				omok[i] = sc.nextLine();
			}
			
			String result = "NO";
			
			loop:
			for (int start = 0; start < n - 4; start++) {
				for (int i = 0; i < n; i++) {
					String temp = "";
					for (int j = start; j < start + 5; j++) {
						temp += omok[i].charAt(j);
					}
					if (temp.equals("ooooo")) {
						result = "YES";
						break loop;
					}
				}
				for (int j = 0; j < n; j++) {
					String temp = "";
					for (int i = start; i < start + 5; i++) {
						temp += omok[i].charAt(j);
					}
					if (temp.equals("ooooo")) {
						result = "YES";
						break loop;
					}
				}
				for (int j = 0; j < n - 4 - start; j++) {
					String temp = "";
					for (int i = start; i < start + 5; i++) {
						temp += omok[i].charAt(i + j);
						if (temp.equals("ooooo")) {
							result = "YES";
							break loop;		
						}
					}
					temp = "";
					for (int i = start; i < start + 5; i++) {
						temp += omok[i + j].charAt(i);
						if (temp.equals("ooooo")) {
							result = "YES";
							break loop;		
						}
					}
				}
				for (int j = 0; j < n - 4 - start; j++) {
					String temp = "";
					for (int i = start; i < start + 5; i++) {
						temp += omok[i].charAt(n - 1 - i - j);
						if (temp.equals("ooooo")) {
							result = "YES";
							break loop;		
						}
					}
					temp = "";
					for (int i = start; i < start + 5; i++) {
						temp += omok[i + j].charAt(n - 1 - i);
						if (temp.equals("ooooo")) {
							result = "YES";
							break loop;		
						}
					}
				}
			}
			
			System.out.printf("#%d %s%n", tc, result);
		}
	}
}