const lista1 = document.getElementById("listaUsuarios");
const button = document.getElementById("btnListar");
const formCriar = document.getElementById("formCriar");
const nome = document.getElementById("nome");
const email = document.getElementById("email");
const senha = document.getElementById("senha");

button?.addEventListener("click", function () {
  fetch("http://127.0.0.1:5000/listar/usuarios")
    .then((resposta) => resposta.json())
    .then((dados) => {
      lista1.innerHTML = "";
      for (const i of dados.usuarios) {
        const li = document.createElement("li");
        const remover = document.createElement("button");
        remover.innerText = "remover";
        li.innerText = `nome:${i.nome}`;
        lista1.appendChild(li);
        lista1.appendChild(remover);
        remover.addEventListener("click", function () {
          li.remove();
          remover.remove();
        });
      }
    });
});

formCriar.addEventListener("submit", function (e) {
  e.preventDefault();
  const senhaValue = senha.value;
  const nomeValue = nome.value;
  const emailValue = email.value;

  const novoUser = {
    nome: nomeValue,
    senha: senhaValue,
    email: emailValue,
  };
  fetch("http://127.0.0.1:5000/usuarios", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(novoUser),
  }).then((resposta) =>
    resposta.json().then((dados) => {
      console.log("Usuario Criado", dados);
      formCriar.reset();
    }),
  );
});
