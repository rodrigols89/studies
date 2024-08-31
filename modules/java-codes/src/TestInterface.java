public class TestInterface {
    public static void main(String[] args) {

        PaymentMethod paymentMethod;

        paymentMethod = new CreditCardPayment();
        processPayment(paymentMethod, 150.0);

        paymentMethod = new PayPalPayment();
        processPayment(paymentMethod, 250.0);
    }

    public static void processPayment(PaymentMethod method, double amount) {
        method.pay(amount);
    }
}
