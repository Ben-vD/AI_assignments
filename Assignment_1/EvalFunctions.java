public class EvalFunctions {

    public static double absoluteValue(double[] x) {

        double sum = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + Math.abs(x[i]);
        }
        return sum;
    } 

}