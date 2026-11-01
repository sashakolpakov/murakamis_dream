# Protected triangular sums: proof dependencies and formal scope

This review concerns Appendix Q and its use of Appendices N and O. It
checks the new gluing argument, the hypotheses of the results it imports,
and the finite certificates used by its explicit example. It is not an
end-to-end formal verification of the analytic or geometric arguments
in those earlier appendices. The [source manifest](protected-sum-snapshot.json) records
the inspected and published files.

## The claim being checked

Each input is an actual marked diagram obtained from a simple triangulated
sphere and a matching of adjacent triangles. Its cyclic orders, crossing
disk frames, protected nonmatching edge and ordinary face targets are
recorded. Every locally allowed noncentral sector must have a shared
positive weight vector giving a strict rate gap. This requirement
includes sectors whose final coefficient vanishes for a separate global
reason. A bound for the already summed invariant is not this hypothesis.

The operation removes a triangle incident to the protected edge from
each sphere, glues the two boundary triangles with opposite orientations,
and pairs the two former partners. The assertion is that the output has
the same kind of certificate, with at least the smaller input gap.

## Local and global reasoning

The source has polynomial-order quartets
\((u,v,c,B)\) and \((u,a,v,B)\) before the operation, and
\((u,a,c,B)\) afterwards. Here \(u=v=0\) are protected
variables, while \(a,c,B\) are ordinary positive weights.
All three ordinary vertices are distinct.

Write \(b=\log B\), \(Q_a=Q(0,a,B)\), and
\(Q_c=Q(0,c,B)\), using the triangle potential defined in Q.
The deleted singleton triangles contribute \(b/2\) each. Thus
\[
 C_1=b/2+Q_c,
 \qquad C_2=Q_a+b/2,
 \qquad X=C_1+C_2-b.
\]
The two input target sums count \(b\) twice and the output counts
it once. This cancels the removed local contribution exactly. It is
essential to compare the full shared coefficient actions, rather than
independently optimized terms at the crossing.

The new sector map is central to central/central, left to left/central,
and right to central/right. The finite row powers \(b^ic^{N-1-j}\)
give precisely these allowable input sides at both parities. The
inequalities \(Q_a,Q_c\ge b/2\) compare both branches of each
one-sided maximum. No scalar factorization of spectral kernels is used.

Whole-vector rescaling leaves each sector action unchanged. Normalize
the two selected input witnesses to \(B=1\); this makes them agree
at the only shared ordinary coordinate. The protected zeros already
agree. A noncentral output string has a noncentral input string, so the
input certificates give a gap of at least
\(\min(\gamma_1,\gamma_2)\). When an input string is central,
its complete minimizing vector is used instead. This explains why the
proof permits a different vector for each string.

The statement about scaling was made explicit during this review:
these are logarithmic rates, not degree-one polynomial functions of the
weights. Scaling by \(t\) adds \(\log t\) to each crossing rate,
and the target subtraction cancels the total change.

## The imported implications

| Step | Required input and conclusion | Location |
| --- | --- | --- |
| Actual diagram | The new simple sphere, matching and oriented inverse cut determine the crossing disks and primitive peripheral curves. The new half-twist pattern must give one main knot component. | Q, section 2; O's geometric construction |
| Exact finite coefficient | The original cups, caps, reduced mark, parity coset, targets and scalar normalization give the stated polynomial. Each spectral degree is at most \(N-1\). | O's finite-source construction and its cited Morse identity |
| Complementary bound | The finite set of phase-uniform sector envelopes and their shared witnesses give a bound on the entire real spectral cube at both parities. | Q, sections 4–5 |
| Filling transfer | The actual weighted Hermite functional, including repeated-root derivatives, has norm at most \(\prod_e(1+|n_e|/2)\). For fixed twists this has zero exponential rate. | N |
| Nonzero contribution | Positive complete geometry and full-rank shared variables give the central asymptotic; the entire Fourier period and its other charges are controlled. | O's analytic theorem |
| Actual volume | Recorded primitive logarithmic filling equations give smooth completion; the regulator and metric use the same oriented fundamental chain and boundary correction. | O's geometric theorem |
| Full invariant | Choose fixed twists long enough that the action drop is smaller than the source gap, then use the reverse triangle inequality. | Q, section 5; the transfer proposition in the reproduction chapter |

The import check found no additional flat-plat, weak-balance or
Conway-tree hypothesis in O's central-contribution theorem. Its positive
packing construction precedes any terminal decoration. Its conclusion
holds for every sufficiently large integer level of either parity;
it is not a nonvanishing assertion at every finite level. These findings
check compatibility of the hypotheses, not every proof of every imported
analytic estimate.

## The seventeen-region example

The certificate runner verifies the exact source incidence, rational
triangle loads and forty-branch cover. The cover includes every locally
allowed noncentral string: fifteen branches select a nonempty set of
right pieces in regions \(2,4,7,12\), and twenty-five branches cover
the remaining case by selecting a one-sided anchor. Only local
protected-zero pieces are removed. The interval gap exceeds \(0.04\).

The obstruction certificate rules out one required anchored bound,
not every anchored bound. This overstatement was corrected in the guide.
Its dual flow mixes complete and pure-middle rows only at regions
\(2,4,7\), with a right anchor at region 12. All other spectators
use complete rows. It therefore also bounds the restricted comparison
function used in Q. If weak balance held at all four of these regions,
that comparison at the complete packing would be at most the complete
action, contradicting its certified excess greater than \(0.025\).

Attachment at region 15 preserves all four possible failed regions.
The complete variational identity preserves their weights up to common
scale. Repeating tetrahedral attachments on the new side produces
\(17+r\) regions without touching them. The argument concerns the
retained mark and diagram, not every presentation of the same knot.

The [reproduction runner](../check_protected_sums.py) replays both
interval certificates and checks eight exact attachments. It verifies
connected cyclic vertex links, connected face adjacency, closed edge
incidence, Euler characteristic two, the matching, protected edge,
ordinary target counts and unchanged candidate regions. These finite
checks complement the general induction; they do not prove an analytic
limit by extrapolation.

## What Lean proves

[ProtectedSum.lean](../../formal/VolumeLogic/ProtectedSum.lean) adds
22 declarations, including elementary maximum/minimum helpers. Its main
theorem constructs the local C/L/R rates, applies the explicit sector
map and duplicate-target identity, and derives the smaller positive
input gap. Rates, targets, complete actions and gaps are doubled to avoid
division. The two triangle lower bounds are explicit hypotheses.

The finite-list corollary assumes the accumulated comparison and proves
the remaining sum inequality. It does not formalize the graph operation,
the existence of the certificate vectors, their rescaling, the analytic
envelopes, the actual spectral functional, or the hyperbolic volume
identity. The runner checks every exported theorem's logical axioms and
rejects admitted proof steps. Its successful build establishes exactly
the stated finite implications.
