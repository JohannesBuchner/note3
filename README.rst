note3 is a Notational Velocity clone
=====================================

Behaviour: 
-----------

note3 is a note-taking application.
It provides full-text search.
Notes found can be edited.

Full intended behaviour can be found at http://notational.net/

Technology:
------------

note3 is a demo project for using Jython, Maven and SWT to
create easily deployable, native but cross-platform, scripted GUIs.

It shows how to 

  * integrate python libraries using the `maven-jython-compile-plugin <http://mavenjython.sourceforge.net/>`_

  * create scalable, testable, stylable GUI applications in Python

Building:
-----------
Make sure the pom has the target platform-specific swt library as
dependency (swt-gtk for linux, swt-win32/64 for windows).

Run 

::

  $ mvn package

You will find a target/note3-VERSION-jar-with-dependencies.jar
This jar is a fully contained Jython+SWT application. You can launch 
it by double-clicking, or with

::

  $ java -jar target/note3-VERSION-jar-with-dependencies.jar




