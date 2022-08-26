//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[][] paper = new int[100][100];
		
		int cnt = 0;
		while (n > 0) {
			n--;
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			for (int i = x; i < x + 10; i++) {
				for (int j = y; j < y + 10; j++) {
					if (paper[i][j] != 1) {
						cnt++;
						paper[i][j] = 1;
					}
				}
			}
		}
		
		System.out.println(cnt);
	}

}
