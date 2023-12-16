import java.util.Arrays;
import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
    
		Scanner in = new Scanner(System.in);
    int a, b, c;
    while (true)
    {
        a = in.nextInt();
        b = in.nextInt();
        c = in.nextInt();
      if (a == 0 && b == 0 && c == 0)
        break;
      if(a == b && b == c && c == a)
        System.out.println("Equilateral");
      else if( a + b <= c || a + c <= b || b + c <= a)
        System.out.println("Invalid");
      else if (a == b || b == c || c == a)
        System.out.println("Isosceles");
      else
        System.out.println("Scalene");

    }
  }
}
  