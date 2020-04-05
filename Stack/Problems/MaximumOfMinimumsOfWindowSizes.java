// { Driver Code Starts
import java.util.*;
import java.io.*;

class WindowMaximum {

    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            String[] inputline = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputline[0]);
            inputline = br.readLine().trim().split(" ");
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputline[i]);
            }
            new MaximumOfWindow().printMaxOfMin(arr, n);
        }
    }
}// } Driver Code Ends
class MaximumOfWindow {

    static void printMaxOfMin(int[] arr, int n) {
        // Your code here
        // Used to find previous and next smaller
        Stack<Integer> s = new Stack<>();

        // Arrays to store previous and next smaller
        int left[] = new int[n+1];
        int right[]  = new int[n+1];

        // Initialize elements of left[] and right[]
        for (int i=0; i<n; i++)
        {
            left[i] = -1;
            right[i] = n;
        }

        // Fill elements of left[] using logic discussed on
        // https://www.geeksforgeeks.org/next-greater-element/
        for (int i=0; i<n; i++)
        {
            while (!s.empty() && arr[s.peek()] >= arr[i])
                s.pop();

            if (!s.empty())
                left[i] = s.peek();

            s.push(i);
        }

        // Empty the stack as stack is going to be used for right[]
        while (!s.empty())
            s.pop();

        // Fill elements of right[] using same logic
        for (int i = n-1 ; i>=0 ; i-- )
        {
            while (!s.empty() && arr[s.peek()] >= arr[i])
                s.pop();

            if(!s.empty())
                right[i] = s.peek();

            s.push(i);
        }

        // Create and initialize answer array
        int ans[] = new int[n+1];
        for (int i=0; i<=n; i++)
            ans[i] = 0;

        // Fill answer array by comparing minimums of all
        // lengths computed using left[] and right[]
        for (int i=0; i<n; i++)
        {
            // length of the interval
            int len = right[i] - left[i] - 1;

            // arr[i] is a possible answer for this length
            // 'len' interval, check if arr[i] is more than
            // max for 'len'
            ans[len] = Math.max(ans[len], arr[i]);
        }

        // Some entries in ans[] may not be filled yet. Fill
        // them by taking values from right side of ans[]
        for (int i=n-1; i>=1; i--)
            ans[i] = Math.max(ans[i], ans[i+1]);

        // Print the result
        for (int i=1; i<=n; i++)
            System.out.print(ans[i] + " ");
        System.out.println("");
    }
}
