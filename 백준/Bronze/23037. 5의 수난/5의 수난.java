import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();

    int a = 10;
    int b = 1;

    int[] array = new int[5];
    for(int i = 0; i < 5; i++){
      array[i] = (n % a) / b;
      
      a = a*10;
      b = b*10;
    }

    int sum = 0;
    for(int i = 0; i < 5; i++){
      sum += Math.pow(array[i], 5);
    }

    System.out.println(sum);
  }
}