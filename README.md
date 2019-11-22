# DnsPython

This script contains a bunch of examples of how the `dnspython` library works. From things like getting `DNS registries`, to evaluate subdomains existence, reverse lookups and even XFR for transfer zones.

The `dnspython` is a open-source library that lets you make check for registries against DNS servers (high-level) and manipulate zones, message, name and registries in a low-level

## A little background

`DNS` (Domain Name Servers) works like a distributed database where it stores domain names and theirs IP addresses and of course the capability of locate other related services.

DNS helps you perform lookup for your internet services such as email services, IP addresses, domain informations, text information, etc.

Internally the `DNS protocol` is identifiable through the `UDP 53 port`. Whenever a client sends a DNS packet it should include the DNS lookup type such as `A`, `AAAA`, `MX`, `NS`, `TXT`, etc

## Usage

You will need to install `dnspython` library. You can check the `requirements.txt` file for that. I recommend to create a `virtualenv` for that.

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
