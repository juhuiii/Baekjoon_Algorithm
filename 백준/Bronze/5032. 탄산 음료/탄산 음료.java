import java.util.*;
public class Main {   
  public static void main(String[] args) {     
    Scanner input = new Scanner(System.in);
    int a =  input.nextInt();
    int b =  input.nextInt(); 
    int c =  input.nextInt();
    int total = a + b;
    int sum = 0;
    while (total >= c){
      int now = total / c;
      sum += now;
      total = now + (total % c); 
    }
    System.out.println(sum);
  } 
}
