import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int t = input.nextInt();

    for(int i = 0; i < t; i++){
      int h = input.nextInt(); // height
      int w = input.nextInt(); // width
      int n = input.nextInt(); // num of people

      int temp = 0;

      if (n % h == 0) {
        System.out.println((h * 100) + (n / h));
      }
      else {
        System.out.println((n % h) * 100 + ((n / h) + 1));
      }
    }
  }
}
