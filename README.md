# PySAL's Main Site
This is the source to [pysal.org](https://pysal.org/).

# Build instructions

The site is built using GitHub Pages Jekyll, see [Jekyll
website](https://jekyllrb.com/) for customizing the build process, and detail on how
what where.

# Quick local testing

Clone this repository locally, and cd into it:

```
git clone https://github.com/pysal/pysal.github.io
cd pysal.github.io
```

Install `bundler`, and use it to install the dependencies to build the website:

```
gem install bundler
bundle install
```

Now you can ask Jekyll to build the website.

```
bundle exec jekyll serve liveserve
```

Open your browser to localhost:4000.

Edit the various parts, the `liveserve` option should automatically rebuild and
refresh the pages when changes occur.

To stop serving the website, press **`Ctrl`**-`C` in your terminal

Enjoy.

# What is where

Most pages are located at the place where their URL is, nothing fancy.  Headers
and footer are in `_includes/head.html`, `_includes/header.html`,
`_includes/footer.html`.

The **navbar** is in `_data/nav.yml` and looks like that:

```
head:
    - Home
    - title: Install
      url: https://pysal.readthedocs.io/en/latest/installation.html
    - About Us
    - Documentation
    - title: News
      url: /news
    - title: Releases
      url: /releases

```

which means, insert in order the following links into the navbar:

    - Link to `Home` page, guess the url by yourself. 
    - link to `Install` page, the url is...
    - Link to `About`, guess the url by yourself, 
    - Link to `/news`
    -  ... etc.

The navbar will automatically target `_blank` pages where the url is explicit,
and mark the correct link as the "current" one.

# How do I create a new page?

Create `my_page.html` (will have url `https://pysal.org/my_page.html`)
or `my_page/index.html` (will have url `https://pysal.org/my_page/`), start with the following:
```
-
-
layout: default
title: My Page
---

write some html here (consider you are already inside `<body></body>`)
```

You cannot do it yet with .md file, but you will be able soon.

Add commit (and don't forget to add to `_data/nav.yml`).

# Inspiration

The site was heavily inspired by [Jupyter.org](https://jupyter.org).
