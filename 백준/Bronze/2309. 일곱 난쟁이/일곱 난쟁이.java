import java.util.Arrays;
import java.util.Scanner;
  public class Main{
    public static void main(String[] args){
      Scanner input = new Scanner(System.in);

      int[] h = new int[9];
      int sum = 0;

      for(int i = 0; i < 9; i++){
        int height = input.nextInt();
        h[i] = height;
        sum += height;
      }
      Arrays.sort(h);

      for(int i = 0; i < 8; i++){
        for(int j = i + 1; j < 9; j++){
          if(sum - h[i] - h[j] == 100){
            for(int k = 0; k < 9; k++){
              if(i == k || j == k){
                continue;
              }
              System.out.println(h[k]);
            }
              return;
          }
        }
      }
    }
  } 