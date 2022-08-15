import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int[][] sudoku = new int[9][9];
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					sudoku[i][j] = sc.nextInt();
				}
			}
			
			int result = 1;
			for (int i = 0; i < 9; i++) {
				int[] cnt = new int[10]; 
				for (int j = 0; j < 9; j++) {
					if (cnt[sudoku[i][j]] == 0)
						cnt[sudoku[i][j]] = 1;
					else
						result = 0;
						
				}
			}
			
			for (int j = 0; j < 9; j++) {
				int[] cnt = new int[10]; 
				for (int i = 0; i < 9; i++) {
					if (cnt[sudoku[i][j]] == 0)
						cnt[sudoku[i][j]] = 1;
					else
						result = 0;
						
				}
			}
			
			for (int i = 0; i < 9; i += 3) {
				for (int j = 0; j < 9; j += 3) {
					int[] cnt = new int[10];
					for (int x = 0; x < 3; x++) {
						for (int y = 0; y < 3; y++) {
							if (cnt[sudoku[x][y]] == 0)
								cnt[sudoku[x][y]] = 1;
							else
								result = 0;
						}
					}
				}
			}
			
			System.out.printf("#%d %d%n", tc, result);
		}
	}

}