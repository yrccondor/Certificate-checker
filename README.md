# Certificate checker
A simple way to check certificate's infomation.

## Download
```
git clone git@github.com:yrccondor/Certificate-checker.git
cd Certificate-checker
```

## Usage
Edit <code>websitelist.json</code> to configure which website you want to scan.

Like:
```json
{
    "wbesite_list": ["flyhigher.top","example.flyhigher.top"]
}
```

Then use it with <code>curl</code>
```
python3 check.py
```
If everything works, you will see
```
Certificate infomation about flyhigher.top:
Check time: 2018-01-15 15:01:03
Start: 2018-01-02 17:30:51
End: 2018-04-02 17:30:51
Issuer Info: CN=Let's Encrypt Authority X3,O=Let's Encrypt,C=US
```