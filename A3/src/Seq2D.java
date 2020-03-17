/** 
 *  Author: Madhi Nagarajan
 *  Date: March 16, 2020
 *  
 *  Description: Seq2D is a generic class that creates a 2D matrix (or array)
 *
 */

package src;

import java.util.ArrayList;

/** 
 *  @brief A generic ADT that represents a 2D matrix
 */
public class Seq2D<T> {

    protected final ArrayList<ArrayList<T>> s;
    private final double scale; 
    private final int nRow;
    private final int nCol;

    /** 
     *  @brief Constructor for Seq2D
     *  @param S A 2D ArrayList of a generic type
     *  @param scl A double value that represents how much to scale each cell
     *  @throws IllegalArgumentException If the scale is below 0, 
     *  if the matrix is empty or if the rows have an uneven number of cells
     */
    public Seq2D(ArrayList<ArrayList<T>> S, double scl) {

        if(scl <= 0 || S.size() == 0 || S.get(0).size() == 0)
            throw new IllegalArgumentException();

        for(int i = 1; i < S.size(); i++)
            if(S.get(0).size() != S.get(i).size())
                throw new IllegalArgumentException();

        this.s = S;
        this.scale = scl;
        this.nRow = S.size();
        this.nCol = S.get(0).size();
    }

    /** 
     *  @brief Returns the value of a cell at a certain point
     *  @param p A point represented by PointT
     *  @return The value of a cell at the point p
     *  @throws IndexOutOfBoundsException If the given point p is not 
     *  in a valid cell of the matrix
     */
    public T get(PointT p) {
        if(!this.validPoint(p)) throw new IndexOutOfBoundsException();
        return this.s.get(p.row()).get(p.col());
    }

    /** 
     *  @brief Sets the value of a point p equal to v
     *  @param p A point represented by PointT
     *  @param v A generic value 
     *  @throws IndexOutOfBoundsException If the given point p is not 
     *  in a valid cell of the matrix
     */
    public void set(PointT p, T v) {
        if(!this.validPoint(p)) throw new IndexOutOfBoundsException();
        this.s.get(p.row()).set(p.col(), v);
    }

    /** 
     *  @brief Getter method for the number of rows
     *  @return The number of rows in the current 2D matrix
     */
    public int getNumRow(){
        return this.nRow;
    }

    /** 
     *  @brief Getter method for the number of columns
     *  @return The number of columns in the current 2D matrix
     */
    public int getNumCol(){
        return this.nCol;
    }
    
    /** 
     *  @brief Getter method for the scale of the 2D matrix
     *  @return The scale of the matrix
     */
    public double getScale(){
        return this.scale;
    }

    /** 
     *  @brief Calculates the number of times a value occurs in the current matrix
     *  @param T A generic value to be checked
     *  @return The number of times T occurs in the current matrix
     */
    public int count(T T){
        int cnt = 0;
        for(int i = 0; i < nRow; i++)
            cnt += countRow(T, i);           
        return cnt;
    }

    /** 
     *  @brief Calculates the number of times a value occurs in the given row
     *  @param T A generic value to be checked
     *  @param i The location of the row
     *  @return The number of times T occurs in a given row i
     *  @throws IndexOutOfBoundsException If the given row i is not valid
     *  in the current matrix
     */
    public int countRow(T T, int i) {
        if(!this.validRow(i)) throw new IndexOutOfBoundsException();
        int cnt = 0;
        for(int j = 0; j < nCol; j++){
            if(s.get(i).get(j).equals(T)) cnt++; 
        }
        return cnt;
    }

    /** 
     *  @brief Calculates the area covered by points that contain the same value
     *  @param T A generic value to be checked
     *  @return The area covered by T in a 2D matrix
     */
    public double area(T T){
        return this.count(T)*(Math.pow(scale,2));
    }

    private boolean validRow(int i){
        return i >= 0 && i <= this.nRow - 1;
    }

    private boolean validCol(int i){
        return i >= 0 && i <= this.nCol - 1;
    }

    private boolean validPoint(PointT p){
        return this.validRow(p.row()) && this.validCol(p.col());
    }

}