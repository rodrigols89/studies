public class Manager extends Employee implements Authentic {

  private int password;
  private int managedEmployees;

  @Override
  public double getBonus() {
    return super.getBonus() + 1000;
  }

  public boolean Authenticates(int password) {
    if(this.password != password) {
        return false;
    }
    // pode fazer outras possíveis verificações, como saber se esse
    // departamento do Gerente tem acesso ao Sistema
    return true;
  }
}
