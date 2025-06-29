import os

man = "Dentro da pasta da ferramenta tem todos os main's da ferramenta traduzidos em pt-br"

infos = """
Ferramentas de Reconhecimento (Discovery)

    * amass, censys, subjs: Focadas em coleta de informações sobre domínios, subdomínios, IPs e outras informações
    de infraestrutura.

    * dnsenum: Especializada em enumeração de DNS, buscando informações sobre servidores de nomes, registros e zonas.

    * host, httpx: Projetadas para verificar a existência de hosts e serviços em endereços IP ou domínios.

    * nmap: Uma das ferramentas mais versáteis, realizando varreduras de portas, detecção de serviços e identificação
    de sistemas operacionais.

    * nuclei: Motor de template para varreduras de vulnerabilidades, altamente personalizável.

Ferramentas de Varredura de Vulnerabilidades (Vulnerability Scanning)

    * dalfox, feroxbuster, ffuf: Focadas em fuzzing de parâmetros e descoberta de endpoints vulneráveis em
    aplicações web.

    * gauplus, gf/tomnomnom: Projetadas para encontrar subdomínios e realizar varreduras de portas em larga escala.

    * kitterunner: Plataforma para gerenciamento de testes de penetração e varreduras de vulnerabilidades.

    * nuclei: Além de ser um motor de templates, é também utilizado para varreduras de vulnerabilidades conhecidas
    e customizadas.

    * wpscan: Especializada em varreduras de vulnerabilidades em sites WordPress.

Ferramentas de Fuzzing e Exploração

    * arjun, dalfox, feroxbuster, ffuf: Como mencionado anteriormente, essas ferramentas são excelentes para fuzzing
    de parâmetros e descoberta de vulnerabilidades.

    * paramspider: Focada em descoberta de parâmetros HTTP e seus valores.

Ferramentas de Exploração de Diretórios e Arquivos

    * dotdotpwn: Busca por diretórios e arquivos ocultos explorando a vulnerabilidade de "dotdot".
    * feroxbuster: Além de fuzzing, também pode ser usada para descobrir diretórios e arquivos.

Ferramentas de Exploração de Git

    * gitdorker: Busca por repositórios Git públicos vazando informações sensíveis.

Ferramentas Auxiliares

    * katana: Framework para automação de tarefas de pentest.
    * metabigor: Ferramenta de coleta de informações sobre subdomínios e IPs.
    * unfurl: Ferramenta para extrair e analisar URLs e informações relacionadas.
    * xargs: Utilitário para execução de comandos em paralelo, frequentemente usado em conjunto com outras
    ferramentas para automatizar tarefas.

Observações:

    * Sobreposição: Algumas ferramentas podem se encaixar em múltiplas categorias, dependendo do contexto de uso.
    Por exemplo, nuclei é tanto um motor de templates quanto uma ferramenta de varredura de vulnerabilidades.

    * API: Muitas dessas ferramentas possuem APIs ou interfaces de programação que permitem sua integração em scripts
    e ferramentas personalizadas.

    * Scan vs. Varredura: Embora os termos "scan" e "varredura" sejam frequentemente usados como sinônimos,
    "scan" pode ter uma conotação mais ampla, enquanto "varredura" pode ser mais específico para a busca de
     vulnerabilidades."""

