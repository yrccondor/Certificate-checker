# Certificate checker
A simple way to check certificate's infomation.

## Download
```
git clone git@github.com:yrccondor/Certificate-checker.git
cd Certificate-checker
```
## Dependence
- curl
- Python3

## Usage
Edit <code>config.json</code> to configure which website you want to scan.

Like:
```json
{
    "config_list": ["example.com","test.example.com"],
    "timeout": 10
}
```

Then use it with <code>curl</code>:
```
python3 check.py
```
If everything works, you will see:
```
------------
Certificate infomation about flyhigher.top:

Check time: 2018-01-15 16:35:44
Start: 2018-01-02 17:30:51
End: 2018-04-02 17:30:51
Common Name: flyhigher.top
Issuer Info: CN=Let's Encrypt Authority X3,O=Let's Encrypt,C=US
------------
```

## Config

config.json:
- website_list: The list of websites. Only need host:port (Without protocol). Default port: 443.
- [timeout]: The duration while connecting. Default: 10(s).
- [sleep]: How long should we wait between scannings. Default: 2(s).
- [output]: How we print results. You can choose "print" or "print\_details". Default: "print". If you choose "print\_details", you will see:
```
[13:29:43] Read config.json successfully.
[13:29:43] Read website_list successfully. 3 web site(s) will be scaned.
[13:29:43] Read timeout successfully. Value: 10s
[13:29:43] Read output successfully. Value: 1s
[13:29:43] Scanning example.com(1 in 3).
[13:29:45] Read reponse successfully.
[13:29:45] Read certificate infomation successfully.
[13:29:45] Environment cleaned.
-----------------------------
Certificate infomation about example.com:

Check time: 2018-01-16 13:29:45
Start: 2015-11-03 00:00:00
End: 2018-11-28 12:00:00
Common Name: www.example.org
Issuer Info: CN=DigiCert SHA2 High Assurance Server CA,OU=www.digicert.com,O=DigiCert Inc,C=US
-----------------------------
```