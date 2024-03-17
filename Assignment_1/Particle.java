public class Particle {


    private double position[];
    private double velocity[];
    private double fitness;
    
    private double localBestPosition[];
    private double localBestFitness;

    private double upperBound;
    private double lowerBound;

    private boolean feasiblePos;

    /**
     * Constructor for the particle.
     * 
     * @param dim
     * @param lowerBound
     * @param upperBound
     */
    public Particle(int dim, double lowerBound, double upperBound, int evalFunction) {
        this.position = new double[dim];
        this.velocity = new double[dim];

        this.upperBound = upperBound;
        this.lowerBound = lowerBound;

        feasiblePos = true;

        for (int i = 0; i < position.length; i++) {
            position[i] =  (Math.random() * (upperBound - lowerBound) + lowerBound);
        }
        localBestPosition = position.clone();

        switch (evalFunction) {
            case 0:
            fitness = EvalFunctions.AbsoluteValue(position);
                break;
            case 1:
            fitness = EvalFunctions.Ackley1(position);
                break;
            case 2:
            fitness = EvalFunctions.Alpine1(position);
                break;    
            case 3:
            fitness = EvalFunctions.Alpine2(position);
                break;
            case 4:
            fitness = EvalFunctions.Step2(position);
                break;
            case 5:
            fitness = EvalFunctions.Schwefel2_23(position);
                break; 
            case 6:
            fitness = EvalFunctions.Step3(position);
                break;
            case 7:
            fitness = EvalFunctions.Shubert4(position);
                break;
            case 8:
            fitness = EvalFunctions.Discus(position);
                break;
            case 9:
            fitness = EvalFunctions.EggCrate(position);
                break; 
            case 10:
            fitness = EvalFunctions.Deb1(position);
                break; 
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

        //Infinity Roaming fix
            feasiblePos = true;
        for (int i = 0; i < position.length; i++) {
            if (position[i] > upperBound || position[i] < lowerBound) {
                feasiblePos = false;
                break;
            }
        }

        if (feasiblePos) {
            if (fitness < localBestFitness) {
                localBestFitness = fitness;
                localBestPosition = position.clone();
            }
        }
        this.fitness = fitness;
    }

    public boolean getFeasiblePos() {
        return feasiblePos;
    }

    public double getLocalBestFitness() {
        return localBestFitness;
    }

    public double[] getLocalBestPosition() {
        return localBestPosition;
    }

    public String stringPositions() {
        String s = "";
        for (int i = 0; i < position.length; i++) {
            s = s + "," + position[i];
        }
        return s;
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