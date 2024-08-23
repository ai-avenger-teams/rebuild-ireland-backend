# Git Local Config

## Per Repo .gitconfig

Replace the following in a file called `.gitconfig` or `.gitconfig-team` at root of the project. Uncomment certain values.

- `Team Member Name`
- `team.member@example.com`
- `@gitHub-ID`
- `~/.gitignore_global`
- `~/.gitconfigs/.gitcommit.tmpl.txt`
- `organization/repo.git`
- `~/path/to/repo/`

**Have you | Can you:**
- [ ] Create an empty .gitconfig in `📂./` root of repository
- [ ] Copy as below.
- [ ] Commit to `{hackathon-repo-name}`
- [ ] Confer with team if all team member can commits.

```plaintext
[core]
    filemode = false
    logallrefupdates = true
    bare = false
    sharedRepository = true

# Edit
[includeIf "gitdir:~/path/to/repo/"]
    path = .gitconfig-team

[user]
    # Edit
    name = Team Member Name
    # Edit
    email = team.member@example.com
    # username = {GitHUBID}
	excludesfile = ~/.gitignore_global

[credential "Windows"]
	# helper = manager
	# helper = "C:/Program Files/Git/mingw64/bin/git-credential-manager-core.exe"

[credential "https://github.com"]
    # username = {GitHUBID}

[remote "origin"]
    # Edit
    url = git@github.com:organization/repo.git
    fetch = +refs/heads/*:refs/remotes/origin/*

[branch "main"]
    remote = origin
    merge = refs/heads/main

[commit]
    template = ~/.gitconfigs/.gitcommit.tmpl.txt
    cleanup = default

# [rebase]
#    autoSquash = true
#    autoStash = true

[pull]
    # merging, not rebasing
    rebase = false  
    ff = only
    # ff = true # default, merge commits as needed, 
    # ff = false # always merge commits, more noise and activity 
    verbose = true

[push]
    default = current
    followTags = true

[fetch]
    prune = true
    pruneTags = true

[http]
	postBuffer = 524288000

[alias]
    co = checkout
    br = branch
    ci = commit
    st = status

```

<sup> **`{value}`**: remove {...} and add in replaced actual value. | **.gitconfig-team** needs testing and editing before deployment.</sup>

> <hr>

