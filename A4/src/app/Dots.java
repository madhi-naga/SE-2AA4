package app;

import java.util.ArrayList;

public class Dots {

    private ArrayList<ArrayList<ColourT>> matrix;
    private int n;

    public Dots(int n){
        this.matrix = new ArrayList<>();
        this.n = n;
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
        for (int i = 0; i < this.n; i++) {
            this.matrix.add(new ArrayList<ColourT>());
            for (int j = 0; j < this.n; j++) 
                addRandomColour(i, j);
        }
    }

    public void dropDots(){
        int emp;
        for(int i = 0; i < this.n; i++){
            emp = this.n-1;

            for(int j = this.n-1; j >=0; j--){
                if(this.getColour(j, i) != null){
                    this.matrix.get(emp).set(i, this.getColour(j, i));
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

}