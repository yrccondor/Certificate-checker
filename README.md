# Certificate checker
A simple way to check certificate's infomation.

## Download
```
git clone git@github.com:yrccondor/Certificate-checker.git
cd Certificate-checker
```
## Dependence
- curl
- python3

## Usage
Edit <code>config.json</code> to configure which website you want to scan.

Like:
```json
{
    "config_list": ["example.com","test.example.com"],
    "timeout": 10
}
```

Then use it with <code>curl</code>
```
python3 check.py
```
If everything works, you will see:
```
Certificate infomation about flyhigher.top:

Check time: 2018-01-15 16:35:44
Start: 2018-01-02 17:30:51
End: 2018-04-02 17:30:51
Common Name: flyhigher.top
Issuer Info: CN=Let's Encrypt Authority X3,O=Let's Encrypt,C=US
```

## Config

config.json:
- website_list: The list of website. Only need host name (Without port/protocol).
- timeout: The duration while connecting.