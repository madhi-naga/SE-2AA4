import org.junit.*;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import src.LuT;
import src.LanduseMapT;
import src.PointT;

public class TestLanduseMapT {

    private LanduseMapT lum1; 
    private PointT p1; 
    private ArrayList<ArrayList<LuT>> m1 = new ArrayList<ArrayList<LuT>>();
    private double one = 1.0;
    private PointT pz = new PointT(0, 0);

    @Before
    public void setUp(){
        m1.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.R, LuT.C, LuT.R)));
        m1.add(new ArrayList<LuT>(Arrays.asList(LuT.C, LuT.T, LuT.A, LuT.A)));
        m1.add(new ArrayList<LuT>(Arrays.asList(LuT.C, LuT.T, LuT.A, LuT.A)));
        lum1 = new LanduseMapT(m1, one);
    }

    @After
    public void tearDown(){

    }

    @Test
    public void testGet(){
        p1 = new PointT(1, 3);
        LuT g1 = lum1.get(p1);
        LuT g2 = lum1.get(pz);
        assertEquals(g1, LuT.A);
        assertEquals(g2, LuT.T);
    }

    @Test
    public void testSet(){
        p1 = new PointT(2, 3);
        lum1.set(pz, LuT.R);
        lum1.set(p1, LuT.C);
        LuT g1 = lum1.get(pz);
        LuT g2 = lum1.get(p1);
        assertEquals(g1, LuT.R);
        assertEquals(g2, LuT.C);
    }

    @Test
    public void testGetNumRow(){
        assertEquals(lum1.getNumRow(), 3);
    }

    @Test
    public void testGetNumCol(){
        assertEquals(lum1.getNumCol(), 4);
    }

    @Test
    public void testGetScale(){
        double n = 1.3;
        assertEquals(lum1.getNumCol(), n);
    }

    @Test
    public void testGetCount(){
        
    }

}