report = """
Template:

git clone https://github.com/fransr/template-generator.git
git clone https://github.com/EdOverflow/bug-bounty-responses.git
cp -a bug-bounty-responses/tpls/. template-generator/tpls/
cd template-generator
php -S localhost:8000

Elementos Essenciais de um Relatório:

Título Conciso e Descritivo:
   * O título deve resumir a vulnerabilidade de forma clara e objetiva.
   Exemplo: "SQL Injection na página de login do sistema de e-commerce".

Descrição Detalhada:
    * Passo a passo para reproduzir o problema: Descreva cada etapa de forma clara e concisa,
    utilizando uma linguagem técnica quando necessário.

    * Impacto da vulnerabilidade: Explique as consequências da exploração da vulnerabilidade,
    como por exemplo, acesso não autorizado a dados sensíveis, execução de código arbitrário
    ou negação de serviço.

    Evidências: Inclua screenshots, vídeos, logs de rede ou outros tipos de evidências que comprovem
    a existência da vulnerabilidade.

Informações Técnicas:
    * Tipo de vulnerabilidade: Especifique o tipo de vulnerabilidade (SQL Injection, XSS, CSRF, etc.)
    e as referências a padrões de segurança relevantes (OWASP Top 10, CWE).

    * Versões de software e hardware: Indique as versões dos softwares e hardware envolvidos, pois isso
     pode ajudar a identificar se a vulnerabilidade já foi corrigida em versões mais recentes.

    * Gravidade: Avalie a gravidade da vulnerabilidade com base no impacto potencial e na facilidade
     de exploração. Utilize uma escala de severidade padrão (crítica, alta, média, baixa).

    * Recomendações: Sugira soluções para corrigir a vulnerabilidade, como patches, atualizações de software
     ou mudanças no código.

Dicas Adicionais:

    Seja claro e objetivo: Evite jargões técnicos excessivos e utilize uma linguagem clara e concisa.
    Organize as informações: Utilize uma estrutura lógica para o seu relatório, facilitando a compreensão do leitor.
    Priorize as informações mais importantes: Destaque as informações mais relevantes para a equipe de desenvolvimento.
    Seja profissional: Mantenha um tom profissional e respeitoso em todo o relatório.
    Utilize ferramentas de relatório: Existem diversas ferramentas que podem auxiliar na criação de relatórios de bug bounty, como plataformas de bug bounty e ferramentas de gerenciamento de vulnerabilidades."""

content = """
Crie um arquivo e copie esse sitema de anotação:

+============================================+
Recon [+] Corporation
+============================================+

Company:

Domains:

Emails:

Employees:

leaks:

+==============================================+
Recon [+] INFRASTRUCTURE OF NETWORK +
================================================+
DNS-Servers:

-----------------------------
Sub-Domains:

-----------------------------
NetBlocks:

-----------------------------
MX-mail-Servers:

-----------------------------
WEB-SERVERS:

--------------------------
FILE-Servers:

-----------------------------
DB-Servers:

-----------------------------
Cisco-Routers-switch:

+===================================================+
[+] Enumeration
+===================================================+
HOST - Port - banner - OS

+=========================================+
[+] Vulnerability-Analysis
+========================================+
HOST | OS | Service | CVE | Exploit"""

