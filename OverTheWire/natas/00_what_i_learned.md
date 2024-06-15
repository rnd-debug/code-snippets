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