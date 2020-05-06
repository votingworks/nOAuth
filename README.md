# Mock OAuth Server

This is an OAuth server to be used for TESTING ONLY!

It has no state, and does just enough to be a valid oauth2 server as
far as standard oauth libraries are concerned.

Run this with:

```
pipenv install
FLASK_ENV=production PORT=<port> pipenv run python app.py
```

The OAuth URLs are:

* `/authorize`
* `/oauth/token`
* `/userinfo`

This only does OAuth2 bearer tokens and lets you authenticate as any email address.