install_debian = """
apt update -y
apt upgrade -y
apt install gccgo-go -y
apt install golang-go -y
sudo apt install pipx
pipx ensurepath
pip install hackerhelp
go install -v github.com/tomnomnom/anew@latest
mv /root/go/bin/anew /usr/bin
go install github.com/tomnomnom/gf@latest && mv /root/go/bin/gf /usr/bin/
mkdir /root/.gf
cd /root/.gf
git clone https://github.com/1ndianl33t/Gf-Patterns
mv /root/.gf/Gf-Patterns/* /root/.gf
rm -rf Gf-Patterns
cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf
go install github.com/tomnomnom/unfurl@latest
mv /root/go/bin/unfurl /usr/bin
git clone https://github.com/devanshbatham/paramspider
cd paramspider
pip install .
cd ..
rm -rf paramspider
pip3 install arjun
GO111MODULE=on go install -v github.com/lc/subjs@latest
mv /root/go/bin/subjs /usr/bin
go install github.com/bp0lr/gauplus@latest
mv /root/go/bin/gauplus /usr/bin
pip install waymore
go install github.com/tomnomnom/waybackurls@latest
mv /root/go/bin/waybackurls /usr/bin
wget https://raw.githubusercontent.com/tomnomnom/hacks/master/anti-burl/main.go
go build main.go
rm main.go
mv main anti-burl
mv anti-burl /usr/bin
git clone https://github.com/j3ssie/metabigor.git
cd metabigor
go install
mv /root/go/bin/metabigor /usr/bin
cd ..
rm -rf metabigor
wget https://github.com/assetnote/kiterunner/releases/download/v1.0.2/kiterunner_1.0.2_linux_amd64.tar.gz
tar -xvf kiterunner_1.0.2_linux_amd64.tar.gz
mv kr /usr/bin
rm kiterunner_1.0.2_linux_amd64.tar.gz
wget https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-small.json.tar.gz
tar -xvf routes-small.json.tar.gz
rm routes-small.json.tar.gz
wget https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz
tar -xvf routes-large.kite.tar.gz
rm routes-large.kite.tar.gz
mv routes-large.kite /usr/bin
mv routes-small.json /usr/bin
git clone https://github.com/gwen001/github-search
cd github-search
pip3 install -r requirements.txt
cd ..
mv github-search /usr/bin
git clone https://github.com/obheda12/GitDorker
cd GitDorker
pip3 install -r requirements.txt
cd ..
mv GitDorker /usr/bin
apt install ffuf
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
mv /root/go/bin/httpx /usr/bin
go install github.com/tomnomnom/httprobe@latest
mv /root/go/bin/httprobe /usr/bin
wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
unzip aquatone_linux_amd64_1.7.0.zip
mv aquatone /usr/bin
rm aquatone_linux_amd64_1.7.0.zip
rm LICENSE.txt
rm README.md
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
mv /root/go/bin/nuclei /usr/bin
nuclei update-templates
go install github.com/hahwul/dalfox/v2@latest
mv /root/go/bin/dalfox /usr/bin
go install github.com/projectdiscovery/katana/cmd/katana@latest
mv /root/go/bin/katana /usr/bin
git clone https://github.com/0x240x23elu/JSScanner.git
cd JSScanner
pip3 install -r  requirements.txt
cd ..
mv JSScanner /usr/bin
apt install leafpad
apt install jsql -y
apt install feroxbuster -y
apt install searchsploit"""

