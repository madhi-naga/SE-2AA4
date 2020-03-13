package src;

public class PointT {
    private final int r;
    private final int c;

    public PointT(int row, int col){
        this.r = row;
        this.c = col;
    }

    public int row(){
        return this.r;
    }
    public int col(){
        return this.c;
    }

    public PointT translate(int dr, int dc){
        PointT newP = new PointT(this.row() + dr, this.col() + dc);
        return newP;
    }
    
}