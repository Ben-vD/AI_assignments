public class Main {

    static final int PARTICLES_NR = 30;
    static Particle[] particles =  new Particle[PARTICLES_NR];
    static double[] globalBestPos;
    
    public static void main(String[] args) {
    
        int approach = Integer.parseInt(args[0]);
        int dim = Integer.parseInt(args[1]);
        int iterations = Integer.parseInt(args[2]);
        int lowerBound = Integer.parseInt(args[3]);
        int upperBound = Integer.parseInt(args[4]);

        createSwarm(dim, lowerBound, upperBound);
        for (int itr = 0; itr < iterations; itr++) {

            fitnessEval();

            setGlobalBestPos();

            printParticles();

        }
    }

    public static void printParticles() {
        System.out.println("Global best:\t" + globalBestPos);
        for (int i = 0; i < PARTICLES_NR; i++) {
            System.out.println("\u001B[31mParticle " + i + "\u001B[0m\n" + particles[i].toString() + "\n");
        }
    }

    public static void setGlobalBestPos() {

        

    }

    public static void createSwarm(int dim, int lowerBound, int upperBound) {
        // Init swarm particles
        for (int i = 0; i < PARTICLES_NR; i++) {
            particles[i] = new Particle(dim, lowerBound, upperBound);
        }
    }

    public static void fitnessEval() {
        for (int i = 0; i < PARTICLES_NR; i++) {
            double fitness = EvalFunctions.absoluteValue(particles[i].getPosition());
            particles[i].setFitness(fitness);
        }
    }

}
