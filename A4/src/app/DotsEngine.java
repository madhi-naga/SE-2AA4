
import app.Dots;
import app.DotsController;
import app.DotsView;

public class DotsEngine {
    public static void main(String[] args) {
        Dots model = new Dots(5);
        DotsView view = new DotsView();
        DotsController cont = new DotsController(model, view);

        cont.startGame();
    }
}