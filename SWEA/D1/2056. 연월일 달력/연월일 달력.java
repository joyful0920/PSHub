import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			int t = Integer.parseInt(sc.nextLine());
			
			for (int i = 1; i <= t; i++) {
				String date = sc.nextLine();
				
				int year = Integer.parseInt(date.substring(0, 4));
				int month = Integer.parseInt(date.substring(4, 6));
				int day = Integer.parseInt(date.substring(6, 8));
				
				if (month < 1 || month > 12) {
					System.out.printf("#%d %d%n", i, -1);
					continue;
				}
				
				switch (month) {
					case 1: case 3: case 5: case 7: case 8: case 10: case 12:
						if (day < 1 || day > 31) {
							System.out.printf("#%d %d%n", i, -1);
							continue;
						}
					case 4: case 6: case 9: case 11:
						if (day < 1 || day > 30) {
							System.out.printf("#%d %d%n", i, -1);
							continue;
						}
					case 2:
						if (day < 1 || day > 28) {
							System.out.printf("#%d %d%n", i, -1);
							continue;
						}
				}
				
				System.out.printf("#%s %s/%s/%s%n", i, date.substring(0, 4), date.substring(4, 6), date.substring(6, 8)); 
		}
	}

}