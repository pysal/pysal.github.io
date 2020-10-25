# PySAL's Main Site 

This is the updated source to pysal.org

# Build instructions

This site is built using Hugo, see [Hugo website](https://gohugo.io/) for documentation and details. 

# Local testing 

Clone this repository locally, and cd into it:

``` 
git clone https://github.com/pysal/pysal.github.io
cd pysal.github.io 
```

Install `Hugo` to build the site. You can use [Homebrew](https://brew.sh/) to install Hugo on macOS and Linux.

```
brew install hugo
```

If you work with a different operating system please see the [Hugo documentation](https://gohugo.io/getting-started/installing/) for additional installing instructions. 

Run the following commands on your terminal to verify that Hugo runs correctly:

Show Hugo's location:
```
which hugo
/usr/local/bin/hugo
```
Verify it runs correctly:
```
hugo version
```
You should see something similar to this:
```
Hugo Static Site Generator v0.13 BuildDate: 2020-10-23T21:34:47-05:00
```
Now you can have Hugo build the website:

```
hugo server -D
```
Open your browser to `localhost:1313/`

Hugo is a fast site generator and will rebuild pages almost instantly. Depending on your text editor, you may have to manually save the file(s) you are working on to see the changes made to the website. 

To stop the server simply press `Ctrl - C` in your terminal. 

# Site Structure

Hugo uses the following [directory structure](https://gohugo.io/getting-started/directory-structure/) to organize content:

```
.
├── archetypes
├── config.toml
├── content
├── data
├── layouts
├── static
└── themes
```
The PySAL wesbite structure emulates the same directory structure. 

# Updating the website

All of PySAL's webiste pages have been set up so that they can be easily updated through markdown files under the content folder(s). 

We have set up the website so that Hugo will automatically use the `partials` files under the '`layouts` folder to render files under the `content` folder. Unless the format/appereance needs to be changed, the files under `layouts` should be kept the same. 

The magic will happen once new files are added to the respective `content` folder. 
 
