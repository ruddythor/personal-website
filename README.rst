A Basic Django ARENA FIGHTER
===============

Cue the battle music. Set up your favorite classes. It's time for the lousiest web RPG to hit the Internet since I was in high school.


Really, I don't have install docs because this is more of a personal project, and for learningz.

I'm using Postgres (yay Postgres!). Everything is pretty minimal right now. Clone and run locally to enjoy! (almost)
^ SCRATCH THAT
I got tired of Postgres and changed it to MySQL. If you want to use Postgres, just change the appropriate settings. The dependency is still in requirements.txt.


If you want to play the game as a command line version, go to the old-arena directory and run "python rpg.py". This is the basic
arena fighter before porting it to Django. This will not be updated.


The Following comand should get you up and running

sudo apt-get install libmysqlclient-dev

sudo apt-get install mysql-client

sudo apt-get install mysql-server

[set up your db user with a password of 'root' to avoid any complications with newer ubuntu mysql installs]

mysql -u root -p ('root')

mysql> create database arenafighter;

mysql> create user 'arenafighter'@'localhost' identified by 'arenafighter';

mysql> grant all on arenafighter.* to 'arenafighter';

(venv)josh@elcapitan:~/code/arena-fighter$ ./manage.py syncdb

(venv)josh@elcapitan:~/code/arena-fighter$ ./manage.py migrate


Alternatively, you can install postgres. 

`sudo apt-get install postgresql postgresql-contrib`

`sudo su - postgres`

`psql`

`postgres=# create database arenafighter;`
`postgres=# create user arenafighter with password 'arenafighter';`
`postgres=# ALTER ROLE arenafighter SET client_encoding TO 'utf8';`
`postgres=# ALTER ROLE arenafighter SET default_transaction_isolation TO 'read committed';`
`postgres=# ALTER ROLE arenafighter SET timezone TO 'UTC';`
`postgres=# grant all privileges on database arenafighter to arenafighter;`



the following command will get you into the correct database.

`psql arenafighter -h localhost -d arenafighter`


make sure you run your migrations!




TODO
--------------
Make characters only available to the person who created them -- DONE (i think)
Combat Round system -- DONE
flesh out item use
Improve battle algorithm/enemy vitals
Implement a .defend() action to boost defense for 1 turn





