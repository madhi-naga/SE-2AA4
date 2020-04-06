/**
 * Author: Madhi Nagarajan
 * 
 * Description: The View module for the Dots Model 
 * which displays the game board and messages
 */

package src;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class DotsView {

    /**
   * @brief Displays the menu messages
   */
    public void startMenu() {
        System.out.println();
        System.out.println("Welcome to Dots!");
        System.out.println("To gain points, type coordinates by (column, row) that are adjacent");
        System.out.println("(Eg. 00,01,11)");
        System.out.println("To play Infinite Mode, enter 'i'");
        System.out.println("To play Target Mode, enter 't'");
        System.out.println("To escape anytime, enter 'e'");
    }

    /**
   * @brief Displays the enter new input message
   */
    public void printEnterNewInput(){
        System.out.println("Enter your next move: ");
    }

    /**
   * @brief Displays the current score message
   * @param n The given score
   */
    public void displayScore(int n){
        System.out.println("Your score: " + n);
    }

    /**
   * @brief Displays the target score message
   * @param n The given target
   */
    public void displayTarget(int n){
        System.out.println("Target: " + n);
    }

    /**
   * @brief Displays the moves left message
   * @param n The given moves left
   */
    public void displayMovesLeft(int n){
        System.out.println("Your moves left: " + n);
    }

    /**
   * @brief Displays the invalid move message
   */
    public void printInvalidMove(){
        System.out.println("Invalid Move");
    }

    /**
   * @brief Displays the reshuffled message
   */
    public void printReshuffled() {
        System.out.println("Reshuffled the Board!");
    }

    /**
   * @brief Displays the score reached message
   */
    public void printScoreReached(){
        System.out.println("Congrats! You've beat the target score.");
    }
    
    /**
   * @brief Displays the moves out message
   */
    public void printMovesOut(){
        System.out.println("You're out of moves. Better luck next time!");
    }

    /**
   * @brief Displays the Dots board layout and its elements
   * @param dots A given model of the Dots game
   */
    public void renderDots(ArrayList<ArrayList<ColourT>> board) {
        System.out.println();
        int n = board.size();
        
        System.out.print("   "); 
        for(int i = 0; i < n; i++)
            System.out.print(i + " ");
        System.out.println();

        for (int i = 0; i < n; i++) {
            System.out.print(i + "  ");
            for (int j = 0; j < n; j++) {
                System.out.print(board.get(i).get(j).name() + " ");
            }
            System.out.println();
        }
    }

     /**
   * @brief Receives the console Stinput from the user
   * @return The console input entered by the user
   */
    public String getInput() {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        String input = null;
        try {
            input = br.readLine();
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println();
        return input;
    }

}