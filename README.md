# git-fish/dev

Welcome to the development branch!

This README file explains different skills helpful for using the command line and git.  Take a look at the git workflow link here to understand forking:

https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow

## Getting started with git

To get started, fork this repo and then clone the fork to your local machine.

To fork the repo: log in to your github account using a web browser and click on the "fork" button!

To clone the repo, open a terminal and type this:

	git clone https://github.com/stackmaps/git-fish.git

To go see whether that worked, use `cd` to navigate into the folder:

	cd git-fish

Now type `ls` to list the files inside the directory, like this:

	ls

You should see the following output:

	README.md
	diver3.gif
	fish.gif
	fish_swimming.py

Use `git status` to see what branch you're on.

	git status

You should see the following message:

	On branch master
	Your branch is up to date with 'origin/master'.

How can you access other branches?  First, retrieve the `dev` branch from the cloud.

	git remote add upstream https://github.com/stackmaps/git-fish.git
	git pull
    git checkout dev
    git pull upstream dev


## Configuring your account

To make your name not appear on github and instead be anonymous run the next two lines::

   	git config user.name "ANONYMOUS"
	git config user.email "imaginary@email.add"

You can change either the ANONYMOUS or imaginary@email.add

##  How to contribute to this repo

Welcome to the `dev` branch!  

Keep your commit history clean and merge process simple by following these steps before starting on any new feature::

Once time only, add this repo as a remote to your fork, e.g.::

HTTPS::
    git remote add upstream https://github.com/stackmaps/git-fish.git

SSH::
    git remote add upstream git@github.com:stackmaps/git-fish.git


Anytime a PR is merged or changes are pushed (or you're starting this process for the first time), you should run::

    git checkout dev
    git pull upstream dev

in order to make sure you are working with an up-to-date copy of the `dev` branch.

Once you have the most recent `dev` code, create a new branch (off of `dev`) for your new feature.

    git checkout -b my-feature

Now you can run `git branch` and should see an output like this:

    $ git branch
      dev
      master
    * my-feature


Pick an issue (or create a new one) which your new feature will address.

Proceed with writing code.  Commit frequently!  Focus on writing very clear, concise commit statements and plentiful comments.  If you have poor comments or zero tests, your PR will not be merged.

## Adding to the repo

If you are aware of changes in the branch you forked from, rebase your branch from that changing branch (in our case that is `dev`) By running:

    git rebase dev

Then resolve all merge conflicts.

Then push all your local changes to your own fork. You should run:

    git push --set-upstream origin my-feature

When your branch is ready (e.g., has comments and tests), submit a Pull Request! To do this, go to GitHub, navigate to your fork (in this case the github extension should be /your-username/stacklearn),
then click `new pull request`. Then change the base to `dev` and the compare to `my-feature.` Finally, click `Create pull request`



IMPORTANT: WHEN YOUR PR IS ACCEPTED, stop using your branch right away (or delete it altogether).  New features (or enhanced versions of your existing feature) should be created on brand new branches (after pulling in all the fresh changes from `dev`).


# Learning Log

 I have learned about how to use git and commands to go along with it. I have also learned how it is helpful in the context of programming.

[ctrl] + x and [ctrl]+s to just save in emacs
and emacs -nw docname to open document

I learned:
- branching in Git
- how rebase and merge are different
- Git commands
Thank you so much!
