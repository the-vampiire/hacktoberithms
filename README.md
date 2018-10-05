# hacktoberithms
algorithms to practice python, git, and contribute to an open source repo for hacktoberfest!

# How to Contribute
### only PRs that follow these steps will be approved!
- [sign up here](https://hacktoberfest.digitalocean.com/sign_up/register)
  - read more about HacktoberFest [here](https://hacktoberfest.digitalocean.com/details)
- fork the repo using the `Fork` button in the top right
- clone your fork of the repo using `git clone https://github.com/your_username/hacktoberithms`
- go to the [`Issues`](https://github.com/the-vampiire/hacktoberithms/issues) tab on this repo and view the available challenges
  - you can sort by the difficulty level labels
- create a new branch for your solution `git checkout -b issue_number-solution`
- create a new file called `challenge-title_your_username.py`
  - **create this file in the challenge level directory**
    - look at the label on the challenge issue to see its difficulty
    - look for the corresponding directory in the repo associated with that difficult label
  - this is to make it easier for me to organize the solutions
  - ex: `profile-lookup_rosdyana.py` would go in the `beginner` directory
- work on a solution to the challenge
- commit your work (dont forget to add commit messages) using `git commit -m "your commit message"` or the VSC built-in utility
- **test that it passes all the requirements!**
- when it satisfies the requirements push your work up to your forked repo using
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

## help people who are stuck
- use the Issues comments and PR reviews to help each other improve as developers

## improve a solution
- repeat the process above but modify an existing solution file
- describe what you changed and why so that others can learn how to write better code
- do not make fun of or be rude in refactoring other peoples code. this is about learning not ego
- be prepared to defend your code during the code review process!

## open a new Issue with an algorithm problem so someone else can solve it
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