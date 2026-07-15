# BIZUÁRIO DE CADASTRO

Este Bizuário é a coletânea de diversos bizuários encaminhados por colegas de várias regionais acrescido das informações da Divisão de Cadastro. É um documento aberto e deverá ser atualizado para ajudar os novos colegas e manter a memória da área. Caso alguma contradição seja encontrada, destaque o texto, coloque um comentário e informe a Divisão de Cadastro.

O objetivo é manter uma fonte de informação prática para orientar procedimentos e facilitar o desenvolvimento do trabalho de todos.

Como o índice ainda não está totalmente organizado, **utilize a busca por palavras chave (Ctrl+F)**.

# Sistemas da PRF

A função de chefia é lançada no SIAPE (titular) e na planilha (da CPAP), os substitutos.

Os sistemas internos (PDI, Frequência, Athena, Chronos) consomem dessas fontes.

As unidades de lotação criadas desde 2019 em diante não existem no SRH, o servidor tem de ser alocado na unidade superior que existir, na árvore.

## Frequência 

Novos códigos trazidos pelo comunica 565974 e atualizados pelo 566038\.

Quais os códigos vigentes agora? 

1001 \- TLTBINTEGRAL \- Teletrabalho Integral \- PGD \- Teletrabalho em Integral em PGD remoto, sem comparecimento a sede conforme Art. 8º, III, da IN SRT/MGI nº 712025;  
1002 \- TLTBPARCIAL \- Teletrabalho Parcial \- PGD \- Teletrabalho Parcial em PGD conforme Art. 8º, III, da IN SRT/MGI nº 712025\. Somente nos dias que não comparecer ao orgão;  
1003 \- TLTBEXTERIOR \- Teletrabalho Exterior \- PGD \- Art. 8º, III, da IN SRT/MGI nº 712025 \- Quando autorizado, se refere ao teletrabalho realizado no exterior;  
1005 \- DESLOCAMENTO \- Efetivo deslocamento \- PGD \- Efetivo deslocamento de servidor em PGD, quando presencial independente da modalidade (integral ou parcial) \- Art. 8º, III, da IN SRT/MGI nº 712025\.

Servidor em PGD registra frequência?  
O servidor que trabalha em regime de PGD não registra frequência em nenhum dia, mesmo nos dias que comparecer presencialmente, salvo a pedido do chefe imediato para controle próprio ou para fins de recebimento de IDFRON. Nestes casos o registro no frequência é do tipo PGD, e esse registro não entra no cômputo das horas do dia, valendo o abono de 8 horas por dia útil.

Como fica a situação do servidor que trabalha em PGD e quer usufruir do recesso?  
Como o servidor em PGD não registra frequência, não existe a possibilidade de compensar ou direcionar as horas. Para estes casos o MGI criou o código de afastamento de recesso \- 0449 \- AURECESPGD \- Recesso em PGD (Exclusivo). Os servidores em PGD devem realizar as entregas normalmente fora dos dias de recesso, para ter direito ao usufruto do recesso, está (a conclusão das entregas) é a única forma de compensação de recesso dos servidores em PGD .

Todas as informações constam do campo de observações dos códigos, no sistema Frequência.

# ASSINATURA DIGITAL (GOV.BR) \- *necessário ter app Gov.br instalado em seu smartphone*.

1. Acessar a url: assinador.iti.br e fazer o login com sua conta gov.br;  
2. Clicar em "Escolher arquivo" e selecione o documento que receberá a assinatura ou localize o documento em seu computador e o arraste para o local indicado;  
3. O site vai carregar e exibir o documento. Clique no botão "Avançar" para continuar;  
4. Posicione a “área de assinatura” no local desejado;  
5. Clique em Assinar e escolha o provedor de assinatura disponível (gov.br);  
6. O portal enviará um código para o número de celular informado na conta Gov.br. O usuário deverá informar no espaço indicado o código enviado pelo Portal através de SMS para o seu celular. Após, clicar em “Autorizar”;  
7. Por fim, deve-se clicar em “Baixar arquivo assinado”. 

# 

# EXERCÍCIOS ANTERIORES

1. Cadastre a função **\>GRIAPROADM** . Essa função inclui o processo e gera dois novos número finais identificadores do processo. Muito importante : anote esse dos novos dígitos na capa do processo ao final de numeração normal, porque você precisará deles para consultas posteriores.

2. Cadastre a função **\>GRINBENEF** . Essa função inclui o servidor beneficiado e os valores. Se for preciso essa função também corrige o valor.

IMPORTANTE: Para cadastrar valores de per capita- ressarcimento de plano de saúde usar o objeto 242

\>TBCOOBJPAG – mostra objeto para pagamento de exercícios anteriores.

# Emissão de GRU

Para emissão de GRU pelo novo portal do PagTesouro, agora existem dois caminhos: 

Independentemente da forma escolhida, a UG Arrecadadora será sempre a 200230\.

1 \- Emissão pelo método antigo.   
Link: https://pagtesouro.tesouro.gov.br/portal-gru/\#/emissao-gru  
Códigos: 18806-9 – Devolução de exercício anterior.   
                    68801-0 – Devolução de créditos da folha – no exercício  
                    68817-7 – Ressarcimento de pessoal cedido  
                   68888-6 – Anulação de despesa no exercício – ajuda de custo 

2 \- Emissão pelo portal de pagamento, que possibilita o pagamento via pix e cartão de crédito.   
Link: 0

Códigos: 017437 – Devolução de exercício anterior.   
                    016430 – Devolução de créditos da folha – no exercício  
                    016431 – Ressarcimento de pessoal cedido

Após o pagamento da GRU e a confirmação do pagamento junto a SOFIP, é necessário fazer o lançamento em folha suplementar. 

\>FPMOVSUPLIN – Folha suplementar, servidor com ocorrência de exclusão – fazer lançamentos igual ao fpatmovfin// servidor excluído

\>FPCLSUPLIN \- cálculo de pagamento de folha suplementar, servidor excluído.

# Transações Siape

