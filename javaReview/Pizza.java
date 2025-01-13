public class Pizza {
    private String type;
    private final double size; 
    private final float price;


    public Pizza(String type, double size, float price) {
        this.type = type;
        this.size = size;
        this.price = price;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public double getSize() {
        return size;
    }
    
    public float getPrice() {
        return price;
    }
}
