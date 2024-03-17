public class EvalFunctions {

    public static double AbsoluteValue(double[] x) {

        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + Math.abs(x[i]);
        }
        return sum;
    } 

    public static double Ackley1(double[] x) {

        double sum_e1 = 0;
        double sum_e2 = 0;
        int d = x.length;

        for (int i = 0; i < d; i++) {
            sum_e1 = sum_e1 + (x[i] * x[i]);
            sum_e2 = sum_e2 + Math.cos(2 * Math.PI * x[i]);
        }

        sum_e1 = -0.2 * Math.sqrt(sum_e1 / (double) d);
        sum_e2 = sum_e2 / (double) d;

        return (-20.0 * Math.exp(sum_e1) - Math.exp(sum_e2) + 20.0 + Math.E);
    }

    public static double Alpine1(double[] x) {
        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + Math.abs((x[i] * Math.sin(x[i])) + (0.1 * x[i]));
        }
        return sum;
    }

    public static double Alpine2 (double[] x) {
        double product = 1;
        for (int i = 0; i < x.length; i++) {
            product = product * Math.sqrt(x[i]) * Math.sin(x[i]);
        }
        return product;
    }

    public static double Step2(double[] x) {
        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + Math.pow(Math.floor(x[i] + 0.5), 2);
        }
        return sum;
    }

    public static double Schwefel2_23(double[] x) {

        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + Math.pow(x[i], 10);
        }
        return sum;
    }

    public static double Step3(double[] x) {
        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + Math.floor(Math.pow(x[i], 2));
        }
        return sum;
    }

    public static double Shubert4(double[] x) {//Not report on
        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            for (int j = 1; j < 6; j++) {
                sum = sum + (j * Math.cos((j + 1) * x[i] + j));
            }
        }
        return sum;
    }

    public static double Discus(double[] x) {

        double sum = Math.pow(10, 6) * Math.pow(x[0], 2);
        for (int i = 1; i < x.length; i++) {
            sum = sum + Math.pow(x[i], 2);
        }
        return sum;
    }

    public static double EggCrate(double[] x) {
        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + Math.pow(x[i], 2) + 24 * Math.pow(Math.sin(x[i]), 2);
        }
        return sum;
    }    

    public static double Deb1(double[] x) {
        int n = x.length;
        double sum = 0;
        for (int i = 0; i < x.length; i++) {

            sum = sum + Math.pow(Math.sin(5 * Math.PI * x[i]), 6);

        }
        return (-1/(double) n) * sum;
    }  

}