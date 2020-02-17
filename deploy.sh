#!/bin/zsh

heroku buildpacks:set heroku/nodejs
heroku buildpacks:add --index 1 heroku/python
git push heroku master
