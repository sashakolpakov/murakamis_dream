# Publication status

This snapshot is prepared and committed locally. **No public repository has been created and no push has been performed.**

The sanctioned in-sandbox GitHub CLI check reports that the active `sashakolpakov` credential is invalid. The connected forge was also unavailable because its configured service could not be resolved. An earlier attempt to check GitHub authentication outside the sandbox was rejected by automatic approval review; it was not retried, and no credential-access workaround was attempted.

The prepared public GitHub target is `sashakolpakov/murakamis_dream`. The snapshot uses the account's GitHub no-reply commit identity. Publication preparation did not edit the mathematical workspace. Only the frozen, independently audited central-anchor note, audit and results, plus its prerequisite observed-kernel scope correction, were added at this checkpoint; ongoing even/noncentral research is excluded.

Authenticate in a user-controlled terminal without putting credentials in chat:

```sh
gh auth login --hostname github.com --git-protocol https
```

From this prepared repository, the authenticated publication command is:

```sh
gh repo create sashakolpakov/murakamis_dream --public --source=. --remote=origin --push
```

That command fails if the name already exists; it does not overwrite an existing repository. Inspect any existing target before attaching a remote. No force push is authorized.

To inspect the exact prepared commit and integrity report:

```sh
git log -1 --oneline
git status --short
cat PUBLICATION_VALIDATION.json
```

The accompanying Git bundle preserves the same `main` commit and can be cloned and published in an authenticated environment. A public URL must only be reported after the remote repository and its uploaded commit are verified.
