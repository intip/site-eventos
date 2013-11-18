#!/usr/bin/env python
#-*- coding:utf-8 -*-

from fabric.api import env, run, cd, sudo


env.hosts = ['deploy@192.168.1.69']
env.password = env.passwd

CLONE_PATH = u'/home/deploy/site-eventos/'
PROJECT_PATH = u'/home/deploy/site-eventos'
PYTHON_BIN = u'/home/deploy/.virtualenvs/site-eventos/bin/python'
PIP_BIN = u'/home/deploy/.virtualenvs/site-eventos/bin/pip'
WEBSERVER = u'httpd'


def pull():
    git("pull --rebase")


def restart():
    sudo("supervisorctl restart site-eventos")
    sudo("service %s restart" % WEBSERVER)


def start():
    sudo("supervisorctl start site-eventos")
    sudo("service %s restart" % WEBSERVER)


def stop():
    sudo("supervisorctl stop site-eventos")


def collectstatic():
    manage('collectstatic --noinput')


def deploy():
    pull()
    install_requirements()
    manage('syncdb --noinput')
    manage('migrate --all')
    collectstatic()
    restart()


def fastdeploy():
    pull()
    restart()


def git(cmd):
    with cd(CLONE_PATH):
        run("git %s" % cmd)


def manage(args):
    with cd(PROJECT_PATH):
        run("%s manage.py %s" % (PYTHON_BIN, args))


def install_requirements():
    with cd(PROJECT_PATH):
        run("%s install -M -r project/requirements.txt" % PIP_BIN)
