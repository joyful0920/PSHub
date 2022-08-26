//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			
			int[] a = new int[n];
			for (int i = 0; i < n; i++) {
				a[i] = sc.nextInt();
			}
			
			int result = -1;
			for (int i = 0; i < n - 1; i++) {
				for (int j = i + 1; j < n; j++) {
					int num = a[i] * a[j];
					String strnum = Integer.toString(num);
					if (strnum.length() == 1) {
						if (num > result)
							result = num;
					}
					else {
						for (int k = 1; k < strnum.length(); k++) {
							int left = strnum.charAt(k - 1) - 48;
							int right = strnum.charAt(k) - 48;
							if (left > right)
								break;
							else {
								if (k == strnum.length() - 1)
									if (num > result)
										result = num;
							}
						}
					}
				}
			}
			
			System.out.printf("#%d %d%n", tc, result);
		}
	}
}