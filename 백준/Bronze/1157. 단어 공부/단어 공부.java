import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int [] alp = new int[26];
    String s = input.next();

    for (int i = 0; i < s.length(); i++){
      if('A' <= s.charAt(i) && s.charAt(i) <= 'Z'){
        alp[s.charAt(i) - 'A']++;
      }
      else {
        alp[s.charAt(i) - 'a']++;
      }
    }
    int max = -1;
    char ans = '?';

    for (int j = 0; j < 26; j++){
      if(alp[j] > max){
        max = alp[j];
        ans = (char) (j + 65);
      }
      else if (alp[j] == max){
        ans = '?';
      }
    }
    System.out.print(ans);
  }
}
