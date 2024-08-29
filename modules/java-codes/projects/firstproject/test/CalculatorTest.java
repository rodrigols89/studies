public class CalculatorTest {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        assert calculator.add(2, 3) == 5 : "Addition test failed";
        assert calculator.subtract(5, 3) == 2 : "Subtraction test failed";

        System.out.println("All Calculator tests passed.");
    }
}
