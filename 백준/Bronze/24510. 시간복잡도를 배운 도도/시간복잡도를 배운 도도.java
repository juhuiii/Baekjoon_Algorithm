  import java.util.Scanner;

  class Main{
      public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int C = sc.nextInt();
      int result = 0;

      for(int i = 0; i <= C; i++) {
        int count = 0;
        String code = sc.nextLine();
        code = code.replaceAll("for", "!");
        code = code.replaceAll("while", "!");

        for(int j = 0; j < code.length(); j++) {
          if(code.charAt(j) == '!')
            count++;
        }
        if(result < count)
          result = count;
      }
      System.out.println(result);
    }
  }