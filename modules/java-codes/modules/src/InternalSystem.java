public class InternalSystem {

  public void login(Authentic employee) {

    int password = //pega senha de um lugar, ou de um scanner de polegar

    // Aqui eu posso chamar o autentica!
    // Pois todo FuncionarioAutenticavel tem
    boolean ok = employee.Authenticates(password);

  }
}
