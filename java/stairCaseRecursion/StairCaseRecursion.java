/**
Author: Ciaran Sanders
Date: 12/2/2018
Credit to CS dojo on youtube for the problem idea
and for the solution since my dumb a$$ couldn't
figure it out myself
**/

import java.util.*;
import java.util.Arrays;

public class StairCaseRecursion{

  /**
  finds the number of different ways to reach the given number using the given increments
  Duplicates not counted (see example in comment above num_ways below)
  **/
  public int num_ways(int stairs, int[] increments){
    //base case
    if (stairs == 0){
      return 1;
    }
    int numOfWays = 0;
    
    for (int i = 0; i < increments.length; i++){
      if (stairs - increments[i] >= 0){
        numOfWays += num_ways(stairs-increments[i], increments);
      }

    }

   return numOfWays;
  }



  /**
  finds the number of different ways to reach the given number using only the increment 1 and 2.
  Duplicates not counted (ex/ given stairs == 4; the case {0,1,2,4} would be the same as {0,2,3,4}
  because both use (1x2)+(2x1) increments, so only one would be counted)
  **/
  public int num_ways(int stairs){
    /**inefficient way**/
    // int numOfWays = 0;
    // if (stairs == 0 || stairs == 1){
    //   return 1;
    // }
    // numOfWays += num_ways(stairs-1) + num_ways(stairs-2);
    //
    // return numOfWays;

/**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**/
    /**efficient way**/

    /**
    can still be improved where only the two most recent
    values are stored within sumWays[] since not all values
    need to be stored
    **/

    // base case
    if (stairs == 0 || stairs == 1){
      return 1;
    }

    int sumWays[] = new int[stairs+1];
    sumWays[0] = 1;
    sumWays[1] = 1;
    for (int i = 2; i <= stairs; i++){
      sumWays[i] += sumWays[i-1] + sumWays[i-2];

    }

    return sumWays[stairs];

  }

}
