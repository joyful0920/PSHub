//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int b2 = b % 10;
		int b1 = b % 100 - b2;
		int b0 = b - b1;
		
		System.out.println(a * b2);
		System.out.println(a * (b1 / 10));
		System.out.println(a * (b0 / 100));
		System.out.println(a * b);
	}

}