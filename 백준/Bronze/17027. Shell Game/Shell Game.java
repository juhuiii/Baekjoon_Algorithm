import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();

    int a [] = new int[n];
    int b [] = new int[n];
    int g [] = new int[n];

    for(int i = 0; i < n; i++){
      a[i] = input.nextInt() - 1;
      b[i] = input.nextInt() - 1;
      g[i] = input.nextInt() - 1;
    }

    int max = 0;
    for(int i = 0; i < 3; i++){
      int temp[] = new int [3];
      temp[i] = 1;
      int result = 0;
      
      for(int j = 0; j < n; j++){
        int test = temp[a[j]];
        temp[a[j]] = temp[b[j]];
        temp[b[j]] = test;
        if(temp[g[j]] == 1) {
          result++;
        }
      }
      if(result > max) {
        max = result;
      }
    }
    System.out.println(max);
  }
} 