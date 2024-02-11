import java.util.*;
public class Main {
  public static void main(String[]args) {
    Scanner sc = new Scanner(System.in);
    int [] arr = new int[32];
    int n = sc.nextInt();
    int res = 1;
    for(int i = 1; i <= n; i++){
      int l = sc.nextInt();
      int m = sc.nextInt();
      arr[l]--;
      arr[m]++;
    }
    int b = sc.nextInt();
    for(int i = 1; i <= 31; i++){
      b += arr[i];
      if (b < 0){
        res = 0;
        break;
      }
    }
    System.out.println(res);
  }
}