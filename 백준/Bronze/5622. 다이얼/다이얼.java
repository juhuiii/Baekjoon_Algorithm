import java.util.Arrays;
import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
    
		Scanner in = new Scanner(System.in);
    String str = in.next();

    char[] array = str.toCharArray();
    int t = 0;

    for (int i = 0; i<array.length; i++){
      if(array[i] >= 'A' && array[i] <= 'C')
        t += 3;
        
      else if (array[i] >= 'D' && array[i] <= 'F')
        t += 4;
        
      else if (array[i] >= 'G' && array[i] <= 'I')
        t += 5;
        
      else if (array[i] >= 'J' && array[i] <= 'L')
        t += 6;
        
      else if (array[i] >= 'M' && array[i] <= 'O')
        t += 7;   

        
      else if (array[i] >= 'P' && array[i] <= 'S')
        t += 8;
        
      else if (array[i] >= 'T' && array[i] <= 'V')
        t += 9;
        
      else if (array[i] >= 'W' && array[i] <= 'Z')
        t += 10;

      else
        t += 11;
    }
    System.out.print(t);
	}
}
