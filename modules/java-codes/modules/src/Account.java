class Account {

  // Class Attributes.
  private static int totalAccounts;

  // Attributes.
  private int number;
  private String holder;
  private double balance;
  private double limit;

  Account() {
    Account.totalAccounts = Account.totalAccounts + 1;
  }

  public static int getTotalAccounts() {
    return Account.totalAccounts;
  }

  // Constructor.
  Account (String holder) {
    this.holder = holder;
  }

  Account (int number, String holder) {
    this(holder); // Call the above constructor.
    this.number = number;
  }

  // Getters and Setters

  public int getNumber(){
    return this.number;
  }

  public void setNumber(int number){
    this.number = number;
  }

  public String getHolder(){
    return this.holder;
  }

  public void setHolder(String holder){
    this.holder = holder;
  }

  public double getBalance(){
    return this.balance + this.limit;
  }

  // Others Methods.

  void withdraw(double quantity){
    double newBalance = this.balance - quantity;
    this.balance = newBalance;
  }

  void deposit(double quantity){
    this.balance += quantity;
  }
}
