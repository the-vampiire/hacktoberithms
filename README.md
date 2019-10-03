# Hacktoberithms!
algorithm challenges to practice python, javascript, git, and helping each other learn in an open source repo for [hacktoberfest](https://hacktoberfest.digitalocean.com/)!

## ~~Python Solutions Only!~~ Python & JavaScript Solutions This Year!
- feel free to fork this repo and make one for another language
- open an issue with a link and ill update this readme with your language fork so people can find it
- feel free to remove old solutions from your fork or to add a `language/` dir to keep them all side by side

## dont forget to register for hacktoberfest first!
- you need to register first to begin tracking your contributions
- [read about hacktoberfest and sign up here](https://hacktoberfest.digitalocean.com/)

# How to Contribute

## only PRs that follow these steps will be approved!

## Fork and Clone
- fork the repo using the `Fork` button in the top right
- clone your fork of the repo onto your machine using `git clone https://github.com/your_username/hacktoberithms`
- if you have already forked / cloned then feel free to just create a new branch for your next solution

## Find a Challenge
- go to the [`Issues`](https://github.com/the-vampiire/hacktoberithms/issues) tab on this repo and view the available challenges
  - you can sort by the difficulty level labels
- select a challenge you want to work on
  - **your PR solutions can not all be from the `beginner` category**
  - if you are stuck ask for help in an issue but do your best to progress into more advanced categories
- **dont look at previous solutions!**
  - you dont learn anything by copying someone else
  - try your best and open issues to discuss and get help
  - **anyone caught copying previous solutions will be blocked and reported to the hacktoberfest maintainers**
  
## Create a Branch
- create a new branch for your solution `git checkout -b issue_number-solution`
  - ex: `git checkout -b 1-solution` for Issue `#1`
  
## Create a Solution File
- **all solutions must be in a single file**
- **you may not use any external dependencies to solve any problem**
- **solutions must be possible to run using `python 3.7+` or `node 10+`**

### Solution file / location format
- solutions go in the corresponding `language/challenge-level/challenge-name_your_user_name.ext`
  - where `ext` will be either `.py` or `.js`

### Python Solutions
- **must go in `python/challenge-level/` directory
  - ex: a python solution for an intermediate level problem: `python/intermediate/`
  - look at the label on the challenge issue to see its difficulty
  - look for the corresponding directory in the repo associated with that difficulty label
- create a new file in that `language/challenge-level` directory called `challenge-title_your_username.py` 
  - ex: `profile-lookup_rosdyana.py` would go in the `python/beginner` directory
- work on a solution to the challenge
- commit your work (dont forget to add commit messages as you progress)
  - using `git commit -m "your commit message"` or the VSC built-in utility
  
### JavaScript Solutions
- **must go in `javascript/challenge-level/` directory
  - ex: a javascript solution for an intermediate level problem: `javascript/intermediate/`
  - look at the label on the challenge issue to see its difficulty
  - look for the corresponding directory in the repo associated with that difficulty label
- create a new file in that `language/challenge-level` directory called `challenge-title_your_username.js` 
  - ex: `profile-lookup_rosdyana.js` would go in the `javascript/beginner` directory
- work on a solution to the challenge
- commit your work (dont forget to add commit messages as you progress)
  - using `git commit -m "your commit message"` or the VSC built-in utility
  
## Merging
- **test that your solution passes all the requirements before opening a PR!**
  - feel free to write unit tests or to just use print statements
  - most challenges include some sample inputs / outputs to test against
- **confirm that your solution is in the correct directory and using the `challenge-name_user_name.ext` format**
- when it satisfies the requirements push your work up to your forked repo using
  - `git push -u origin issue_number-solution`
    - the `-u` flag will set the upstream branch on your forked repo so future pushes do not need the remote or branch name
  - `git push` if you have already set the upstream branch
- open a pull request to merge your branch solution into this repo
  - go to your branch on your forked repo (under your username)
  - hit the `New Pull Request` button next to the branch name on GitHub
  - choose `Base fork: the-vampiire/hacktoberithms`
- write a pull request message that includes:
  - your approach / thought process
  - anything you were stuck on and how you solved it
  - instructions on how to run your solution 
- i will review and merge as many as i can a few nights a week
  - on the weekends i will catch up with any that i missed

# Getting help

## If you get stuck
- create a new issue to ask for help if any part of the contribution process is confusing you
- ask a question / discuss about a problem using an Issue comment on the relevant challenge issue
- **dont post solutions in the comments - create a branch and contribute!**

# Other ways to contribute

## help people who are stuck
- use the Issues comments and PR reviews to help each other improve as developers

## help write unit tests to automate the process
- i check these solutions by hand
- helping by writing some unit tests would be awesome and a good way to practice writing tests

## help analyze / test solutions that are in PR
- look for open PRs and test out their solutions locally
- leave comments (tagging me) if anything goes wrong
- feel free to review their code and provide feedback like i (try to) do

## improve a solution
- repeat the process above but modify an existing solution file
- describe what you changed and why so that others can learn how to write better code
- do not make fun of or be rude in refactoring other peoples code. this is about learning not ego
- be prepared to defend your changes during the code review process!

## open a new Issue with an algorithm challenge so someone else can solve it
- use an appropriate label to mark the difficulty level
- use the following template
- **make sure the problem statement is open source / public domain or one you created yourself**
  - **do not forget to add a url to the license if one is available**
```
Credit: [adapted from SOURCE NAME](SOURCE URL)
[License](LICENSE URL)

# Challenge

## test data

## starter code

## notes
```
