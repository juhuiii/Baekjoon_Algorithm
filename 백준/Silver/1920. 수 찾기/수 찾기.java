import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int[] arr = new int[n];
			int max = 0;
			for(int i=0;i<n;i++) {
				arr[i] = sc.nextInt();
			}
			Arrays.sort(arr);
			int m = sc.nextInt();
			for(int i=0;i<m;i++) {
				int a = sc.nextInt();
				System.out.println(binarySearch(arr, a));
			}
	}
	static int binarySearch(int[]arr, int n) {
		int left = 0;
		int right = arr.length-1;
		while(left<=right) {
			int mid = (left+right)/2;
			if(n==arr[mid]) {
				return 1;
			}else if(n < arr[mid]) {
				right = mid-1;
			}else {
				left = mid+1;
			}
		}return 0;
	}
}