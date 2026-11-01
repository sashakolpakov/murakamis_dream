# Polynomial products, formal coefficients, and the volume-proof interfaces

This reading began at commit `021e6482b99f8456b4a34912e9f97969fc546a69`.
It revisited the finite source and canonical-degree arguments in Chapter 2
and Appendices N and M, the analytic contribution in O, and its use by P
and Q. It also checked the new formal statements against their mathematical
meaning. It is not a complete rederivation of the quantum tangle matrices,
the circle-packing existence theorem, or every geometric reconstruction.

## Two corrections to the manuscript

Appendix Q used \(Q(0,11,14)\) in the argument locating a balance failure.
The integers there are face labels. The actual inequality is

\[
 Q(0,e^{q_{11}},e^{q_{14}})\ge\frac12q_{11}.
\]

It follows by evaluating the defining maximization at its simplex vertex
for the weight \(e^{q_{11}}\). The corrected text defines the weights at
the point of use. This does not change the certificate or its numerical
margin.

Appendix O wrote \(B_{e,N}\to C_e>0\) in its second account of the charge
estimate. Its actual conclusion is holomorphic convergence to a function
\(B_{e,0}(\delta^2)\), with \(B_{e,0}(0)=C_e>0\). The limit away from
zero need not be constant. On a smaller fixed complex chart, continuity
and uniform convergence give \(\operatorname{Re} B_{e,N}>0\) for all
sufficiently large levels. This is precisely the property needed for
the displayed positive imaginary part of the first-charge critical point.
Both corrections have also been made in the corresponding research notes.

## The finite algebra now proved in Lean

`MonicProduct.lean` constructs multiplication of ascending coefficient
lists. It proves the coefficient identities, including associativity,
and proves that multiplying a constructed monic multiple gives another
multiple of the same modulus. Applying the existing synthetic division
identity then gives

\[
 \operatorname{rem}_p(fg)=
 \operatorname{rem}_p\bigl(\operatorname{rem}_p(f)
                              \operatorname{rem}_p(g)\bigr).
\]

The theorem does not assume compatibility of multiplication with a
quotient. It constructs the relevant multiple in its proof. Canonical
products are associative and may be reduced after every multiplication
in a finite list. No degree restriction on the initial factors is needed.
The top-coefficient functional has the same value after these reductions;
it is not asserted to be multiplicative.

At a repeated root \(r\), the canonical remainder retains both the value
and the formal derivative. In particular the product derivative is
\(f'(r)g(r)+f(r)g'(r)\), even if either value vanishes. This remains true
when the modulus contains further roots. The existing permutation theorem
allows the two occurrences of \(r\) to be placed first. No inverse root
difference or characteristic-zero assumption is used. Appendix N now
states and proves these facts in ordinary polynomial notation.

`FormalRegrading.lean` treats a bivariate series as its table of
coefficients. The substitution \(u=hs\) places \(B_{a,b}\) at the index
\((a+b,b)\). Reading that entry recovers the original coefficient, so
the substitution is injective. The range consists exactly of tables
whose \((n,b)\) entry vanishes when \(b>n\). The module also proves the
precise finite-order statement: equality through order \(h^L\) is
equivalent to equality of the original coefficients with \(a+b\le L\).
The nonzero term \(h^{L+1}\) supplies an explicit limitation of every
finite truncation, with \(1\ne0\) required for that example.

This checks the coefficient argument in Appendix M. It does not prove
existence of the all-orders expansion, its analytic remainders, the
actual operator identity, or the longitude identification. The module
does not claim a formal-series multiplication theorem or an analytic
estimate with \(s\) growing like the quantum level.

## The source estimates used by the volume conclusions

The local interpolation in O was checked against the cited cofactor
proofs. The required complex estimates precede interpolation: the
interior and protected cofactor constructions control the actual complex
recurrences, including the odd skipping summand and the even physical
anchor. Cauchy–Lagrange interpolation is applied only after this outer
control has been supplied. Derivative estimates use smaller complex
domains. The argument does not infer derivatives from agreement at the
physical nodes alone.

The global angular argument also distinguishes its steps. It first
bounds every physical node, restores the omitted terminal-node factors,
and controls the interpolation norm on the whole real interval. A
polynomial complex-growth estimate then extends it to a thin strip.
The separated-spectral estimate is a different input. The connected
ordinary face graph permits these two bounds to be combined while
retaining the original common coefficient weights and targets.

The charge argument uses exact sign pairing, a nonzero amplitude and
bounds for the entire remaining Fourier period. The geometric argument
separately retains primitive logarithmic filling periods, smooth metric
completion and the absolute regulator calibration. P and Q supply their
own full complementary-source bounds before the finite norm theorem in N
is applied. No general full-remainder estimate is imported into their
proofs from O.

These checks found no further defect in the examined interfaces. The
full source for a general unchanged matched sphere is still not bounded
by these arguments. The odd-level estimate for a single cap, with its
other spectra fixed, does not supply that missing result.

## The dependency check and what it means

The [declared map](../manuscript_logic.json) has seventeen nodes for the
N–Q interfaces. Full volume conclusions must supply six separate roles:
exact invariant, nonzero contribution, full remainder, specified metric,
absolute volume, and final rate transfer. The checker propagates the
written hypotheses, checks level scope and source anchors, and rejects
cycles. Seven deliberately invalid substitutions test those checks.

The map is authored mathematical metadata. Its consistency does not
verify its nodes, and its source hashes establish provenance rather than
truth. It deliberately includes the unresolved general remainder. The
weak-balance and protected-sum routes retain their own sufficient
conditions and their fixed-data quantifiers. Independently negative
filling integers are allowed by requiring large absolute values.

The combined Lean build and axiom report are in
[the proof-logic result](../results/proof-logic/summary.json). The
[dependency-map result](../results/manuscript-logic/summary.json) records
the source snapshot and invalid substitutions. These replace neither
the written analytic estimates nor the geometric proofs.
