package app;

import java.util.ArrayList;

public class Dots {

    private ArrayList<ArrayList<ColourT>> matrix;

    public Dots(){
        this.matrix = new ArrayList<>();
    }

    public ArrayList<ArrayList<ColourT>> matrix(){
        return this.matrix;
    }

    public ColourT getColour(int i, int j){
        return this.matrix.get(i).get(j);
    }

    public void setColour(int i, int j, ColourT c){
        this.matrix.get(i).set(j, c);
    }

    public void addRandomColour(int i, int j){
        this.matrix().get(i).add(ColourT.getRandomColour());
    }
    
    public void setRandomColour(int i, int j){
        this.matrix.get(i).set(j, ColourT.getRandomColour());
    }

    public void dropColour(int i, int j, int x){
        ColourT c = this.matrix.get(i-x).get(j);
        this.matrix.get(i).set(j, c);
    }

    public void initializeDots() {
        for (int i = 0; i < 3; i++) {
            this.matrix.add(new ArrayList<ColourT>());
            for (int j = 0; j < 3; j++) 
                addRandomColour(i, j);
        }
    }

}