
import src.Dots;
import src.DotsController;
import src.DotsView;

public class DotsEngine {
    public static void main(String[] args) {
        Dots model = new Dots(5);
        DotsView view = new DotsView();
        DotsController cont = new DotsController(model, view);

        cont.startGame();
    }
}