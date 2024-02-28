public class EvalFunctions {

    public static double absoluteValue(double[] x) {

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

        sum_e1 = -0.2 * Math.sqrt((1/d) * sum_e1);
        sum_e2 = (1/d) * sum_e2;

        return (-20 * Math.exp(sum_e1) - Math.exp(sum_e2) + 20 + Math.E);
    }

}