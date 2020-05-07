# nOAuth

This is an OAuth server that performs zero actual authentication and
is to be used for TESTING ONLY!

It has no state, and does just enough to be a valid oauth2 server as
far as standard oauth libraries are concerned.

Run this with:

```
pipenv install
PORT=<port> pipenv run python app.py
```

The OAuth URLs are:

* `/authorize`
* `/oauth/token`
* `/userinfo`

This only does OAuth2 bearer tokens and lets you fake authentication as any email address.


