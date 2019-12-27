/**
 * Main method for stair case recursion problem
 */
import java.util.*;
import java.lang.Integer;

public class driver{

    public static void main(String[] args){
        int n;
        int[] x;
        String temp;
        String[] split;
        Scanner sc = new Scanner(System.in);

        temp = sc.nextLine();
        split = temp.split(" ", 0);
        n = Integer.parseInt(split[0]);
        x = new int[split.length-1];
        for(int i = 1; i < split.length; i++){
            x[i-1] = Integer.parseInt(split[i]);
        }

        StairCaseRecursion scr = new StairCaseRecursion();
        System.out.println(scr.num_ways(n,x));
    }

}
