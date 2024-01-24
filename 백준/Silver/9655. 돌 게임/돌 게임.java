import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();

    if(n % 2 == 0){
      System.out.println("CY");
    }
    else
      System.out.println("SK");
  }
}