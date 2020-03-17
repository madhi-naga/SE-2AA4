/** 
 *  Author: Madhi Nagarajan
 *  Date: March 16, 2020
 *  
 *  Description: Testing the PointT class
 *
 */


import org.junit.*;
import static org.junit.Assert.*;
import src.PointT;

public class TestPointT {
    private PointT p1; 
    private PointT p2; 
    private PointT pz = new PointT(0, 0);

    @Before
    public void setUp(){
        p1 = new PointT(3, 7);
        p2 = new PointT(-16, 35);
    }
    
    @After
    public void tearDown(){
        p1 = null;
        p2 = null;
        pz = null;
    }

    @Test
    public void testRow(){
        assertEquals(p1.row(), 3);
        assertEquals(p2.row(), -16);
        assertEquals(pz.row(), 0);
    }

    @Test
    public void testCol(){
        assertEquals(p1.col(), 7);
        assertEquals(p2.col(), 35);
        assertEquals(pz.col(), 0);
    }

    @Test
    public void testTranslate(){
        PointT p10 = p1.translate(pz.row(), pz.col());
        assertEquals(p10.row(), 3);
        assertEquals(p10.col(), 7);

        PointT p20 = p2.translate(100, -34);
        assertEquals(p20.row(), 84);
        assertEquals(p20.col(), 1);
    }


}