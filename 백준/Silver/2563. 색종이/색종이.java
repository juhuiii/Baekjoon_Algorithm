import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();
    int[][] square = new int[100][100];
    
    for(int i = 0; i < n; i++){
      int x = input.nextInt();
      int y = input.nextInt();
      for(int m = x; m < x + 10; m++){
        for(int a = y; a < y + 10; a++){
          square[m][a] = 1;
        }
      }
    }
    int black = 0;
    for(int k = 0; k < 100; k++){
      for(int i = 0; i < 100; i++){
        if(square[k][i] == 1){
          black += 1;
        }
      }
    }
    System.out.println(black);
  }
}