// Problem 67
// By starting at the top of the triangle below and moving to adjacent numbers 
// on the row below, the maximum total from top to bottom is 23.

// 3
// 7 4
// 2 4 6
// 8 5 9 3

// That is, 3 + 7 + 4 + 9 = 23.

// Find the maximum total from top to bottom in triangle.txt 
// (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.


import java.util.*;
import java.io.*;
public class MaximumPath
{
    public static void main(String args[])throws IOException{
        String filename = "triangle.txt";
        File file = new File(filename);
        Scanner sc = new Scanner(file);
        String fileContents = "";
        int lineCount = 0;
        while (sc.hasNextLine()){
            fileContents += sc.nextLine() + " ";
            lineCount++;
        }   
        //System.out.println(fileContents);
        int pathsum[][] = new int[lineCount][lineCount];
        int start = 0, end;
        for(int i = 0;i<lineCount;i++){
            for(int j=0;j<=i;j++){
                end = fileContents.indexOf(' ', start+1);
                pathsum[i][j] = Integer.parseInt(fileContents.substring(start, end));
                start = end+1;
                //System.out.print(path[i][j] + "\t");
            }
            //System.out.println();
        }
        
        for (int i = lineCount - 2;i>=0;i--){
            for(int j = 0; j<=i; j++){
                int max = pathsum[i+1][j] > pathsum[i+1][j+1] ? pathsum[i+1][j]:pathsum[i+1][j+1];
                pathsum[i][j] = pathsum[i][j] + max;
            }
        }
        for (int i = 0;i< lineCount;i++){
            for(int j = 0; j<=i; j++)
                System.out.print(pathsum[i][j] + "\t");
            System.out.println();
        }
        
        System.out.println("Maximum path sum = " + pathsum[0][0]);
}
} 
            
        

