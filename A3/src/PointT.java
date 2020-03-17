/** 
 *  Author: Madhi Nagarajan
 *  Date: March 16, 2020
 *  
 *  Description: PointT is an ADT of a point (row and column) 
 *  on a matrix/table
 *
 */


package src;

/** 
 *  @brief An ADT that represents a point on a matrix/table
 */
public class PointT {
    private final int r;
    private final int c;

    /** 
     *  @brief Constructor for PointT
     *  @param r The location of the row that a point is on
     *  @param c The location of the column that a point is on
     */
    public PointT(int row, int col){
        this.r = row;
        this.c = col;
    }

    /** 
     *  @brief Getter method for the current row
     *  @return The location of the row that the current point is on
     */
    public int row(){
        return this.r;
    }

    /** 
     *  @brief Getter method for the current column
     *  @return The location of the column that the current point is on
     */
    public int col(){
        return this.c;
    }

    /** 
     *  @brief Translates the current point by a certain num of rows and cols
     *  @param dr Delta R; how much rows that a point should be translated
     *  @param dc Delta C; how much columns that a point should be translated
     *  @return The translated point based on the original point 
     */
    public PointT translate(int dr, int dc){
        PointT newP = new PointT(this.row() + dr, this.col() + dc);
        return newP;
    }
    
}