[Siape Comandos](https://drive.google.com/open?id=1cHN2_kEHpyhOQDQTay3nGDzEQYMt8xwc) \- Link para o arquivo com todos os comandos listados.

**\>ADMINIST**

1-\>**ADCOLOG \-** verificar, através de consultas, todas as atualizações (inclusões, alterações e exclusões). Verificar lançamentos que um servidor do RH fez, caso haja erro.

\>ADCONVEHAB – consulta habilitação no siape para determinado servidor. Você abre a função e vê qual habilitação você precisa ter para acessá-la.

2- \> ADCOTRANS – mostra em que nível de acesso ao sistema você tem. Às vezes você tenta entrar em uma função no siape e aparece “acesso a função não disponível'.. aí você entra na adcotrans e mostra como você precisa estar habilitado para acessar.

Ex: fpatmovfin – você vê quem pode acessar essa função, em que nível deve estar cadastrado.

3- \>MUDAPAH \- o cadastrador altera os perfis dos usuários no siape (Hirôo)

**\>CAAPSERVID. LANÇAR A [APOSENTADORIA](#aposentadoria), (LANÇAMENTO DE APOSENTADORIA):**

**ALERTA: Nunca lance a aposentadoria na mesma folha de publicação. Salvo se os efeitos forem a partir do dia 1º do mês.**

*O recadastramento do **aposentado** é feito pelo planejamento. Sempre ver se o aposentado fez o recadastramento, se não fez, antes de suspender o pagamento é preciso fazer a publicação em edital.*

**\>TBSIAPE** (apertar F8 na tela principal para chegar nesta função)

\>tbcoorgao \- Consulta tabela de código de órgão.

\>tbfunciona (tabelas funcionais)

\--- a tabela mais importante é a tabela de rubricas, e suas incidências

\>TBCOBENEF – consulta a tabela de benefícios do dependente

\>benefdepen – tabela de cadastro de condição de dependente – condição/benefício

\>CARGEMP – consulta CBO, grupo/cargo, jornada de trabalho, escolaridade do cargo. Por escolaridade você acha o cbo. É bom ver a área de atuação – T/M/P/S – técnico, médico, professor e saúde, para ver se pode acumular cargo – acumulação de cargo. Consulta pelo **grupo de cargo** ou **escolaridade**.

\>TBCONIVCEM – consulte a tabela de salário, importante para fazer pagamento de exercícios anteriores. Nível salarial.

– VOCÊ PODE ACESSAR A CONSULTA DE TABELAS PELO \>CONSULTAS – ex: \>COTBRUBRI

**COMANDOS BÁSICOS** 

\>CDCOINDFUN – Dados individuais FUNCIONAIS;

\>CDCOINDPES –  Dados individuais PESSOAIS;

\>CACODADORH – Consultar Dados Pessoais do RH.

\>FPCLPAGTO – Cálculo do pagamento do mês do servidor \- FOLHA ABERTA

\>FPCOFICHAF – Consulte FICHAS ANTERIORES \- INDIVIDUALMENTE

\>FPEMFICHAF– Emite fichas financeiras de vários meses juntos.

**\>CONLEG – constantes legais**

Tabela de imposto de renda, seguridade social.

\>tbcoclegdv – consulta valor do salário mínimo, teto salarial.

\>tbconsfunc – você consulta o valor do **DAS** para instrução de processo e etc. Bom para pagar **substituto**. Substituição – sistemática C

\>tbconinfun – consulta quintos administrativos feitos via cadastro

TABELAS FUNCIONAIS SIAPE

\>TBCOOCORRE – Consulta ocorrências

\>TBCORUBRIC – lista de rubricas para pagamento

\>TBINCORUBR \- ex situação de determinação judicial para excluir rubrica de consignação em folha, coloca a matrícula do servidor ou pensionista. A margem não abre pro servidor só quando a consignatária libera. Incompatibiliza uma rubrica de um servidor.

\>TBCORUBRIC – consulta rubrica (código: 00001\)

RENDIMENTO TRIBUTÁVEL NÃO SIGNIFICA QUE DESCONTA TODOS OS TRIBUTOS. Nessa função também consulta o valor máximo lançado em cada rubrica, o limite máximo. Quando o valor do lançamento excede o valor da rubrica, você faz autorização especial – adautoriza

também mostra os assuntos de incidência de rubricas (o que incide sobre a rubrica- imposto, pss...)

\>COTBRUBRI – CONSULTA INCIDÊNCIAS DE PSS, IMPOSTO DE RENDA, POR RUBRICA, SEQUÊNCIA COMPATÍVEL

\*\*\* Obs.: rubricas de 1 a 5 é para pagamento de mês atual. Já as rubricas de 6 a 9, são para pagamento de anteriores dentro do mês.

\*\*\* para auxílio-natalidade, a base é o menor vencimento; já para cargo de curso e concurso, a base é o maior vencimento.

**\-** Se você for cadastrar os dados bancários de um servidor e o banco não estiver cadastrado, você pede para o Alô SEGEPE cadastrar. Você pode consultar o banco nas tabelas gerais no siape.

**\>TBCOUF** – consulta valores de auxílio alimentação, pré-escolar

\>TBCOORGAO \- tem o contato, CNPJ de outros órgãos. Não precisa entrar no sipec para consultar.

\>TBCOUORG \-\> CONSULTA UNIDADE ORGANIZACIONAL por código

\>TBCOAUXTRAN \- tabela consulta auxílio-transporte.

# Transações SIAPECAD

\>TBCOASSPAR – consulta assuntos de cálculo

\>FPATPARAM – parâmetros de cálculos automáticos. Cálculos automáticos para cada servidor, às vezes está desabilitado, aí você habilita.

Para descobrir a UPAG do servidor, vai no CDCOUPGSER

Alteração de dados específicos do servidor.  
\>CAALPESERR \- Altera dados pessoais por erro. 

\>CAALENDRH \- Altera endereço de servidor.

# MANUAL DE PROCEDIMENTO NO SIAPE

Encontre os manuais de procedimentos acessando o Sigepe.

\>FPATRENDEX – atualiza rendimentos extra siape. Limita um teto remuneratório para o servidor cedido ou requisitado. Quando a PRF cede algum servidor

# MACRO

PARA LANÇAR O MESMO VALOR PARA VÁRIAS MATRÍCULAS

\> fpatmovfin, coloque a matrícula+enter \- você vai em ações/gravar macro – colocar nome da macro+ok/ ou seja, a partir desse momento você vai gravar a macro e repetir depois, em outros lançamentos /// SE A MACRO NÃO ABRIR, VC VAI EM ''AÇÕES/ EXIBIR MACRO''

DELETAR A LINHA DE VALOR E COLOCAR O CURSOR EM CIMA – COLOCAR NO ÍCONE DO PROMPT (AO LADO DO RELÓGIO), DIGITAR O VALOR NO NOME DO PROMPT. VC PODE COLOCAR PROMPT ONDE AS COISAS SÃO **DIFERENTES**. TIPO VALOR, JUSTIFICATIVA E DOC LEGAL.

PARA ACABAR COM A MACRO, VC VAI EM ''AÇÕES, PARAR MACRO''.

DEPOIS'' VC COLOCA A MATRÍCULA DE OUTRO SERVIDOR, ENTER, ''REPRODUZ A MACRO NO CAMPO ESPECÍFICO (NO ÍCONE REPRODUZIR MACRO)

\>FPATMOVFIN

1 \- colocar a matrícula do servidor \+ enter

2 \- na barra de tarefas, clicar em 'exibir / gerenciador de macro'

3 \- 'ações / gravar macro' \- colocar o nome da macro \+ enter

4 \- preencher os campos do \>fpatmovfin – rubrica, sequuencia e inclusao \+ ok

5 \- apagar toda a linha do valor e deixar o cursor em cima do mesmo campo

6 \- clicar no ícone do PROMPT (ao lado do relógio) – você clica no prompt toda vez que o campo não pode ter as mesmas informações, tipo valor, doc legal... (Ex: nome do prompt \= valor // enter // colocar o valor)

7- clicar em F12 // agora você deve terminar a macro e parar de gravar as informações, logo clicar em ' ações / parar macro' /

8 \- nesse momento você vai lançar as informações de outro servidor, coloque a matrícula \+enter

9 – clicar em ''reproduzir macro'' / digitar as informações diferentes (valor, doc legal) \+ enter

Você pode salvar a macro na pasta pessoal de macros e depois é só executá-las.

\>CAATCONPSS – permite atualizar a base de contribuição do servidor. EX: O servidor está de licença sem remuneração e contribui no pss por 2 meses. Ele leva o comprovante e você lança no siape para atualização. É bom pois contará para a aposentadoria. Faz atualização desde a vida funcional do servidor no órgão.endereço

# 

# AUXÍLIO TRANSPORTE

**(COMO LANÇAR O DESCONTO MENSAL)**

(apenas os servidores administrativos têm usado este direito, porque para os demais o valor do desconto é maior que o que irá receber)

Observação: No mês que o servidor tirar **férias**, o sistema lança automaticamente o desconto dessa gratificação, atentar então para n**ão descontar duas vezes** esse valor ao lançar o valor do desconto.

**1º passo**: pegar as folhas ponto do mês que for lançar o desconto;

**2º passo**: abrir a planilha salva em: NUAP-MOVIMENTAÇÃO FINANCEIRA-2012-AUXÍLIO TRANSPORTE, na aba do mês que for lançar o desconto;

**3º passo:** conferir em o valor recebido a título de auxílio transportes (e lançá-lo na coluna de valores recebidos), se houve **férias** nesse mês o sistema já desconta um certo valor, logo terá que **abater**;

**4º passo:** lançar quantos dias trabalhou na coluna dias trabalhados (presença)

**5ª passo**: lançar o valor do que resultar na coluna **desconto** a título de auxílio-transporte no SIAPE usando a função **\>FPATMOVFIN**

Observações: 1.providenciar o acerto do mês anterior, pois o auxílio-transporte é pago **antecipadamente**. O valor a ser observado é o do mês do pagamento. EX: O servidor pediu aumento do vale no dia 20 de março de 2006\. Deve pagar na folha de abril, o valor da diferença paga em fevereiro para ser usado em março. E da diferença paga em março para usar em Abril, sequência 6\.

Descontar os dias não trabalhados, pois paga-se 22 dias.

NO SIGEPE:

Exclua o benefício no Sigepe Benefícios com a data mais antiga que conseguir, para evitar futuros acertos automáticos.

Faça a atualização pelo FPATMOVFIN: ASSUNTO DE CÁLCULO para lançamento sem prazo no Siape tela preta: 44\.

**Comunica de Março de 2025:**

 “*Desta forma, as rubricas abaixo serão utilizadas SOMENTE para lançamentos automáticos 00951 AUXÍLIO-TRANSPORTE 00370 AUXÍLIO TRANSPORTE-CLT 82850 AUXÍLIO-TRANSPORTE CDT .*

*Para os casos em que forem necessários ajustes manuais, estes, deverão ser realizados nas rubricas específicas, criadas exclusivamente para esse fim. Essas rubricas devem ser utilizadas apenas em situações excepcionais e pontuais 83297 ACERTO \- AUX TRANSPORTE AT 83296 ACERTO \- AUX TRANSPORTE CLT 83295 ACERTO \- AUX T RANSPORTE CDT.*”

# Pagamento de Indenização pela Flexibilização Voluntária do Repouso Remunerado \- IFR

RUBRICA: 83081

Montar macro:  
Planilha com os servidores aprovados no Frequência.  
Planilha arquivo .csv na pasta Macro seq.6.  
Monta macro python.  
FPATMOVFIN, rodar a macro no tela preta.  
Doc. Legal: Lei nº 13.712/2018  
JUSTIFICATIVA:                                                
INSTRUÇÃO NORMATIVA N° 108, DE 06/04/2023 E REGULAMENTO R005  
PAGAMENTO DE INDENIZACAO POR FLEXIBILIZACAO VOLUNTARIA DO\_\_\_  
REPOUSO REMUNERADO IFR. CONFORME PROCESSO SEI \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
*08675.001115/2023-95* *Ofício 65 (SEI nº 66614313\)*\_\_\_\_\_\_\_\_\_\_\_\_  
IFR OCORRIDO NO MES DE JUNHO DE 2025.\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# AUXÍLIO ALIMENTAÇÃO

 **inclusão e exclusão \-** rubrica **00136**

**Valor pago em 2024 : R$ 1.000,00**

**\>CDATALIIND, (PARA EXCLUIR TAMBÉM)**

preencher: **Data início** – data do ingresso e **tipo**: A

No primeiro mês lançar manualmente no **FPATMOVFIN**, sequência **1 proporcional** (para o mês **atual**) e **sequência 2 integra**l (para o **mês seguinte adiantado**), ambas com prazo **001**. valor: **R$ 1.000,00**  
	

# AUXÍLIO 	PRÉ \- ESCOLAR

 \- se o pedido for lançado **na 	folha de pagamento do mesmo mês do nascimento**  
	  
**Valor pago em 2024:  R$ 484,90 por dependente.**  

**observação: 	APOSENTADO NÃO FAZ JUZ**

Se 	o pedido for lançado **na folha de pagamento do mesmo mês do nascimento** 	do filho, basta fazer:  
	

1\. 	o cadastramento do dependente na função ***\>CDIADEPEND** 	e o sistema paga 	automaticamente sem fazer mais nada.*  
	

(precisa 	apenas verificar se o filho que nasceu já foi incluído em: 	**\>CDCODEPEND** 	(01 	AUXILIO-PRE ESCOLA – INDIRET).  
	

2\. 	Alterar nº de dependentes no: 	**\>CAIASERVID** 	– mudar o **número** 	de dependentes  
	

	  
	

**06\. 	AUXÍLIO 	PRÉ- 	ESCOLAR** \- 	se o pedido for lançado **em 	folha de mês posterior** 	a	data do requerimento)  
	

	Se for **depois**, além do cadastramento, precisa pagar os **atrasados na função:** \>FPATMOVFIN  
	

1 – Lançar o dependente do servidor na função ***\>CDIADEPEND** (É preciso **excluir** a linha do tipo **02** – aux pré-escolar direto. O sistema só paga o **indireto e** deixar os demais conforme a declaração).*A data é a do primeiro requerimento.  
	

2 – Alterar nº de dependentes em ***\>CDIADEPEND*** 	– acrescentando o novo dependente  
	

3 – Pagar o auxílio pré-escolar (\>FPATMOVFIN) referente aos meses **anteriores** conforme a data do requerimento **e descontar a cota parte correspondente**:  
		

**Obs:**  
	

* 		  
   precisa lançar o **crédito** e depois também o **débito** (que depende da faixa salarial R$8,90; R$17,80; ou R$4,45 	apenas para os novos PRF). 	Basta ver qual o sistema lançou na rubrica automática na função \>FPCLPAGTO em: D 73580 COTA PARTE PRE-ESCOLAR e copiar igual).  
   		  
* nunca lançar valor proporcional, **sempre** integral  
   	

	

	  
	

	**Obs:** 	As faixas salariais é que determinam a porcentagem do desconto da cota parte conforme a faixa salarial do servidor:  
	

	 FAIXA 	 VALOR BASE VALOR DO SUBSÍDIO 	  
	

	 01 5,00% 	 de 6.174,85 até ….  
	

	 02 10,00% 	 12.349,70 até …..  
	

	 03 15,00% 	 18.524,55  
	

	 04 20,00% 	 24.699,40  
	

	 na tela:  
	

REND/DESC: 	**D** 	 	  
	

CODIGO 	 : **0700** 	 	  
	

SEQUENCIA: 	**6** 	 OPERACAO (I/A/E): **I** 	 	  
	

valor 	informado (R$ 89,00)  
	

D= 	Rubrica **73580**  
	

	  
	

	  
	

**1\. 	Qual a legislação que regulamenta o auxílio pré-escolar?**  
	

**Decreto 	nº 977, de 10 de novembro de 1993; Instrução Normativa SAF n° 12, de 23 de dezembro de 1993; Portaria nº 6 58, de 06 de abril de 1995\.**  
	

**2\. 	Quem tem direito a receber o auxílio pré-escolar?**  
	

	  
	

**O 	auxílio pré-escolar é destinado aos dependentes dos servidores 	públicos da Administração Pública Federal direta, suas autarquias e fundações, em efetivo exercício, na faixa etária compreendida do nascimento aos 5 anos de idade.**  
	

**3\. 	Qual é o valor do benefício?** Os valores estão “congelados” desde a PORTARIA Nº **658, DE 06 DE ABRIL DE 1995**,	em **R$ 	89,00**, porém a cota-parte a ser descontada varia conforme a faixa salarial de **R$ 4,45; R$ 8,90 ou R$ 17,80**.  
	

	

**4\. 	Como é calculado o valor da participação do servidor (cota parte)?**  
	

**A cota-parte referente à participação dos servidores e, com sua anuência, é consignada em folha de pagamento, e ocorrerá em percentuais que variam de 5% (cinco por cento) a 25% (vinte e cinco por cento) incidindo sobre o valor-teto, proporcional ao nível de 	sua remuneração, a ser descontada na folha de pagamento referente ao mês de competência da concessão do benefício.**

Os valores estão “congelados” desde a PORTARIA Nº **658, DE 06 DE ABRIL DE 1995** em **R$ 89,00**, porém a cota-parte a ser descontada varia conforme a faixa salarial de **R$ 4,45; R$ 8,90 ou R$ 17,80**.

**Documentos necessários: 1.formulário de requerimento do auxílio; 2\. formulário de cadastro de dependente; 3.certidão de nascimento; 4\. número do CPF**

# AUXÍLIO NATALIDADE

**observação: APOSENTADO FAZ JUZ**

**ATENÇÃO: VALOR EM 2022 *R$ 659,25***

1º Passo: Cadastrar o dependente **primeiro em \>CDIADEPEND**

Em caso de gêmeos, cadastrar todos os filhos antes de pagar o auxílio

2º Passo: **CDINAUXNAT**

Digitar a matrícula do servidor e depois o CPF da mãe.

Selecionar para qual filho quer pagar.

Para cadastrar o auxílio para outros filhos, volte na mesma operação e selecione o outro. 

* 	  
   **OBSERVAÇÕES**

***NA HIPÓTESE DE PARTO MULTIPLO (GÊMEOS), O PAGAMENTO DO AUXILIO SERA NO VALOR DE R$ 659,25 PARA O PRIMEIRO FILHO E PARA OS DEMAIS FILHOS O VALOR CORRESPONDENTE A 50% POR CENTO DO DO VALOR PRINCIPAL, CONFORME EXEMPLO ABAIXO:***

***P1º FILHO*** **R$ *659,25***

***2º FILHO R$ 988,87***

***3º FILHO R$ 1318,50***

* 	  
   Fundamentação Legal: Art. 160, I, c da Lei nº 5.810/94.  
   	  
* O 	que é?  
   R.É um benefício de natureza assistencial devido ao servidor no valor correspondente a um salário-mínimo, após a apresentação da certidão de nascimento para a inscrição do dependente.  
   	  
* Qual o valor do benefício?  
   Já o menor valor básico da Administração Pública Federal, de acordo 	com a [**Portaria nº 51**](http://www.planejamento.gov.br/secretarias/upload/Legislacao/Portarias/2013/Portaria_51.pdf), publicada EM **14/02/2013** 	no Diário Oficial, corresponde ao cargo de nível auxiliar do Seguro Social, **R$ 523,65.**  Ele	será pago a título de Auxílio-Natalidade à servidora que o requerer por ocasião do nascimento de filho, inclusive no caso de natimorto.

O dispositivo legal que ampara o recebimento do Auxílio-Natalidade é o artigo 196 da Lei 8.112/90, que estabelece, ainda, o acréscimo de 50% por filho, no caso de parto múltiplo.

* 	  
   Onde 	requerer?  
   R.O 	servidor deverá ingressar com o seu pedido junto ao seu órgão de lotação.

**INSALUBRIDADE – lançamento e exclusão é no SIAPEnet; porém para pagar valores eventuais é no SIAPE**

**\>FPATMOVFIN**

Seqüência : 1

PRAZO: em branco

ASSUNTO DE CÁLCULO : 01

PERCENTUAL : 10% no sistema coloca ( 1000\)

sem valor informado

Quando for valor informado o prazo é 001 e não tem porcentagem nem assunto de cálculo.

# PERICULOSIDADE

**Se for pagar avulso:**

RUBRICA : 00067

FOLHA/FPATMOVFIN

**Se for para conceder de forma permanente:**

Acesse o Siapenet na função: Órgão/UPAG \> SAÚDE E SEG DO TRABALHO\> AVALIAÇÃO AMBIENTAL \> CONCESSÃO DE ADICIONAIS \> LOCALIZAR SERVIDORES / GERAR PORTARIA

Atenção:

1\. O laudo precisa estar **já** cadastrado no siapenet no caminho: Órgão/UPAG \> Adicional \> Laudo- INCLUIR.

2\. A UORG do exercício (não é só de lotação) do servidor deverá estar cadastrada entre as que fazem jus ao recebimento do adicional (se não estiver, precisa incluí-la na função: Órgão/UPAG \> Adicional \> Laudo – ALTERAR clicando em uorg\* e escolhendo a do exercício do servidor).

***LICENÇA PATERNIDADE***

*Basta entrar na função \>CAINOCORSE e lançar o código **00122***

*INICIO DA OCORRENCIA : \_\_\_\_\_\_\_\_\_*

*FIM PREVISTO DA OCORRENCIA: \_\_\_\_\_\_\_\_\_*

*FIM REAL DA OCORRENCIA : \_\_\_\_\_\_\_\_\_*

***LICENÇA NOJO (falecimento pessoa da família)***

**1.O que é?**

E a concessão de licença ao servidor para afastar-se do serviço, sem prejuizo, ***por 8 (oito) dias***

***consecutivos e***m virtude de falecimento de pessoa da família.

**2.Requisitos:**

**2.1.** falecimento de pessoa da família;

**2.2.** para esta licença, considera-se pessoa da família o cônjuge, companheiro(a), pais, madrasta ou padrasto, filhos, enteados, menor sob guarda ou tutela e irmãos.

**3\. Fique atento para:**

**3.1.** a licença nojo e considerada como de efetivo exercício;

**3.2.** o período de licença começa a contar na data do falecimento do familiar;

**3.3.** esta licença interrompe pagamento de vale transporte

***11\. LICENÇA PARA ASSUNTOS PARTICULARES E LANÇAMENTO DE EXONERAÇÃO***

1. 	  
    	Fazer o acerto, adicional noturno, vale alimentação e etc;  
    	  
2. Desligar o parâmetro de AUX. ALIMENTAÇÃO (\>**CDATALIIND**), e Aux.Transporte (**CDATAUXTRA).**  
    	  
3. CORTAR O PAGAMENTO DO SERVIDOR:

**\>CDATAFAST (lançar afastamento- esta função “corta o pagamento” e não deixa gerar passivo de reposição ao erário)** ESTA TRANSAÇÃO FOI INATIVADA. Agora está no Sigepe

**( \_ ) 0096 SUSTEMAMDI (é o código de afastamento indicado para suspender pagto do servidor enquanto não sai portaria de recondução ou de posse em outro cargo)**

**( \_ ) 104** \- TRAT ASSUNT PARC ART 91 – 8112/90

Após a data da publicação inserir ocorrência no:

**SIAPE,SIAPECAD,AUSENCIAS,AFASTAMEN,CAINOCORSE**

**Encerrar aposentadoria sem certidão de óbito:**

Coloca o código 243  SUSPENSÃO TEMPORÁRIA ADMINISTRATIVA (\>CAENEXCAPO) para não gerar folha para o aposentado.

Quando tiver a certidão, exclui esse afastamento (\>CACAENCAPO) e encerra a aposentadoria por óbito.

**12\. LPA ( licença prêmio por assiduidade)**

SIAPE, SIAPECAD, AUSÊNCIAS, LPA, **\>CAIFGZLPA**

Se o servidor pedir para dividir o período , trocar o nº 1 pelo número de meses pedidos.

**Se errar, ou o servidor mudar o período, CAEXGZLP**

**13\. SUSPENSÃO DE DESCONTO EM FOLHA DE CONSIGNATÁRIA não autorizado**

**PROCEDIMENTOS LEGAIS:**

1\. SERVIDOR, APOSENTADO OU PENSIONISTA ABRE TERMO DE OCORRÊNCIA JUNTO A UPAG;

2\. ÓRGÃO RECEBE DECISÃO JUDICIAL PARA SUSPENSÃO DO DESCONTO CONSIGNADO

NA FOLHA DE PAGAMENTO;

3\. ÓRGÃO COMUNICA A CONSIGNATÁRIA SOBRE A ABERTURA DO TERMO DE OCORRÊNCIA OU RECEBIMENTO DE DECISÃO JUDICIAL;

4\. AS PARTES TERÃO QUE CUMPRIR RIGOROSAMENTE OS PROCEDIMENTOS E PRAZOS ESTABELECIDOS NOS DOCUMENTOS LEGAIS CITADOS ACIMA;

**PROCEDIMENTOS OPERACIONAIS(NO SIAPE)**:

1\. A TRANSACAO "TBINCORUBR" ESTA DISPONIBILIZADA PARA USUÁRIOS COM PERFIL FOLHA DE PAGAMENTO (MANUTFOLHA);

2\. UTILIZAR A TRANSAÇÃO "\>**TBINCORUBR**" PARA INCOMPATIBILIZAR MATRÍCULA O SERVIDOR, APOSENTADO OU PENSIONISTA COM RUBRICA DE CONSIGNAÇÃO. É IMPORTANTE O PREENCHIMENTO DA JUSTIFICATIVA QUANDO DA UTILIZAÇÃO DA REFERIDA TRANSAÇÃO CONTENDO DADOS DO TERMO DE OCORRÊNCIA ABERTO OU DA DECISÃO JUDICIAL RECEBIDA O CPF DO USUÁRIO QUE EXECUTOU A TRANSAÇÃO FICARÁ GRAVADO NO HISTÓRICO DA TRANSAÇÃO E SERÁ VISUALIZADO NA CONSULTA "TBCOINCRUB".

**\>ADCOLOG** – Consulta lançamentos feitos pelo servidor.

**\>CAIACGMAT –** Observações sobre lançamentos para Servidores

**13\. LANÇAMENTO DE ADICIONAL TEMPO DE SERVIÇO**

DNER – CLT

Início: ......

Fim: 11dez1990

órgão – 49000 Tipo: \- Bruto TAS	

Nat jur – 01 Reg Jur- 01 Ativ Ext – 136

DNER – RJU

Início: 12dez1990

Fim: 03fev1991

órgão: 49000 Tipo: \- Bruto TAS	

Nat jur – 01 Reg Jur- 02 Ativ Ext – 136

MJ \- PATRULHEIRO

Início: 04FEV1991

Fim: 02JUN1998

órgão: 20000 Tipo: \- Bruto TAS	

Nat jur – 01 Reg Jur- 02 Ativ Ext – 136

só faz o TAS até aqui. A partir do MJ-PRF é PCA. Não pode ser TAS.

MJ – PRF

Início: 03jun1998

órgão 20000 \-Até 31jul2004

órgão 30802 – a partir de 01ago2004

**14\. PAGAMENTO DE ENCARGO DE CURSO OU CONCURSO**

1º passo: Acesse \>FPATMOVFIN

2º passo: Na tela abaixo lance da seguinte forma:

DADOS DA RUBRICA

REND/DESC: R

CODIGO : 00066

SEQUENCIA: 6 OPERACAO (I/A/E): I

**15\. ACOMPANHAMENTO DO LANÇAMENTO DAS PROGRAMAÇÕES DE FÉRIAS**

1º PASSO:Ir em Atualização cadastral/férias/consultas UPAG/Solicitação de férias

2º PASSO: Escolher a UPAG  e o ano do exercício (em regra o próximo ano);

3ºPASSO: clique em analisar uorgs

4ºPASSO:Na coluna férias não marcadas, verificar o eventual motivo de ainda não terem sido marcadas clicando no número de ocorrência desta coluna, caso exista.Não Marcada

**16\. AVERBAÇÃO DO CURSO DE FORMAÇÃO DA PRF (TURMA DE 2004 E 1999\*)**

**\*Observação: se for lançar a o tempo de serviço da turma de 1999 começar pelo** 7º PASSO e usar como modelo o processo **08656013730/2006-71** da PRF LUIZA DE MARILAC REZENDE COUTO

1º PASSO: Verificar as **datas** e os **valores** recebidos durante o curso de formação da PRF no site abaixo:

[http://www.transparencia.gov.br/PortalComprasDiretasPrincipal2.asp](http://www.transparencia.gov.br/PortalComprasDiretasPrincipal2.asp)

2º PASSO: Clique nos botão “**exercício**”, colocando o ano que o servidor realizou o curso na PRF; clique no botão “**por Favorecido**” escolhendo a opção “pessoa física empresas e outro”; a seguir clique em CONSULTA

3º PASSO: irá então aparecer a nova tela, na parte de baixo dela, logo à frente da palavra “**Pesquisar**”: dentro do retângulo digite **o nome, parte do nome ou CPF do servidor** que pediu a averbação e clique em **OK;** Vai aparecer o nome do servidor em **azul, clique nele;**

4º PASSO: Na próxima tela clique na frase escrita em azul

5º PASSO: Na próxima tela clique na frase escrita em azul (departamento de polícia rodoviária federal)

6º PASSO: Aparecerão vários valores do ano solicitado.

Faça uma tabela com esses valores para calcular os 11% sobre cada um, mês a mês. (basta colocar o valor e multiplicar por 0,11, que o valor obtido na calculadora já serão os 11%;

Exemplo R$300,00 **\*** 0.11= 33

7º PASSO: (correção dos valores do 11% desde o dia do recebimento da bolsa até o dia da véspera em estiver calculando o valor)

entre no site:[https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormCorrecaoValores.do?method=exibirFormCorrecaoValores\&aba=4](https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormCorrecaoValores.do?method=exibirFormCorrecaoValores&aba=4)

Neste site (conforme tela abaixo), há um ferramenta de cálculo dos valores recebidos, onde se digitará:

1\. Data inicial: será a data do dia do recebimento dos valores da bolsa do curso;

2\. Data final: será a data do dia **anterior** ao que você está digitando

3.Valor a ser corrigido: o resultado obtido no 6º passo ( que serão os 11% sobre cada bolsa, mês a mês)

A seguir clique em **corrigir o valor**. Os valores obtidos, serão o Resultado da Correção pela Selic até a data da digitação.

Após o passo acima se digitará uma planilha conforme modelo abaixo que está salva na pasta NUAP em MOVIMENTAÇÃO FINANCEIRA\\2012\\averbação CURSO FORMAÇÃO PRF

Observação: Todos os valores corrigido das bolsas deverão ser **somados**, um a um para se imprimir uma DARF

8º PASSO: O servidor interessado deverá imprimir a DARF com os valores corrigidos das bolsas para serem pagos. Conforme roteiro abaixo

**ROTEIRO PARA PREENCHIMENTO DO Darf**

	

	

	

	 **1635**

**Darf Comum**

PREENCHIMENTO EM GERAL (PAGAMENTOS A PARTIR DE **01.04.97**)

ROTEIRO PARA PREENCHIMENTO DO Darf

| 			 CAMPO DO Darf 		 | 			 O QUE DEVE CONTER 		 |
| ----- | ----- |
| 			 **01** 		 | 			 **Nome** e **telefone** do contribuinte. 		 |
| 			 **02** 		 | 			 **Data** da ocorrência ou do encerramento do período base no formato **DD/MM/AA.** 		 |
| 			 **03** 		 | 			 Número de inscrição no **CPF** ou CGC. 		 |
| 			 **04** 		 | 			 **Código da receita que está sendo	paga**. Os códigos de tributos e contribuições administrados pela SRF podem ser obtidos na [Agenda Tributária.](http://www.receita.fazenda.gov.br/Pagamentos/agenda/default.htm) 		 |
| 			 **05** 		 | 			 Preencher com: \- código da Unidade da SRF responsável pelo despacho aduaneiro, se relativo ao recolhimento do Imposto de Importação e IPI Vinculado à Importação; \- número do imóvel rural na Receita Federal, se relativo ao ITR/97 ou ITR/98; número do lançamento, se relativo ao ITR/96 ou anteriores; \- código do município 	produtor, se relativo ao IOF \- Ouro; \- número da respectiva inscrição, se relativo a débito inscrito em Dívida Ativa da União; \- número do processo, se pagamento oriundo de processo fiscal de cobrança ou de parcelamento de débitos; \- número de inscrição no Departamento Nacional de Telecomunicações, se relativo a taxa FISTEL; \- número de inscrição do imóvel, se relativo a rendas do Serviço de Patrimônio da União. 		 |
| 			 **06** 		 | 			 **Data de vencimento** 	da receita no formato DD/MM/AA 		 |
| 			 **07** 		 | 			 **Valor principal** da receita que está sendo paga. 		 |
| 			 08 		 | 			 [Valor da multa, quando devida](http://www.receita.fazenda.gov.br/Pagamentos/PgtoAtraso/atraso.htm) 		 |
| 			 09 		 | 			 [Valor dos juros de mora, ou encargos do DL \- 1.025/69 (PFN), quando devidos](http://www.receita.fazenda.gov.br/Pagamentos/jrselic.htm) 		 |
| 			 **10** 		 | 			 Soma dos campos 07 a 09\. 		 |
| 			 11 		 | 			 Autenticação do Agente Arrecadador. 		 |

Passo 9 **\- Encaminha-se o processo à DIREC/CGRH/DPRF, para análise do assunto. Se, de acordo, encaminha-se à SOFIP/CGRH, para providenciar o cálculo e recolhimento da Contribuição Patronal ao PSS (22% sobre o valor pago ao servidor, como bolsa, durante o curso de formação).**

Passo 10 \- Após o recolhimento da Contribuição Patronal o processo deverá retornar à regional de origem para que sejam tomadas as providências cabíveis à conclusão do pleito, que são:

* 	  
   	**Elaborar a Certidão de Tempo de Serviço do Curso de Formação da PRF e a portaria de averbação desse tempo;**  
   	  
* 	**Publicar, em Boletim de Serviço, a Portaria de averbação do tempo de serviço referente ao período em questão;**  
   	  
* 	**Cadastrar a averbação no SIAPE/SIAPECAD;**  
   	  
* 	**registrar na pasta funcional;**  
   	  
* 	**Cientificar o servidor; e**  
   	  
* 	**Arquivar os autos.**

**17\. VERIFICAR FORÇA POR NÚCLEOS/SEÇÕES/GABINETE/DELEGACIA**

1.Acesse o SIAPE na função **\>CAEMFORCTR** ( FORÇA DE TRABALHO)

Escolha a opção: UORG: **250**

( x ) DO CARGO PARA A ESTRUTURA DA UORG INFORMADA.... CARGO: **911001** (digite o código de cada cargo, são cerca de 15 em MINAS GERAIS, ex. PRF, motoristas, telefonista etc)

A seguir aparecerá a tela com NÚMERO (quantidade) de servidores por seção/núcleo/gabinete/delegacia

**18\. ADICIONAL NOTURNO**

**\> FPATMOVFIN**

Rubrica 00028

Seqüência: 6 a 9

Valor informado: calcular pela planilha

Observar macro ( mudar o mês)

**19\. ADVERTÊNCIA, ELOGIOS**

1º \-Primeiro tem que editar documento legal. Portaria, ofício, memorando, BS em **\>DPEDITADL**	

**![][image1]**

	

na opção **041\-A SERVIDOR/BS**

2º-e só depois lançar a referência elogiosa 				**CAINELOGIO**

**20\. AUSÊNCIAS**

Lançar em: \> **CAINOCORSE**

***21\. SUSPENSÃO DO EXERCÍCIO DA FUNÇÃO PÚBLICA ( NOVO) :***  
C**om base no Art. 319,VI e § 4º do CPP**, a mesma deverá ser lançada no SIAPE na  ocorrência de Afastamento **\>CDATAFAST \- ( ATUALIZA AFASTAMENTO )**  
ESTA TRANSACAO FOI INATIVADA. Agora está no Sigepe  
 Grupo   **03**  
 Código  **024 \-  DECISAO JUDICIAL**,   ser observado o art. 45 § 4º da IN nº CG/2010.  
 Se quiser consultar códigos semelhantes usar:  
         **\>COTBOCORRE**

Licença médica: Verificar o tipo de licença e fazer o lançamento. Comparar os dias homologados com os dias lançados na folha. Se estiver diferente, olhar com o chefe da delegacia ou os médicos para consertar o erro.

Se o servidor estiver de férias: Se a licença médica acontecer antes das férias o que vale é o atestado médico. As férias deverão ser remarcadas, impresso uma notificação manual e enviar à época das férias ao servidor sistema só aceita reprogramação após o servidor gozar todos os períodos.

Se for durante as férias, o que vale são as férias.

# REMOÇÃO

1\) – Remoção para o mesmo estado: Observar a portaria de remoção e publicação no BS. Só pode remover após publicação. Função: \>CAROCOLHIS

Para consultar UORG (de origem normalmente é a UORG 250\) UORG de Destino, usar F1 a partir de 250, sendo que é preciso observar na portaria de remoção o núcleo/seção/delegacia específico para lançar

**Início da Lotação – data da publicação do BS ou conforme estiver na portaria. (se for preciso ver a data da publicação, entrar na intranet em** [http://intranet.sede.dprf.gov.br/PortalIntranet/intranet/boletinsServico.faces](http://intranet.sede.dprf.gov.br/PortalIntranet/intranet/boletinsServico.faces)

**DL de lotação**: escrever nº da portaria, data da assinatura, nº do BS e data da publicação.

**SELEÇÃO MANUAL.** ENTER

Na Matrícula NOME DO SERVIDOR Colocar a matrícula do servidor (se não tiver dar F1 ) e ao lado preencher com a lotação atual (para UORG que está indo \- lotação e exercício iguais).

Importante :FAZER integração: \>**CAEEINTGRS**

**Atenção:** os servidores cedidos/requisitados/movimentados deverão ser incluídos na lotação **\>RECDEX**

A lotação específica dos servidores cedidos/requisitados/movimentados estarão no campo localização de exercício do servidor (onde encontramos os órgãos em que os servidores estavam cedidos).

As Regionais de origem deverão cadastrar a remoção dos servidores por meio das transações:

 **\>CATCREMOCA:** disponibilização de servid

or removido

 **\>CADLREMOCA**: cadastro de remoção e desligamento do servidor

A Regional de destino recebe o servidor por meio da transação  **\>CALCEXERIN**

LEMBRAR de INCLUIR (Não alterar, incluir mesmo) a lotação no SRH;

## PROCEDIMENTOS DE REMOÇÃO DICAD:

	Incluir o processo no bloco interno de remoções seguindo o padrão de informações.

	Incluir marcador de remoção no processo e o prazo no marcador.

Alteração no SRH. Não é para usar Alterar, e sim Incluir nova unidade de lotação. Observar a unidade mais próxima da atual, o SRH não tem as novas unidades. Caso não possua, incluir na unidade Superintendência.

	Incluir no processo ofício (modelo) no processo informando a remoção e encaminhar para as duas unidades de GP regionais envolvidas.

Incluir no processo portarias de Remoção e Designação (se houver).

	Caso tenha cargo de chefia, é necessário incluir a chefia no SRH também. A descrição da função também é de acordo com o modelo antigo, ajustar para ficar equivalente.

	Encaminhar o processo via Sei e também notificar por email Sei.

Observar o valor no auxílio alimentação que o servidor recebia no estado que trabalhava. O auxílio alimentação é pago no mês anterior (referente a 22 dias) para ser gozado no mês seguinte Fazer o acerto proporcional ao dia da remoção caso os auxílios sejam diferentes.

**Nos casos de erro por lotação de exercício divergente é preciso cancelar a remoção.**

**Caso seja necessário o cancelamento da remoção-** Deve-se fazer os dois passos a seguir,

**\>CAEXLOTERR-** Para excluir a lotação por erro, e depois fazer:

**\>CAEXLOCEXE** para cancelar o exercício,

FAZER integração: \>**CAEEINTGRS, (**depois é preciso refazer a lotação com as correções)

**2\) Remoção para o fora do estado**.

FAZER integração: \>**CAEEINTGRS** para verificar se há algum erro.

Realizar os acertos financeiros e juntada de todos os documentos pertinentes no AFD dos servidores.

Manual do Ministério da Economia (Doc SEI n°25420596)

UPAG de origem: \>CATCREMOCA e \>CADLREMOCA

UPAG de destino: \>CALCEXERIN

**Para alterar a uorg.**

De servidor aposentado

**CACAUTLOC \-\> CANCELA ULT UORG LOCALIZAÇÃO**

# CORREÇÃO DE PCA (FUNDAMENTAÇÃO DA APOSENTADORIA

Na pasta: CADASTRO\\PCA\\2012\\CORREÇÃO PCA APOSENTADOS, estão as planilhas com as relações de aposentados que há necessidade de fazer este serviço. Porém, às vezes aparecerão outros aposentadorias em que poderão ser também necessário fazer tal operação no SIAPE.

**1º passo:** desarquivamento da pasta pessoal e dos processos da aposentadoria (sempre), e ainda LPA e averbação de tempo (se houver)

**2º passo:** verificar se o servidor já tem PCA em **\>CACOPCA** (SIAPE) você verá todos os PCA que já foram feitos para o servidor, sendo que haverá um linha para cada PCA (normalmente os aposentados só têm o 3º PCA, logo precisaria lançar o 1º e 2º e tempo de serviço anterior averbado em **\>CACOTAS** (se o tempo de DNER e DPRF estiverem averbados em CACOTAS estará errado, **imprima** e depois **exclua** estes tempos em **\>CAEXTAS ;**

**3º passo:** Se a correção estiver sendo feita na ficha de um PRF **que tiver LPA não gozada**, fazer o cálculo automático da LPA na função **\>CACSLPAHT** (concessao de LPA – automatica), porém se for servidor não PRF (administrativo) tem que ir na função \>CACSHTLPA;

**4º passo:** logar no SIAPE na função \>**CAINPCAHIS,** depois entrar na pasta NUAP em: CADASTRO\\PCA\\2012\\CORREÇÃO PCA APOSENTADOS\\MANUAIS PARA CADASTRO PCA, onde deverá começar a tarefa da correção do PCA em regra, pelo 1º PCA (que é o Cargo de PRF Provimento período do **1º Ingresso até 11/12/1990** período em houve a transformação dos Regimes Celetista para Estatutário) abrindo o arquivo em PDF e copiando e colando, atente para saltar em alguns pontos e alterar alguns dados para MG;

**Atenção** muito cuidado na hora de lançar a primeira informação (ORGAO DO PCA), se lançar errado, todo o serviço de lançamento do 1º PCA será **perdido**, porque a primeira tela mostrará o código **atual** que sempre será **DIFERENTE** do que é **preciso lançar** (copiando do texto do manual PCA em PDF). Além disso há outros dados (exemplo fator 1.4) que não é possível alterar, se isso ocorrer, precisará também excluir o PCA .

**1º PCA**: (época do DNER); obs. Na segunda tela usar **6º** DNER-**MG**, no lugar de 1ºDNER-RJ e pular a 1ª e 3ª linhas (do **ingresso** no DNER até 11dez1990);

**2º PCA**: 49201 (ainda é época do DNER); (de 12DEZ1990 a 03FEV1991)

**3º PCA**: 20000 (época que foi feita a mudança para o **Ministério da Justica**); (de 04FEV1991 a 03MAI1998);

**4º PCA:** (também órgão 20000) Cargo de PRF com ingresso por meio da Portaria 441 de 06/07/1994;(de 04MAI1998 a 02JUN1998)

**5º PCA:** (também órgão 20000); (de 03JUN1998 a 31JUL2004)

**6º PCA:** (também órgão 20000\). (de 01AGO2004 a 31JUL2006)

**7ª PCA:** (órgão 30802)A PARTIR DE 01AGO2006

Se errar no lançamento de algum dado ir em: **\>CAALDTPCA** que irá possibilitar a alteração do dados lançados, EXCETO algumas informações tais como ***ORGAO DO PCA e fator 1.4, que neste caso será necesário excluir todo PCA já feito, fazendo o seguinte:***

1.Vá na função: **\>CADTMATFP** (que realiza a **desativação** da matrícula para fins de integração);

2.Exclua o PCA na função: **\>CAEXPCAHIS** (que realiza a exclusão do PCA historico);

3.Vá na função: **\>CARTMATFP** (que REATIVA a MATRícula para INTEGRAção, importante se não fizer esta função, não conseguirá prosseguir na tarefa de corrigir o PCA e o servidor ficará SEM PAGAMENTO\!\!\!\!\!;

4\. Após o realizada tarefa de exclusão do lançado errado voltar na função **\>CAINPCAHIS** para lançar novamente corrigido.

**Observação**: em alguns casos ao tentar lançar o PCA o SIAPE irá “criticar” aparecendo um letra I (**Impedimento**) ou letra A (alerta), nestes casos será necessário **excluir** cada uma dessas com a letra I(somente) na função \>CAEXOCORSE (que exclui as ocorrencias do servidor), porém MUITO CUIDADO, antes de excluir esta ocorrencias, é necessário **copiar** todas elas e **imprimir**, porque terão que ser **todas** novamente lançada no siape na função \>CAIFHISOCO; após realizar essas operações poderá então seguir com o PCA;

**5º passo:** após incluir os PCA necessários (***em regra para-se no 3º PCA***, pois o 4º teria sido lançado na época da aposentadoria) ir na função: **\>CAALPROVEN** (onde será feita a alterção da fundamentação conforme a portaria da aposentadoria (todo o serviço até agora foi feito apenas para se chegar neste ponto), nesta tela lançar o 1ª dia do ano corrente conforme tela abaixo:

SIAPE,SIAPECAD,APOSENTADO,PROVENAPOS, **\>CAALPROVEN** (ALTERA PROVENTOS DE APOS)

NOVOS PROVENTOS C/ VIGENCIA A PARTIR DE: 1ª dia do ano corrente (se já tiver feito essa operação no mesmo ano, usar os dias seguintes até que o sistema aceite).

\----------------------------------------------------------------------------

**SENTENCA JUDICIAL** : **N** (S/N) UTILIZA (em regra marca **N**) **CONTAGEM DA LPA EM DOBRO**: (S/N) (**S** se usou e **N** se não usou)

A partir daí, na próxima tela e, em regra, se escolhe a 1ª opção (LC 51). Nesse momento no final da tela há o campo observação em deverá lançar o seguinte texto: Ofício nº 28950/2011/CGU-MG/CGU-PR

**6º passo**: ir na função **\>CACOAPOSSE**, atenção poderá aparecer mais de uma linha/opção, marque a que estiver sem finalização e dê entra.

Na próxima tela faça o seguinte:

( X ) aposentadorias do cpf, clique F1, digite a matrícula , depois digite o X na linha do nome, dê entra.

Irá aparecer várias telas, copie TODAS, imprima todas e junte ao processo de aposentadoria e depois mande arquivar\!\! SE você CHEGOU ATÉ AQUI PARABÉNS você BRILHOU\!\!\!\! GAME OVER\!\!\!

**SIAPE,SIAPECAD,PCA,ALTDADOPCA,CAALDTPCA ( ALTERA DADOS DO PCA )**

**Alteração de PCA para mudar o fator 1.4 para homens, 1.2 para mulheres:**

**Se PCA encerrado ou histórico utilizar a transação**

**CAINREGJUR. Se PCA vigente transação CAALREGPCA**

**![][image2]**

**DEPENDENTES \- inclusão – exclusão \- alteração \-reativação**

Antes de lançar ou alterar, consulte. (CDCODEPEND), se for **novo** dependente

***Incluir** dependente: use a função **CDIADEPEND (e-SIAPE)***

***OBSERVACOES:***

***1\. Para filho e esposa lançar a opção 32 (onde exige a dependência). Ao escolher que funções deixar na tela e quais apagar em regra se usa as seguintes: 01, 03, 09, e 11, as demais tem que apagar os números(para incluir filho, se for cônjuge seria apenas 03 e 11);***

***2\. Cuidado ao incluir o dependente: a tela do SIAPE às vezes mostra o NOME DO DEPENDENTE IGUAL AO DA MÃE (EM VERMELHO), basta mudar onde está o nome igual para ficar certo.***

O dependente deverá estar inscrito no anexo II. Deverá ser lançado conforme estiver no anexo: ex: Imposto de renda , plano de saúde , salário família. Conforme tabela abaixo:

NOME DEPENDENTE: escreva o nome

DATA NASCIMENTO: escreva a data SEXO : F ou M NACIONALIDADE : 1(BRASILEIRO)

GRAU PARENTESCO: 5(conjuge), 8(filhos) CONDICAO : 32 (em regra, que é sem exigencia de condição para esposa e filhos)

NOME DA MAE : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TABELA DE BENEFICIO POR PARENTESCO/CONDICAO

COD DENOMINACAO BENEFICIO

01 AUXILIO-PRE ESCOLA \- INDIRETA (SÓ PARA FILHO MENOR DE 6 ANOS)

02 AUXILIO PRE-ESCOLA \- DIRETA **(NÃO USAR ESTE)**

03 DEDUCAO IMPOSTO DE RENDA (é a letra “A” do requerimento de designação/exclusão de dependente) atenção se for **pais** tem que colocar condição **22** (sem rendimentos) e se for **filho maior de 21 anos** tem que colocar **condição estudante**

04 SALARIO FAMILIA **(NÃO USAR ESTE)**

05 ASSIST A SAUDE SUPLEMENTAR (só pra quem tem plano de saúde) (é a letra “B” do requerimento de designação/exclusão de dependente)

06 ASSIST MEDICO HOSPITALAR

07 AUXILIO FAMILIAR

08 AJUDA DE CUSTO

09 AUXILIO NATALIDADE (PAGA SÓ QUANDO NASCE E SÓ PARA QUE JÁ É ATIVO NA PRF)

11 ACOMPANHAM PESSOA DA FAMILIA (LANÇAR PARA TODOS)(é a letra “C” do requerimento de designação/exclusão de dependente)

Se o servidor colocou (**não**) para qualquer um deles, deverá **apagar** no sistema. A d**ata de inclusão é a data do requerimento.**

**Para Excluir** dependente**:** CDEXDEPEND

**Para Alterar** dependente: CDIADEPEND (E-SIAPE)

OBSERVAÇÕES IMPORTANTES:

Se for preciso alterar o cadastro **Para Reativar** um dependente ou apenas u**ma das opções que foram excluídas** faça o seguinte:

1\. entre na função **\>CDIADEPEND**

2\. selecione o dependente na “subtelinha” que aparece na tela marcando um X nele e digite ENTRA;

3\. Na próxima tela preencha **mais uma linha com a mesma opção** que havia sido excluída e na mesma data que aparece na linha excluída (encerrada);

Obs. Se for para **reativar** o dependente faz **21** anos (o sistema retira automaticamente), precisa alterar o item **condição de 32 para 14** neste caso, o servidor deverá requerer nova inclusão, apresentando o comprovante da escola);

5\. Se for para **reincluir o “dependente inteiro” e não apenas mais uma função :apague** a linha onde aparece a data da exclusão e o número ao lado, depois confirme.

observação: Para o item **05** (plano de saude 05-ASSIST A SAUDE SUPLEMENTAR) precisa primeiro entrar em **\>CDINTITSAU (para servidores) e** **\>CDINPSTSAU (para pensionista)** colocar **S** plano de saúde escrevendo abaixo o nome do plano (**ex. Geap e outras que tenham CONVÊNIO como o DPRF**), e só **depois** entrar em \>CDIADEPEND para alterar, já que **o siape não deixa alterar se não for titular de plano**. Para concluir a alteração precisa ir de novo em \>CDINTITSAU colocar **N** plano de saúde. (essa providência é **necessária** para permitir que a GEAP possa receber do DPRF sua cota). Atenção: quando o servidor SAIR da GEAP, PRECISA ALTERAR A FUNÇÃO **\>CDINTITSAU** ou **\>CDINPSTSAU** colocar **N** em plano de saúde.

Observação: A **PORTARIA NORMATIVA Nº 5, DE 11 DE OUTUBRO DE 2010\.** QUE INSTITUI O RESSARCIMENTO ***NÃO PERMITE QUE SE RECEBA VALORES POR TER OS PAIS COMO DEPENDENTES,*** APENAS SOBRE CONJUGES, COMPANHEIROS E FILHOS. LOGO NÃO SE RECEBE PARCELA DE PER CAPITA PELOS PAIS. SE TIVER GEAP ELA TEM QUE DESCONTAR A PARCELA DELES NO CONTRACHEQUE.DOS BENEFICIÁRIOS DO PLANO DE ASSISTÊNCIA À SAÚDE SUPLEMENTAR

Observações

1\. A diferença do GEAP é que o valor do per capita é pago pelo governo diretamente para o plano, por isso a impressão de que o valor apenas está "passando" pelo contracheque do servidor. O Benefício para o servidor nesse caso traduz-se no menor valor da mensalidade do plano. Ou seja, enquanto nos outros planos o servidor custeia todo o valor do plano e solicita o ressarcimento, no GEAP o plano já desconta o valor do per capita do valor cobrado do servidor. Portanto, é possível sim que que o valor do plano seja menor que o per capita, principalmente quando há muitos dependentes menores de 18 anos.

**PORTARIA NORMATIVA Nº 5, DE 11 DE OUTUBRO DE 2010\.**

Estabelece orientações aos órgãos e entidades do Sistema de Pessoal Civil da Administração Federal – SIPEC sobre a assistência à saúde suplementar do servidor ativo, inativo, seus dependentes e pensionistas e dá outras **providências.**

**ATENÇÃO. RESSARCIMENTO DE DESCONTO INDEVIDO DA GEAP**

Usar a função FPATMOVFIN, Com os seguintes dados:

**R/D: R receita**

**código/rubrica: 82737 PER CAPITA \- SAUDE SUPLEMENTAR**

**sequencia: 6**

**mês de referecia: o mês do desconto indevido**

**prazo: 001**

**valor: o que foi descontado indevido por parte da GEAP (está aparecendo com sequencia 4\)**

Constatou-se que aquela empresa consignatária estaria deixando de receber repasses de obrigação da UNIÃO (patrocinador) de alguns servidores. Recentemente a GEAP sofreu intervenção da ANS. Os novos gestores se preocuparam em sanar os déficits existentes, dentre eles os decorrentes das falhas cadastrais do SIAPE (\>CDINTITSAU).

Todavia, visando cobrir um débito que era da **União**, a GEAP lançou um débito, na folha dos **servidores**, que aparece na folha de pagamento na rubrica **32623**.

**FUNÇÃO DE CHEFIA \- Nomeação e exclusão**

Obs.fazer **integração** sempre nomear ou excluir a nomeação em \>CAEEINTGRS

funçã

**Nomeação de função de chefia: \>CANOPFUDEX**

| 			 FUNÇÃO 		 | 			 Denominação 		 | 			 Código da Função 		 |
| ----- | ----- | ----- |
| 			 Chefe de **SEÇÃO** 		 | 			 código da denominação: 			**41** 		 | 			 FGR-1 			 		 |
| 			 Chefe de **DELEGACIA** 		 | 			 código da denominação: 			**59** 		 | 			 FGR-2 		 |
| 			 Chefe de **NÚCLEO** Chefe de SETOR | 			 código da denominação: 			**61** 		52 | 			 FGR-3 	/  FEX0101		 		FEX.0102 |

	Caso apresente a mensagem (não existe previsão de função para a uorg) deve-se entrar em contato com o departamento e informar o ocorrido.

Observações: CBO PRF \= 517210 (NÃO É OBRIGATÓRIO)

1\. A data de **posse** do novo chefe é a data da **publicação** da portaria de sua nomeação.

2\. Se não fizerem portaria para dispensar o ex-chefe, usar a mesma da nomeação do novo chefe.

3\. IMPORTANTE: Ao final da operação aparecerá a linha: DESEJA DAR EXERCICIO ?**digite** sempre **N, não dê apenas entra que o sistema também entende como sim\!\!\!.**

4\. O servidor só pode ser chefe no setor que esteja lotado. Se for nomeado apenas substituto não precisa.

5\. Para a nomeação de chefe de núcleo da delegacia não esquecer de remover o servidor para o núcleo de policiamento (no caso das delegacias) e, quando for dispensado, não esquecer de removê-lo de volta para sua delegacia (porque apenas o chefe titular do núcleo pode permanecer lotado nela).

Se a UORG estiver sem chefia é preciso pedir a liberação da uorg ao departamento via comunica.(ver como fazer comunica nesse manual).LIBERAR VAGA: Solicitar via COMUNICA ao Departamento. Informar na comunica qual Tipo de Função, UORG e UPAG, nome e matrícula do a ser nomeado. A função **\>CACODETPFU verifica chefias, consulta chefia.**

ADCOVAGA ( CONSULTA VAGA )

**EXCLUSÃO Dispensa de função de chefia:**

 **\>CAVADIRFEX**Observação importante: Se for chefe do **núcleo** de policiamento e fiscalização, precisa **retorná-lo** para UORG da sua delegacia na função **\>CAROCOLHIS;** fazer a integração na função **\>CAEEINTGRS** e fazer a EXCLUSÃO de chefia.

A data da dispensa do ex-chefe se for simultânea com a nomeação do novo chefe é a véspera da data da publicação da portaria do novo chefe (ou seja, no fundamento legal do ex-chefe, você coloca a data anterior à publicação da portaria... e o novo chefe é a data da publicacao da portaria). Se for NÃO simultânea com a nomeação do novo, será a data da publicação da portaria da dispensa.

037 DISPENSA\_DA FUNCAO/CARGO COMISSAO/CNE

A data da dispensa do chefe **é um dia antes da publicação**.

**fazer integração sempre nomear ou excluir a nomeação em \>CAEEINTGRS**

Se houver problema na nomeação por ter sido nomeado automaticamente o substituto ao se excluir o titutar, use a função \>CAEXNOMEAC que EXCLUI a nomeação. Para isso precisa desativar a matrícula do servidor que, se for preciso excluir a nomeação indevida (use a função \>CADTMATFP, mas não esqueçer de reativar depois\!).

(cuidado se fizer esta função e não fizer a reativação depois com a \>CARTMATFP o servidor ficará SEM PAGAMENTO

OBS: fazer os acertos financeiros no **\>fpatmovfin**;

OBS: Lembrar que para excluir chefia e substituto, lançar a data do documento legal 1 dia antes da publicação se o novo chefe e substituto entrarem no dia da publicação do documento legal.

Depois mudar os servidores no **SRH**\- chefe e substituto

**\>CACODETPFU** ( DETALHE DE PROV.FUNCAO/CC/CNE ) \- CONSULTA AS FUNÇÕES EXERCIDAS PELO SERVIDOR

\>grcoserrub – CONSULTA DE SERVIDORES COM RUBRICA. ve os lançamentos por rubrica – você pega o número e depois joga no \>gremserrub

\>gremserrub \- EMITE SERVIDORES COM RUBRICA.

\>caenexcapo – Encerrar aposentadoria por falecimento

DIRF – Todo mês de fevereiro temos que declarar para poder gerar os comprovantes de rendimento.

Referente aos meses de dez a nov.

\-pagamento de AUXILIO-NATALIDADE: pago a partir do nascimento.

\- o pagamento de SUBSTITUIÇÃO é contado por DIAS. Se o mês tiver 31, você paga os 31 dias.

\- AUXILIO FUNERAL: processo sumaríssimo, feito em até 48h após a comprovação da morte (familiar deve trazer nota fiscal dos gastos) se for familiar, ganha 1 mês de remuneração. Se for outra pessoa, somente paga o valor na NF.

\>GRCOSERRUB – consultar lançamentos feitos em uma rubrica – fpatmovfin // DEPOIS VC VAI EM \>GREMSERRUB através do número da transação que o siape informar

\>FPEXCLPAGC – SERVIDORES EXCLUIDOS DA FOLHA \- consultar essa transação sempre antes de homologar a folha

– acerto na folha de servidor com líquido negativo

\>fpexpspagc – pensionista excluído da folha

\>GRCOFINDDP – mostra relatório de gastos com pessoal- ex: gastos com os servidores ativos, estagiários etc.

\>TBCOSAUSUP – Lista de assistência saúde – per capita

\>TBCOPREESC – Cota parte do pre escolar.

\>TBCOFARBEN – consulta fator de reajuste – bom para fazer aposentadoria- índices de reajuste

\>TBCOPROCES – consulta data de processamento da folha

Consulta de processos – consulta CPROD

site: servidor.org.br – acessar LEGISLAÇÂO (CONLEGIS) ;.. também pode ver TABELA DE REMUNERAÇÃO

HÁBITOS RH\-diário oficial

\-comunicas (ver se sai as trilhas de auditoria) todo pagamento que precisa de justificativa, é requisitado no comunica do siape – AUDITORIA PREVENTIVA

\- Lançar aux transporte \-

\- Lançar per capita – sempre guardar os comprovantes nos processos dos servidores, ver planilhas de operadoras, salvar relatório do siapenet (órgão/upag \- envio e obtenção de arquivos- obtenção de arquivos- saúde suplementar)

\- NA HOMOLOGAÇÃO : sempre ligar para os aposentados para fazer o recadastramento.

recadastramento

\-SERVIDORES NÃO RECADASTRADOS SERÃO EXCLUÍDOS DA FOLHA, SUSPENSÃO NO SIAPE.. NO FINAL DEVE PUBLICAR EM EDITAL

\-Depois de 3 meses, se o órgão não excluir, a segepe exclui depois de 3 meses

siapenet\>modulo orgao\>aba órgão/upag\> atualização cadastral de aposentado e pensionista\>acompanhar atualização cadastral\>selecionar lote de aniversariantes de mês...

# Links importantes

[https://conlegis.planejamento.gov.br/conlegis/legislacao/index.htm](https://conlegis.planejamento.gov.br/conlegis/legislacao/index.htm)

[https://www2.prf.gov.br/webmail/](https://www2.prf.gov.br/webmail/)

[https://www2.scdp.gov.br/novoscdp/home.xhtml](https://www2.scdp.gov.br/novoscdp/home.xhtml)

[https://www.prf.gov.br/portal/acl\_users/credentials\_cookie\_auth/require\_login?came\_from=https%3A//www.prf.gov.br/portal/painel](https://www.prf.gov.br/portal/acl_users/credentials_cookie_auth/require_login?came_from=https%3A//www.prf.gov.br/portal/painel)

[http://www.siapenet.gov.br/Portal/Servico/Apresentacao.asp](http://www.siapenet.gov.br/Portal/Servico/Apresentacao.asp)

[https://www.prf.gov.br/protocolo/login.do?reqXode=logar](https://www.prf.gov.br/protocolo/login.do?reqXode=logar)

[https://servicosdoservidor.planejamento.gov.br/web/segep/portal-gestao-pessoas](https://servicosdoservidor.planejamento.gov.br/web/segep/portal-gestao-pessoas)

[http://www.prf.gov.br/sipac/?modo=classico](http://www.prf.gov.br/sipac/?modo=classico)

[http://www.prf.gov.br/sigrh/login.jsf;jsessionid=871F6114BD9CC6B8A5D3ED77C49F756C](http://www.prf.gov.br/sigrh/login.jsf;jsessionid=871F6114BD9CC6B8A5D3ED77C49F756C)

[http://sei.prf.gov.br/sip/login.php?sigla\_orgao\_sistema=PRF\&sigla\_sistema=SEI](http://sei.prf.gov.br/sip/login.php?sigla_orgao_sistema=PRF&sigla_sistema=SEI)

### Módulo de ações judiciais, ação judicial

[https://www.servidor.gov.br/gestao-de-pessoas/sigepe/modulo-acao-judicial](https://www.servidor.gov.br/gestao-de-pessoas/sigepe/modulo-acao-judicial)

[Ação Judicial — Portal do Servidor](https://www.gov.br/servidor/pt-br/acesso-a-informacao/gestao-de-pessoas/sigepe/modulos-sigepe/modulo-acao-judicial/copy_of_modulo-acao-judicial)

# FÉRIAS

* 	  
   QUANDO UM SERVIDOR VEM DE OUTRA 	REGIONAL COM OCORRÊNCIA DE EXCLUSÃO DE FÉRIAS NO SIAPE: verificar 	se o servidor está com 2 matrículas siapecad.. você deve pedir 	unificação no alo segep. Para consultar as matrículas siapecad 	você vai em  **\>CACOPCA.**  
   	  
* Conferir se a vacância do outro 	órgão foi feita corretamente.  
   	  
* ''PARCELA COM PERDA DE DIREITO 	INFORMADO''-

QUALQUER UNIFICAÇÃO DE MATRÍCULA VOCÊ DEVE FAZER ALÔ SEGEPE… SOMENTE TEM 2 EXCEÇÕES: PROFESSOR SUBSTITUTO OU TEMPORÁRIO DO IBGE

	\- SERVIDOR VINDO DE OUTRO ÓRGÃO com ''PARCELA COM PERDA DE DIREITO INFORMADO''

	Informar férias CAIFFERIAS \-\> INFORMA FÉRIAS DO SERVIDOR

	Depois de informada é possível recuperar o direito de férias CAREPERFER \-\> RECUPERA DIREITO DE FÉRIAS e disponibilizar o servidor para alterações ou marcação de férias.

# RECADASTRAMENTO DE APOSENTADO / restabelecimento de pagamento de pensão

* siapenet  
   	  
* órgão/upag  
   	unificação  
* recadastramento  
   	  
* realizar recadastramento/preencher cadastro  
   	  
* imprimir 2 vias: 1 o servidor 	assina e a outra coloca na pasta funcional  
   	  
* caso tenha algum problema, ligar 	para o Planejamento: (cleber – 61 2020-1491)

* 	Quando o pagamento é suspenso, 	você deve criar um processo de suspensão, depois criar portaria de restabelecimento de pagamento. Só depois você pode reestabelecer 	o pagamento no siapenet, e deve também realizar os acertos financeiros (lançar os atrasados). Na hora de restabelecer o pagamento no siapenet, você deve colocar o mês de aniversário do 	aposentado ou pensionista como base.  
   	  
* Qualquer dúvida, baixar o manual no siapenet – documentação e legislação

\*\*\*\*\*\*\*\*\*\*\*\*Caso o **pagamento** caia por erro no sistema, o pagamento pode ser feito excepcionalmente via Ordem bancária, conforme disposto no parágrafo 2° do art. 2 da portaria nº110/2014-SEGEP – instruir processo com requerimento do servidor, comprovação de erro material ou sistemico, planilha de cálculo do contracheque devido (incluindo PSS,IR e Pas ) e despacho para DIPAG.

# INCLUSAO DE DEPENDENTE

\>CDIADEPEND

\>CAIASERVID – alterar número de dependentes\! Sempre\!

# HOMOLOGAÇÃO DE FOLHA

* 	  
   Pequena monta: \>fpatpeqmse

# CADASTRAR PENSAO JUDICIAL

* CDINPSBENE (inclui beneficiário)  
   	  
* FPATPSCOTA (cota para beneficiário)  
   	  
* FPSRPSPGTO (Atualizar pagamento)

# INCLUSÃO DE ESTAGIÁRIO \- SIGEPE

Pelo Sigepe:

1. Gestão de Pessoas  
2. Gestão de Vínculos.  
3. Estagiário  
4. Cadastrar Ingresso  
   1. Se não houver opção no campo Autorização de Contratação atualize a página. Caso não apareça será necessário o cadastro.  
   2. Cadastre em:  
      1. gestor \- UPAG \-   
      2. seleção de pessoas  
      3. controle de estágio \-   
      4. cadastrar autorização de estágio

Arquivos para anexo no sigepe não pode ser via download, apenas por impressão em pdf. O sigepe não aceita se for por download.

\> Menor de idade: começar inclusão pelo **\>CAEDHTITVG**

# Desligamento de Estagiário no Sigepe.

Sigepe \> Gestão de Vínculo \> Estagiário \> Consultar Vínculos \> Desligar

Realizar os cálculos pois o sistema não calcula sozinho.  
Verificar se existem dias de recesso não usufruídos que deverão ser indenizados.

Caso tenha recebido a mais, é necessário fazer uma GRU para os acertos.  
Acerto de GRU deve ser feito via folha suplementar.

ALTERAÇÃO DE FÉRIAS DE SERVIDOR QUE VEIO DE OUTRO ÓRGÃO PÚBLICO FEDERAL

\> Abrir processo de averbação

\---de emergência solicitar a portaria de nomeação e vacância no cargo ..

entrar no **\>caatdadsia** e alterar a data de entrada no serviço público

BUSCA DE ORIENTAÇÃO NORMATIVA – CONLEGIS

LANÇAMENTO DE CASSAÇÃO DE APOSENTADORIA

\>CAENEXCAPO

\>CAEEINTGRS

\>FPCLPAGTO – conferir	\>

\>CAALDTPCA – no campo observação lançar os dados: processo, portaria etc.

# EXTRAVIO / PERDA FUNCIONAL

\-Fazer requerimento próprio no SEI

\-servidor faz BO na Civil

\-servidor publica extravio em jornal de grande circulação

\-informar a Corregedoria Regional o fato

\-aguardar 20 dias até encaminhar o processo à DICAD

\-publicar no boletim regional – importante informar o numero do espelho (ver no processo) e numero e data do BO – PORTARIA..... ''O Senhor... Resolve: Tornar público o extravio da identidade funcional''

 

CERTIDÃO DE TEMPO DE CONTRIBUIÇÃO/ SERVIÇO

\-na parte de pss recolhido e pss atualizado, pegar ficha anula no SIAPE – função \>CACOCONPSS

SERVIDORES LOTADOS NO ORGAO POR PERÍODO

\>cacolotper

CERTIDÃO DE TEMPO DE SERVIÇO – SIAPE

\>CAEMCERPTS

CESSÃO DE SERVIDORES

Atenção ao pagamento da GDATPRF para os servidores administrativos.

Art. 19\. Os titulares dos cargos de provimento efetivo, integrantes do PECPRF, quando não se encontrarem em exercício no DPRF (cedidos ou requisitados), ressalvado o disposto em legislação específica, somente farão jus à respectiva gratificação de desempenho quando:

I \- requisitados pela Presidência ou Vice-Presidência da República ou nas hipóteses de requisição previstas em lei, situação na qual perceberão a gratificação de desempenho calculada com base nas regras aplicáveis como se estivessem em efetivo exercício no DPRF;

II \- cedidos para o órgão supervisor do Plano de Cargos a que pertence o servidor ou para entidades a ele vinculadas, situação na qual perceberá a respectiva gratificação de desempenho GDATPRF, calculada com base nas regras aplicáveis como se estivesse em efetivo exercício no DPRF;

III \- cedidos para órgão ou entidade do Poder Executivo Federal para exercício nas unidades gestoras dos sistemas estruturadores da administração pública federal, para a percepção da Gratificação Temporária das Unidades dos Sistemas Estruturadores da Administração Pública Federal \- GSISTE, receberão a GDATPRF a que fariam jus em virtude da titularidade de seu cargo efetivo, calculada como se estivessem em exercício no DPRF, nos termos da legislação aplicável; e

IV \- cedidos para órgãos ou entidades da União distintos dos indicados no inciso I e investidos em cargo de Natureza Especial, de provimento em comissão do Grupo-Direção e Assessoramento Superiores \- DAS, níveis 6, 5, 4 ou equivalentes, perceberão a gratificação de desempenho calculada com base no resultado da avaliação institucional do DPRF no período.

Parágrafo único. Os servidores ocupantes de cargos em comissão ou função de confiança, que se encontrem na situação prevista nos incisos I, II e III do caput, serão avaliados na dimensão individual somente pela chefia imediata.

Ao sair para a Cessão, os pagamentos das GDATPRFs não são devidos, e ao regressar retomar os pagamentos destas.

\- Salvar processo em bloco interno

**\>CAINCESSAO** – CESSÃO DE SERVIDORES no SIAPE (codigo 38 (pagto pela PRF) verificar na portaria ou 262 quando ônus para órgão cessionário.

\- Alterar situação funcional no SRH

\- Passar dados para Fernanda (Planilha de Controle)

**Atenção:** os servidores cedidos/requisitados/movimentados deverão ser incluídos na lotação **\>RECDEX**

A lotação específica dos servidores cedidos/requisitados/movimentados estarão no campo localização de exercício do servidor (onde encontramos os órgãos em que os servidores estavam cedidos).

\- **\>CAALORGCE** (ALTERA ORGAO CESSAO \- Se for preciso alterar o tipo de afastamento/cessão.

\- **\>CARRSERCED** – RETORNO DO SERVIDOR CEDIDO

\- CAEEINTGRS \- integra servidor

\- FPCLPAGTO \- roda folha

\- \>CACONLOTAC \- imprime exercício e insere no processo para comprovar o retorno do servidor

\- Encaminha à SGP responsável para conhecimento

\- Atualiza anotações do bloco com a data de retorno

\- Alterar situação funcional no SRH

\- Passar data de retorno para Fernanda (Planilha de Controle)

S

\>RETIRAR CESSAO – PORTARIA SEM EFEITO

\- \>CADTMATFP

\- \>CAEXLOCEXE

\- \>CARTMATFP

\-\>CACOSERVEE \- retorna servidores cedidos

\- Salvar processo em bloco interno

**\>CAINREQUIS** – REQUISIÇÃO DE SERVIDORES no SIAPE 

\- Alterar situação funcional no SRH

\- Passar dados para Fernanda (Planilha de Controle)

\- **\>CARRSERREQ** – RETORNO DO SERVIDOR REQUISITADO

\- CAEEINTGRS \- integra servidor

\- FPCLPAGTO \- roda folha

\- \>CACONLOTAC \- imprime exercício e insere no processo para comprovar o retorno do servidor

\- Encaminha à SGP responsável para conhecimento

\- Atualiza anotações do bloco com a data de retorno

\- Alterar situação funcional no SRH

\- Passar data de retorno para Fernanda (Planilha de Controle)

MODELO CARTA ENVIAR APOSENTADOS / CARTA DE NOTIFICAÇÃO

SIAPENET \> ORGÃO/UPAG \> ATUALIZAÇÃO CADASTRAL DE APOSENTADO E PENSIONISTA \> MANTER CARTAS DE NOTIFICAÇÃO

Selecionar o mês do lote a notificar

selecione os servidores que não atualizaram, (selecionar e gerar PDF padrão de Notificação)

CONSULTA DE LANÇAMENTOS POR MATRÍCULA /

\>ADCOLOG

RETIRAR FUNÇÃO DE SUBSTITUTO NO PERIODO DE FÉRIAS DO CHEFE TITULAR // RETIRAR FUNÇÃO DEPOIS QUE O SERVIDOR FOI REMOVIDO

PARA CRÍTICA SIAPE: (4912) NAO PERMITIDO. EXISTE EXERC.DE PFU C/INICIO APOS ESTA DATA

O problema é que o SIAPE agora lança automaticamente o provimento futuro para o substituto nas férias do titular. Consultando o CACODETPFU (DETALHE DE PROV.FUNCAO/CC/CNE) ver-se-á lançado o período de 16/11/2017 a 25/11/2017, que impede o lançamento da vacância. Dessa feita, são necessárias as seguintes transações:

\- \>CADTMATFP \- DESATIVAR MATRÍCULA

\- \>CAEXEXRCER \- EXCLUIR O EXERCÍCIO FUTURO ENTRE 16/11/2017 A 25/11/2017.(todos OS FUTUROS que estiverem aparecendo na transação)

\- \>CARTMATFP \- REATIVAR MATRÍCULA

\- PROCEDER COM AS TRANSAÇÕES HABITUAIS PARA EXONERAÇÃO DA FUNÇÃO. (\>CAVADIRFEX)

\>FPATPSCALC

\- calculo de beneficiário de pensão

UNIFICAÇÃO DE MATRICULA

\- NÃO UNIFICAR MATRÍCULA DE: contrato temporário IBGE (cacopca)/ professor substituto IBGE--- se o servidor teve contrato temporário como professor substituto ou temporário do IBGE

\-Você pode unificar a matrícula do restante para evitar problemas \- \>caeeintgrs // \>CACOPCA // \>

ALTERAÇÃO DE CARGA HORÁRIA E MUDANÇA DE REGIME

\-

# LANÇAMENTO DE AVERBAÇÃO DE TEMPO DE SERVIÇO

\>CAINTAS

| 			 \- 		 | 			 LOCAL OU ÓRGÃO PRESTOU O SERVIÇO 		 | 			 NATUREZA 			JURÍDICA 		 | 			 REGIME JURÍDICO 		 | 			 ATIVIDADE 			EXTERNA 		 |
| ----- | ----- | ----- | ----- | ----- |
| 			 1 		 | 			 Iniciativa Privada 			(Celetista- CLT) 		 | 			 12 		 | 			 01 		 | 			 001 		 |
| 			 2 		 | 			 AUTÔNOMO 		 | 			 02 		 | 			 01 		 | 			 158 		 |
| 			 3 		 | 			 Servidores da **Administração Pública Federal em geral** 			(inclusive da Justiça Federal e do TJDF) 		 | 			 01 		 | 			 02 		 | 			 **018** 		 |
| 			 4 		 | 			 Professor 			estatutário 		 | 			 10 		 | 			 03 		 | 			 006 		 |
| 			 5 		 | 			 Professor 			celetista 		 | 			 12 		 | 			 01 		 | 			 001 		 |
| 			 6 		 | 			 Prefeituras 		 | 			 07 		 | 			 03 		 | 			 006 			(048 se for professor ensino fundamental e médio) 		 |
| 			 **7** 		 | 			 **Políciais 			Militares e Civis Estaduais (atenção é tempo policial 			e não apenas militar)** 		 | 			 10 		 | 			 03 		 | 			 **157** 		 |
| 			 8 		 | 			 Bombeiros MILITAR 		 | 			 10 		 | 			 03 		 | 			 157 		 |
| 			 9 		 | 			 Bombeiros **NÃO** 			MILITAR 		 | 			 Lançar como tempo estadual 		 | 			 Lançar como tempo estadual 		 | 			 Lançar como tempo estadual 		 |
| 			 10 		 | 			 Ex-militares, inclusive do Exército: é usado para os servidores militares federais concursados que vieram para o DPRF 			 É o caso dos **oficiais e sargentos de carreira** (considera o período aquisitivo para férias) 		 | 			 **01** 		 | 			 04 		 | 			 002 		 |
| 			 11 		 | 			 FORÇAS ARMADAS( inclusive Exército) 			 (Serviço militar **obrigatório** dos soldados, cabos e sargentos **temporários**) 		 | 			 **18** (FORÇAS ARMADAS) 		 | 			 04 		 | 			 002 		 |
| 			 12 		 | 			 Tiro de Guerra 			 (Serviço militar **obrigatório** dos chamados atiradores) 		 | 			 **18** ( 			FORÇAS ARMADAS) 		 | 			 04 		 | 			 002 		 |
| 			 13 		 | 			 IBGE 		 | 			 04 		 | 			 21 		 | 			 063 		 |
| 			 14 		 | 			 Sociedade de Economia mista 		 | 			 06 		 | 			 01 		 | 			 071 		 |
| 			 15 		 | 			 Curso Formação PRF turma 94 (em regra, só poderia averbar de quem tem ação judicial com decisão favorável, ou então apenas para progressão) 			 			 			 Atenção: 	lançar os dias de curso apenas na linha de **progressão**, 			nas **outras** linhas lance 000 (como o exemplo) abaixo: 			 			 			 				 DENOMINACAO 				…..QUANT. DIAS 				 APOSENTADORIA.... 				000 				 LPA.............................. 				000 				 				 ANUENIO 				…...............000 				 				 PROGRESSAO............**040** 				 				 			 		 | 			 01 		 | 			 02 		 | 			 018 		 |
| 			 16 		 | 			 ALUNO APRENDIZ \- 			**estatutário** 			 			 		 | 			 12 		 | 			 01 		 | 			 001 		 |
| 			 17 		 | 			 ALUNO APRENDIZ Celetista 			(certidão do INSS) 		 | 			 12 		 | 			 01 		 | 			 001 		 |
| 			 18 		 | 			 SERVICO PUBLICO ESTADUAL 		 | 			 10 		 | 			 03 		 | 			 006 		 |

* 	  
   	 	

PASSO A PASSO:

* 	  
   Abre-se processo com certidões (cópias autenticadas, originais só no 	processo de aposentadoria)  
   	  
* análise NUCAP;  
   	  
* confecção portaria (número fornecido pelo gabinete);  
   	  
* enviar 	arquivo digital para NUAT (apoio técnico) para publicação.  
   	  
* Enviar 	02 vias portarias para superintendência assinar (uma no corpo do 	processo e outra contra capa);  
   	  
* após assinatura, lançar no sistema (abaixo descrito);  
   	  
* encaminhar ao servidor retirada portaria em anexo (contracapa);  
   	  
* Arquivamento.

SIAPE,SIAPECAD,TEMPOS,**TAS,CAINTAS** (OU F2 “\>CAINTAS”)

Lançar a data de início depois a de fim. No formato padrão “08MAR2007”

Selecionar órgão ou empresa com F1 caso não encontre digitar nome. (ou um ou outro)

Tipo Líquida ou Bruta (liquida usuário digita o tempo bruta o sistema calcula)

Verificar no final se confere os dias para que devem ser averbados (aposentadoria, anuenios...)

Obs.: lancei dados que identifiquem o documento.

Natureza Jurídica, Regime jurídico, Atividade Externa (usar F1)

(Caso seja necessário mude a data do **1o. Emprego**, quando o siape der crítica data lançada anterior ao primeiro emprego, conforme já consta no siape , basta ir na função **\>CAALDOCUME** e mudar a data para o 1º dia do período mais antigo de tempo a ser lançado.)

1. Incluir 	detalhes de acordo com a certidão(consultar F1)

ano=365 dias

mês=30 dias

	

PARA ALTERAR DADOS PESSOAIS, como **DATA DO 1º EMPREGO**: \>CAALDOCUME

Observar no processo : tempo **estadual** – a contagem de tempo tem quaverbe ser emitida pela **SEPLAG**

tempo **paralelo/concomitante** – mesmo tempo dois lugares: tirar o tempo de um dos lugares até não ser paralelo mais. Ex: 21 jan 2001 a 30dez de 2001 – SEPLAG(Secretaria de planejamento e Gestão) e 01 jan 2000 a 20mar2001 jota brinquedos. Deixar o tempo todo da SEPLAG e diminuir para 01jan2000 a 20jan2001 o da Jota brinquedos, ou vice versa. Se o tempo público for igual ao do privado, deixar o público e informar no proc

AVERBAÇÃO

\*\*\*\*só averba o que não for do executivo federal – se não for executivo federal você vai

EXCEÇÃO \- CERTIDÃO DO INSS- *AVERBAR “DATA INÍCIO E DATA FIM”* . E NÃO DIAS

EXCEÇÃO- EXÉRCITO – CERTIDÃO CPOR/TIRO DE GUERRA- AVERBAR *“TIPO DE AVERBAÇÃO LÍQUIDA”*

EXCEÇÃO- CERTIDAO DO ESTADO INFORMANDO FALTAS/ LICENÇA PARA TRATAR DE ASSUNTO PARTICULAR – COLOCAR *“TIPO DE AVERBAÇÃO \- LÍQUIDA”*

REGRA: TIPO DE AVERBAÇÃO BRUTA

EM OBSERVAÇÕES – COLOCAR PROCESSO E NÚMERO DE DOC SEI

\-NÃO ESQUECER DE ALTERAR A DATA DO PRIMEIRO EMPREGO- **\>CAINTAS**

**\>CAALDOCUME –** VAI DIRETO PRA PAGINA DO CAINTAS

LPA \- até 1996 averba

ANUÊNIO- até 1998\.

Para consultar \- **\>TBCOINCNAT**

**Para alterar a averbação por decisão judicial, fator 1.4 – para aposentadoria**

OBS: atividades insalubres e periculosidade, por mandado de injunção ou quando vem do inss com fator 1.4- quando o servidor vai se aposentar pelas regras gerais – **mulher é 1.2 e homem 1.4**

\>**tbcoincnat** – se você não achar a incidência dos 3 parâmetros do \>caintas, você pode consultar no \>tbcoincnat (incidências do tipo de atividade externa) // incidência por natureza jurídica(para ver todas as opções, você pode apertar ENTER até achar a melhor opção

**\>caaltas** – alteração de algum período de averbação

**\>caintas –** incluir o período que terá o fator 1.4

- natureza: 12  
- regime juridico \- 01  
- atividade 065- decisão judicial- conversão 1.4

\>**cacotas** – estilo de consulta genérica. Quando você olhar o mapa de serviço do servidor, a quantidade de dias averbados será multiplicado… **ex**: se ele tiver averbado 2 anos no fator 1.4, ele terá o total de 730 dias(365 x 2 \= 730 dias), mas no sistema vai constar 1.022 dias.

Aposentadoria do prf já tem fator 1.4…. se ele quiser se aposentar pela emenda 22, 40… não tem direito a aposentadoria do policial

**lei complementar 51/85** – alteração da aposentadoria compulsória aos 75 anos

\>tbcofundle – vê o fundamento legal de aposentadoria

**Lançamento no PCA – Averbação de serviço publico federal executivo siape**

	 → pca histórico – averbação antes da criação do siapecad

\-antes de 88 era contrato de trabalho (DNER)

averba no pca do ingresso até a 8112, e depois averba posterior

\>sipaecad \>pca \>

→ a saida e entrada nos pcas devem ser iguais. por exemplo, se ele saiu por transformação de cargo, ele deve entrar por transformação de cargo.

\>tbcoestcar-

**\>PCAHIST \>CAINPCAHIS** – pca histórico (quando é serviço público antes de 88, pois era contrato de trabalho) lei 8112 é de 12/12/1990, então os pcas históricos encerram em 11/12/90 (“órgão de destino” fica em branco se você for averbar o restante do tempo no pca normal// “forma de entrada” **501**\- admissao sem concurso público // “forma de saida” – **534**\- tranformacçao / “dl de vacância” – lei 8112 // nivel MEDIO – ANTES DA 8112).. depois você continua no pca normal.(entrada no pca normal- seria por 534- transformação no cargo // forma de saida- **611** \- vacancia, posse em outro cargo inacumulado// órgão de destino – não deve ser informado por essa forma de entrada // NIVEL)

OBS: normalmente quando dá problema no pca histórico, você tem que consultar o pca, imprimir, excluir o pca e incluir de novo.

**ABONO DE PERMANÊNCIA**

**LANÇAMENTO**

observações: no processo precisa juntar as telas da função \>CAEMTRQAPO que emite o mapa de tempo de serviço para aposentadoria e simulação do contagem de tempo para fins de abono que está na pasta NUAP em :\\\\172.17.4.6\\nuap\\ABONO DE PERMANÊNCIA\\2013\\planilhas de contagem de tempo abono modelo CGRH

**NÃO ESQUEÇER DE FAZER A INTEGRAÇÃO\!\!\!\!**

1\. Acessar o SIAPE em **\>CDISPSSABP**

2\. conforme tela abaixo, onde deverá digitar a matrícula do servidor beneficiado pelo abono de permanência:

3.clique **S** ou **N** para o caso do servidor ter contado OU não a LPA em dobro.

4.Na tela seguinte faça como demonstrado abaixo

GRUPO/OCORRENCIA: ***16*** / clique F1 aqui e escolha a opção **codigo** e digite **006** (mais usado inclusive para quem tem **tempo PM**) **007** ou **008** conforme o fundamento

\++++++++++++++++++++++++++++++++++++++++++++++++++

GRUPO/OCORRENCIA : **16 / \_\_\_**

INICIO OCORRENCIA : data que a portaria concedeu (Conforme planilha )

TERMINO OCORRENCIA : deixar em branco

FUNDAMENTO LEGAL: **17001**(exemplo para quem tem tempo de polícia, PM civil etc(cuidado não apague esta linha\!\! se esta linha estiver apagada tem que voltar e refazer

5\. Faça a integração da matrícula função **\>CAEEINTGRS**

6\. Copie as telas da função **\>FPCLPAGTO**, imprima e junte ao processo

7\. Calcule os dias que faltarem desde a data do lançamento (que iniciou o pagamento) do abono até o último dia do mês anterior, já que **o sistema só paga automaticamente a partir do mês do pagamento que estiver sendo atuado**. Pague na função \>FPPATMOVFIN os meses anteriores usando o código **82273** ; imprima e junte ao processo. Se tiver valores de anos anteriores pode ser necessário abrir processo de exercícios anteriores.

**Observações**: este lançamento costuma dar sempre problema porque qualquer diferença nos lançamentos de tempo de serviço, **faltas** etc. interfere nesta função e dá a mensagem que o servidor não teria tempo ainda para a concessão. Nestes casos precisa, ANTES de tentar lançar novamente, descobrir o que impede o lançamento, CORRIGIR a inconsistência encontrada e só então lançar o abono.

Em cumprimento à Nota Informativa nº 412/2013/CGNOR/DENOP/SEGEP/MP,datada de 20/09/2013, informamos que foi disponibilizado no SIAPE o Grupo/Ocorrência **16/009** para a concessão do abono de permanência com base nos artigos 6º da Emenda Constitucional nº 41/2003 e 3º da Emenda Constitucional 47/2005.

**observação: se apenas cadastrar no siape na função \>griaproadm (exercícios anteriores) usar o OBJETO DE PAGAMENTO: 099**

**ABONO DE PERMANÊNCIA**

**EMISSÃO DAS PÁGINAS DO PROCESSO**

No Siape use as funcões \>CDCOINDFUN; (emite o Documento comprobatório da d**ata de admissão** do requerente)

\>CASIAPOSEN (emite o Documento **comprobatório da idade** do requerente)

e \>CAEMTRQAPO (emite o Mapa de contagem de tempo de serviço e/ou de contribuição para aposentadoria.

Depois basta copiar as telas imprimir e juntar aos autos.

SERVIDOR COM DUAS MATRICULAS SIAPECAD ATIVAS

\* PARA A MATRÍCULA XXXXXXX

\>CADTMATFP (Desativa matrícula)

\>CACANPCA (cancela PCA por erro)

\>CARTMATFP (reativa matrícula)

\>CAEEINTGRS (executa integração)

\* Efetuar o calculo da folha (\>FPCLPAGTO)

Em princípio, isso vai resolver. Se não rodar a folha, e der a mesma mensagem "VAGA NÃO RESERVADA PARA O SERVIDOR", na matrícula 2077242, fazer o \>CAALVAGA.

Concessão de Aposentadoria – ERRO NO FUNDAMENTO LEGAL \- atualização do Fundamento Legal de Aposentadoria do servidor \- Licença em duplicidade

\-Excluir o lançamento da LPA indevida do \>CACOTAS;

\- Fazer a correção dos proventos no \>CACRPROVAP;

\- Fazer a atualização da aposentadoria no \>CDATAPOSEN (Verificar o fundamento legal do servidor conforme Tabela de Fundamentos Legais. \>TBCOFUNDLE)

Corrigir o fundamento na transação \>CAALPROVEN. (No item ''Utiliza contagem da LPA em dobro", marcar ''S'')

Ou seja, após a exclusão da Licença em duplicidade, é necessário cadastrar a contagem em dobro no \>CAALPROVEN.

\- isenção de imposto de renda: \>CDISIMPREN

para isenção de imposto e de pss por doença especificada em lei e decisão judicial usar código 006x. Só isenção de IR usar código 005\.

**FUNDAMENTO LEGAL DESATIVADO**   : 500001 VOLUNTARIA (ART. 186 ITEM III ALINEA A): O que fazer?

 \--- DADOS DO FUNDAMENTO LEGAL \------------------------------------------------  
 FUNDAMENTO LEGAL   : 500001 VOLUNTARIA (ART. 186 ITEM III ALINEA A)             
 TIPO APOSENTAD.    : VOLUNTARIA                                                 
 TIPO DE CALCULO    : C-CARGO DO SERVIDOR                                        
 PROPORCAO APOS.    : 100%                                                     

Transação \>CDATAPOSEN

OCORRENCIA DE APOSENTADORIA   

  GRUPO/OCORRENCIA   : 17 / 001 LC 51 1º I  (voluntariamente, com proveitos integrais, após 30 (trinta) anos de serviço, desde que conte, pelo menos 20 (vinte) anos de exercício em cargo de natureza estritamente policial)

\>CAEEINTGRS para verificar se a pendência foi sanada.

Rodar o cálculo após a alteração no cdataposen.

# CONSULTAS SIAPE

## VAGAS DE CARGO

DISTRIBUIÇÃO DE VAGA DE CARGO

\>ADCOVAGA   \-\> CONSULTA DADOS DA VAGA (copiar toda a tela e colar num bloco de notas pq vai precisar repetir esses dados )

\>ADEXVAGDIS \-\> EXCLUI VAGAS DISTRIB. P/ UORG (vai excluir a UORG atual da vaga) \- Opção “Vaga Informada”

\>ADDIVAGAPR \-\> DISTRIBUI VAGAS APROV. P/ UORG (vai distribuir pra a UORG desejada) \- Opção “Vaga Informada”

Por fim, pode consultar o ADCOVADA de novo para confirmar se o código de vaga realmente foi vinculado a UORG correta.

CACOAPOSSE ( CONSULTA APOSENTADORIA)

SOLICITAÇÃO DE CÓDIGO DE VAGA PARA SERVIDOR REVERTIDO/REINTEGRADP/ETC

1- verificar vaga anterior do servidor- \>CDCOINFUN (pesquisar data anterior à saida do servidor para aparecer a vaga ocupada)

2- verificar se a vaga está ocupada no \>ADCOVAGA

3- se estiver ocupada, disponibilizar vaga PRF 3-1 e solicitar que a regional faça o reenquadramento das progressões do servidora

PROVIMENTO DE CARGO COM VAGA EM OUTRA UORG // POSSE EM OUTRA UORG– (vaga disponibilizada em outra UPAG, posse por engano)

1- desativar matrícula no \>CADTMATFP

2- cancelar o PCA (quando não for servidor de outro órgão SIAPE antes da PRF) \>CACANPCA

3- excluir siapecad no \>CAEXMATRIC

4- criar outra siapecad no \>CAINMATRIC

–\-------------------verificar provimento de cargo// posse servidor em outra uorg / upag quando ele foi de outro órgão SIAPE

CÓDIGO DE VAGA PARA SERVIDOR REVERTIDO/REINTEGRADO/ETC

Quando um servidor voltar ao serviço público e a regional solicitar código de vaga, primeiro verificar a vaga ocupada anteriormente por ele:

1- **\>adcovaga** (colocara data retroativa no \>cdcoindfun e pesquisar a vaga que o servidor ocupava)

PROCEDIMENTO CORRETO: Caso a vaga esteja ocupada, disponibilizar vaga na classe/padrão **3I**. A regional faz o procedimento de inclusão do servidor como se ele fosse **3I** e depois efetua o reenquadramento no **\>CAALPROGMA** (coloca o servidor na classe padrão que ocupava anteriormente, na mesma data que entrou… ex: a portaria de reversão saiu 02/06/2017.. você dá provimento pro servidor no 3I em 02/06/2017. Após isso, você reenquadra no \>cainprogma como SI em 02/06/2017).

PROCEDIMENTO COM ERRO: Caso a regional der provimento para o servidor na classe/padrão que ocupava anteriormente, ocasionará erro nos dados de ingresso no serviço público e a transação **\>caatdadsia** fica bloqueada (erro siape: **“EH NECESSÁRIO SOLICITAR AUTORIZAÇÃO PARA ALTERAR OS DADOS DE INGRESSO NO SERVIÇO PÚBLICO DESSE SERVIDOR E/OU OS DADOS DE INGRESSO NO CARGO ATUAL)**

Logo, é necessário solicitar autorização para a transação **\>CDAUSPUBL**. Para ser habilitado, o servidor do RH não pode ter habilitação do **TROCAHAB.**

Depois de autorizado, é possível alterar a data de ingresso no serviço público do servidor reintegrado, na transação **\>CAATDADSIA**. (**OBS:** ALTERAÇÃO NA TRANSAÇÃO \>CAATDADSIA **\-** observar que a data do ingresso no órgão, caso o servidor tenha tomado posse antes de 2004, ficará como 01AGO2004, por causa da reforma administrativa. Ou seja, devemos alterar somente o ingresso no serviço público, conforme termo de posse do servidor)

Após alterar, ocorrerá erro no código de vaga, pois a vaga seria para um servidor 3I e não SI por exemplo.

Logo, é necessário fazer o reenquadramento do servidor no **\>CAALPROGMA**. Colocar o servidor no **3I** novamente, na data de publicação da portaria de reversão, por exemplo.

Após, efetuar a transação **\>caalvaga** e copiar o mesmo código de vaga.

Logo depois, colocá-lo na classe padrão que ocupava anteriormente, SI por exemplo, na transação **\>CAALPROGMA.**

Quando pesquisar no \>cacopospro, você verá 3 situações do servidor.. para apagar os que foram feitos com erro, utilizar a transação **\>CAEXPOSIC**

CONSULTA DE VAGAS DISPONÍVEIS – CARGO ADM E PRF – vaga

\>GRCOQUAVAG

origem-

grupo- 911(prf) ou 437(adm)

cargo – 001 “ ou 014 “

situação – 2

## TRANSAÇÕES SIAPE 

### Nomeação tornada sem efeito

1\. Desativar matrícula (CADTMATFP)

2\. Cancelar a nomeação (CAEXNOMEAC)

3\. Reativar a matrícula (CARTMATFP)

Se necessário, realizar a integração após esse procedimento

### ALTERAÇÃO DA DATA DE INGRESSO NO SERVIÇO PÚBLICO

Apenas para cargos da 8112 ou por decisão judicial.

Solicitar habilitação na transação **\>CDAUSPUBL**.

 Para ser habilitado, o servidor do RH não pode ter habilitação do **TROCAHAB.**

Depois de autorizado, é possível alterar a data de ingresso no serviço público do servidor reintegrado, na transação **\>CAATDADSIA**. (**OBS:** ALTERAÇÃO NA TRANSAÇÃO \>CAATDADSIA **\-** observar que a data do ingresso no órgão, caso o servidor tenha tomado posse antes de 2004, ficará como 01AGO2004, por causa da reforma administrativa. Ou seja, devemos alterar somente o ingresso no serviço público, conforme termo de posse do servidor)

### ALTERAÇÃO DA DATA DE POSSE SERVIDOR

\>CAALDTPCA

SERVIDOR COM ENTRADA JUDICIAL / POSSE SERVIDOR JUDICIAL / SUB JUDICE

\- Após o trânsito em julgado e publicação de Portaria, é necessário apenas arquivar a mesma na pasta funcional do servidor. (A portaria é feita pela DIPEC)

\- aguardar homologação de estágio probatório, pois o Sistema SIAPE não altera a condição dele para estável automaticamente.

\- Após a homologação do estágio, utilizar a transação \>CAATDADSIA e alterar de **01165** para **01166\.**

\-Logo, o sistema muda a forma de entrada de DECISÃO JUDICIAL para ESTABILIDADE DECLARADA.

CONSULTA PENDÊNCIA/ E

RRO

\>CACOPENDAT

VER HISTÓRICO COMPLETO DE SERVIDOR – DOSSIE

\>CAEMDOSSIE

VERIFICAR MATRÍCULAS ATIVAS DO SERVIDOR – SIAPECAD \-

\>CACOPCA

VERIFICAR PENDENCIA SERVIDOR – DADOS ERRADOS

\>CACOPENDAT

TIPO DE ATUALIZAÇÃO A SER EFETUADA: ATUALIZAÇÃO GERAL DA MATRÍCULA

REJEITADO POR: NÃO PERMITIDA UTILIZAÇÃO DA OCORRÊNCIA DE EXCLUSÃO 02/227

Servidor falecido lançado pelo batimento do cartório no SIAPE

Nesta sequencia:

CADTMATFP

CACAENCAPO (se aposentado) ou CACANVAC (se ativo).

CACAOBITRH...

Depois:w

CARTMATFP

CAENEXCAPO (aposentado) ou CAVAEXCEP (ATIVO)

CAIFOBITRH

### PROCEDIMENTO DE REGULARIZAÇÃO DE LANÇAMENTO ERRADO DE REVERSÃO (SERVIDOR COM MAIS DE 1 MATRÍCULA SIAPECAD)

1- CACOPCA (para consultar, CDCOINDFUN – por nome /// CARTMATFP – mostra todas as matrículas )

2 – CADTMTFP – desativa matricula

3 – CACANPCA – cancela os pca’s que estão sobrando

4 – CAEXMATRIC \- exclui matrículas

5 – CDCOINDFUN – consultar no mês que o servidor foi aposentado – ex: set2014.. e pegar numero de vaga)

6 – ADCOVAGA – verificar se a vaga está desocupada – classe padrão e uorg // reversão 003 forma de entrada

7 – PEATPROVEX \- “MATRICULA DESATIVADA PARA INTEGRAÇÃO’’

8 – CARTMATFP reativa matricula na folha de pagamento

SE CONTINUAR DANDO ERRO DE MATRÍCULA DESATIVADA PARA INTEGRAÇÃO, abrir alô-segep e enviar o CAALVAGA

AGUARDAR RESPOSTA ALÔ SEGEP

SERVIDOR DEMITIDO POSSE IRREGULAR –. APÓS DECISÃO JUDICIAL, TORNAR PORTARIA DE DEMISSÃO SEM EFEITO – RETORNO DE SERVIDOR

### AJUSTE DE PSS E CONTRIBUIÇÃO

***"O sistema não apura o valor do PSS quando a remuneração contributiva é lançada manualmente**, portanto não há erro. **O Siape só apura o PSS quando a remuneração é carregada automaticamente pelo sistema**. O importante é constar na base o valor da remuneração considerada e a reajustada. Orienta-se que, após lançar/corrigir valores no CAATCONPSS deve acessar o CACOCONPSS, informar o ano em que foi efetuada a alteração, pressionar a tecla Enter e depois F8, para avançar a página, e visualizar os valores informados, para conferência. Cabe registrar que a planilha do CAEMTIPENS é calcula com base nas remunerações reajustadas e não no PSS apurado."*

# AVERBAÇÃO DE TEMPO DE SERVIÇO

Para incluir a contribuição, utilize a transação CAATCONPSS.

É preciso incluir os meses zerados. Para isso, selecione apenas os meses zerados e confirme.

# REQUISITADO \- SERVIDOR CEDIDO DE OUTRO ÓRGÃO

ALTERAÇÃO DE LOTAÇÃO (localização do servidor)

CDALFUNC \- Não informe a lotação nem a data, apenas a localização.  
CDALFUNC   \-\> ALT DADOS FUNC \- CARGO/FUNCAO

Remoção de servidor requisitado.

CONSULTA VÍNCULO DE SERVIDOR \-

\>CDCONVINC

EXERCÍCIO PROVISÓRIO/ CEDIDO PARA A PRF

\>CDINREGIST (Solicita dados bancários, dados funcionais do servidor, é preciso inseri-los) Feito no e-Siape.

\>CDIADADOS ( INCL SERVIDOR \- ALTERA DADOS \- Se necessário alterar a situação funcional por crítica do sistema. Movimentação para Compor Força de Trabalho \- Est 44; est 19; est 03\.  
Ocorrência de ingresso: 0184  exerc ext parag 7 art 93 \- Lei 8112/90.

Caso seja necessário alterar a upag:

* SIAPE,CADSIAPE,CADASTRO,TRANSFER ( TRANSFERE SERVIDOR UPAG/ORGAO )  
* CDLIUPAG   \-\> LIBERA PARA MUDANCA DE UPAG  
* CDACTFUPAG \-\> ACEITA ENTRADA EM NOVA UPAG

\>CDCONVINC

\>FPCLPAGTO

Servidores movimentados para compor força de trabalho devem estar na situação funcional: 44 EXERC. 7 ART 93 8

\>CAATSITSIA \- SIAPE,SIAPECAD,INTEGRACAO,CAATSITSIA ( ATUAL.SITUACAO FUNCIONAL SIAPE )

SERVIDORES QUE VEM DE OUTRO ÓRGÃO FEDERAL PARA A PRF É EST3 – REQUISITADO NO SIAPE

SE VIER DE ÓRGÃO MUNICIPAL/ESTADUAL/DF SERIA EST14-REQ. DE OUTROS ÓRGÃOS- neste caso, a prf deve fazer o ressarcimento via movimentação financeira – SOFIP – todo mês para o órgão de origem do servidor… no caso de servidor federal não precisa.

PARA EXCLUIR VACÂNCIA DE CHEFE EM OUTRA LOTAÇÃO

\>cadtmatfp – DESATIVAR MATRICULA

\>caexlocexce – excluir exercício

\>CAEXLOTERR-EXCLUIR LOTAÇÃO ERRADA

\>CACAVACPFU

\>cartmatfp – reativa matrícula

LANÇAR VACÂNCIA

AI O SERVIDOR ESTÁ COM A CHEFIA DE NOVO NA OUTRA REGIONAL

AI VC TIRA A CHEFIA (ler com sotaque carioca, p\*\*\*\*\!)

\>CAVADIRFEX

ATIVAR MATRICULA \- \>CARTMATFP

REMOVER NO \>CAROCOLHIS

# PENSÃO E APOSENTADORIA

Quando sair a portaria de pensao ou aposentadoria, é necessário esperar a próxima folha para lançar no SIAPE, uma vez que se efetuar o lançamento na mesma folha, o pagamento não é gerado.

mudancas no pca

1998 – criação do cargo

2001-

2004 \-

2006 – prf passa a receber por subsídio

autuação dos processos de APOSENTADORIAS e PENSÕES

PENSÃO: 1 \- No formulário de concessão de pensão EC 41/2003, o teto previdenciário do INSS hoje é de R$ 8.157,41.

2 \- A Certidão de Casamento deve ser atualizada (com a data posterior ao óbito do servidor(a)) e autenticada.

3 \- Assinalar o campo correto no requerimento de pensão referente ao grau de parentesco com o servidor(a) falecido(a).

4 \- No caso de companheira(o) com comprovação de união estável, apresentar nos autos no mínimo 3 provas documentais de acordo com a NOTA TÉCNICA Nº 23/2010/COGES/DENOP/SRH/MP. 5 \- No caso de ex-conjuge ou companheira(o) com percepção de pensão alimentícia, apresentar o documento que comprove receber a pensão alimentícia no mês anterior a data do óbito do servidor(a).

# APOSENTADORIA {#aposentadoria}

1\. Certidão disciplinar nacional (abrangendo todas as unidades da federação) atualizada.

2 \- Laudo Médico Pericial original assinado pela junta médica.

3 \- Certidões de Tempo de Serviço **original**.

4 \- Declaração assinada pelo servidor, no caso de aposentadoria por invalidez ou compulsória, informando se ele possui ou não débito com o erário e se acumula ou não outro cargo, emprego ou função, assim como se recebe proventos de aposentadoria, pensão ou reforma.

5 \- Autenticar o Histórico Funcional, assim como o Mapa de Tempo de Serviço.

6 \- Autenticar os documentos pessoais do servidor(a) e o comprovante de endereço.

7 \- Fechar o Mapa de Tempo de Serviço um dia antes da data de publicação da portaria de concessão da aposentadoria, quando o processo retornar para a regional.

Essas observações são de suma importância para que o benefício seja concedido com celeridade e posteriormente seja julgado pela legalidade pela CGU \- CONTROLADORIA GERAL DA UNIÃO e pelo TCU \- TRIBUNAL DE CONTAS DA UNIÃO.

**26\. APOSENTADORIA**

Art 1º , inciso I da lei complementar nº 51/85 , utilizar valor integral 186 III “B”.código **500260:** o mesmo de professor. (verificação permanente no site [www.in.gov.br](http://www.in.gov.br/), diário oficial) obs.: outras casos de aposentadoria deve ser analisado utilizando \<FI\>

1} Pagar Ad. Noturno mês anterior (seq 6\) , mês atual (seq 1).

2} Descontar vale transporte e/ou vale alimentação proporcional ao mês da aposentadoria e um integral .(as demais rubricas serão desativadas ao desligar parâmetros (FPATPARAM- item 4\)	

Cadastrar documento legal (interno) no módulo – acesso DPEDITADL – finalizar (item 7 e 8\)

3} Calcular **planilha** (Programas EXCEL/CALC) valores proporcionais ATIVO/APOSENTADO (pasta NAP ). Observar que as **rubricas mudam** para aposentado. **Imprimir Ficha Financeira** do mês anterior e também fazer **\>fpclpagto** (imprimir)

4} Desligar parâmetros **(\>FPATPARAM) imprimir antes de desligar** para retornar no mês seguinte com os mesmos parâmetros. ( **no próximo mês reativar os parametros novamente)**

5} Pagar valores proporcionais p/ativo (\>FPATMOVFIN) e descontar PSS ATIVO. Conforme planilha do item 4\.

6} **Editar DL (\>DPEDITADL)**

– Assunto 059

N° \= (numero portaria, etc.\<F1\>) uorg \= (250) ano \= 2008 tipo \= (Portaria \= 2)) \-DATA EMISSAO- data da publicação no DOU

\-VIGÊNCIA – data da publicação

\-PUBLICAÇÃO – data da publicação no DOU

7} **Finalizar DL (\>DPFINAL)** – texto finalização exemplificado abaixo – **não emitir DL**

“ O COORDENADOR-GERAL DE REC HUMANOS DO DPRF, SÉRGIO MAX BASTOS LINS, RESOLVE: CONCEDER APOSENTADORIA INTEGRAL AO SERVIDOR xxxxxxxxxxx, MAT.xxxxxxx, OCUPANTE DO CARGO DE PRF, COD NI-911001, CLASSE “x”, PADRAO “x”, DO QUADRO DE PESSOAL DO DPRF, LOTADO NA 4ª SRPRF/MG, COM FUNDAMENTO NO ART. 1º, INCISO I, DA LEI COMPLEMENTAR 51/85 DE ACORDO COM O PROCESSO Nº 08.656.005.051/2008-91.”

“A COORDENADORA-GERAL DE REC HUMANOS DO DPRF \- SUBSTITUTA, AMIRCE FERREIRA RODRIGUES DOS SANTOS, RESOLVE: CONCEDER APOSENTADORIA INTEGRAL AO SERVIDOR ALTAIR CARDOSO DA SILVA, MAT. 0163859, OCUPANTE DO CARGO DE PRF, COD NI-911001, CLASSE “I”, PADRAO “III”, DO QUADRO DE PESSOAL DO DPRF, LOTADO NA 4ª SRPRF/MG, COM FUNDAMENTO NO ART. 1º, INCISO II, DA LEI COMPLEMENTAR 51/85, CONSIDERANDO O DISPOSTO NO PROCESSO Nº 08.656.015.919/2008-61.”

8\) **LANÇAR A APOSENTADORIA, (LANÇAMENTO DE APOSENTADORIA):**

**ALERTA: Nunca lance a aposentadoria na mesma folha de publicação. Salvo se os efeitos forem a partir do dia 1º do mês.**

**\>CAAPSERVID.**

()

SE HOUVER ERRO DE LANÇAMENTO NOS DADOS DA APOSENTADORIA E NÃO FOR POSSÍVEL CORRIGIR, EM ÚLTIMO CASO, EXCLUIR APOSENTADORIA (\>CAEXAPOS) – ESSA OPERAÇÃO IRÁ GERAR UMA FALHA NO “PCA”, PARA SANÁ-LO DEVE-SE IR AO (\>CACANVAC) E EFETUAR O CANCELAMENTO DA VACÂNCIA DA APOSENTADORIA.

EM SEGUIDA, EFETUAR NOVAMENTE O LANÇAMENTO DA APOSENTADORIA CORRETAMENTE

Sentença judicial \= n ( se for, coloca s)

tabela de posicionamento \= 001

uorg de localização: 250

uorg exercício financeiro : 250

número do processo: se o processo não estiver aqui, procurar no protocolo da intranet \- enter

escrever o documento legal da aposentadoria – portaria, data e publicação

e na observação escrever o fundamento legal.

9\) Lançar através do **\>FPATMOVFIN** todos as **rubricas que o servidor tem direito**.

10\) Verificar períodos de férias a gozar e dar perda de direito.

FUNÇÃO PRF

EM 2017 mudou de FCPRF para FCPE

 \_\_ SIAPE,SIAPECAD,PCA,VACANCIA,CACANVAC ( CANCELA ULT.VACANCIA(POR ERRO) )\_\_\_\_ Cancela última vacância por erro em caso de alterar data de lançamento de demissão, por exemplo.

**27\. ANUÊNIO**

Todas as ocorrências de afastamento devem ser lançadas antes do cálculo do anuênio.

Observar os anuênios anteriores, no \>CACOANUENI e imprimir. Depois, após ter sido feito o tempo de serviço, se o tempo for para todos os fins, ou seja, tempo público federal, ir no SIAPECAD, INCGRATAD,CDANUENIO,CAACLSIND e fazer o cálculo.

Caso seja Instituidor de pensão a transação é a SIAPE,PENSAO,PSINSPEN,CDALPSINST ( ALTERA INSTITUIDOR DE PENSAO )

O anuênio foi cortado em **09mar1999.**

**28\. COMUNICA**

SIAPE/ COMUNICA/ ADMMSG/ CEIAMENSAG

Destinatário da msg: 1

Preencher somente assunto

Código dos órgãos/uorg: 30802 00000001(ou consultar lista “uorg departamento”)

**29\. Cadastrar agência bancaria**

Para incluir uma agência no siape deve fazer comunica como acima enviar ao departamento de cadastro. Deve constar endereço completo, o nome da agência , o código da agência e o banco.

Código dos órgãos/uorg: 30802 00000001(ou consultar lista“uorg departamento”)

**30\. CONSIDERAÇÕES GERAIS DA MATRÍCULA**

SIAPE, SIAPECAD, DADOSPESS, ALTSERV, **\>CAIACGMAT**

Tudo que fizer de diferente para o servidor, como algum pagamento ou desconto (exemplo reposição ao erário) fora do normal, deve ser anotado no considerações gerais.

**31\. ALTERAÇÃO DE DADOS BANCÁRIOS (conta para pagamento)**

Trocar banco, agência conta: SIAPE, SIAPECAD, DADOSPESS, ALTSERV, \>**CAATDADBCO**

Consultar Banco: SIAPE, TBSIAPE, TBGERAIS.

**\>TBCOAGEN se uma agência existe, antes de pedir cadastramento de nova agência bancária.**

Consultar dados bancários do servidor: \>CDCOINDFUN

Para cadastrar Conta Poupança do Banco do Brasil

A conta poupança é composta de 9 (nove) algarismos sendo o ultimo o digito verificador.

Caso seja informado um número de conta poupança basta verificar se este começa por 1 seguido de zeros, caso contrário acrescentar.

Exs:

56789-8 incluir “100” no inicio e somar 2 no (DV) digito verificador. Vira 10056789-X

1234-X Vira 10001234-1 veja ”1000” ao invés de “100” para completar os 9 algarismos com o DV.

A sequência de DVs é: 0,1,2,3,4,5,6,7,8,9,X

Ou seja para substituir: 0+2=2; 1+2=3; 2+2=4; 3+2=5; 4+2=6; 5+2=7; 6+2=8; 7+2=9; 8+2=X; 9+2=0; X+2=1;

**32\. EDITAR DOCUMENTO LEGAL**

**PROCDOCPUB** (DL, DOCLEGAL, DPEDITADL, )

Número (nº da portaria)

UORG – 250(4ª srprfmg)

Ano – ano da publicação da portaria

tipo – tipo do documento – (clique F1) para portaria nº 02 – enter

assunto : (conforme a questão)

emissão: data da assinatura

vigência: data da publicação ou retroagir conforme o caso.

Publicação: data da publicação. Enter e F3

Para alguns procedimentos é necessário **finalizar** o documento legal.( DPFINAL)

**33\. EXONERAÇÃO** VACÂNCIA POR EXONERAÇÃO A PEDIDO ou DE OFÍCIO

Se a portaria de exoneração ainda não foi publicada e o pagamento deve ser cortado:

CDATAFAST. Lançar código 187 com a data da vacância ou a data do dia do lançamento.

CACOOCORSE (verifica se servidor tem alguma ocorrência em aberto se tiver finalizar)

CACOPENDAT (verifica se servidor tem alguma pendência)

Tendo : Regularizar

Não tendo:

CAVAEXONER

informar opção referente a PROVIMENTO SEM PUBLICAÇÃO

selecionar a opção de exoneração

preencher o HISTORICO do DL

Para lançamento de exoneração no Siape, qual data deverá ser lançada, o dia de publicação ou o dia anterior?

A data correta para lançamento da exoneração no SIAPE deve ser o dia ANTERIOR à publicação da portaria. Conforme os procedimentos internos, ao lançar a vacância por exoneração, deve-se utilizar o código correspondente e informar a data como sendo um dia antes da publicação​. Isso garante que não haja rompimento abrupto do vínculo, especialmente em casos de posse em outro cargo público, assegurando que os direitos do servidor sejam preservados.

 

**34\. G.R.U.**

[**https://consulta.tesouro.fazenda.gov.br/gru/gru\_simples.asp**](https://consulta.tesouro.fazenda.gov.br/gru/gru_simples.asp)

UG \= 200230 Gestão \= 00001

Código de Recolhimento \= 68801-0

Número de Referência \= “Nº da Matrícula do Servidor”

Competência \= Mês do Débito

Vencimento \= Último dia do mês subsequente ao da geração da guia

**35\. ISENÇÃO DE IMPOSTO DE RENDA**

**\>CDISIMPREN** (esta função também “**consulta**” porque se a pessoa **já tem implementada**, mostra a data do início, fim etc)

\>CDATPSOCCA \- incluir isenção de IR para uma pensionista.

**36\. FALTA (129)**

Confirmar na folha ponto e no mapa de freqüências se houve falta não justificada (129).

Lançar ausência no \>CAINOCORSE com código 129\.

Observar que enquanto o servidor não ser apresentar no próximo dia útil à administração ele receberá falta (mesmo que ele não esteja escalado para trabalhar no dia).

Descontar do total de rendimentos a fração dos dias que faltou sobre 30 dias. (se faltou dois dias descontar 2/30 do total recebido inclusive auxilio alimentação, pré escolar, transporte etc).

\>fpatmovfin Rubrica 80001

Sequência 6; Prazo 001; informar mês da(s) falta(s); assunto de cálculo 27; fração de acordo com os dias (exemplo 02/30). Para servidores administrativos lançar valor informado

Descontar auxilio transporte e alimentação proporcional a 22 dias.

Fazer o cálculo para conferir os lançamentos.

Confirmar com o chefe da delegacia se a falta foi informada à corregedoria.

**FÉRIAS Programar, Reprogramar, cancelar, interromper**

**SIAPE, SIAPECAD, AUSÊNCIAS**.

Preencher requerimento assinatura do servidor, chefe imediato e chefe do RH

**1.Programar**: \>CAIFFERIAS

**2.Reprogramar**: \>CAPRFERIAS

Ler legislação.

OBS: DL 06, UORG 1100, ANO 2011, TIPO 04

**3.Consultar férias não marcadas:** (todo mês de **setembro** tem que fazer esta consulta) só pode marcar as férias do ano seguinte após marcar a do ano atual.

**4.cancelamento de férias. –** *QUANDO PASSA DE UM ANO PARA O OUTRO*

Pede-se que o chefe da delegacia/núcleo do servidor faça um memorando explicando os motivos do cancelamento das férias.

Com o nº do memo, que será o número do documento, edita-se um Documento Legal na função siape: **\>DPEDITADL** (assunto: **232**) \*UORG do DL (será a da delegacia)conforme tela abaixo:

Vá então na função **\>CACAFERIAS** para fazer a nova programação de férias, já lançando o a nova data para gozo que substituirá a cancelada. Por fim volta na função \>CACOFERIAS para ver se deu certo.

Ou então: já vai em **\>CACAFERIAS e cadastra o documento legal digitando F2 para abrir essa opção e depois F4 para incluir o documento legal**

**5.interromper férias: \>CAITFERIAS** Primeiro Pede-se que ao Superintendente emita um memorando pedindo para interromper

Com o nº do memo, que será o número do documento, edita-se um Documento Legal na função siape: \>DPEDITADL (assunto: 232\) \*UORG do DL (será o do Gabinete)

observação:

**para o caso de algum servidor que vier de outro órgão federal com saldo de férias para serem gozadas no DPRF:**

	Para que sejam lançadas as férias é necessário primeiro alterar a data de ingresso no serviço publico do servidor para a data que ingressou no órgão federal anterior pelo **\>CAATDADSIA**

	Posterior a isso, informar as férias por meio do **\>CAIFFERIAS**

	Importante lembrar que para nesse caso o SIAPE **NÃO** PERMITE lançamento de férias **de menos de 30 dias**. Portanto deve-se lançar dois períodos e dar perda no primeiro período que já foi gozado no outro órgão, informando no campo de observação que foram gozadas no órgão anterior.

	Outra coisa importante é que o SIAPE vai gerar o pagamento de **1/3 de férias**, o que **deve ser lançado como desconto** na mesma rubrica (porque se tirou um algum dia de férias no órgão anterior ele já recebeu o 1/3 de férias), o valor referente à proporção dos dias a serem gozados aqui no DPRF, já que o sistema automaticamente já descontará a parcela dos dias de perda. Quaisquer dúvidas entra em contato com a DICAD.

**38\. INTEGRAÇÃO DA MATRÍCULA**

Usado sempre que remover alguém e para outros casos

**\>CAEEINTGRS**

**39\. PENDÊNCIA**

Às vezes, quando vamos lançar alguma coisa do servidor, o sistema critica como pendências a serem resolvidas. Na maioria dos casos, resolve-se no \>**CAIASERVID** e/ou **\>CAATDADSIA.** Depois faz a Integração \>CAEEINTGRS.

**40.NOMEAÇÃO**

**Editar documento legal interno** \- DPEDITADL – assunto :016

finalizar DPFINAL

**1ª ETAPA**

**(inclui/altera servidor)**

Preencher todos os campos.

Os campos titulação/formação se possuir 2º grau (antigo científico) deverão ser preenchidos com os códigos 42 e 20 respectivamente.

INGRESSO NO ÓRGÃO:

Data: (INFORMAR A DATA DE EXERCÍCIO)

Ocorrências: 01100 – nomeação de cart. Efet. Art 9, item I L.8112/90.

Dipl. Legal, Cod : 04 NR: (portaria) data: data da publicação (igual ao Doc legal)

INGRESSO NO SERVIÇO PÚBLICO.

Data: mesma data da publicação da portaria de nomeação

Se ocupar cargo público anteriormente, informar a data de ingresso no órgão de origem, excluindo estados e municípios que deverão ser atualizados quando da averbação de tempo de serviço.

OCORRÊNCIA : 01100 – nomeação de cart. Efet. Art. 9 item I L.8112/90

Dipl. Legal cod :04 NR: nº da portaria Data: data da publicação da portaria.

**2ª ETAPA**

**\>PEATPROVEX (provimento excepcional)**

**CPF**

**DATA DE INÍCIO:**

**FORMA DE PROVIMENTO- 009**

**CARGO – 911001**

**TABELA – 912**

**ÓRGÃO DE ORIGEM – Não preencher**

**Enter**

**NÍVEL – NI**

**CLASSE – G**

**PADRÃO – I**

**VAGA – Nº constante na portaria**

**UORG – lotação – conforme portaria da superintendência**

**UORG – Exercício – conforme portaria da superintendência**

**DL EXTERNO – Não preencher**

**Enter**

**Preencher o DL INTERNO**

**Enter, será exibida a matrícula Siapecad**

**Enter, será exibida a matrícula do servidor. Anotar**

**Enter, confirma.**

**Não esquecer de pagar o AUXILIO ALIMENTAÇÃO (CDATALIIND)**

**PENSÃO ALIMENTÍCIA**

Observação: para verificação e emissão de relatórios de **Pensão Alimentícia Ativas (em Pagamento) de cada Mês/Ano siga o seguinte caminho do** SIAPENET:

**WWW.SIAPENET.GOV\>atualização cadastral\>pensão alimentícia\>relatórios gerenciais**

**ou verifique na pasta NUAP: nuap\\PENSÃO ALIMENTÍCIA**

**Inclusão ou alteração:**

Arquivar o original na pasta do servidor. Inserir os dados da pensão no arquivo digital da pasta **NUAP\\PENSÕES ALIMENTÍCIAS\\Cadastro de Pensões Alimentícias.ODS**

**Para novas pensões**: entrar em contato com a pensionista para preencher o formulário de cadastro (pasta NUap\\Pensões Alimentícias\\Ficha Cadastro Pensão Alimentícia).

Entrar no site [www.siapenet.gov.br](http://www.siapenet.gov.br/) (mesma senha do Siape) \- *atualização cadastral* – *pensão alimentícia.*

**Procedimento Antigo:**

Inclusão Manual (Rubrica 97002\)

**FOLHA/FPATMOVFIN**

**Antes de fazer, verificar se no ofício do juiz consta todos os dados em negrito abaixo .**

SALÁRIO BRUTO \+13o. \-INSS E \-IR: \- assunto de cálculo 06\. 20% utililzar 2000, 10% utilizar 1000\. Dá enter, preenche com os dados do beneficiário. **Nome dos filhos e CPF da mãe ou dos filhos conforme o caso. Banco , agência e conta para depósito.**

SALÁRIO MÍNIMO: \- assunto de cálculo 08\. 1 salário 100%, 2 salários, 200%. Dá enter, preenche com os dados do beneficiário. **Nome dos filhos e CPF da mãe ou dos filhos conforme o caso. Banco , agência e conta para depósito.**

**OBS \-** Se o juiz der sobre o 13º ( na pensão sobre o salário mínimo) tem que anotar e pagar manualmente no final do ano.

**42\. AJUDA DE CUSTO REMOÇÃO EX-OFFÍCIO**

O valor da ajuda de custo corresponderá a **01 (uma) remuneração, caso o servidor possua até 01 (um) dependente,** a **02 (duas)** remunerações, ***caso o servidor possua 02 (dois) dependentes***, e a **03 (três) remunerações, caso o servidor possua 03 (três) ou mai**s dependentes.

A ajuda de custo será concedida em valor proporcional ao da remuneração do servidor, correspondente ao mês em que ocorrer o deslocamento para a nova sede.

O valor da ajuda de custo corresponderá a **01 (uma) remuneração, caso o servidor possua até 01 (um) dependente,** a **02 (duas)** remunerações, ***caso o servidor possua 02 (dois) dependentes***, e a **03 (três) remunerações, caso o servidor possua 03 (três) ou mai**s dependentes.

Na hipótese em que o servidor fizer jus à ajuda de custo e que, da mesma forma, o cônjuge ou companheiro o fizer, somente um perceberá a vantagem.

São assegurados à família do servidor que falecer na nova sede, ajuda de custo e transporte para a localidade de origem, dentro do prazo de 01 (um) ano, contado do óbito.

O servidor fica obrigado a restituir os valores da ajuda de custo quando, injustificadamente, não se apresentar na nova localidade no prazo de 30 (trinta) dias ou quando, antes de decorridos 03 (três) meses do deslocamento, pedir exoneração ou abandonar o serviço.

Não haverá restituição quando o regresso do servidor ocorrer ex-offício, em razão de doença comprovada, ou em virtude de exoneração, no interesse da Administração, após 90 (noventa) dias do exercício na nova sede.

Será concedida ajuda de custo àquele que, não sendo servidor da União, for nomeado para cargo comissionado (DAS), com mudança de domicílio.

Não se concederá ajuda de custo ao servidor que se afastar do cargo ou reassumi-lo em virtude de mandato eletivo ou que for exonerado, a pedido, do cargo em comissão que ocupa nem, tampouco, em exercício posterior ao fato que ensejou o direito a essa indenização.

Correm por conta da Administração, as despesas de transporte do servidor e de seus dependentes, compreendendo passagem, preferencialmente por via aérea, e transporte de mobiliário e bagagem.

O servidor que, atendido o interesse da Administração, utilizar condução própria no deslocamento para a nova sede, fará jus à indenização da despesa do transporte, correspondente a 40% (quarenta por cento) do valor da passagem de transporte aéreo no mesmo percurso, acrescida de 20% (vinte por cento) do referido valor por dependente que o acompanhe, até o máximo de 03 (três) dependentes.

Quando os dependentes do servidor não se utilizarem do meio de deslocamento previsto no parágrafo anterior, a repartição fornecerá passagens rodoviárias ou aéreas para os que, comprovadamente, se utilizarem destes meios.

Na concessão do transporte de mobiliário e bagagem será observado o limite máximo de 12m3 (doze metros cúbicos) ou 4.500kg (quatro mil e quinhentos quilogramas) por passagem inteira, até 02 (duas) passagens, acrescida de 3m3 (três metros cúbicos) ou 900Kg (novecentos quilogramas) por passagem adicional, até 03 (três) passagens.

Compreende-se como mobiliário e bagagem os objetos que constituem os móveis residenciais e bens pessoais do servidor e de seus dependentes.

Na hipótese de o dependente não acompanhar o servidor quando do seu deslocamento, deverá ser informado ao respectivo órgão de pessoal as razões que motivaram a sua permanência na origem, de modo que a ajuda de custo possa ser paga quando do efetivo deslocamento do dependente, não podendo, entretanto, passar de um exercício para o outro.

São dependentes do servidor para fins de concessão de ajuda de custo, passagem aérea e de transporte de mobiliário e bagagem:

* 	  
   	Cônjuge 	ou companheira legalmente equiparada;  
   	  
* 	Filho de 	qualquer condição ou enteado;  
   	  
* 	Menor 	que mediante autorização judicial viva sob sua guarda e sustento;  
   	  
* 	Pais, 	desde que comprovadamente vivam às suas expensas e se desloquem 	para a nova sede do servidor;  
   	  
* 	Filho 	maior de idade, desde que inválido;  
   	  
* 	Estudante 	de nível superior, menor de 24 (vinte e quatro) anos, que não 	exerça atividade remunerada.

Somente para efeito de concessão de transporte (passagem aérea), considera-se dependente do servidor, um empregado doméstico, com carteira assinada pelo servidor.

O servidor é obrigado a entregar o comprovante do seu deslocamento e de seus dependentes, na unidade de Recursos Humanos do seu novo local de trabalho, no prazo máximo de 30 (trinta) dias, sob pena de devolução do valor da ajuda de custo que tenha recebido.

São documentos válidos para comprovar o deslocamento do servidor e seus dependentes com a mudança de domicílio (endereço residencial):

* 	  
   	Contrato 	de locação de imóvel residencial, se for o caso;  
   	  
* 	Comprovante 	de matrícula em instituição de ensino;  
   	  
* 	Conta de 	água, luz ou telefone residencial em nome do servidor;  
   	  
* 	Bilhetes 	de passagem em nome do servidor e seus dependentes, se for o caso; e  
   	  
* 	Outros 	documentos que comprovem a mudança de domicílio em caráter 	permanente.

**43\. PRISÃO**

**\>CAINOCORSE**

Ocorrência **167**

Informar início da ocorrência, fim previsto, e observações (documento legal).

Lançar também no cadastro: **\>CDATAFAST**

Grupo: **003**

Data início:

Data término(se houver).

Preencher documento legal.

Em qualquer caso, o servidor deixa de trabalhar e, portanto, não tem direito de receber pagamento enquanto estiver preso. Assim, sendo a prisão preventiva, temporária ou definitiva, deve-se lançar a ocorrência de prisão.

Normalmente, quando a prisão é definitiva é porque o servidor já foi julgado e condenado. Nesse caso, deve-se observar se a sentença do Juiz determinou a perda do cargo. Se isso ocorreu, deve-se abrir um processo, instruí-lo e mandá-lo a esta CGRH para os procedimentos de praxe, visando a publicação de ato demissionário do servidor.

**44\. PROGRESSÃO**

**\>CAINPROGMA**

**observação**: Se for fazer a **revisão de progressão**, observar se envolve o período de entre **fevereiro e março de 2008,** já que nesta época houve a **mudança do cargo 911 para 912**, logo precisa fazer o posicionamento (código **546**, na função **\>CAINPOSHIS**), ficará o servidor então com **02 linhas repetidas** da mesma classe padrão nesse período (na tela da função \>CACOPOSPRO). Só após fazer isto é possível “excluir” todas a progressões antigas para lançar a nova corrigida conforme a portaria do servidor.

Para incluir progressão funcional: Aguardar Portaria do CGRH.

\*\_1ª ETAPA \_ \>DPEDITADL\* (edita documento legal Interno)

**\>DPEDITADL** ( EDITA DOC. LEGAL INTERNO )

NUMERO : nº da Portaria

UORG : Regional

ANO : 2007

TIPO : 02 PORTARIA

\------------------------------------------------------------------------------

ASSUNTO : 71 Progressão funcional manual

APÓS PREENCHIDOS OS CAMPOS

TECLAR \------- F3 – Atualiza e Sai

\*\_2ª ETAPA\_ \>CAINPROGMA \*

\>CAINPROGMA ( INCLUI PROGRESSAO FUNC.-MANUAL)

**UTILIZAÇÃO DA MACRO MUDAR DADOS EDITANTO A MACRO:**

**DADOS TAIS:**

* 	  
   **DA 	PORTARIA**  
   	  
* **DATA 	LANÇAMENTO: OU MARÇO OU SETEMBRO.**

\>CACOPOSPRO: (CONSULTA POSICIONAM/PROGRESSÃO) \-Verificar lançamentos

\>CAEXPOSIC \-\> EXCLUI POSICIONAMENTO (caso em que erre no lançamento)

Obs.: Não deve-se rodar a macro mais de uma vez (siape registra todos os lançamentos)

DOCUMENTO LEGAL \- NUMERO DO DL: ( nº da Portaria) UORG: Regional ANO: 2007 TIPO: 02 \-Portaria

MATRICULA : Informar a a matrícula do servidor com direito a progressão constante na portaria

FORMA DE ENTRADA: 046 PROGRESSAO FUNCIONAL MANUAL

DATA VIGENCIA : 01MAR2007

NOVO POSICIONAMENTO

NIVEL : NI \- nível intermediário para PRF, servidores do quadro especial NS para nível superior, NI \- nível intermediário e NA para nível auxiliar.

CLASSE : consultar portaria

PADRAO : consultar portaria

OBS: Não finalizar o DL antes do lançamento de todos os servidores beneficiados pela portaria de progressão. Entretanto, caso aconteça utilizar a transação \>DPRBDL ( REABRE DOCUMENTO LEGAL )

**\*Para servidores a aposentados utilizar a transação \***

\>\*CACRPROVAP ( CORRIGE PROVENTOS APOS POR ERRO\*

\>CAALPROVEN ( ALTERA PROVENTOS DE APOS)

\*Depois de adotados os procedimentos, consultar a transação \>CDCOINDFUN ( DADOS INDIVIDUAIS FUNCIONAIS ), para verificação dos lançamentos.\*

**\*Para INSTITUIDORES PENSAO utilizar a transação \*** \>CDALPSINST ( ALTERA INSTITUIDOR DE PENSAO )

\*\*\*\*\*\*\*\*OBS: NO FINAL DO PROCESSO, FAZER \>CAEEINTGRS E VERIFICAR O PAGAMENTO. SE A FOLHA ESTIVER FECHADA, DEVEMOS LANÇAR O PGTO RETROATIVO PROPORCIONAL

* INSTITUIDOR DE PENSÃO (Transações na ordem de utilização)

CAENEXCAPO

CAIFOBITRH

CDATSITFUN

CACAENCAPO

CDINPSBENE

FPATPSCOTA

FPCLPAGTO

FPATPSCALC

* INSTITUIDOR DE PENSÃO \- ATUALIZAÇÃO DO FUNDAMENTO LEGAL, FUNDAMENTO DESATIVADO

CDATAPOSEN

CDALPSINST

CACAENCAPO

CDINPSBENE

FPATPSCOTA

FPCLPAGTO

FPATPSCALC

Obs: Para verificar qual o tipo de pensão compatível com o grau de parentesco, consultar TBCOPENSÃO.

**FALECIMENTO DE PENSIONISTA**

\>CDEXPSDABE – encerramento de pensão \- falecimento de pensionista

**46\. RECONHECIMENTO DE DÍVIDA – PAGAMENTO DE EXERCÍCIOS ANTERIORES**

**\>GRINBENEF**

**\>GRATUABEN**

Lançar ou Alterar dados conforme reconhecimento de dívida.

**47\. SUSPENSÃO**

RUBRICA : 80701

Lançar no FPATMOVFIN.

D(desconto), rubrica 80701, seqüência 1, I(inclui), ENTER, prazo 001, assunto 26, fração X / 30, onde X são os dias de suspensão. Rubricas de incidência (linhas de baixo, lançar só 5 rubricas de cada vez se for o caso). Incide sobre as rubrica: 82483\.

Repetir a operação em separado para Auxílio Alimentação: D(desconto), rubrica 80701, seqüência 2, I(inclui), ENTER, prazo 001, assunto 26, fração X / 22, onde X são os dias de suspensão. Incide sobre as rubrica: 136\.

Não esquecer de lançar ocorrência 127 no \>CAINOCORSE.

**48\. REPOSIÇÃO AO ERÁRIO / INDENIZAÇÃO AO ERÁRIO (usado para descontar o pagamento de honorários advocatícios de processos)/RESSARCIMENTO AO ERÁRIO**

**Quando o servidor tiver que devolver dinheiro a união por recebimento indevido. Deve-se observar o processo e se há ciência do servidor para efetuar esse lançamento.**

\>FPATMOVFIN ou \>FPATPSMFIN (se for pensionista) (lembrando que o siape já lança automático, não pode/deve lançar quantas parcelas, deixe a linha em branco \_\_\_, sob pena de dar errado por conta da limitação de 10% do subsídio/pensão)

Rubrica **00145 OU 83212 (sem incidência de PSS)**

Seqüência: **6**

Assunto **38** (**já lança automático parcelas no limite de 10% do subsídio)**.

Para pagamento em parcelas calculadas pelo sistema: informar montante da dívida em real OU prazo 001 e Valor informado para pagamento integral (inserir valor total com vírgula)

Transação: \> FPAT**MOV**FIN ou **\>FPATPSMFIN**

REND/DESC: **D**

CODIGO : **145**

SEQUENCIA: **6** OPERACAO (I/A/E): **I**

RUBRICA:VERIFICAR NO PROCESSO (Ex. PSS (para ativos) é RUBRICA **98002; 220 (férias não gozadas)**

MONTANTE DA DÍVIDA: Valor da reposição ou indenização

RETIRAR FUNÇÃO CHEFIA DO SIAPE – como se nunca tivesse chefia antes

\>CAEXNOMEAC

RETIRAR EXERCÍCIO

\>CAEXLOCEXE

REABRIR DOCUMENTO LEGAL QUANDO FOI FINALIZADO – DOC LEGAL, FINALIZAR, ABRIR

\>DPRBDL

FOLHA PENSIONISTA – PENSÃO. CÁLCULO PENSIONISTA

\>FPATPSCALC

CONSULTA DADOS DE BENEFICIÁRIO DE PENSÃO

\>CDCOPSDABE

FICHA FINANCEIRA PENSIONISTA – PENSÃO.

\>FPCOPSFICF

ALTERA REPRESENTANTE LEGAL PENSIONISTA- PENSÃO

\>CDALPSRLEG

SERVIDOR FOI REMOVIDO MAS A CHEFIA FICOU NA REGIONAL ANTIGA – LANÇAMENTO CHEFIA HISTÓRICO

\>CADTMATFP – DESATIVAR MATRÍCULA

\>CAEXNOMEAC – EXCLUI NOMEAÇÃO DE CHEFIA DA REGIONAL ANTERIOR

\>CARTMATFP – ATIVA MATRÍCULA

\>FPCLPAGTO – RODAR PAGAMENTO

\>CANHISPFU – INCLUI HISTÓRICO DE FUNÇÃO

\>CACODETPFU – CONSULTA FUNÇÃO

CONSULTA DE VAGAS DISPONÍVEIS – CARGO ADM E PRF – vaga

\>GRCOQUAVAG

origem-

grupo- 911(prf) ou 437(adm)

cargo – 001 “ ou 014 “

situação – 2

VERIFICAR VÍNCULOS DO SERVIDOR \- SE JÁ FOI SERVIDOR DE OUTRO ÓRGÃO

\>CDCONVINC

ALTERAÇÃO DE FÉRIAS INTERROMPIDAS – INTERRUPÇÃO DE FÉRIAS

\- A legislação diz que ao interromper férias, o restante do período deve ser gozado em parcela única.

\- mas, em caso de necessidade de alteração, e caso seja uma parcela histórica, a alteração pode ser feita na transação:

\>CAITFERIAS

ca

OBS: O PRIMEIRO DIA INTERROMPIDO, O SERVIDOR NAO TRABALHA.. OU SEJA, SE ELE SOLICITOU INTERRUPÇÃO NO DIA 16, ELE NÃO DEVE TRABALHAR.. MAS CASO ESTEJA TRABALHANDO, VC DEVE INTERROMPER A PARTIR DO DIA 17

AVERBAÇÃO – SERVIDOR ÓRGÃO SIAPE

Quando o servidor vier de órgão federal que utiliza SIAPE, não precisa averbar no CAINTAS, somente instruir processo.

POSSE / PROVIMENTO SERVIDOR EM CLASSE PADRÃO DIFERENTES

Quando o código de vaga está reservado para outra classe/padrão, a PRF deve solicitar ao MPOG para modificar a vaga para AI.

Mas é possível, mesmo assim, dar provimento em outra classe/padrão, burlando o SIAPE (OBS: não repassar ;p)

1- dar provimento na classe/padrao errada (aquela que aparece no ADCOVAGA) – fazer todo o procedimento de posse até o servidor entrar na folha de pagamento

2- quando você consulta o CACOPOSPRO, é possível observar a classe padrão errada.

3- pegar o doc legal de nomeação para usar como DL – pode pegar no CACOPOSPRO

4- Após, entrar no CAALPROGMA e colocar o servidor na classe padrao correta utilizando o DL de nomeação

\- forma de entrada: 009

\- data: data de posse

\- aviso: quer continuar? S

\- Novo posicionamento: NI / A / I

\-Confirma? S

5- \>CAEXPOSIC – excluir o posicionamento errado (retificado)

6- confirmar se o posicionamento esta correto no \>CACOPOSPRO

EXONERAÇÃO DE SERVIDOR / EXONERADO \- FÉRIAS

Quando o servidor pede exoneração, ele perde o direito às férias (\>PERDADIREI \- CAIFPERFER.. quando não há quebra de vínculo, ou seja, se ele tomar posse em outro órgão sem a quebra, o servidor poderá usufruir o restante do período (férias especiais- CAIFFERESP)

você pode consultar no \>cacopca se o servidor tem esse direito às férias

ALTERAÇÃO DE UPAG DE APOSENTADO/PENSIONISTA

No primeiro comando de envio do servidor para nova UPAG colocar a data do requerimento, no segundo comando de recebimento colocar a data posterior ao requerimento. EX: 14/01/2020 “CALITRANSF” 15/01/2020 “CAACTRANSF”

 Para pensão indenizatória utilize: CDLIPSGRAC ( LIBERA INS/BENEF.PENS.GRACIOSA ) e CDACPSGRAC \-\> ACEITA INST/BENEF.PENS.GRACIOS

OBS: Incluir no **Bloco Interno 219445**

TROCA DE UPAG

Mudança de upag de aposentado

Mudança de upag de pensionista

1\) fazer TROCAHAB e selecionar UPAG de origem do servidor

2\) \>CALITRANSF – enviar o servidor para a UPAG nova ( ex: em 01/01/2018)

3\) fazer TROCAHAB e selecionar a UPAG de origem

4\) \>CAACTRANSF – receber o servidor (ex: 02/01/2018)

\*Em caso de pensionistas os comandos são: \>CDLIPSUPAG e \>CDACPSUPAG

ou \>CDLIPSGRAC e \>CDACPSGRAC (pensão graciosa)

OBS: Para tirar o extrato e anexar ao processo sei usaor o e-siape **CDCOINDFUN** no caso de aposentado. Já para pensionista usar CDCOPSDABE também no esiape.

ALTERAÇÃO DE ENDEREÇO DE UORG / REGIONAL

\>TBCOESTUOR

SERVIDOR APOSENTADO COM FUNÇÃO EM OUTRO ÓRGÃO

Se um servidor aposentado na PRF assumir função em outro órgão, o RH da PRF não efetua nenhum cadastro. Não existe cessão de servidor aposentado.

Ou seja, o órgão que o servidor assumir função irá criar uma nova matrícula SIAPECAD para o aposentado e cadastrar a função.

REMOÇÃO DE SERVIDOR COM 2 MATRÍCULAS SIAPECAD

\-DESATIVAR MATRÍCULA COM ERRO

\-CACANPCA

\-CAEXMATRIX

\-CAEEINTGRS

ALTERAÇÃO DE ESTRUTURA – NOME / NOMENCLATURA UORGS ETC

\>TBALUORG

CONSULTA PREVISÃO DE FUNÇÃO/ REMANEJAMENTO DE FUNÇÃO

EX: você vai cadastrar a função e ela não está disponível para a divisão… ai você pode remanejar de outra divisão que estiver função disponivel.

\>ADCOPREFUN – consulta previsão de função

apertar F1 para ver a opção para remanejamento

REVERSÃO DE APOSENTADORIA

**ALERTA: Nunca lance a reversão da aposentadoria na mesma folha de publicação. Salvo se os efeitos forem a partir do dia 1º do mês.**

\>caenexcapo – cancela a aposentadoria por reversão (003); informar a data da portaria

\>patprovex – aguardar a próxima folha para lançar, pois o servidor pode ficar com o líquido negativo (no próximo mês você lança os retroativos); fazer novo provimento no 003-reversão, data: 1 dia após a data da portaria de reversão

CANCELAMENTO DE APOSENTADORIA

\>caenexcapo – encerramento excepcional a aposentadoria; informar a data da portaria.

\>cacanvac – cancela vacância

EXCLUSÃO DE APOSENTADORIA

\>caexapos – exclusão de aposentadoria; correção de cadastro.

A exclusão da aposentadoria não cancela a vacância, então é preciso ir no

\>cacanvac – cancela vacância

Obs: Deve ser evitada a exclusão.

# ESTATÍSTICA DE PESSOAL

\>GRCOLOTREA – CONSULTA LOTAÇÃO REAL, permite a consulta de vagas ocupadas e disponíveis por cargo e grupo cargo, upag e uorg.

CACOCHEFIA ( CHEFIA E UORGS SEM CHEFIA ) consulta chefias do órgão

CACODETPFU \-\> DETALHE DE PROV.FUNCAO/CC/CNE 

\>ADCOCRIFUN \-\> CONSULTA VAGAS DE FUNÇÃO NO ÓRGÃO

ESTILO DE CONSULTA:          (   ) GENERICO                                

                    ( \_ ) DETALHADO                               

                    ( X ) CONSOLIDADO POR FUNCAO/CARGO EM COMISSAO

PAINEL ESTATÍSTICO DE PESSOAL DO MINISTERIO DO PLANEJAMENTO:

[http://painel.pep.planejamento.gov.br/QvAJAXZfc/opendoc.htm?document=painelpep.qvw\&lang=en-US\&host=Local\&anonymous=true](http://painel.pep.planejamento.gov.br/QvAJAXZfc/opendoc.htm?document=painelpep.qvw&lang=en-US&host=Local&anonymous=true)

# 

# GDATPRF

	SIGA OS SEGUINTES PASSOS:

ACESSE O SIAPENET \> Órgão/UPAG \> Servidor \> Gratificação \> Concessão de Gratificação \> COLOQUE A MATRÍCULA DO SERVIDOR

CLIC EM CONSULTA \> CLIC NO NOME DO SERVIDOR \> CLIC NO ÓRGÃO 30802

CLIC EM 0084 GDATPRF \> CLIC EM ALTERA (Altera a data-fim da concessão para 31/10/20XX e o valor da pontuação do servidor)

CLIC EM GRAVAR → OK → OK.

OBSERVAÇÃO: Depois de implantada a GDATPRF confira o pagamento do servidor, utilizando a transação \>FPCLPAGTO.

O mesmo se dá com a GDACE, basta selecionar a gratificação correta.

Caso não apareça a opção, é porque faltam ser incluídos os dados institucionais. Estes devem ser incluídos no caminho: Órgão/UPAG \> Servidor \> Gratificação \> Dados Institucionais

A conferência do pagamento da GDATPRF aos servidores é de responsabilidade de cada Regional. Qualquer ajuste deverá ser feito na folha de pagamento de dezembro, visando evitar que valores devidos aos servidores caiam em exercícios anteriores.

**GDATPRF – APOSENTADOS**

MEDIA DE PONTOS, relatório Siape \>CONSGRAT

Incorporação da GDATPRF, conforme Lei 13324/2016:

Art. 88\.

I \- a partir de 1o de janeiro de 2017: 67% (sessenta e sete por cento) do valor referente à média dos pontos da gratificação de desempenho recebidos nos últimos sessenta meses de atividade;

II \- a partir de 1o de janeiro de 2018: 84% (oitenta e quatro por cento) do valor referente à média dos pontos da gratificação de desempenho recebidos nos últimos sessenta meses de atividade; e

III \- a partir de 1o de janeiro de 2019: o valor integral da média dos pontos da gratificação de desempenho recebidos nos últimos sessenta meses de atividade.

[Nota Técnica SEI nº 5431/2023/MGI](https://drive.google.com/file/d/1i9iTz853vFEzKTGPXLx0E1C-Zhw0ZOxi/view?usp=share_link): Expedição de orientações aos órgãos e entidades integrantes do SIPEC quanto a possíveis impactos decorrentes da reforma administrativa promovida pela Medida Provisória nº 1.154, de 1º de janeiro de 2023\.

# 

# SENHA SIAPENET

***1)Entrar*** no portal [www.siapenet.gov.br](http://www.siapenet.gov.br/) selecionar campo "servidor";

**2\) Verificar** se o sevidor está **bloqueado** no SITE;

**2\) inserir** identificação unica e \<avançar\>

**3\)** Nesta tela, **verificar mensagens automática do sistema** "mensagens em vermelho" acima do quadro usuário e senha.

**4\)** caso não se lembre do : usuário e da senha, peça para ***"RECUPERAR" usuário e senha***, então o sistema vai abrir uma nova tela e assim sucessivamente. Lembre-se o sistema é automático, enviando todas as informações necessárias para o email cadastrado.

5\) na tela anterior, o servidor deverá ter muito cuidado ao ***informar os dados*** que se pedem, inclusive nos dados de CEP e Telefone devem ser os que estão no SIAPE. No caso do **"código de segurança"** eu estou pedindo para recuperar para você, e ele vai ser ***enviado para seu email.***

Acredito que até aqui, você poderá executar sem problemas, os passos adiante vão depender do servidor em lançar os dados requeridos, peço devida atenção para as respostas automáticas do sistema, e ter o EMAIL cadastrado aberto em outra "janela" do windows para estar sempre atualizado com as mensagens do SIAPENET.

\+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

2\. **Atualizar** o e-mail no **siapenet** se **não** estiver **bloqueado** e apenas esqueçeu ou está sem acesso ao e-mail cadastrado;

3\. Peça para o servidor que acesse o **siapenet** e o **webmail** da intranet **simultaneamente**, cadastre **usuário e senha**, se não for possível (não lembra a senha, nunca acessou, etc.) tente até efetivamente bloquear (03-três tentativas), depois de bloqueado faça novamente o cadastro no SIAPENET,que então enviará a resposta para o e-mail cadastrado no SERPRO(\>caiservid)/siapenet, que serão, doravante, envidadas ao novo e-mail cadastrado:

**3\)** Nesta tela, **verificar mensagens automática do sistema** "mensagens em vermelho" acima do quadro usuário e senha.

**4\)** caso não se lembre do : usuário e da senha, peça para ***"RECUPERAR" usuário e senha***, então o sistema vai abrir uma nova tela e assim sucessivamente. Lembre-se o sistema é automático, enviando todas as informações necessárias para o email cadastrado.

5\) na tela anterior, o servidor deverá ter muito cuidado ao ***informar os dados*** que se pedem, inclusive nos dados de CEP e Telefone devem ser os que estão no SIAPE. No caso do **"código de segurança"** eu estou pedindo para recuperar para você, e ele vai ser ***enviado para seu email.***

Acredito que até aqui, você poderá executar sem problemas, os passos adiante vão depender do servidor em lançar os dados requeridos, peço devida atenção para as respostas automáticas do sistema, e ter o EMAIL cadastrado aberto em outra "janela" do windows para estar sempre atualizado com as mensagens do SIAPENET.

Os contracheques deixaram de ser impressos. Se você deseja continuar recebendo faça sua opção no Siapenet, no caminho: **SIAPEnet/Servidor:**

**Dados Financeiros \> Opção de Emissão do Contracheque**.

# SIAPE EXTRATOR

Extração de CNH:

\- ARQUIVO: SIPE-U-RH-EXTR

campos:

\_ CO-CONTROLE-RH CS

X NU-CPF-RH CS

\_ NO-RH CS

\_ NO-RH-DIFERENCIADOR CS

\_ IN-SEXO-RH

\_ CO-ESTADO-CIVIL-RH CS

\_ DA-NASCIMENTO-RH CS

\_ NO-MUNICIPIO-NASCIMENTO-RH

\_ SG-UF-NASCIMENTO-RH

\_ NO-PAI-RH

\_ NO-MAE-RH

\_ CO-ESCOLARIDADE-RH CS

\_ IN-NACIONALIDADE-RH

x NU-CART-MOTORISTA-RH

x NU-REGISTRO-CART-MOTORISTA-RH

x IN-CATEGORIA-CART-MOTORISTA-RH

x SG-UF-CART-MOTORISTA-RH

x DA-PRIMEIRA-HAB-MOTORISTA-RH

x DA-EXPEDICAO-CART-MOTORISTA-RH

x DA-VALIDADE-CART-MOTORISTA-RH

\_ NU-PIS-PASEP-RH

\_ NU-PASSAPORTE-RH

\_ NU-ISS-RH

\_ CO-PAIS-ORIGEM-RH CS

\_ DA-CHEGADA-BRASIL-RH

\_ TX-NACIONALIDADE-RH

# PENSÃO INDENIZATÓRIA

**Ao indicar o servidor responsável pela inclusão da pensão, verificar se constam no processo os dados bancários (um para cada cpf), cpf de todos os beneficiários, RG (data de nascimento, sexo, nome da mãe, órgão expedidor, UF e data de expedição), estado civil, endereço, telefone, e-mail e informações do título de eleitor. Caso não constem todos os dados, solicitar a inclusão.**

1- ACESSAR SIAPE DAR TROCAHAB PARA A REGIONAL DO BENEFICIÁRIO, consultar código da upag através da transação: TBCOUPAG (CONSULTA UNID. PAGADORA) 

CONFIRMA HABILITAÇÃO AUTOMÁTICA: **S**

2-\>**CDINPSGRAC** \-\> INCLUI INST. PENSAO GRACIOSA

Caso a transação não esteja disponível na sua habilitação, imprima a tela do siape e inclua no processo. Restitua o processo informando a Dicju.

3 \-\> UORG CONTROLE  

: \_\_\_\_\_ (código da upag) 

\- CAMPO PROCESSO \= PROCESSO SEI

4- DATA LEI/PROC \= DATA DA PORTARIA OU DATA QUE DETERMINAR OS EFEITOS \- CITADO EM PORTARIA OU FORÇA EXECUTÓRIA

5- DATA DA PUBLICAÇÃO \= DATA DE PUBLICAÇÃO NO D.O.U OU DATA DO INÍCIO DO PROCESSO

6- RESUMO \= NÚMERO DO PROCESSO JUDICIAL+SEI E OUTRAS INFORMAÇÕES

7- ANOTAR MATRÍCULA GERADA

8- SIM \=S

COMANDO INCLUIR BENEFICIÁRIO (QUANDO TIVER DEPENDENTE)

COMANDO= \>**CDINPSBENE**

9- \>**CDIAPSBENE** 	\-\> INCLUI / ALTERA DADOS DO BENEFICIÁRIO

10- CONTROLE \= N° 	DA REGIONAL

11- MAT. INSTITUIDOR \= MATRÍCULA ANOTADA ANTERIORMENTE

12- CPF DO BENEFICIÁRIO

13- PREENCHER OS DADOS \= MÃE, SEXO,DEPENDENTE,PROCESSO SEI,,ESTADO CIVIL, RG, ENDEREÇO, TELEFONE, EMAIL SEU OU DA SGP.REGIONAL DELE, REPRESENTANTE LEGAL CASO TENHA.

14- TIPO DE CONTA \= 04/BANCO= DADOS BANCARIOS

15- TIPO DE PENSÃO \=F1 PARA SELECIONAR

16- ORGÃO PAGADOR \= 06 SIAPE

17- ANOTAR MATRICULAS

PARA ATERAR O CADASTRO OU BASE DE CÁLCULO BRUTO

1- DAR O COMANDO \>CDIAPSBENE

2- ALTERAR O QUE FOR NECESSÁRIO (SOLICITADO NO PROCESSO SEI).

3- ALTERAR BASE DE CÁLCULO BRUTA

OBS: Para alterar a base de cálculo bruta primeiro tem que dar o comando **CDAUPSCRIT** no BENEFICIÁRIO para retirar a crítica ((:AUTOR. NÃO CRITICAR DADOS PENSIONISTA). ( CRÍTICA: SEM PERMISSÃO PARA ATUALIZAR). depois fazer a alteração.

\* Usar como base o valor dado pelo [Formulário de Concessão de Pensão E.C 103/2019](https://sei.prf.gov.br/sei/controlador.php?acao=arvore_visualizar&acao_origem=procedimento_visualizar&id_procedimento=28259583&id_documento=28274610&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=b8db4cb06f00f886cdf77eb41575b87122a337b3b9510fb9de53ee75cb1b1e3c). ou citado em documento sei.

OBS: FPATPSCALC: Rodar folha de pagamento de beneficiário de pensão

Pensão indenizatória o valor é lançado por movimentação financeira.

Uma vez lançado o valor, o processo deve ser encaminhado a SGP de controle pra acertos financeiros, se houver.

COMANDO PARA IMPRIMIR TELA DO CADASTRO

1- DAR O COMANDO \>CDCOPSDABE

2- SALVAR E ANEXAR AO PROCESSO

3- ENCAMINHAR A DIPAG PARA ACERTOS FINANCEIROS

# CONTROLE DE VAGAS

Planilha Controle de vagas (X:\\DICAD\\1. SISTEMAS DE RH\\VAGAS)

Verificar qual aba da planilha corresponde ao cargo/classe/padrão e registrar a reserva da vaga.

Solicitar a distribuição da vaga a CGGP.

Finalizar DL de progressão e SIAPE apresenta o seguinte erro "programação de bp não foi efetuada" → transação \>dppoblbs

CDAUPSCRIT: Autoriza não criticar exclusão de pensionista

# Exclusão de pensionista e redistribuição de cotas

Quando ocorre qualquer mudança entre os beneficiarios é necessário redistribuir cotas (FPATPSCOTA), calcular Instituir (FPCLPAGTO) e cálculo dos beneficiários (FPATPSCALC)

CDEXPSDABE: Exclui dados do benefício/ excluir restrição de pagamento.

# PROGRESSÃO FUNCIONAL ADMINISTRATIVA (MANUAL).

1- Entrar no siape

2 \- Digitar o comando CAINPROGMA

3 \- Criar a MACRO no seguinte passo a passo: EXIBIR/GERENCIADOR DE MACRO/ GRAVAR MACRO/ DEFINE O NOME DA MACRO E DA OK/ VAI APARECER UMA MENSAGEM DE INFORMAÇÃO DAR OK.

4 \- DAR TAB ATÉ A LINHA DL HISTORICO/DIGITAR OS DADOS DA PORTARIA “ EX: PORT N° 000….) E APERTA ENTER/ F1 E DAR TAB ATÉ A LINHA MAT. EM SEGUIDA CLICAR NA OPÇÃO INCLUIR UM PROMPT/ DAR NOME E TÍTULO AO PROMPT E MARCAR A OPÇÃO VALOR OBRIGATÓRIO E DAR OK E DEPOIS DIGITE A MATRÍCULA DO PRIMEIRO SERVIDOR A CADASTRAR A PROGRESSÃO/ SELECIONA O SERVIDOR E DA ENTER.

5 \- DIGITE NA FORMA DE ENTRADA O CODIGO 046/ DATA DA VIGENCIA(01JAN2020) DAR ENTER.

6 \- PREENCHER

\-NÍVEL: NS

\- CLASSE- 2..3..S..1..

\-PADRÃO: I..II..IV..V.

7 \- DAR ENTER MARCAR (S) ANTES DE DAR ENTER CLIQUE NA OPÇÃO INTERROMPER MACRO.

8 \- COMO A MACRO JÁ ESTÁ CRIADA SÓ IR EM REPRODUZIR MACRO E DIGITAR A MATRÍCULA QUE JA VAI PUXAR OS DADOS PREENCHIDOS

# PROGRESSÃO FUNCIONAL JUDICIAL

INCLUÍDO EM 26/03/2020

1- Recebe o processo na divisão geralmente com despacho DICJU informando se é CUMPRIMENTO ou INFORMAÇÃO.

2- Incluir o processo em bloco interno de controle 63391\. (Dicad)

3- Ler o despacho para entender a decisão e fazer exatamente como determina o juiz.

4- Após entender consultar o CACOPOSPRO (no Siape) e anexar ao processo.

5- Elaborar as planilhas usando como base os modelos salvos em DICAD/DESENVOLVIMENTO FUNCIONAL/PROGRESSÃO/PROGRESSÕES JUDICIAIS/MODELOS

6- criar uma pasta com o nome do servidor em DICAD/DESENVOLVIMENTO FUNCIONAL/PROGRESSÃO/PROGRESSÕES JUDICIAIS/TODOS e colocar todos os documentos nela: cacopospro/planilha...etc

6- Após elaborar as planilhas usando a data de ingresso no órgão ou outra data determinada pelo juiz elabora-se o despacho contendo a situação atual e nova.

7- Se for informação usar como modelo para despacho o sei [23586397](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=28720386&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=4a9a462f4eee44f2fdd430a7562e5a5cf465004a0b829b07a77e3ba51974a369). E nesse caso não tem minuta de portaria nem portaria, só faz o despacho, pede a chefia para assinar, assina posterior a chefia e devolve a DIPAG ou DICJU.

8\. Se for cumprimento, além do despacho DOC SEI modelo [22793805](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=27809790&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=6570b891b4c8ce9105eeb4d770596403d378f8192e2e68396cf9d6e14741615b) contendo as planilhas tem que fazer a minuta de portaria modelo sei [22926400](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=27964202&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=170f2b602d964825ebba9820bb0c9b192553ccd218c636d48220d929a742eec0) encaminhar o processo para a DGP para publicação da portaria, quando era CSEF nos mesmos fazíamos a portaria e esperava o chefe assinar e publicava a portaria no BSE.

9- Como fazer e publicar a portaria:

A: para fazer a portaria é só ir em: INCLUIR DOCUMENTO/PORTARIA/ COLOCAR O DOC SEI DA MINUTA DE PORTARIA E SALVAR.

B: Após a assinatura da chefia na portaria vai aparecer a opção AGENDAR PUBLICAÇÃO/EM OBSERVAÇÃO COLOCAR PROGRESSÃO FUNCIONAL POR DECISÃO JUDICAL/SALVAR e pronto só encaminhar para a regional atualizar o cacopospro DOC SEI modelo: [23015217](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=28066543&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=de872d11993dcf1675db308a12a47a043cb31382cfcecf9e7d05a8c6cc768aca).

OBSERVAÇÕES EM RELAÇÃO A ELABORAÇÃO DAS PLANILHAS:

1): No caso de inclusão do tempo de CFP considerar na planilha atual a data de ingresso no órgão já na situação nova considerar a data gerada pelo cálculo da planilha com tempo de CFP.

EX:

2\) Considerar os afastamentos da situação atual na situação nova. (interrupções do interstício devido a suspensão, faltas, licenças para tratar de interesse particular, prisão…).

3\) Observar as datas de início e fim para ver se não há sobreposição de datas.

4\) **COMO PREENCHER A PLANILHA:**

**A) SITUAÇÃO ATUAL:**

DATA BASE: Quem ingressou no primeiro semestre sempre colocar 01/09 e o ano da posse

na **Data Base do 1º Interstício.**

EX1: ingresso em 01/06/2005 na data base ficará 01/09/2005.

Já no segundo semestre coloco o ano posterior:

EX2: ingresso em 01/07/2005 na data base será 01/09/2006.

\* Com exceção da turma de 94 que sempre mantém o ano da posse 01/09/1994 independente se entrou no primeiro ou segundo semestre.

\* Na turma de 94 conferir desde o início colocando conceitos 2 e 1 até bater com o cacopospro.

\* A situação atual tem que ficar de acordo com o cacopospro

\* Sempre que mudar de setembro pra março ou vice versa será conceito 2\.

**B) SITUAÇÃO NOVA:**

**\-** Data de ingresso no órgão ou tempo de CFP, vai depender da decisão do juiz.

\- Ficar atendo ao decreto 8282 de 3 de julho de 2014 e a portaria 2778/2015.

\* ingresso posterior a 3 de julho os efeitos ficaram no interstício 2013/2014, já anterior ficará no interstício 2014/2015.

Ao fazer a portaria de pessoal concedendo a progressão judicial, não coloque progressão antes de 01/08/2006, pois as atualizações serão apenas a partir desta data.

# E-PESSOAL

## ATOS DE ADMISSÃO

\- Chegará na DICAD um processo para cada novo servidor, instruído com os vários documentos apresentados no momento da sua posse.

\- Conferir no processo os documentos imprescindíveis para o cadastramento do Ato de Admissão, tais quais: Edital de Abertura, Edital de Homologação, Portaria de Nomeação, Termo de Posse e Exercício, ADCOVAGA e Portaria que gerou a vaga.

ü Caso falte algum documento, enviar um Ofício à Regional solicitando a inclusão da documentação faltante. (Modelo [36655046](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=43376809&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=ac9df29d3414f852ee6feec9bb85580b05b162c19f5737fd489c5803e1f5ebff))

ü Caso trate-se de nomeação por via judicial, inserir o processo no Bloco Interno **e-Pessoal (SISAC) \- JUDICIAIS anos diversos** e encaminhar Ofício à DISEP, em que solicita a Decisão Judicial e a data do trânsito em julgado, se for o caso. (Modelo [36541314](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=43249845&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=20fae7ca5a05f5cb999a1b4241afe7f4e093e9e9a8aece0e4ccdb3e7c31e4506))

\- Entrar no Portal TCU

·        Gerenciar Atos de Subunidade Cadastradora

·        Subunidade Cadastradora: Divisão de Cadastro

·        Cadastrar Novo Ato

·        Tipo de Ato: Admissão – CPF – Inserir Novo

·        Preencher o formulário do site do TCU de acordo com as informações contidas nos documentos de admissão do servidor, inseridos no processo SEI

o   Bizu desta turma de Novinhos Regulares (última turma)

o   Data da Publicação do Edital: 19/01/2021

o   Data da Publicação da Homologação: 06/10/2022

o   Data de Validade do Concurso: 06/10/2024

o   Foi prorrogada? Não

o   Origem da Vaga e Data de Publicação (Liberação): ADCOVAGA \+ Portaria

o   Portaria de Nomeação: 860

o   Data de Publicação da Portaria: 07/10/2022

o   Nome e CPF do signatário: SILVINEI VASQUES \- 743.916.079-72

·        Salvar/ Criticar/ Encaminhar

\- Visualizar Espelho \- Salvar o Formulário na máquina e inserir como Anexo no Processo SEI

\- Encaminhar Processo à Regional com Ofício (Modelo [44521252](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=51092232&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=f02cb4e1367f33074f603d15e9f4b084aa491a9bae418c6c4df27101292c2801)) para inclusão na AFD do servidor.

\- Incluir nas anotações do Bloco Interno: o Nome do servidor, PRF ou ADM, Lotação, Data de conclusão do processo e nome de quem o fez.

ATO DE ADMISSÃO \- QUANDO HOUVER CRÍTICA DE ACUMULAÇÃO IRREGULAR DE CARGOS NO PORTAL E-PESSOAL

 Conforme processo [08650.016325/2023-66](https://sei.prf.gov.br/sei/controlador.php?acao=procedimento_trabalhar&acao_origem=procedimento_controlar&acao_retorno=procedimento_controlar&id_procedimento=53478794&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=785410ed1077653b0b3266dc98db3384a85bf7b29d0e74f06e2d0a50d425ea87)

Ao finalizar o cadastramento dos dados no portal e-pessoal, deve-se mandar criticar antes de enviar ao TCU. Pode ocorrer duas situações:   
	1\) Crítica de acumulação de cargos com **um** campo para a PRF justificar:

* Anexar justificativa (ato de desligamento, publicação a exoneração, licenciamento, etc)  
* Criticar novamente  
* Encaminhar para o TCU  
* Justificar no módulo indícios

	2\) Crítica de acumulação de cargos com **dois** campos para justificar \- um para a PRF e outro para o outro órgão:

* Anexar justificativa no campo destinado à PRF (ato de desligamento, publicação a exoneração, licenciamento, etc)  
* Inserir no campo destinado ao outro órgão a seguinte informação: AGUARDANDO MANIFESTAÇÃO DO ÓRGÃO XXXXXXX  
* Criticar novamente  
* Encaminhar para o TCU  
* Justificar no módulo indícios

Após o encaminhamento para o TCU, o ato deve ser justificado também no módulo indícios.

No módulo indícios vá em “Registrar esclarecimento”. Clique em “Consulta de indícios” e pesquise pelo nome ou CPF do servidor.

Na coluna “Editar” clique no local indicado para inserir os dados associados ao esclarecimento.

![][image3]

Na tela que se abrirá selecione uma resposta para a pergunta “Qual o posicionamento do órgão?” e anexe um documento oficial para comprovar o que se deseja esclarecer. Salve e feche a tela. Note que na coluna “Estado” indicará “Esclarecimento iniciado”.

 

## **ATOS DE VACÂNCIA**

\- Chegará na DICAD um processo instruído com vários documentos justificando a vacância. Para nós só interessa o PDF com a publicação da vacância no DOU.

\- Consultar o CPF do servidor em algum sistema de RH

\- Entrar no Portal TCU

\- Clicar nos 3 tracinhos do canto superior esquerdo do site (Menu e-Pessoal)

\- Atos –\> Desligamento / Restabelecimento de Admissão

\- Pesquisar por CPF

\- Clicar no ícone mais à direita (Cadastrar Desligamento)

\- Incluir Novo Desligamento

·        Data de Desligamento / Data de Publicação em Órgão Oficial / Motivo do Desligamento / SALVAR

\- Salvar o Formulário na máquina e inserir no Processo SEI

\- Incluir o Processo no Bloco **ATOS DE VACÂNCIA \- SISAC** (306040) e escrever nas Anotações: desligamento \-  Nome do servidor, PRF ou ADM, Lotação e ano de saída.

\- Encaminhar Processo à Regional com Ofício (Modelo [4](https://sei.prf.gov.br/sei/controlador.php?acao=documento_visualizar&acao_origem=protocolo_modelo_listar&id_documento=48301047&infra_sistema=100000100&infra_unidade_atual=110002991&infra_hash=08a09ab1137fb7911a5198637adf9effc32796fb0735d53838c18ef8a774154c)6845774\) para inclusão na AFD do servidor.

Para casos onde o servidor foi demitido, reintegrado e demitido novamente (ou que a reintegração foi tornada sem efeito), considerar a última data (data da portaria que torna sem efeito a reintegração).

# Consultas Gerenciais no Siape

COMO CONSULTAR CARGOS VAGOS DE PRF.

1**)** Dar o comando **GRCOLOTREA**

2\) GRUPO: 911

3)CARGO: 001

4\) O total sempre será 13.098 e deverá ser diminuído pelo número de **OCUPADOS** que dará o número real de **VAGOS**.

Caso necessite que a consulta retorne todas as carreiras discriminadas por cargo proceda da seguinte forma:

1) Órgão: 30802; Tecle Enter  
2) Msg: “Deseja discriminar por grupo de cargo?” Selecione NAO “N”  
3) Msg: “Deseja discriminar por cargo emprego?” Selecione SIM “S” e tecle Enter.

Consulta de Servidores por situação funcional, regime jurídico, cargo. 

SIAPE,GERENCIAL,GRCADAS,GRCOSITCAR ( SERVIDOR P/ SIT. FUNC./CARGO )

1 \- TOTAL DE SERVIDORES POR SITUACAO;                                

2 \- TOTAL DE SERVIDORES POR REGIME JURIDICO;                         

3 \- TOTAL DE SERVIDORES POR SITUACAO EM UM REGIME JURIDICO;          

4 \- TOTAL DE SERVIDORES POR REGIME JURIDICO EM UMA SITUACAO;         

5 \- TOTAL DE SERVIDORES POR CARGO EMPREGO EM UMA SITUACAO FUNCIONAL; 

6 \- TOTAL DE SERVIDORES POR SITUACAO FUNCIONAL EM UM CARGO EMPREGO;  

7 \- TOTAL DE INSTITUIDORES DE PENSAO POR REG. JURID. EM UMA SITUACAO;

8 \- TOTAL INSTITUIDORES PENSAO POR SIT. FUNCIONAL EM UM CARGO EMPREGO

# ATUALIZAÇÃO DO HISTÓRICO FUNCIONAL-PROGRESSÃO JUDICIAL

1- Analisar o processo com a portaria de progressão judicial

2- lançar no siape, conforme portaria através do comando **CAINPOSHIS**

3- PREENCHENDO:

A- TABELA

\- LEI 11358/06 ENQUADRAMENT0 \= 911

\- LEI 11784/08 POSICIONAMENTO= 912

\- LEI 12775/12 ENQUADRAMENTO= 913

B- NIVEL \- NS OU NI

C- CLASSE \- G

PADRÃO \- II

D= DOCUMENTO LEGAL \- DOCUMENTO DA PORTARIA

FORMA DE ENTRADA: \- 054 – JUDICIAL

DATA INICIO E FIM CONFORME PORTARIA.

APOS LANÇAR DAR O COMANDO **CAEXPOSIC** E EXCLUIR O ANTERIOR.

Transacionamento de Cessão / Requisição – SIAPE

1\) LISTA DE FUNÇÕES ENVOLVIDAS

Menu de acesso (tela preta): SIAPE → SIAPECAD → DADOSFUNC → LOTACAO → LOCALEXER

Código | Sistema | Função | Finalidade

CAINCESSAO | Tela preta | Informar Cessão | Registrar saída por cessão

CAINREQUI S | Tela preta | Informar Requisição | Registrar saída por requisição

CARRSRCED | Tela preta | Retorno Servidor Cedido | Registrar ingresso de cedido

CARRSRREQ | Tela preta | Retorno Servidor Requisitado | Registrar ingresso de requisitado

CARREXEREX | Tela preta | Retorno Exercício Externo | Registrar retorno à origem

CALIREDIST | Tela preta | Liberar Matrícula | Disponibiliza matrícula para nova UPAG

CDEXCADAST (102) | Tela preta | Excluir cadastro | Libera matrícula no órgão cessionário

CDCONVINC | Tela preta | Consultar liberação | Confirma se matrícula foi liberada

CALCEXERIN | Tela preta | Consultar | Localizar exercício interno

CALCEXEXT | Tela preta | Consultar | Localizar exercício externo

CAALPESMUT | Tela preta | Mutação de registro | Ajustar/atualizar registro

CAEEINTGRS | Tela laranja | Integração | Sincronizar vínculo oficialmente

Regra operacional:

Após movimentações no SIAPE (tela preta),

executar CAEEINTGRS (tela laranja).

Usar CDCONVINC quando houver dúvida sobre a liberação da matrícula.

2\) SITUAÇÕES — EXEMPLOS SIMPLIFICADOS

SITUAÇÃO 1 — Servidor da PRF será cedido para outro órgão

1\) Liberar matrícula → CALIREDIST (tela preta)

2\) Registrar cessão → CAINCESSAO (tela preta)

3\) Integrar → CAALPESMUT (tela preta, se aplicável) → CAEEINTGRS (tela laranja)

Concluído

SITUAÇÃO 2 — Servidor cedido retorna à PRF

1\) Cessionário libera matrícula → CDEXCADAST (102) (tela preta)

2\) Consultar liberação → CDCONVINC (tela preta)

3\) Registrar retorno → CARREXEREX (tela preta)

