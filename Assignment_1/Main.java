public class Main {

    static final int PARTICLES_NR = 2;
    static Particle[] particles =  new Particle[PARTICLES_NR];

    static double[] globalBestPos;
    static double globalBestFitness;
    static int globalBestParticle;

    static double c1;
    static double c2;
    static double w;

    public static void main(String[] args) {
    
        int approach = Integer.parseInt(args[0]);
        int dim = Integer.parseInt(args[1]);
        int iterations = Integer.parseInt(args[2]);
        int lowerBound = Integer.parseInt(args[3]);
        int upperBound = Integer.parseInt(args[4]);
        c1 = Double.parseDouble(args[5]);
        c2 = Double.parseDouble(args[6]);
        
        //w = 0.5 * (c1 + c2) - 1;

        createSwarm(dim, lowerBound, upperBound);
        for (int itr = 0; itr < iterations; itr++) {

            fitnessEval(itr);

            printParticles();
            //printAvgFitness();
            //System.out.println(globalBestFitness);

            updateVelAndPos(dim);
        }
    }

    public static void updateVelAndPos(int dim) {
        for (int p = 0; p < PARTICLES_NR; p++) {

            double[] pos = particles[p].getPosition();
            double[] vel = particles[p].getVelocity();

            double[] new_pos = new double[dim];
            double[] new_vel = new double[dim];

            double[] bestPos = particles[p].getLocalBestPosition();

            for (int d = 0; d < dim; d++) {

                //Update Velocity
                double r1 = Math.random();
                double r2 = Math.random();

                new_vel[d] = (vel[d]) + (c1 * r1) * (bestPos[d] - pos[d]) + (c2 * r2) * (globalBestPos[d] - pos[d]);

                //Update Position
                new_pos[d] = pos[d] + new_vel[d];
            }

            particles[p].setVelocity(new_vel);
            particles[p].setPosition(new_pos);

        }
    }

    public static void createSwarm(int dim, int lowerBound, int upperBound) {
        // Init swarm particles
        for (int i = 0; i < PARTICLES_NR; i++) {
            particles[i] = new Particle(dim, lowerBound, upperBound);
        }
    }

    public static void fitnessEval(int itr) {

        if (itr != 0) {

            for (int i = 0; i < PARTICLES_NR; i++) {

                double fitness = EvalFunctions.absoluteValue(particles[i].getPosition());
                particles[i].setFitness(fitness, itr);

                updateGlobalBest(i, fitness);
            }

        } else {

            double fitness = EvalFunctions.absoluteValue(particles[0].getPosition());
            particles[0].setFitness(fitness, itr);

            globalBestFitness = fitness;
            globalBestParticle = 0;
            globalBestPos = particles[0].getPosition().clone();

            for (int i = 1; i < PARTICLES_NR; i++) {
                fitness = EvalFunctions.absoluteValue(particles[i].getPosition());
                particles[i].setFitness(fitness, itr);

                updateGlobalBest(i, fitness);
            }
        }

    }

    public static void updateGlobalBest(int i, double fitness) {
        if (fitness < globalBestFitness) {
            globalBestFitness = fitness;
            globalBestParticle = i;
            globalBestPos = particles[i].getPosition().clone();
        }
    }

    public static void printParticles() {

        String globalBestPosStr = "";
        for (int i = 0; i < globalBestPos.length; i++) {
            globalBestPosStr = globalBestPosStr + globalBestPos[i] + " ";
        }

        System.out.println("Global best:\tParticle: " + globalBestParticle + "; Pos: (" + globalBestPosStr + "); Fitness: " + globalBestFitness + "\n");
        for (int i = 0; i < PARTICLES_NR; i++) {
            System.out.println("\u001B[31mParticle " + i + "\u001B[0m\n" + particles[i].toString() + "\n");
        }
        System.out.println("---------------------------------------");
    }

    public static void printAvgFitness() {
        double sum = 0;
        for (int i = 0; i < PARTICLES_NR; i++) {
            sum = sum + particles[i].getFitness();
        }
        System.out.println(sum / PARTICLES_NR);
    }
}