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
- **Live Terminal observations (prompt redacted for privacy):**
  Ran `ping -c 4 google.com` and `nslookup google.com`:

  ```text
  [redacted]@[redacted] digital-detective-8460 % ping -c 4 google.com
  PING google.com (142.251.106.102): 56 data bytes
  64 bytes from 142.251.106.102: icmp_seq=0 ttl=108 time=50.232 ms
  64 bytes from 142.251.106.102: icmp_seq=1 ttl=108 time=23.414 ms
  64 bytes from 142.251.106.102: icmp_seq=2 ttl=108 time=24.128 ms
  64 bytes from 142.251.106.102: icmp_seq=3 ttl=108 time=24.827 ms

  --- google.com ping statistics ---
  4 packets transmitted, 4 packets received, 0.0% packet loss
  round-trip min/avg/max/stddev = 23.414/30.650/50.232/11.317 ms

  [redacted]@[redacted] digital-detective-8460 % nslookup google.com
  Server:         8.8.8.8
  Address:        8.8.8.8#53

  Non-authoritative answer:
  Name:   google.com
  Address: 142.251.222.142
  ```

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
- `ping -c 4 google.com`: Verified live network reachability (`4 packets transmitted, 4 packets received, 0.0% packet loss`, average round-trip time `30.650 ms`).
- `nslookup google.com`: Queried DNS server `8.8.8.8` (port `53`) and resolved `google.com` to public IP address `142.251.222.142`.
- `git add` and `git commit`: Stages and commits Mission 7 documentation locally.

## 4. My understanding
Networks connect devices at different scales (LAN, MAN, WAN) using shared protocols so computers of all kinds can communicate. Packet switching splits messages efficiently across routers, DNS turns memorable names into IP addresses, and the client-server model structures how browsers request and display websites.

## 5. Difficulties faced
No major difficulties once tested on a live network connection (an initial test in an offline sandbox returned `Unknown host`, and the live Terminal prompt username/device name was redacted before saving).

## 6. How I resolved them
Ran `ping -c 4 google.com` and `nslookup google.com` in the live macOS Terminal and replaced the username and device name in the prompt with `[redacted]@[redacted]`.

## 7. Evidence / files
- [mission-07-networking/README.md](README.md) — Network concepts table, live privacy-safe `ping`/`nslookup` observations, and 6-step website loading walkthrough.

## 8. Commit details
- Local commit message: `Explain networking concepts and website communication`
- Follow-up commit message: `Add live ping and nslookup observations to Mission 7`
- Push status: Committed locally; **[User action required]** push to GitHub (`git push origin main`) and confirm on GitHub.
