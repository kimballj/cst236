Welcome to CST 236 Lab 1
------------------------

**If you have not already done so. Ensure you have completed the instructions
on blackboard.**

The goal of this lab is to familiarize yourselves with GIT, Python, RST Files, Sphinx and
DocTests. I have divided the lab up into the following categories:\

#. Getting Python Setup
#. Coverting RST (this file)
#. Gitting to know Git
#. Getting to know nose2
#. Getting to know sphinx
#. Continous Integration
#. Lab write-up

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

GITting to know GIT
===================

This lab will not cover every detail of how to use GIT. Instead I have provided a 
brief overview on GIT. The expectation is that you research the additional details
about GIT using online resources such as Atlassian's Tutorial_.

.. _Tutorial: https://www.atlassian.com/git/tutorials/

Creating your own Repo
**********************

If you do not already have a GIT server setup you will now want to 
go to github and register for an account and follow github's instructions
for creating a GIT repo. 

The URL generated from this process is what you will want to clone locally
and send to me at the end of the lab.

Each lab should be committed as a branch to allow each referencing other 
labs throughout this course. The master branch should be used to contain
a project template (one is provided under origin/lab1_template on the CST236 
repo). As the class progresses it's highly recommended that you rebase
changes onto master that you feel would be useful in future labs.

For example:

.. code::

    Master branch             Branch
    |
    O------------------------ Lab1
    |________________________ Lab2
    |
    O
    |
    O
    |
    O
    |
    O------------------------- Lab3

In the above example lab1 and two are both branched off the same version of master
because there wasn't any new reusable code added on master. But after Lab2 you found
several plugins and such that you wanted to use on future labs so you added it to master
and branched Lab3 off the new head of master.

Your first Commit
*****************

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
*************************

GIT branches are useful for collaboration reasons. Branches allow individual team members to
commit code to their personal branch to share with others without affecting the main (master)
branch. 

Branching is also useful because they allow a team member to make as many commits 
as they want and squash them before it's integrated into master. Squashing makes it so
that only one commit message shows up and avoids flooding other team members logs with
too many unnecessary commits. 

One final reason for using branches in GIT is that a project can be setup to build branches
whenever a new commit is made. This allows developers and team members to know the build/test
status for each branch (useful for organizations that use integration branches)

A git branch can be created using "git checkout -b [name_of_your_new_branch]"

To push a new branch use "git push origin [name_of_your_new_branch]"

Use "git branch" to view a listing of all local branches. "git branch -a" to view all local and remote.
The branch indicated with "*" is your current branch.

Switch to the "Lab1_example" branch on the CST236 repo

The now checked out files contain the testing template that will be used for the remaining labs. 
Copy these changes and check them into the master branch on your lab repo. Next create  branch called "lab1" 
push it to the server. This is where the remaining changes for this lab should be pushed(Unless you find 
something that might be useful to have available on all labs)


Rebasing a Branch
*****************

Rebasing a branch is useful when you have changes on a branch that you want on the master branch.

This can be accomplished using the "git rebase" command

Cherry picking allows grabbing a single commit from a branch and adding it to the current branch.

This can be accomplished using the "git cherry-pick" command

Viewing the Log
***************

Using the "git log" command you are able to see many details and commit history for the
current branch. There are many parameters to git log. Review these parameters and try
out a few to better understand git log

Diffing two revisions
*********************

Using the "git diff" command you can diff two commits or even the file itself that was changed
Review the parameters and try out a few to better understand git diff.

Squashing two commits
*********************

One of the nice features of GIT is you can make many commits locally without pushing and they will provide you
with restore points as you develop your feature locally. When it's time to push to an integration branch or
master you will likely want to squash those changes to have all your changes in a single commit. The advantage
of this is you won't flood your fellow engineer's git log.

Research the different ways to squash git commits

Reverting Changes to the last Commit
************************************

Using the "git revert" you can undo changes or cleanup unneed files. 

.. note:: important

    Careful once something is reverted it is gone forever

Review the parameters and try out a few to better understand git revert

Getting to nose nose2
=====================

Nose2 is one of many various unit test tools that are available for python. 
The majority of these testing tools use test framework called unittest or pyunit (if doing a 
google search). 

The difference in the case of Nose2 and pyunit here is that pyunit is what your test is 
written as (in a moment we will see that test classes all inherit from the pyunit modules).
Tools like Nose2 automates finding and running multiple pyunit tests. 

What nose2 provides us:

