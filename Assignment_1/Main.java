public class Main {

    static final int PARTICLES_NR = 30;
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
        w = Double.parseDouble(args[7]);
        int evalFunction = Integer.parseInt(args[8]);

        createSwarm(dim, lowerBound, upperBound, evalFunction);
        for (int itr = 0; itr < iterations; itr++) {

            fitnessEval(evalFunction);

            //printParticles();
            //printAvgFitness();
            printParticleCoords(itr);
            //System.out.println(globalBestFitness);

            updateVelAndPos(dim);
        }
    }

    public static void updateVelAndPos(int dim) {
        for (int p = 0; p < PARTICLES_NR; p++) {

            double[] pos = particles[p].getPosition().clone();
            double[] vel = particles[p].getVelocity().clone();

            double[] new_pos = new double[dim];
            double[] new_vel = new double[dim];

            double[] localBestPos = particles[p].getLocalBestPosition().clone();

            for (int d = 0; d < dim; d++) {

                //Update Velocity
                double r1 = Math.random();
                double r2 = Math.random();

                //System.out.println(r1 + " " + r2);

                new_vel[d] = (w * vel[d]) + ((c1 * r1) * (localBestPos[d] - pos[d])) + ((c2 * r2) * (globalBestPos[d] - pos[d]));

                //Update Position
                new_pos[d] = pos[d] + new_vel[d];
            }

            particles[p].setVelocity(new_vel);
            particles[p].setPosition(new_pos);

        }
    }

    public static void createSwarm(int dim, int lowerBound, int upperBound, int evalFunction) {
        // Init swarm particles
        for (int i = 0; i < PARTICLES_NR; i++) {
            particles[i] = new Particle(dim, lowerBound, upperBound, evalFunction);
        }
    }

    public static void fitnessEval(int evalFunction) {

            //Evaluate each particle
            evalMethod(evalFunction);

            //Find global best position
            globalBestFitness = particles[0].getLocalBestFitness();
            globalBestParticle = 0;
            globalBestPos = particles[0].getLocalBestPosition().clone();

            for (int i = 1; i < PARTICLES_NR; i++) {
                if (particles[i].getLocalBestFitness() < globalBestFitness) {

                    globalBestFitness = particles[i].getLocalBestFitness();
                    globalBestParticle = i;
                    globalBestPos = particles[i].getLocalBestPosition().clone();
                }
            }
    }

    public static void evalMethod(int evalFunction) {

        switch (evalFunction) {
            case 0:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.absoluteValue(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 1:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Ackley1(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
            default:
                break;
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

    public static void printParticleCoords(int itr) {

        for (int i = 0; i < PARTICLES_NR; i++) {
            System.out.println(itr + "," + i + particles[i].stringPositions());
        }
    }

    public static void printAvgFitness() {
        double sum = 0;
        for (int i = 0; i < PARTICLES_NR; i++) {
            sum = sum + particles[i].getFitness();
        }
        System.out.println(sum / PARTICLES_NR);
    }
}