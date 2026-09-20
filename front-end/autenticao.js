async function fetchAutenticacao(rota) {
  const resposta = await fetch(rota, {
    credentials: "include",
  });

  if (resposta.status === 401) {
    const resposta_refresh = await fetch("http://127.0.0.1:5000/refresh", {
      method: "POST",
      credentials: "include",
    });

    if (resposta_refresh.ok) {
      const NovaResposta = await fetch(rota, {
        credentials: "include",
      });

      return NovaResposta;
    } else {
      

      window.location.href = "login.html";
    }
  } else {
    return resposta;
  }
}
