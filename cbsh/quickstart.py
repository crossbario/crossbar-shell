###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Crossbar.io Technologies GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", fWITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

import os
import uuid

import click
import yaml
from cookiecutter.main import cookiecutter

from autobahn import util

README = """# Crossbar.io Quickstart Project

This project was generated using quickstart templates for Crossbar.io based services.

The services are [Docker](https://www.docker.com/) based, and the service bundling is
using [Docker Compose](https://docs.docker.com/compose/).

To check and view the services configuration:

```console
make version
```

To start your services:

```console
make start
```

> Note: the latter is simply starting all services with `docker-compose up`. To start
the services in the background, type `docker-compose up --detach`.
"""

MAKEFILE = """
SUBDIRS = $(shell ls -d */)

version:
\tfor dir in $(SUBDIRS) ; do \
\t\techo "$$dir" ; \
\t\tcat $$dir/service.json ; \
\t\tmake -C  $$dir version ; \
\tdone

start:
\tdocker-compose up
"""

_cookiecutters = [
    # Crossbar.io
    ('gh:crossbario/cookiecutter-crossbar', 'Add a Crossbar.io OSS router'),
    #('/home/oberstet/scm/crossbario/cookiecutter-crossbar/', 'Add a Crossbar.io OSS router'),

    #('gh:crossbario/cookiecutter-crossbar-fabric', 'Add a Crossbar.io Fabric router'),

    # Autobahn
    #('gh:crossbario/cookiecutter-autobahn-python', 'Add an AutobahnPython (Python 3) based component'),
    #('gh:crossbario/cookiecutter-autobahn-js', 'Add an AutobahnJS (NodeJS) based component'),
    #('gh:crossbario/cookiecutter-autobahn-java', 'Add an AutobahnJava (Java8 / Netty) based component'),
    #('gh:crossbario/cookiecutter-autobahn-cpp', 'Add an AutobahnC++ (GCC / ASIO) based component'),

    # third-party
]


def run(cfg):
    click.echo('Crossbar.io project quickstart:\n')

    click.echo('  0: Exit')
    num = 1
    for template, desc in _cookiecutters:
        click.echo('  {num}: {template:50s} -> {desc}'.format(num=num, desc=desc, template=template))
        num += 1
    click.echo('')

    select = None
    while select not in range(num):
        select = click.prompt('Please select a template to initialize, or 0 to exit', type=int, default=1)

    if select > 0:
        click.echo('Initializing cookiecutter {} ...'.format(template))

        extra_context = {
            'uid': os.getuid(),
            'service_uuid': str(uuid.uuid4()),
            'generated': util.utcnow(),
        }
        output_dir='.'

        # cookiecutter returns the fully qualified path within which the template
        # was initialized.
        output_dir = cookiecutter(template, output_dir=output_dir, extra_context=extra_context)

        # the last part of the fully qualified output directory is the service name
        # that comes from "cookiecutter.json"
        service_name = os.path.basename(output_dir)

        readme_filename = 'README.md'
        if not os.path.isfile(readme_filename):
            with open(readme_filename, 'w') as fd:
                fd.write(README)
            click.echo('{} created'.format(readme_filename))

        makefile_filename = 'Makefile'
        if not os.path.isfile(makefile_filename):
            with open(makefile_filename, 'w') as fd:
                fd.write(MAKEFILE)
            click.echo('{} created'.format(makefile_filename))

        docker_compose_filename = 'docker-compose.yml'
        if not os.path.isfile(docker_compose_filename):
            docker_compose = {
                'version': '3',
                'services': {}
            }
            with open(docker_compose_filename, 'w') as fd:
                fd.write(yaml.safe_dump(docker_compose))
            click.echo('{} created'.format(docker_compose_filename))

        docker_compose = None
        with open(docker_compose_filename) as fd:
            data = fd.read()
            docker_compose = yaml.safe_load(data)

        if type(docker_compose) != dict:
            click.error('invalid type {} found in {} for top level object'.format(type(docker_compose), docker_compose_filename))

        if 'services' not in docker_compose:
            docker_compose['services'] = {}

        # we expect the cookiecutter to produce a docker-compose-<service_name>.yml file
        service_docker_compose_filename = os.path.join(output_dir, 'docker-compose-{}.yml'.format(service_name))

        if not os.path.isfile(service_docker_compose_filename):
            click.error('docker-compose fragment for service was not generated by cookiecutter. missing file:\n{}'.format(service_docker_compose_filename))

        service_docker_compose = None
        with open(service_docker_compose_filename) as fd:
            data = fd.read()
            service_docker_compose = yaml.safe_load(data)

        if service_name in docker_compose['services']:
            click.echo('updating service "{}" existing in docker-compose.yml'.format(service_name))
        else:
            click.echo('adding service "{}" to docker-compose.yml'.format(service_name))

        docker_compose['services'][service_name] = service_docker_compose

        with open(docker_compose_filename, 'w') as fd:
            fd.write(yaml.safe_dump(docker_compose))
        click.echo('{} written'.format(docker_compose_filename))