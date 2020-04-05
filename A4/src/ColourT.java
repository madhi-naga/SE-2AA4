/**
 * Author: Madhi Nagarajan
 * 
 * Description: An enum class that represents colours on the Dots board
 */

package src;

import java.util.Random;

/**
 * @brief Defines the Enum type class for ColourT
 */
public enum ColourT {
    R,
    G,
    B,
    Y,
    P;

    /**
     * @brief Generates a random ColourT 
     */
    public static ColourT getRandomColour() {
        Random random = new Random();
        return values()[random.nextInt(values().length)];
    }
}