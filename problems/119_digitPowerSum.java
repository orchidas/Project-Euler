
/*The number 512 is interesting because it is equal to the sum of its digits raised to some power: 
 * 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.
We shall define an to be the nth term of this sequence and insist that a number must contain at 
least two digits to have a sum. You are given that a2 = 512 and a10 = 614656. Find a30.*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class digitPowerSum {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int B = sc.nextInt();
        //solving only for base 10
        //10<x^n<(10)^100 according to the constraints
        //max limit of x = 99999... 99 times = 99*9
        //10/log10(x) < n < 100/log10(x)
        BigInteger base,power;
        List<BigInteger> list = new ArrayList<BigInteger> ();                        
        
        for(int x = 2; x<= 99*9; x++){
            int minN = (int)Math.ceil(1/(Math.log((double)x)/Math.log((double)10)));
            int maxN = (int)Math.floor(100/(Math.log((double)x)/Math.log((double)10)));  
            for(int n = minN;n <= maxN; n++){
               
                base = new BigInteger(Integer.toString(x));  
                power = base.pow(n); 
             
                if(sumOfDigits(power).compareTo(base) == 0)
                   list.add(power);  
                
            }
        }
        Collections.sort(list);
        System.out.print(list.get(29));
        /*for(int i=0;i<list.size();i++)
            System.out.print(list.get(i) + " ");*/  
    }
                                                            
    public static BigInteger sumOfDigits(BigInteger n){
        BigInteger sum = BigInteger.ZERO;
        while(n.compareTo(BigInteger.ZERO) == 1){
            sum = sum.add(n.remainder(BigInteger.TEN));
            n = n.divide(BigInteger.TEN);
        }
        return sum;
    }                                   
}
