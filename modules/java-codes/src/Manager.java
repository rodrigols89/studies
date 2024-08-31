public class Manager extends Employee {

    private int password;
    private int managedEmployees;

    public double getBonus() {
        return super.getBonus() + 1000;
    }
}
