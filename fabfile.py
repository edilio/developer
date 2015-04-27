from fabric.api import run, env, task, cd, sudo
from fabric.operations import get

"""
pip install fabric

how to run:
fab deploy -H root@www.jedutils.com
"""

ENV_NAME = 'dev'
PROJECT_NAME = 'developer'
PORT = 8011


def gen_unicorn_cmd():
    return 'gunicorn -w 2 -b 127.0.0.1:{} -n {} {}.wsgi:application'.format(PORT, ENV_NAME, PROJECT_NAME)

@task
def deploy():
    home = '/var/www/django/developer'
    with cd(home):
        sudo('git pull')
        run('workon {} && python manage.py collectstatic --noinput'.format(ENV_NAME))
        run('workon {} && python manage.py migrate'.format(ENV_NAME))
        run('workon {} && {} &'.format(ENV_NAME, gen_unicorn_cmd()))