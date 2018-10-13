# CORS

If you see the exploitable ones below:

Poorly implemented, Best case for Attack:
```
Access-Control-Allow-Origin: https://attacker.com
Access-Control-Allow-Credentials: true
```

Poorly implemented, Exploitable:
```
Access-Control-Allow-Origin: null
Access-Control-Allow-Credentials: true
```
    
Bad implementation but not exploitable:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```
or just
```
Access-Control-Allow-Origin: *
```

You can test using:
```
curl https://test.victim.com -H "Origin: https://test.site" -I
```
And checking teh response to see if the gorgin is set to `test.site`

Sometimes you might have to use it on a specific endpoint, and if it works, then it is vulnerable.

You can also test using the CORS.html doc. You just have to replace `targer.com` with the actual targer.
