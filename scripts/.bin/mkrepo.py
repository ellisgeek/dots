#!/usr/bin/env python2

"""mkrepo

Usage:
    mkrepo --name <name> --description <description> --url <homepage>
    mkrepo -n <name> -d <description> -u <url>
    mkrepo (-l | --login)
    mkrepo (-h | --help)

Options:
    -h --help                                      Show This Screen.
    -n <name>,  --name <name>                      Name of the repository to create.
    -d <description>, --description <description>  The description of the repository.
    -u <url>, --url <url>                          Homepage of the repository.
    -l --login                                     Interactive Login
"""

from docopt import docopt
import github3
import getpass
import os

authfile = "~/.MKREPO_AUTH"

def twofa():
    code = ''
    while not code:
        code = raw_input('Enter Two Factor Authentication code: ')
        return code

def login(authfile):
    authfile = os.path.expanduser(authfile)

    if not os.path.exists(authfile):
        user = getpass.getuser()
        password = ''

        while not password:
            password = getpass.getpass('Password for {0}: '.format(user))

        note = 'mkrepo.py'
        note_url = 'http://github.com/ellisgeek/mkrepopy'
        scopes = ['repo']

        auth = github3.authorize(user, password, scopes, note, note_url, two_factor_callback=twofa)
        print(auth.token)
        print(auth.id)

        with open(authfile, 'w') as fd:
            fd.write(auth.token + '\n')
            fd.write(str(auth.id))

    else:
        token = id = ''
        with open(authfile, 'r') as fd:
            tomken = fd.readline().strip()  # Can't hurt to be paranoid
            id = fd.readline().strip()

        gh = agithub3.login(token=token)
        if gh:
            print("WOOT You are already logged in!")

def mkrepo(authfile, name, description='', url=""):
    authfile = os.path.expanduser(authfile)
    token = id = ''
    with open(authfile, 'r') as fd:
        token = fd.readline().strip()  # Can't hurt to be paranoid
        id = fd.readline().strip()

    gh = github3.login(token=token)

    repo = None

    var = {}
    var['name'] = name

    if description:
        var['description'] = description
    if url:
        var['homepage'] = url

    print(var)

    repo = gh.create_repo(name=var.pop('name'), **var)

    if repo:
        print("Created {0} successfully.".format(name))


arguments = docopt(__doc__, version='mkrepo 1.0.0')
if arguments['--login']:
    login(authfile)
else:
    mkrepo(authfile, arguments['--name'], arguments['--description'], arguments['--url'])
