const loginForm = document.getElementById("formLogin");
const senhaLogin = document.getElementById("loginSenha");
const emailLogin = document.getElementById("loginEmail");

loginForm?.addEventListener("submit", async function (e) {
  e.preventDefault();

  const senhaLoingValue = senhaLogin.value;
  const emailLoingValue = emailLogin.value;

  const login = {
    email: emailLoingValue,
    senha: senhaLoingValue,
  };
  try {
    const resposta = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(login),
    });

    const dados = await resposta.json();

    if (resposta.ok) {
      console.log("login com sucesso", dados.mensagem);
      loginForm.reset();
    } else {
      console.log("Erro ao login", dados.error);
    }
  } catch (erro) {
    console.log("Falha na rede", erro);
  }
});
