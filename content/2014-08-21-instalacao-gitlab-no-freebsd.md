Title: Instalação Gitlab no FreeBSD
Date: 2014-08-21 08:03
Category: Gerenciamento
Tags: Gitlab, Freebsd

![Gitlab Logo](/blog/images/gitlab_logo.png "Gitlab Logo")

O que é Gitlab ?
----------------

Gitlab é um gerenciador de repositorio GIT para o ambiente WEB com a maioria das opções oferecidas pelo o Github. Com o Gitlab você terá a oportunidade de ter seu próprio gerenciador de repositorio, no seu ambiente de trabalho. O projeto é desenvolvido em Ruby com o framework Ruby on Rails.

Veja mais detalhes no site do projeto: https://about.gitlab.org

#### O que vamos usar ?

Instalação pura do:

*FreeBSD 10 amd64 - GENERIC*

    # uname -a
    FreeBSD gitlab.gugabsd 10.0-RELEASE FreeBSD 10.0-RELEASE #0 r260789: Thu Jan 16 22:34:59 UTC 2014     root@snap.freebsd.org:/usr/obj/usr/src/sys/GENERIC  amd64

*Gitlab 7.1 Stable*

#### O que vamos precisar ?

Vamos usar o gerenciador de pacotes binarios PKG para suprir nossa demanda de pacotes dependentes do Gitlab, para isso, execute o comando abaixo para atualizar o pkg:

    :::text
    root@gitlab:~ # pkg update
    
    
    The package management tool is not yet installed on your system.
    Do you want to fetch and install it now? [y/N]: y
    Bootstrapping pkg from pkg+http://pkg.FreeBSD.org/freebsd:10:x86:64/latest, please wait...
    Verifying signature with trusted certificate pkg.freebsd.org.2013102301... done
    Installing pkg-1.3.6: 100%
    Message for pkg-1.3.6:
     If you are upgrading from the old package format, first run:
    
      # pkg2ng
    Updating repository catalogue
    Fetching meta.txz: 100% of 944 B                                                                   
    Fetching digests.txz: 100% of 2 MB                                                                  
    Fetching packagesite.txz: 100% of 5 MB                                                              
    
    Adding new entries: 100%
    Incremental update completed, 23436 packages processed:
    0 packages updated, 0 removed and 23436 added.

Feito isto, estamos preparado para instalar os pacotes necessários:

    pkg install -y git redis icu libxml2 libxslt python2 bash sudo gcc gmake

Para o RVM (veremos abaixo):

    pkg install -y autoconf automake libtool bison readline libyaml sqlite3 gdbm cmake pkgconf

Vamos ligar nosso servidor Redis:

    :::shell
    echo 'redis_enable="YES"' >> /etc/rc.conf
    /usr/local/etc/rc.d/redis start
    Starting redis.

Nesse tutorial, vou fazer uso do Postgresql como base de dados do Gitlab, porém, o Gitlab também é compativel com Mysql, fica a seu criterio:

    :::shell
    pkg install -y postgresql92-server
    echo 'postgresql_enable="YES"' >> /etc/rc.conf
    /usr/local/etc/rc.d/postgresql initdb
    /usr/local/etc/rc.d/postgresql start

Crie a base que iremos usar com o Gitlab:

    :::shell
    root@gitlab:~ # su - pgsql
    $ psql -d template1
    psql (9.2.9)
    Type "help" for help.

    template1=# CREATE USER git CREATEDB;
    CREATE ROLE
    template1=# CREATE DATABASE gitlabhq_production OWNER git;
    CREATE DATABASE
    template1=# \q

Como vamos "enjaular" tudo em um usuário do sistema, vamos cria-lo no FreeBSD com o comando abaixo:

    pw add user -n git -m -s /usr/local/bin/bash -c "GitLab"

E com o usuário criado, vamos fazer o uso do Ruby, que é a linguagem de construção do Gitlab através do RVM. Para isto, vamos virar usuário `git` e instalar o ambiente do RVM com uma versão do ruby:

    root@gitlab:~ # su - git
    [git@gitlab ~]$ 
    [git@gitlab ~]$ \curl -sSL https://get.rvm.io | bash -s stable

    source /home/git/.rvm/scripts/rvm

