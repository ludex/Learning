These files are based on [this tutorial](https://www.youtube.com/watch?v=YdgIWTYQ69A)
about keeping credentials in local environment files.

Copy `.env.example` to `.env`, replace every placeholder with development-only
values, and never commit the resulting `.env` file. API keys should be sent in
request headers rather than query strings so they do not leak through URL logs,
history, caches, or referrer headers.
