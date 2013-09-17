bind = "127.0.0.1:8008"
workers = 5
pidfile = "/home/deploy/run/site-eventos.pid"
accesslog = "/home/deploy/logs/site-eventos/gunstdout.log"
errorlog = "/home/deploy/logs/site-eventos/gunstderr.log"
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'http',
                         'X-FORWARDED-PROTO': 'http',
                         'X-FORWARDED-SSL': 'off'}
