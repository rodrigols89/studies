public abstract class Employee {

  // Attributes.
  protected String name;
  protected String socialSecurity;
  protected double salary;

  public abstract double getBonus();

  public String getName() {
    return this.name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public double getSalary() {
    return this.salary;
  }

  public void setSalary(double salary) {
    this.salary = salary;
  }
}
