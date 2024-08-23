# Contributing Guides
First of all, thank you for your effort to improve this action. This guide will help you regarding various aspects like putting issues, contributing a feature, etc.

## Code of Conduct
This project and everyone participating in it is governed by the [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please read the full text so that you can read which actions may or may not be tolerated.

## Before Submitting a Pull Request
Before submitting your pull request make sure the following requirements are fulfilled:

**Option 1**: Full/Internal Collaborator Status

- Check for your contributor/collaboator repository status
- Check for your contributor/collaboator repository permissions
- Clone the repository
- Ensure main branch is branch protected.
- Create a new branch for your contribution.
- Do an initial fetch and pull with IDE or CDE enviornment
- Confirm back to team repository maintainer(s)
- Copy the commit template and story under [~/git-configs/.gitcommit.tmpl.txt] locally. 
- Download or copy the sample .gitcommit temaplate from [./.github/local-config/..](./.github/local-config)
- Edit per repo [./.gitconfig](./.gitconfig) .. see below as follows.
- Make a 1st commit and confirm successful push or troubleshoot, with repository maintainer, the config issues.
- Change necessary code for bug fix, a new feature
- Check linting and format it
- Create a new Pull Request. 
- Contact PR approvers.

**Option 2**: External Contributor Status
- Fork the repository
- Create a branch from main
- Run per language {package-manager-init} in the repository root
- Check, and update, `[.gitignore](./.gitignore)` to exclude any package management, `.env` files or locations of stored secrets.
- Change necessary code for bug fix, a new feature
- Check linting and format it
- Create a new Pull Request. 
- Contact PR approvers.

## Reporting an issue
Before submitting an issue, you need to make sure:

- Use the <sub>![](https://img.shields.io/badge/New_issues-29903b)</sub> issue picker under GitHub Issues.
- These use GitHub Issue forms<sup>* *beta*</sup>.
- Kindly provide an adequate description and a clear title
- If a field is not absent, these issue can be edited in plain markdown once submitted.

### Good First Issue

- Supply your contact information or GitHub handle/url. Note, will be public, so disclose with care..
- Write a summary of how to address the issue.
- List the steps to reproduce the issue.
- Ask or list any questions or clarifications.
- Update the labels as necessary.

## Per Repo .gitconfig

Replace the following in a file called `.gitconfig` or `.gitconfig-team` at root of the project.

- `Team Member Name`
- `team.member@example.com`
- `~/.gitignore_global`
- `~/.gitconfigs/.gitcommit.tmpl.txt`
- `organization/repo.git`
- `~/path/to/repo/`

```shellscript
[core]
filemode = false
logallrefupdates = true
bare = false
sharedRepository = true
autocrlf = true

[user]
name = Team Member Name
email = team.member@example.com
excludesfile = ~/.gitignore_global

[commit]
template = ~/.gitconfigs/.gitcommit.tmpl.txt
cleanup = default

[remote "origin"]
url = git@github.com:organization/repo.git
fetch = +refs/heads/*:refs/remotes/origin/*

[branch "main"]
remote = origin
merge = refs/heads/main

[http]
postBuffer = 524288000

[includeIf "gitdir:~/path/to/repo/"]
path = .gitconfig-team

[alias]
co = checkout
br = branch
ci = commit
st = status

```

<sup>**.gitconfig-team** needs testing and editing before deployment.</sup>