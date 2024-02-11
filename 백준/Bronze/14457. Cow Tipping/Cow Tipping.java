import java.util.*;
public class Main {
  public static void main(String[]args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int cow[][] = new int[n][n];
    for(int i = 0; i < n; i++){
      String str = sc.next();
      for(int j = 0; j < n; j++) {
        cow[i][j] = Integer.parseInt(str.substring(j, j + 1));
      }
    }
    int cnt = 0;
    for (int i = n - 1; i >= 0; i--){
      for(int j = n - 1; j >= 0; j--){
        if(cow[i][j] == 1){
          for (int x = 0; x <= i; x++){
            for(int y = 0; y <= j; y++){
              if( cow[x][y] == 1) {
                cow[x][y] = 0;
              }
              else {
                cow[x][y] = 1;
              }
            }
          }
          cnt++;
        }
        if(cow[j][i] == 1) {
          for(int x = 0 ; x <= j; x++){
            for (int y = 0; y <= i; y++) {
              if(cow[x][y] == 1) {
                cow[x][y] = 0;
            }
              else{
                cow[x][y] = 1;
              }
          }
        }
          cnt++;
      }
    }
  }
    System.out.println(cnt);
  }
}