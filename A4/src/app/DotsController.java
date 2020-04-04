package app;

import java.util.concurrent.ThreadLocalRandom;

public class DotsController {

    private final Dots model;
    private final DotsView view;
    private String[] input;

    String infinite = "i";
    String target = "t";
    String esc = "e";

    public DotsController(Dots model, DotsView view) {
        this.model = model;
        this.view = view;
    }

    public boolean isValidInput(String buffer) {
        input = buffer.split(",");

        if (input == null || input.length < 2){
            return false;
        }

        for (String s : input) {
            if (s.length() > 2)
                return false;
            if (Character.getNumericValue(s.charAt(0)) > 5 || Character.getNumericValue(s.charAt(1)) > 5)
                return false;
        }
        return true;
    }

    public String[] toArray(String buffer) {
        return buffer.split(",");
    }

    public void startGame() {
        model.initializeDots();
        view.startMenu();

        String s = view.getInput();
               
        if (s.equals(infinite))
            InfiniteMode();
        else if(s.equals(target))
            TargetMode();
    }

    public void InfiniteMode(){
        int score = 0;
        while (true) {
            view.displayScore(score);
            view.renderDots(model);
            view.printEnterNewInput();
            String s = view.getInput();

            if (s.equals(esc))
                System.exit(0);

            if(this.isValidInput(s)){
                String[] input = this.toArray(s);
                if (model.isValidPath(input)){
                    model.processDots(input);
                    score += input.length;
                }
                else view.printInvalidMove();
            }
            else 
                view.printInvalidMove();
        }
        
    }

    public void TargetMode(){
        int score = 0;
        int target = ThreadLocalRandom.current().nextInt(20, 40);
        int movesleft = ThreadLocalRandom.current().nextInt(7, 15);
        boolean scoreReached = false;
        
        while (true) {
            if(score >= target){
                scoreReached = true;
                break;
            }

            if(movesleft == 0)
                break;    

            view.displayTarget(target);
            view.displayScore(score);
            view.displayMovesLeft(movesleft);
            view.renderDots(model);
            view.printEnterNewInput();
            
            String s = view.getInput();

            if (s.equals(esc))
                System.exit(0);

            if(this.isValidInput(s)){
                String[] input = this.toArray(s);
                if (model.isValidPath(input)){
                    model.processDots(input);
                    score += input.length;
                }
                else view.printInvalidMove();
            }
            else 
                view.printInvalidMove();

            movesleft--;
        }

        if(scoreReached)
            view.printScoreReached();
        else
            view.printMovesOut();

        System.exit(0);
    }
    

}