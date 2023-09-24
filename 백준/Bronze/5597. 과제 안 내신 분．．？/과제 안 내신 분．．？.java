import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		// 30명, 1<=n<=28
		int[] address = new int[31];
		for(int i=1; i<29; i++) 
			address[scan.nextInt()] ++;
		
		for(int i=1; i<address.length; i++) {
			if(address[i] == 0)
				System.out.println(i);
		}
		
		scan.close();
	}

}