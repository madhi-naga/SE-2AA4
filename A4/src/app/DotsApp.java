import app.Dots;
import app.DotsController;
import app.DotsView;
import app.DotsEngine;

public class DotsApp {
    public static void main(String[] args) {
        DotsEngine d = new DotsEngine();
        d.startGame();
    }
}