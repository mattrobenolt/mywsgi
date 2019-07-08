# mywsgi

Setting up [uWSGI](https://uwsgi-docs.readthedocs.io/) for a new Python project is hard. uWSGI provides a million configuration options
and a million ways to do everything. I have slimmed this down to a core set of basic options.

These options are very opinionated and how I've grown to like doing things.

## How do I

There are two APIs for working with mywsgi. A Python API, and a CLI API.

### CLI

mywsgi comes along with a CLI interface. This is the simplest way to get going.

```sh
$ mywsgi --help
usage: mywsgi [-h] module bind

positional arguments:
  module      python wsgi module
  bind        ip:port to bind to

optional arguments:
  -h, --help  show this help message and exit
```

```sh
mywsgi foo.wsgi:application 127.0.0.1:8000
```

If you want to override or change any uWSGI variables, the only way to do this is through
uWSGI's native environment variables. So something like:

```sh
export UWSGI_MAX_REQUESTS=1000
export UWSGI_HARAKIRI=30
mywsgi foo.wsgi:application 127.0.0.1:8000
```


### Python API

The Python API is simple, it exposes one function with two required arguments.

```python
import mywsgi
mywsgi.run(
    "foo.wsgi:application",
    "127.0.0.1:8000",
)
```

Running this ultimately `exec`s out and hands off all control over to `uWSGI`. So beyond this call,
nothing else will run. Your program is gone.

You can pass additional uWSGI arguments along to this as additional kwargs:

```python
import mywsgi
mywsgi.run(
    "foo.wsgi:application",
    "127.0.0.1:8000"
    max_requests=10000,
    harakiri=30,
)
```

Anything passed in as kwargs is directly passed along to uWSGI and will override my defaults.

## Bring your own uWSGI

This package does not directly require uWSGI, but it supports working with both the `uWSGI` package and the great `pyuwsgi` package.

I'd highly recommend using `pyuwsgi` instead of `uWSGI` directly. `pyuwsgi` is just a compiled binary distribution of `uWSGI`.
