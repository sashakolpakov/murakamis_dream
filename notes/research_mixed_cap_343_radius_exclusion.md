# The ordinary cap-initialized 343 family lies outside the deeper-radius estimate

Research result, 8 November 2026. The shared parameter of every
ordinary cap-initialized \(343\) reference satisfies
\[
                         |Y_*|>7/10.
\]
Thus the recently proved estimate with the additional hypothesis
\(|Y_*|\le7/10\) does not apply to any reference in this family.
The earlier analytic inequalities remain conditional statements;
they give no knot coverage here.

## 1. The geometric family and the statement

Use the original cap and ordinary-block equations of
[the local next-source theorem, Section 2](research_mixed_three_four_next_local_source.md).
The first two vertex types are three and four, and the third
vertex is an ordinary three. Let \(b=s_4\) be the next external
leg. The unknowns are
\[
                 (e,a,u,p,y,s,z).
\]
Here \(e,a,u\) belong to the first capped vertex, \(p,y\) are the
two legs of the four, and \(s,z\) are the two legs of the following
three. In particular \(y=t_2\), and \(Y_*=\exp(-2\pi i y)\).
The seven original logarithmic equations, including their
branches, are written in equations (5)--(7) of
[the fixed coverage protocol](research_mixed_cap_343_radius_coverage_protocol.md).

Consider the two closed reduced input disks
\[
\begin{split}
P_3&=\{|b-(7/20-i/100)|\le83/1000\},\\
P_4&=\{|b-(3/10-13i/250)|\le3/50\}.
\end{split}
\tag{1}
\]
The unique original critical point depends holomorphically on
\(b\) on a neighborhood of each disk. This follows from
[cap-phase entrance, Lemma 1](research_mixed_alternating_cap_phase_entrance.md).
It retains the original left cap and the final ordinary incidence.

**Theorem.** For every \(b\in P_3\cup P_4\), the shared coordinate
of this original seven-variable critical point satisfies
\[
       \Im y(b)+\frac{\log(10/7)}{2\pi}>0.
\tag{2}
\]
Consequently \(|\exp(-2\pi i y(b))|>7/10\).

For an actual complete open word in the original powers three
and four, beginning \(343\) and of length at least four, the
third vertex is ordinary. If the word has
length four, its external leg \(b=s_4\) is attached to the last
cap. If the word is longer, that leg is ordinary. The
[actual reference domains](research_mixed_actual_last_row_reference_domains.md)
place it in \(A_3,A_4,O_3\), or \(O_4\), according to its type
and role. Each such set is contained in the corresponding disk
in (1). Thus the theorem applies to every such actual reference.
It makes no assertion about the complete-ended word \(343\),
whose third vertex is terminal and obeys different equations.

## 2. Proof on the whole disks

Set
\[
             m(b)=\Im y(b)+\frac{\log(10/7)}{2\pi}.
\]
This is harmonic near both closed disks. It is therefore enough
to give a strictly positive lower bound on each entire boundary
circle.

The protocol partitions each circle into the 512 closed angular
intervals
\[
       [2\pi k/512,\,2\pi(k+1)/512],
                    \qquad 0\le k<512.
\tag{3}
\]
The intervals retain their endpoints and cover the circle.
For each interval, the certificate establishes a strict
complex-disk contraction for the original seven equations,
uniformly over every parameter in that interval. The branch
and chamber tests identify the resulting roots with the
holomorphic critical point above. A separate smaller inclusion
certifies its midpoint value.

The implicit derivative of these same equations bounds the
variation of \(m\) over the whole interval. More precisely,
equations (12)--(15) of the protocol give an interval containing
\[
             m(b_{\mathrm{mid}})+[-\omega L,\omega L],
             \qquad \omega=\pi/512,
\]
where \(L\) bounds the absolute angular derivative on the
whole interval. The recorded outward interval has strictly
positive lower endpoint in every one of the 1,024 cases.
There are no failed, inconclusive, or unprocessed cases.

For each circle, take the least of its finitely many certified
lower endpoints. The resulting rational number is positive;
the exact values are recorded in the whole-disk margin
enclosure field of the result below.
The harmonic minimum principle extends this positive bound to
the entire closed disk. This proves (2).

Finally, \(|\exp(-2\pi i y)|=\exp(2\pi\Im y)\). Equation (2)
therefore implies
\[
       |\exp(-2\pi i y)|>\exp(-\log(10/7))=7/10.
\]
The actual-word conclusion follows from the input inclusions
already stated. \(\square\)

## 3. The fixed certificate

The checker was run once, after the protocol, code, settings,
and source dependencies were fixed and reviewed. It used
256-bit outward ball arithmetic, the 1,024 intervals in (3),
and the prescribed independent rational starting vector for
every interval. No retry, subdivision, saved-root evaluation,
action evaluation, or dilogarithm evaluation occurred.

The complete result is
[the radius-coverage record](../repro/results/research-mixed-cap-343-radius-coverage-attempt01.json),
SHA256
\[
\texttt{1edec732c28ac64dd11ca63026722e8062a0598aa49b15ea2f2887a7dcbdb3d5}.
\]
It contains both root inclusions, branch checks, derivative
bounds, transported margin intervals, all fixed identifiers,
and initial and final dependency hashes. Its provenance
validation succeeded. Each disk has 512 completed positive
cells and no other cell verdict.

The frozen inputs are:

- [Protocol](research_mixed_cap_343_radius_coverage_protocol.md):
  \(\texttt{971fb50a335c9ad3588ef431e09ee0ccd204e6ef95c4b14b23695b96dbe070ae}\).
- [Checker](../experiments/check_mixed_cap_343_radius_coverage.py):
  \(\texttt{ce4942685353371270917272a5d069e230df2597df5207ae5d52c11117c27084}\).
- [Manifest](../repro/protocols/research-mixed-cap-343-radius-coverage.json):
  \(\texttt{45091a7e3284acbcf4d8adf03267ef505f378d8a019f3a867aba7ca77255fb25}\).

The bound uses complete parameter intervals and a harmonic
minimum principle. It does not extrapolate from a list of
numerical roots.

## 4. Consequence for the volume-conjecture argument

The [complete lower-left estimate at deeper radius](research_mixed_next_three_deep_radius_complete_lower_left.md)
assumes that the actual reference has \(|Y_*|\le7/10\).
The theorem above shows that its actual ordinary \(343\)
subfamily is empty. Its conditional nonzero lower-half
asymptotic must therefore not be invoked for these words.

The next source comparison must apply to the actual range
\(|Y_*|>7/10\). The already proved local geometric contribution
and the estimates whose hypotheses do not impose the excluded
radius restriction retain their stated scope. The remaining
signed contour terms and stability under arbitrary short
partial fillings are still unproved. No new knot volume
identity follows from this exclusion theorem.
