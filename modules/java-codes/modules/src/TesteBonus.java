public class TesteBonus {

  public static void main(String[] args) {
    
    BonusControl control = new BonusControl();

    Manager employee1 = new Manager();
    employee1.setSalary(5000.0);
    control.registry(employee1);
    System.out.println("Total Bonus: "+control.getTotalBonus());

    Employee employee2 = new Employee();
    employee2.setSalary(1000.0);
    control.registry(employee2);
    System.out.println("Total Bonus: "+control.getTotalBonus());
  }
}