4\) Integrar → CAALPESMUT (tela preta, se aplicável) → CAEEINTGRS (tela laranja)

Concluído

CACODADORH — Relação de Dados Pessoais do RH

Tipo: Consulta  
Finalidade: Emitir relatório consolidado de dados pessoais, funcionais, bancários, acadêmicos e familiares do servidor.  
Sistema: SIAPE (Tela Laranja / e-SIAPE)  
Caminho: Órgão → SIAPECAD → Cadastro Detalhado Servidores → CACODADORH

Campos disponíveis para consulta

1\. Nome completo

2\. CPF

3\. Sexo

4\. Data de nascimento

5\. Grupo sanguíneo

6\. Nome do pai

7\. Nome da mãe

8\. Naturalidade

9\. UF de naturalidade

10\. Escolaridade (nível)

11\. Estado civil

12\. União estável

13\. Cor/origem étnica

14\. Pessoa com deficiência (sim/não)

15\. Quantidade de dependentes economicamente

16\. Situação nacional (brasileiro nato/naturalizado/estrangeiro)

17\. Nascido no estrangeiro (sim/não)

18\. Tipo de documento de identidade (RG, CPF, etc.)

19\. Número do RG

20\. Órgão expedidor do RG

21\. UF do RG

22\. Data de expedição do RG

