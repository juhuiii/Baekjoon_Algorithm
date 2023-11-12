import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    double a = input.nextDouble();
    double b = input.nextDouble();
    double c = input.nextDouble();
    double d = input.nextDouble();

    double result = a/c + b/d;
    double result1 = c/d + a/b;
    double result2 = d/b + c/a;
    double result3 = b/a + d/c;

    if((result >= result1) && (result >= result2) && (result >= result3))
    {
      System.out.println(0);
    }
      
    else if((result1 >= result) && (result1 >= result2) && (result1 >= result3))
    {
      System.out.println(1);
    }
      
    else if((result2 >= result) && (result2 >= result1) && (result2 >= result3))
    {
      System.out.println(2);
    }
      
    else
    {
      System.out.println(3);
    }
  }
}