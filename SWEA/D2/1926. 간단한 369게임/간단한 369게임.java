import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for (int i = 1; i <= n; i++) {
			int j = i;
			
			int cnt = 0;
			while (j > 0) {
				if (j % 10 == 3 || j % 10 == 6 || j % 10 == 9)
					cnt += 1;
					
				j /= 10;
			}
			
			if (cnt != 0) {
				while (cnt > 0) {
					System.out.print("-");
					cnt -= 1;
				}
			} else {
				System.out.print(i);
			}
			
			System.out.print(" ");
		}
	}

}
