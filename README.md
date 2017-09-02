# bind9-python


#JSON format
```
{
  "Domain": "exsample.org",
  "TTL":"1D",
  "records": [
    {
      "SOA": [
        {
          "primaryDNS":"ns.nameserver.info.exsample.org.",
          "zone-contact":"mail.exsample.org.",
          "serial":"2001235469",
          "refresh":"4H",
          "retry":"1H",
          "expire":"24H",
          "NX":"2H"
        }

      ],
      "A": [
        {
          "@":"127.0.0.1",
          "www":"127.0.0.1",
          "shop":"127.0.0.2"
        }
      ],
      "AAAA" : [
        {
          "@":"::1",
          "www":"::1",
          "shop":"::1"
        }
      ],
      "NS": [
        {
          "@":"ns.nameserver.info.exsample.org.",
          "@":"ns2.nameserver.info.exsample.org.",
          "@":"ns3.nameserver.info.exsample.org.",
          "@":"ns4.nameserver.info.exsample.org."
        }
      ],
      "MX": [
        {
          "mail":"10 exsample.org."
        }
      ],
      "CNAME": [
        {
          "mail":"exsample.org."
        }
      ],
      "DNAME": [
        {
          "dev":"host.exsample.org"
        }
      ]
    }
  ]
}

```
