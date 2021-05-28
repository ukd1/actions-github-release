#!/usr/bin/env python3

from github import Github
import os
wanted_release = os.environ['INPUT_TYPE']
repository = os.environ['INPUT_REPOSITORY']
token = os.getenv('INPUT_TOKEN', None)

G = Github(token)
repo = G.get_repo(repository)
releases = repo.get_releases()
for release in releases:
    if wanted_release == 'stable':
        if release.prerelease == 0 and release.draft == 0:
            print('::set-output name=release::{}'.format(release.tag_name))
            print('::set-output name=release_tarball_url::{}'.format(release.tarball_url))
            print('::set-output name=release_zipball_url::{}'.format(release.zipball_url))
            break
    elif wanted_release == 'prerelease':
        if release.prerelease == 1:
            print('::set-output name=release::{}'.format(release.tag_name))
            print('::set-output name=release_tarball_url::{}'.format(release.tarball_url))
            print('::set-output name=release_zipball_url::{}'.format(release.zipball_url))
            break
    elif wanted_release == 'latest':
        print('::set-output name=release::{}'.format(release.tag_name))
        print('::set-output name=release_tarball_url::{}'.format(release.tarball_url))
        print('::set-output name=release_zipball_url::{}'.format(release.zipball_url))
        break
    else:
        print('Cant get release')
