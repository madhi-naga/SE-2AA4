package src;

import java.util.Collections;
import java.util.ArrayList;
import java.util.Comparator;

public class Seq1D<T extends Comparable<T>>{

    TieHandler tieHandler;
    ArrayList<T> s;

    public Seq1D(ArrayList<T> S, TieHandler t){
        this.s = S;
        this.tieHandler = t;
    }

    public void setTieHandler(TieHandler t){
        this.tieHandler = t;
    }

    public double rank(T p){
        if(count(p, this.s) == 0) throw new IllegalArgumentException();
        
        ArrayList<Integer> ind = indexSet(p, sort(this.s));
        ArrayList<Integer> ind2 = toSeq(ind);

        return this.tieHandler.rCalc(ind2);
    }

    private ArrayList<Integer> indexSet(T i, ArrayList<T> B){
        ArrayList<Integer> ret = new ArrayList<Integer>();
        for(int j = 0; j < B.size(); j++){
            if(i == B.get(j))
                ret.add(j);
        }
        return ret;
    }

    private ArrayList<T> sort(ArrayList<T> A){
        ArrayList<T> A2 = new ArrayList<T>();
        for(int i = 0; i < A.size(); i++)
            A2.add(A.get(i));
        Collections.sort(A2);
        return A2;
    }

    private int count(T a, ArrayList<T> A){
        int cnt = 0;
        for(int j = 0; j < A.size(); j++){
            if(a == A.get(j))
                cnt++;
        }
        return cnt;
    }

    private ArrayList<Integer> toSeq(ArrayList<Integer> A){
        return A;
    }

}