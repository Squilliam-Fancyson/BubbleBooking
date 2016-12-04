# Bubble Booking Scheduling System (BBSS)

*Float up a room.*

A class project for COMP 3500 (Software Modeling and Design) at Auburn
University.

---

## Overview

The BBSS is an academic-oriented room scheduling application that finds the
perfect room for your schedule. Whether you're a professor who needs a class or
a student who's hosting an event, the BBSS can help you find which rooms are
available at specific times and locations.

Runs on the [Flask] web microframework. Built off of the [Flask-Foundation]
project.

---

## Contributing

### Source Code

#### Python

The minimum requirement for the application is Python 3.3 and above. To
incidate this, please use a `#!/usr/bin/env python3` shebang line at the top of
every Python file.

#### Flask

Since the functionality of Flask has slightly changed with version 0.11, be
aware of the new `flask` CLI command when debugging `app.run()` should no
longer be used, so if you desire to start a test server, use either `flask run`
or `python -m`.

Flask resources:
* [Creating Websites With Flask]
* [Getting Bigger With Flask]
* [Larger Applications With Flask].

### Version Control

Make sure you're familiar with git version control. We will be using a style
that incorporates a standard development cycle into its branching, so pay close
attention to how you merge and branch your code.

Do not, **under any circumstances**, do a fast forward when merging.

Git resources:
* [Basic git tutorial].
* [Guide to a successful git branching model].

## License

Flask-Foundation is licensed under the BSD license.
The new and modified code for the Bubble Booking Scheduling System is licensed
under the MIT license.

For more info, see LICENSE.md

[Flask]: https://flask.pocoo.org/
[Flask-Foundation]: https://github.com/JackStouffer/Flask-Foundation/
[Basic git tutorial]: https://rogerdudler.github.io/git-guide/
[Guide to a successful git branching model]: https://nvie.com/posts/a-successful-git-branching-model/
[Creating Websites with Flask]: https://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/
[Getting Bigger with Flask]: https://maximebf.com/blog/2012/11/getting-bigger-with-flask/
[Larger Applications with Flask]: https://flask.pocoo.org/docs/patterns/packages/
