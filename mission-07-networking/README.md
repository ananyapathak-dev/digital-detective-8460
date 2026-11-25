# Mission 7 — How Computers Communicate

## 1. Task / objective
Explain foundational networking concepts (`LAN`, `MAN`, `WAN`, `DNS`, `Router`, `Protocol`, `Packet switching`, `Client-server`), describe connectivity testing and DNS lookups, and trace in 5–7 steps what happens when a user opens a website.

## 2. Work completed
- Completed the network-concepts table with plain-language explanations and real-world examples.
- Answered the connectivity-test and DNS-lookup questions and recorded the offline sandbox limitation for live `ping` / `nslookup` execution.
- Wrote a 6-step explanation of how a website loads from browser request to page display.

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
|---|---|---|
| `LAN` | A Local Area Network connects devices within a small, single location such as a home, classroom, or office. | Laptops, phones, and a printer connected to the same home Wi-Fi or office switch. |
| `MAN` | A Metropolitan Area Network spans a larger area such as an entire city or a big university campus, often linking multiple LANs. | Interconnected buildings across a multi-block university campus network. |
| `WAN` | A Wide Area Network spans large geographical regions across cities, countries, or continents. | The global internet or a company network connecting offices in different countries. |
| `DNS` | The Domain Name System acts like the internet's phonebook, translating human-readable domain names into numeric IP addresses. | Translating `example.com` into its destination IP address so a browser knows where to connect. |
| `Router` | A networking device that connects separate networks together and forwards data packets along paths toward their destination. | A home Wi-Fi router forwarding web requests from your LAN out to your ISP and the internet. |
| `Protocol` | An agreed set of formatting and communication rules that devices follow so they can exchange data reliably. | `HTTPS` for encrypted web pages, `DNS` for name lookups, and `TCP/IP` for packet delivery. |
| `Packet switching` | A method where large messages are split into small packets that travel across the network independently and are reassembled at the destination. | Downloading a web page or image broken into small `IP` packets across shared internet links. |
| `Client-server` | A communication model where a client program requests a resource or service and a server program processes the request and sends back a response. | Your web browser (client) requesting a page from a website's web server. |

### Task 7.2 — Observe network information
- **Offline execution note:** Testing `ping -c 2 example.com` inside the offline workspace sandbox returned `ping: cannot resolve example.com: Unknown host`, and `nslookup example.com` could not reach a network DNS server. No live IP address, Wi-Fi name, or fabricated output is included.
- **[User action required — practical verification]:** From your connected macOS Terminal, run:
  1. `ping -c 3 example.com`
  2. `nslookup example.com`
  Record the public `example.com` observations here if desired, making sure to redact any personal/local router IP addresses or Wi-Fi details.

Answers:
- **What a connectivity test helps you check:** A connectivity test (such as `ping`) checks whether your computer can reach another host over a network and receive replies, helping verify basic network reachability, packet loss, and round-trip latency.
- **What information a DNS lookup displays:** A DNS lookup tool (`nslookup` or `dig`) displays the DNS server queried (redacted if private/local) and the DNS records returned for a domain—such as the `A` (IPv4) or `AAAA` (IPv6) address mapped to that domain name.
- **Role of DNS when you enter a website name in a browser:** Because network routers forward packets using numeric IP addresses rather than English domain names, the browser relies on DNS to look up and return the server's IP address before opening a connection to fetch the site.

### Task 7.3 — What happens when you open a website?
1. **User enters URL in the client:** You type a website address (such as `https://example.com`) into your web browser, which acts as the **client**.
2. **DNS lookup resolves the domain:** The client asks a **DNS** resolver to translate the human-readable domain name into the destination server's numeric IP address.
3. **Request travels through the local router:** Using standard **protocols** (`TCP/IP` and `TLS`/`HTTPS`), the client breaks the request into small packets and sends them through your local network and **router** toward the internet.
4. **Packets route across the network:** Intermediate routers across the WAN forward those packets hop by hop until they reach the destination **server** matching that IP address.
5. **Server processes and responds:** The web **server** receives the `HTTP`/`HTTPS` request, locates or generates the requested web page, and sends the `HTML`, `CSS`, images, and status code back as packets following the same **protocol** rules.
6. **Client renders the page:** Your browser (**client**) reassembles the response packets, verifies the `HTTPS` security session, and displays the finished web page on your screen.

## 3. Commands / tools used
- `ping -c 2 example.com`: Tested basic reachability in the sandboxed environment (returned `Unknown host` offline; documented for user execution on a live network).
- `nslookup example.com`: Intended DNS lookup command to map a domain name to its public IP address (requires live network).
- `git add` and `git commit`: Stages and commits Mission 7 documentation locally.

## 4. My understanding
Networks connect devices at different scales (LAN, MAN, WAN) using shared protocols so computers of all kinds can communicate. Packet switching splits messages efficiently across routers, DNS turns memorable names into IP addresses, and the client-server model structures how browsers request and display websites.

## 5. Difficulties faced
External network access and DNS resolution are disabled in the sandboxed execution environment (`ping: cannot resolve example.com: Unknown host`), so live `ping` and `nslookup` outputs for `example.com` could not be captured directly here.

## 6. How I resolved them
Recorded the exact offline command result honestly without inventing network outputs, explained the concepts clearly, and listed the two live Terminal commands (`ping -c 3 example.com` and `nslookup example.com`) as a short user verification task.

## 7. Evidence / files
- [mission-07-networking/README.md](README.md) — Network concepts table, connectivity/DNS notes, and 6-step website loading walkthrough.

## 8. Commit details
- Local commit message: `Explain networking concepts and website communication`
- Push status: Committed locally; **[User action required]** push to GitHub (`git push origin main`) and confirm on GitHub.