23\. Número do título de eleitor

24\. UF do título de eleitor

25\. Zona eleitoral

26\. Seção eleitoral

27\. Data de emissão do título

28\. Número do certificado militar

29\. Órgão expedidor do certificado militar

30\. Série do certificado militar

31\. Carteira de trabalho (número)

32\. Série da carteira de trabalho

33\. UF da carteira de trabalho

34\. Indicação se é digital (sim/não)

35\. Número da carteira de motorista (CNH)

36\. Registro CNH

37\. UF da CNH

38\. Data de expedição CNH

39\. Categoria CNH

40\. Data da 1ª habilitação

41\. Validade da CNH

42\. Número do PIS/PASEP/NIT

43\. Número do passaporte

44\. Data do primeiro emprego

45\. Logradouro residencial

46\. Número do endereço

47\. Complemento

48\. Bairro

49\. Município

50\. UF

51\. País

52\. CEP

53\. Caixa postal

54\. DDD telefone fixo

55\. Número do telefone fixo

56\. Ramal

57\. DDD celular

58\. Número do celular

59\. Fax (DDD e número)

60\. E-mail pessoal (endereço eletrônico)

61\. Zip code (para uso internacional)

62\. Tipo de conta bancária (corrente/salário/outras)

63\. Indicação de conta judicial (sim/não)

