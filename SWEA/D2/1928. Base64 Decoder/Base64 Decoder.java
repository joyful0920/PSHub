//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.UnsupportedEncodingException;
import java.util.Base64;
import java.util.Base64.Decoder;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException {
//		System.setIn(new FileInputStream("src/swea_d2/input.txt"));
		Scanner sc = new Scanner(System.in);
		Decoder decoder = Base64.getDecoder();
		
		int t = Integer.parseInt(sc.nextLine());
		for (int tc = 1; tc <= t; tc++) {
			String encodedString = sc.nextLine();			
			byte[] decodedBytes = decoder.decode(encodedString);			
			String decodedString = new String(decodedBytes, "UTF-8");
			
			System.out.printf("#%d %s%n", tc, decodedString);
		}
	}

}