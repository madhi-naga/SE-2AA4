package app;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class DotsView {


    public void startMenu() {
        System.out.println();
        System.out.println("Welcome to Dots!");
        System.out.println("To gain points, type coordinates (row location, column location) that are adjacent");
        System.out.println("(Eg. 00,01,11)");
        System.out.println("To play Infinite Mode, enter 'i'");
        System.out.println("To play Target Mode, enter 't'");
        System.out.println("To escape anytime, enter 'e'");
    }

    public void printEnterNewInput(){
        System.out.println("Enter your next move: ");
    }

    public void displayScore(int n){
        System.out.println("Your score: " + n);
    }
    public void displayTarget(int n){
        System.out.println("Target: " + n);
    }

    public void displayMovesLeft(int n){
        System.out.println("Your moves left: " + n);
    }

    public void printInvalidMove(){
        System.out.println("Invalid Move");
    }

    public void printScoreReached(){
        System.out.println("Congrats! You've beat the target score.");
    }
    
    public void printMovesOut(){
        System.out.println("You're out of moves. Better luck next time!");
    }

    public void renderDots(Dots dots) {
        System.out.println();
        int n = dots.matrix().size();
        
        System.out.print("   "); 
        for(int i = 0; i < n; i++)
            System.out.print(i + " ");
        System.out.println();

        for (int i = 0; i < n; i++) {
            System.out.print(i + "  ");
            for (int j = 0; j < n; j++) {
                System.out.print(dots.matrix().get(i).get(j).name() + " ");
            }
            System.out.println();
        }
    }

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