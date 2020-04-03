package app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class DotsController {

    private final Dots model;
    private final DotsView view;
    private String[] input;

    public DotsController(final Dots model, final DotsView view) {
        this.model = model;
        this.view = view;
    }

    public String[] processInput(String buffer) {
        input = buffer.split(",");

        if (input == null || input.length < 2)
            throw new IllegalArgumentException();

        for (String s : input) {
            if (s.length() > 2)
                throw new IllegalArgumentException();
            if (Character.getNumericValue(s.charAt(0)) > 5 || Character.getNumericValue(s.charAt(1)) > 5)
                throw new IllegalArgumentException();
        }
        return input;
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
                prevc = model.matrix().get(i).get(j);
            } else {
                if ((model.getColour(i, j) != prevc) || !(i == previ || j == prevj)
                     || (i == previ && j == prevj)) {
                    view.printInvalidMove();
                    return false;
                }
            }
            previ = i;
            prevj = j;
            x++;
        }
        return true;
    }

    public void processDots(String[] input) {
        for (String s : input) {
            int i = Character.getNumericValue(s.charAt(0));
            int j = Character.getNumericValue(s.charAt(1));
            model.setColour(i, j, null);
        }        
        model.dropDots();
    }
}