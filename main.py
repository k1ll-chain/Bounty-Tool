import Config.Banners.main_banner as Banner
import Config.Enumeration.main_enum as Enumeration
import Config.Information.main_info as Information
import Config.Scanners.main_scan as Scanners
import Config.Structure.main_struct as Structure
import Config.Subdomain.main_sub as Subdomain
import Config.Options.main_opt as Options

import os

def main():
    while True:
        try:
            print((Banner.banner_main))

            domain = str(input(("Digite a url: ")))
            tool = int(input(("Digite o número da ferramenta: ")))

            match tool:
                # -- Enumeration --
                case 1:
                    Enumeration.gf(domain)
                case 2:
                    Enumeration.arjun(domain)
                case 3:
                    Enumeration.unfurl(domain)
                case 4:
                    Enumeration.paramspider(domain)
                case 5:
                    Enumeration.subjs(domain)
                case 6:
                    Enumeration.anti_burl()
                case 7:
                    Enumeration.amass(domain)
                case 8:
                    Enumeration.metabigor(domain)

                # -- Information --

                case 9:
                    Information.host(domain)
                case 10:
                    Information.whois(domain)
                case 11:
                    Information.censys(domain)
                case 12:
                    Information.dnsenum(domain)
                case 13:
                    Information.dnsrecon(domain)
                case 14:
                    Information.nmap(domain)
                case 15:
                    Information.waf(domain)

                # -- Scanners --

                case 16:
                    Scanners.jsql()
                case 17:
                    Scanners.dotdotpwn()
                case 18:
                    Scanners.search()
                case 19:
                    Scanners.wp_scan(domain)
                case 20:
                    Scanners.burp_suit()

                # -- Structure --

                case 21:
                    Structure.xargs()
                case 22:
                    Structure.nuclei()
                case 23:
                    Structure.dalfox()
                case 24:
                    Structure.katana(domain)

                # -- Subdomain --

                case 25:
                    Subdomain.kitterunner(domain)
                case 26:
                    Subdomain.git_api(domain)
                case 27:
                    Subdomain.git_dorker(domain)
                case 28:
                    Subdomain.wfuzz(domain)
                case 29:
                    Subdomain.ffuf(domain)
                case 30:
                    Subdomain.feroxbuster(domain)
                case 31:
                    Subdomain.gauplus(domain)
                case 32:
                    Subdomain.waymore(domain)
                case 33:
                    Subdomain.httpx(domain)
                case 34:
                    Subdomain.httprobe()
                case 35:
                    Subdomain.aquatone()

                # -- Options --

                case 36:
                    print((Options.man))
                case 37:
                    print((Options.infos))
                case 38:
                    Options.other(domain)
                case 39:
                    print((Options.report))
                case 40:
                    Options.pytools()
                case 41:
                    print((Options.content))
                case 42:
                    Options.options_install_tools()

        except Exception as e:
            print((f"\nAlgo deu errado: {e}"))
            sequence = str(input(("Deseja continuar? [y/n] ")))

            if sequence == "y":
                os.system("clear")
                continue
            else:
                break

if __name__ == "__main__":
    main()
