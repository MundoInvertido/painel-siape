# deploy.ps1
# Script para subir o painel automaticamente para o GitHub

# 1. Verificar se o Git está instalado no PATH
$gitCmd = Get-Command git.exe -ErrorAction SilentlyContinue
if (!$gitCmd) {
    $userGit = "$env:USERPROFILE\AppData\Local\Programs\Git\cmd\git.exe"
    if (Test-Path $userGit) {
        $gitPath = $userGit
    } else {
        Write-Host "[ERRO] Git não encontrado. Por favor, certifique-se de que a instalação do Git foi concluída e aprovada na tela." -ForegroundColor Red
        Exit
    }
} else {
    $gitPath = "git"
}

# 2. Inicializar repositório Git se necessário
if (!(Test-Path .git)) {
    Write-Host "[INFO] Inicializando repositório Git local..." -ForegroundColor Cyan
    & $gitPath init
    & $gitPath branch -M main
}

# 3. Configurar remote origin
$remote = & $gitPath remote get-url origin 2>$null
if (!$remote) {
    Write-Host "--------------------------------------------------------"
    Write-Host "Configuração do Repositório GitHub" -ForegroundColor Green
    Write-Host "Por favor, crie um repositório vazio no GitHub e cole a URL abaixo."
    Write-Host "Exemplo: https://github.com/usuario/repositorio.git"
    Write-Host "--------------------------------------------------------"
    $repoUrl = Read-Host "URL do Repositório GitHub"
    if ($repoUrl) {
        & $gitPath remote add origin $repoUrl
        Write-Host "[INFO] Remote 'origin' adicionado com sucesso." -ForegroundColor Green
    } else {
        Write-Host "[ERRO] URL não informada. Abortando deploy." -ForegroundColor Red
        Exit
    }
}

# 4. Adicionar arquivos e fazer commit
Write-Host "[INFO] Adicionando arquivos..." -ForegroundColor Cyan
& $gitPath add index.html procedimentos.html base.yml "painel_espanso_siape corrigido.html" "painel_procedimentos_sgp_nuap.html" .gitignore deploy.ps1 *.md *.txt

# Verificar status
$status = & $gitPath status --porcelain
if (!$status) {
    Write-Host "[INFO] Nenhuma alteração pendente para commitar." -ForegroundColor Green
} else {
    Write-Host "[INFO] Fazendo commit das alterações..." -ForegroundColor Cyan
    # Configurar identidade local se estiver vazio
    $hasEmail = & $gitPath config user.email
    if (!$hasEmail) {
        & $gitPath config user.email "nathanaeladmin@gmail.com"
        & $gitPath config user.name "Nathanael Lacerda"
    }
    & $gitPath commit -m "Auto-deploy: atualização do painel, manuais e atalhos"
}

# 5. Push para o GitHub
Write-Host "[INFO] Enviando arquivos para o GitHub (main)..." -ForegroundColor Cyan
& $gitPath push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "[SUCESSO] Arquivos enviados com sucesso para o GitHub!" -ForegroundColor Green
} else {
    Write-Host "[ERRO] Falha ao enviar para o GitHub. Verifique suas credenciais de acesso." -ForegroundColor Red
}
