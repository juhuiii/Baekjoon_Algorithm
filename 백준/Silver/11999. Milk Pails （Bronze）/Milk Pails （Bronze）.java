import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int x = input.nextInt();
    int y = input.nextInt();
    int m = input.nextInt();

    int temp = m;
    int max = 0;
    for(int i = 0; i <= m / y; i++){
      for(int j = 0; j <= m / x; j++){
        int sum = x * j + y * i;
        if(temp - sum >= 0){
          if(max < sum){
            max = sum;
          }
        }
        else{
          break;
        }
      }
    }
    System.out.println(max);
  }
} 