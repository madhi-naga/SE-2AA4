package src;

import java.util.ArrayList;
import java.util.Collections;
import java.lang.Integer;


public class DemT extends Seq2D<Integer> {

    public DemT(ArrayList<ArrayList<Integer>> S, double scl) {
        super(S, scl);
    }

    public int total(){
        int z = 0;
        int sum = 0;
        for(int i = 0; i < this.getNumRow(); i++){
            for(int j = 0; j < this.getNumCol(); j++){
                sum = sum + (int) this.s.get(i).get(j);
            }
        }
        return sum;
    }

    public Integer max(){
        int z = 0;
        Integer max = Collections.max(this.s.get(0));

        for(int i = 0; i < this.getNumRow(); i++){
            if (max < Collections.max(this.s.get(i))) 
                max = Collections.max(this.s.get(i));
        }
        return max;
    }

    public boolean ascendingRows(){
        int isum = 0;
        int isum2 = 0;

        for(int i = 0; i <= this.getNumRow() - 2; i++){
            if(!this.validRow(i)) return false;
            for(int j = 0; j < this.getNumCol(); j++){
                isum += (int) this.s.get(i).get(j);
                isum2 += (int) this.s.get(i+1).get(j);
            }
            if(isum > isum2) return false;
        }
        return true;
        
    }

    private boolean validRow(int i){
        return i >= 0 && i <= this.getNumRow() - 1;
    }

    private boolean validCol(int i){
        return i >= 0 && i <= this.getNumCol() - 1;
    }

}