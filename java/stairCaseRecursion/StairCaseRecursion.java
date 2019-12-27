/*
 * Ciaran Sanders
 * Date: 12/26/2019
 * Stair Case Recursion problem as presented by CS Dojo on youtube
 * Video desciribing problem and solution: https://www.youtube.com/watch?v=5o-kdjv7FD0
 * This is my second attempt at the problem, I do not know/remember the solution
 * at the time of coding this
 */


public class StairCaseRecursion {

    /**
     * Given n stairs and x different possible step intervals,
     * find the number of different combinations of steps we can take
     * to get to the top of the staircase
     * @param n    The number of steps to the top of the staircase
     * @param x    Array of integers representing the possible step intervals
     * @return    The number of possible ways of reaching the top of the
     *            staircase given n and x
     */
    public int num_ways(int n, int[] x){
        int numWays = 0;
        for(int i : x){
            if((n-i) ==0){
                numWays++;
            }else if((n-i) > 0){
                numWays += num_ways(n-i, x);
            }
        }


        return numWays;
    }


}
