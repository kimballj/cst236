Welcome to CST 236 Lab 1
------------------------

**If you have not already done so. Ensure you have completed the instructions
on blackboard.**

Getting Python Setup
====================

#. If you don't already have python 2.7.8 download and install it now
#. Ensure "C:\python27;C:\python27\scripts;C:\python27\lib\site-packages" is in your env path variable
#. Open a command prompt to the root of the CST236 repo and run "python install get-pip.py"
#. pip (python installation package) manages extra modules not included in standard python
#. Run "pip install -r requirements.txt". 

    .. note:: Important

        This will install all standard modules used for this class. If your lab assignment or
        project requires additional modules you must create a requirements.txt file in the root
        of your repo and check it in


Converting RST
==============

Isn't this document format ugly? ReStructured text (RST) is a very powerful "what you see is what you get" markup format for creating documents.
I'm not sure about you but if you run "rst2html.py Lab1.rst Lab1.html" It looks a whole lot better. Granted it would look better with CSS but 
it does accomplish the goal of making it easier to read. 

ReStructured Test is especially useful when working with a GIT repo that works better with plain text files than complex binary (.doc/.chm) files.

.. note:: 

    Each lab for this class will end with a set of write-up questions that must be completed to get full credit for the lab. The write-up must
    be submitted as part of the lab git repo and be in the form of RST capable of being converted using rst2html.

For more information about ReStructured Text see RST_.

.. _RST: http://docutils.sourceforge.net/docs/user/rst/quickref.html


Creating your own Repo
======================

If you do not already have a GIT server setup you will now want to 
go to github and register for an account and follow github's instructions
for creating a GIT repo. 

The URL generated from this process is what you will want to clone locally
and email to me at the end of the lab.

Each lab should be committed as a branch to allow each referencing other 
labs throughout this course. The master branch should be used to contain
a project template (one is provided under origin/lab1_template on the CST236 
repo). As the class progresses it's highly recommended that you rebase
changes onto master that you feel would be useful in future labs.

Your first Commit
=================

No matter the repo no matter what the first commit to the repo should always
be to the .gitignore file. The reasoning for this is to ensure binary files
or other files are not checked in and essentially ruin the repo.

Often when working with GIT you will hear a lot of complaints about
binary files in a GIT repo. For the most binary files are only acceptable
if they are only going to be added and never or rarely modified. The issue
in GIT with binary files is that git does not store files it stores deltas. 
This means on clones GIT downloads the complete list of changes (every commit 
on every branch that has ever been made to a repo). 

At first this seems less like a feature and more like a bug of GIT. But 
statistically on text files like source code this is actually a much more 
efficient way of storing files since statically most changes won't be total
re-writes of the files. Additionally this provides the user with the ability 
to review the entire list of changes after a clone without needing to interact
with a server. In theory this would mean I can clone each of your repos for a 
given lab board a plane with no wifi and grade each of your assignments by
the time I land.

The downfall to this model is binary files such as exes and bitmaps. Every time
an exe is complied a high percentage of the exe is changed. This means with each
commit containing a binary change the other collaborates have much more data to 
fetch.

Now lets get ignoring the binary files out of the way.

#. Clone your repo locally
#. Open a git bash to the root of your repo
#. Execute "touch .gitignore"
#. Add "*.exe" and "*.pyc" to the .gitignore file
#. Add the file to the repo by executing "git add .gitignore"
#. Run "git commit -a -m "Added .gitignore file"
#. Run "git push"

You have now made your first commit and pushed to the server with a message of "Added .gitignore file"

The following set of sections highlight the important git commands. there are many other commands available
and each command has many different parameters. It's highly recommended you spend time with each to 
better understand GIT.

Switching to a new branch
=========================

A git branch can be created using "git checkout -b [name_of_your_new_branch]"

To push a new branch use "git push origin [name_of_your_new_branch]"

Use "git branch" to view a listing of all branches. The branch indicated with "*" is your current branch.

Switch to the "Lab1_example" branch on the CST236 repo

