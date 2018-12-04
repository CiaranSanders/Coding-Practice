/**
Author: Ciaran Sanders
Date: 12/2/2018
**/

import java.util.*;

public class TestStairCaseRecursion{

    public static void main (String[] args){

      StairCaseRecursion newSearch = new StairCaseRecursion();
      int numOfWays,numOfWaysInc, numOfStairs;
      int[] increments;

      /** check if user input is correct**/
      if (!(args.length >= 2)){
        System.out.println("Usage [number of stairs] [step increments]");
        System.exit(0);
      }

      increments = new int[args.length-1];
      for (int i = 1; i < args.length;i++){
        increments[i - 1] = Integer.parseInt(args[i]);
      }


      System.out.println(Arrays.toString(increments));
      numOfStairs = Integer.parseInt(args[0]);


      numOfWaysInc = newSearch.num_ways(numOfStairs, increments);
      numOfWays = newSearch.num_ways(numOfStairs);


      System.out.println("The number of ways to get to " + numOfStairs + " using 1 and 2 steps is " + numOfWays);
      System.out.println("The number of ways to get to " + numOfStairs + " using the given increments is " + numOfWaysInc);



    }
}