64\. Banco (número e nome)

65\. Agência bancária

66\. Número da conta bancária

67\. Localização da agência (ex.: Setor Comercial Sul, Boa Vista)

68\. Conta de FGTS vinculada (sim/não)

69\. Banco/Agência do FGTS

70\. Número da conta FGTS

71\. Data de opção pelo FGTS

72\. Controle SIPE

73\. Matrícula SIAPECAD

74\. Matrícula SIAPE

75\. Data de ingresso no órgão

76\. Código da ocorrência de ingresso

77\. Descrição da ocorrência de ingresso

78\. Data de ingresso no serviço público

79\. Ocorrência de ingresso no serviço público

80\. Descrição da ocorrência no serviço público

81\. Data de ingresso no cargo atual

82\. Ocorrência de ingresso no cargo atual

83\. Pontuação de gratificação de desempenho

84\. Direito à assistência à saúde suplementar (sim/não)

85\. Direito a férias especiais (sim/não)

86\. Data e hora da última integração com SIAPE

87\. Integração pendente (sim/não)

88\. E-mail corporativo

89\. Código da formação (curso)

90\. Nome da formação

91\. Sequência da formação no cadastro

92\. Titulação (nível da formação)

93\. Estabelecimento de ensino

94\. Município da instituição

95\. País da instituição

