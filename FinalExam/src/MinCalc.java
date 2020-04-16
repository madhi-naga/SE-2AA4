package src;

import java.util.Collections;
import java.util.ArrayList;

public class MinCalc implements TieHandler {

    @Override
    public double rCalc(ArrayList<Integer> s) {
        double min = s.get(0);
        for(int i = 1; i < s.size(); i++ ){
            if(s.get(i) < min)
                min = s.get(i);
        }
        return min;
    }

}