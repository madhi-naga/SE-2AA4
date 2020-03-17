/** 
 *  Author: Madhi Nagarajan
 *  Date: March 16, 2020
 *  
 *  Description: LanduseMapT inherits from the generic class, Seq2D.
 *  It handles only integer values.
 *
 */

package src;

import java.util.ArrayList;
import java.util.Collections;
import java.lang.Integer;

/** 
 *  @brief An ADT that represents a 2D matrix of integers
 */
public class DemT extends Seq2D<Integer> {

    /** 
     *  @brief A subclass constructor that inherits from Seq2D
     *  @param S A 2D ArrayList of Integers
     *  @param scl A double value that represents how much to scale each cell
     */   
    public DemT(ArrayList<ArrayList<Integer>> S, double scl) {
        super(S, scl);
    }

    /** 
     *  @brief Calculates the total of all values in the current matrix
     *  @return The integer sum of all values in the 2D matrix
     */ 
    public int total(){
        int sum = 0;
        for(int i = 0; i < this.getNumRow(); i++){
            for(int j = 0; j < this.getNumCol(); j++)
                sum += (int) this.s.get(i).get(j);
        }
        return sum;
    }

    /** 
     *  @brief Calculates the max value of the current matrix
     *  @return The max integer value of the 2D matrix
     */ 
    public Integer max(){
        int z = 0;
        Integer max = Collections.max(this.s.get(0));

        for(int i = 0; i < this.getNumRow(); i++){
            if (max < Collections.max(this.s.get(i))) 
                max = Collections.max(this.s.get(i));
        }
        return max;
    }

    /** 
     *  @brief Checks if the rows in the matrix are sorted in ascending order 
     *  by the sum of each row
     *  @return A boolean value of whether the rows are in ascending order (by sum)
     */ 
    public boolean ascendingRows(){
        int isum;
        int isum2;

        for(int i = 0; i <= this.getNumRow() - 2; i++){
            isum = 0;
            isum2 = 0;
            if(!this.validRow(i)) return false;
            for(int j = 0; j < this.getNumCol(); j++){
                isum += (int) this.s.get(i).get(j);
                isum2 += (int) this.s.get(i+1).get(j);
            }
            if(isum > isum2) return false;
        }
        return true;
        
    }

    private boolean validRow(int i){
        return i >= 0 && i <= this.getNumRow() - 1;
    }

    private boolean validCol(int i){
        return i >= 0 && i <= this.getNumCol() - 1;
    }

}