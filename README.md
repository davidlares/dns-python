## DNS Python

This script contains a bunch of examples of how the `dnspython` library works. From things like getting `DNS registries`, to evaluating subdomains' existence, reverse lookups, and even XFR for transfer zones.

The `dnspython` is an open-source library that lets you make checks for registries against DNS servers (high-level) and manipulate zones, messages, names, and registries in a low-level

## A little background

`DNS` (Domain Name Servers) works like a distributed database where it stores domain names and their IP addresses, and of course, the capability of locating other related services.

DNS helps you perform lookups for your internet service,s such as email services, IP addresses, domain information, text information, etc.

Internally, the `DNS protocol` is identifiable through the `UDP 53 port`. Whenever a client sends a DNS packet, it should include the DNS lookup type, such as `A`, `AAAA`, `MX`, `NS`, `TXT`, etc

## Usage

You will need to install `dnspython` library. You can check the `requirements.txt` file for that. I recommend creating a `virtualenv` for that.

## Credits
[David Lares S](https://davidlares.com)

## License
[MIT](https://opensource.org/licenses/MIT)
