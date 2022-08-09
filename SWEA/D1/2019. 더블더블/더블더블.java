import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int num = 1;
		System.out.print(num);
		
		while (n > 0) {
			n -= 1;
			num *= 2;
			System.out.printf(" %d", num);
		}
	}

}