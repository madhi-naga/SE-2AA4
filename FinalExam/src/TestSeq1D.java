package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

public class TestSeq1D
{

   ArrayList<Integer> a1;
   ArrayList<Integer> a2;
   ArrayList<Integer> a3;

   Seq1D<Integer> s1;
   Seq1D<Integer> s2;
   Seq1D<Integer> s3;
   Seq1D<Integer> s4;

   @Before
   public void setup()
   {
      MinCalc min = new MinCalc();
      MaxCalc max = new MaxCalc();
      a1 = new ArrayList<Integer>(Arrays.asList(3,5,5,6,8,9));
      a2 = new ArrayList<Integer>(Arrays.asList(1,1,1,2,0,1,1));
      a3 = new ArrayList<Integer>(Arrays.asList(3,5,5,6,8,9));
   
      s1 = new Seq1D<Integer>(a1, min);
      s2 = new Seq1D<Integer>(a1, max);
      s3 = new Seq1D<Integer>(a2, min);
      s4 = new Seq1D<Integer>(a2, max);
   }

   @After
   public void tearDown()
   {
      a1 = null;
      a2 = null;
      a3 = null;

      s1 = null;
      s2 = null;
      s3 = null;
      s4 = null;

   }

   @Test
   public void testRank()
   {
      assertEquals(s1.rank(5), 1, 0.1);
      assertEquals(s2.rank(5), 2, 0.1);

      assertEquals(s1.rank(9), 5, 0.1);
      assertEquals(s2.rank(9), 5, 0.1);

      assertEquals(s3.rank(1), 1, 0.1);
      assertEquals(s4.rank(1), 5, 0.1);

   }

   @Test (expected=IllegalArgumentException.class)
   public void testRankExc(){
      s1.rank(10);
      s2.rank(10);
   }


}
