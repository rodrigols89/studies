public class TestReference {

  public static void main(String[] args) {

    Account c1; // Reference variable.
    c1 = new Account(); // Instance Account Object.
    c1.deposit(100);

    // Passes the memory address saved in reference variable c1 to c2.
    Account c2 = c1;
    c2.deposit(200);

    System.out.println(c1.balance);
    System.out.println(c2.balance);
  }
}
