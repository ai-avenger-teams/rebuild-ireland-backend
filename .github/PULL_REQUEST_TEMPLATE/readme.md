# Pull Request Templates

- Only availble in classic .md [markdown template formats](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository).
- Check out the [GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository) for creating a pull request template.
- Notably, only 1 pull request template is on by default.
- For multiple templates, the [query parameter has to be manually tweeked](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/using-query-parameters-to-create-a-pull-request) to extract each one'; which is a bit arcahic. 
- Comparable Issue forms are not available for Pull Request Templates

## Use the Template

## Example Template

```plaintext
# PR 🔂: `{pr-title}`

- [ ] Reviewers assigned
- [ ] Approved
- [ ] Branch From:
- [ ] Branch To: 
- [ ] Commit PR 
- [ ] Add Labels | Milestone | Project

### Related

- Opens: #
- WIP: #
- Resolves: #
- SeeAlso: #

## PR Kind
> Select all that apply, remove those that don't.
- [ ] fix: 
- [ ] feat:
- [ ] docs:
- [ ] chore:
- [ ] refact:
- [ ] style:
- [ ] lint:
- [ ] revert:
- [ ] build:
- [ ] ci:
- [ ] perf:
- [ ] test:
- [ ] release:

## PR Integration Strategy

- [ ] Trunk to Main
- [ ] Main to Release
- [ ] Other

## PR method

- [ ] Merge
- [ ] Squash
- [ ] Rebase

## Description

> Outline the merge

```
-
```

## Visuals

> Attatch Mobile/Desktop or Diagrms#Mermaid

## Tests

- [ ] Yes | No | Define New

## Documentation

- [ ] Type:
- [ ] Purpose: 
- [ ] Path: 
- [ ] Tooling:  

## Integration Tasks

- [ ] Pre-release
- [ ] Release
- [ ] Post Release

## PR Policy

```