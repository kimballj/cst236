Welcome to CST 236 Lab 1
------------------------

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
changes onto master that you feel would be useful in future labs

Your first Commit
=================

Switching to a new branch
=========================

Rebasing a Branch
=================

Viewing the Log
===============

Diffing two revisions
=====================

Diff the current working changes
================================

Reverting Changes to the last Commit
====================================

Creating your first test
========================

Creating a GIT hook
===================

Documenting using Sphinx
========================


Creating DocTests
=================

Lab Write-up
============

Each of the following questions must be copied to your lab write-up and made into section headers. Any code responses provided must 
utilize rst code block format. Likewise bullet and number lists must follow the same syntax.

#. What was the hardest part of this lab?
#. During the course of this lab, why did we exclude .pyc files?
#. Name three files which would likely need to have a gitignore added?
#. What is a TestCase?
#. What is the difference between a git cherry pick and a rebase?