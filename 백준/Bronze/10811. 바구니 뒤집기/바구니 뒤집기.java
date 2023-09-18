import java.util.Scanner; 
import java.util.Arrays; 

public class Main {
  public static void main(String[] args) {
		Scanner in = new Scanner(
System.in
);
  
    int basket = in.nextInt();
    int M = in.nextInt(); 

    int[] basketarr = new int[basket];
    for(int i = 0; i < basket; i++) {
      basketarr[i] = i + 1; 
    }
    for(int j = 0; j < M; j++) {
      int a = in.nextInt()-1;
      int b = in.nextInt()-1;

    while(a < b) {
      int temp = basketarr[a];
      basketarr[a] = basketarr[b];
      basketarr[b] = temp; 
      a++;
      b--;
      }
    }
    for(int k = 0; k < basket; k++) {
      System.out.print(basketarr[k] + " ");
    }
  }
} 