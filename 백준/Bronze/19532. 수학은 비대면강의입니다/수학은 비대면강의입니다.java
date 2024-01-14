import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
 
public class Main {
	public static int a,b,c,d,e,f;
	public static int result = 0;
	public static int x, y;
	
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	a = Integer.parseInt(st.nextToken());
    	b = Integer.parseInt(st.nextToken());
    	c = Integer.parseInt(st.nextToken());
    	d = Integer.parseInt(st.nextToken());
    	e = Integer.parseInt(st.nextToken());
    	f = Integer.parseInt(st.nextToken());
    	
    	simulate();
    	System.out.print(x + " " + y);
    }
    
    
    
    public static void simulate() {
    	for(int i=-999;i<=999;i++) {
    		for(int j=-999;j<=999;j++) {
    			int first = a * i + b * j;
    			int second = d * i + e * j;
    			if(first == c && second == f) {
    				x = i;
    				y = j;
    				return;
    			}
    		}
    	}
    	
    }
}