## Commit Message Standards

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) | [Article|Tutorial](https://julien.ponge.org/blog/the-power-of-conventional-commits/)
- [KeepAChangelog](https://keepachangelog.com/en/1.1.0/)
- [Gitmoji](https://gitmoji.dev/)

**Versioning**
- [SemVer](https://semver.org/)
- [CalVer](https://calver.org/)
- [EffVer](https://jacobtomlinson.dev/effver/)

<sup>[Alternative Versioning Conventions](https://nesbitt.io/2024/06/24/from-zerover-to-semver-a-comprehensive-list-of-versioning-schemes-in-open-source.html)</sup>

## .GitCommit Template

- An @iPoetDev prefered template for commits is as follows. 
- Also can show from a command line approach <sup>More info needed</sup>

### Configure template

- Configure via `📂./.gitconfig`.
    - Edit per repo [./.gitconfig](./.gitconfig) .. see below as follows.
- Copy the commit template and story under [~/git-configs/.gitcommit.tmpl.txt] locally. 
- Download or copy the sample .gitcommit temaplate from [./.github/local-config/..](./.github/local-config)
- Editing and configuration this will allow VSCode Template to appear the in commit window.

```plaintext
{gitmoji} type: (scope) Short description

branch: main | branch
tag: v.
PREVIOUSLOG 2024.08.dd v0.0.1-0000
CHANGELOG 2024.08.dd v.0.0.1-0000

--- . ---

🔸 bump: .v
    - :
🔸 merge: .intent
    - :
🔸 add: .intent
    - :
🔸 modify: .intent
    - :
🔸 edit: .intent
    - :
🔸 remove: .intent
    - :

opens: #
wip: #
resolves: #
seeAlso: #

BREAKINGCHANGE: ✅ | ❌

---


Co-authored-by: @iPoetDev <ipoetdev-github-no-reply@outlook.com>

```

<sup>`📂./.github/local-config/.gitcommit.tmpl.txt`</sup>

### Template Elements

- [ ] Commit First Line: `type: (scope) Short Description`
- [ ] `{Keep Blank}`
- [ ] Branch: {main|branch-name}
- [ ] Bump: {.v} & short reason for bump
- [ ] Tag: `v0.0.1-0000`
- [ ] `PREVIOUSLOG 2024.08.dd v0.0.1-0000`
- [ ] `CHANGELOG 2024.08.dd v0.0.1-0000`
- [ ] `{Keep Blank}`
- [ ] --- . --- 
- [ ] {Full Description}
- [ ] --- . --- 
- [ ] merge: {`.intent`}   
    - :  
- [ ] add: {`.intent`}   
    - :  
- [ ] modify: {`.intent`} 
    - :    
- [ ] edit: {`.intent`} 
    - :  
- [ ] remove: {`.intent`}
    - : 

- [ ] Connected Issues 
    - opens: #
    - wip: #
    - resolves: #
    - see also: #

- [ ] BREAKING CHANGE: ✅ | ❌  
- [ ] ---  
- [ ] `{Keep Blank}`
- [ ] `{Keep Blank}`
- [ ] Co-authored-by: @GitHub_ID <email>  2023.08.dd
- [ ] Co-authored-by: @GitHub_ID <email>  2023.08.dd

## IDE Commit Editing

- Using VSCode extensions for standardised commit template design. The same template above can be applied via the settings.

### Commit Message Editor

- 🔗<sub>[![](https://img.shields.io/badge/VisualStudio:_Extensions-Commit_Message_Editor-3c8dbc?labelColor=3c8dbc&color=181717&logo=&logoColor=white)](https://marketplace.visualstudio.com/items?itemName=adam-bender.commit-message-editor)</sub>
    - Commit messages can be editable in a customizable form.
        - Standard Template
        - Dynamic Template 
        - Editable Form Inputs
    - This helps you to use a standardized format.
    - Portable configuration to share settings with teammates.
    - A huge textarea on a dedicated tab.
    - Follows the Conventional Commits specification.

> <hr>

## Building a Commit Message

### 1. The First Line: *Commit Subject*

- `<intention|type> [scope?][:?] <message>`
    - *intention|type*: An emoji|text from the list.
    - *scope*: An optional string that adds contextual information for the scope of the change.
    - *message*: A brief explanation of the change.

### 2. Second Line: Blank

- Separate between commit subject and commit body 

### 3. Next Lines: *Commit Body*

#### Branch

#### Bump

#### Tag

#### ChangeLog: SemVer

#### ChangeLog: Add/Modify/Remove/Merge

#### Issues: Autolinks

#### Issues: Breaking Change

### 4. Commit Footer

#### Co-authors

## Gitmoji | Commit Types

> Add a bit of spark for and suggestions for commit activity/intentions.

- 🎨 :art: Improve structure / format of the code.
- ⚡️  :zap: Improve performance.
- 🔥 :fire: Remove code or files.
- 🐛 :bug: Fix a bug.
- 🚑️ :ambulance: Critical hotfix.
- ✨ :sparkles: Introduce new features.
- 📝 :memo: Add or update documentation.
- 🚀 :rocket: Deploy stuff.
- 💄 :lipstick: Add or update the UI and style files.
- 🎉 :tada: Begin a project.
- ✅ :white_check_mark: Add, update, or pass tests.
- 🔒️ :lock: Fix security or privacy issues.
- 🔐 :closed_lock_with_key: Add or update secrets.
- 🔖 :bookmark: Release / Version tags.
- 🚨 :rotating_light: Fix compiler / linter warnings.
- 🚧 :construction: Work in progress.
- 💚 :green_heart: Fix CI Build.
- ⬇️ :arrow_down: Downgrade dependencies.
- ⬆️ :arrow_up: Upgrade dependencies.
- 📌 :pushpin: Pin dependencies to specific versions.
- 👷 :construction_worker: Add or update CI build system.
- 📈 :chart_with_upwards_trend: Add or update analytics or track code.
- ♻️ :recycle: Refactor code.
- ➕ :heavy_plus_sign: Add a dependency.
- ➖ :heavy_minus_sign: Remove a dependency.
- 🔧 :wrench: Add or update configuration files.
- 🔨 :hammer: Add or update development scripts.
- 🌐 :globe_with_meridians: Internationalization and localization.
- ✏️ :pencil2: Fix typos.
- 💩 :poop: Write bad code that needs to be improved.
- ⏪️ :rewind: Revert changes.
- 🔀 :twisted_rightwards_arrows: Merge branches.
- 📦️ :package: Add or update compiled files or packages.
- 👽️ :alien: Update code due to external API changes.
- 🚚 :truck: Move or rename resources (e.g.: files, paths, routes).
- 📄 :page_facing_up: Add or update license.
- 💥 :boom: Introduce breaking changes.
- 🍱 :bento: Add or update assets.
- ♿️ :wheelchair: Improve accessibility.
- 💡 :bulb: Add or update comments in source code.
- 🍻 :beers: Write code drunkenly.
- 💬 :speech_balloon: Add or update text and literals.
- 🗃️ :card_file_box: Perform database related changes.
- 🔊 :loud_sound: Add or update logs.
- 🔇 :mute: Remove logs.
- 👥 :busts_in_silhouette: Add or update contributor(s).
- 🚸 :children_crossing: Improve user experience / usability.
- 🏗️ :building_construction: Make architectural changes.
- 📱 :iphone: Work on responsive design.
- 🤡 :clown_face: Mock things.
- 🥚 :egg: Add or update an easter egg.
- 🙈 :see_no_evil: Add or update a .gitignore file.
- 📸 :camera_flash: Add or update snapshots.
- ⚗️ :alembic: Perform experiments.
- 🔍️ :mag: Improve SEO.
- 🏷️ :label: Add or update types.
- 🌱 :seedling: Add or update seed files.
- 🚩 :triangular_flag_on_post: Add, update, or remove feature flags.
- 🥅 :goal_net: Catch errors.
- 💫 :dizzy: Add or update animations and transitions.
- 🗑️ :wastebasket: Deprecate code that needs to be cleaned up.
- 🛂 :passport_control: Work on code related to authorization, roles and permissions.
- 🩹 :adhesive_bandage: Simple fix for a non-critical issue.
- 🧐 :monocle_face: Data exploration/inspection.
- ⚰️ :coffin: Remove dead code.
- 🧪 :test_tube: Add a failing test.
- 👔 :necktie: Add or update business logic.
- 🩺 :stethoscope: Add or update healthcheck.
- 🧱 :bricks: Infrastructure related changes.
- 🧑‍💻 :technologist: Improve developer experience.
- 💸 :money_with_wings: Add sponsorships or money related infrastructure.
- 🧵 :thread: Add or update code related to multithreading or concurrency.
- 🦺 :safety_vest: Add or update code related to validation.