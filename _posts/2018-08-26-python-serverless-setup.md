---
layout: post
title: My Python Serverless Setup
updated: 2018-08-26
language: en
---

<p class="lead">
    I've been toying around with <a
    href="https://serverless.com">Serverless</a> and Python for a few years on
    my spare time, and more recently at work. I've noticed my basic setup
    (<code>serverless.yml</code> and the directory structure) has remained the
    same, so I've decided to share it in one single place for anyone that could
    find it useful.
</p>

<hr />

You can get the full working source code for this example on Github at
[egrajeda/serverless-python-template](https://github.com/egrajeda/serverless-python-template).

## The `serverless.yml`

Let me start by sharing a simple `serverless.yml` for a single API with two
endpoints, and then I'll start commenting on pieces of it:

```yaml
service: chatty

provider:
  name: aws
  runtime: python3.6
  stage: dev

package:
  individually: true

functions:
  hello:
    handler: functions/hello/lib/function.main
    environment:
      NAME: ${opt:name, "John Doe"}
    events:
      - http: GET hello
    package:
      exclude:
        - ./**
      include:
        - functions/hello/lib/function.py
        - functions/hello/venv/lib/python3.6/site-packages/**

  joke:
    handler: functions/joke/lib/function.main
    events:
      - http: GET joke
    package:
      exclude:
        - ./**
      include:
        - functions/joke/lib/function.py
        - functions/joke/venv/lib/python3.6/site-packages/**

plugins:
  - serverless-plugin-aws-alerts

custom:
  alerts:
    stages:
      - production
    topics:
      alarm:
        topic: ${self:service}-${self:custom.config.stage}-alerts
        notifications:
          - protocol: email
            endpoint: me@egrajeda.com
    alarms:
      - functionErrors
      - functionThrottles
  config:
    region: ${opt:region, self:provider.region}
    stage: ${opt:stage, self:provider.stage}
```

## The directory structure

I create one directory per function to try and keep their code, tests and
dependencies as separate as possible. In this example, each function has its
own directory: `functions/hello/` and `functions/joke/`.

![The directory structure](/images/python-serverless-setup-structure.png){: .float-left}

The function handler's code is always inside `lib/function.py`. I create as
many files inside `lib/` as necessary, but the entry point is always in the
same place. The corresponding tests to all this code is under `tests/`.

I also initialize each function directory with a `setup.py` file, a virtual
environment under `venv/` and the list of requirements **for each specific
function** in `requirements.txt`.

## The virtual environment

Each function's directory is initialized with a virtual environment:

```
$ cd functions/hello
$ python -mvenv venv
$ source venv/bin/activate
```

I then define and install its dependencies:

```
$ pip install -r requirements.txt
```

The virtual environment is then used in each function declaration in
`serverless.yml`:

```yaml
package:
  exclude:
    - ./**
  include:
    - functions/hello/lib/function.py
    - functions/hello/venv/lib/python3.6/site-packages/**
```

As you can see, it is stated that only `lib/function.py` and its dependencies
should be packaged and then uploaded.

When your code runs online, it won't be able to find its dependencies unless
you manually update the `sys.path` at the top of each file that will use them.
These are the first lines of `functions/joke/lib/function.py`:

```python
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../venv/lib/python3.6/site-packages"))

import requests # Any manually installed dependency has to be added *after* updating the path
```

## The `setup.py` file and running the tests

I create a `setup.py` with the [standard
content](https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use)
and specifying where the tests are located:

```python
from setuptools import setup, find_packages

setup(name='joke',
      packages=find_packages(),
      test_suite='tests')
```

Then I use it to run the tests:

```
$ cd functions/joke
$ source venv/bin/activate
$ python setup.py test
```

Make sure to create an empty `__init__.py` file under `tests/` or the script
won't be able to run the tests.

## Package each function individually

I package each function individually to avoid Serverless from creating one
single big ZIP file and uploading it to every function:

```yaml
package:
  individually: true
```

Under normal circumstances, Serverless will generate one single ZIP package and
upload that to S3:

```
$ sls package
$ ls -lh .serverless/*.zip
-rw-r--r-- 1 egrajeda egrajeda 18M Aug 25 20:59 .serverless/chatty.zip
```

If you package them individually, Serverless will generate one ZIP package per
function:

```
$ sls package
$ ls -lh .serverless/*.zip
-rw-r--r-- 1 egrajeda egrajeda 3.8M Aug 25 21:11 .serverless/hello.zip
-rw-r--r-- 1 egrajeda egrajeda 4.8M Aug 25 21:11 .serverless/joke.zip
```

## The `${self:custom.config}` parameters

I store all my custom variables under `custom.config`, which I then reference
throughout `serverless.yml`.

This example doesn't use any resources, but if I was using DynamoDB tables or
SNS topics I would be assigning their unique names to variables:

```yaml
custom:
  config:
    region: ${opt:region, self:provider.region}
    stage: ${opt:stage, self:provider.stage}
    dynamoDb:
      confTable: ${self:service}-${self:custom.config.stage}-conf
    sns:
      newTransactionsTopic: ${self:service}-${self:custom.config.stage}-new-transactions
```

## The `serverless-plugin-aws-alerts` plugin

No much to say here as the
[serverless-plugin-aws-alerts](https://github.com/ACloudGuru/serverless-plugin-aws-alerts)
name is pretty self-explanatory.

I've recently started to use this plugin to monitor certain aspects of my
functions without having to manually setup the alerts.

## Deployment

Nothing special here, but I did want to mention something that took me a while
to discover: [referencing CLI
options](https://serverless.com/framework/docs/providers/aws/guide/variables#referencing-cli-options).

In the example, one of the functions expect the `${opt:name}` variable to be
passed through the CLI by using `--name`:

```yaml
functions:
  hello:
    handler: functions/hello/lib/function.main
    environment:
      NAME: ${opt:name, "John Doe"}
```

So when I deploy this, I would use:

```
$ sls deploy -v --name="Eduardo"
```

## And that's it

The whole post ended up being longer than I originally expected even though I
had to leave some stuff out (e.g. creating resources and the
[serverless-pseudo-parameters](https://github.com/svdgraaf/serverless-pseudo-parameters)
plugin).

If you're working with Serverless and Python, I hope you find it useful, and if
you have ideas on how to improve this setup, please let me know!

