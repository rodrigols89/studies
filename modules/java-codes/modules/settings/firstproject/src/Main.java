public class Main {
    public static void main(String[] args) {

        Calculator calculator = new Calculator();

        int sum_result = calculator.add(2, 3);
        System.out.println("Result: " + sum_result);

        int square_result = MathUtils.square(4);
        System.out.println("Square: " + square_result);
    }
}
