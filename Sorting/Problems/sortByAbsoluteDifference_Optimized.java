{
//Initial Template for Java
import java.util.*;
import java.io.*;
import java.lang.*;
class Sorting
{
    public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		while(t-->0){
		    String inputLine[] = br.readLine().trim().split(" ");
		    int n = Integer.parseInt(inputLine[0]);
		    int x = Integer.parseInt(inputLine[1]);
		    
		    int arr[] =  new int[n];
		    inputLine = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++){
		        arr[i] = Integer.parseInt(inputLine[i]);
		    }
		    new SortABS().sortABS(arr,n, x);
		    System.out.println();
		}
	}
}
}
/*This is a function problem.You only need to complete the function given below*/
//User function Template for Java
class SortABS
{
    // here k is the value with which we have to 
    // compute absolute difference
    // length of array can be computed as arr.length
    static void sortABS(int arr[], int n,int k)
    {
        // add your code here
        TreeMap<Integer, ArrayList<Integer>> m = new TreeMap<>(); 
              
            // Store values in a map with the difference  
            // with X as key 
            for (int i = 0; i < n; i++) 
            { 
                int diff = Math.abs(k - arr[i]); 
                if (m.containsKey(diff))  
                { 
                    ArrayList<Integer> al = m.get(diff); 
                    al.add(arr[i]); 
                    m.put(diff, al); 
                } 
                else 
                { 
                        ArrayList<Integer> al = new ArrayList<>(); 
                        al.add(arr[i]); 
                        m.put(diff,al); 
                } 
            } 
  
            // Update the values of array 
            int index = 0; 
            for (Map.Entry entry : m.entrySet())  
            { 
                ArrayList<Integer> al = m.get(entry.getKey()); 
                for (int i = 0; i < al.size(); i++) 
                        arr[index++] = al.get(i); 
            }
        for(int i=0;i<n;i++)
            System.out.print(arr[i]+" ");
    }
}

