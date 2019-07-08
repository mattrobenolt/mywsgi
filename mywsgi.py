from __future__ import unicode_literals

import os
import sys

try:
    basestring
except NameError:
    basestring = str


def prepare_environ(options, env):
    for k, v in options.items():
        if v is None:
            continue
        key = "UWSGI_" + k.upper().replace("-", "_")
        if isinstance(v, basestring):
            value = v
        elif v is True:
            value = "true"
        elif v is False:
            value = "false"
        elif isinstance(v, int):
            value = str(v)
        else:
            raise TypeError("Unknown option type: %r (%s)" % (k, type(v)))

        env.setdefault(key, value)


def run(module, bind, **kwargs):
    options = {
        "auto_procname": True,
        "chmod_socket": 777,
        "die_on_term": True,
        "disable_write_exception": True,
        "enable_threads": True,
        "ignore_sigpipe": True,
        "ignore_write_errors": True,
        "lazy_apps": True,
        "log_format": '%(addr) - %(user) [%(ltime)] "%(method) %(uri) %(proto)" %(status) %(size) "%(referer)" "%(uagent)"',
        "log_x_forwarded_for": True,
        "master": True,
        "module": module,
        "need_app": True,
        "processes": 1,
        "protocol": os.environ.pop("UWSGI_PROTOCOL", "http"),
        "single_interpreter": True,
        "threads": 1,
        "thunder_lock": True,
        "vacuum": True,
        "virtualenv": sys.prefix,
        "wsgi_env_behavior": "holy",
    }

    options.setdefault("%s_socket" % options["protocol"], bind)

    options.update(kwargs)

    prepare_environ(options, os.environ)

    try:
        import pyuwsgi
    except ImportError:
        os.execvp("uwsgi", ("uwsgi",))
    else:
        pyuwsgi.run([])


def cli():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("module", help="python wsgi module")
    parser.add_argument("bind", help="ip:port to bind to")
    args = parser.parse_args()
    run(args.module, args.bind)


if __name__ == "__main__":
    cli()
