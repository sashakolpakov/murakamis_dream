# Publication status

This snapshot is prepared locally. **No public GitHub repository was created and no push was performed in the restricted session.** The available GitHub CLI had no accessible OAuth credential, and running its authentication check outside the sandbox was rejected by the environment policy. No credential-access workaround was attempted after that rejection.

The target is `sashakolpakov/murakamis_dream`, public. The snapshot uses the account's GitHub no-reply commit identity. The original mathematical workspace is unchanged.

From this prepared repository, authenticate in an unrestricted terminal without putting a token in chat:

```sh
gh auth login --hostname github.com --git-protocol https
gh auth status
```

Then publish with:

```sh
gh repo create sashakolpakov/murakamis_dream --public --source=. --remote=origin --push
```

The create command fails if the name already exists; it does not overwrite that repository. Inspect any existing repository before choosing another name or attaching a remote. No force push is authorized by this snapshot.

To inspect the prepared commit and validation:

```sh
git log -1 --oneline
git status --short
cat PUBLICATION_VALIDATION.json
```

The accompanying Git bundle preserves the same commit and `main` branch, so it can also be cloned and published from an unrestricted environment.