* Discovery of and execution of pyunit tests
* Converts results into multiple formats (html, junit, etc)
* Automates running of coverage
* Can be setup to run tests in parallel
* Expandable to allow you to write your own plugins ( http://nose2.readthedocs.org/ )

In my cst236 repo that I have provided for you on the Lab1 branch I have provided a sample
setup and test for you to look at and better understand nose.

In the root of the repo you will see a file named nose2.cfg. Nose2.cfg tells nose how you
would like nose2 to be executed. It also provides ways to add additional plugins and configure
those plugins. The contents of the file are as such:

.. code::

    [unittest]                          # All settings after this is for unittest (main plugin)
    start-dir = .                       # Where to execute the tests from
    code-directories = source           # The location where the code to be tested is located
    test-file-pattern = *_test.py       # Defines the pattern to look for when discovering tests (This means every test file must end with _test.py
    plugins = tests.plugins.coverage    # Defines plugins we wish to utilize (in this case we are using a coverage plugin from tests/plugins/coverage
    exclude-plugins = nose2.plugins.coverage
                                        # Defines plugins we wish to disable and not use. In this case we are not using nose2 coverage and using our own plugin instead.

    [output-buffer]                     # Output buffer is a useful plugin that can be used to capture output from tests
    always-on = True
    stderr = True
    stdout = True
        
    [log-capture]                       # Log capture is used to capture logging output from tests
    always-on = True
    clear-handlers = True
    log-level = DEBUG

.. note::

    In the example above each line in the nose2.cfg file must not be indented and must 
    be at column 0 of their respective lines.
    
Now lets take a look at an actual test procedures. The sample test procedure ('source1_test.py')
is located in the tests folder. The term test procedure is used to refer to a logical 
grouping of test cases. With python this is typically a .py file (like the example source1_test).
Many times projects prefer test procedures to be a one to one relationship with the source code
module that they test. So in this case source1_test tests source1.py in the source folder.

If you open the source1_test file you will first notice that we import the function we plan on testing.
This import can be either a function import, module import, or class import. No matter what
you must import the code you plan on testing. The next thing you will see is the line importing 
TestCase.

TestCases are a grouping of steps that verify that the code when given some input will provide the 
expected output. In most cases the TestCases should test a single function (regardless of whether 
that function is in a class). 

To implement a test case you want to first name it something that indicates what is being tested.
in the sample I provided the TestCase "TestGetTriangleType" is used to verify the output from
the function get_triangle_type. TestGetTriangleType inherits from the TestCase so that pyunit
registers this class as a TestCase and will execute it. If our class was not a child or
descendent of TestCase then the tests inside the class would not run.

Next up we have the test_step itself. We see 'test_get_triangle_equilateral_all_int' when writing unit tests
we want to make the code as verbose as to what is going on as possible but at the same time we want to avoid 
lengthy commenting as it creates clutter and maintenance issues. This is why the test step name is so lengthy 
because the test step name indicates exactly what is being tested in that step. You will notice that
the function begins with 'test_' this is another requirement of pyunit. If a function inside of
a TestCase does not begin with 'test_' then it will not be called as a test step. This does
not mean you can't add other functions. In actuality I and other testers would encourage use 
of helper functions or class or modules. It's just important to note that they will note be called
unless one of your test steps call them.

Inside of the two test steps provided you will see two lines. The first is calling 'get_triange_type'
the second is verifying the return from the function. Each test step allows you to add as many
setup up, function calls, etc that you want. Likewise you can compare as many values as you wish.
From a maintenance standpoint it's much better if each of your test steps are singular. This means
that each test step should be only as long as it needs to be to verify the functionality it intends.
In the example provided you can tell by the step name that we are verifying that get_triangle_type
will return equilateral when equilateral lengths are provided in the form of floats.

.. note:: 

    In the example I have split this into two function because we are clearly testing two 
    separate program paths and functionality. By splitting this I make it easier for 
    future test writers to understand what I was testing.
    
There are hundreds of different comparison functions available through pyunit_

.. _pyunit: https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertEqual

If there is a comparison that isn't natively covered in pyunit that you plan on using
often you always have the option to add it as a member function to your local test case 
class. In my job I've often found it helpful to create base tests that I can add common
functionality to so that all my tests can reuse my custom comparisons. For example you
could create something like:
unittest.TestCase => ProjectBaseTest => SpecificTestCaseClass.

Finally, there are a number of functions in TestCase that can be overwritten to aid in testing. 
The major functions most commonly overwritten is:

* setUp: called before each test function. Useful when there is some operation that needs to occur before each test
* tearDown: called after each test function executes. Useful if there is some cleanup that needs to occur after each function

Running your first Nose2 Test
*****************************
To ensure proper setup I have included a test case that you may use as a guide
for the remaining tests.

To execute open a command prompt and execute the following:

.. code::

    nose2

.. note::

    Oh no it looks like Gaben broke the tests. Your job is now to fix the broken tests.
    

Using nose2 you are able to execute a single test using syntax such as the following:

.. code::

    >nose2 -s . tests.source1_test.TestGetTriangleType.test_get_triangle_scalene_all_int

Creating your first test
************************

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

Getting to know Sphinx
======================

Sphinx documentation utilizes in line documentation (function comments see get_triangle_type for example) and
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
*****************

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
#. Did you find the second issue in get_triangle_type? Did you choose to test the code as is or fix the code in get_triangle_type

.. note::

    Please ensure all your work is committed and pushed to your Lab 1 branch. Now submit the assignment through blackboard and include repo and
    drone.io job URLs. Looking on github is a good way to check that I will be able to see all your work.
