import java.io.*;
import java.util.*;

public class Main{
  public static void main(String[] agrs) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());
    
    for(int i = 0; i < n; i++){
      String str = br.readLine();
      int res = 0;
      int count = 1;
      for(int j = str.length() - 1; j >= 0; j--){
        int num = Integer.parseInt(str.charAt(j) + "");
        
        if(count % 2 == 0){
          num *= 2;
          if(num >= 10) 
            num = (num / 10 + num % 10);
        }
        res += num;
        count++;
      }
      if(res % 10 == 0){
        bw.write("T\n");
      }
      else{
        bw.write("F\n");
      }
    }
    bw.flush();
    bw.close();
  }
}