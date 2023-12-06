import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int [] place = new int[1001];
    int result = 0;
    int n = input.nextInt();
    for (int i = 0; i < n; i++){
      int s = input.nextInt();
      int t = input.nextInt();
      int b = input.nextInt();

      for(int j = s; j <= t; j++){
        place[j] += b;
        result = Math.max(result, place[j]);
      }
    }
    System.out.println(result);
  }
}