# Outcome of the fixed right-strip saved-face comparison

Research record, 7 November 2026. The single prescribed saved-data check
completed with full coverage. Six of the eight real-face families have
strictly negative adjusted saved bounds. The left real transform face
and the right real private face remain inconclusive under the fixed
costs. This records the saved outcome; it does not rerun or refine the
comparison and makes no new phase, root or source evaluation.

## 1. Frozen provenance and complete inventory

The input and interpretation are the
[fixed protocol](research_mixed_three_four_right_strip_saved_faces_protocol.md)
and the [analytic transport proof, Section 8](research_mixed_three_four_private_left_right_extension.md).
The parent executed the sole approved run in session 22904, which ended
with exit code zero. The output is
[the complete saved result](../repro/results/research-mixed-three-four-right-strip-saved-faces.json).

| Artifact | SHA256 |
|---|---|
| Protocol | `613fab372915864925959d52de088d5cf673d4aa4eb46dc6351cc8ac1e4440b6` |
| Analytic cost proof | `4c263a6302e331d0b34e8d2c260c8321a4fe37eb0bda0afac5a4ecc45b6017cc` |
| Standalone checker | `9d43648472fed4156df69b5d22a7f4664903da3cfeca462d8b0bf4d74c6ae35b` |
| Saved result | `abd1f98e09312ba8c6ceffcb88478a8f031730cc845f31e483e8bd143612ea14` |

The saved result verifies all 40,131 original jobs, with 1,911 jobs
in each of the 21 original families. It retains all 15,288 selected
jobs in families 0 through 7. The original own-four reference cells
comprise 1,002 cells with incoming type three and 909 with incoming
type four; no new filter selects a favorable subset. The extra type
coverage is conservative saved-reserve coverage, while the analytic
right-strip transport remains restricted to the actual ordinary (3,4)
reference family.

All 425 recorded dependency bindings passed the final audit. The
record has no changed input, error or unprocessed job. Its counters
for phase, root, primitive, source and derivative evaluations,
optimizer calls, new cells, new exclusions, refinements and source
replays are all zero. Original geometric exclusions retain their
original completed-replay meaning, including both length cases at
each coupled exclusion.

## 2. All eight outcomes

The table copies the recorded family summaries. Every family has
1,911 jobs. An excluded-only job has a null source maximum; it is
not counted as a negative bound. Each successful family has at least
one source-bearing job and every such adjusted upper is strictly
negative.

| Family | Original real face | Cost | Source jobs | Excluded only | Insufficient jobs | Maximum witness | Outcome |
|---:|---|---:|---:|---:|---:|---:|---|
| 0 | t=.15, private main | 7/400 | 1830 | 81 | 145 | 9429 | inconclusive |
| 1 | t=.5, private main | 0 | 1830 | 81 | 0 | 36751 | proved |
| 2 | e=.27, transform main | 0 | 1830 | 81 | 0 | 36731 | proved |
| 3 | e=.49, transform main | 103/2000 | 1828 | 83 | 191 | 318 | inconclusive |
| 4 | corner (.15,.27) | 7/400 | 1828 | 83 | 0 | 9139 | proved |
| 5 | corner (.15,.49) | 7/400 | 1828 | 83 | 0 | 9140 | proved |
| 6 | corner (.5,.27) | 0 | 1828 | 83 | 0 | 36756 | proved |
| 7 | corner (.5,.49) | 0 | 1828 | 83 | 0 | 36757 | proved |

For exactness, the following are the eight recorded maxima of
`original_upper_rational + cost_rational`, in family order. These
fractions are copied verbatim from `maximum_adjusted_upper_rational`;
no rounding or additional threshold comparison is used.

```json
[
  {
    "family": 0,
    "maximum_adjusted_upper_rational": "3483368803166245826495278959220684070392102817959962378884944508544516251063187616841608407766939283/200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 9429
  },
  {
    "family": 1,
    "maximum_adjusted_upper_rational": "-18422104827138741218374178103147440700437541464085013519387533556157390864451826019703644029770911/200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 36751
  },
  {
    "family": 2,
    "maximum_adjusted_upper_rational": "-25000884287371895793533459998834916010859449505524705442544550504056575116658960898225743436322271/500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 36731
  },
  {
    "family": 3,
    "maximum_adjusted_upper_rational": "27167101001433627588760662752913496543223133124387101340556466317645409405614270679857301144085193/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 318
  },
  {
    "family": 4,
    "maximum_adjusted_upper_rational": "-24750928429678355263360120508468953291811901925593409214271378095582180055048607054458185382524823/2500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 9139
  },
  {
    "family": 5,
    "maximum_adjusted_upper_rational": "-2346342654555887672770214355693772703982500310824975111212315129523600057539661781811298755519653/100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 9140
  },
  {
    "family": 6,
    "maximum_adjusted_upper_rational": "-58875557474384158609136696977371127718962445866477467641586315574433108638626767432754817212586849/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 36756
  },
  {
    "family": 7,
    "maximum_adjusted_upper_rational": "-3338619512709901059777753738597405119178402388960473859564530761217697894964894090569790050939481/10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "witness_job": 36757
  }
]
```

The result also retains each original displayed ball, its exact
midpoint and radius, its outward rational upper, its cost, its
adjusted upper and its sign outcome. The complete insufficient-job
lists are `families[0].insufficient_jobs` and
`families[3].insufficient_jobs`; every associated row remains in
`jobs`. All other insufficient-job lists are empty. Nothing is
removed from the saved result in this summary.

## 3. What this establishes and what remains

The fixed comparison proves families 1, 2, 4, 5, 6 and 7 on the
whole original saved cover. In particular, both left-transform
real corners survive the positive transport cost, and all four
real-real corners are paid. The actual ordinary (3,4) interpretation
uses the complete first-cap plane, its exact marginal cancellation
with the terminal plane, and the analytic transfer costs on
incoming real part [9/20,1/2] at the original attached height.

Family 0 has 145 insufficient comparisons and family 3 has 191.
These are limitations of the prescribed saved-upper-bound test.
They do not show that either actual face reaches or exceeds the
geometric rate. They also do not permit replacing the costs,
restricting the reference set, adding exclusions or rerunning this
protocol.

The horizontal main rectangle, penalized alias anchors and physical
complements retain their separate source proofs. The two unresolved
whole real faces, all required connectors and the complete one-circle
assembly are not supplied by this result. No whole terminal bound,
outside-color theorem or new short-filling knot family follows from
this saved comparison alone.
