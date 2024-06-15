# Natas
Web service security.

## Natas3
There are several ways of telling to web indexing bots / crawlers to not index some resources. 
- `noindex` tag. See https://developers.google.com/search/docs/crawling-indexing/block-indexing :
```html
<head>
<meta name="robots" content="noindex">
</head>
```
- a `robots.txt` file at the server root path. See https://developers.google.com/search/docs/crawling-indexing/robots/intro

The urls can still be accessed by users and indexed if other pages direct to them.

## Natas4
`curl -u natas4 -v -H "Referer: http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/`

### Header "Referer" vs Header "Origin"
#### Referer
Where we were before accessing the current page. From where (which other page) we accessed. The address of the page that contained the link to the current page. Might include the domain + entire path.
> _The Referer header allows a server to identify referring pages that people are visiting from or where requested resources are being used. This data can be used for analytics, logging, optimized caching, and more._

Is a security issue for the server that emitted the request:
- https://developer.mozilla.org/en-US/docs/Web/Security/Referer_header:_privacy_and_security_concerns
- [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) might help to mitigate.

#### Origin
Includes only the domain. Sent with CORS and same-origin other than GET and HEAD requests.

## Natas5
The response had a "Set-Cookie" header. Cookies can be modified in dev tools.

## Natas8
- `xxd` to create an hexa dump. ``xxd -r` to revert.
- `rev` to revert lines in a file and revert those lines.

echo "3d 3d 51 63 43 74 6d 4d 6d 6c 31 56 69 56 33 62" | xxd -r

echo "==QcCtmMml1ViV3b" | rev | base64 -d


## To catch up
natas2 TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
natas6 0RoJwHdSKWFTYR5WuiAewauSuNaBXned
natas7 bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
natas8 xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q
natas9 is ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
natas10 t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk 