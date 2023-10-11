import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int[] alphabet = new int[26];
    for(int i = 0; i < 26; i++){
      alphabet[i] = -1;
    }

    String w = input.nextLine();
    for(int j = 0; j < w.length(); j++) {
      char c = w.charAt(j);
      if(alphabet[c - 'a'] == -1){
        alphabet[c - 'a'] = j;
       }
    }

    for(int k = 0; k < alphabet.length; k++){
      System.out.print(alphabet[k] + " ");
    }
    
  }
} 
