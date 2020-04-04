
import org.junit.*;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import app.Dots;
import app.DotsController;

public class TestDots {
    private Dots dots;
    
    @Before
    public void setUp(){
        Dots dots = new Dots(4);

        dots.matrix().add(new ArrayList<ColourT>(Arrays.asList(ColourT.R, ColourT.G, ColourT.B, ColourT.Y)));
        dots.matrix().add(new ArrayList<ColourT>(Arrays.asList(ColourT.R, ColourT.G, ColourT.G, ColourT.P)));
        dots.matrix().add(new ArrayList<ColourT>(Arrays.asList(ColourT.B, ColourT.P, ColourT.P, ColourT.P)));
        dots.matrix().add(new ArrayList<ColourT>(Arrays.asList(ColourT.R, ColourT.G, ColourT.G, ColourT.G)));
    }

    @After
    public void tearDown(){
        dots = null;
    }

    @Test
    public void testGetColour(){
        ColourT t = dots.getColour(0, 2);
        assertEquals(t, ColourT.B);
    }

    @Test
    public void testSetColour(){
        dots.setColour(3, 0, ColourT.B);
        assertEquals(dots.getColour(3, 0), ColourT.B);
    }

    @Test
    public void testIsValidPath(){
        String[] path1 = {"00", "01", "02"};
        assertFalse(dots.isValidPath(path1));
        String[] path2 = {"01", "11", "12"};
        assertTrue(dots.isValidPath(path2));
        String[] path3 = {"21", "22", "23", "13"};
        assertTrue(dots.isValidPath(path3));
        String[] path4 = {"00", "40"};
        assertFalse(dots.isValidPath(path4));
    }
}