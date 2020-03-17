/** 
 *  Author: Madhi Nagarajan
 *  Date: March 16, 2020
 *  
 *  Description: Testing the DemT class
 *
 */

import org.junit.*;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import src.PointT;
import src.DemT;

public class TestDemT {
    private PointT p; 
    private DemT dem1;
    private DemT dem2;
    private ArrayList<ArrayList<Integer>> d1 = new ArrayList<ArrayList<Integer>>();
    private ArrayList<ArrayList<Integer>> d2 = new ArrayList<ArrayList<Integer>>();

    @Before
    public void setUp(){
        d1.add(new ArrayList<Integer>(Arrays.asList(3, 2, 6, 4)));
        d1.add(new ArrayList<Integer>(Arrays.asList(1, 7, 22, 3)));
        d1.add(new ArrayList<Integer>(Arrays.asList(-5, 1, -15, 4)));

        d2.add(new ArrayList<Integer>(Arrays.asList(0, 1, 6)));
        d2.add(new ArrayList<Integer>(Arrays.asList(3, 2, 7)));
        d2.add(new ArrayList<Integer>(Arrays.asList(12, 9, 3)));

        dem1 = new DemT(d1, 1.0);
        dem2 = new DemT(d2, 3.0);
    }

    @After
    public void tearDown(){
        dem1 = null; 
        dem2 = null; 
        d1 = null; 
        d2 = null;
    }

    @Test
    public void testTotal(){
        int t1 = dem1.total();
        assertEquals(t1, 33);
    }

    @Test
    public void testMax(){
        int m1 = dem1.max();
        assertEquals(m1, 22);
    }

    @Test
    public void testAscRows(){
        assertFalse(dem1.ascendingRows());
        assertTrue(dem2.ascendingRows());
    }

}