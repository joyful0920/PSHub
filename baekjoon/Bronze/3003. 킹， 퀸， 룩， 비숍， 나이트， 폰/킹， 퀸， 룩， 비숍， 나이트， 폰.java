//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int[] standard = {1, 1, 2, 2, 2, 8};
		for (int i=0; i < 6; i++) {
			System.out.print(standard[i] - sc.nextInt() + " ");
		}
	}

}
