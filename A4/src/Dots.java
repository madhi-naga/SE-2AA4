/**
 * Author: Madhi Nagarajan
 * 
 * Description: An Model/ADT that represents the game board & pieces 
 * of the Dots Game
 */


package src;

import java.util.ArrayList;

public class Dots {

    private ArrayList<ArrayList<ColourT>> matrix;
    private int n;

    /**
   * @brief Initializes the Dots model
   * @param n The size of the Dots matrix board 
   */
    public Dots(int n){
        this.matrix = new ArrayList<>();
        this.n = n;
    }

    /**
   * @brief Returns a 2D array tha represents the Dots matrix board
   * @return The matrix board 
   */
    public ArrayList<ArrayList<ColourT>> matrix(){
        return this.matrix;
    }

    /**
   * @brief Returns the size of the Dots matrix board
   * @return The size of the Dots matrix board
   */
    public int n(){
        return this.n;
    }

    /**
   * @brief Returns the colour at a specific point in the matrix
   * @param i The ith row of the matrix
   * @param j The jth column of the matrix
   * @return The colour at position i,j in the matrix
   */
    public ColourT getColour(int i, int j){
        return this.matrix.get(i).get(j);
    }

    /**
   * @brief Sets an existing location to the given colour
   * @param i The ith row of the matrix
   * @param j The jth column of the matrix
   * @param c The colour to set, represented by ColourT
   */
    public void setColour(int i, int j, ColourT c){
        this.matrix.get(i).set(j, c);
    }

    /**
   * @brief Adds a new random colour to the matrix
   * @param i The ith row of the matrix
   * @param c The colour to set, represented by ColourT
   */
    public void addRandomColour(int i){
        this.matrix.get(i).add(ColourT.getRandomColour());
    }
    
    /**
   * @brief Sets an existing location to a random colour
   * @param i The ith row of the matrix
   * @param j The jth column of the matrix
   */
    public void setRandomColour(int i, int j){
        this.matrix.get(i).set(j, ColourT.getRandomColour());
    }

    /**
   * @brief Initializes a new Dots Matrix with random colours
   */
    public void initializeDots() {
        for (int i = 0; i < this.n; i++) {
            this.matrix.add(new ArrayList<ColourT>());
            for (int j = 0; j < this.n; j++) 
                addRandomColour(i);
        }
    }

    /**
   * @brief Checks if the given input is a valid path in the matrix
   * @param input The input entered by the player, represented by an array
   * @return A boolean based on whether the input is a valid path
   */
    public boolean isValidPath(String[] input) {
        ColourT prevc = null;
        int previ = -1;
        int prevj = -1;
        int x = 0;

        for (String s : input) {
            int i = Character.getNumericValue(s.charAt(0));
            int j = Character.getNumericValue(s.charAt(1));

            if (x == 0) {
                prevc = this.matrix.get(i).get(j);
            } else {
                if (this.getColour(i, j) != prevc)
                    return false;
                if(!(i == previ || j == prevj))
                    return false;
                if(i == previ && j == prevj)
                    return false;
                if(Math.abs(i - previ) > 1 || Math.abs(j - prevj) > 1)
                    return false;
            }
            previ = i;
            prevj = j;
            x++;
        }
        return true;
    }

    /**
   * @brief Modifies the matrix by moving down above elements to existing null spaces
   * in the matrix and fills rest of the elements (now null) with random colours 
   */
    private void dropDots(){
        int emp;
        for(int i = 0; i < this.n; i++){
            emp = this.n-1;

            for(int j = this.n-1; j >=0; j--){
                if(this.getColour(j, i) != null){
                    this.setColour(emp, i, this.getColour(j, i));
                    if(emp != j) 
                        this.setColour(j, i, null);
                    emp--;
                }
            }
        }   

        for(int i = 0; i < this.n; i++){
            for(int j = 0; j < this.n; j++){
                if(this.matrix.get(i).get(j) == null){
                    this.setRandomColour(i, j);
                }
            }
        }   
    }

    /**
   * @brief Clears (makes null) elements of the matrix based on a given path and 
   * drops the existing elements
   */
    public void processDots(String[] input) {
        for (String s : input) {
            int i = Character.getNumericValue(s.charAt(0));
            int j = Character.getNumericValue(s.charAt(1));
            this.setColour(i, j, null);
        }        
        this.dropDots();
    }

    public boolean hasValidCombo() {
        for(int i = 0; i < this.n - 1; i++){
            for(int j = 0; j < this.n - 1; j++){
                if(this.getColour(i, j) == this.getColour(i, j+1))
                    return true;
                if(this.getColour(i, j) == this.getColour(i+1, j))
                    return true;
            }
        }
        return false;
    }

}