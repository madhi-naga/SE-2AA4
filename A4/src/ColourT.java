package src;

import java.util.Random;

public enum ColourT {
    R,
    G,
    B,
    Y,
    P;

    public static ColourT getRandomColour() {
        Random random = new Random();
        return values()[random.nextInt(values().length)];
    }
}