Agora, instalar o Ruby 2.1.2 necessário para o Gitlab 7.1:

    :::bash
    rvm install 2.1.2

    ...

    Install of ruby-2.1.2 - #complete

Pronto, já estamos com o ambiente com Ruby instalado e preparado para implementar o Gitlab.

    :::shell
    [git@gitlab ~]$ which ruby
    /home/git/.rvm/rubies/ruby-2.1.2/bin/ruby
    [git@gitlab ~]$ ruby -v
    ruby 2.1.2p95 (2014-05-08 revision 45877) [x86_64-freebsd10.0]

Veja mais informações sobre o projeto RVM em: http://rvm.io/


#### Começamos então a clonar o repositorio do Gitlab:

    cd
    git clone https://gitlab.com/gitlab-org/gitlab-ce.git -b 7-1-stable gitlab

E então, começar a configurar o Gitlab:

Copie o arquivo de exemplo do Gitlab:

    cd /home/git/gitlab
    cp config/gitlab.yml.example config/gitlab.yml

`ee config/gitlab.yml`

- Altere a entrada `localhost` para o hostname/dominio completo do seu servidor, por exemplo: `gitlab.mundounix.com.br`

- Se for usar https, altere a porta de escuta de 80 para 443

- Corriga o path do usuário git no arquivo de configuração para o formato `/usr/home/git`, já que o Gitlab não se da bem com links simbolicos. Faça isso nas linhas: 199, 208, 211, 212 do arquivo.

- Atualize o cominho do binario do git para o padrão do FreeBSD: `/usr/local/bin/git` na linha 225

    cp config/unicorn.rb.example config/unicorn.rb

`ee config/unicorn.rb`

- Habilite o modo "cluster" se você tiver muito acesso, aumentando o número de "workes" de acordo com a carga do seu servidor (CPU, Memória, etc)

    cp config/initializers/rack_attack.rb.example config/initializers/rack_attack.rb

Habilite a configuração da base de dados do Postgresql:

    cp config/database.yml.postgresql config/database.yml

Configure uma conta global do GIT para o usuario git do sistema:

    git config --global user.name "GitLab"
    git config --global user.email "exemplo@exemplo.com"
    git config --global core.autocrlf input

Acertando algumas permissões:

    :::bash
    chown -R git log/
    chown -R git tmp/
    chmod -R u+rwX log/
    chmod -R u+rwX tmp/
    chmod -R u+rwX tmp/pids/
    chmod -R u+rwX tmp/sockets/
    chmod -R u+rwX  public/uploads

Criando diretorios para "satellites":

    :::shell
    mkdir /home/git/gitlab-satellites
    chmod u+rwx,g=rx,o-rwx /home/git/gitlab-satellites

Vamos agora instalar os pacotes `Gems`, que são uma série de libs do Ruby necessárias para o Gitlab funcionar, usando a ferramenta bundle:

    :::shell
    gem install bundle

    export CC=gcc47
    export CXX=c++47
    export CPP=cpp47

    bundle install --deployment --without development test mysql aws

Instalação do Gitlab Shell
--------------------------

GitLab Shell é um software de acesso ssh e gerenciamento de repositório desenvolvido especialmente para GitLab.

Vá para o diretorio de instalação do Gitlab:
`cd /home/git/gitlab`

Rode uma tarefa de instalação do gitlab-shell:

    bundle exec rake gitlab:shell:install[v1.9.6] REDIS_URL=redis://localhost:6379 RAILS_ENV=production


    # Por padrão, a configuração gitlab-shell é gerado a partir de sua configuração do gitlab principal. 
    # 
    # Nota: Ao usar GitLab com HTTPS por favor alterar o seguinte: 
    # - Fornecer caminhos para os certificados ca_file e ca_path. 
    # - A opção "gitlab_url" deve apontar para o https do GitLab. 
    # - No caso de você estiver usando o certificado auto-assinado, altere a opção "self_signed_cert" para "true". 
    # Você pode rever (e modificar) a configuração gitlab-shell da seguinte forma: 
    ee /usr/home/git/gitlab-shell/config.yml

Não esqueça ainda de alterar nesse arquivo de configuração o path (caminho) do usuário *git*, de `/home/git` para `/usr/home/git` na linha 7 do arquivo.

