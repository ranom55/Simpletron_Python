O simpletron é uma abstração de computador, que usa uma linguagem fictícia (SML) para funcionar.
Como podemos ver, temos no repositorio o arquivo text, que é um programa em SML, aí vem a pergunta, o que esse programa faz?
Ele basicamente soma dois números e mostra a soma na tela, o simpletron não faz coisas mirabolantes, porém é muito simples de
ser programado.
Vou começar explicando como funciona, o simpletron possui um acumulador (registrador),
ou seja, podemos colocar dados nesse acumulador para fazer operações aritméticas nele
e enviar para um local específico na memória.
Este é um exemplo de código em SML:<br>
1098<br>
1198<br>
Os números do código (1098 e 1198) são divididos em duas partes: código de operação (10 e 11) e operando (98 e 98).
O código de operação representa o que o simpletron fará, no caso irá ler um valor (código de operação 10) e escrever o valor
na tela (código de operação 11)<br>
O operando representa qual local da memória será usada para a operação, no caso usará o endereço 98 para receber o valor
e mostra-lo na tela.<br>
Abaixo podemos ver os códigos de operação do simpletron:<br>
<div id = "ops">
<b>READ</b> = 10 (lê o valor e coloca no local especificado pelo operando)<br>
<b>WRITE</b> = 11 (Escreve na tela o valor do local especificado pelo operando)<br>
<b>LOAD</b> = 20 (Carrega valor do local especificado pelo operando para o acumulador)<br>
<b>STORE</b> = 21 (Carrega valor no acumulador para o local especificado pelo operando)<br>
<b>ADD</b> = 30 (Soma o valor no acumulador com o valor do local especificado pelo operando)<br>
<b>SUBTRACT</b> = 31 (Subtrai o valor no acumulador pelo valor do local especificado pelo operando<br>
<b>DIVIDE</b> = 32 (Dividi o valor no acumulador pelo valor do local especificado pelo operando)<br>
<b>MULTIPLY</b> = 33 (Multiplica o valor no acumulador pelo valor do local especificado pelo operando<br>
<b>MODULOS</b> = 34 (Faz módulo do valor no acumulador pelo valor do local especificado pelo operando<br>
<b>BRANCH</b> = 40 (Vai para a instrução especificada pelo operando)<br>
<b>BRANCHNEG</b> = 41 (Vai para a instrução especificada pelo operando, se o valor no acumulador for negativo)<br>
<b>BRANCHZERO</b> = 42 (Vai para a instrução especificada pelo operando, se o valor no acumulador for zero)<br>
<b>HALT</b> = 43 (Finaliza o programa)<br>
BRANCH, BRANCHNEG e BRANCHZERO são instruções de transferência de controle, ou seja, eles pulam para a instrução do endereço
especificado pelo operando (lembrando que as instruções estão na lista data, não na lista list2, list2 apenas guarda variáveis)<br>
Se houverem dúvidas, deem uma olhada no arquivo Simpletron.py, ou entrem em contato comigo, ou ainda você pode procurar no github, já que aqui há vários códigos do Simpletron.
<br>Escrito por: Rulyan B. Schiavo (ranom55).<br>
Data: 26/10/2019<br>
E-mail: br-schiavo@hotmail.com<br>
</div>
