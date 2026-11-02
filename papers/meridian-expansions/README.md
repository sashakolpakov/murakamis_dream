# Meridian expansions and classical symbols of quantum recurrences

Theorem 1.1 proves every finite inverse-level order of the actual normalized meridian state on disks $|s|<1$ and fixed translated compact sets in the upper half-plane. At order $N^{-r}$ its logarithmic coefficient is an even polynomial of degree at most $r+1$. The highest-degree terms come from the stationary value of the explicitly normalized physical-edge deformation.

The covered sources are strict Conway expressions with independently long fixed signed powers, summed-criterion circle trees, and the full directed circle-tree criterion, including its separate local and mixed degree/twist corollaries. A high-degree vertex in the last two classes can have zero twist. The directed all-orders proof normalizes by each exact child scalar and retains the original conditional error margins.

Theorem 1.2 starts with a specified fixed finite recurrence annihilating the **whole reduced function at every sufficiently large integer level**. It proves that the first nonzero classical symbol vanishes on the analytic characteristic germ. It neither constructs an annihilator by interpolation nor asserts an equality of full recurrence ideals. The exact reduced/full gauge retains the meridian divisor and negative longitude sign. Corollary 8.1 identifies the selected geometric factor using separate marked classical theorems. For its strict class, the fixed power threshold is the maximum of the analytic and classical thresholds; no comparison between those constants is assumed.

The main imports are precise and one-way:

- *Moving-meridian source estimates for strict Conway tangles*, Theorems 1.1–1.2: whole-source reduction, primitive local packet, real-angular bounds, all charges and nonzero joint first contribution.
- *Volume asymptotics for trees of crossing circles*, Theorems 1.1–1.2 and Sections 2–6: the summed source, full Newton kernel and joint Fourier contours. Its Theorem 1.3, Corollary 1.4, equations (7.3), (7.8), (7.9), and Sections 7.1–7.6 supply the directed conditional recursion, error margins, regenerated bounds and restored original endpoint. The directed criterion is recalled in full in Section 4 of this paper.
- *Finite spectral evaluation and uniform filling bounds*, equation (10.11): the full modified-dimension convention, including its $N$-only phase.
- *Exact Newton calculus for tangles with a moving meridian*, Proposition 6.1, Theorem 7.1 and Proposition 8.1: full spectral normals, actual contraction and scalar ledger.
- *Spectral estimates for Conway tangle sources*, Lemma 2.1: finite complete Hermite conditioning.
- *Holomorphic source asymptotics and volume limits for strict Conway compositions*, Lemma 2.1 only: canonical factorial interpolation and every finite bulk order. Its signed high-index recurrence is not a prerequisite of the present pure-source route.
- *Nonparabolic holonomy of trees of crossing circles*, Theorem 1.2 and Corollary 7.1, and *Preferred longitudes of Conway tree complements*, Theorems 1.2–1.3: original-group branch and preferred-longitude identification used only in Section 8.

Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex` in this folder. The illustration `figures/translated-charts.tex` shows the parameter neighborhoods required by a fixed recurrence.

The bounded algebra checker requires Python and SymPy:

```sh
python3 -I papers/meridian-expansions/check.py --output /tmp/meridian-expansion-check
```

The output directory receives `summary.json`; an older summary is removed before validation. The checks derive the reduced/full ratio modulo the actual relation $q^N=-1$, verify the cleared classical divisor/sign, check the rational sine identities, and exercise formal coefficient recovery with finite-jet negative controls. They do not test analytic remainders or identify a geometric representation by finite samples. The written coefficient recovery is also the finite algebra represented by the existing `FormalRegrading` formal module; analytic existence and the operator/source correspondence remain the written arguments here.
