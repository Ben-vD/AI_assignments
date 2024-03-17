import java.io.FileWriter;
import java.io.IOException;

public class Main {

    static final int PARTICLES_NR = 30;
    static Particle[] particles =  new Particle[PARTICLES_NR];

    static double[] globalBestPos;
    static double globalBestFitness;
    static int globalBestParticle;

    static double[] itrBestPos;
    static double itrBestFitness;
    static int itrBestParticle;

    static double c1;
    static double c2;
    static double w;
    static double lamda;
    static double[] lamdaArray;

    public static void main(String[] args) throws IOException {
    
        int approach = Integer.parseInt(args[0]);
        int dim = Integer.parseInt(args[1]);
        int iterations = Integer.parseInt(args[2]);
        double lowerBound = Double.parseDouble(args[3]);
        double upperBound = Double.parseDouble(args[4]);
        c1 = Double.parseDouble(args[5]);
        c2 = Double.parseDouble(args[6]);
        w = Double.parseDouble(args[7]);
        int evalFunction = Integer.parseInt(args[8]);
        lamda = Double.parseDouble(args[9]);
        int experiments = Integer.parseInt(args[10]);
        lamdaArray = new double[dim];

        System.out.println("Lamda: " + lamda);
        System.out.println("Eval: " + evalFunction);
        System.out.println("Appr" + approach);
        System.out.println("c1: " + c1);
        System.out.println("c2: " + c2);
        System.out.println("w: " + w);

        int runs = approach + 1;
        if (approach == 5) {
            runs = 5;
            approach = 0;
        }

        for (int a = approach; a < runs; a++) {

            if (a == 0) {
                lamda = 0;
            } else if (a == 2) {
                lamda = Math.random();
            } else if (a == 3) {
                lamda = 1;
            } else if (a == 4) {
                intitLamdaArray(dim);
            }
    
            //FileWriter coordWriter = new FileWriter("./Data/particleCoordsData" + a + "_" + evalFunction + ".txt");
            FileWriter diversityWriter = new FileWriter("./Data/diversityData" + a + "_" + evalFunction + ".txt");
            FileWriter fitnessWriter = new FileWriter("./Data/fitnessData" + a + "_" + evalFunction + ".txt");
    
            for (int exp = 0; exp < experiments; exp++) {
                //For linear decrease reset lamda each experiment
                if (a == 3) {
                    lamda = 1;
                }
                createSwarm(dim, lowerBound, upperBound, evalFunction);
                for (int itr = 0; itr < iterations; itr++) {
    
                    fitnessEval(evalFunction);
    
                    //printParticles();

                    //coordWriter.write(printParticleCoords(itr));
                    diversityWriter.write(Diversity(dim));
                    fitnessWriter.write(printAvgFitness());

                    updateVelAndPos(dim, a, iterations);
                }
    
            }
            //coordWriter.close();
            diversityWriter.close();
            fitnessWriter.close();
        }
    }

    public static void intitLamdaArray(int dim) {
        for (int i = 0; i < dim; i++) {
            lamdaArray[i] = Math.random();
        }
    }

    public static void updateVelAndPos(int dim, int approach, int iterations) {
       
        if (approach == 1 || approach == 2 || approach == 4) {
            findCurrentBestPos();
        } else if (approach == 3) {
            findCurrentBestPos();
            lamda = lamda - (1 / (double) iterations);
        }

        findCurrentBestPos();

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
                if (approach != 4) {
                    new_vel[d] = (w * vel[d]) + ((c1 * r1) * (localBestPos[d] - pos[d])) + ((c2 * r2) * ((1 - lamda) * (globalBestPos[d] - pos[d]) + (lamda) * (itrBestPos[d] - pos[d])));
                } else {
                    new_vel[d] = (w * vel[d]) + ((c1 * r1) * (localBestPos[d] - pos[d])) + ((c2 * r2) * ((1 - lamdaArray[d]) * (globalBestPos[d] - pos[d]) + (lamdaArray[d]) * (itrBestPos[d] - pos[d])));
                }
                //Update Position
                new_pos[d] = pos[d] + new_vel[d];
            }

