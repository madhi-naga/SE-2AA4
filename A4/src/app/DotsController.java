package app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class DotsController {

    private final Dots model;
    private final DotsView view;
    private final BufferedReader br;
    private String[] input;
    String start = "s";
    String esc = "e";

    public DotsController(final Dots model, final DotsView view) {
        this.model = model;
        this.view = view;
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public String getInput() {
        String s = null;
        try {
            s = br.readLine();
        } catch (final Exception e) {
            e.printStackTrace();
        }
        return s;
    }

    public String[] processInput(final String buffer) {

        try {
            input = buffer.split(",");
        } catch (final Exception e) {
            e.printStackTrace();
        }

        if (input == null || input.length < 2)
            throw new IllegalArgumentException();

        for (final String s : input) {
            if (s.length() > 2)
                throw new IllegalArgumentException();
            if (Character.getNumericValue(s.charAt(0)) > 5 || Character.getNumericValue(s.charAt(1)) > 5)
                throw new IllegalArgumentException();
        }
        return input;
    }

    public boolean checkPath(String[] input) {
        ColourT colour = null;
        int previ = -1;
        int prevj = -1;
        int x = 0;

        for (String s : input) {
            int i = Character.getNumericValue(s.charAt(0));
            int j = Character.getNumericValue(s.charAt(1));

            if (x == 0) {
                colour = model.matrix().get(i).get(j);
                previ = i;
                prevj = j;
                // model.setRandomColour(i, j);
            } else {
                if (model.matrix().get(i).get(j) != colour) {
                    System.out.println("Invalid input");
                    return false;
                }

                if (!(i == previ || j == prevj)) {
                    System.out.println("Invalid input");
                    return false;
                }
                // model.setRandomColour(i, j);
                previ = i;
                prevj = j;
            }
            x++;
        }
        return true;
    }

    public void processDots(String[] input) {
        int previ = -1;
        int col = 1;
        for (String s : input) {
            int i = Character.getNumericValue(s.charAt(0));
            int j = Character.getNumericValue(s.charAt(1));

            if (previ != -1) {
                if (previ == i)
                    col++;
                else
                    col = 1;

                if (i == 0)
                    model.setRandomColour(i, j);
                else {
                    for (int x = 0; x < i; x++) {
                        if (i - x == 0)
                            model.setRandomColour(i - x, j);
                        else
                            model.dropColour(i - x, j, col);
                    }
                }
            }
            previ = i;
        }
    }

    public void runGame() {
        view.startMenu();
        String s = this.getInput();
        if (s.equals(start)) {
            while (true) {
                model.initializeDots();
                view.renderDots(model);
                view.printEnterNewInput();
                s = getInput();

                if (s.equals(esc))
                    System.exit(0);

                String[] input = processInput(s);
                if (checkPath(input))
                    processDots(input);
            }
        }
    }

}