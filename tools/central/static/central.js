// Central AMtech: saída ao vivo das execuções e confirmação antes de ações. Sem dependências.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("form[data-confirmar]").forEach((f) => {
    f.addEventListener("submit", (ev) => {
      const botao = ev.submitter;
      if (botao && botao.value === "recusar") return;
      if (!window.confirm(f.dataset.confirmar)) ev.preventDefault();
    });
  });
  const saida = document.getElementById("saida");
  if (!saida || saida.dataset.vivo !== "1") return;
  const estado = document.getElementById("estado");
  const fonte = new EventSource(`/execucao/${encodeURIComponent(saida.dataset.id)}/eventos`);
  fonte.onmessage = (ev) => {
    saida.append(JSON.parse(ev.data) + "\n");
    saida.scrollTop = saida.scrollHeight;
  };
  fonte.addEventListener("fim", (ev) => {
    estado.textContent = ev.data === "0" ? "terminou: ok" : `terminou com código ${ev.data}`;
    estado.className = ev.data === "0" ? "ok" : "erro";
    fonte.close();
  });
  fonte.onerror = () => { estado.textContent = "conexão perdida; recarregue a página"; fonte.close(); };
});
