# 📘 Painel SGP-PA PRF — Central de Gestão & Procedimentos Operacionais

> **Central de Gestão, Procedimentos Operacionais (POPs), Prazos e Processos SEI**  
> **Unidade**: Seção de Gestão de Pessoas (SGP) e Núcleo de Administração de Pessoal (NUAP) — PRF no Pará  
> **Acesso ao Portal**: [https://sgppaprocedimentos.com.br](https://sgppaprocedimentos.com.br/)

---

## 🚀 Funcionalidades Principais

* 📖 **Procedimentos Operacionais Padronizados (POPs)**: Manuais e tutoriais passo a passo com suporte a Markdown, tabelas, imagens e navegação por etapas.
* ⏳ **Gestão de Prazos Legais e Administrativos**: Acompanhamento de datas limites com cálculo automático de dias restantes, destaques visuais por criticidade e banner dinâmico.
* 📊 **Kanban de Processos SEI**: Quadro visual com colunas customizáveis para controle de tramitação de processos administrativos SEI.
* 📧 **Notificações Automáticas em 2º Plano (EmailJS)**: Envio automático de e-mails em segundo plano sem necessidade de cliente nativo instalado para toda a equipe PRF cadastrada (`ana.silva`, `gustavo.aquino`, `sgp.pa`, `nuap.pa`, `nathanael.lacerda`, `rafael.guimaraes`, `silvana.socorro`).
* 🤖 **Automação Diária 24/7 (GitHub Actions)**: Routine em Python rodando diariamente na nuvem para monitoramento de prazos críticos.
* 💻 **Biblioteca de Comandos Espanso (YAML)**: Coleção de atalhos e expansores de texto para produtividade administrativa.
* 🔗 **Central de Links Úteis**: Atalhos corporativos organizados no menu lateral de todas as páginas.
* 🧮 **Hub de Ferramentas Utilitárias**: Calculadoras de substituição de função, adicionais de periculosidade e contagem de dias úteis/corridos.

---

## 📖 Documentação Completa

Para ler a documentação técnica detalhada (arquitetura, APIs, credenciais, segurança e fluxos de dados), consulte o arquivo:
👉 **[DOCUMENTACAO.md](./DOCUMENTACAO.md)**

---

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML5, Vanilla JavaScript (ES6+), CSS3 (Modern Glassmorphism Design, Grid/Flexbox)
- **Email Service**: EmailJS Browser API (`@emailjs/browser`)
- **Persistence & Cloud Sync**: LocalStorage + GitHub Gists REST API (`5bd8f241cdc0e04c683bc580bd379c45`)
- **CI/CD & Automation**: GitHub Actions, Python 3
- **Hosting**: GitHub Pages com domínio customizado `sgppaprocedimentos.com.br`

---
*Desenvolvido para a Superintendência da Polícia Rodoviária Federal no Pará (SGP/NUAP-PA).*
