import java.util.*;
class Main {
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    long w = input.nextInt();

    long[] arr = new long[n];

    for (int i = 0; i < n; i++){
      arr[i] = input.nextInt();
    }

    long coin = 0;
    for(int i = 0; i < arr.length - 1; i++) {
      if (arr[i] < arr[i + 1]) {
        if(w >= arr[i]){
          coin += w / arr[i];
          w = w % arr[i] ;
        }
      }
        else if (arr[i] > arr[i + 1]) {
          w += coin * arr[i];
          coin = 0;
        }
      }
      w += coin * arr[n - 1];
      System.out.println(w);
  }
}