The now checked out files contain the testing template that will be used for the remaining labs. 
Copy these changes and check them into the master branch on your lab repo. Next create  branch called "lab1" 
push it to the server. This is where the remaining changes for this lab should be pushed(Unless you find 
something that might be useful to have available on all labs)


Rebasing a Branch
=================

Rebasing a branch is useful when you have changes on a branch that you want on the master branch.

This can be accomplished using the "git rebase" command

Cherry picking allows grabbing a single commit from a branch and adding it to the current branch.

This can be accomplished using the "git cherry-pick" command

Viewing the Log
===============

Using the "git log" command you are able to see many details and commit history for the
current branch. There are many parameters to git log. Review these parameters and try
out a few to better understand git log

Diffing two revisions
=====================

Using the "git diff" command you can diff two commits or even the file itself that was changed
Review the parameters and try out a few to better understand git diff.

Squashing two commits
=====================

One of the nice features of GIT is you can make many commits locally without pushing and they will provide you
with restore points as you develop your feature locally. When it's time to push to an integration branch or
master you will likely want to squash those changes to have all your changes in a single commit. The advantage
of this is you won't flood your fellow engineer's git log.

Research the different ways to squash git commits

Reverting Changes to the last Commit
====================================

Using the "git revert" you can undo changes or cleanup unneed files. 

.. note:: important

    Careful once something is reverted it is gone forever

Review the parameters and try out a few to better understand git revert

Creating your first test
========================
To ensure proper setup I have included a second test case that you may use as a guide
for the remaining tests.

To execute open a command prompt and execute the following:

.. code::

    nose2

.. note::

    Oh no it looks like Gaben broke the tests. Your job is now to fix the broken tests.

Using nose2 you are able to execute a single test using syntax such as the following:

.. code::

    C:\CST236\Main\CST236>nose2 -s . tests.source1_test.TestGetTriangleType.test_get_triangle_scalene_all_int

Now that you have fixed the broken test lets see what the coverage looks like. Execute the following commands:

.. code::

    nose2 --with-coverage --coverage-report html

* This will generate an html report for the coverage results in htmlcov/index.html.
* If you look at this file the coverage is currently including the tests in the results. 

#. Lets automatically run for coverage by adding the following to nose2.cfg (without spaces or tabs before the lines):

    .. code::
   
        [coverage]
        coverage = .
        always-on = True
        coverage-report = html

#. Change directory being used to gather coverage by modifying "coverage" attribute above to point to the source folder
#. Now rerun nose2 and look at the results. You will notice coverage was automatically run and there is numerous red(uncovered) blocks of code
#. Create additional test cases and functions to get 100% coverage on the provided source code.
#. Now create a new function in a new source file that will take four values to determine if the object is a square or rectangle
#. Create additional tests to completely cover the new function
#. Create .gitignore exceptions for the coverage output folder and .coverage file (binary output from coverage run)

.. note::

    Bonus 15 points for anyone who modifies the function just created to also accept angles and determine if the object
    is a rhombus or disconnected object.

Creating a GIT hook
===================

GIT hooks are useful in ensuring that some project requirement or server requirement is met before or after some
operation of the user. Some example of git hooks can be found below


Sample GIT hook
^^^^^^^^^^^^^^^

Prior to trying this we need to make sure that git.exe and sh.exe are in the path. If using a windows command
prompt you are unable to execute git.exe or sh.exe you will need to add the 'git/bin' folder to your path
variable. For Example: 'C:\Program Files (x86)\Git\bin' on windows 7

Next navigate from the root of your repo to .git/hooks and create a file named "pre-commit" (no file extension)

Now place this code inside of the "pre-commit" file

.. code::

    #!/usr/bin/env python
    import collections
    import subprocess
    import sys

    ExecutionResult = collections.namedtuple(
        'ExecutionResult',
        'status, stdout, stderr'
    )


    def _execute(cmd):
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        status = process.poll()
        return ExecutionResult(status, stdout, stderr)

    changes = _execute(['git', 'diff', '--staged'])
    if 'print ' in changes.stdout:
        print "print detected in changes. Use Logging instead"
        sys.exit(1)
    else:
        sys.exit(0)

