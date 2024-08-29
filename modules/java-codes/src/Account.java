class Account {

    // Class Attributes.
    private static int totalAccounts;

    // Instance Attributes.
    private int number;
    private String holder;
    private double balance;
    private double limit;

    // construtors.
    Account(String holder) {
        this.holder = holder;
    }

    Account() {
        Account.totalAccounts = Account.totalAccounts + 1;
    }

    // Methods.
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public String getHolder() {
        return holder;
    }

    public void setHolder(String holder) {
        this.holder = holder;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public double getLimit() {
        return limit;
    }

    public void setLimit(double limit) {
        this.limit = limit;
    }

    public static int getTotalAccounts() {
        return Account.totalAccounts;
    }
}
