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
    public Particle(int dim, int lowerBound, int upperBound) {
        this.position = new double[dim];
        this.velocity = new double[dim];

        for (int i = 0; i < position.length; i++) {
            position[i] = (int) (Math.random() * (upperBound - lowerBound) + lowerBound);
        }

        localBestPosition = position.clone();

    }

    public double[] getPosition() {
        return position;
    }

    public void setPosition(double[] position) {
        this.position = position;
    }

    public double[] getVelocity() {
        return this.velocity;
    }

    public void setVelocity(double[] velocity) {
        this.velocity = velocity;
    }

    public double getFitness() {
        return this.fitness;
    }

    public void setFitness(double fitness, int itr) {
        if (itr != 0 && fitness < this.fitness) {
            localBestPosition = position.clone();
        }
        this.fitness = fitness;
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