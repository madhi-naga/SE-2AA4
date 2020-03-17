/** 
 *  Author: Madhi Nagarajan
 *  Date: March 16, 2020
 *  
 *  Description: LanduseMapT inherits from the generic class, Seq2D.
 *  It handles only LuT values.
 *
 */

package src;

import java.util.ArrayList;

import src.Seq2D;

/** 
 *  @brief An ADT that represents a 2D matrix wtih LuT values
 */
public class LanduseMapT extends Seq2D<LuT> {

    /** 
     *  @brief A subclass constructor that inherits from Seq2D
     *  @param S A 2D ArrayList of type LuT
     *  @param scl A double value that represents how much to scale each cell
    */
    public LanduseMapT(ArrayList<ArrayList<LuT>> S, double scl) {
        super(S, scl);
    }

}