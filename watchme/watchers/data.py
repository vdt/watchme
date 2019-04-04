'''

Copyright (C) 2019 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''

from watchme.logger import bot
from watchme.utils import ( 
    which, 
    get_user
)

from watchme.command import get_commits
import os

# Data Exports


def export_dataframe(self, task,
                           filename, 
                           name=None,
                           from_commit=None,
                           to_commit=None,
                           base=None):
    '''Export a data frame of changes for a filename over time.

       Parameters
       ==========
       task: the task folder for the watcher to look in
       name: the name of the watcher, defaults to the client's
       base: the base of watchme to look for the task folder
       from_commit: the commit to start at
       to_commit: the commit to go to
       grep: the expression to match (not used if None)
       filename: the filename to filter to. Includes all files if not specified.
    '''
    if name == None:
        name = self.name

    if base == None:
        base = self.base

    # Quit early if the task isn't there
    if not self.has_task(task):
        bot.exit('%s is not a valid task for %s' % name)

    repo = os.path.join(base, self.name)
    if not os.path.exists(repo):
        bot.exit('%s does not exist.' % repo)

    filepath = os.path.join(base, self.name, task, filename)

    # Ensure that the filename exists in the repository
    if not os.path.exists(filepath):
        bot.exit('%s does not exist for watcher %s' %(filepath, name))

    # Now filepath must be relative to the repo
    filepath = os.path.join(task, filename)

    commits = get_commits(repo=repo,
                          from_commit=from_commit, 
                          to_commit=to_commit,
                          grep="ADD results %s" % task,
                          filename=filepath)

    #for commit in commits:                        
    print(commits)