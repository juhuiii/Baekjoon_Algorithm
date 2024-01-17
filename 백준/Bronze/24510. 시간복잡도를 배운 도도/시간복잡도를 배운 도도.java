import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int c = input.nextInt();
        int[] count = new int[c];

        for(int i = 0; i < c; i++){
            String str = input.next();
            str = str.replaceAll("for", "~");
            str = str.replaceAll("while", "~");

            for(int j = 0; j < str.length(); j++){
                if(str.charAt(j) == '~')
                    count[i]++;
            }
        }

        int max = 0;
        for(int i = 0; i < c; i++){
            if(max < count[i]){
                max = count[i];
            }
        }
        System.out.println(max);
    }
} 