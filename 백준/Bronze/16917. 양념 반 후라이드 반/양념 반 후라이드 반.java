import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int a = input.nextInt();
    int b = input.nextInt();
    int c = input.nextInt();
    int x = input.nextInt();
    int y = input.nextInt();
    int total = 0;
    if(a + b <= c * 2){
      total += a * x + b * y;
    }
    else{
      if(x > y){
        total = y * 2 * c;
        total += Math.min((x - y) * a, (x - y) * c * 2);
      }
      else{
        total = x * 2 * c;
        total += Math.min((y - x) * b, (y - x) * c * 2);
      }
    }
    System.out.println(total);
  }
} 
