package app;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class DotsView {


    public void startMenu() {
        System.out.println();
        System.out.println("Welcome to Dots!");
        System.out.println("To make connections, type coordinates that are adjacent in the specific order");
        System.out.println("To escape the game, enter 'e'");
        System.out.println("To start, enter 's'");
    }

    public void printEnterNewInput(){
        System.out.println("Enter new input: ");
    }

    public void renderDots(Dots dots) {
        System.out.println();
        System.out.println("   0 1 2 3 4");
        for (int i = 0; i < 3; i++) {
            System.out.print(i + "  ");
            for (int j = 0; j < 3; j++) {
                System.out.print(dots.matrix().get(i).get(j).name() + " ");
            }
            System.out.println();
        }
    }

    public String[] readInput() {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        String[] input = null;
        try {
            input = br.readLine().split(",");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return input;
    }

}