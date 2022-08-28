---
Links: [[000 - Index|home]]
Tags: #hacking, #blog
title: "Infosec: por onde começar ?"
published: 2022-08-27
---

# Infosec: por onde começar ?

<br><br>
### Whoami ?
Meu nome é Leonardo, sou estudante de ciência da computação, técnico em telecomunicações e entusiasta em segurança de informação. Gosto de **programação**, **eletrônica**, **engenharia reversa(reverse engineer RE)** e ... pra ser mais sincero, **gosto de computação de forma geral**, mas estes são os princiais xD.

Como estive dando voltas no meu aprendizado sobre infosec, decidi inciar uma jornada de aprendizado(um "walkthrough") e pretendo utilizar este blog para divulgar o meu progresso e poder compartilhar o pouco que eu sei sobre **infosec/cybersecurity**.

A vida é uma jornada de aprendizado e todo conhecimento é bem-vindo, sinta-se livre para criticar os posts. Serei grato pelas correções e opiniões :D.


### Onde começar ?

Bom, "por onde começar ?" é uma pergunta que devemos fazer antes de iniciar essa jornada maluca de hacking, até porque existem muitos sites, conteúdos e informações, o que  pode deixar qualquer iniciante bemmm perdido(me incluo nisso xD) !

<div style="width:100%;height:0;padding-bottom:84%;position:relative;"><iframe src="https://giphy.com/embed/BoQiOO2AzHjUvLGRes" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/theoffice-episode-3-the-office-tv-BoQiOO2AzHjUvLGRes">via GIPHY</a></p>


