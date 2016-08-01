Title: Instalando OpenBSD em um cloud Linux
Date: 2016-08-01 16:37
Category: OpenBSD
Tags: OpenBSD, BSD, Cloud, Linux, Install
Authors: Luiz Gustavo Costa
Summary: <p align="center"><img src="/blog/images/blog/Carp.gif" /></p> Tutorial de instalação do OpenBSD em um cloud com Linux instalado, neste exemplo vamos usar o cloud (que na verdade é uma VM) da CloudAtCost.

<p align="center"><img src="/blog/images/blog/Carp.gif" /></p>

Tutorial de instalação do OpenBSD 5.9 em um cloud com Linux

É muito simples, basta ter instalado no cloud um Linux com grub2 e você também precisa ter acesso ao terminal dele, ao menos para gerenciar o boot da VM/Cloud. Com isso, vamos fazer o grub carregar na memória uma imagem do OpenBSD na RAM do cloud, de forma que podemos ter o disco disponivel para formatação, a instalação dos binarios é pela rede.

Vamos ao exemplo pratico, o que temos?

- Um cloud na CloudAtCost [1]
- Instalação do Ubuntu 14.4

Faça a instalação do cloud com ubuntu (ou outro linux com grub2), feita a instalação, veja se ele configurou alguma partição sem lvm (normalmente o /boot, como no exemplo abaixo)


Faça o download do arquivo bsd.rd no repositorio do OpenBSD e mova para a raiz de montagem da partição sem lvm:

    :::shell
    wget http://ftp.openbsd.org/pub/OpenBSD/5.9/amd64/bsd.rd
    mv bsd.rd /boot/

Feito isso, adicione a entrada abaixo no arquivo /etc/grub.d/40_custom

    :::shell
    menuentry "Install OpenBSD from RAM disk" {
     set root=(hd0,1)
     kopenbsd /bsd.rd
    }

É recomendavel também que você aumente o tempo de timeout do grub no arquivo /etc/default/grub para que você possa escolher a opção de carregar o openbsd na memoria.

Agora, gere uma nova configuração do grub com o comando abaixo:

    update-grub

Reinicie o cloud

    reboot

E pronto !! na hora do boot, no menu do grub, escolha a opção "Install OpenBSD" e faça a instalação dele !

[1] http://www.cloudatcost.com/

Fonte essencial para isso: http://openbsd-archive.7691.n7.nabble.com/how-to-install-OpenBSD-in-a-computer-with-Linux-and-Grub2-td41148.html

Qualquer dúvida, só postar ai nos comentários.

Abraços
