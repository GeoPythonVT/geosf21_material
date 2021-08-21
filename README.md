# Geo Data Science with Python, Fall 2021

## Submitting Homework

Homework submissions will be accomplished through GitHub. At this point, I am assuming you have worked through the Git Configuration document and successfully added the README file via the command line.

Submitting homework will involve adding your homework to the tracked files, committing changes, and finally pushing your changes to your remote repo.

After you have completed your assignment and saved your final knitted document, in the terminal, do the following:

### Make sure your local copy is synced with your remote copy

```git
git pull
```

### Add your homework files to the list of tracked files
```git
git add <your homework file>
```
### Commit changes you care about
```git
git commit -m "final version of homework"
```
### Push your homework to your remote repo
```git
git push
```

So, the basic workflow is:
```git
git pull
<do work>
git pull
git add ./*ipynb
git add ./*pdf
git commit -m "my first draft"
git push
```
As you work on your homework, you can and should add/commit/push often to save your work! Again, if you want to learn more, check out the docs and the cheatsheet:

https://services.github.com/on-demand/downloads/github-git-cheat-sheet/


# Geo Data Science with Python, Fall 2021

## Submitting homework

To submit homework, you need to use 4 commands (ok, really 3, but the first one is a good habit):
```
git pull
## assuming your homwork was saved as HW1_pid.ipynb
git add HW1_pid.ipynb
git commit -m "HW1 submitted!!"
git push
```

