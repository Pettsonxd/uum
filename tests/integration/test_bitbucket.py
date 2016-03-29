#!/usr/bin/env python

import logging

#################################################################################
# Enable logging

log = logging.getLogger('test.bitbucket')

#################################################################################

import sys

from tests.helpers import GitRepoTestCase

from git_repo.services.service import bitbucket

class Test_BitBucket(GitRepoTestCase):
    log = log

    def get_service(self):
        return bitbucket.BitbucketService(c=dict())

    def get_requests_session(self):
        return self.service.bb.session

    def test_00_fork(self):
        self.action_fork(cassette_name=sys._getframe().f_code.co_name,
                         local_namespace='guyzmo',
                         remote_namespace='abdo2015',
                         repository='git_tutorial')

    def test_01_create(self):
        self.action_create(cassette_name=sys._getframe().f_code.co_name,
                           namespace='guyzmo',
                           repository='foobar')


    def test_02_delete(self):
        self.action_delete(cassette_name=sys._getframe().f_code.co_name,
                           namespace='guyzmo',
                           repository='foobar')

    def test_03_delete_nouser(self):
        self.action_delete(cassette_name=sys._getframe().f_code.co_name,
                           repository='git_tutorial')

    def test_04_clone(self):
        self.action_clone(cassette_name=sys._getframe().f_code.co_name,
                          namespace='guyzmo',
                          repository='git-repo')

    def test_05_add(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo')

    def test_06_add__name(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo',
                        name='test0r')

    def test_07_add__alone(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo',
                        alone=True)

    def test_08_add__alone_name(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo',
                        name='test0r',
                        alone=True)

    def test_09_add__default(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo',
                        tracking='bitbucket')

    def test_10_add__default_name(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo',
                        name='test0r',
                        tracking='bitbucket')

    def test_11_add__alone_default(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo',
                        alone=True,
                        tracking='bitbucket')

    def test_12_add__alone_default_name(self):
        self.action_add(cassette_name=sys._getframe().f_code.co_name,
                        namespace='guyzmo',
                        repository='git-repo',
                        alone=True,
                        name='test0r',
                        tracking='bitbucket')

    def test_13_open(self):
        self.action_open(cassette_name=sys._getframe().f_code.co_name,
                         namespace='guyzmo',
                         repository='git-repo')


