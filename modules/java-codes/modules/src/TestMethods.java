public class TestMethods {
  public static void main(String[] args) {

    Account myAccount; // Reference variable.
    myAccount = new Account(); // Instance Account Object.

    myAccount.holder = "Rodrigo";
    myAccount.balance = 1000.0;

    myAccount.withdraw(500);
    myAccount.deposit(1000);
    System.out.println(myAccount.balance);
  }
}
