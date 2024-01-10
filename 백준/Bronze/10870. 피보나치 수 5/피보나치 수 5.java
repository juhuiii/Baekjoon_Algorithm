import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();
    if(n == 0){
      System.out.println("0");
    }
    else if(0<n && n<=2){
      System.out.println ("1");
    }
    else {
      long n1 = 0, n2 = 1, n3 = 1;

      for(int i = 2; i <= n; i++){
        n3 = n1 + n2;
        n1 = n2;
        n2 = n3;
      }
      System.out.println(n3);
    }
  }
}