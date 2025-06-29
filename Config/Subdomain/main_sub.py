import os

def kitterunner(domain):
    print("""
 _ __ _    _
| / /<_> _| |_  ___  _ _  _ _ ._ _ ._ _  ___  _ _
|  \\ | |  | |  / ._>| '_>| | || ' || ' |/ ._>| '_>
|_\\_\\|_|  |_|  \\___.|_|  `___||_|_||_|_|\\___.|_|

O kitte é uma ferramenta que faz fuzzing e scan ou brute de API's em sites.

/usr/bin/routes-large.kite
/usr/bin/routes-small.json

Comandos:
[0] Pré-Pronto: kr scan <domain> -w /usr/bin/routes-large.kite -A=apiroutes-210228:20000 -x 10 --ignore-length=34
[1] Brute: kr brute <domain> -A=raft-large-words -A=apiroutes-210228:20000 -x 10 -d=0 --ignore-length=34 -ejson,txt
[2] Monte seu comando.

-h, --help: ajuda
-o, --output:  formato de saída de string. pode ser json,text,pretty (padrão "pretty")
-q, --quiet modo silencioso: silenciará o "texto bonito" desnecessário
-v, --verbose nível de string de verbosidade de registro. pode ser erro,info,debug,trace (padrão "info")

brute: brute um ou vários hosts com uma lista de palavras fornecida
help: Ajuda sobre qualquer comando
kb: Manipula o esquema do kitebuilder
scan: Escaneia um ou vários hosts com uma lista de palavras fornecida
version: Versão do binário que você está executando
wordlist: Olha suas listas de palavras em cache e listas de palavras remotas\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            print(f"Comando executado: kr scan {domain} -w /usr/bin/routes-large.kite -A=apiroutes-210228:20000 -x 10 --ignore-length=34")
            os.system(f"kr scan {domain} -w /usr/bin/routes-large.kite -A=apiroutes-210228:20000 -x 10 --ignore-length=34")
        case 1:
            print(f"Comando executado: kr brute {domain} -A=raft-large-words -A=apiroutes-210228:20000 -x 10 -d=0 --ignore-length=34 -ejson,txt")
            os.system(f"kr brute {domain} -A=raft-large-words -A=apiroutes-210228:20000 -x 10 -d=0 --ignore-length=34 -ejson,txt")
        case _:
            shell = str(input("Seu Comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def git_api(domain):
    print("""
 ____    ___   _____
).-._(  )_ _( )__ __(
|( ,-.  _| |_   | |
)_`__( )_____(  )_(

O git search é uma ferramenta simples que serve para procurar api's de sites
dentro do github.

[0] Pré-pronto: python3 /usr/bin/github-search/<file> -t <keu> -d <domain>
[1] Github:python3 /usr/bin/github-search/github-subdomains.py -t <key> -d domaintosearch | httpx --title
[2] Monte seu comando

Opções:

1 - github-secrets.py      6 - github-users.py
2 - github-dorks.py        7 - github-subdomains.py
3 - github-employees.py    8 - github-survey.py
4 - github-endpoints.py    9 - github-survey2.py
5 - github-contributors.py\n """)
    command = int(input("Comando:"))

    match command:
        case 0:
            token = str(input("Informe seu token: "))
            file_choosen = str(input("Digite qual das opções executar: "))
            print(f"Comando executado: python3 /usr/bin/github-search/{file_choosen} -t {token} -d {domain}")
            os.system(f"python3 /usr/bin/github-search/{file_choosen} -t {token} -d {domain}")
        case 1:
            token = str(input("Informe seu token: "))
            print(f"Comando executado: python3 /usr/bin/github-search/github-subdomains.py -t {token} -d {domain}| httpx --title")
            os.system(f"python3 /usr/bin/github-search/github-subdomains.py -t {token} -d {domain}| httpx --title")
        case _:
            shell = str(input("Seu Comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def git_dorker(domain):
    print("""
  /$$$$$$  /$$   /$$           /$$$$$$$                      /$$
 /$$__  $$|__/  | $$          | $$__  $$                    | $$
| $$  \\__/ /$$ /$$$$$$        | $$  \\ $$  /$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$   /$$$$$$
| $$ /$$$$| $$|_  $$_/        | $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$          | $$  | $$| $$  \\ $$| $$  \\__/| $$$$$$/ | $$$$$$$$| $$  \\__/
| $$  \\ $$| $$  | $$ /$$      | $$  | $$| $$  | $$| $$      | $$_  $$ | $$_____/| $$
|  $$$$$$/| $$  |  $$$$/      | $$$$$$$/|  $$$$$$/| $$      | $$ \\  $$|  $$$$$$$| $$
 \\______/ |__/   \\___/        |_______/  \\______/ |__/      |__/  \\__/ \\_______/|__/

"GitDorker é uma ferramenta que utiliza a API de pesquisa do GitHub e uma extensa lista do GitHub que compilei
de várias fontes para fornecer uma visão geral das informações confidenciais armazenadas no github com base em
uma consulta de pesquisa."

/usr/bin/GitDorker/Dorks/medium_dorks.txt
/usr/bin/GitDorker/GitDorker.py

Comandos:

[0] Pré-pronto: python3 /usr/bin/GitDorker/GitDorker.py -tf <token> -p -d <dorks> -o <domain>
[1] Monte seu comando.

-d DORKS: Arquivo dorks (obrigatório)
-k PALAVRA-CHAVE: Pesquisa em uma palavra-chave em vez de uma lista de dorks
-q CONSULTA: Consulta (obrigatório ou -q)
-ri: Classifica os resultados das consultas do mais recente primeiro
-uf USERFILE: Arquivo contendo usuários separados por nova linha
-org ORGANIZATION: Nome do GitHub da organização (obrigatório ou -org se a consulta não for especificada)
-e THREADS: Máximo de n threads, padrão 1
-p: Exibir Apenas resultados positivos
-o OUTPUT: Saída para nome do arquivo (obrigatório ou -o)\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            token = str(input("Informe seu token: "))
            print(f"Comando executado: python3 /usr/bin/GitDorker/GitDorker.py -tf {token} -p -d /usr/bin/GitDorker/Dorks/medium_dorks.txt -o {domain}")
            os.system(f"python3 /usr/bin/GitDorker/GitDorker.py -tf {token} -p -d /usr/bin/GitDorker/Dorks/medium_dorks.txt -o {domain}")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def ffuf(domain):
    print("""
 ______  ______  _    _   ______
| |     | |     | |  | | | |
| |---- | |---- | |  | | | |----
|_|     |_|     \\_|__|_| |_|

Um web fuzzer rápido escrito em Go.

Comandos:

[0] Pré-pronto: ffuf -u <domain> -w <wordlist> -t <int> -mc 200
[1] Monte seu comando:

-mc: Corresponde aos códigos de status HTTP ou "all" para tudo. (padrão: 200-299,301,302,307,401,403,405,500)
-ac: Calibrar automaticamente as opções de filtragem (padrão: false)
-acc: String de calibração automática personalizada. Pode ser usada várias vezes. Implica -ac
-ach: Autocalibração por host (padrão: false)
-ack: Palavra-chave de calibração automática (padrão: FUZZ)
-acs: Estratégias de calibração automática personalizadas. Podem ser usadas várias vezes. Implica -ac
-config: Carregar a configuração de um arquivo
-json: Saída JSON, imprimindo registros JSON delimitados por nova linha (padrão: false)
-maxtime: Tempo máximo de execução em segundos para todo o processo. (padrão: 0)
-maxtime-job: Tempo máximo de execução em segundos por trabalho. (padrão: 0)
-p: Segundos de `atraso` entre solicitações ou um intervalo de atraso aleatório. Por exemplo "0.1" ou "0,1-2,0"
-rate: Taxa de solicitações por segundo (padrão: 0)
-search: Procura por uma carga útil FFUFHASH do histórico ffuf
-sf: Para quando > 95% das respostas retornam 403 (padrão: falso)
-t: Número de threads simultâneos. (padrão: 40)

Arquivos pra Fuzzing:

0-999999-hashgen.py                                               FuzzingStrings-SkullSecurity.org.txt
1-4_all_letters_a-z.txt          doble-uri-hex.txt                HTML5sec-Injections-Jhaddix.txt
3-digits-000-999.txt             email-top-100-domains.txt        http-request-methods.txt              special-chars.txt
                                 environment-identifiers.txt      IBMMQSeries-channels.txt
4-digits-0000-9999.txt           extensions-Bo0oM.txt             JSON.Fuzzing.txt                      SSI-Injection-Jhaddix.txt
5-digits-00000-99999.txt         extensions-compressed.fuzz.txt   LDAP-active-directory-attributes.txt  template-engines-expression.txt
6-digits-000000-999999.txt       extensions-most-common.fuzz.txt  LDAP-active-directory-classes.txt     template-engines-special-vars.txt
alphanum-case-extra.txt          extensions-skipfish.fuzz.txt     LDAP.Fuzzing.txt                      Unicode.txt
alphanum-case.txt                extension-test.txt               LDAP-openldap-attributes.txt          UnixAttacks.fuzzdb.txt
                                 file-extensions-all-cases.txt    LDAP-openldap-classes.txt             URI-hex.txt
big-list-of-naughty-strings.txt  file-extensions-lower-case.txt                                         URI-XSS.fuzzdb.txt
char.txt                         file-extensions.txt              Metacharacters.fuzzdb.txt             User-Agents
command-injection-commix.txt     file-extensions-upper-case.txt   numeric-fields-only.txt               Windows-Attacks.fuzzdb.txt
country-codes-lower-case.txt     FormatString-Jhaddix.txt         os-names-mutated.txt                  XML-FUZZ.txt
country-codes.txt                fuzz-Bo0oM-friendly.txt          os-names.txt
country-codes-upper-case.txt     fuzz-Bo0oM.txt                   php-magic-methods.txt                 XXE-Fuzzing.txt \n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            file = str(input("Digite o nome do arquivo: "))
            threads = int(input("Threads: "))
            print(f"Comando executado: ffuf -u {domain}FUZZ -w /usr/share/seclists/Fuzzing{file} -t {threads}")
            os.system(f"ffuf -u {domain}FUZZ -w /usr/share/seclists/Fuzzing/{file} -t {threads}")
        case _:
            print("Algumas listas para você usar: ")
            os.system("wordlists -l")
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def gauplus(domain):
    print("""

 .oOOOo.                       o
.O     o                      O
o                             o
O                             O
O   .oOOo .oOoO' O   o  .oOo. o  O   o  .oOo
o.      O O   o  o   O  O   o O  o   O  `Ooo.
 O.    oO o   O  O   o  o   O o  O   o      O
  `OooO'  `OoO'o `OoO'o oOoO' Oo `OoO'o `OoO'
                        O
                        o'

Comandos:

[0] Pré-pronto: echo \"domain\" | gauplus -b png,jpg,gif -t <int> -random-agent -subs -o gauplus | anew
[1] Monte seu comando:

-b string: extensões para pular, ex: ttf,woff,svg,png,jpg
-json: escreve a saída como json
-o string: nome do arquivo para escrever os resultados
-p string: proxy HTTP para usar
-providers string:  provedores para buscar URLs (padrão "wayback,otx,commoncrawl")
-random-agent: usa user-agent aleatório
-subs: inclui subdomínios do domínio de destino
-t int: quantidade de workers paralelos (padrão 5)
-v habilita o modo verbose\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            threads = int(input("Threads: "))
            print(f"Comando executado: echo \"{domain}\" | gauplus -b png,jpg,gif -t {threads} -random-agent -subs -o gauplus | anew")
            os.system(f"echo \"{domain}\" | gauplus -b png,jpg,gif -t {threads} -random-agent -subs -o gauplus | anew")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def waymore(domain):
    print("""
#     #
#  #  #   ##   #   # #    #  ####  #####  ######
#  #  #  #  #   # #  ##  ## #    # #    # #
#  #  # #    #   #   # ## # #    # #    # #####
#  #  # ######   #   #    # #    # #####  #
#  #  # #    #   #   #    # #    # #   #  #
 ## ##  #    #   #   #    #  ####  #    # ######

Owaymore é uma ferramenta que busca por subdiretórios dentro do web archive.

[0] Pré-pronto: echo \"domain\" | waymore | anew | tee waymore_results
[1] -n, --no-subs: Não inclui subdomínios do domínio de destino
[2] -mode {U,R,B} O modo de execução: U (recuperar somente URLs), R (baixar somente Respostas) ou B (Ambos).
[3] -v: verbose
[4] Monte seu comando\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            print(f"Comando executado: echo \"{domain}\" | waymore | anew | tee waymore_results")
            os.system(f"echo \"{domain}\" | waymore | anew | tee waymore_results")
        case 1:
            print(f"Comando executado: echo \"{domain}\" | waymore -n | anew tee waymore_results")
            os.system(f"echo \"{domain}\" | waymore -n | anew tee waymore_results ")
        case 2:
            mode = str(input("Mode: "))
            print(f"Comando executado: echo \"{domain}\" | waymore -mode {mode}| anew | tee waymore_results")
            os.system(f"echo \"{domain}\" | waymore -mode {mode}| anew | tee waymore_results")
        case 3:
            print(f"Comando executado: echo \"{domain}\" | waymore -v | anew | tee waymore_results")
            os.system(f"echo \"{domain}\" | waymore -v | anew tee waymore_results")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def feroxbuster(domain):
    print("""
 _____                    ____            _
|  ___|__ _ __ _____  __ | __ ) _   _ ___| |_ ___ _ __
| |_ / _ \\ '__/ _ \\ \\/ / |  _ \\| | | / __| __/ _ \\ '__|
|  _|  __/ | | (_) >  <  | |_) | |_| \\__ \\ ||  __/ |
|_|  \\___|_|  \\___/_/\\_\\ |____/ \\__,_|___/\\__\\___|_|

Feroxbuster é uma das ferramentas mais rápidas de brute force de url
para ser usada!

Comandos:

[0] Pré-Pronto: feroxbuster -u {domain} -t <threads>
[1] -a: Para definir um usuário (padrão: feroxbuster/2.10.2).
[2] -f: Anexa / ao URL de cada solicitação.
[3] --dont-scan <URL>: Para excluir varreduras
[4] Monte seu código.\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            threads = int(input("Threads: "))
            print(f"Comando executado: feroxbuster -u {domain} -t {threads}")
            os.system(f"feroxbuster -u {domain} -t {threads}")

        case 1:
            version = str(input("User: "))
            print(f"Comando executado: feroxbuster -a {version} -u {domain} ")
            os.system(f"feroxbuster -a {version} -u {domain} ")

        case 2:
            print(f"Comando executado: feroxbuster -f -u {domain} ")
            os.system(f"feroxbuster -f -u {domain} ")

        case 3:
            url = str(input("Url: "))
            print(f"Comando executado: feroxbuster --dont-scan {url} -u {domain}")
            os.system(f"feroxbuster --dont-scan {url} -u {domain} ")

        case _:
            shell = str(input("Seu Comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def wfuzz(domain):
    print("""
\\ \\        /  _|
 \\ \\  \\   /  |    |   | _  / _  /
  \\ \\  \\ /   __|  |   |   /    /
   \\_/\\_/   _|   \\__,_| ___| ___|

O Wfuzz é uma ferramenta de fuzzing para testar aplicações web de forma simples e eficiente.

Comandos:

[0] Pré-Pronto: wfuzz --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ
[1] -p ip:port:type : Para uso de proxy. (SOCKS4, SOCKS5, HTTP)
[2] --script= : para uso de scripts
[3] -t <num> : Especifique o número de conexões simultâneas (10 padrão)
[4] -L : Siga redirecionamentos HTTP
[5] Método -X: Especifique um método HTTP para a solicitação, ou seja. HEAD ou FUZZ
[6] -d pós-dados: Use dados de postagem (ex: "id=FUZZ&catalogue=1")
[7] Monte seu comando.\n""")

    print("Arquivos a serem usados: ")
    os.system("ls /usr/share/wfuzz/wordlist/general/")

    command = int(input("\nComando: "))
    file = str(input("Digite o arquivo para fuzzing: "))

    match command:
        case 0:
            threads = int(input("Threads: "))
            print(f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} --hc 404 -u {domain}FUZZ -t {threads}")
            os.system(f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} --hc 404 -u {domain}FUZZ -t {threads}")

        case 1:
            proxy_config = str(input("IP:PORT:TYPE = "))
            print(
                f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -p {proxy_config} --hc 404 -u {domain}FUZZ")
            os.system(
                f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -p {proxy_config} --hc 404 -u {domain}FUZZ")

        case 2:
            scripts_list = str(input("\nListar scripts?[y/n]")).lower()
            if scripts_list == "y":
                os.system("wfuzz -e scripts")
            elif not scripts_list:
                pass

            script = str(input("\nDigite o 'name' do script: "))
            print(f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} --script={script} --hc 404 -u {domain}FUZZ")
            os.system(f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} --script={script} --hc 404 -u {domain}FUZZ")

        case 3:
            threads = int(input("Número de threads: "))
            print(f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -t {threads} --hc 404 -u {domain}FUZZ")
            os.system(
                f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -t {threads} --hc 404 -u {domain}FUZZ")

        case 4:
            print(f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -L --hc 404 -u {domain}FUZZ ")
            os.system(f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -L --hc 404 -u {domain}FUZZ")

        case 5:
            m_tod = str(input("HEAD or FUZZ: "))

            print(f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} {m_tod} -X --hc 404 -u {domain}FUZZ ")
            os.system(f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} {m_tod} -X --hc 404 -u {domain}FUZZ")

        case 6:
            dates = str(input("Dates: "))

            print(f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -d '{dates}' --hc 404 -u {domain}FUZZ ")
            os.system(f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -d '{dates}' --hc 404 -u {domain}FUZZ")

        case _:
            shell = str(input("Seu Comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def httpx(domain):
    print("""
    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \\/ __/ __/ __ \\|   /
 / / / / /_/ /_/ /_/ /   |
/_/ /_/\\__/\\__/ .___/_/|_|
             /_/

httpx é um kit de ferramentas HTTP rápido e multifuncional que permite executar vários testes
usando a biblioteca retryablehttp. Ele foi projetado para manter a confiabilidade dos resultados
com um número maior de threads.

Comandos:
[0] Pré-pronto: httpx -l <archive_list> -t <int> | anew | tee httpx_results
[1] Domain: curl -s https://dns.bufferover.run/dns?q=<domain> |jq -r .FDNS_A[] | sed -s 's/,/\n/g' | httpx -silent | anew
[2] Shodan: domain="<domain>";shodan domain $domain | awk -v domain="$domain" '{print $1"."domain}'| httpx -threads 300 | anew shodanHostsUp | xargs -I@ -P3 sh -c 'jaeles -c 300 scan -s jaeles-signatures/ -u @'| anew JaelesShodanHosts
[3] Xss-SQLI: httpx -l master.txt -silent -no-color -threads 300 -location 301,302 | awk '{print $2}' | grep -Eo '(http|https)://[^/"].*' | tr -d '[]' | anew  | xargs -I@ sh -c 'gospider -d 0 -s @' | tr ' ' '\n' | grep -Eo '(http|https)://[^/"].*' | grep "=" | qsreplace "<svg onload=alert(1)>" "'
[4] Monte seu comando.

-l, -list string: arquivo de entrada de string contendo a lista de hosts para processar
-rr, -request string: Arquivo contendo solicitação de "brute"
-u, -target string[]: Entrada de host(s) de destino para sondar\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            os.system("ls")
            archive_choosen = str(input("Caminho ou nome do arquivo: "))
            threads = int(input("Threads: "))
            print(f"Comando executado: httpx -l {archive_choosen} -t {threads} | anew | tee httpx_results")
            os.system(f"httpx -l {archive_choosen} -t {threads} | anew | tee httpx_results")

        case 1:
            print(f"Comando executado: curl -s https://dns.bufferover.run/dns?q={domain} | jq -r .FDNS_A[] | sed -s 's/,/\n/g' | httpx -silent | anew | tee httpx_results")
            os.system(f"curl -s https://dns.bufferover.run/dns?q={domain} | jq -r .FDNS_A[] | sed -s 's/,/\n/g' | httpx -silent | anew | tee httpx_results")

        case 2:
            awk = " awk -v domain=\"$domain\" '{print $1\".\"domain}'| httpx -threads 300 | anew shodanHostsUp | xargs -I@ -P3 sh -c 'jaeles -c 300 scan -s jaeles-signatures/ -u @'| anew JaelesShodanHosts | tee httpx_results"
            print(f"Comando executado: domain=\"{domain}\";shodan domain $domain | {awk} | tee httpx_results")
            os.system(f"domain=\"{domain}\";shodan domain $domain | {awk} | tee httpx_results")

        case 3:
            os.system("ls")
            lista_01 = str(input("Informe o nome ou caminho da lista:"))
            awk = "awk '{print $2}' | grep -Eo \'(http|https)://[^/\"].*\' | tr -d \'[]\' | anew  | xargs -I@ sh -c \'gospider -d 0 -s @\' | tr \' \' \'\n\' | grep -Eo \'(http|https)://[^/\"].*\' | grep \"=\" | qsreplace \"<svg onload=alert(1)>\" \"\'"
            print(f"Comando executado: httpx -l {lista_01} -silent -no-color -threads 300 -location 301,302 | {awk} | tee httpx_results")
            os.system(f"httpx -l {lista_01} -silent -no-color -threads 300 -location 301,302 | {awk} | tee httpx_results")

        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def httprobe():
    print("""
.-..-. .-.  .-.                  .-.
: :; :.' `..' `.                 : :
:    :`. .'`. .'.---. .--.  .--. : `-.  .--.
: :: : : :  : : : .; `: ..'' .; :' .; :' '_.'
:_;:_; :_;  :_; : ._.':_;  `.__.'`.__.'`.__.'
                : :
                :_;

O httprobe é uma ferramenta que pega uma lista de domínios e investigua
servidores http e https em funcionamento.

Comandos:
[0] Pré-pronto: cat <archive_file> | httprobe | tee results_httprobe
[1] Monte seu comando.

-c int: Define o nível de simultaneidade (padrão 20)
-p: Valor adiciona sonda adicional (proto:port)
-s: Ignora as sondagens padrão (http:80 e https:443)
-t int: Timeout (milissegundos) (padrão 10000)
-v: Erros de saída para stderr\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            os.system("ls")
            archive_chosen = str(input("Caminho ou nome do arquivo: "))
            print(f"Comando executado: cat {archive_chosen} | httprobe | tee results_httprobe")
            os.system(f"cat {archive_chosen} | httprobe | tee results_httprobe")
        case _:
            shell = str(input("Seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")


def aquatone():
    print("""
d s.     sSSSs   d       b d s.   sss sssss   sSSSs   d s  b d sss
S  ~O   S     S  S       S S  ~O      S      S     S  S  S S S
S   `b S       S S       S S   `b     S     S       S S   SS S
S sSSO S       S S       S S sSSO     S     S       S S    S S sSSs
S    O S       S S       S S    O     S     S       S S    S S
S    O  S   s S   S     S  S    O     S      S     S  S    S S
P    P   "sss"ss   "sss"   P    P     P       "sss"   P    P P sSSss


Aquatone é uma ferramenta para inspeção visual de sites em uma grande quantidade de hosts
e é conveniente para obter rapidamente uma visão geral da superfície de ataque baseada em HTTP.

Comandos:

[0] Pré-pronto: cat <list> | aquatone -threads <int>
[1] Monte seu comando.

-chrome-path string: Caminho completo para o executável Chrome/Chromium a ser usado.
-debug: Imprime informações de depuração
-http-timeout int: Tempo limite em milissegundos para solicitações HTTP (padrão 3000)
-nmap: Analisa a entrada como Nmap/Masscan XML
-out string: Diretório para gravar arquivos (padrão ".")
-ports string: Portas para escanear em hosts. Aliases de lista suportados: small, medium, large, xlarge (padrão "80,443,8000,8080,8443")
-proxy string: Proxy a ser usado para solicitações HTTP
-resolution string: resolução de captura de tela (padrão "1440,900")
-save-body: Salvar corpos de resposta em arquivos (padrão true)
-scan-timeout int: Tempo limite em milissegundos para varreduras de porta (padrão 100)
-screenshot-timeout int: Tempo limite em milissegundos para capturas de tela (padrão 30000)
-session string: Carregar arquivo de sessão Aquatone e gerar relatório HTML
-silent: Suprimir todas as saídas, exceto erros
-template-path string: Caminho para o modelo HTML a ser usado para o relatório
-threads int: Número de threads simultâneas (número padrão de CPUs lógicas)\n""")
    command = int(input("Comando: "))

    match command:
        case 0:
            os.system("ls")
            archive_choosen = str(input("Diretório ou nome da lista: "))
            threads = int(input("Threads: "))

            print(f"Comando executado: cat {archive_choosen} | aquatone -threads {threads}")
            os.system(f"cat {archive_choosen} | aquatone -threads {threads}")
        case _:
            os.system("ls")
            shell = str(input("Seu Comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")