Now if you try to commit a file that contains a print it will not allow you to commit (prints in python while ok for
debugging should not be used. Instead using logging as it allows setting log levels and is thread safe)


Create your own GIT hook
^^^^^^^^^^^^^^^^^^^^^^^^

Next update the git hook that will execute your python unit tests in order to commit. This is a good way to ensure
every commit contains working unittests.

Documenting using Sphinx
========================

Sphinx documentation utilizes inline documentation (function comments see get_triangle_type for example) and
ReStructured Text to create end user documentation. This allows the code changes to automatically be updated in
the resulting code.

I've included a template for documenting the source1.py file in the doc folder. This can be built using the following

.. code::

    cd doc
    make html

This will create an index.html in build/html. View this file to get an idea of what this looks like.

** Now build a rst doc for the source file for four sided objects that was created earlier **

.. note::

    Don't forget to add your new rst file to the index to make it accessible


Creating DocTests
=================

Sphinx doctests are useful in that they allow you to embedded checks in code or RST files that checks that changes
to the code are updated in the associated documentation. Imagine the case where you have some defined API but then
you change some of the parameters. If the associated documentation is not updated you'll have a very unhappy customer.

This is where doctests come into play. Doctests provide a check and doctests also get printed to the html output.
There are two ways to include doc tests

Simple doctests
^^^^^^^^^^^^^^^

The simplest method of including a doctest is using the ">>>" operator. For example:

.. code::

    >>> x = 1
    >>> y = 2
    >>> print x + y
    3

In the above example the code will be displayed exactly how it is included in the comment or RST.

Complex doctests
^^^^^^^^^^^^^^^^

Complex doc tests split up tests into 3 - 4 different groups.
* Test setups: provide a set of code to execute before the test specified (does not show up in html)
* Test code: The actual test that gets executed (shows up in HTML)
* Test output: The expected output from executing the test code (shows up in HTML)
* Test cleanup: Steps to take after a test to cleanup after the test (does not show up in html)

Example:

.. code::

    .. testsetup:: *

        x = 1
        y = 2

    .. testcode:: addition

        print x + y

    .. testoutput:: addition

        3

In the above example by indicating '*' for the test setup we are indicating that this setup should be performed for
every testcode block in the file. If we changes that to 'addition' the test setup will only be performed
prior to for the addition testcode.

Executing doctests
^^^^^^^^^^^^^^^^^^

By using the same make as building the html doc above we can execute doctests by running:

.. code::

    make doctest

** Now create doctests for using both simple and complex doctests. **

Continuous Integration
======================

Since testing that has only been executed on a single computer can fail to reveal flaws in both the source code
and the tests. Tests and results which are not consistent and reproducible are useful. Plus how will we be able to
detect the next time that Gaben breaks the build again?

#. Go to Drone.IO_
#. Register Drone IO with your github account.
#. Connect Drone to build your nose2 and doctests.
#. Setup drone to build the nose2 and doctests the same way you built them locally.

* You will want to make sure this will build each branch. This means drone will build each of your builds
* This is a good way to make sure that your tests will work on my computer
* This also ensures that your requirements.txt is correct

.. _Drone.IO: http://drone.io


Lab Write-up
============

Each of the following questions must be copied to your lab write-up and made into section headers. Any code responses
 must utilize rst code block format. Likewise bullet and number lists must follow the same syntax.

#. What was the hardest part of this lab?
#. During the course of this lab, why did we exclude .pyc files?
#. Name three files which would likely need to have a gitignore added?
#. What is a pyunit TestCase?
#. What is the difference between a git cherry pick and a rebase?
#. How could you use git to print out just the author name of a given file for the current version of the repo?
#. During this lab did you explore Tortoise Git or GIT Extensions? If not take a look at them, they probably would be useful for the remainder of the class

.. note::

    Please ensure all your work is committed and pushed to your Lab 1 branch. Now email me the address to your repo and
    drone.io job. Looking on github is a good way to check that I will be able to see all your work.