install_arch = """
sudo pacman -Syu
curl -O https://blackarch.org/strap.sh
echo "8c48df016a6037a15e6b48066e0f1dd80922dfc3 strap.sh" | sha1sum -c
chmod +x strap.sh
sudo ./strap.sh
rm -f strap.sh
sudo pacman -S --noconfirm blackarch
sudo pacman -S --noconfirm gcc
sudo pacman -S --noconfirm go
sudo pacman -S --noconfirm pipx
sudo pacman -S --noconfirm seclists
sudo pipx ensurepath
sudo pipx install hackerhelp
sudo set -U fish_user_paths $HOME/.local/bin $fish_user_paths
sudo go install -v github.com/tomnomnom/anew@latest
sudo mv /root/go/bin/anew /usr/bin
sudo go install github.com/tomnomnom/gf@latest && mv /root/go/bin/gf /usr/bin/
sudo mkdir /root/.gf
sudo cd /root/.gf
sudo git clone https://github.com/1ndianl33t/Gf-Patterns
sudo mv /root/.gf/Gf-Patterns/* /root/.gf
sudo rm -rf Gf-Patterns
sudo cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf
sudo go install github.com/tomnomnom/unfurl@latest
sudo mv /root/go/bin/unfurl /usr/bin
sudo git clone https://github.com/devanshbatham/paramspider
sudo cd paramspider
sudo cd ..
sudo rm -rf paramspider
sudo pip3 install arjun
sudo GO111MODULE=on go install -v github.com/lc/subjs@latest
sudo mv /root/go/bin/subjs /usr/bin
sudo go install github.com/bp0lr/gauplus@latest
sudo mv /root/go/bin/gauplus /usr/bin
sudo pipx install waymore
sudo set -U fish_user_paths $HOME/.local/bin $fish_user_paths
sudo go install github.com/tomnomnom/waybackurls@latest
sudo mv /root/go/bin/waybackurls /usr/bin
sudo wget https://raw.githubusercontent.com/tomnomnom/hacks/master/anti-burl/main.go
sudo go build main.go
sudo rm main.go
sudo mv main anti-burl
sudo mv anti-burl /usr/bin
sudo git clone https://github.com/j3ssie/metabigor.git
sudo cd metabigor
sudo go install
sudo mv /root/go/bin/metabigor /usr/bin
sudo cd ..
sudo rm -rf metabigor
sudo wget https://github.com/assetnote/kiterunner/releases/download/v1.0.2/kiterunner_1.0.2_linux_amd64.tar.gz
sudo tar -xvf kiterunner_1.0.2_linux_amd64.tar.gz
sudo mv kr /usr/bin
sudo rm kiterunner_1.0.2_linux_amd64.tar.gz
sudo wget https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-small.json.tar.gz
sudo tar -xvf routes-small.json.tar.gz
sudo rm routes-small.json.tar.gz
sudo wget https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz
sudo tar -xvf routes-large.kite.tar.gz
sudo rm routes-large.kite.tar.gz
sudo mv routes-large.kite /usr/bin
sudo mv routes-small.json /usr/bin
sudo git clone https://github.com/gwen001/github-search
sudo cd github-search
sudo pip3 install -r requirements.txt
sudo cd ..
sudo mv github-search /usr/bin
sudo git clone https://github.com/obheda12/GitDorker
sudo cd GitDorker
sudo pip3 install -r requirements.txt
sudo cd ..
sudo mv GitDorker /usr/bin
sudo pacman -S ffuf
sudo go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
sudo mv /root/go/bin/httpx /usr/bin
sudo go install github.com/tomnomnom/httprobe@latest
sudo mv /root/go/bin/httprobe /usr/bin
sudo wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
sudo unzip aquatone_linux_amd64_1.7.0.zip
sudo mv aquatone /usr/bin
sudo rm aquatone_linux_amd64_1.7.0.zip
sudo rm LICENSE.txt
sudo rm README.md
sudo go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
sudo mv /root/go/bin/nuclei /usr/bin
sudo nuclei update-templates
sudo go install github.com/hahwul/dalfox/v2@latest
sudo mv /root/go/bin/dalfox /usr/bin
sudo go install github.com/projectdiscovery/katana/cmd/katana@latest
sudo mv /root/go/bin/katana /usr/bin
sudo git clone https://github.com/0x240x23elu/JSScanner.git
sudo cd JSScanner
sudo pipx install -r requirements.txt
sudo cd ..
sudo mv JSScanner /usr/bin
sudo pacman -S --noconfirm jsql-injection
sudo pacman -S --noconfirm feroxbuster
sudo pacman -S --noconfirm burpsuite
sudo pacman -Syu
sudo pacman -Ss openjdk
sudo pacman -Syu jdk-openjdk
sudo archlinux-java set java-23-openjdk
sudo set -U fish_user_paths $HOME/.local/bin $fish_user_paths
git clone https://github.com/offensive-security/exploitdb.git /opt/exploitdb
sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit
searchsploit -u"""

