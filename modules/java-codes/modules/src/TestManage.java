public class TestManage {
  public static void main(String[] args) {

    Manage m = new Manage();

    m.setName("Rodrigo");
    m.setSalary(10000);

    System.out.println("Name: "+m.getName()+"\nSalary: "+m.getSalary());
    System.out.println("Salary Bonus: "+m.getBonus());
  }
}
