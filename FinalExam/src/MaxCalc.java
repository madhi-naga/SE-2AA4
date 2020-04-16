package src;

import java.util.Collections;
import java.util.ArrayList;

public class MaxCalc implements TieHandler {

    @Override
    public double rCalc(ArrayList<Integer> s) {
        double max = s.get(0);
        for(int i = 1; i < s.size(); i++ ){
            if(s.get(i) > max)
                max = s.get(i);
        }
        return max;
    }


}