96\. Ano de conclusão

97\. Carga horária

98\. Matrícula vinculada ao dependente

99\. Indicação de atualização via módulo dependente (sim/não)

100\. Quantidade de dependentes para imposto de renda

101\. Quantidade de dependentes para salário-família

102\. Nome do dependente

103\. Grau de parentesco

104\. Incidências/benefícios do dependente

105\. Período de vigência de cada benefício

106\. Tipos de benefícios (ex.: dedução IR, auxílio pré-escola, assistência à saúde suplementar, auxílio natalidade, acompanhamento de pessoa da família)

Observações

• Cada matrícula funcional é listada separadamente, inclusive contas bancárias, FGTS e formações associadas.  
• As informações refletem o espelho cadastral completo do servidor no SIAPECAD, utilizado para conferência e auditoria de dados pessoais.  
• Relatório pode ser exportado para PDF ou impresso diretamente do SIAPE.

# DRIVE DA DAPP

Endereço: [https://drive.google.com/drive/folders/0ABzmVBvAHErQUk9PVA](https://drive.google.com/drive/folders/0ABzmVBvAHErQUk9PVA)  
	repositório de legislação  
	repositório de análise de temas

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABKYAAALiCAIAAABsZUnxAACAAElEQVR4Xuy9ZbRdx5H+7SSeWZNkTf5hTxwzMzMzM8QYsxND4phBJplkZkiMMjMzxCzbMTPIIJkhpsSxdHUP7H6f1C9d0zpwda9ie4301vPhrD69u6urq6qrqzZOkgKBQCAQCAQCgUAgMJFiktaKQCAQCAQCgUAgEAhMLIiULxAIBAKBQCAQCAQmWkTKFwgEAoFAIBAIBAITLSLlCwQCgUAgEAgEAoGJFpHyBQKBQCAQCAQCgcBEi0j5AoFAIBAIBAKBQGCiRaR8gUAgEAgEAoFAIDDRIlK+QCAQCAQCgUAgEJhoESlfIBAIBAKBQCAQCEy0iJQvEAgEAoFAIBAIBCZaRMoXCAQCgUAgEAgEAhMtIuULBAKBQCAQCAQCgYkWkfIFAoFAIBAIBAKBwESLSPkCgUAgEAgEAoFAYKJFpHyBQCAQCAQCgUAgMNEiUr5AIBAIBAKBQCAQmGgRKV8gEAgEAoFAIBAITLSIlC8QCAQCgUAgEAgEJlpEyhcIBAKBQCAQCAQCEy0i5QsEAoFAIBAIBAKBiRaR8gUCgUAgEAgEAoHARItI+QKBQCAQCAQCgUBgokWkfIFAIBAIBAKBQCAw0SJSvkAgEAgEAoFAIBCYaBEpXyAQCAQCgUAgEAhMtIiULxAIBAKBQCAQCAQmWkTKFwgEAoFAIBAIBAITLSLlCwQCgUAgEAgEAoGJFpHyBQKBQCAQCAQCgcBEi0j5AoFAIBAIBAKBQGCiRaR8gUAgEAgEAoFAIDDRIlK+QCAQCAQCgUAgEJhoESlfIBAIBAKBQCAQCEy0iJQvEAgEAoFAIBAIBCZaRMoXCAQCgUAgEAgEAhMtIuULBAKBQCAQCAQCgYkWkfIFAoFAIBAIBAKBwESLSPkCgUAgEAgEAoFAYKJFpHyBQCAQCAQCgUAgMNEiUr5xo16v67enp6eqKmoo9Pb26rfZbNKAsn4bjUb5+49//IOCjqrj6NGj+asy7dspJBuiVqvpL7+qUQEiHIUHdVQ9XShASkdhoD/wQaHAiOUsqGFQDmkU/0tB0mgZlHLd4H9pj+h8CrR34jQbM2ZMSYdRSjpOv2WmSEk8+7gqwB4UkCRTUIFDLmfq2wcqR5ExQMeFD1Cukxo1alR5tARDMGUK1FB2HhAUw6WCcsu4AwKD9lPO5V83LTq6uGCmYSbtUiqHoAEDlepOeYLenXonrkpECjUq+Ss6/leHXESuLGTVLOzNGaYlXfyvFzqi5I0CNZQ76gvOvZJmqcv68rKkVJk1lh29fTPri+EYlyXgki8pN7L/ATAvsu6FSu0jrmRkNQXKLdRoLAoc1e8XX3xB5ZdffkmBZj6LAcm5GxjO2W73Ni3wBaIuriwXGg1E062Lo+1ydplQr0pvzK9P1i3QCf77cm4H4zoFr6GyVFAyjbgcmJ33SnmUusH/Jptjw5DalsxXhXY/NlB9cQjbc25B+Ve9aCk5l9aIfMpmDfM/5UocKDxCgFTKS8D14vJ3q+AvBQeaStk86AgFJOPNqOS33W+4U6LxP1m0xtQ3zEOWqnd+aF8OVLXt7xD0GilinEbCrJ0lxgoEAt8kIuUbB9gMKDcs1GgJkRsWlbrvw6Wmws9CoW5Zh7s53GvTXDkuNWUH2jBfnIpouG7RLX0h20JNUGBHZYtT7gYYYDgvcIjR4aoMOlPBkm8qHKUyGXuSBryxXTllgptyFNowOw992IcQBbP2QVMOreAQCqiDmjT2XtK0ZMMPeWUp8JRTkZTl7IfYRCHITMVJ3TIcmkEZfgTf8mnpbHREeRT6gCGo9yFoUM4FqZaS7yfGQ87wg5TY+GnTLLRJM/66ABmIX44yUMpREWV48L7NHM34ZBW5+lHnH5r1IvFDdHDro/ihhi1eiNDXZcugsEf7dpSHmv3QV9Mss1SQN6NNZXCWVCBlwpC8Vzd9MTUN4VKq5eDSJcDotex/YDvZcBQgyPR9FdCFowxKR4b2ZrUcTMNeqS8kQz1EaMZAfcu5G8pFSmHUqFE+Yh8o2atbDO05KpOi3E3OVEo7rhQ/Wk6fgk8cJv8dOXubFkDHy8wLuGRcFy3yqeWsiXl19M8+nWQxOjPqg5+Bgsk6Y4zuM0oD0Zd3SVkUpQejkt+SJnNkRhRcAtQ0iwSp/0B9lCm4Hv2QRi85dDZ842D0Zj5H5g2cDt7GGzPljn6DXliLDsnq0KObX4us0tj8eE3KYvQa9ndnzE/0pGKRdoQnuir4jFobBQKBrxOR8o0DDdv4//a3v6XsJZu2JYyx0734RK/3LqnYaaq88accDOG1vcAhp0bZNyG8vHv2dvgG0FucendS3dDCLTVNm5p7ZKfpca0KNYsgaUDLMXZWmI2cxuw0Kc/dp6lfD989oXJmmjnigR/gwnQkE6OPiPBhL2Uijbz981vlbY8GkNWhv//97/ytLOaGpjhs58EFwiEKLkOHhlaAwhy9V0dUOaak7JVeqOUYrtfOMphy/nc4F8V4YEByblr80Wsom3GINlW+dp2MOJotiXhH5IZJQMd/QSk01ylDiAEP/lx0KY9IkETjhl30cw5THsLblMJkgvwtOWlBNXB9ccing4FVXdZXygFTlfMiutCsXV/lEMlaKgWijevIufXuLUS8QVmASQblr4ekdKlZsleuX9emT3aMwQXrHX0gKgcELldqmiU/fcDFCLxLGdEiGfjvKOde82bNvPDVt/3SvXdBdGUNGA8594GmIXWyw2RGjp2LrCyNxctYqIxRnM9/LsVO/rmRLwe10P834cwD54RD/ddXZaJrWgaC+pLxjI0BiDfN8Bq2eGmJBmHDVQboUtb0E855e1/WOIdgj8bovSocSzmRkg5H/VAppdTdbzjlklTdsmhJABliHn6Ilkgv5bNFHfd3TnPThrFq+RxQR8A23ZPp1McNBALfGCLlGwdaHBO+2F0wqaB7Opw4zpGW3pg2auABsRPhEJXJHG5l23N97Pu1oJzyeWi60IaOYoYCvpUu9G0HLVM+9cjfcvNIxdw5yui+hZT7k/9lV+A32fUZ5kW+6qIowybOOvs0K9s8tCUwd3IJxfoM6mc02bRK7fh2AjWG4JegoZyFM9+bLw2VcvZNumlRQksX2rsQIM6GV87L23QDE0Q+1DCEtCA6zIWxvEuVw1M01Yd+u2GgciZqZDjvyF86lnIum3E0ZTmUUUijiIz9L6KuFxdaaUAZUqDHQFnslaJo5NPYEGzp6OLqtTMXUK4Xt0b3DWfV2RunvlIObqp8ZT51WV8NOwfhzHhE5fxXY+uLypS9ATVQrhmcVZ91OdNSbo18YbDXcoMye/dfuvMXxirTqRs/DWrmTEp5joecu8FJ9VpSjVRbG2U0DYjFJ8LfmtkznPuC7UPOjIJISyHUszNPRVifviI59wEYa9FsMjv0/KeRtwCfhffFDjna0T83itukm3Y+xQf6qoD0UuHHAKy6QPjbTV90QQ61YhXQF734eVKmSSX0ffVxFJm4Z/ND/Uczb0BV3r59uHKlp7xevHFlG0czZ6SN4oI5vq4a+3wTE2e+jS5+w10xwmmMnUOWEyyXlVfCDzRpDG+1vL+nPJeSE+/eDrqgR6bA39Z2gUDg60SkfOMA+03Kd194WjXGTn2xAzXsgRkcX/uGTfuquNaXzIHiK92BprzJ+V9vr0Bc4+IlUw4+UqbsjRt5q3bn24cXLveh0l8zKGPRoNfQwiS9PGph12kWty2VvDlU6U8WqfEouy5R7jfIxPuS13lfCjTzAhPvzfEfO7e3bOStrm7wegJxJuX1f//73z///HNmVy82UY761JiCq1W9Umapli+IlVt+N/hRhFDZvu4xCgJh6/XIkjZ+tJxRPzF+ckYapa0ywVIRdET+VXEZkEk1Dfyli7ehvsp3RVKGpgu/ZlE4sqWmUVzo80CNGmgCN4DK4gyfHaNDmV7lKuiIsi/oW1/eHk4oMyh/6cKkvHEtR2BMqpu+Sm7JT1K+E49KB72q/DQOlbXiPkBQyjZlnhvF3bDlYmE4Z4CzNrRs5Ky7aeqrBi7njqCXX4EfY3mIT6cdPkQjX+hokaFPH5/ZTc71nKgjDYQgNnyytPTZfVVy7gNOvCrgdoj9sHDcZWEY5dBOpESVvVll4sLRMa+vCoxbtfmxgeoLoXkGCJrFWT86+u05EGwWt7NC0OnDQGnkA0WzcI/l7PyvQxt6WYMGvVwaQN1AGSOhZSOf0PGOLX6jPOToset71IsHJIxYyim3d+xt29+/MFB2NZWG3RGffPJJyhbluggEAt8YIuXrF3BSuEV3jgQ0VVsuh/trFvec8ItjrRXXTHrs8QnfpRgFtw5ZeVU2gCrfE1IVd0+xhbPzscfTwPeMdt9dogxHei1LccpizJn0SjVmB01FMAG3+G44bBhS3m7/uWXZKN4XrqikcT2nB8SOFJw3z6uRLVeiGjm/hZNSBSnv3IRB5b7iok55XpAlY+eQ7510H2234dGYnY8C+oI4bThKDTPqI3prYTiNHVpV+bJYqcpSJo3iqYwBYTzkXIaPyCFlJcIeoWEpZyJyb09jFxflptkqM3VqPXZDZi3fPFwvzh+jDrrQvgRt+C3v/0w5fmWaYwx0rxeX3Kvi7seOGKi+mmOfvmGpOpH29eWrr6d4VJUFlbroq3fsm719UhSaY/sfn5oG8l5S3Jh8T6ybfd1uCETpAHWkPKnKznwlG3GU3WbpzTwEr+eFQLn/cu4G+iaz0tH5UoYrug+gF58mDjOZnBFOzU7T9CFnlEW9K50ZIQ3XplsyDf4dOXtlC9yiHD4iBeh7sx47UwknMFnPzrajf7Z1+c+jqLJme0T7oOONalx+rJ/68vZjDDRDKalwL7Rpju15MMjUtvQ4WhLvP5xtBI5hYAPuhdCLa4Fftz26OMGe4iFGtxM3DzcbZ77Fb3CIURrF2bFkZzarfJ2tPFOQMj+wAT/8RXq1sff3pp20pcChkv8WaAlApKftkdFAIPCNIVK+caDKF6bkKK+77rr9DX/+85/l41577bVk7hgn/tRTT918882PP/74TTfddOedd6pw//33v/zyyyn7XOHRRx998MEHVX+3gSHYLXz7eeKJJzTQvffeq5Zq8/DDD7/11lt+VE5ZA91+++333XffsGHDHjQ88MADjz322JVXXgnD9eJGL4boCHEufjSWKIhbjSjGPvjgA7YTdnoNccMNN2i+annrrbc+9NBDb7/9NhuJny9k29DvPffcc+ihhx555JEihU93z+5/RfD444+XDC+77LL33nvvs88+k3ibtg1/8sknmojGUhsm+Nxzz9HRQwQKGveOO+7QWEOGDJGIYIALsGr/+eefJ9taREfMHHjggVdfffXfDe+//36y7UfQlDWWeG6XM9vwI488IpFq4k8//TT1zzzzjCrhjWBIfSUT1Uh0t912m7QwfPjwv/71r6lTcFbCt1gmqLmLAdmPCN54442i+cYbb3BO1Df+559/XqNrUlKZjESFgl5/MVA5q8EhhxzSImfaSHfJzECcH3vssQcddNAVV1wh4UvOLgEJRGOJiKamslp6POEDqV5H1Uyz068k8Je//EWVMryUkyUai7K0JvvZc889L7nkEon6nXfe+fDDDwn1RFNyQyOi4+srmeEx7uuvv6756pAWqUbRiBzyBt0wHvqSBYr+9ddfrzaajn5lbN3Wlw75itYcr732Woh00xfBFgFf0+IwGafWXTf/k8xBqUZsqxn+RwVR09CycIbD7DWQGFYDjUt3Zt1jlxOlYtWrl1pqIFF44YUXpIVU5DzPPvusiIvOQOXcDe7TJLT55ptPvrfv9ZVy8lO3DFMM3HLLLZKtuJUQxL8KWtrjlDO+vVZE6lqGOoTRqpkKIvjSSy+l7Mm/EjnTrB2+WdDy448/xg5FQZaGHaoyFfdAer4nBrSQDz/8cM2R7vx6Qb+ic9xxxx188MFDhw7VKv7oo4+4HESzrwTd/NiA9CW4M5fwTznlFO0pZ5xxhuYuN85KHGUv+FFfUVDfu+66S4VkSsS/sRJlvTJRjSXiWjUq+BD9B3oRJxpCOnWPp4nIipKN9e6776pGs/7000/pJTa0Up588knthuIBvctIRESqlNlIZfplCiKllvTSXx2S5XTzG5o7U5Z50Fj0JW33Y4KcoTqKuFZ0ZSj50XDIp+P+ztVg2cYou6+hMXa+2g2a4KyzzirF0d1NNBAIfDOIlK9f0Bay/PLL77rrrtdcc4087LbbbquwY9111y19lmLQI4444oADDlhxxRXXX399BcoKgi+//HLfv7XpKjLWbrrzzjvPMsss8n2+GVf52p1CWG3JiyyyyI477qi4VrvvTjvtNP/888vVsktpxMMOO2yppZbaaKONBg0aNHjwYBHUWEpspphiipTDOxp7YN0OHVL0qb4LLbTQlltuKc733XdfjbjggguqTFgvj699dO2119ZYmpeG0IwWWGCB7bbbDs6b+U4PbbRrrrnmr3/9a205ijzUYKWVVtIORxsiBv1V5dZbb33RRRcpO9KMllhiCfXSX/YhbYdbbLHFMssss8ceeyis32effTT00ksvPWLEiHpxD6HYXm211dRSsbLG2mqrrdZZZx1lj6mIC5WXLrvssptuuqmSPW1pIjXHHHOoy5lnnsnOpAhVlQsvvLDkrOGkF8lZU5NsoaAZSarTTTedZn3qqacm264UWOy3334zzDCDfkfbi8vURkS22WYbyeeYY45RY81IbGuyfe9nHr8iH23wsgrpQhrRnipq4l90Ro4ciYSFSy+9VBqXABdddFEpQqyi5YFiQHKWTm8wIGfXqetdOpV5yPgVWGj688wzzyabbHL66aej06uuukomqvUi+jIwmRbLAS3U7XS75qvJuj1raqIjw5PwFc95S/GjZbXBBhtIiVqDWhqSgySmvzAsypxNkCqlI2mcleWxiFhSHKn5yj61gvbaay9FwOVllj7kOR76knA0F61lyVCLWlOTwLutL9HRilB7CUHUpplmGvcbHfUld6TUIpkkiZW1Fg4wdPQ/stW99957ww03POqoo1Qvra266qriSgxoIhIFAZ9IaTri5A9/+INkKM9DLtcsbv1SRCgjXGyxxURQWtCvbF4EX331VQJftVS8q/luvPHGA5VzNzBNsXHiiSfKX1HjttoRvgAVmGqxrL766vLYko8kI2nj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cBIUzAwUPfb5E8khZX/SRwiecojfsDdsycY0BZmcFgu6kBFKVpK25Na0K0gPPvigOBR9sepylkw8ueI6uaam6WhqEohMVI2lHeVvPD8MxilnKV38iAhylsHIo2pbEU0ZzK677uqkWtDRDv/7v/9b60WcaFKao0JqXn2kSREmir4q5cfknzm509E/y1qkNbXUHLWW55xzTk5vpewQkkWfF1544XcM48xO2yGeJStNXJL/6U9/KscrjYh5yVAFXmIpOSuX0+JSm276glSy++q1q4pbOXAtCold2xB3jkjOOiT/LAp4CW272nylXNXL58hpiIgmK+JSt1QvNYk3tZc/l2/UysWqU87Mu0FSkm+Ue1nG3nMmMWodiZToaLOTeOXotFQ1tBaO5rvddts187U4ebPvf//7nmknO1fLrEVE60tE9BdHVNnTJRKL7ETrTgVZo1pq1jIAzUIqltI1lkQhNuSQZX48I9pjePrppzVThSsSteYoLchXiJ9Gzjbldb/3ve817bwe2tdSklWIuIQv+xEzEh32U+W4y5dJR4y2m2toI59w0003VXaOCU/IWGns8Mz/lnRK9H20//i/TKfKEW/qX7waCPSNCSnlw/pTcSrIFwNHW8odkXIEXBm1lv2sHaOKV1cr+tFud+65577wwgvu5hr2zIOaKdb54IMP3njjjZEjR3700UdvvfWWdnFSO/lfFd555x1VqoET17jvvvuu2r/88stEDJqaCto83n//fW1OGogtWZ76S3sVgcqvvPKK6Cg5fPPNNxXPaRT9VaXopLG/6bTzzjt/+9vf5uEHhqvsziKfL31FZMSIESPtpSwM4e88VAMxDDM4aFVqmsm2Ja4DsA/pV42VbMibixphqHj26xKiWberUkpEr7nmmmuvvZYNgF8Uoexa85I09Mub7lO+etbI59dRnLhVOHLFFVe8/fbbvWM/Y+PUxOftt99+3nnn3XPPPexPaI14SExKaH3ImewxWR5+kcHfxOi7o6Qnq1C92JDSJQF/GSOxL6REXHvqpJNOKl249fbaRRsP3KVNMSyWNJysBVnREog+tqEGaqb2Uo3G1e+r9mZ8j+x333136Z24J2Wx+FH9Vffhw4dLzvr151HHQ87JRCpLkIQVcvmnkxsWZ4uOTEsMw6TG0gQlK2lZawFzFRDgGwZiMk1QbaQgdUdxhO+VhTuXXXaZdCGunnrqKSiojTpqFNFR99IMVCNqGppkVatDGlelatA+YhQ/vBcEiPktttjiu9/9Lne1MeuO+lJfidHfJprGFk77+nLbwBTFmxgWG68ZREdkYY+F3G1dUO9v8U22HjWLFv9DCipu/R22OipBqaUyUo2F9kfbux80roirRgVPLTRrjc5k/b3qrxrEpPjBGzCdUfZhNNyyemkgNUPOGhe9l3LuP6Cf7Cthfl23D2AwshYKGp3FIn4kGc1RM8Ibly+L11ExKW+genSKNmnjuhtp0FwkKC1J9cK6NPd+yhkhq4HPS4U3DSLoj+N2RIsdaiCJV8mweBYbrji3Q3ewsh/5Zy1SzRF3Nzo/5l2z6/NNS0Kuu+66q6++usU/AyxcXeRXb7nlFmd+QMDIxaoWvoxBzGC0UocO1eyKNPamo33oq8dOhCV7Alap72mnnaadRWUko0MaQr00ysixHxsTEZGSatidWTgqa71oRC1VFIGzgpT/dgPyFBEJWdyKDdEUKWmTQxiPXJaUxayTZdrYJ+/b1MTRQrIH3sS22BBBFZh13d5IxFEdGmlrSnMRqyrz6z5BbXRUY2GT7v9lXSKCZ2AVi20YqPL9mf46zSpfSxdXkqS8rvZ3DY3ogNs8M+0ILEfEZV0LLLBAI5+s970Jp0F57K7/QlWg9ViBlgbt7f+XygRCB4FU/YtXA4G+McGkfFh5ZQ4I0+/mGlLRuGVtsGzq+eEu9zJ9L6FaBjsifq1mXwOjxluSTY22CyDUyLdS9qgRh96wt27QxidSt4s/NXuIy71n0256cYJeUDNoegrBoV578v5LuzDyi1/8YqONNkoWGZQxHL0Yl16+TZZSZXchTKnbI/su9tEGb0NfL9Cmlm++9S6jijcZOtvaPNydeRcKpeh68stI+IsYnQi61hC9hjH5Awm0ZFCST+BH+5DzGLvayRDlXFBiZW/v5BDde/MdpF6ZjDGGmGqqqXg6DttLxdCeZDplxvrCPoFAM36r/MYRZuQ6RcJ1uydT5SmnnHLDDTeEgo9CF0Zv5B23bicO4XlAcq4bnGF0RxsXY8NemwHNylSMcXpL3sIKJ73Ft0OoQV9NC4Ma2aQh6zLUIZe/CyeZZIib/2EvwYMr4R928ZYuzIW+8DPG3osA89NMM81aa61Vmaj70Bc1gGy/1x50qXdZXz5WymuHRcFAqXARyUZEWR3XBfw07GbRmt11zLxKMx6VX7OUTImlHgnaGsVDnskkwBSSiY72XuNiL827MnsYnV8YSDPaUKDG+6ZxXTDpCBjQdJTb8C5K56EjEBfACEn/sJOmLXZXX49dHq8ZqMEU4RMhIO2aOWfmRQMmhbrp3lHOTftkNpUpe2kkJhuu8n25jNhiVy1ot0PsLeVVgNkwa2/sU3MjdCb522PwZswR/qviyXM3J1fugMDUUAHGk7L0KPfmt1Jjdd30BT9OAbab9sA2bdAglbSRl3PFQaqeb2Jv2CJyxY2xc7hoB8pQ4LcbEGBL2RdRKm41Z16glu8i9uVDAYE087tzoEmDv9lLlZ0OM9VArrvRtgu4THACrvdkE/cVnYrTxD1m2xxiXDd7F7hLCR58E2Q60OkIpr/qqqvyGgInyC/dUUTfdAaEdpW5zQwI7V2+GTpVjnir4nJfH+0Dgb4xwaR8+Cb3R6lwFh3Rcqj8+79EDX1vXTgm955UuvN150hNleO2VJCl0M421OqWJTbzbe7OHusc9+eVBA0fffSR70YcJVCjFy2Tedhpp52W91umYkdxl+3tGYsrD5UFxNSzG7XIp5E/RdiT3wYOe1/a15Cq/HoY9oNk43rYnUyGjRzrjMnnOB1IADrJKCPYmqGR94OGbYej7V4RUWBol6dT67HMmWZOkKF7LS5Hbh3lzF+fJmBSjbzXJpPGmJyl09eJNIrcRhKYYoop3nvvPW2ucFgOl4zt8r5KeKPM+V0aw20qgh6a+VEOaaznnnuOBuzcaWy9uz0znXqO5PovZ8DoiIXgwNmmPuVNixraVPbskzPz8ccfww8tm/a4UZVf71nL0QYgcE/GailqOnpNOagvT3oxO3qRFsIPEQkUNIpSvrfeeksNGK4PfWEYPvHyMjs8wBvri9Gh6WIvgajHuS4a2fAwFVeKS9KFBg8wmYw9b+wzwpw8E6NLOV/gNF3XcNsoziDAKkvemUG2dbvfjPJ4wKdw4oknlpfQu2FM/gxDyslzGttDliYEOMoUaMAQmGs5HIprGmjZTzk38g0CqVANfylXfb4Jgwb+F2rImaEpJ7v25daS8lk/teHyTr04JcF5EHphOTDQa+fOqC/RwsOAgHBq2Y2MtjMFJZ/MosrnZbrpq8qnmWCGJdNCvG7ry8XrbDsRd+Ou2V7bFyizVCnXOm2FLfCjJQN+tNdO6zA7929VXhqgkTejVKiPeuYrIn6Rk2Y+KNJw5mmfCmYYvWZbFWX3+anYUGiZxj7v0DD3Dm8sPb/Kx7yQlTPcEZi9Fm+LcNqlWmWUZf6213ihaeAvZSr/t/XYJxrK+v+zdCiXaBdXINB/TDApX7lgarYTj7GEgbVEfbO4fOG9/CgNRtnDxzg+2riX7Ia6oSquIaR8ecGDLXaXVFDzxrV8z8wYA6M3DHULrKGQsqtloJSZp8YPsfE08wUThm7mfaLHTuY1ck7FduLbXjNLyUdkF+GXGirZJ6hsWrSqMrFCymSTDU1LOGFGmcz/DsehZE7fBehRRTIRfWmPP3n3Wj73SV+Xaq+h7AhlyKKmer4gSRdkTtBW6pqWqYucXUS08YEYwo2nDNmrfInvS3ukMBXbMF18dDSY8sSpRCAQdDn46GjZRdEszv4iZ5ohFjcG2Chn53LwX5/pgORM2s8o1LgYWZh0aeSQlAZ1Q8o89+Yz+s3i9DxycGlTGG0X6LxvI6+dWv4QGcz3WvxBQgIpFxcTccmnPJfyL8PBgF9jTHl2qZO+6OJmUDJPobdtfaUsNMSS7FaruuWBnpkgnKZdR+q4LhBgyrquzGmMtptp+evmUTP/U+UsMWUmkWejcJisay6GjMpXOTiDw8qtW6LrWiunhi4QL9P32YEWOXt9/wGfLmGXQB9wb8/oksMYwyh7vSptONpr6Y1LA0NKNigNmBQS+7u9qJnuUGYUenWUM8Khi8u5mT/ihxhRujfrCFe6O2FGgYgvEJTSY1/LaBro6w2SyRA4WV+DKS98uGKyY/IZOuboMhkQXOyN4jRBMpa+tDtiqhwHJxuxm75Yhi6EMnEalS93uwa/tMuhTJbukG3m9LJu4QQsIc8xtn3TpT/nF8odp1yt/OItsTEOoYKUByKRo7JWOJmGPSJYtqeMi8Oues3Z+mRhAwpYRbO4jwN7SIVv7DV4X8rI0/+6wZT7XTKCVT7NXd4g3RHIORWbps+Xv2yRzRykYQZNM7Ny+nSkkgYUymY08EpvRnkCouMezIXWtx0GAn1jgkn5KgPlRx55hG/QPfDAA/fdd9/999//gEHle++998EHH/zLX/6ioypQQ5v7DGo2bNgwdVebdsrt6M1vNUy2ICuLpfB03gb3yu1nzZyMVbZT4g0B7r6RQ1gapOxqawYoNPMFJY56DS4+FW66njMBp0/B3Q3N/J4ir1ehvBWEAjsH7h7Pwq9PlkNjLLh0ZpKN4pfy4DMVlzvcSdGl3KfpAigz1picz5f7AV6vKi6lJhsatr0l0sBLMnRvDuCSSR5RQ7ybnJu2TVY5f+DXe0HqM3sxDx1T5r9p6iB2YXS3n1SEI64ImEnGpEumlq/yVcV39mrZPKh3dZNhVgbo+K/rvZQz6Cm+o1hKr/9ydgMgUamKTDhlPbq4YBjxpmyrzRybjs63BcKS6eFfDKtBed3MZ+1G5UwyOr9uqPAMTXQNn/Xinq6GncN2Afbkz8pxyMt96KuysJIGpEyNLuurmU+uu2XSAMAATGL/qcu6gAIFLITYEZHW83WSdg02c/BBJYz5NL0lDVyJLQ1SXmW0oUEq0o+ygfsTJlXlqHRAqOW8yG2sPH/Ujno+BwdLSNvHhRn8ZIsh8TvKzozQ3kckcKd7M1+LRqpullBolzNaqxef4kjGGxp0uTXzDZnd0MwxInbILNiA0DhcNYoHB5Ix7F6onpdtR//cyDdjp2K+Kcu/MjgPMD8gwCQ8NGxN+cJ3MXIojc1Yu76ct96cJ5ee1p0/k0VWvuRTlnnJD9Ohfd0AKUZnO/gX9S5w18EyZCLuwBEdM02FKyuXG4M2zW3SDHCqhZrSUEHDULP1DgXmxVFsz7tAuTLTLW82djt3/++HmpZj++hojeE4Woq0Gxg0GWVk0pNfZEUDhWQKzBSeeVxH2HavhXAK5x42tMR1tOFXHWnjFLyNlycsOh6vKuhFSqXEAoGBYsJL+eRcjj766EMOOeTggw/ef//99Tt48GD9PfTQQ1U+6KCDDjvsMDU44ogjqDnwwANVebCBwqBBg3TohBNOGJXPHZbeswU06LErCe7RquKKn/tHvGqVb0hLRZg42pBJ/ms43HoqQjefY/tvygGB1/iG5J69afC/7sE9CEh5t2NEqLnTxwvTwHd9Rumx9AD22P84yiHvlQqnXw5XFfErNWUvJFMV0Sqju/SceItAmoVGysZVkUunLLfK9OKkGhY6OHv+W7bnb6l0OvLXrwJ5RMugtHfivk83iqDZ93X+AtqjFw55MMRfGCg39d4c6zQMHE3ZJLBDb8AvwmGvpbEbkk+tP3Jm/2Zcp9DMDzQ2sx0SpXlfN54xY9+LSBufb0s95TR2bERlKSKfo4/unKMFH9G7u6iRDO3pwuil0r07oBIVIIHy1ym3rC8qaWPC+yfQCM1SsSIQV7PTuigZS1k+1JOB+99k2VH7TKviuVAOVWYb0KQAWR/L5VauX9owHAXsyq3d6beUBwpGTxb+dlxBJTiEnSOxhl18Y2FCilNOLueamTTtIeIS4BAE69ldow66UNO3nJ1IKvyDm6WLsaXcDigD/qbchRERDjXujujrZuYGQy9fj9CkWTlNZs3RKi98SA0IznZpCZxwSTYXjJ/hmEs3fTVNpy3SqPKJJxpAql5kdG6WjOvE3ZemQkrQb5gZ0Kwb/LocozTyBTFGT4Xf9inQ3hXn7toHch2NyicKaQM1ejn9NHZI4NN3mi3EaewTRIDOdsqnVEpxpcJgfFLUl+6rDzi3zp5PRHNUSKbATOHZwYbBhoMtbFNBcd0Qgwr6SyznbRQBqqDuRxpUICz0NjSb4OgI++23nzoef/zx/YlXA4G+McGkfIFAIBAIBAKBQCAQGCgi5QsEAoFAIBAIBAKBiRaR8gUCgUAgEAgEAoHARItI+QKBQCAQCAQCgUBgokWkfIFAIBAIBAKBQCAw0SJSvkAgEAgEAoFAIBCYaBEpXyAQCAQCgUAgEAhMtIiULxAIBAKBQCAQCAQmWkwwKV/TPq/MB0P9q6l8kvKLL77gC5X+ufN68d3YlL8Tyld0qSwP8UlQ/9aqf3Xavy7qZP0Tyb32SWh4SPmzxeWI7WCUspCKLykPCHxfOGVOIMLHTGngX4Nt5s/yIjf/VCtfWXUZMmXvzldfXVb+XWCa+Vd6+ctY5Wfc+UY5fX2C/PW58xcxurL4Wi6s0reybwTTMhXfL/Y2ACEwO/2Wn4VVM/FT5W8ip/wl3GTzcoF8rWAUxAifpTFwtGlwfqpCs+VHkzvKWb2QjyuFBi2iQyylRsbP/BwuZ3jwcsrTYb007UvizfypdDry1+VQlqHg+vUvGiMHX560b9j3talRmQ8iu8X6HOUiKIgOcnMKNCvNSS1ZC/7FW46WyycZTf56s4Yhjb3Gvz642BER35VGki1OzE3dP+YLkGppCUzcHVo7nWb+zH0q5uu2nWzu/rcx9sfcvaV3dxNq2qpUTa99sRoBls6ZZlXbunDOW5Q4HkCPfDad6adCyC4lNfPPhTvPKSudxuUaZ47wBs/e3j+xnQrD9u2GZsg85Q+RwwPjungDgUAgEBgnJpiUj01O+6Lv8WyEZeJBmV+2WJXZFLVf+mbJX4/8PGLjKHs2kZAHzSo0DUR7tGQz9jij1xKYTKkDGpbDpBy4eOwyIBCT6Re2X3nlleHDh3u4UFluk3LMrb/XX3/9nnvuOWjQoBtuuGGMwVM7puBkaxbn+RAeeQCXUplQ0f3jjz9OFuWQkFBZNxA5iSC99HvhhRcedthhBx544COPPJKyOvjVEPR99NFHBw8evMceezz77LMpR9gecJPCXXTRRYcccsh+++03bNgwKLjuwK233nr33XfrqKjdf//9d955J7Mrg1dv/HUD2bYHgigOthE4cnYz+9vf/qbfzz//PHWRcyoSDGpKcUkmpR4hDiccVRcX+4DgWiZEfvXVV1944QVIuTb9VzXPP//8XnvtJZU99dRTGEa5kL0sai2Bvh8SqXvuuefhhx++66677rvvPun3z3/+s1t7r6UKybLiG2+8UYYhm9egGvqTTz6Bmpsu0bP++sJhvSRjADqSvJbMvgbRgUnSPBrIqG655Zabb7753nvvFVcys9tuu23kyJHQh+zXCqaDhLGTXkutmZS4/eyzz1I+NZCy/QBJw1PWuqUuPXYiqVRKRzooV5XYJKJoWnrvulbBB03FqSJfoeqODdPRbQa4cVI5znVRN9BlvO2ZsT799FP+Yh7JiDds38E8/PQik+rIz/vvv1/ZCTjPDOv5rJZLgCFc2l6PKDQFtFM625TXwocffpgyY8kk4zQDgUAgEOiGCSbl89iC3yeeeOL444/fddddlRsojtTv7bffzhZIDNGw/Oqss85S5KejRx111B//+EenALRZXnPNNUo/lIQcfvjhiu3233//Y489Vn8PPvhgJQwMql/1VTNV6qhosutDypMHgpJuKGPZ6t++wPLMM8+ImRlnnHHyySe/7LLLko2uiUP/o48+0q+iz3nnnVczUtZ3xx13bLnllttssw2Rh0Z/7LHHDjrooL333jvZRGqGZLwdcMABhx56KDmSIrPTTz9dRI444ghVnnvuuYzluYoKxxxzjIRz9NFHS84ieOKJJyr2hSyRE5MVqQUWWGCXXXZRlHz11Vcvu+yyf/rTn3SUOCnl2O6SSy6ZeeaZL7/88ptuumn++edXgaMwqaEVZi233HK77767gn7RUVka0SGCSBh77rnnZp11Vk1QjO2zzz7iXwbwzjvvNPOVtB5DaQxfE8SV0iGxoQxWmhLzioYlRvEjDUoUhIMkCQocjzvuuHXWWWezzTaTyf31r3+Fw6bF3x3l7JGiCuTtZ5xxhuZ75JFHal1IMqnIpVkXmvh4xMTtENmXXnpJ1jKD4eKLL6beWWpaJqayWFp44YVlh9ddd93000+PxaKLMXZSxtcFK8vpACpffPHFueaaS1OTWjWolr+koWyEuWA8iraXWGIJ2YaMR8MtueSSp512GpQxwoZdGHG9+4iVZQtYhf5+8MEHorPbbrspexSdpZZaSsP5mlVLiXrqqaeW09C6GDJkiNQhrrTEfv/7338lsh0nXKHJbF6cSCZyXFpTNcOpp56qSnm/k046SUboEn7vvfckw/XWW2/jjTeWLb311lvKnFN2IOqlufRBJ5kMzz77bNaUZq0GsNTM57+kFGl8zz33PNgganKbStcx8iqfSlNWo5xZApStqhlORkZ70UUXoXTxA0G5iG7rom6XrzG5FvsZKOQ2TznlFM1UdnWE4YQTTnj66adH2aVRZoeZaYIS3QYbbLDppptq+koUfWg1kz1IF/rVgpUwRVPr1NdC3a4zayHILx1mwEFJRHKw7DtYGspVYwlzlVVWWXfddXGYDMS5icryw3IWgUAgEAh0xISU8lXFKVLFmtogFe5feOGFChGUJyiXUAr00EMPsV8SJSuj01Ft4Ysuuugss8xCzOGhmzbLP/zhD9qeFRkrCt9iiy223nrroUOHnnnmmUomRd9Po1555ZXKPbQxK4hULkEsAjP14rY6DyX7QC3fZNXIFw0GBA2hIOD8889XJKrupxsYF245v64hhg0b9vjjjzfyJR2Nu8kmmyj3G2UXPJ9//vnVVltt+eWXVwhVXghS4L700ksvs8wyDz74YLIo6qqrrrr00ksVwSy44ILzzTcf57MJnSno6Kqrrqp88pxzzpGgFA5uv/32Cy20kFKsZMkVqYjCNZFKOTpXpSLpp556inHrdtJaUdc000yTcv6syHuqqaZSZZVvW1Wb3/72t+edd15JR9G5ZkokVLd71RSTKUD08KiZ7wpOxWWcfyc67D807vDhwxUd7rDDDsqiqbz99tt33nnn9ddfXwGls/3mm28qRVd498ILLyi9USi52GKLPfvss9Jyr10Q7ihnaeq1115zk9ZMlQnLhhWmS1/KsdEX4Xtm6p+oG+jiFysGBCUAWhQKXjWEloySIjfsykJkVPb6669r9SlMT1nm0003nXKzNPbVsF67QkV32TBZAWC5SZsyV5+Fr52mXSmCsixcrqBpmQCWsPjii0uebq61fCnbb/X0WByUdOgFHbkaKSsZe3SUN6gMVKqg9JL8pz9+4N8HqUgy+ciDTTnllHILUkfTkhMlvfKNSrDl2dSybmcEPv7445lmmklTe/XVV9944w2lEHPMMYdMCGlLoarRApT9dKOTTIaXG+RX55lnHilX6xSWEK9+1WWNNdZQAiyW5IG1YGX/ytg/+eQTc5P/lI+oyUfpkFyQHK8MW0Oo41/+8peS2ogRI+R2uq0LWqa88NO/Yc8yUXG74oor7rfffrJn2JbXWmuttXA1cP7222/PPffc0vXLL78slk4++WT5H/GjVYDVXXDBBauvvrryf1GTO9U6/c1vfiMhjxw5spmv7Gn5n3jiiZqU1rL2Hc293HeQj5SFT1CyLWVpy1N7yVCu21Xv3n6smQQCgUAg0IYJJuVLOXBnX9eG98ADD2iDTLbhsUcqZCFD8Ed6KkvMtCsrJDrkkEO0ZVZ2Ot9DQIUajz32GPQVTGh7pnzbbbcpXiHoIchT+YQTTtCufNBBB3HxZEy+y5Rmqc8LfQSFvfkmHMqtjfoBupO2JeNZgUU935o1xu6y681X4Tw8JTK47LLLyjhVkY0EotwsFZcLFKwo8FIm7JEZnB911FGqVzhSXiz16euo8hkqoaOIUHlO3S7jULnbbruRuqACHbrxxhsHDRoEkWTJoTQl8fqtiTokrSkKdFmpctttt02FctVG2e8+++zDFJJFwB9++KFCNycCY6Psdj4G6snXHr8BiIfDDjvs2muv/fzzz5GGWFVcu91226XiEazZZ59dEa2LS0J49NFHFZFz3Sl1kbNiStkwCpWWdYib04444ghFk0r8FMRjw1DozY+hUiNOyuSq/xhjt7qJSQxSo0hNKdsnSwM+Tz/9dGmHMqPvvvvusiXmRTO/UNPIz9EB2otJSUnSW3LJJfkLz3WDm7oKWrN0bOSbqK+44grZPJOlJmVr90VUtytFTQvHa3atTxF5MnFhP+qotaNZsH4b9vgW447JZxBUs+yyy7711lu4Fwb6WkEewlw0unKDlgZiW8lJ6Wc23njju+66q2nZOLOT99CSd4sSFlxwwRbX1EIHKamgVOSUU07R73HHHeerD1ejNscee+yVV16JfpGV1vv6669PGe2jEVGWX5W5Ns2RipRsGKlqjsr3Hn/88W7rAgtBKclUOX72zHAaepdddtGOAGMNO/ug2Wn9MmsRlyiUqdbytWJx+Mgjj4gfJIAVKZ275ZZbYCzZZK+66qpNNtnEpSRFqAHlct+59dZb2XdwlXLOGstPyYnaM888M+ecc/LXLc3JBgKBQCDQDRNSysc2TICorU574TbbbNNrFwcIR7Qj3nfffYoqaO9bsvZIokPt1k4k2Y7+61//Wht2r2HIkCGKPBqGe+65R2lPKnZT0ZlrrrmICBUVUelhEIUycmoBez949913FfIOHTqUG6UGhPIRRPF52mmnKWhL+YbGlNMwQFTk10CULCnqoq9YVbql/EERxs0330x7xVLK0x5++OHtt98+5bPalWGBBRYQt4oUl1tuOfHgARbhiIJ4xcTIyp93mn/++Zl1PV8IZWgKonz88ceXwaIOrb322iNHjoRhgsUHH3xw00039SnUi3P59FK9gk7FWI3iUcn3339/tdVWow3WgigUL8Jwvbid8msFoeGRRx559dVXp0KkSvm23HJLn5T4V3ILb+Q/tDzwwAMvuOCC0YbUSc7CVFNNhQGnYo1IX8qR1EZ5iF8T8PwEvPfee+ca/N7a/sPtDVYJW3st/kbsro4NN9zwlVdewWAQ+LPPPiudwjD1dFGiLiJnnXWW2GaOVXFhX2JZaaWVGnbVurJb7DjkcmC4UXZJGYKq0exOOOGEctYwJmPWQEozuAvaeXY60Keseq1Wmau39GbUqCy7nWeeeZIJpFyDXxP+6aRsIlXO5+WdenMi2mOX1sXJLLPMkmwu+I011lhjxIgRqTjlpEOSj0tbpGabbbaU9dtOx2enQ0rGdFSSXGyxxegOY1A+9NBDZatw2LSzdQ3LYeo5K2vmExAqy4+dccYZTCplaIjjDH2sC1d0Mns+zzAe9owSVdhqq60eeuihlFduMqeh1QTPYmbw4MGIy92g/oqfSy65RC2Z+3777XfhhRdC0J2wFOR/tXO99NJL9NW+I1NsWgZ+9913K+dMNiOl06LDktFf7RoUDjjggMMPP5y5I9UUCAQCgcC4MMGkfI3i7WQEcI899tgOO+yQ8oler9fO2rC4kL+KA1ZffXVtz/r7q1/96oUXXkjFaf5LL730jTfegKwyh4svvrhh6cFrr712zTXXePgivPXWW+utt57oqNfGG2/MHYlELSlv5H0ADtVYEZLC0O985zvf+ta3/ORu/0FYlmxoRSEK1+A52aT8Lj4u9RATKMJWJqwgY6211qrsDZbQ2XfffZXsPffccyuvvHLTTk7vvPPOynWV+HElLRnDav/0009vt912iq01onLCF198MWVpMy9FLTfccEOteAfmM888s+SSS5bhiMdhX9r7Qj/55BPlhPpFfQhQ+Ql3AHryIPUttdRSyQyAxK9mSBZyaTiF7Ao9P/744x57RA35qNdMM8204oorKttf2KCAjNzApZf5+npRWWx9zDHHcBEMMxbbd91111577UUIq0ouEKXCmLHht99+e/HFF2/k9KmjnJWEU67nFzA+8MADStpJ0ddff32Cy3pOYJIF9JLG+eef/5//+Z+ywzPPPJP6/gN1UNCgCtkvuugiZOu/jCj+eZasnk8QvPPOO/Bc5qLSpkQ06aSTTjLJJFoXVQZd1P3111+fbrrpZKsLLrjgMsssM+OMM15xxRVYS8MeOnWZNOyWaf0qh5Q3ePXVV1kIo+0pX9ooyNZA//Ef/yG2y/tIPY5PpjvZqv5+8MEHs88+u5I66psGXmqS8sUWCVNaJuH0Ub4+iAF/eQnMk5VVtkBoI648VUPOO+6443l2U7R7LdZdM9/OoMIMM8zQBx13dErj11xzzWQPoCqrl5Op5zM7dbtqqszkpptuSsU9tLLDRRZZhO4pDwq4W4F6NE79CiusoIFS93VBl9Kev/3tb4+HPVd2ckFsb7HFFk888UTKLkK/I0aM4ByfGshuuV+9lhNCDFv8LLHEEs7PkUceeeWVVzbzO2CSnebA5hu2vygZ5j1GyfYd7iLWxH3f0SH5PTk3lEJHFC1ft/baa2OEyTgf5+4TCAQCgcAEk/KlfPqcLVAYNmyYIhhPyRo5J1x66aUJBJuWj6mNv9nv6quvViDilwWILeoWduv36KOPVtDQzIHIP+zNkLRUJLfVVls9/PDDDH355ZcfeuihDM1ZWDZvDzo7gqhChVtuuUWhraITEWxt1A9AB94UZRLDpXxi3kMBD+b+8Ic/KHL66U9/SujfyPnDPvvsc8cdd0hoSgUVaihLXGihhXRIubRyP8QCBc397vwyG2WYBx54YG9+8orQZ/DgwTynp+4KAU8++eR5553Xn9NjUAoEKCKliO32229vWsIDZRXEJ++7S/kypv6ussoqzgkF4j9+lVjyFhMMA1LSrLIjgrPK0ktRJgCt5xC5b2V9hRBjYkY5mLILZRr6VW6z9957c1syzChrRUQ+UzqqMPfcc6fucp511lmV9SWTCfavwh577KGUkglquEGDBo2220fhx6UkO1R8LFPkracDBZYPWYXsf/rTn1KWqlTM6tCvFC1Wm/nuPnGuGHqllVaijK7pdeuttyoH+853vqOUNXX6CsXhhx+uLE5pWNOeaFVKf/3113t3xOWGoSRQDVA6knEJqP3999+vgbQGedUQDZyZmiXVY+zmVTG//PLLy1Y5hPRo32O3g1JebbXVhg8fDg+M8rWCUZgsBa04NyH4T5YHMqlkqZcab7PNNkpOjjvuuDvvvJNUnITQ2VZWxp3V3ehUlg3KRcgn1OwUg/zqXnvtxVF3O4cccohsle5S1umnn660+bnnnnMteEqpxkp7tDQQODVYi4yfIbw+jb0ukvFDvXT9rW99S/Y8Hn6V2WnQHXbY4YUXXuBkhCAfsvHGG8vpYVSaAmMxLxeaDs0xxxwUdEiGesUVVySzf4n9tNNO01EySffSdNTstO9ccMEFzWLf4dBMM81ES8biaGUvv5GuqeT0Ge0DgUAgEOgDE0zK5zsfUGBxzz33KOyo8nWAhp0E1Q66+uqr83IIgqE555yzmfMKbeTas9kjywg72YZ64oknamuHSBr73RKq4eQ3qY768kAFXNVzAlZ2aQE7ei2fG/7ss88++ugjH31AKKMNhW7n2ls0Kws14I2xaMY0Ne7IkSOVDD/yyCPEDU27OUqBrCISJX6S5FFHHUX2qEpuavULLIquGhn6KxmmPNnKXqxywgknfP/735/G8F//9V+bbbYZWbfHcLABBR1Snqb4vpbvSkJTCl+U3UkynhsIaszZccJQn6YAHeXzfhGDZJKBaEZ7/b7xxhsLL7wwzKAF19rXCgLWww47TKH2lVdeeeaZZ1522WVDhw5VyqfgEkWIE8XZzXyjKdP37hI+bEsCxx9//A9+8IPppptOcv7ud7+75ZZbKiEhPMVoK8uoFaB305ero2mmojz/448/Hj85oDsgxrDDXnvazTWr8qKLLqrUAmao+eCDD0j5qEFHFKRT3kHP39F291oz5x6uvmQT0TKXTp1OvbjKpHkpsVEOQBePs/10T7L7SDUccy+NoZ6/Yaj2Eo7o3Hzzzd3owLkmuOCCC9ImjS2ZrwkIATnzO/PMMzNuo/hS3KyzzoqN0Qs7kc0oGVOStuyyy6677rrc5uBrhxs7W+iQ8kEH/eJXYUNqko2VCVuP3ZP5wx/+UG7zl7/85SSTTLL55ptrXD8XAH0KqbCflJmE8nzzzUchdVkXjNj4KuwZ+lqna6yxhn633npr8SwGzj//fAiqwWKLLQbbzXx/B2KBHw5pnR555JGTTTbZtNNOO/XUU2vuW221lYzNucWYU2b7lFNOueiii5r5O5aSUmWZvGzbx6K9i2Kuueby12hBMxAIBAKBvjEhpXzsfP/4xz/Yax999NGddtqJo9r/PIBQNKm0gQBXQfb//M//KNVRbqDfFVZY4Re/+MU111zTtGTAt+26QWEH72UBRDyqF3HFjtq8FbyKyPLLL7/44ov/7Gc/889CJIv5yoikI8rYi7Bp7OP9gstBXInC6aefzkMjXk8bEiTuWCNeEYevvfaapkBjtdxzzz1vuOGGZKGMsogFFligxx7defLJJ8sbOxWO/PSnP9WsFfsiRs392muv5Si/Rx99NDWi/Nhjjyki4cKRCHo+xnwV7iu9UQxNPQLsMaig7I77G5mOGrz55psaMeXgxsENn6LD85AcZQhIIWEEAhT+NovYN+X85+uGRjnmmGMuvfTSZHwS0cp6f//733tIPf3009MY5rGlhkXzCuVTjoMlZ1kvXSRnhd283nC03bIoan+zr8lNPvnk3fTlsaYXPAQfEJr5ZSduhxdccIEvh5Tz6mQ36yo3YxQU/c4776y++uoQQWXEuBRgzBcIhzwZ5hpIr10B1l9JgGZ+sb1h92EqUufyHYcwD9jzZVjPaV5vvmmwVny7r7IrPFrpiK4bHUjJzxxyyCGqKb9W93XDJdy0FEtLu2bnF2qWATK7eeaZx/Xr2kdi4NZbb+URRKAuEl1vfkDa6SifwSaRz/XXX//zn/9cBiblatyVV155qqmm4iWf7gZ33313LuOrrKxSq++BBx7gr4ux3X5KE5LA0W89J+Ht6+Krsmcoy20q0zvnnHPEuexHixQhcEg8aBdIJkBkCFeVgXtfk7E0ZMgQrdO6QStUEn7mmWcghYLysP+EnIPmXlbCjLJlFxe/dbvyLDrzzz9/yvfrjt98A4FAIPD/N0wwKV+y7+R6yKJ97uGHH+ZDc2yQBDTKEHjuomGPTPzqV7968MEHR4wY8e677/71r399/vnnFXasu+66jfwkEh0p8NbslAPocm9ef/31b7nlFhEfOXKkAsrhw4crJthkk02ShQK+Jfs9Oe2A8yq/XM6DxYGC2DTldOWPf/yjAhSLlP71+CIDpXyNDt54R4Wg4KNpp5P/P/bOO86O4tj3Djhh3+dwfZ0wNhiRRJJBCJGjAZNzFmCCZYzBJGNETiIaTDDYJJFFRkLkDCLI5CySMMlkRJS0uydMv5/re7tua3fPWhKId3df/f44nzk93dXV1VXVVTM9M6o2fPjwiy++GDoPPvgg32pP9siNBOttJa7bb7/9mWeeefPNNydMmKC8USLddttt2+yCPc0V4lx00UUENCLy7rvvKgDyTz97GK22YoBXyDTz+xK4YYKohw4dyovs6Fp1JOd99923Ld+CgJTkr1n2LY51Sw9IbqHGTkJ0AOKaGkWlVf7YQ5XvIMHYzAPjOvTQQ5WZMyPo2y233PLrX/+aCuJ/xx13vPrqq10VfSrvvPNOpd8erCvlu/DCCzssRdF4Na0LLLCAf6Idea6xxhpq1Wq+quK6g0/fJ5EDnfIqlJolIR70t9mLc3baaSeyLx+dJm633XZjilOe65TvWaUiA4QahWVMzFmdUiJRDkoHDz30kPKTRx55pN2AetDKbcf3bDeKJ4Q79fLwww8vscQS48aNa+SHSLulg84PGTJEQoYCV1s+A7hZtdn+UlmWe8LKoL/kIeiSNP+ee+5hgDqmVbJ3ukhJGKAgkULWBaua5Fc1g8o33XRTkZJflUvEr8pF/PKXv3RFVat99tlHSWCbfSilzZ6OHjx4MFsbXENSF/1J2f2iS7IR/7RJ6s4ufOrTJ9ZnHMJvf/tbqRCjSNmTeB05KPhBwjCpv7xLjLQw2eYL/7qguNLqIwFq7XBu+cVyTzzxRNYdHk5uZsclmxVZCPpcC9dcc43yUkRdy9+eCQQCgUCgZ/SalI8oobKYntBKKd+ee+7pFYgXtST7BjMtqEsttdRke6ECYQfVll9+eeUkDcuRiIOTrcGKpxV21G17mC/5igO06i+55JJ+G4GFXMerrLKKIhiaV/amh8xLN2Dth8j7779/pcHjy2mHsw0nxx9/POECMQRRSIddTm7YbRAPMvT36aefXnHFFT3m2G+//XjjP7EOUhWHEqwiLZq/8sorvHEB/jn48MMPJRB/1aGaH3zwwddddx0cNu3+wG233aZQMhWZpzJJxeIizkbEZLtbaeL0lfYommGmaKi4R7mohzUaspKZxRZbTBEn0WTDXt1RGaCT8l1f5JCMJeW0m222GX+hw8FnAA3k8MMPv+OOO+CWOFW5hH9RQOwpRVlmmWVSvpyRcgaiQj4iwnQodfR3uzctFlf8p5w85SzojTfeWHbZZemi2/kCLmHJVmk/NacLTbtR3GZJnbpQ2MrXOyrLNLj2gXrfeOONW221Vcrv71HhNttsI8WTIfuUYTtiQ0ahnJbZ8eeU0FgNjb6cW80pn+IANfsE4sCBA6Ub5QZOPAN7OOvF2/zVkbqDWvlMlPh/7rnnJDGlMT4dregkY/vnP/+5P3mYpg7QZxIQRSPv6xPP6667rnKwWr5Rqd/HHnts7bXXbtq1lYkTJz755JMrrbQSbLfbzaJklsI7k/AAGteqq66qmh32ZfZkSvLoo4/Klulrin0tY9CgQbggN7FkD1G32V19roIp7eF5tiq7oFtvvXXDDTdEUK30p27v+EFzMFvYa2UX4JPrszsEcfj44483baMEbCArXLdyMHVN5fLsEksswaN6lAwfPpyxA9W86667ZKdNQ7Kh+dukjj32WK07NOQsx0qkpYQp38HW6JgUTRCP7zJf7k4DgUAgEOgBvSblSxZaeY6kNf76669XZuLrrkoU3/B1AZZhxRBaTVkOWS9ZUE866aRjjjnGy6GW7NLsRRddRLhA5MrSrnI1qQycbdqFapWffPLJDbtRUMuPh8FeVxCpUOeCCy74nIH7VDMAmBdN5Xt/+9vf2vJXxRgIfSlU4mV3hKc83XTDDTfU8nbHvffem5TPS8Cdd97Js3wqFPHjjjsOuamav3WTTx1KGgTrBx10kCKtj+11pvSu34022kiJH/J56aWXFlxwQX9JHUGMCvlSYt3QYYnKoosuqnSIagrgeBF802JN9fXqq68utNBCismYCMJH0RGftXyPSKcWWGABZY9VziXefPNNBU9KupJtcCUwpV+GM1PRtFdZjBo1KplYYFITseeee6J+yfTwiCOOULjpO3LF5JZbbslbMTQ0yg888ECFkpMMzvx22213+eWXN+1RQOmkv66w2/minAk977zzpISf//znlfxQbXrBWCRJyV/m5tHnlPwFhcoutQwePBjhi22phOaU5pUlA07knHPOET9f/OIXzz33XGxNVuaJh9IqNrWSUr733nuLL744rwiq2TWd8ePHK997/vnn2+1x3Mq2WSpuHjFiBFy5xPRXXagjdedPajVy+qR4eumll1ZD7KJpb3BpRUdn5Yi22GILyj06p8JMhV9jgh8lqMsttxwWITY0doldmUZll4H0q0TuC1/4glwfl0hQRWmFtK6Rv/egtmqy8sork5CoC8lZ+Qx7MjsswZMzlE+omeOt57ewqqbkc/TRR3fY9TKxobSHl0/6xTJR2Hjjja+77jqXT1f9aeab/428RfOwww7beuutW9kFv59cnz1P3mmnnZ5++mnPvprFPUnkrDHKs0ksla0RyT5+I374K9mKH17fUtk7lup2iVB0dthhBy4xNPPrXvF4sk1pY8rSkOT/5Q2tlXzCeuutN8XQsARvt91206oHJ8inPqPPCAQCgUDg/yv0mpSPOIC1TcejR49eZ5115plnnvXXX3/++edffvnll1pqqZEjRxKlJXsd5dxzz63CX/ziF/feey+Fzz333AorrKDof7HFFttnn30IiLUqr7nmmgprlBHNO++8q622muoQAQhKftSLYqmVVlrpkUceqSx+euqpp1ZddVURV/C63377eac9h3oKCIh+xowZM8sssyji5DWA0wslMMcff7wYXtyg8FTZnXhWPpBMRERXioZXX331RRZZRCHCuuuu279/f39lpaIHBSWKoRUiKy4kbq7bDbTBBqVVu++++84776w8TQIUfT5uoYYPPPCApK1+Jd79998/WW45YMAAsSEpPfTQQynHT6+//rrkKToSmmKdQYMGSYaqrLaSnhjTgeInBkW4I6gjzY6yd/GsQfEmHiAOlQTq7LLLLquoVPyLN8lBpBTIUqeyNE9yVvI/11xz6VeRlti49tprPef3yf0MoHFtuummEqlEpOiNKO1Xv/qVhvajH/1IsSyJTbLgUoHvfPPNp7MKaqVaJ598cjIxJhuXRr3wwgtLSyV/zUKymE9tX375ZZXvsssuw4YNk0yk3tLMHuarkXcgK1f58pe/rCj5k+ihhjbI4Hq41157UWGKXWdRd2JGXMnKJAHxJoZLe6nyblvnx+9kAnRDPA8ZMkTGrqBcKdZPf/pTZY+IDoXXKOacc07JZ4MNNhA/q6yyivRNOrnvvvsSQ7v3EEF1oY78jZ2erOpXudMPfvADNZQSSrvkEHqgo4ZKMMaNGzfJbm0R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1uSDYomkjqcf2EXDrkdUxe6AuiFN/YhaymGD/DY1vTmt6MVdujd3IpJb6dycT0q6otW4OKbQWS1rdpJP01DWSeZ+RYT9lhIIF8W8Pn25oBoWO7Xyz03LDGsWcjSKRwyaNpucdTof25ZdFzVj7MiXvVDLpkWVXZeMQGC60GtSvpStiOPSm2OTmAEVME538XIr5Trq4SMm5+babgGW22HpEbBb7929W1veHFLyUzo1anZyQJ8ELgT1eO+99/71r3895phjHnzwQfyU86NBNQz/+Mc/jjzyyKOPPvr1119nUJ3GJWoPPfTQCSecMHz48KeffpqIECLNYtV8/vnnReeII44QHaThRKocVI0dO/awww47/vjjX3vtNaTazKkgK4E3mdlw76mMtFwC68XKzaR0Sn3FpCRJHbQIRYJ598WsDdShLzWv8lrlS3JgWqDoil+ftWaOcrwkZbPtYb6AG0jK3gA75VRppzXbd+1T9ikaqQMVeuONN440TJgwgXLMEDuC+R7sqxWd9uLyfCN7J0njxBNPPOuss5566ipZ6xMAAIAASURBVCkoU+2j/HxvssHKKBTQXHDBBX/5y18uvfRSRITLqlnk+uyzzx577LHi55///GcqbPwzQKc54q+mG4nxl8lyD+9ZLhlXPW/Cn5z3+b/33nvJxE41vCUN3WxpnrKzQt/q+T4Pv06hZ3TlJ+VJR7zJhqa/YozylEPYZhHxB1rB1ZVjX2W8gs9Xla8K+VoszacOAqeaV+C6XipcTRkV0LAVPKNrs+2m3c573dagVvMOq7Qtkw14ll7xNAd9JVPsVnRYkpKJonSklQH5oISu/1T2B1xxO6lYNynhmL/eMOX7Zhx3TP2wA8ewUYZGwD02S6236ooexuWSQYYNuzjbSj4uARp6fEhbKqfMmAoVYimIOu200xRQMTvOc2rhnwHi1epWWfaoWOuoo446/fTTX3rppZqluPTozIwaNeq222676667br31Vh3cfPPNcOKMpan1PBCYLvSmlK/KacMHH3zAmio/eNlllw0dOvT3v/+9whf36cks7fLLL1cmc9FFF1144YVnnnmmbOnOO+90S8bs3aQvueSSYcOGbb/99n/605+USinQUbagjur26O0111xzzjnniIh6ueqqq2AmZZf3sSFZ2KpOxc+uu+46cuRIXNu/XSemC0hAfmfFFVfcbrvt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/Fk/0T/88MMvu+wy31Y6efJk/d1kk03oSL9K/+add96nn366Kj4A+Nhjj/Xr14/eKen09GBgpgKZA587v44QCAQCgUAgEAj0dvSalK9m310oS5ZZZhmlT4suuih/eTxvkUUWSflFLDpYaKGFOPC2CusHDhxIiaodcsghV1xxhbK766+/Plkv48eP32qrre6+++5f/epXKWd3w4cPVxLoRJr2Vb0dd9yRTZi8PvSYY45RjpfsaxA8sKff+eabD7Kqf8oppxx99NGkE75188MPPzzssMNOP/10lfBgYcNe4MnZwMyG5k4Tp6lhXvwdP4FAIBAIBAKBQN9Ar0n5Uk7byMEUqffv318HBx544JFHHulh+oABA3ghJ9X0l1uC5GBUI0uE2gEHHKBkb9y4ceuvv37dPus3ZMiQ22+//f777994442dzkEHHXT55ZcnS9623XZb2vKqFd4fo+MjjjjiyiuvTEU6N3bs2OWXX94ZWHrppd944w1nFSL6+9prr6kadxQp9Fe8BGY2zjvvvM8ZLrroIlLuVNzuCwQCgUAgEAgEejt6Tcrn977IoPS3X79+5GODBg168sknKV9wwQW5xcc+SaV81GnaF/YgRZ3K3t75hz/8gSf9Vl111QkTJnz44YdLLLGE/ioJHDp0KE30q8Ty97///RlnnKEMYb755nv33XfLj0boQEnC8OHDL7jgAnK2N998869//euSSy75zDPP+O7QBRZYQGdJJ6r8ZlG1VQXxCW/+KlH+BmY2brrppllmmWXWWWe95ZZbqvxFx0AgEAgEAoFAoM+g16R8fuOFe2s6YH+mYvQxY8YMGTIk2SNYKqzZ9+7I8djn6Q2TZVNKvbxk2LBh1157rY5HjRq1884766+SOrX9+9//rhzPb8R1TfmgUD70tf/++//0pz/t37//bLPN9tWvfnXjjTdW4idSnuMtuuiiEGzah9dTTu1UqKyVA08ynWxgpkJz8dFHH02cONGfrqzZdxc71wsEAoFAIBAIBHonek3K57f4avZpPiVLyu467At4OrXFFlvceeedU6ZMUWGVX+VClsXtvspemElMP2DAAH+gTnnaddddR53llltOzSdPnqwkTSkfd/nIyrpu7NSpDz74wHlT14cddtjIkSP51sLYsWOXXXbZe+6557+5N/i7ZNLUr4FJ9sxh0+A9Bj4bcKvW79ZW+cuNgUAgEAgEAoFA30CvSfmSpXB8Xo+/5XN6TzzxxIorrqgD3yEJllxySeVgzby1UhUmTZo0ePBgf2prn3324cUtwpgxYy699NLKdvfdfffdu+66a2r9+halhbfeeuu1116rZK/DcNxxx/EsX7JHDd95552FF174pZde+vjjj+FZueJtt93Gs3+kFvR1ww037LDDDtxZYp8nRAKfAZhf8m2/B+sTHQgEAoFAIBAI9Hb0mpSvvPdFgM7LMEmQdPaQQw7505/+NHDgwEbxxssVVliBz7WTHCpjfPzxx5dffnm/yaaUTxlX3eDEdXzLLbfssssu3AJK3X2kQafOPPPME044IeUto4ceeugll1xC79xUVIK37rrrOocPPPDASiut5BXoTlhsscXuv//+ZF9xSDkb9LOBmQrN4+WXX37VVVf5vt/ONQKBQCAQCAQCgd6MXpPyJUvGyLXIl0j5KEn2tQPlTv379+cWDds4H374Yb6HzifOP/jggwEDBowbN46kUTX33Xffm266iXA/FR/Zu/POO/fYYw8oK1E85phjLr744mSvV9FZeDjppJNOO+20lL8JcfDBBytz8GyN5GGLLbYYM2aMl6jOTjvt9OqrryZLNkRtk002EXFu/XHvMfK9zxKnn346b+w899xzXQ16mAJOkbSjHpWhc71/h0b+DKM3R4s61/t3oLkz4H+9ZBrhXfum6BkgEggEAoFAIBD4X4hek/KRFOlXsalSo1VXXXWOOebQ784778wDfjo7cuRIFXoT8rfzzz9/0UUX3WyzzXbYYYfZZptt1KhRitdr9kDgfvvtt8giiygJXG211ZQHksg9//zza6yxxuDBg2efffY//vGPH3/88Yorrvizn/1sySWXHDhw4Nprr62zyy233AorrKC/Ip4seVt//fXVtVqtvPLKY8eObdh9RVF75ZVXlHMOGzZMJWJeLB111FFLL730poaFFlronHPOUSLK04kpv7HTbzkGZjaUpX/rW9/6+te/zjcV67b1twf5e5rHBQiOO1fK+LdZE6pYy28kaoUe6HRbTn2HF3a6vdwtyrH/28qBQCAQCAQCgf/96DUpn6JVf5BPobZ/4eCdd94hVSPr04E/p+dQw2efffbuu+/2CJi4VjkYQbAqQN/zrnrxTF15oDr+oBdEeFTvo48+SnZ7kNSUU9ARY5D1m0iq88QTT7CZ8733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DDfeeOPee+/9+uuvN208KDcB3nPPPY8++mhOd2/8o4/EHr/22munTZuW54rzZLILOwEAqEbfRL48/ZKvTRuxNthggximl9H57Nmz491Ro0Zl/FuwYMHmm2/+i1/8YrD3fM7Mb/HnM888s9NOO2W6i9fDDz88RvxNmx4ztr300ktbbrll1BBVRYHRo0ffddddg+1zO5tegCyP64yVlue+lORJv5gyZcpKK630N3/zN1OnTpXYAQCoT99EvqYXyTKqxcRaa62V8zOb5cxVV1216Z3lW2211TLvxYKZ0PL5HE3vZGBGuLFjx9544415XWiEtxtuuCEWjIyXZ3ti/lZbbTVz5sy8njPX2M2QJebNnTs3J+gjsbsj8r397W/P2J9Hl+wHAEA1+ibyZcoqZ/ki5q2++uo5nT+ZkBOR5TLIRYF11113Uft7elksxvHz588vkS+jWj4J5v3vf/8WW2yx6aabxtD/M5/5zM9//vOm82CPjTfe+JVXXhnoPZkzr/3LVJC1RU7IE33l9j/6RezH51q5c4da3XtEAQCgr/VN5Gs6z88cbH9CPRJaJLEyQM8zextttFEWiNcIchnMIv6Vay/zhr1IgzknChxzzDHTpk3LP6+55pp46/HHH++Gt/XXXz8qj6XyVOHXv/71yIebbbbZu9/97jXWWOPZZ58tJek7GdfzOBH2AACoTz9FvhiRR9LL6y3jz3JhZ7nkMiLZO9/5zjwdN3fu3F122eWhhx7KH14f7v2Se7z+8Ic/3HXXXbPCmHPYYYddddVV5Vq+Bx54YNSoUa+//nre+BfZ7+CDD7711lsj9eXJvQyHsZaJEyd+5zvfyROJA+0TO13b2adyD5a852wtAADV6JvIV+7Wa9rTfRHAtttuuyeeeKJpL87Mp+o/9dRT2267bbm57v77799+++3zDr2mHcdn9vvEJz4xY8aMTIZRz+mnn3711VdHXIx3M7Odf/75X/nKV2bPnp313HvvvTvuuGNO54+85/WckffOPPPMpvNwf+eI+k4cG9OnT//+979fnvpTwj8AAFSgbyLfcPtTeJHQyjm92267bYcddsiReoSu3//+95tuuunNN9/ctBd5RrF4K5LbPvvs03QeyDFmzJhddtml3BMYxY444oiIfDnd9J7A+alPfeqhhx7K04CzZs067LDD9t133/ydhlw2wuHxxx8/derUjHnlZsKsln5x+eWXv+1tb3v7299+5ZVXurATAID69E3kK7+OHXmvnFWbMGHCaqutdsABB3zta1/7wAc+cOmlly5sZcl58+bFIP7kk09eddVV995778MPP3z99dc/5ZRTsqoo9uqrr2622WZ/+7d/O2rUqM033/zee+8tefKxxx77n//zfx566KFZVWTIM888c+21195rr72inkiA22yzzcc//vEnn3wy7yHMqFDuNqRfxDGz0korReq7+OKLy5Hjwk4AAKrRN5EvDbW/slBu5wuvv/76jBkz7rvvvu6jXCLslRNuMY6PP2+88cbp06fH9Ny5c7OGfBbLYCsnyqV9mQkz/kX5DHVN+9Pt999//+233x61xXSUzxvASoFy8pB+Ebv4kUceieief0bYK4cWAABUoJ8iX/n185zuXoZX7ruL8XqeoinXW5abAIc7v+nXtIkur/Yc7t2bFxN5q17TJslSsun85l5ZY8kGmS1z2XyLPjIi8Dee2wkAQF36KfLBX1x+cTDcXl3c9L44yPCfWbF8TZB/DgwMdJ8HE3PyzzKzPc38LwmzvLVkPWXBpteG8oVFzuzW84evNzplysysaqn15J/dW1K7ywIA0L9EPnhr8oLepvcM2DI/g9a/llua/z/KDLWWnM5i+TrUy6UjjFjXYPurJE17etxZawCAOoh88NaUU2FXX331hRdeeNFFF5133nlTpkyZPHlyvl7UuvTSS6+88sorrrgiJi5sxczJPZMmTcqlrmrFRPwZM5dVT4iJnFMKxGtUe8EFF1xyySXXtGIi/oyZuZYslqu+7LLLYkXLqifWno2MMuXRtUtNiQAA9BeRD96C/A2Ppr29M8LV8ccfP378+GOOOebojrGtY4899qRWTMSf3/zmN4866qhSJhc54YQTzmzFRJlZLLWeMKJM1HzcccdNaMVE/JnFyupykWjqqaeeuqx6xo0bFwWiGRE783FE+WiikdsPAEC/EfngrSkP/pkzZ07Gv39fNOpeVDniAssV7t+8MS8LRMzLJxUN9+7rAwCg34l88NZEFspfhuzmqKHek1EyvA22D24pRtxr1016WaDMWX49g+1jXYY7D2Ipr/mLlCNm/vH15NqzAQPtc24HRD4AgCqIfPAWjAhCA73rPJc03Ml1b37nDzJ0dedkMOvOKfNHTHR109ryZxZLradpz17mb1GWOVIfAEAFRD54ayJQ5bM6M6GVs3Z53iwnRpzK65YpZ96W6o+vpzsx1FHeKobbMFny5FLryemmdx6y/EAlAAD9rm8iX/dcSl6Klg+Rz59EH+r8tljTOzuxcOHC/PG0LDnQub4uR7Q58C2j2xwT50Pql3XqBgAAoI/0TeQrqWxEumva8xJ5QVo5yxGvs2bNyrd6FTTz5s3LiQx1TeeZhHmDU1QSETFrG2rvaCrLAgAA9KO+iXypRL68IC2T3kD79IuYXrBgQTcQDveuZ1u4cGHOyYCXp/4G25upctk5c+aUCjM35orKtXAAAAD9qM8iX9M7uRfZLNJaXrGZwSwvxezmtHJxZhZr2rBXMmG8m4GwlMnQmH8mJ/oAAIC+1jeRL5NeTuTVmyWt5Z8l/nVPzcX8N954I5fNu/5yOk/xZZkFrZyeN29evBWvea6vVw0AAEBf6pvI13Ru58tQN2vWrIGBgXJjXtO7Ja/p/PpZyXULFy7ME4N5VWeEunIGLzJh01aeb+W5wVyLs3wAAEBf66fIl6fmBnu3891999333HPPfffdd9ttt911111Nm9byrQULFjz33HMPPvjgTTfd9Otf/7rp5bqf/vSn995777Rp0x555JF8nmdmwjlz5tx8881HH330CSeccOedd+a9f7kIAABA/+qnyJePWmnaM3Lz588//fTTjznmmP3222+VVVZZa621XnnllVIsXn/0ox8deeSR/+N//I+vfOUrkehy/vnnnz927NiVV155zJgx8+bNy2j329/+9hOf+MTo0aOnT59+xRVX7LPPPttss81rr73W/Fs/aQ0AAPBXrs8iX157WZ7Csnjx4gh+kyZNOuSQQ7773e/mNZnlYs6w6qqrRpx77LHH8ia9nPmBD3wgl82So0aNuu6665o24MUqIgdG9tt4443zjGKpilqVHZ1fATQe2wMAQEX6KfLF0DwH5eXazrDllls+//zzTz755A477DDcPqwl50eZSIYbbLDBz372s/XWW6/pPLfzve99b9P7Ub4pU6YceeSR5dcd4jVWMX/+/P3333/q1KlZnorFMXDzzTfffvvt5ZLgcjIZAAAq0DeRL0fh+XPq+WCVmPPMM8/svPPOWWCjjTZ6+eWXc+Cez3RZvHjx6quvHq+HH374JZdcUiLfu9/97sx7MR2Z8NFHH806mzYHZg0PP/zwtttum+Wp2FVXXbVS69prry0zneUDAKAafRP5ykmYnM4/x44de/nll7/xxhsxRj/nnHNOOumkmJ9XbJaLNuPP119/fd11150zZ05GwZguNay22mr5VJj8M4NfBst11lnH2Z7qTZ48+W2tOJDy8T/5ZNeR5QAAoD/1TeRLJcs17Y80vP/97y9vvfLKK5tuuml3sL5o0aJSYNKkSQcddFDThsa11147Zy5cuDCnh9pfdOj+mHssG5HvXyqiao+1yp9yPgAANembyFcG4nlSLiZuueWWCGyHHnro2LFjjz766OOOO+6d73znnXfeGZktAtu8efMiwq233np5Qi8W2XzzzR955JGmvZevPK5j1VVXbXoXgparPfMhMe973/v+Zd3Uq1zuG7s+pwdbbyoEAAB9q28iX7kUM2+3i1S21157TZw48a677vrhD384Y8aMm266adKkSV/72tfyTr9cZNSoUbl4zIm8t91228XEBz/4wTKm/+xnP/v44483baTMi/qa9vzhQw899PnPfz7XSN1K2Evl1x0BAKACfRP5ylm+nJg3b145C9d9tv773//+8iCWkL/HUEbwkRIvu+yytdZaa1Er5kRQ3H777bNM5r1cfKeddpo+fbqhf/XmzJnz9NNPP/PMM5n08oTwyEIAANC3+ibyzZ8/P4bj5Ymd55133imnnJLxbNasWVkm/jz11FMnT56c003vJ/iG2tvzYuL1118fNWrUu971rlIgfPGLXxwzZkzmvcWto48+evTo0bku6nbttdeutNJKf/M3f3PNNdc0vW8HlvP4lvKknyyTh0333WUlxnyrFCjFMmeWMt3COT3CiHpSNqOc3F7WsgAA/AfUN5Ev5G/u/fa3vz3kkEP+/u///t3vfvdWW22Vl2XOmTPn4Ycf3n777f/u7/7une985ze+8Y0IbJtvvnkM5TfeeONPfepT+ct7MRSeNGlSDPGzwoULF0ad8XrggQduuOGGUe3xxx//kY985Otf//prr70WBebOndtZPxWaMmVKHCRvf/vbp06dWr4FWE5kyqwVx1Lmq5xeTvmi5LQsvNRFljpzhCXrKQ3Ia57LWwAA0PRR5Fu8eHGOyGM4O3v27F//+tcvvfTSr371q3KGZNGiRT//+c9j5iuvvBIFmvacXkzHzHw6SxnQP/roo4PtMzmzWNb5y1/+8oorrrjhhhuiTk/v+I8jjp8bb7zxlltuycuDB/6t32HPd+MIKUGrHJYjFsw5y5I1dMsPteei893u/DcvN1LTaUDWkFV1awAA4D+yvol8ORpueiPjSICR2fJ6tjlz5pRTLjknhu8R86JAlMwzdXmVZs7J2nLIHiVnzpyZy8ac+DPKDLWizrzfj7qVizPLEbWc/Z4HYR4tJWWV9DWiZCk84t2c052/5JyizFzy3Zwz2MqDNguIfAAAFH0T+Zr2ws4ci+ejWZre+Y2B3o8rlDFxuc+qjObzRN+CBQtycJzXc2bhcv4wU+JwmxuXczcX9cngVP7sTi9pyXeHewmwKH/mu0X5c8RS3bTWK/uv8/Ot7vzunyNa4tAFAKCrbyJfxLDuALecgovklrkuH+KST9vPYq+99lpOZIE8GZKLNL0QmJUM90b85ZEtWWbOnDn5J7UqASnDVfy5+N/6kYaySBxsWTgOm/wqYbgNaakbxrozs0zTHpB5HWmuN4/At1pPPtYomlF+Z6J8zQEAAE0fRb6md3IvB7s5J2NbMdwmt5g52F752XR+eqHphca8eG+oHXOX8XQEvAyEw+2lnlFDd5xNxfJIyImSo5Y8j1d0D7/77rvv3nvv/cEPfjBjxozvf//7d/fk9D333BPv/vCHP4yJmHPXXXfl/O+3YuLOO++MiR+2YiL+LMv+8fXEzHgrWvKjH/0oW5WZ8F9bDADAf2x9E/lynN2NcOWsSMiTcjmnxLmh9n68XKQM4vMUTaknz/KVwlmmrMLQuXrDb76Ot3yt8OZS/6qcFp43b96pp556zDHHjBkz5qjW0T05feyxxx5//PHjx48fN25czPnmN785duzYLBkTsWBMRJlTWjERf+bMt1RPFDjiiCOizGmnnVa+qljOvYgAAPxH0zeRDwAAgLdK5AMAAKiWyAcAAFAtkQ8AAKBaIh8AAEC1RD4AAIBqiXwAAADVEvkAAACq1TeRb3BwcHh4uPz8ekzPnz+/6f1sevfXtPNn2Zv297Lzp9hjesGCBfkr1flayqRYPH+SO0s27SpG/DJ7/uZ7FHvjjTdKsRQl88ev/QR2Xys/wp6HGQAAVKBvIl+K/BZJL1NcJrEl382kN2fOnJyTCS0tbmWWmzdvXsS2GNxnyUhrMT8Ld7PliICXkSAb8Lvf/S7rzLfoR7ErI/+XrB5/5i4GAIA69E3kK2fhmjaJXX755ccdd9w3v/nNcePGHXzwwTFx8sknH3vssUcdddQdd9yRkSzi36233hoFxo8fP2bMmCOOOOJb3/rWCSeccP3115czeC+//PK3v/3t/fbbL4qdeuqpUWbq1Kn33XdfxIAS/HK9s2fP/s53vrPtttvuuOOOMZHnCTMTZpKMCWmhT+UBkxO5N9/8PgAA9Ku+iXxNe6ptqBXJau+9946Ad84551x44YW77rrrXnvtdX7roIMOOuaYYzKqReSbMWPGBa0vfvGLe+yxx7nnnjtp0qQf/OAHTe/ivQhykydP3mSTTY4++ugIchdffHFEx5122mnPPfcsZ35effXVF154Yc0115wwYcKLL7741FNPnXnmmautttrzzz+fF5cWJTnQL+bMmZP5P46HzPkjSwAAQD/rp8jXdC7U/PznP//YY4/lzDPOOOOyyy7LwfqNN9647777Nr1LMfPurFgqkt555523ePHiksqiniwTqW///fePcJjzs57DDz/8hBNOmDt3bl78uf76699zzz3z5s3LMpEGH3jggbXXXrvpNGm4lQXoI+U+z4h8Oe0sHwAA1eibyFdG4ZnZIvI9/PDDeRdWZLPJkyfnA1fuvPPOr371q2WpeDfmx+uECRPOPvvspj2ZEzWUe/MWtw9uidqeeOKJvKgv7wacOXPmxhtvPNzeFnjmmWceccQReUIv5vzqV79q2ngwZsyYeKtc/DnijB99YdasWZMmTYrjJ+/MTCIfAADV6JvI1/Ru58uINWXKlJdeeinnR5a7+OKLY34EuRdffPG6667LK/QiwpWLM88777wLLrggp7vzM/vtvvvuebVnKfCb3/xmjTXWaNrR/yabbPLyyy+Xa0ojBGYkiOy3/fbbz507tzwX1Fm+vjNx4sSVVlrpP//n/3zJJZfErswDw34EAKAafRP5Muk17bWaTXtZZtMOzSOzTZgwYfLkyaVM9/cYciLG8aeffnoM7ofbJ7JkPMvze2n06NGPPvpoFMu3Xnvttc022+ymm27KaLfKKqvkqru5LuqJd9ddd92sKt8tT4WhX9x1111ve9vb3v72t996661Ne6hksB9ZDgAA+lPfRL48t5ahq+n9sF6eeYs4d+mll8acjF7ljrtyeV7Es9NOO+3CCy/MekogLCHtC1/4wtZbb73bbrvtu+++n/zkJ9daa62LLrpouD2pGEaNGpUrysWzwpyOkrNnzy7rEvn6TuzWl19++fXXX89dnMdGOcwAAKDf9U3kK3fKDfR+9zwH6BnnzjvvvFIyCkT8i3fzLr433ngjXidOnDhlypSMZHm33mArg9+ee+4ZoXH69Onf+973fvKTn8ydOzfryQDwvve9LzNAZIOmlzbz8aHrrLNOhL2YjsLu5etTA62mcz2ns3wAAFSjbyJf0150V+7Ba3rXdoYJEyacc845TZvl8kxgPrWllAwXXHDBueeeu6j9vfVyLi5DXSyyzz775BM7y1g/Zmbwi7V84QtfePDBBzPjZQOy8uuuu26//fbLuwG75wDpR/kdQU6X88MAANDv+ibyleF4RKw5c+aUAXq8nnTSSZHo8uxfKZbT+atrEeTOOuusM888s9SWt2yVhLbbbrs98MADMTNPD5ZsmUEu3tpkk00yLmb5vOBzww03fPLJJ6M98+bNy2eHOjvUd2L3XXvttdOmTYtDJf9c3N7kObIcAAD0p76JfEO9X1DIP2OAXjLYKaecctlll5UTgCOCXy573nnnnX322XkFZrzmGbwMflHVHnvscf/99zdvPsuXwS+T4fjx4yMWLm6fFxpmz569zz777LnnnlkyF3FhZz+aOnXqSq2YiB2dR46ztQAAVKNvIl/Tey5LxLD8CbWIbTvssMP666+/ySabrLrqqttss83mm29efnAvvPLKK5EGo8C6664brxtuuOGWW24ZhceNG9f0Ths+++yzH/vYx+KttddeO8psvfXWl156aY74y7h/5syZ8Xr++eevvPLKu+++++jRo9dbb72TTz55sH3456xZsxb1Tg/mWUH6yLRp0yLv/af/9J9iommv4817NQEAoA59E/kG20etROrLWJWBLZ+WGTPzzzynl6kv5+TJuqb3Cwo5M8pHVTE/S+bzV7JMSYz5/M9YJFeRV3vGxP333//kk0/mtX95H2DTnt9zXqh/vfDCC7/85S/zYt08zZsngQEAoAJ9E/ny3EveLzfc/h56zlnc++WGPAc40Pud9JRvDbRyIpNbufKzRLUsmTXnKsrMpvPkmHyISy6Yp/VK/MtUmeXpF7nLyr7LHTqyEAAA9K2+iXzwVyLDYX4F0L2BM78mKNN522d+L1Deyq8G8juC4fasdfPm89IAALBiiXzw1pT7/fIHHpv2DHOJdhnqRuS3zH7l3e65xJzI20G7iwAAwAoh8sFbkBmvafPeueee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7JTddttt9dVXv/zyy0tf5a84xCD1wlY+lWSoPXWwqNX0BpfRwlgqxq8f+chHvvvd7za9/TjYu/FyoPez9UPtuYvyZ9eS/TPQ+uQnPxlxqGn3USx77733xsg1x8e5c5s3XyH5p5vX/pZaTHzuc5+L/tlrr732aMVevuqqq7r9E69xrMYRGDkwjtgNNtggj8zsn3KsZvk8C/TMM89ssskmkSSbztGSvZQlF7W/s5f15IKlhujtWOl111130EEHbbbZZh//+MczM8TMPOETGaN7wjk2JNpcwmH5jGRtf7bIt+OOO8aRFsfYpz71qQgtETZG7K8RkW+485vsZdvzeFtq5GuWfRxmt2RP5tGSJYfalDXY+5nErCfe3XLLLaO78sDrfk7LvshmxJ/5LU+3n/NS89LJ73nPewbbH8aIAzs+XLnqddZZZ6gVb2266ab5fUf5SivXWD6eOWfJyJeNKV86ZOSLtSzrc5GNjObF4uUa43hdd911u7/oMNB+DVe2FAD4y+r7yHfWWWfFAOWee+75yU9+8rvf/S5HUTkMykVGXNiZVZVxSdMbJA0tI/LFUjvttFOOieN1iy222HjjjbfeeusYasf0l7/85TLGuvLKK//P//k/m2++ecyPYeK222773//7f8+TAzm8vv7662MVOajKNTZtEvjxj3880Ls8Mmbm/V1N5+qveCsH32XguGSkifFZtCTaluPOqHDKlCn/8A//EG3Opn7iE5/4r//1v958881N52TOCrGwfcbM17/+9VNOOSV2xIwZM2655ZZMIIs6T6EIq6666mArOiT3Rckng+2IORsW+3G99da77bbbhtpQV7Yxui72wjbbbBND+dwFMaqODYxN+/CHP/zpT3+67Isl+yenY2ScZ2CattmxigMPPLAEyCw2bty4ssgKMdiG1WjPhAkTIp7deeedt956a8aAjKxZLPonhtH5Z/RDDM2HWk27N3MiT/XknDzUf/nLX0bIKZV89KMfjSMweib6JwLkxz72sQ9+8IMfb+28887R7QPtlx15hA+0mnbbY5dFn2edTdvVkUj/7u/+Lo6cqG2rrbaK4/m//bf/dsMNNzS9uxObv0Tki897HGO33377Y489FiGn+xFe6oWdTSe0LO7codcsI/It6zhc3MqS0UvRsXkERofHaxx++RGL1+jnXFHMfO6557J8duxwe1HuUPtV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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>