            particles[p].setVelocity(new_vel);
            particles[p].setPosition(new_pos);

        }
    }

    public static void findCurrentBestPos(){
        double tempCurrentBest = Double.POSITIVE_INFINITY;
        for (int i = 0; i < PARTICLES_NR; i++) {
            if (particles[i].getFitness() < tempCurrentBest && particles[i].getFeasiblePos()) {
                tempCurrentBest = particles[i].getFitness();

                itrBestFitness = particles[i].getFitness();
                itrBestPos = particles[i].getPosition().clone();
                itrBestParticle = i;
            }
        }
    }

    public static void createSwarm(int dim, double lowerBound, double upperBound, int evalFunction) {
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
            findCurrentBestPos();
    }

    public static void evalMethod(int evalFunction) {

        switch (evalFunction) {
            case 0:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.AbsoluteValue(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 1:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Ackley1(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 2:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Alpine1(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 3:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Alpine2(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 4:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Step2(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 5:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Schwefel2_23(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 6:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Step3(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 7:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Shubert4(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 8:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Discus(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 9:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.EggCrate(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            case 10:
            for (int i = 0; i < PARTICLES_NR; i++) {
                double new_fitness = EvalFunctions.Deb1(particles[i].getPosition());
                particles[i].setFitness(new_fitness);
            }
                break;
            default:
                break;
        }

    }

    public static String Diversity(int dim) {

        // Calculate mean vector (mean positions per dimention)
        double[] meanPos = new double[dim];
        for (int d = 0; d < dim; d++) {
            double sum = 0;
            for (int p = 0; p < PARTICLES_NR; p++) {
                sum = sum + particles[p].getPosition()[d];
            }
            meanPos[d] = sum / PARTICLES_NR;
        }

        double diversity = 0; 
        for (int p = 0; p < PARTICLES_NR; p++) {
            double var = 0;
            for (int d = 0; d < dim; d++) {

                var = var + Math.pow(particles[p].getPosition()[d] - meanPos[d], 2);

            }
            diversity = diversity + Math.sqrt(var);
        }

        diversity = (1 / (double) PARTICLES_NR) * diversity;
        //System.out.println(diversity);
        return (diversity + "\n");
    }

    public static void printParticles() {

        String globalBestPosStr = "";
        String itrBestPosStr = "";
        for (int i = 0; i < globalBestPos.length; i++) {
            globalBestPosStr = globalBestPosStr + globalBestPos[i] + " ";
            itrBestPosStr = itrBestPosStr + itrBestPos[i] + " ";
        }

        System.out.println("Current best:\tParticle: " + itrBestParticle + "; Pos: (" + itrBestPosStr + "); Fitness: " + itrBestFitness + "\n");        

        System.out.println("Global best:\tParticle: " + globalBestParticle + "; Pos: (" + globalBestPosStr + "); Fitness: " + globalBestFitness + "\n");
        for (int i = 0; i < PARTICLES_NR; i++) {
            System.out.println("\u001B[31mParticle " + i + "\u001B[0m\n" + particles[i].toString() + "\n");
        }
        System.out.println("---------------------------------------");
    }

    public static String printParticleCoords(int itr) {

        String str = "";
        for (int i = 0; i < PARTICLES_NR; i++) {
            //System.out.println(itr + "," + i + particles[i].stringPositions());
            str = str + (itr + "," + i + particles[i].stringPositions()) + "\n";
        }
        return str;
    }

    public static String printAvgFitness() {
        double sum = 0;
        for (int i = 0; i < PARTICLES_NR; i++) {
            sum = sum + particles[i].getFitness();
        }
        return (sum / PARTICLES_NR) + "\n";
    }

    public static void printArr(double[] arr) {

        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + ", ");
        }
        System.out.println();
    }

}
