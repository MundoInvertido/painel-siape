import json
import urllib.request
import datetime
import os
import sys

# Garante codificação UTF-8 no stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

GIST_ID = "5bd8f241cdc0e04c683bc580bd379c45"
TOKEN = os.environ.get("GITHUB_TOKEN_GIST", "")

RECIPIENTS = [
    "ana.silva@prf.gov.br",
    "gustavo.aquino@prf.gov.br",
    "sgp.pa@prf.gov.br",
    "nuap.pa@prf.gov.br",
    "nathanael.lacerda@prf.gov.br",
    "rafael.guimaraes@prf.gov.br",
    "silvana.socorro@prf.gov.br"
]

def fetch_gist_data():
    url = f"https://api.github.com/gists/{GIST_ID}"
    req = urllib.request.Request(url)
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req) as response:
            gist_json = json.loads(response.read().decode('utf-8'))
            content_str = gist_json['files']['siape_unified_data.json']['content']
            return json.loads(content_str)
    except Exception as e:
        print(f"Erro ao carregar dados do Gist: {e}")
        return None

def main():
    data = fetch_gist_data()
    if not data:
        print("Nenhum dado retornado da nuvem.")
        return

    today = datetime.date.today()
    critical_items = []

    # 1. Checa Agendamentos (Prazos)
    agendamentos = data.get('agendamentos', [])
    for item in agendamentos:
        dt_str = item.get('data') or item.get('dataLimite') or item.get('prazo')
        if dt_str:
            try:
                target_date = datetime.datetime.strptime(dt_str[:10], "%Y-%m-%d").date()
                diff_days = (target_date - today).days
                if diff_days <= 3:
                    critical_items.append({
                        "type": "Prazo / Requerimento",
                        "title": item.get('numero') or item.get('titulo') or item.get('descricao') or 'Prazo SGP',
                        "desc": item.get('descricao') or item.get('obs') or '',
                        "date": dt_str[:10],
                        "days": diff_days,
                        "resp": item.get('responsavel') or item.get('servidor') or 'SGP/NUAP'
                    })
            except Exception:
                pass

    # 2. Checa Processos SEI (Kanban)
    kanban = data.get('kanban', {})
    cards = kanban.get('cards', []) if isinstance(kanban, dict) else []
    for card in cards:
        dt_str = card.get('deadline')
        if dt_str:
            try:
                target_date = datetime.datetime.strptime(dt_str[:10], "%Y-%m-%d").date()
                diff_days = (target_date - today).days
                if diff_days <= 3:
                    critical_items.append({
                        "type": "Processo SEI (Kanban)",
                        "title": f"SEI {card.get('sei', '')} - {card.get('title', '')}",
                        "desc": card.get('description') or '',
                        "date": dt_str[:10],
                        "days": diff_days,
                        "resp": card.get('assignee') or 'NUAP/SGP'
                    })
            except Exception:
                pass

    print(f"Relatório de Prazos SGP-PA - {today.strftime('%d/%m/%Y')}")
    print(f"Destinatários Oficiais: {', '.join(RECIPIENTS)}")
    print(f"Total de itens críticos/vencendo: {len(critical_items)}")

    if not critical_items:
        print("Nenhum prazo vencendo nos próximos 3 dias.")
        return

    print("\n--- ITENS PRÓXIMOS DO VENCIMENTO ---")
    for item in critical_items:
        status_text = "VENCIDO!" if item['days'] < 0 else ("HOJE!" if item['days'] == 0 else f"{item['days']} dia(s)")
        print(f"• [{item['type']}] {item['title']} - Vencimento: {item['date']} ({status_text}) - Resp: {item['resp']}")

    # Prepara resumo para saída no GitHub Step Summary
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(f"## Alerta de Prazos SGP-PA - {today.strftime('%d/%m/%Y')}\n\n")
            f.write(f"**Destinatários Notificados:** `{', '.join(RECIPIENTS)}`\n\n")
            f.write("| Tipo | Processo / Item | Vencimento | Status | Responsável |\n")
            f.write("| --- | --- | --- | --- | --- |\n")
            for item in critical_items:
                status_text = "🔴 VENCIDO" if item['days'] < 0 else ("🟠 HOJE" if item['days'] == 0 else f"🟡 em {item['days']} dia(s)")
                f.write(f"| {item['type']} | {item['title']} | {item['date']} | {status_text} | {item['resp']} |\n")

if __name__ == "__main__":
    main()
