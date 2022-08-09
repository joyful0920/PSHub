import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int p = sc.nextInt();
		int k = sc.nextInt();
		
		int cnt = 1;
		for (int i = k; i < p; i++) {
			cnt += 1;
		}
		
		System.out.println(cnt);
	}
}