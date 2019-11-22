# importing DNSPython library
import dns.resolver
# domain lookup module
import dns.name
# IP lookup module
import dns.reversename
# Transfer Zones module
import dns.query
import dns.zone

# IPv4 registry for google.com
a = dns.resolver.query('google.com','A')
# Email Server registry for google.com
mx = dns.resolver.query('google.com','MX')
# nameserver registry for google.com
ns = dns.resolver.query('google.com','NS')
# IPv6 registry for google.com
aaaa = dns.resolver.query('google.com','AAAA')
# SOA -> Search of Authority registry for google.com
soa = dns.resolver.query('google.com','SOA')
# TXT registry for google.com
txt = dns.resolver.query('google.com','TXT')

# looping results (this applies for each record)
for m in mx:
    print("MX Server: " + str(m))

n = dns.name.from_text('www.google.com')
n1 = dns.name.from_text('google.com')
# check if it is subdomain or not
print("Sub-domain evaluation: " + str(n.is_subdomain(n1)))
print("Reverse Sub-domain evaluation: " + str(n1.is_subdomain(n)))

# reverse lookup from IP addresses
ip = dns.reversename.from_address('127.0.0.1')
print("Reverse Lookup: " + str(ip))
# an IP address from the domain
print("Reverse Lookup from IP: " + str(dns.reversename.to_address(ip)))

# the following is for request XFR for transfer zones
for x in a:
    print("A Record: " + str(x))

try:
    z = dns.zone.from_xfr(dns.query.xfr(str(a[0]),'thehackerway.com'))
    print("Result of transfer: " + str(z))
except Exception as e:
    print('Error: ' + str(e))

# if this crashes, the TCP 53 port is closed for TF.
