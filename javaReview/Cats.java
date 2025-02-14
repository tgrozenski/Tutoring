public class Cats {

/** This will represent how many feet the cat can jump. */
private double jumpHeight;

/** The second value is the maximum number of pizzas the cat can eat. */
private int maxPizzas;

/** The third variable is how many pizzas the cat has currently eaten.  This is also an integer. */
private int pizzasAte;

// The last variable contains the cat's current position.   This variable is a double.  
private double position; 

/** Constructor */
// The constructor will take in 2 parameters: how high the cat can jump and how many pizzas it can eat. 
// The cat starts on the ground and has not eaten any pizzas.


public Cats(double jumpHeight, int maxPizzas){
    this.jumpHeight = jumpHeight;
    this.maxPizzas = maxPizzas;

    this.pizzasAte = 0;
    this.position = 0;
}

// public Cats(double jumpHeight, int maxPizzas, int pizzasAte, double position){
//     this.jumpHeight = jumpHeight;
//     this.maxPizzas = maxPizzas;
//     this.pizzasAte = pizzasAte;
//     this.position = position;
// }

/** instance methods */
// There will be 3 instance methods.  All three methods are accessible outside of the class. 

// The first one will be called getHeight, which takes no parameters and returns a double. 
// It will return the cat's current height.
public double getHeight() {
    return this.position;
}


Cats mycat = new Cats(10, 3);
//double height = mycat.height; // cant do this
//double height = mycat.getHeight(); // can do this
//mycat.setHeight(10); // can do this


// The second method is called getFull, which returns a double and tells the percentage of the cat's fullness.   
public double getFull(){
    double fullness = this.pizzasAte / this.maxPizzas * 100;
    return fullness;
    // return this.pizzasAte / this.maxPizzas * 100;
}

// The third method, called jump, takes in a double describing the height the cat wants to reach.   
// It will return a boolean value, with a true if it can reach it and a false if it cannot.   
// The cat's ability to jump is hindered based on how full it is.   
// The jump variable is multiplied by the percentage of how full the cat is.  
// If the cat is 0% full, it can jump to the full amount.  
// If the cat is 50% full, it can jump half that amount; if it is 100% full, it cannot.   
// It can always jump down, and the jump is based on the current height. 
public boolean jump(double targetHeight){

    // fullness, jump height = actualJumpHeight
    double actualJump = this.jumpHeight * this.getFull();
    // ==, <, >, >=, <=
    // return true or false
    if (targetHeight < this.position) { // jumping down
        //always true
        return true;
    }
    else if(actualJump + this.position >= targetHeight) { // jumping up, we can
        //we can make the jump
        return true; 
    }
    return false;
}

}
