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
 *  @brief An ADT that represents a 2D matrix
 */
public class Seq2D<T> {

    protected final ArrayList<ArrayList<T>> s;
    private final double scale; 
    private final int nRow;
    private final int nCol;

    /** 
     *  @brief An ADT that represents a 2D matrix
     *  @param S A 2D array of a generic type
     *  @param scl A double value that represents how much to scale each cell
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

    public T get(PointT p) {
        if(!this.validPoint(p)) throw new IndexOutOfBoundsException();
        return this.s.get(p.row()).get(p.col());
    }

    public void set(PointT p, T v) {
        if(!this.validPoint(p)) throw new IndexOutOfBoundsException();
        this.s.get(p.row()).set(p.col(), v);
    }

    public int getNumRow(){
        return this.nRow;
    }

    public int getNumCol(){
        return this.nCol;
    }
    
    public double getScale(){
        return this.scale;
    }

    public int count(T T){
        int cnt = 0;
        for(int i = 0; i < nRow; i++)
            cnt += countRow(T, i);           
        return cnt;
    }

    public int countRow(T T, int i) {
        if(!this.validRow(i)) throw new IndexOutOfBoundsException();
        int cnt = 0;
        for(int j = 0; j < nCol; j++){
            if(s.get(i).get(j).equals(T)) cnt++; 
        }
        return cnt;
    }

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