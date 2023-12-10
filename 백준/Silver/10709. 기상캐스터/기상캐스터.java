import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int x = input.nextInt();
    int y = input.nextInt();
    String[][] arr = new String[x][y];

    for (int i = 0; i < x; i++) {
      String m = input.next();
      for (int j = 0; j < y; j++){
        arr[i][j] = String.valueOf(m.charAt(j));
      }
    }

    for (int i = 0; i < x; i++){
      int d = -1;
      for (int j = 0; j < y; j++){
        if (d != -1){
          d++;
        }
        if (arr[i][j].equals("c")) {
          d = 0;
        }

        System.out.print(d + " ");
      }
      System.out.println();
    }
  }
}