install_manual = """
A opção que você selecionou é um manual com todos os comandos que você vai precisar
executar caso sua máquina não tenha alguma delas instalado!

[0] Golang:
 apt install gccgo-go
 apt install golang-go

[1] Anew:

go install -v github.com/tomnomnom/anew@latest
mv /root/go/bin/anew /usr/bin

[2] GF:

go install github.com/tomnomnom/gf@latest && mv /root/go/bin/gf /usr/bin/
mkdir /root/.gf
cd /root/.gf
git clone https://github.com/1ndianl33t/Gf-Patterns
mv /root/.gf/Gf-Patterns/* /root/.gf
rm -rf Gf-Patterns
echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf

[3] Unfurl:

go install github.com/tomnomnom/unfurl@latest
mv /root/go/bin/unfurl /usr/bin

[4] ParamSpider:

git clone https://github.com/devanshbatham/paramspider
cd paramspider
pip install .
cd ..
rm -rf paramspider

[5] Arjun:

pip3 install arjun

[6] Subjs:

GO111MODULE=on go install -v github.com/lc/subjs@latest
mv /root/go/bin/subjs /usr/bin

[7] Gauplus:

go install github.com/bp0lr/gauplus@latest
mv /root/go/bin/gauplus /usr/bin

[8] Waybackurls:

go install github.com/tomnomnom/waybackurls@latest
mv /root/go/bin/waybackurls /usr/bin

[9] Anti-Burl:

wget https://raw.githubusercontent.com/tomnomnom/hacks/master/anti-burl/main.go
go build main.go
rm main.go
mv main anti-burl
mv anti-burl /usr/bin

[10] Metabigor:

git clone https://github.com/j3ssie/metabigor.git
cd metabigor
go install
mv /root/go/bin/metabigor /usr/bin
cd ..
rm -rf metabigor

[11] Kiterunner:

wget https://github.com/assetnote/kiterunner/releases/download/v1.0.2/kiterunner_1.0.2_linux_amd64.tar.gz
tar -xvf kiterunner_1.0.2_linux_amd64.tar.gz
mv kr /usr/bin
rm kiterunner_1.0.2_linux_amd64.tar.gz
wget https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-small.json.tar.gz
tar -xvf routes-small.json.tar.gz
rm routes-small.json.tar.gz
wget https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz
tar -xvf routes-large.kite.tar.gz
rm routes-large.kite.tar.gz
mv routes-large.kite /usr/bin
mv routes-small.json /usr/bin

[12] Api git:

git clone https://github.com/gwen001/github-search
cd github-search
pip3 install -r requirements.txt
cd ..
mv github-search /usr/bin

[13] Git-Dorker:

git clone https://github.com/obheda12/GitDorker
cd GitDorker
pip3 install -r requirements.txt
cd ..
mv GitDorker /usr/bin

[14] Ffuf:

apt install ffuf

[15] Htppx:

go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
mv /root/go/bin/httpx /usr/bin

[16] Httprobe:

go install github.com/tomnomnom/httprobe@latest
mv /root/go/bin/httprobe /usr/bin

[17] Aquatone:

wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
unzip aquatone_linux_amd64_1.7.0.zip
mv aquatone /usr/bin
rm aquatone_linux_amd64_1.7.0.zip
rm LICENSE.txt
rm README.md

[18] Nuclei:

go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
mv /root/go/bin/nuclei /usr/bin
nuclei update-templates

[19] Dalfox:

go install github.com/hahwul/dalfox/v2@latest
mv /root/go/bin/dalfox /usr/bin

[20] Katana:

go install github.com/projectdiscovery/katana/cmd/katana@latest
mv /root/go/bin/katana /usr/bin

[22] Waymore

pip install waymore

[23] Searchsploit

apt install searchsploit"""

def options_install_tools():
    print(install_manual)
    install = int(input("Deseja instalar todas as ferramentas? [0/1]"))
    if install == 0:
            system = int(input("Qual tipo de distro você está usando? | Debian = 0 | Arch = 1 [0/1]"))
            if system == 0:
                os.system(f"{install_debian}")
            else:
                os.system(f"{install_arch}")
    else:
        pass

