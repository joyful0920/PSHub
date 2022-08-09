import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		System.out.print(n);
		for (int i = n - 1; i >= 0; i--) {
			System.out.printf(" %d", i);
		}
	}

}