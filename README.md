# TBX Coding Task

## Setting up a local build

This repository includes a Vagrantfile for running the project in a Debian VM and
a fabfile for running common commands with Fabric.

To set up a new build:

Once you have unpacked the contents of the zip file follow the following commands to get started.

``` bash
cd tbx-coding-task
vagrant up
vagrant ssh
```

Then within the SSH session:

``` bash
dj migrate
dj createcachetable
dj createsuperuser
djrun
```

This will make the site available on the host machine at: http://127.0.0.1:8000/

# Tasks to complete
Please complete the bugs and features listed below. Please also bear the following in mind while completing the tasks.
- ensure you return this as a git repository with the .git folder.
- make sure you provide tests where appropriate.

## Bugs
We would like you to fix the following bugs.
- Create a ticket - an internal server error occurs DONE
- Update a ticket - an internal server error occurs DONE
- It is possible to move a ticket from one project to another by altering the URL on the edit ticket page. This should not be allowed DONE
- Deleting a project leaves tickets in the database DONE

## Features
Please implement the following features:
- On the project list page, add a new column showing the count of how many tickets there are in each project DONE
- Add ability to comment on a ticket DONE

## Bonus tasks
If you feel like carrying on improving this application, please do! Some ideas are shown below.
- On the project list page, projects that the user has assigned tickets on should be shown above the other projects DONE
- Add the ability to delete tickets DONE
