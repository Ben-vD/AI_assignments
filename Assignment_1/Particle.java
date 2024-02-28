public class Particle {


    private double position[];
    private double velocity[];
    private double fitness;
    
    private double localBestPosition[];
    private double localBestFitness;

    /**
     * Constructor for the particle.
     * 
     * @param dim
     * @param lowerBound
     * @param upperBound
     */
    public Particle(int dim, int lowerBound, int upperBound, int evalFunction) {
        this.position = new double[dim];
        this.velocity = new double[dim];

        for (int i = 0; i < position.length; i++) {
            position[i] = (int) (Math.random() * (upperBound - lowerBound) + lowerBound);
        }
        localBestPosition = position.clone();

        switch (evalFunction) {
            case 0:
            fitness = EvalFunctions.absoluteValue(position);
                break;
            case 1:
            fitness = EvalFunctions.Ackley1(position);
            default:
                break;
        }
        this.localBestFitness = fitness;
    }

    public double[] getPosition() {
        return position;
    }

    public void setPosition(double[] position) {
        this.position = position.clone();
    }

    public double[] getVelocity() {
        return velocity;
    }

    public void setVelocity(double[] velocity) {
        this.velocity = velocity.clone();
    }

    public double getFitness() {
        return fitness;
    }

    public void setFitness(double fitness) {

        if (fitness < localBestFitness) {
            localBestFitness = fitness;
            localBestPosition = position.clone();
        }
        this.fitness = fitness;
    }

    public double getLocalBestFitness() {
        return localBestFitness;
    }

    public double[] getLocalBestPosition() {
        return localBestPosition;
    }

    @Override
    public String toString() {
        
        String s = "Position:\t";
        for (int i = 0; i < position.length; i++) {
            s = s + position[i] + " ";
        }

        s = s + "\nVelocity:\t";
        for (int i = 0; i < position.length; i++) {
            s = s + velocity[i] + " ";
        }
        
        s = s + "\nLocal Best Position:\t";
        for (int i = 0; i < position.length; i++) {
            s = s + localBestPosition[i] + " ";
        }

        s = s + "\nFitness:\t" + fitness;

        return s;
    }
}