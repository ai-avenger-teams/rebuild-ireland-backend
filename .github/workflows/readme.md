# Hackathon Repo [] Workflows

## Workflows: Maintenance

### Contributors

#### [Contrubute List](https://github.com/marketplace/actions/contribute-list "GitHub Marketplace|Actions|Contribute List: Contributors-Readme-Action is a simple GitHub action to automate contributors list in README file.")

> Contributors-Readme-Action is a simple GitHub action to automate contributors list in README file. Not only contributors, collborators, sponsors, bots or any user.<br><br>
> As it uses a GitHub action it's secure and very easy to integrate into your projects. Once added it will automatically add all the repository contributors to your readme in a well-formatted table, including future contributors 

- URL: https://github.com/marketplace/actions/contribute-list
- ACTION: [.github/workflows/main.yml](.github/workflows/main.yml)
- ENV: `{GITHUB_TOKEN}`

- [ ] Update the root `📂./Readme.md`, if exists, with the following:

>> Add the below comment inside your README.md where you want it to appear.

```plaintext

<!-- readme: contributors -start -->
<!-- readme: contributors -end -->

```

>> What if you wanted to add direct collaborators of a project, no worries
>> - \#\# Collaborators

```plaintext

<!-- readme: collaborators -start -->
<!-- readme: collaborators -end -->

```

>> \#\# Contributors

```plaintext

<!-- readme: contributors -start -->
<!-- readme: contributors -end -->

```