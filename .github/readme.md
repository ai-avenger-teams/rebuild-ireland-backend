# README: GitHub Settings 

## GitHub.com

> Hackathon Repository Template: 

> A base template for a common and consistent repository initialise and configuration experience.

- Can be 
  - [ ] Cloned from source template on GitHub.com. *<sup>Quickest</sup>*
  - [ ] Cloned standard fashion.
  - [ ] Forked, in public visibility.
  - [ ] Downloaded as a zip.

### Table of Contents

1. [Using a respository template](#using-a-respository-template)
2. [Clone repository template](#clone-repository-template)
3. [Getting Started](#getting-started)
4. [Preconfigured Issues Templates](#preconfigured-issues-templates)
5. [Settings](#settings)
6. [Acknowledgements](#acknowledgements)

## Using a respository template

- [ ] Check if  the tag <sub>![](https://img.shields.io/badge/Private_template-0d1117)</sub> | <sub>![](https://img.shields.io/badge/Public_template-0d1117)</sub> is next to repo name and a green <sub>![](https://img.shields.io/badge/Use_this_template-29903b)</sub> is in top right.
- Clone the template repo.

**Next Steps**

- [ ] Create a new repository:
  - [ ] Select repository template: `{org}/template-hackathon-base`.
  - [ ] Select a `repo owner` or `{org}`.
  - [ ] Assign new repo name & description.
  - [ ] Do not include all branches from source template (`unchecked`).
  - [ ] Designate: `Public` or `Private`.
  - [ ] Grant Marketplace apps access.
- [ ] New repo should have `generated from` source template.

## Clone repository template 

- [ ] Clone to local machine.
- [ ] Check if all team members can clone and fetch to repository.

## Getting Started 

> Per repository settings: https://github.com/{org/owner}/{repo}/settings

### Initial Config

**Settings/Features**
- [ ] Enable, if not already, GitHub Issues.
- [ ] If agreed, ✅ enable GitHub Discussions.
- [ ] If agreed, ✅ enable GitHub Wiki.
- [ ] If agreed, ✅ enable GitHub Sponsorships.

**Issue Picker/Config**
- [ ] Edit [📂./.github/ISSUE_TEMPLATES/config.yml](./.github/ISSUE_TEMPLATES/config.yml) to update urls to new `{org/owner}/{hackathon-repo-url}`

## Preconfigured Issues Templates

**Have you:**
- [ ] Inspect the Issue Templates, preconfigured `yaml` folder, [here](./.github/ISSUE_TEMPLATE/).
- [ ] Update the Issue Templates urls and markdown references for `{org/owner}`/`{hackathon-repo-name}` and for all references.
  - [ ] Update: `{org/owner}`
  - [ ] Update: `{hackathon-repo-name}`
- [ ] Have you tested if the <sub>![](https://img.shields.io/badge/New_issues-29903b)</sub> issue picker and each issue template button works. Don't commit a new issue, just switch to differengt issue on testing.


## Settings

> Per repository settings: https://github.com/{org/owner}/{repo}/settings

**Features to select**:

- [x] General
- [x] Collaborators

<sub>*Code and automations*</sub>
- [ ] Branches: 
- [ ] Tags
- [ ] Rules
- [ ] ~~Actions~~
- [ ] ~~Webhooks~~
- [ ] Environments:
- [ ] Codespaces
- [ ] Pages

<sub>*Security*</sub>
- [ ] ~~Code security and analysis~~
- [ ] Deploy Keys: [Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys)
- [ ] Secrets and variables
  - [ ] Actions
  - [ ] Codespaces
  - [ ] ~~Depandabot~~


<sub>*Integrations*</sub>
- [ ] GitHub Apps
- [ ] Email Notifications: Set up notfications for push events.
- [ ] ~~Autolink references~~

<sub>Items ~~strikedout~~ are unlikely needed in a hackathon</sub>

The following are the MRU settings groups/categories. Left blank for team selection and configuration per hackathon.

### General

### Access: Collaborators

### Branches

### Tags

### Rules

### Environments

### Codespaces

### Pages

### Deploy Keys

- [Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys)

### Secrets and Variables

### GitHub Apps

> Few selections may advance productivity, collavboration and ease of communication etc. Or not.

### Email Notifications

> Pro: 
> - Setup email addresses for all team members to receive notifications when push events are triggered.
> - Setup email address for selected/elected team leads (primary/secondary). Team decision & choice.

> Con: Risk of spam noise to signal during the hackathon. 


### Security Config

- Security Tab: 
  - Security policy: `enabled`: Commit via [`📂./.github/SECURITY.md`](./.github/SECURITY.md)
  - [Dependabot Alerts](https://github.com/{individual}/{hackathon-repo}/security/dependabot) 

## 📂.github/

> Given the hidden nature of `📂.github/`, it is an excellent candiate to store customisation per repoistory instructions, as per below, and other local configs for each team member without impacting the organisation of the visible solutions project files. The benefits of using preconfigured configurations and templares, in a team collborations, are greater consistency and speed to first commit for the solution.

### READMEs

- `📂.github/readme.md` (this) is displayed until `📂./README.md` is edited and loaded in root of project. 
- `📂.github/ISSUE_TEMPLATES/readme.md` outlines the issue templates meta and purposes. Adapt as needed.
- `📂.github/local-config/readme.md` outline the local configurations for post cloning a repository setup. See also [../CONTRIBUTIONS.md](../CONTRIBUTORS.md).
- `📂.github/workflow/readme.md` outline the GitHub actions in use on the repository.

> <sub>This readme.md is located in 📂./.github intentionally as this is a hidden folder and deals with per repo github settings. Edit as needed.</sub>

### Folders

- `📂.github/` stores the following folders:
  - `📂.github/ISSUE_TEMPLATES/` stores issue templates yml GitHub forms. Adapt as needed.
  - `📂.github/local-config/` stores the local configurations and samples for a post-cloning repository setup. See also [../CONTRIBUTIONS.md](../CONTRIBUTORS.md).
  - `📂.github/PULL_REQUEST_TEMPLATES/` stores PR template, as onlly one automatic, markdown template. Adapt as needed.
  - `📂.github/workflow/readme.md` stores the GitHub actions in use on the repository. Some can be located under `📂.github/`.

**Have you**
- [ ] Added a root level README.md
- [ ] Added a read and familarised self with `📂ISSUE TEMPLATES/readme.md` and `📂PULL_REQUEST_TEMPLATES/readme.md`.
- [ ] Copy the contents of local-config to your prefered local settings/per team member.

## Common Files

The following sections cover the common/custom root level files that are best practice and are regularly used. These files can be stored, optionally, under `📂./github/`, though by convention are stored under the root: `📂./`

1. [📂./AUTHORS.md](../AUTHORS.md)
   - [📂./AUTHORS.md Template](AUTHORS.md.tmpl)
2. [📂./CONTRIBUTORS.md](../CONTRIBUTORS.md)
3. [📂./CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md)
4. [📂./CITATION.cff](../CITTATION.cff) <sup>🔸</sup>
      - [📂./CITATION Templatel](CITTATION.cff.tmpl)
5. [📂./CODEOWNERS](../CODEOWNERS)
   - [📂./CODEOWNERS Template](../CODEOWNERSmd.tmpl)
6. [📂./GOVERNANCE.md Template](GOVERNANCE.md)
7. [📂./LICENSE](../LICENSE)
8. [📂./SECURITY.md](SECURITY.md)
   -  [📂./SECURITY_CONTACTS.md](../SECURITY_CONTACTS.md)
9. [📂./SUPPORT.md Template](SUPPORT.md)

<sup>Edit Templates in name or with `.tmpl` extension and remove `.tmpl|.md.tmpl` when ready</sup>

**Have you**
- [ ] Added/edited an Authors file to specify the hackathon team members.
- [ ] Added/edited the Contributors file. [GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [ ] Discussed and Added/edits a Code of Conduct. [GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)
- [ ] Added/edits an Citations file for good referencing. [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)
- [ ] Added/edits Codeowners for defining repository, code/path, and PR codeownership and responsibilities. [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners "About code owners")
- [ ] Added/selected/reviewed the Licence. This is initialised on repository creation. Update as per [Choose An Open Source License](https://choosealicense.com/ "https://choosealicense.com/") | [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

- Consider the more optional, for a hackathon, files, like GOVERNANCE, SECURITY and SUPPORT.

### For example

Using a support file, via a team agreement, could be a useful location for providing contact details and who to ask for help during remote, days to week long events. This could be a centralised location and is always visible when creating issue on GitHub.com or via cloned files.

### Custom Common Files

The following are adopting practices from using GitHub Marketplace apps/actions or per config variants that control the repository and its behaviours/consistency.   

10. [📂./codemeta.json](../codemeta.json)<sup>*Optional*</sup> - See the [CODE FAIR GitHub App]() and `CITATIONS.cff`<sup>🔸</sup>

## Acknowledgements

### Contributors

- <sub>[![Email](https://img.shields.io/badge/Author-Charles%20J%20Fowler-0077B5?logo=gmail&logoColor=white)](mailto:ipoetdev-github-no-reply@outlook.com "Contact CJ on GItHub email: ipoetdev-github-no-reply@outlook.com") <sup>|</sup> [![LinkedIn](https://img.shields.io/badge/Charles%20J%20Fowler-LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://ie.linkedin.com/in/charlesjfowler "@CharlesJFowler @Linkedin.com") <sup>|</sup> [![GiThub](https://img.shields.io/badge/iPoetDev-GitHub-0077B5?logo=GitHub&logoColor=white)](https://github.com/ipoetdev "@iPoetDev @GitHub")</sub>