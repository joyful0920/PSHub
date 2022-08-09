import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String n = sc.nextLine();
		
		int result = 0;
		for (int i = 0; i < n.length(); i++) {
			result += (int) (n.charAt(i) - '0');
		}
		
		System.out.println(result);
	}

}
