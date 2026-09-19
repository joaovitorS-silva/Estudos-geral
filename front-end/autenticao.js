async function fetchAutenticacao(rota) {
  const access_token = localStorage.getItem("access_token");

  const resposta = await fetch(rota, {
    headers: {
      Authorization: `bearer ${access_token}`,
    },
  });

  if (resposta.status === 401) {
    const refresh_token = localStorage.getItem("refresh_token");

    const resposta_refresh = await fetch("http://127.0.0.1:5000/refresh", {
      headers: {
        Authorization: `bearer ${refresh_token}`,
      },
    });
    const dados = await resposta_refresh.json();

    if (resposta_refresh.ok) {
      const novo_access_token = dados.access_token;

      localStorage.setItem("access_token", novo_access_token);

      const NovaResposta = await fetch(rota, {
        headers: {
          Authorization: `bearer ${novo_access_token}`,
        },
      });

      return NovaResposta;
    } else {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");

      window.location.href = "login.html";
    }
  } else {
    return resposta;
  }
}
