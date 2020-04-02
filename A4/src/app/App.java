package app;

public class App {
    public static void main(String[] args) throws Exception {
        Dots model = new Dots();
        DotsView view = new DotsView();
        DotsController cont = new DotsController(model, view);
        cont.runGame();
    }
}