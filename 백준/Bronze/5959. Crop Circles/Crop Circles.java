import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] x = new int[n];
    int[] y = new int[n];
    int[] r = new int[n];

    for(int i = 0; i <n; i++){
      x[i] = sc.nextInt();
      y[i] = sc.nextInt();
      r[i] = sc.nextInt();
    }

    for(int i = 0; i < n; i++){
      int count = 0;

      for(int j = 0; j < n; j++)
        {
          if (i != j) {
            if (Math.sqrt(Math.pow(x[i] - x[j], 2) + Math.pow(y[i] - y[j], 2)) < r[i] + r[j]){
             count++; 
            }
          }
        }
      System.out.println(count);
    }
  }
}