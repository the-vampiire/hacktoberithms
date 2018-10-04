# hacktoberithms
algorithms to practice python, git, and contribute to an open source repo for hacktoberfest!

# How to Contribute
- [sign up here](https://hacktoberfest.digitalocean.com/sign_up/register)
  - read more about HacktoberFest [here](https://hacktoberfest.digitalocean.com/details)
- fork the repo using the `Fork` button in the top right
- clone your fork of the repo using `git clone https://github.com/your_username/hacktoberithms`
- go to the `Issues` tab on the repo and view the incomplete challenges
- create a new branch for your solution `git checkout -b issue_number-solution`
- work on a solution to the challenge
- commit your work (dont forget to add commit messages) using `git commit -m "your commit message"` or the VSC built-in utility
- push your work up to your forked repo using
  - `git push -u origin issue_number-solution`
    - the `-u` flag will set the upstream branch on your forked repo so future pushes do not need the remote or branch name
  - `git push` if you have already set the upstream branch
- open a pull request to merge your branch solution into this repo
  - go to your branch on your forked repo
  - hit the `New Pull Request` button next to the branch name on GitHub
  - choose `Base fork: the-vampiire/hacktoberithms`
  - write a pull request message that describes your approach, anything you were stuck on and solved, and instructions on how to use the solution

## If you get stuck
- create a new issue to ask for help if any part of the contribution process is confusing you
- ask a question / discuss about a problem using an Issue comment
- dont post solutions in the comments - create a branch and contribute!

# Other ways to contribute

## improve a solution
- repeat the process above but modify an existing solution file
- describe what you changed and why so that others can learn how to write better code
- do not make fun of or be rude in refactoring other peoples code. this is about learning not ego
- be prepared to defend your code during the code review process!

## open a new Issue with an algorithm problem so someone else can solve it
- use an appropriate label to mark the difficulty level
- use the following template
```
Credit: [adapted from SOURCE NAME](SOURCE URL)

# Challenge

## test data

## starter code

## notes
```

- help people out in the issue comments