Provavelmente você já tenha pesquisado sobre como começar em outros locais e tenha se deparado com o termo capture the flag(ou CTF para os mais íntimos 😏) e sites populares como [hack the box](http://hackthebox.com/) e [try hack me](https://tryhackme.com/). CTFs são desafios de hacking(ah num diga ?) com o objetivo de testar suas habilidades em áreas específicas como engenharia reversa, desenvolvimento de exploits, teste de exploração(pentest), criptografia e afins. CTFs são uma das melhores formas de por em prática suas habilidades, contudo, pode ser desafiador até demais para iniciantes com pouco conhecimento em TI começarem pelos sites mais populares, sendo assim, proponho um início um pouco diferente, utilizando WeChall.net e OverTheWire.org, dois sites antigos da comunidade, mas pouco divulgados.


###### WeChall.net
WeChall.net é um site que hospeda diversos desafios, sendo uma comunidade relativamente ativa que contém um hub de sites de CTFs, você pode utiliza-lo para encontrar desafios específicos por tipo e difículdade.


![alt text](/static/img/wechall.png "WeChall.org")

###### OverTheWire.org  

OverTheWire.org é um site conhecido da comunidade, porém pouco divulgado para iniciantes. *Ele* possui Wargames(CTFs) que vão desde de desafios simples até os mais avançados, conténdo níveis de dificuldades dentro de uma mesma Wargame que vai escalando conforme você passa de fase.

![alt text](/static/img/overthewire.png "OverTheWire.org")

O CTF que requer conhecimentos mais básicos no site é o **bandit**, ele irá testar suas habilidades utilizando o shell Linux, sendo uma base necessária para jogar outros CTFs ! Vale lembrar que podemos utilizar o WeChall em conjunto com o Overthewire para exibir nosso progresso e pontuação no sistema de ranking do WeChall, maneiro não ? 😉

Obviamente, os comandos que você irá executar serão na máquina host do CTF, mas a recomendação aqui é para que você possa progresseguir com seus estudos além do CTF !

Beleza, então irei listar sobre o que iremos precisar para começar:

-  <s>2 xícaras (chá) de açúcar</s>
-  <s>3 xícaras (chá) de farinha de trigo</s>
-  <s>3 ovos</s>
- Uma máquina **Linux**. Não é obrigatório no começo, mas é o recomendado, pois a maior parte dos CTFs requer habilidades utilizando-o, então recomendo que tenha uma VM ou ao menos utilize o WSL para praticar 🙂.
- Acesso **SSH**(calma, irei explicar). Se você tem alguma máquina Linux, então com certeza você já tem as ferramentas necessárias xD.
- Criar uma conta no Wechall.
- Estar pronto 😤🤯.

##### Preparação
- 0 - Então vamos lá, crie sua conta no Wechall e siga as instruções de [scoreboard do over the wire](https://overthewire.org/information/wechall.html) junto comigo. Primeiro você irá acessar Account > Warbox e copiar o seu WarToken.

![alt text](/static/img/wechall_warbox.png "Configuração de warbox do Wechall")


- 1 - Com seu WarToken em mãos edite o arquivo ~/.bashrc e adicione ao final as seguintes variáveis de ambiente, adicionando o seu nome de usuário e o token que você recuperou.

```bash
export WECHALLUSER="YourUserName" # O seu nomde de usuário no wechall
export WECHALLTOKEN="YOUR-WECHALL-TOKEN-HERE" # o war token aqui!
```

- 2 - Agora edite(ou crie se não existir) o arquivo de configuração de ssh em ~/.ssh/config e adicione no arquivo essa configuração:

```bash
Host *.labs.overthewire.org
  SendEnv WECHALLTOKEN
  SendEnv WECHALLUSER
```

Essa configuração irá enviar o seu nome de usuário e token para os CTFs do over the wire toda vez que você se conectar em algum, sendo possível agora registrar seu progresso em um nível utilizando o comando **wechall** no terminal !

- 3 - Agora vamos linkar a conta do Wechall ao site do OverThewire acessando Account > Linked Sites, você irá informar o site, usuário e email e clicar em **Link Site**, com isso você conseguira exibir sua pontuação no seu perfíl de usuário !

![alt text](/static/img/wechall_linksite.png "Linkando um site no Wechall.")

Antes de tudo, caso tenha algum problema de conexão com o CTF, recomendo ler as [informações da página](https://overthewire.org/wargames/bandit/). Existem algumas explicações de como contornar o problema.



Agora, vamos ao que interessa !


<div style="width:100%;height:0;padding-bottom:50%;position:relative;"><iframe src="https://giphy.com/embed/LcfBYS8BKhCvK" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/LcfBYS8BKhCvK">via GIPHY</a></p>

### Overthewire - bandit

Os Wargames do Overthewire são compostos por diferentes níveis, sendo nível 0 o mais básico.
O objetivo é resolver o desafio do nível e conseguir a chave de acesso paro o próximo nível, essas chaves de acesso são conhecidas como flags(dai o nome capture the flag XD), seu formato pode variar de acordo com o CTF, mas no geral possuem o formato de um hash ou de uma cadeia de caracteres comuns.

![alt text](/static/img/bandit0_description.png "Descrição do Bandit no level 0.")

**Cada nível é composto por um usuário e uma senha**, sendo no nível 0  **bandit0** para ambos. Para termo acesso aos níveis seguintes, **devemos utilizar a chave de acesso encontrada no nível anterior como senha e o nível a ser acessado como usuário(ex.: bandit1).**

Para nos conectarmos ao servidor do bandit iremos utilizar o protocolo SSH. O ssh é bem comum nos CTFs, sendo normalmente a principal forma de conexão, porém não irei explicar em detalhes o seu funcionamento já que não é o foco principal aqui, então deixarei para alguma publicação futura. A sua forma mais simples de uso é informar o usuário, o endereço do servidor e a porta de conexão, caso não informa a porta ele irá se conectar na porta padrão.

A baixo temos o exemplo de utilização:

```bash
# troque user, host e port pelos valores desejados:
ssh <user>@<host> -p <port>

# Use isso para se conectar no nível 0:
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

Agora vamos nos conectar ao servidor:

![alt text](/static/img/bandit_print0.png " ")

Ao acessar o servidor, irá aparecer um banner de conexão e algumas informações sobre o servidor:

![alt text](/static/img/bandit_print1.png " ")


Se você leu a [descrição do nível](https://overthewire.org/wargames/bandit/bandit0.html), perceberá que existe uma descrição de possíveis comandos para serem utilizados em cada nível, além de uma explicação sobre o problema.

![alt text](/static/img/bandit_print2.png " ")

Com base nas referências da descrição, os comandos a serem utilizados são o **ls** e **cat**. O comando ls significa list directory, ele serve como o nome descreve, para listar estruturas de diretórios(pastas) no linux, já o cat é responsável por concatenar arquivos para o output(saída) do terminal, de forma simples, ele irá exibir o conteúdo do arquivo. Essa é uma explicação bem breve sobre essas duas ferramentas, porém elas são muito mais poderosas.

Agora podemos resolver o desafio com base nos comandos **ls** e **cat** da seguinte forma:

![alt text](/static/img/bandit_print3.png " ")


Agora execute o comando **wechall** para atualizar seus pontos no wechall:

<!-- \<img\> -->

Com isso nós obtemos a flag e podemos processeguir para o próximo nível !
Esse nível é bem simples, como pode ver, mas  eu não iria te spoilar e passar a flag né 🤣. Para os próximos níveis  irei dar uma explicação sobre o que cada comando faz e dicas, assim evito acabar com agraça,  como os criadores do CTF pedem 🙃:

![alt text](/static/img/bandit_print4.png " ")

Eventualmente irei ser mais detalhista em alguns níveis e colocarei o writeup completo, porém recomendo que tente resolver o desafio antes de ler alguma dica ou mesmo o writeup por completo, assim você conseguirá progredir. Além disso, por favor, siga as boas práticas e regras do servidor e não publique as flags !


Bom, é isso pessoal, até uma próxima !


![alt text](/static/img/gaguinho_meme.png " ")





