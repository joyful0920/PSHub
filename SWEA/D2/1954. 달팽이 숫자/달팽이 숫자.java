//import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
		
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int n = sc.nextInt();
			int[][] snail = new int[n][n];
			
			int x = 0;
			int y = 0;
			int idx = 0;
			for (int i = 1; i <= n * n; i++) {
				snail[x][y] = i;
				
				int nx = x + dx[idx];
				int ny = y + dy[idx];
				
				if ((0 <= nx && nx < n) && (0 <= ny && ny < n) && snail[nx][ny] == 0) {
					x = nx;
					y = ny;
				} else {
					idx = (idx + 1) % 4;
					x += dx[idx];
					y += dy[idx];
				}
			}
			
			System.out.printf("#%d%n", tc);
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					System.out.print(snail[i][j] + " ");
				}
				System.out.println();
			}
		}
	}

}