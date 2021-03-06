/** 
 *  Author: Madhi Nagarajan
 *  Date: March 16, 2020
 *  
 *  Description: Testing the LanduseMapT class
 *
 */

import org.junit.*;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import src.LuT;
import src.LanduseMapT;
import src.PointT;

public class TestLanduseMapT {

    private LanduseMapT lum1; 
    private LanduseMapT lum2; 
    private PointT p1; 
    private ArrayList<ArrayList<LuT>> m1 = new ArrayList<ArrayList<LuT>>();
    private double one = 1.0;
    private PointT pz = new PointT(0, 0);
    private double tol = 0.1; //for tolerance parameter

    @Before
    public void setUp(){
        m1.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.R, LuT.C, LuT.R)));
        m1.add(new ArrayList<LuT>(Arrays.asList(LuT.C, LuT.T, LuT.A, LuT.A)));
        m1.add(new ArrayList<LuT>(Arrays.asList(LuT.C, LuT.T, LuT.A, LuT.A)));
        lum1 = new LanduseMapT(m1, one);
        lum2 = new LanduseMapT(m1, 8.51);
    }

    @After
    public void tearDown(){
        lum1 = null; 
        lum2 = null; 
        p1 = null; 
        m1 = null;
    }

    @Test (expected=IllegalArgumentException.class)
    public void testConsExcScl(){
        LanduseMapT scltest = new LanduseMapT(m1, 0);
        LanduseMapT scltest2 = new LanduseMapT(m1, -5.5);
    }

    @Test (expected=IllegalArgumentException.class)
    public void testConsExcEmpty(){ 
        ArrayList<ArrayList<LuT>> m2 = new ArrayList<ArrayList<LuT>>();
        LanduseMapT lum3 = new LanduseMapT(m2, 1);

    }

    @Test (expected=IllegalArgumentException.class)
    public void testConsExcEmpty2(){ 
        ArrayList<ArrayList<LuT>> m2 = new ArrayList<ArrayList<LuT>>();
        m2.add(new ArrayList<LuT>(Arrays.asList()));
        LanduseMapT lum3 = new LanduseMapT(m2, 1);
    }

    @Test (expected=IllegalArgumentException.class)
    public void testConsExcUneven(){ 
        ArrayList<ArrayList<LuT>> m2 = new ArrayList<ArrayList<LuT>>();
        m2.add(new ArrayList<LuT>(Arrays.asList(LuT.C, LuT.T, LuT.A, LuT.A)));
        m2.add(new ArrayList<LuT>(Arrays.asList(LuT.C, LuT.T, LuT.A)));
        LanduseMapT lum3 = new LanduseMapT(m2, 1);
    }


    @Test
    public void testGet(){
        p1 = new PointT(1, 3);
        LuT g1 = lum1.get(p1);
        LuT g2 = lum1.get(pz);
        assertEquals(g1, LuT.A);
        assertEquals(g2, LuT.T);
    }

    @Test (expected=IndexOutOfBoundsException.class)
    public void testGetExc(){
        lum1.get(new PointT(10, 23)); 
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

    @Test (expected=IndexOutOfBoundsException.class)
    public void testSetExc(){
        lum1.set(new PointT(15, 21), LuT.C); 
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
        assertEquals(lum1.getScale(), one, tol);
    }

    @Test
    public void testCountRow(){
        int c1 = lum1.countRow(LuT.C, 1);
        int c2 = lum1.countRow(LuT.A, 0);
        assertEquals(c1, 1);
        assertEquals(c2, 0);
    }

    @Test (expected=IndexOutOfBoundsException.class)
    public void testCountRowExc(){
        lum1.countRow(LuT.T, 5);
    }

    @Test
    public void testCount(){
        int c1 = lum1.count(LuT.T);
        int c2 = lum1.count(LuT.A);
        assertEquals(c1, 3);
        assertEquals(c2, 4);
    }

    
    @Test
    public void testArea(){
        double a1 = lum2.area(LuT.T);
        double a2 = lum2.area(LuT.A);
        assertEquals(a1, 217.26, tol);
        assertEquals(a2, 289.68, tol);
    }

}