import argparse
import threading
import queue
import time

import dns.resolver

def banner():
    print(r"""
 ____  _   _ ____                  _       
|  _ \| \ | | __ )  ___  __ _  __ _| |_ ___ 
| | | |  \| |  _ \ / _ \/ _` |/ _` | __/ __/
| |_| | |\  | |_) |  __/ (_| | (_| | ||  __/
|____/|_| \_|____/ \___|\__, |\__,_|\__\___|
                        |___/              
    """)
    print("Author: Leandro Naves | Tool: DNSBruteForce\n")


def parse_args():
    parser = argparse.ArgumentParser(description="Enumerador de subdomínios usando DNS bruteforce (multithreaded)")
    parser.add_argument("target", help="Domínio alvo para enumerar")
    parser.add_argument("wordlist", help="Arquivo com lista de subdomínios")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Número de threads (padrão: 10)")
    parser.add_argument("-o", "--output", help="Arquivo para salvar resultados")
    return parser.parse_args()

def load_wordlist(path):
    try:
        with open(path, "r") as file:
            return file.read().splitlines()
    except Exception as error:
        print("[!] Erro ao abrir wordlist: {}".format(error))
        exit(1)

def save_results(results, path):
    try:
        with open(path, "w") as file:
            for line in results:
                file.write("{}\n".format(line))
    except Exception as error:
        print("[!] Erro ao salvar resultados: {}".format(error))

def worker(q, target, resolver, results, lock):
    while not q.empty():
        subdomain = q.get()
        full_domain = "{}.{}".format(subdomain, target)
        try:
            answers = resolver.resolve(full_domain, "A")
            for answer in answers:
                with lock:
                    print("{} -> {}".format(full_domain, answer))
                    results.append("{} -> {}".format(full_domain, answer))
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.resolver.Timeout):
            pass
        except Exception as error:
            with lock:
                print("[!] Erro em {}: {}".format(full_domain, error))
        finally:
            q.task_done()

def main():
    banner()
    args = parse_args()
    resolver = dns.resolver.Resolver()

    subdomains = load_wordlist(args.wordlist)
    q = queue.Queue()
    for sub in subdomains:
        q.put(sub)

    results = []
    lock = threading.Lock()

    print("[*] Iniciando bruteforce DNS em: {}".format(args.target))
    print("[*] Threads: {}".format(args.threads))
    start = time.time()

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, args=(q, args.target, resolver, results, lock))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print("\n[*] Subdomínios encontrados: {}".format(len(results)))
    print("[*] Tempo total: {} segundos".format({end - start:.2}))

    if args.output:
        save_results(results, args.output)
        print("[*] Resultados salvos em: {}".format(args.output))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrompido pelo usuário.")
        exit(0)