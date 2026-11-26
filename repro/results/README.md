# Reading the verification records

The current paper checks are in `paper-collection/` and
`manuscript-and-lean/`. Their summaries identify their actual inputs by
hash. The [combined record](manuscript-and-lean/verification-summary.json)
links the builds, finite certificates, declared dependencies and Lean
compilation. Its scope distinguishes these checks from written proofs.

`conway-submission/` records preparation of the fixed seven-paper source
collection. It does not record a remote submission.

The compact `research-*.json` files have a different purpose: they record
arithmetic certificates or finite calculations useful to retained open
research. An embedded hash refers to the version used for that run.
Editorial changes to a linked note can change its hash without rerunning
the calculation. Such a record is not evidence that the current working
tree was checked. Historical hashes are preserved rather than silently
replaced. Rerun the producing program when current-version verification
is needed.

The pre-cleanup sources and small records are available in
[the Git snapshot](https://github.com/sashakolpakov/murakamis_dream/tree/19d5b911bc409486f0e72b51a876a6a2bc70ee02).
Bulk checkpoints and abandoned run dumps were omitted from that source
snapshot and removed from the working collection. Current research
outputs are ignored by default; compact certificates needed by retained
arguments must be deliberately added to Git.
