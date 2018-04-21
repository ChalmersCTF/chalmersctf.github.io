# chalmersctf.se

We use [pelican](https://blog.getpelican.com/) to generate our site.

## How to install pelican

Make sure you are using Python 3.6, and follow this steps.

```
$ git clone git@github.com:ChalmersCTF/chalmersctf.github.io.git
$ cd chalmersctf.github.io
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

This will create a new workspace inside the `venv` folder which contains a Python interpreter. By running `source venv/bin/activate` you will update your shell to use all the python related commands found inside the `venv` folder. This means when you install new packages, i.e. from requirements.txt, they will be installed into the `venv` folder, instead of your system, which is nice because it doesn't pollute your system with a bunch of python packages.

## How to write posts and pages

All the content can be found in the `content` folder. Pages can be found in `content/pages` and post categories are the remaining folders. Currently we have two categories, `news` and `events`. In order to create a new category, simply create a new folder inside `content` called `myCategory`. If you want to create a new `event` post, simply create a new `.md` file inside `content/event/my-cool-event.md`. Posts and pages are written in markdown format, check existing content for guidelines.


## Serve the site locally

Simply run `make devserver` which will create a simple HTTP web server listening on port `8000`. See ![Makefile](Makefile) for more commands. The result of the site generation can be found in `output/`.


## How to publish to Github

When you are done editing, follow the these commands in order to push to github:


```
$ make html
$ ghp-import -b master output
$ git push origin master
```

This updates the master branch with the new content found in the output folder.