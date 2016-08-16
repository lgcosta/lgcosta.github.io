Title: Crowdfunding para implementar OAuth no CP do pfSense
Date: 2016-08-16 11:50
Category: pfSense
Tags: FreeBSD, pfSense, Crowdfunding
Authors: Luiz Gustavo Costa
Summary: <p align="center"><img src="/blog/images/blog/mutual-funds.jpg" /></p> Campanha de Crowdfunding para o desenvolvimento de um patch para implementar a autenticação via oauth (Facebook, Google, etc) no captive portal do pfSense.

<p align="center"><img src="/blog/images/blog/mutual-funds.jpg" /></p>

Crowdfunding para implementar OAuth no CP do pfSense

A ideia é fazer um post de arrecadação para financiar horas de desenvolvimento de implantação de mecanismo de autenticação OAuth no Captive Portal do pfSense nas versões de demanda (via comentários no final da página), levando em conta a ultima versão 2.3.2.

A autenticação via OAuth vai permitir a integração com vários portais de integração de login, como:

- Facebook
- Google (Gmail)
- Github
- Entre outros que usem o mecanismo OAuth

O que vai ser desenvolvido?

- Página de configuração para a integração OAuth dos portais
- Página de login personalizavel.
- Página de "Termos de uso"
- Engine de integração do OAuth
- Engine de relatorio de acesso
- Integração do login com Proxy (??? demanda ???)

*A implementação do patch vai ser livre ?*

Sim, a ideia do Crowdfunding é somente a de financiar as horas de trabalho envolvidas no código, testes, e suporte. Todo o código estará disponivel sob licença BSD (ou beerware [1] -- como preferir) e seus arquivos estarão versionados no Gitlab.

[1] https://pt.wikipedia.org/wiki/Beerware

*Porque não usar um portal de Crowdfunding ?*

Porque eles tem um custo, ou melhor, uma comissão e toda uma burocracia para pagamentos, como se trata de uma implementação que não é muito grande, não vejo porque não faze-lo diretamente.

E estarei atualizando no final desse post uma lista dos contribuidores do Crowdfunding.

*Como faço para fazer a contribuição ?*

Você tem duas opções:

Paypal:

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
    <input name="cmd" value="_s-xclick" type="hidden">
    <input name="hosted_button_id" value="9Q729XTN5PJ2S" type="hidden">
    <input src="https://www.paypalobjects.com/pt_BR/BR/i/btn/btn_donateCC_LG.gif" name="submit" alt="PayPal - A maneira fácil e segura de enviar pagamentos online!" type="image" border="0">
    <img alt="" src="https://www.paypalobjects.com/pt_BR/i/scr/pixel.gif" height="1" width="1" border="0">
</form>

Via transferencia bancaria:

    Nr. banco: 001
    Banco do Brasil
    AG: 4398-2
    C/C: 10613-5
    Luiz Gustavo dos Santos Costa
    CPF: 084.219.847-48

Qualquer dúvida, deixe mensagem nos comentários aqui no final do post.

*Contribuidores:*

lista_de_contribuidores
