//Problem 28
public class spiralArray{
    public static void main(String args[]){
        int N = 1001;
        int spiral[][] = new int[N][N];
        int start = N/2;
        int i = start,j = start;
        
        int num = 1;
        int count = 1;
        spiral[i][j] =num;
        while (true){
            
            for(int k=1;k<=count;k++){
                if(j+1 < N) 
                    spiral[i][++j] = ++num;
                //System.out.println(num);
                }
            if(count == N)
                break;
            for(int k=1;k<=count;k++){
                if(i+1 < N)
                    spiral[++i][j] = ++num;
                //System.out.println(num);
                }
            count++;
            for(int k=1;k<=count;k++){
                if(j-1 >= 0 )
                    spiral[i][--j] = ++num;
                //System.out.println(num);
                }
                
            for(int k=1;k<=count;k++){
                if(i-1 >= 0)
                    spiral[--i][j] = ++num;
                //System.out.println(num);
            }
            count++;
        }
        
        //printing the array
//         for(i=0;i<N;i++){
//             for(j=0;j<N;j++)
//                 System.out.print(spiral[i][j] + "\t");
//             System.out.println();
//         }
        
        //find sum of diagonals
        int sumdiag = 0;
        for(i=0;i<N;i++){
            for(j=0;j<N;j++){
                if(i==j || i+j == N-1)
                    sumdiag += spiral[i][j];
                }
            }
        System.out.println("Sum of the diagonals is " + sumdiag);
    }
}

                
            
        
        