import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    String s = input.next();

    for(int i = 1; i <= n; i++){
      boolean check = true;
      
      for (int j = 0; j <= n - i; j++){
        String s1 = s.substring(j, j + i);
        for (int k = 0; k <= n - i; k++) {
          if(j == k)
            continue;
          if(s1.equals(s.substring(k, k + i))) {
            check = false;
            break;
          }
        }
        if (!check)
          break;
      }
      if (check) {
        System.out.println(i);
        break;
      } 
    }
  }
}
