# DNSBrute — Subdomain Enumerator

```bash
🔍 Um enumerador de subdomínios via DNS Bruteforce utilizando multithreading, desenvolvido em Python.

Este projeto tem como objetivo realizar a descoberta de subdomínios de um alvo de forma rápida e eficiente, útil para atividades de reconhecimento em testes de segurança, pentests e CTFs.

---

✨ Funcionalidades
- Busca de subdomínios por força bruta usando wordlists.
- Suporte a multithreading para execução mais rápida.
- Possibilidade de salvar os resultados em um arquivo.
- Tratamento robusto de erros (DNS Timeout, NXDOMAIN, etc).
- Relatório de tempo total de execução e quantidade de subdomínios encontrados.
- Interface de linha de comando intuitiva com argparse.
- Código limpo, modular e escalável.

---

🚀 Uso
# Execução básica
python3 dnsbrute.py <dominio> <wordlist.txt>

# Execução com opções adicionais
python3 dnsbrute.py <dominio> <wordlist.txt> -t 20 -o resultados.txt

---

🛠️ Parâmetros
Parâmetro          | Descrição
------------------ | --------------------------------------------------------
<dominio>          | Domínio alvo para a enumeração.
<wordlist.txt>     | Caminho para a wordlist contendo subdomínios.
-t, --threads      | Número de threads (padrão: 10).
-o, --output       | Arquivo para salvar os resultados encontrados.

---

📄 Exemplo de Saída
[+] admin.example.com -> 192.168.0.1
[+] mail.example.com -> 192.168.0.2
[*] Subdomínios encontrados: 2
[*] Tempo total: 5.32 segundos

---

⚡ Tecnologias Utilizadas
- Python 3
- dnspython
- threading
- queue

---

📢 Aviso Legal
Este projeto foi criado para fins educacionais e de pesquisa em segurança da informação.
O uso deste software em domínios sem autorização é ilegal e pode configurar crime.
O autor não se responsabiliza por qualquer uso indevido.

---

🤝 Contribuição
Sinta-se à vontade para fazer um fork, abrir issues ou enviar pull requests!

---

📬 Contato
- LinkedIn: https://www.linkedin.com/in/leandro-naves-guerra-7928a721b/
