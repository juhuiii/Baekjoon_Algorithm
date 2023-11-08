import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
      int n = input.nextInt();
      long[] arr = new long[n + 1];
      arr[1] = 5;
      for(int i = 2; i < arr.length; i++){
        arr[i] = arr[i-1] + (i*5) +(1-(2*i));
      }
      System.out.println(arr[n] % 45678);
    }
}