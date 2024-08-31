public class Employee {

    // Attributes.
    protected String name;
    protected String socialSecurity;
    protected double salary;

    public double getBonus() {
        return this.salary * 0.10;
    }
}
