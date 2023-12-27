import java.util.*;
public class Main{
  public static void main(String[] agrs){
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();

    int[] m = new int[n];

    int count = 1; 

    for(int i = 0; i < n; i++){
      m[i] = input.nextInt();
    }
    int temp = m[n - 1];

    for(int i = n - 2; i >= 0; i--){
      if(m[i] > temp){
        count++;
        temp = m[i];
      }
    }
    System.out.println(count);
  }
} 