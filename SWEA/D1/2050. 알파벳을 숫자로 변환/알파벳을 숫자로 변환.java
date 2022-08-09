import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		
		for (int i = 0; i < s.length(); i++) {
			int num = (int) s.charAt(i) - 64;
			System.out.printf("%d ", num);
		}
	}

}