Vamos agora inicializar a base de dados:

    bundle exec rake gitlab:setup RAILS_ENV=production

Verifique se esta tudo ok:

    bundle exec rake gitlab:env:info RAILS_ENV=production

Configure o cache de componentes web da interface (assets):

    bundle exec rake assets:precompile RAILS_ENV=production

Pronto ! Gitlab configurado, precisamos agora configurar a inicilização do mesmo:

Como root (saia do /home do git -> `exit`):

    cp /usr/home/git/gitlab/lib/support/init.d/gitlab /usr/local/etc/rc.d/gitlab.sh

Feito isso, vamos inicializar o Gitlab:

    :::shell
    root@gitlab:~ # /usr/local/etc/rc.d/gitlab.sh start
    Starting both the GitLab Unicorn and Sidekiq.
    The GitLab Unicorn web server with pid 36244 is running.
    The GitLab Sidekiq job dispatcher with pid 36271 is running.
    GitLab and all its components are up and running.

    root@gitlab:~ # ps ax |grep ruby
    36244  -  S      0:10.35 ruby: unicorn_rails master -D -c /home/git/gitlab/config/unicorn.rb -E prod
    36248  -  S      0:00.00 ruby: unicorn_rails worker[0] -D -c /home/git/gitlab/config/unicorn.rb -E p
    36249  -  S      0:00.00 ruby: unicorn_rails worker[1] -D -c /home/git/gitlab/config/unicorn.rb -E p
    36271  -  Ss     0:10.15 ruby: sidekiq 2.17.0 gitlab [0 of 25 busy] (ruby)

    root@gitlab:~ # sockstat -4l
    USER     COMMAND    PID   FD PROTO  LOCAL ADDRESS         FOREIGN ADDRESS      
    git      ruby       36249 13 tcp4   127.0.0.1:8080        *:*
    git      ruby       36248 13 tcp4   127.0.0.1:8080        *:*
    git      ruby       36244 13 tcp4   127.0.0.1:8080        *:*
    pgsql    postgres   11726 4  tcp4   127.0.0.1:5432        *:*


Vamos agora configurar um front para nosso Gitlab e para essa tarefa, vamos usar o Nginx. Porém, se você estiver familiarizado com outro servidor web, você poderá também configura-lo, basta consultar o endereço abaixo para mais informações:

https://gitlab.com/gitlab-org/gitlab-recipes/

Vamos instalar o NGINX:

    pkg install -y nginx

Copie agora o arquivo de configuração pronto do Gitlab para NGINX:

    cp /usr/home/git/gitlab/lib/support/nginx/gitlab /usr/local/etc/nginx/gitlab.conf

- Altere o arquivo de acordo com o seu hostname. *Isso é importante !*
- Na linha 59, altere a entrada do proxy_pass para o endereço interno do Gitlab: http://127.0.0.1:8080;
- Na linha 68, comente a entrada "gzip_static on;" colocando um "#" na frente. A versão do nginx compilada para o repositorio pkg não vem com suporte a gzip. Opcionalmente você poderá ativar isso compilando a versão do nginx para o ports.

Adicione agora no arquivo /usr/local/etc/nginx/nginx.conf, antes do ultimo "}", na linha 117, o include para nosso arquivo de configuração do Gitlab:

    include /usr/local/etc/nginx/gitlab.conf;

Alguns diretorios necessários para nosso ambiente:

    :::shell
    mkdir -p /var/tmp/nginx /var/log/nginx
    chown -R www: /var/log/nginx /var/tmp/nginx

E podemos agora configurar a inicialização do NGINX:

    :::shell
    # echo 'nginx_enable="YES"' >> /etc/rc.conf
    # service nginx start
    Performing sanity check on nginx configuration:
    nginx: the configuration file /usr/local/etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /usr/local/etc/nginx/nginx.conf test is successful
    Starting nginx.

Agora estamos com a configuração completa ! basta apontar seu navegador para o endereço do servidor e se logar com as credenciais padrões de inicialização:

    root
    5iveL!fe

É isso, qualquer dúvida, comente abaixo.

Referencias:

<https://gitlab.com/gitlab-org/gitlab-ce/blob/7-1-stable/doc/install/installation.md>

