package src;

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

    public void setMatrix(ArrayList<ArrayList<ColourT>> c){
        this.matrix = c;
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

    public void initializeDots() {
        for (int i = 0; i < this.n; i++) {
            this.matrix.add(new ArrayList<ColourT>());
            for (int j = 0; j < this.n; j++) 
                addRandomColour(i, j);
        }
    }

    public boolean isValidPath(String[] input) {
        ColourT prevc = null;
        int previ = -1;
        int prevj = -1;
        int x = 0;

        for (String s : input) {
            int i = Character.getNumericValue(s.charAt(0));
            int j = Character.getNumericValue(s.charAt(1));

            if (x == 0) {
                prevc = this.matrix().get(i).get(j);
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

    public void processDots(String[] input) {
        for (String s : input) {
            int i = Character.getNumericValue(s.charAt(0));
            int j = Character.getNumericValue(s.charAt(1));
            this.setColour(i, j, null);
        }        
        this.dropDots();
    }

}