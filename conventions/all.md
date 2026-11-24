# General conventions

Applies to every repo, independent of language or framework.

## Git and pull requests

- **Branches**
  - **Naming**: Name work branches `<type>/<slug>`, where `<type>` is a Conventional Commits type — `feat`, `fix`, `chore`, `refactor`, `ci`, `docs`, `style`, `test`, `perf`, or `build` — and `<slug>` is a short kebab-case description of the change. Never use a `claude/` prefix or a random session suffix.
  - **Renaming an assigned branch**: The naming rule above overrides the branch name a session is assigned by default — if you were given one, rename it before the first push.
- **Commit messages and PR titles**: [Conventional Commits](https://www.conventionalcommits.org), using the branch types above.
  - **Summary**: lowercase and imperative, saying what changes for whoever uses the code, not how (`fix: keep saved filters when another device syncs`).
  - **Scope**: optional; leave it off rather than invent one.
  - **Breaking changes**: `!` only in a repo that versions a public API.
  - **Squash merges**: the PR title is the commit message, with ` (#<number>)` appended.
  - **Squashing several PRs together**: only on command. One summary covering them all, with every PR number at the end, oldest first (`chore: update dependencies (#534, #538, #539)`).
- **PR review threads**: Always reply on the thread with what changed (or why it wasn't changed), then mark the thread resolved. Do this for every thread you act on, not just the ones that needed discussion.
- **Labels**: Every PR and issue carries at least one _type_ label; more than one is fine where a change really is more than one kind.
  - **Type labels**: named for the Conventional Commits type, except `feat` is `feature` and `perf` is `performance`. A PR's labels include its title's type.
    - **`bug` and `fix`**: `bug` is for issues, `fix` for PRs. A PR is never `bug`.
  - **Issues**: titled like the PR expected to close them (`feat: …`), except bugs, which are `bug: …`. `question` stays on while the issue waits on an answer before work can start.
  - **Action labels**: a label a workflow reads (`run ci`, `preview`, `refresh-data`) is named for what adding it does, with a GitHub description saying so. Each repo's `CLAUDE.md` lists its own in a table: label, what adding it does, and the workflow that reads it.
  - **Other labels** (`a11y`, `question`, `help wanted`, `duplicate`, `wontfix`): go beside the type label, never in place of it. Only `a11y` has a title form, as a scope (`fix(a11y): …`). Close `duplicate` and `wontfix` issues with GitHub's matching reason too.
  - **GitHub's defaults**: bring them in line with the table below, renaming rather than recreating so existing issues and PRs carry across.

| GitHub default | Becomes |
| --- | --- |
| `enhancement` | `feature` |
| `documentation` | `docs` |
| `accessibility` | `a11y` |
| `bug` | kept, for issues only; PRs labeled `bug` become `fix` |
| `invalid`, `good first issue` | deleted |
| `question`, `help wanted`, `duplicate`, `wontfix` | kept |

An existing `perf` label is renamed `performance`.

## Tooling

- **Formatting**: Run the repo's format script after making edits and before every commit. Each language's conventions say what it is.

## Testing

- **Testing internals**: Never widen a module's API for a test. Where something is only public so a test file can reach it, keep it internal and drive it through the public thing that uses it — the test then pins behaviour someone can actually depend on, and survives the internal being renamed or absorbed. A repo's test-support module is the exception: being imported by tests is its whole job.
- **Checking a new test can fail**: A test that passes against broken source pins nothing. Before keeping a new case, break the behaviour it names and confirm that case — and ideally only that case — goes red.
- **Trivial cases**: Avoid writing test cases whose whole subject is one plain line in src code, e.g. prop spreads, a simple ternary, specific error types, etc. It restates the line rather than pinning behavior anyone could get wrong, and is one more case to read and keep in step.

## Comments

- **Where a comment goes**: A doc comment (i.e., above a function) is for _callers_ — what the thing is/does, what it gives back, what it costs them, etc. Any note about _how_ it does that, or explaining a cast, a workaround, or a library's behaviour, etc., goes in a line comment _within_ the function _at_ the code it describes, since it doesn't need to be known to the caller. This goes for any function, internal to a file or exported.
- **Doc comment shape**: A doc comment that runs to more than one line opens with its summary alone — what the thing is, usually one sentence — then a blank line before any specifics: conditions, defaults, the reason it's built the way it is. A comment that is only a summary, however many lines it wraps to, needs no gap.

## Writing

- **Oxford comma**: A list of three or more takes a comma before its final `and` or `or` — in prose, comments, documentation, and commit messages alike.
