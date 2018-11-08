import java.util.*;

public class TestStairCaseRecursion{
    public static void main (String[] args){
      /** check if user input is correct**/
      int[] input = new int[args.length];
      if (!(input.length >= 2)){
        System.out.println("Usage [number of stairs] [step increments]");
        System.exit(0);
      }
      int[] increments = new int[args.length-1];
      for (int i = 1; i < args.length;i++){

        increments[i-1] = Integer.parseInt(args[i]);
      }

      int numOfStairs = Integer.parseInt(args[0]);
      StairCaseRecursion newSearch = new StairCaseRecursion();
      newSearch.num_ways(numOfStairs, increments);




    }
}
