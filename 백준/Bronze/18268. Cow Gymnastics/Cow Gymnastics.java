import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int k = input.nextInt();
    int n = input.nextInt();
    int[][] rank = new int[11][21];

    for(int i = 0; i < k; i++){
      for(int j = 0; j < n; j++){
        int r = input.nextInt();
        rank[i][r] = j;
      }
    }

    int cnt = 0;
    for(int i = 1; i <= n; i++){
      for(int j = 1; j <= n; j++){
        if(i == j)
          continue;
        boolean check = true;
        for (int l = 0; l < k; l++){
          if (rank[l][i] > rank[l][j]){
            check = false;
            break;
          }
        }
        if (check) cnt++;
      }
    }
    System.out.println(cnt);
  }
}