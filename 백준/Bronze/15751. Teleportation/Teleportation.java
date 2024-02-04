import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int a = input.nextInt();
    int b = input.nextInt();
    int x = input.nextInt();
    int y = input.nextInt();

    int e1 = Math.abs(b - a);
    int e2 = Math.abs(a - x) + Math.abs(b - y);
    int e3 = Math.abs(a - y) + Math.abs(b - x);
    
    int sum = Math.min(e1, Math.min(e2, e3));
    System.out.println(sum);
  }
} 