
import org.junit.*;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import src.Dots;
import src.DotsController;
import src.ColourT;

public class TestDots {
    private Dots dots;
    private ArrayList<ArrayList<ColourT>> arr;
    
    @Before
    public void setUp(){
        dots = new Dots(4);
        arr = new ArrayList<ArrayList<ColourT>>();

        arr.add(new ArrayList<ColourT>(Arrays.asList(ColourT.R, ColourT.G, ColourT.B, ColourT.Y)));
        arr.add(new ArrayList<ColourT>(Arrays.asList(ColourT.R, ColourT.G, ColourT.G, ColourT.P)));
        arr.add(new ArrayList<ColourT>(Arrays.asList(ColourT.B, ColourT.P, ColourT.P, ColourT.P)));
        arr.add(new ArrayList<ColourT>(Arrays.asList(ColourT.R, ColourT.G, ColourT.G, ColourT.G)));
        dots.setMatrix(arr);
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
        String[] path4 = {"00", "30"};
        assertFalse(dots.isValidPath(path4));
    }

    @Test
    public void testHasValidCombo(){
        assertTrue(dots.hasValidCombo());
    }
    
}