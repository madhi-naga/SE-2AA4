package app;

import java.util.concurrent.ThreadLocalRandom;

public class DotsEngine {
   
    String infinite = "i";
    String target = "t";
    String esc = "e";

    Dots model = new Dots(5);
    DotsView view = new DotsView();
    DotsController cont = new DotsController(model, view);

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

            String[] input = cont.processInput(s);
            if (cont.isValidPath(input)){
                cont.processDots(input);
                score += input.length;
            }
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

            String[] input = cont.processInput(s);
            if (cont.isValidPath(input)){
                cont.processDots(input);
                score += input.length;
            }
            movesleft--;
        }

        if(scoreReached)
            view.printScoreReached();
        else
            view.printMovesOut();

        System.exit(0);
    }
    
    public static void main(String[] args) throws Exception {
        DotsEngine d = new DotsEngine();
        d.startGame();
    }
}