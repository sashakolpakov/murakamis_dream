# Publication status

This snapshot is prepared locally. **No public repository has been created and no push has been performed. No public URL has been verified.**

The latest sanctioned in-sandbox check was `gh api user --jq .login`. It failed with `error connecting to api.github.com` and `check your internet connection or https://githubstatus.com`. The current blocker is GitHub API connectivity; this check did not establish the current authentication state and displayed no credential. An EARLIER `gh auth status` check reported an invalid token. The earlier outside-sandbox authentication check was rejected by automatic approval review; no escalation, alternate credential route, or authentication retry was performed after that rejection.

The intended public target is `sashakolpakov/murakamis_dream`. This isolated repository uses the account's GitHub no-reply commit identity. The latest refresh includes internally reviewed positive Newton multiplication, the cuboctahedral period, the odd central/four-rung cube packets, and the actual generic recoupling/Racah source identity, with their exact scope and audits. It also retains the corrected EXPOSED-mark hypothesis and exact nested-cap regression. Mathematical source files were not edited by publication preparation.

The general volume conjecture, full cube source control and arbitrary branched-graph survival remain open. Internal analytical reviews and finite audits are not external peer review; a `PASS` output is not by itself an asymptotic proof.

Once normal GitHub access is available, use a user-controlled terminal to check access and inspect whether the target already exists. Do not put credentials in chat. Authentication may separately need repair; the latest connectivity failure does not decide that.

From this prepared repository, the creation command is:

```sh
gh repo create sashakolpakov/murakamis_dream --public --source=. --remote=origin --push
```

This command fails if the name already exists and does not overwrite an existing repository. An existing target must be inspected for owner, visibility, content and compatible ancestry before attaching a remote. No force push is authorized.

```sh
git log -1 --oneline
git status --short
cat PUBLICATION_VALIDATION.json
```

The accompanying Git bundle preserves the same `main` commit. Claim publication only after public visibility and the uploaded commit are independently verified.
