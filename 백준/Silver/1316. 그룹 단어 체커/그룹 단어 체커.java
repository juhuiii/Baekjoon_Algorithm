import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();
    int count = 0;
    int pre = 0;
    for(int i = 0; i < n; i++){
      String str = input.next();
      boolean [] check = new boolean[26];
      for(int j = 0; j < str.length(); j++){
        int index = str.charAt(j) - 'a';
        if(check[index]){
          if(index != pre){
            break;
          }
        }
        else{
          check[index] = true;
        }
        pre = index;
        if (j == str.length() - 1){
          count++;
        }
      }
    }
    System.out.println(count);
  }
}