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
-----------------------------
Certificate infomation about example.com:

Check time: 2018-01-16 14:52:31
Start: 2015-11-03 00:00:00
End: 2018-11-28 12:00:00
Common Name: www.example.org
Issuer Info: CN=DigiCert SHA2 High Assurance Server CA,OU=www.digicert.com,O=DigiCert Inc,C=US
-----------------------------
```

## Config

<code>config.json</code>:
- <code>website_list</code>: The list of websites. Only need <code>host[:port]</code> (Without protocol). Default port: 443.
- <code>[timeout]</code>: The duration while connecting. Default: 10(s).
- <code>[sleep]</code>: How long should we wait between scannings. Default: 2(s).
- <code>[output]</code>: How we print results. You can choose <code>"print"</code> or <code>"print\_details"</code>. Default: <code>"print"</code>. If you choose <code>"print\_details"</code>, you will see:
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

Here is an example of <code>config.json</code>:
````json
{
    "website_list": ["example.com","test.example.com"],
    "timeout": 15,
    "sleep": 1,
    "output": "print_details"
}
````