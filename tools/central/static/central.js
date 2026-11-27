// Central AMtech: saída ao vivo das execuções, confirmação antes de ações e aviso de "pensando". Sem dependências.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("form[data-confirmar]").forEach((f) => {
    f.addEventListener("submit", (ev) => {
      const botao = ev.submitter;
      if (botao && botao.value === "recusar") return;
      if (!window.confirm(f.dataset.confirmar)) ev.preventDefault();
    });
  });
  document.querySelectorAll("form[data-pensando]").forEach((f) => {
    f.addEventListener("submit", () => {
      const b = f.querySelector("button");
      if (b) { b.disabled = true; b.textContent = f.dataset.pensando; }
    });
  });
  document.querySelectorAll("pre.saida[data-vivo='1']").forEach((saida) => {
    const id = saida.dataset.id;
    const estado = document.querySelector(`[data-estado-de="${CSS.escape(id)}"]`);
    const fonte = new EventSource(`/execucao/${encodeURIComponent(id)}/eventos`);
    fonte.onmessage = (ev) => {
      saida.append(JSON.parse(ev.data) + "\n");
      saida.scrollTop = saida.scrollHeight;
    };
    fonte.addEventListener("fim", (ev) => {
      if (estado) {
        estado.textContent = ev.data === "0" ? "terminou: ok" : `terminou com código ${ev.data}`;
        estado.className = ev.data === "0" ? "ok" : "erro";
      }
      fonte.close();
    });
    fonte.onerror = () => { if (estado) estado.textContent = "conexão perdida; recarregue a página"; fonte.close(); };
  });
});
