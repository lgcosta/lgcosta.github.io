Title: Lançado o Centreon 2.6
Date: 2015-04-22 08:00
Category: Monitoramento
Tags: Centreon, PHP, Nagios, Monitoramento

Hoje foi feito oficialmente o lançamento da versão 2.6 do Centreon.

Eu fiz abaixo uma tradução livre do [post original](https://blog.centreon.com/centreon-2-6-released-today/), acompanhe:

![Centreon Logo](/blog/images/blog/centreon_logo.png "Centreon")

### Experiência do usuário aprimorada e melhor exploração do ambiente...

Centreon 2.6 oferece uma série de melhorias e aprimoramentos para permanecer 
fiel ao que os usuários de longa data mais esperam sobre o Centreon, em destaque:

- Escalabilidade continua em termos de uso
- Melhor controle do usuário e adaptabilidade
- Configuração mais fácil no uso geral
- Adicionais de compatibilidade com os padrões da indústria de código aberto

### Continua Escalabilidade de Usuário

Gerenciamento de ACL foi melhorada para permitir um maior número de usuários 
simultâneos para trabalharem na mesma plataforma de monitoramento. 
Com o lançamento do 2.6, Centreon está aumentando esses limites ainda mais.

Agora você pode esperar de forma razoável, a ter 30 usuários que exploram 
a mesma plataforma de monitoramento, trabalhando em mais de 200 mil checagens a cada vez.

### Melhor de Controle do Usuário

Uma das maiores vantagens da utilização de código aberto está na flexibilidade 
para adaptar as suas capacidades técnicas ao nível do contexto do usuário e ambiente. 
No Centreon, mantemos essa vantagem e para oferecermos tais capacidades para nossos usuários.

Na versão 2.6, um desses recursos é permitir que você possa promover traps SNMP com 
execução do Centreontrapd. Você tem agora a possibilidade de:

- Transformar ou adaptar uma mensagem de saída de um trap SNMP, por exemplo, para padronizar as mensagens de saída de acordo com o que você precisa para monitorar;
- Executar um código específico vinculado à uma mensagem de um trap SNMP, para acionar, por exemplo, algum serviço ou reiniciar processo;
- Desconsiderar alguns traps SNMP de um host específico quando é declarada um tempo de inatividade.

Outro exemplo, 2.6 permite reconstruir de forma eficiente a sua visão de 
relatórios no caso de perda de informações devido a um incidente. 
Centreon 2.6 faz isso executando uma simples análise do banco de dados de log 
para regerar eventos necessários para a reconstrução. 
Tudo que você precisa fazer é especificar uma data de início do incidente para recuperar as 
informações necessárias. Dessa forma, a análise de todo o banco de dados 
não é mais necessário e você economiza tempo e recursos.

### Mais fácil de configurar

A configuração é simplificada com o lançamento da versão 2.6, para alcançar 
uma integração homogénea com alterações óbvias para o ambiente de monitoramento existente.

- Centreon 2.6 introduz a capacidade para os serviços dependentes de uma série de herdar automaticamente a sua criticidade configurado. Também é possível definir os níveis de criticidade global de um determinado host e de cluster serviços dependentes, graças à utilização de templates.

- Compatibilidade com a versão 5.4 do PHP

Fãs de Debian 6, Ubuntu 13.04, Redhat 7 e CentOS 7 vai apreciar a nova compatibilidade da versão 5.4 do PHP
para a interface de usuário do Centreon 2.6.

A instalação do Centreon 2.6 para versão Entreprise é muito simples
e de forma rápida, terá um ambiente de monitoramento homogêneo, distribuído e seguro!

Disponibilizado pela primeira vez na versão 2.6, a compatibilidade PHP é planejada
como uma melhoria ao longo do tempo para todos os produtos Centreon, de forma gradual e segura.

Veja mais detalhes:

[Notas de lançamento](https://documentation.centreon.com/docs/centreon/en/2.6.x/release_notes/centreon-2.6.0.html)

[Download](https://download.centreon.com/?tab=Centreon%20UI)