def other(domain):
    print("""

  ___  _   _
 / _ \\| |_| |_  ___ _ _ ___
| (_) |  _| ' \\/ -_) '_(_-<
 \\___/ \\__|_||_\\___|_| /__/

Sabe aquelas linhas gigantes que esses streamers e youtubers usam
e você não entende nada? Bom oh elas aqui! São linhas para bounty! Aproveite.

[0] Open redirect: echo \"domain\" | waybackurls | httpx -silent -timeout 2 -threads 100 | gf redirect | anew
[1] Asn - Amass: amass intel -org <domain> -max-dns-queries 2500 | awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' amass intel -asn @ -max-dns-queries 2500''
[2] Asn - Metabigor: echo \"ip\" | metabigor net --asn -o metabigor_result_01 | anew
[3] Shodan + xargs: shodan domain <domain>| awk '{print $3}'|  httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @
[4] Shodan + nuclei: shodan domain <domain> | awk '{print $3}' | httpx -silent | nuclei -t /root/nuclei-templates
[5] Chaos Search Js: chaos -d <domain> | httpx -silent | xargs -I@ -P20 sh -c 'gospider -a -s "@" -d 2' | grep -Eo "(http|https)://[^/"].*.js+" | sed "s#]
[6] Subdomain with gospider: gospider -d 0 -s "<domain>" -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt | grep -Eo '(http|https)://[^/"]+' | anew
[7] Gospider + chaos: chaos -d <domain> -bbq -filter-wildcard -http-url | xargs -I@ -P5 sh -c 'gospider -a -s "@" -d 3'
[8] Checking invalid certificate: xargs -a {domain} -P1000 -I@ sh -c 'bash cert.sh @ 2> /dev/null' | grep "EXPIRED" | awk '/{domain}/{print $5}' | httpx
[9] Using shodan & Nuclei : shodan domain <DOMAIN TO BOUNTY> | awk '{print $3}' | httpx -silent | nuclei -t /root/nuclei-templates
[10] Open Redirect test using gf: echo "domain" | waybackurls | httpx -silent -timeout 2 -threads 100 | gf redirect | anew
[11] Jaeles para escanear recompensas de bug: wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv ; cat domains.txt | anew | httpx -silent -threads 500 | xargs -I@ jaeles scan -s /jaeles-signatures/ -u @
[12] Using to findomain to SQLINJECTION: findomain -t domain -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli -batch --random-agent --level 1
[13] Baixe para listar os alvos de recompensa. Injetando e usando o sed .git/HEAD.
[14] Monte seu comando.(se puder)\n""")
    command = int(input("Comando:"))

    match command:
        case 0:
            os.system(f"echo \"{domain}\" | waybackurls | httpx -silent -timeout 2 -threads 100 | gf redirect | anew")
        case 1:
            org = str(input("Org: "))
            awk = "awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' amass intel -asn @ -max-dns-queries 2500''"
            os.system(f"amass intel -org {org} -max-dns-queries 2500 | {awk}")
        case 2:
            ip = str(input("Digite o ip: "))
            os.system(f"echo \"{ip}\" | metabigor net --asn -o metabigor_result_01 | anew")
        case 3:
            awk = "awk '{print $3}'|  httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @"
            os.system(f"shodan domain {domain} | {awk}")
        case 4:
            awk = "awk '{print $3}' | httpx -silent | nuclei -t /root/nuclei-templates"
            os.system(f" shodan domain {domain} | {awk}")
        case 5:
            os.system(f""" chaos -d {domain} | httpx -silent | xargs -I@ -P20 sh -c 'gospider -a -s "@" -d 2' | grep -Eo "(http|https)://[^/"].*.js+" | sed "s#]""")
        case 6:
            os.system(f"""gospider -d 0 -s "{domain}" -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt | grep -Eo '(http|https)://[^/"]+' | anew""")
        case 7:
            os.system(f"""chaos -d {domain} -bbq -filter-wildcard -http-url | xargs -I@ -P5 sh -c 'gospider -a -s "@" -d 3'""")
        case 8:
            awk = f" awk \'/{domain}\'"
            awk2 = "{print $5}' | httpx"
            os.system(f"xargs -a {domain} -P1000 -I@ sh -c 'bash cert.sh @ 2> /dev/null' | grep \"EXPIRED\" | {awk2}{awk}")
        case 9:
            awk = " awk \'{print $3}\'"
            os.system(f"shodan domain {domain} | {awk} | httpx -silent | nuclei -t /root/nuclei-templates")
        case 10:
            os.system(f"echo \"{domain}\" | waybackurls | httpx -silent -timeout 2 -threads 100 | gf redirect | anew")
        case 11:
            os.system("wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv ; cat domains.txt | anew | httpx -silent -threads 500 | xargs -I@ jaeles scan -s /jaeles-signatures/ -u @")
        case 12:
            os.system(f"findomain -t {domain} -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli -batch --random-agent --level 1")
        case 13:
            os.system("wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv | cat domains.txt | sed 's#$#/.git/HEAD#g' | httpx -silent -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew")
        case _:
            shell = str(input("Monte seu comando: "))
            print(f"Comando executado: {shell}")
            os.system(f"{shell}")

def pytools():
    choice = int(input("HackerHelp / Wapiti3 : [0/1] "))
    match choice:
        case 0:
            os.system("hackerhelp")
        case 1:
            os.system("wapiti3")
