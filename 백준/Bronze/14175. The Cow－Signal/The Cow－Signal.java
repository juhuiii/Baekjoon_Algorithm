import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int m = input.nextInt();
    int n = input.nextInt();
    int k = input.nextInt();
    char arr[][] = new char[m][n];

    for(int i = 0; i < m; i++){
      String str = input.next();
      for(int j = 0; j < n; j++){
        arr[i][j] = str.charAt(j);
      }
    }

    for(int x = 0 ; x < m; x++){
      for(int y = 0; y < k; y++){
        for(int z = 0; z < n; z++){
          for(int a = 0; a < k; a++){
            System.out.print(arr[x][z]);
          }
        }
        System.out.println();
      }
    }
  }
} 