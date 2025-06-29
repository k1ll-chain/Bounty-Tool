import os

def gf(domain):
    print("""
   ,___        _   ______
  /   /o      //  (  /     o             /
 /  __.  _   //    -/--_  ,  _  _ _   __/
(___/ (_/ (_(/_   _/  / (_(_(/_/ / /_(_/_

Gf é uma ferramenta de enumeração de vulnerabilidades por parametros em diversas
urls passadas.

Sinopse:

echo "domain" | <crawler> | gf <patterns> | anew

Comandos:

[0] Pré-pronto = echo "domain" | <crawler> | gf <patterns> | anew | tee gf_result
[1] Monte seu comando

Patterns disponiveis:

1 - debug_logic     5 - interestingparams  9 - sqli     13 - ssrf
2 - idor            6 - interestingsubs    10 - rce
3 - img-traversal   7 - jsvar              11 - ssti
4 - interestingEXT  8 - lfi                12 - xss\n""")

    command = int(input("Comando: "))

    match command:
        case 0:
            crawler = str(input("Digite o crawler a ser usado: "))
            pattern = str(input("Qual pattern listado a cima deseja usar? "))

            print(f"Comando executado: echo \"{domain}\" | {crawler} | gf {pattern} | anew | tee gf_result")
            os.system(f"echo \"{domain}\" | {crawler} | gf {pattern} | anew | tee gf_result")

        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def unfurl(domain):
    print("""
╔══════════════════════════════════════════╗
║,--. ,--.         ,---.               ,--.║
║|  | |  |,--,--, /  .-',--.,--.,--.--.|  |║
║|  | |  ||      \\|  `-,|  ||  ||  .--'|  |║
║'  '-'  '|  ||  ||  .-''  ''  '|  |   |  |║
║ `-----' `--''--'`--'   `----' `--'   `--'║
╚══════════════════════════════════════════╝
O conceito do unfurl é simples, ele apenas enumera endpoints normalmente.

Sinopse:

echo "domain" | <crawler> | unfurl <key> | anew

Comandos:

[0]Pré-pronto = echo "domain" | <crawler> | unfurl <key> | anew | tee unfurl_result
[1]keys: Chaves da string de consulta (uma por linha)
[2]values: Valores da string de consulta (um por linha)
[3]keypairs: chaves Pares chave=valor da string de consulta (um por linha)
[4]domains: O nome do host (por exemplo, sub.example.com)
[5]paths: O caminho da solicitação (por exemplo, /users)
[6]apexes: O domínio apex (por exemplo, example.com de sub.example.com)
[7]json: Objetos de URL/formato codificados em JSON
[8]format: Especifique um formato personalizado (veja abaixo)
[9]Monte seu comando\n""")

    command = int(input("Comando: "))
    crawler = str(input("Digite o crawler a ser usado: "))

    match command:
        case 0:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl path | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl path | anew | tee unfurl_result")
        case 1:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl keys | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl keys | anew | tee unfurl_result")
        case 2:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl values | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl values | anew | tee unfurl_result")
        case 3:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl keypairs | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl keypairs | anew | tee unfurl_result")
        case 4:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl domains | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl domains | anew | tee unfurl_result")
        case 5:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl path | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl path | anew | tee unfurl_result")
        case 6:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl apexes | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl apexes | anew | tee unfurl_result")
        case 7:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl json | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl json | anew | tee unfurl_result")
        case 8:
            print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl format | anew | tee unfurl_result")
            os.system(f"echo \"{domain}\" | {crawler} | unfurl format | anew | tee unfurl_result")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def paramspider(domain):
    print("""
                                      _    __
   ___  ___ ________ ___ _  ___ ___  (_)__/ /__ ____
  / _ \\/ _ `/ __/ _ `/  ' \\(_-</ _ \\/ / _  / -_) __/
 / .__/\\_,_/_/  \\_,_/_/_/_/___/ .__/_/\\_,_/\\__/_/
/_/                          /_/

O paramspider é uma ferramenta de enumeração de url/vuls feita em python.

Comandos:

[0] Pré-Pronto: paramspider -d {domain} -s | anew | tee paramspider
[1]-d <domain>: Nome de domínio para buscar URLs relacionados.
[2]-l <list>: Arquivo contendo uma lista de nomes de domínio.
[3]-s: Transmita URLs no terminal.
[4]--proxy PROXY: Define o endereço de proxy para solicitações da web.
[5] Monte seu comando\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            print(f"Comando execultado: paramspider -d {domain} -s | anew | tee paramspider")
            os.system(f"paramspider -d {domain} -s | anew | tee paramspider")
        case 1:
            print(f"Comando executado: paramspider -d {domain} | anew | tee paramspider")
            os.system(f"paramspider -d {domain} | anew | tee paramspider")
        case 2:
            archive_list = str(input("Caminho da lista: "))
            print(f"Comando executado: paramspider -d {domain} -l {archive_list} | anew | tee paramspider")
            os.system(f"paramspider -d {domain} -l {archive_list} | anew | tee paramspider")
        case 3:
            print(f"Comando executado: paramspider -s -d {domain} | anew | tee paramspider")
            os.system(f"paramspider -s -d {domain} | anew | tee paramspider")
        case 4:
            prox = str(input("Digite o proxy a ser usado: "))
            print(f"Comando executado: paramspider -d {domain} --proxy {prox} | anew | tee paramspider")
            os.system(f"paramspider -d {domain} --proxy {prox} | anew | tee paramspider")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def arjun(domain):
    print("""
    _
   /_| _ '
  (  |/ /(//) v2.2.6
      _/
Arjun serve para encontra parâmetros de endpoints de URL.

Comandos:

[0] Pré-Pronto: arjun -u {domain} -o arjun.txt -t <int> -d 1
[1] Monte seu comando.

-u: Url de desinto
-o JSON_FILE: Salva o resultado em um arquivo json (-oT para texto)
-oB [BURP_PROXY]: Saída para o Burp Suite Proxy. O padrão é 127.0.0.1:8080.
-d DELAY Atraso: entre solicitações em segundos. (padrão: 0)
-t THREADS: Número de threads simultâneas. (padrão: 5)
-w WORDLIST: Caminho do arquivo da lista de palavras. (padrão: {arjundir}/db/large.txt).
-stable: Prefira estabilidade à velocidade.
--disable-redirects: desabilita redirecionamento\n""")
    command = int(input("Monte seu comando: "))

    match command:
        case 0:
            threads = int(input("Threads: "))
            print(f"Comando executado: arjun -u {domain} -o arjun.txt -t {threads} -d 1")
            os.system(f"arjun -u {domain} -o arjun.txt -t {threads} -d 1")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def subjs(domain):
    print("""
  >=>>=>            >=>
>=>    >=>          >=>         >=>
 >=>       >=>  >=> >=>              >===>
   >=>     >=>  >=> >=>>==>     >=> >=>
      >=>  >=>  >=> >=>  >=>    >=>   >==>
>=>    >=> >=>  >=> >=>  >=>    >=>     >=>
  >=>>=>     >==>=> >=>>==>     >=> >=> >=>
                             >==>

Subjs busca arquivos javascript de uma lista de URLS ou subdomínios.
A análise de arquivos javascript pode ajudá-lo a encontrar endpoints não documentados, segredos e mais


Comandos:

[0] Pré-Pronto: echo \"domain\" | gauplus -t <int> -b png,jpg,gif -subs | subjs | anew js | tee subjs_result
[1]-c int: Número de threads simultâneos (padrão 10)
[2]-i string: Arquivo de entrada contendo URLS
[3]-t int: Tempo limite (em segundos) para cliente http (padrão 15)
[4]-ua string: User-Agent para enviar solicitações
[5] Monte seu comando.\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            threads = int(input("Threads: "))
            print(f"Comando executado: echo \"{domain}\" | gauplus -t {threads} -b png,jpg,gif -subs | subjs -c {threads}| anew js | tee subjs_result")
            os.system(f"echo \"{domain}\" | gauplus -t {threads} -b png,jpg,gif -subs | subjs -c {threads} | anew js | tee subjs_result")
        case 1:
            threads = int(input("Número de threads: "))
            print(f"Comando executado: echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -c {threads} | anew js | tee subjs_result")
            os.system(f"echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -c {threads} | anew js | tee subjs_result")
        case 2:
            archive_url = str(input("Caminho do arquivo url: "))
            print(f"Comando executado: echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -i {archive_url} | anew js | tee subjs_result")
            os.system(f"echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -i {archive_url} | anew js | tee subjs_result")
        case 3:
            time_laps = int(input("Número de tempo: "))
            print(f"Comando executado: echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -t {time_laps} | anew js | tee subjs_result")
            os.system(f"echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -t {time_laps} | anew js | tee subjs_result")
        case 4:
            user_agent = str(input("Número de threads: "))
            print(f"Comando executado: echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -ua {user_agent} | anew js | tee subjs_result")
            os.system(f"echo \"{domain}\" | gauplus -b png,jpg,gif -subs | subjs -ua {user_agent} | anew js | tee subjs_result")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def anti_burl():
    print("""
.______  .______  _____._.___
:      \\ :      \\ \\__ _:|: __|
|   .   ||       |  |  :|| : |
|   :   ||   |   |  |   ||   |
|___|   ||___|   |  |   ||   |
    |___|    |___|  |___||___|

O anti-burl é uma ferramenta de validação de arquivos js.

Comandos:

[0] Pré-Pronto: cat <archive_js> | anti-burl | awk '{print $4}' | anew js200 | tee anti_burl_result
[1] Monte seu comando.\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            archive_js = str(input("Diretório do arquivo com as url .js: "))
            awk = "'{print $4}'"
            print(f"Comando executado: cat {archive_js} | anti-burl | awk {awk} | anew js200 | tee anti_burl_result ",)
            os.system(f"cat {archive_js} | anti-burl | awk {awk} | anew js200 | tee anti_burl_resultt")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def amass(domain):
    print("""
        .+++:.         :++:                             .+++.       .+++.
      +W@@@@@@8        &+W@#               o8W8:      +W@@@@@@#.   oW@@@W#+
     &@#+   .o@##.    .@@@o@W.o@@o       :@@#&W8o    .@#:  .:oW+  .@#+++&#&
    +@&        &@&     #@8 +@W@&8@+     :@W.   +@8   +@:          .@8
    8@          @@     8@o  8@8  WW    .@W      W@+  .@W.          o@#:
    WW          &@o    &@:  o@+  o@+   #@.      8@o   +W@#+.        +W@8:
    #@          :@W    &@+  &@+   @8  :@o       o@o     oW@@W+        oW@8
    o@+          @@&   &@+  &@+   #@  &@.      .W@W       .+#@&         o@W.
     WW         +@W@8. &@+  :&    o@+ #@      :@W&@&         &@:  ..     :@o
     :@W:      o@# +Wo &@+        :W: +@W&o++o@W. &@&  8@#o+&@W.  #@:    o@+
      :W@@WWWW@@8       +              :&W@@@@&    &W  .o#@@W&.   :W@WWW@@&
        +o&&&&+.                                                    +oooo.

O amass é uma ferramenta de enumeração de subdominios e asn.

Comandos:

[0] Pré-Pronto: amass enum -d domain -o amass_scan_01 | anew
[1] Monte seu comando.

* amass intel - Descubra alvos para enumerações
* amass enum - Execute enumerações e mapeamento de rede\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            print(f"Comando executado: amass enum -d {domain} -o amass_scan_01 | anew")
            os.system(f"amass enum -d {domain} -o amass_scan_01 | anew")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def metabigor(domain):
    print("""
 _ _ _
' ) ) )   _/_      /
 / / / _  /  __.  /__o _,  __ __
/ ' (_</_<__(_/|_/_)<_(_)_(_)/ (_
                       /|
                      |/

Metabigor é uma ferramenta de Inteligência, seu objetivo é realizar tarefas OSINT e muito mais
,mas sem nenhuma chave de API.

Comandos:

[0] Pré-Pronto: echo \"domain\" | metabigor related -o metabigor_result_01 | anew
[1] Monte seu comando.

cert: Pesquisa de certificados
conclusion: Gera o script de preenchimento automático para o shell especificado
help: Ajuda sobre qualquer comando
ip: Extrai Shodan IPInfo de internetdb.shodan.io
ipc: Resumo sobre a lista de IP
net: Descobre informações de rede sobre alvos (o mesmo com o comando net, mas usa dados estáticos)
netd: Descobre informações de rede sobre alvos (semelhante ao comando 'net', mas usa dados de terceiros)
related: Encontra mais domínios relacionados do alvo aplicando várias técnicas
scan Wrapper: para executar varredura de porta a partir da entrada fornecida

* -c int: simultaneidade (padrão 5)
* --debug: Depurar
* -h: Ajuda do metabigor
* -i strings: Entrada para executar
* -I string:  Arquivo de entrada
* -J: Saída como JSON
* -o string: Arquivo de saída
* --proxy: string Proxy para fazer solicitação
* -q: Mostrar apenas informações essenciais
* --retry int: Repetir (padrão 3)
* --timeout int: tempo limite (padrão 40)
* -T string: Pasta de saída temporária
* -v: Detalhação\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            print(f"Comando executado: echo \"{domain}\" | metabigor related -o metabigor_result_01 | anew")
            os.system(f" echo \"{domain}\" | metabigor related -o metabigor_result_01 | anew")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")
