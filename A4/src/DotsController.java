/**
 * Author: Madhi Nagarajan
 * 
 * Description: The Controller Module of the Dots Model 
 * which communicates between and updates the model and view 
 * to run the Dots game 
 */


package src;

public class DotsController {

    private Dots model;
    private final DotsView view;
    private String[] input;

    String infinite = "i";
    String target = "t";
    String esc = "e";

    /**
   * @brief Constructor for the Dots Game Controller
   * @param model The Dots model
   * @param view The Dots view
   */
    public DotsController(Dots model, DotsView view) {
        this.model = model;
        this.view = view;
    }

    /**
   * @brief Checks if the given input is a valid sequence of coordinates
   * @param buffer The input given
   * @return A boolean based on if the given input is a valid sequence of coordinates
   */
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

    /**
   * @brief Splits and returns an array of the input given
   * @param buffer The input givennah 
   * @return An array of the input given
   */
    public String[] toArray(String buffer) {
        return buffer.split(",");
    }

    /**
   * @brief Begins the Dots game
   */
    public void startGame() {
        model.initializeDots();

        while(!model.hasValidCombo()){
            int n = model.n();
            model = new Dots(n);
            model.initializeDots();
        }

        view.startMenu();

        String s = view.getInput();
               
        if (s.equals(infinite))
            InfiniteMode();
        else if(s.equals(target))
            TargetMode();
    }

    /**
   * @brief The Infinite game mode of Dots
   */
    public void InfiniteMode(){
        int score = 0;
        while (true) {
            view.displayScore(score);
            view.renderDots(model);
            view.printEnterNewInput();
            String s = view.getInput();

            if (s.equals(esc))
                System.exit(0);
            
            if(!model.hasValidCombo()){
                int n = model.n();
                model = new Dots(n);
                model.initializeDots();
                view.printReshuffled();
                continue;
            }

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

    /**
   * @brief The Targel game mode of Dots; Player needs to beat the target score 
   * with a limited amount of moves
   */
    public void TargetMode(){
        int score = 0;
        int target = (int) (Math.random() * (30));
        int movesleft = (int) (target/2.3);
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