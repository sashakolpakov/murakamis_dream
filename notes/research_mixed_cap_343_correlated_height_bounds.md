# Two correlated height bounds for the actual ordinary 343 family

Research result, 8 November 2026. The original cap-initialized
ordinary \(343\) reference satisfies
\[
             \frac7{10}<R<\frac{41}{50},
             \qquad r_s>\frac45R.
\tag{1}
\]
The upper and correlated bounds follow from one prescribed
saved-response certificate on two complete parameter disks.
The lower bound is the earlier radius-exclusion theorem.
No finite-source estimate or complementary-contour bound is
asserted by this geometric result.

## 1. Original branch and precise family

Retain the seven-variable critical point in the order
\[
                   v=(e,a,u,p,y,s,z),
\tag{2}
\]
with the original left cap, vertex types \(3,4,3\), and last
ordinary incidence to the external leg \(b=s_4\).
Thus \(p=s_2\), \(y=t_2\), and \((s,z)=(s_3,t_3)\);
their zero-based coordinate indices are \(3,4,5,6\).
The literal action and original logarithmic branches are those
of [cap-phase entrance, Lemma 1](research_mixed_alternating_cap_phase_entrance.md)
and [the original coverage protocol, equations (5)--(7)](research_mixed_cap_343_radius_coverage_protocol.md).
They give a unique original critical point, holomorphic on a
neighborhood of each of the closed disks
\[
\begin{split}
 P_3&=\{|b-(7/20-i/100)|\le83/1000\},\\
 P_4&=\{|b-(3/10-13i/250)|\le3/50\}.
\end{split}
\tag{3}
\]
Define, on this same branch,
\[
 R(b)=|e^{-2\pi i y(b)}|=e^{2\pi\Im y(b)},\qquad
 r_s(b)=|e^{-2\pi i p(b)}|=e^{2\pi\Im p(b)}.
\tag{4}
\]
In particular \(p\) and \(y\) are coupled outputs of the
original half-chain, not independent points of containing boxes.

**Theorem 1.** Equations (1) hold for every \(b\in P_3\cup P_4\).
They consequently hold at the original geometric reference of
every complete open word in the original powers three and four,
beginning \(343\), with length \(m\ge4\).

For \(m=4\), the leg \(b=s_4\) is attached to the final cap;
for \(m>4\), it is ordinary. The actual domains
\(A_3,A_4,O_3,O_4\) in
[actual reference domains, Sections 1--2](research_mixed_actual_last_row_reference_domains.md)
are contained in the corresponding disks (3).
Restricting the original full critical point to its first three
vertices gives exactly (2), with this value of \(b\).
Uniqueness in the original chamber identifies it with the
holomorphic branch used here. This is the same identification as
in [the radius-exclusion theorem, Section 1](research_mixed_cap_343_radius_exclusion.md).

The complete-ended word \(343\), of length three, has a terminal
third vertex and different final equations. It is excluded.
Conversely the whole-disk statement does not assert that every
independent \(b\) in (3) is realized by a complete word.

## 2. Harmonic proof and the saved certificate

The two real functions
\[
\begin{split}
 f_1(b)&=\frac{\log(41/50)}{2\pi}-\Im y(b),\\
 f_2(b)&=\Im p(b)-\Im y(b)-\frac{\log(4/5)}{2\pi}
\end{split}
\tag{5}
\]
are harmonic on neighborhoods of the closed disks (3).
The [fixed saved-height protocol](research_mixed_cap_343_saved_height_protocol.md)
uses all 512 closed angular cells on each boundary circle.
For every cell it inherits, unchanged, the exact rational center,
preconditioner, original root identification, and both strict
root inclusions from the previous radius certificate.
The midpoint radius is \(2^{-30}\), and the uniform radius is
\(1/256\).

The new mathematical work consists of the uniform original
Jacobian, the two fixed logarithmic constants, and the response
bounds and transported comparisons in protocol equations
(5)--(9). In particular,
the derivative center for \(f_1\) has sign \(+\gamma A_{46}\).
The derivative of \(f_2\) uses
\(-\gamma(A_{36}-A_{46})\), with the error-row difference
\(E_{3j}-E_{4j}\) formed before taking moduli.
The midpoint difference retains both coordinate radii.
The resulting outward interval encloses each \(f_j\) on the
entire closed parameter cell.

The sole saved attempt records the following complete inventories:

| Disk | Test | Completed positive cells | Failed, blocked, inconclusive or unprocessed |
|---|---|---:|---:|
| \(P_3\) | \(f_1\) | 512 | 0 |
| \(P_3\) | \(f_2\) | 512 | 0 |
| \(P_4\) | \(f_1\) | 512 | 0 |
| \(P_4\) | \(f_2\) | 512 | 0 |

Every recorded whole-cell lower endpoint is strictly positive.
For each row of the table, the least of the finitely many
certified lower endpoints is therefore positive. Its exact
rational value is retained in that row's
\(\texttt{harmonic\_whole\_disk\_enclosure\_exact}\) field.
The harmonic minimum principle extends this bound to the
entire closed disk. Thus both functions in (5) are strictly
positive there.

Exponentiating their defining inequalities gives
\[
                 R<41/50,\qquad r_s/R>4/5.
\tag{6}
\]
The [earlier radius-exclusion theorem](research_mixed_cap_343_radius_exclusion.md)
proves \(R>7/10\) on the same two full disks and the same
original branch. Combining it with (6) proves (1).
The actual-word conclusion follows from the identification in
Section 1. \(\square\)

The immutable certificate and its reviewed inputs are:

- [Saved result](../repro/results/research-mixed-cap-343-saved-height-comparisons-attempt01.json):
  \(\texttt{b55fb88f26d07f0cde491d341b8b5f5bff93e69b2c3e1a2ea4a42717bbef76ee}\).
- [Authorized manifest](../repro/protocols/research-mixed-cap-343-saved-height-comparisons.json):
  \(\texttt{a770b957ed9f1c22fc82cfe5b0898dc60966344b39628be76fa7fa7cfdd4886f}\).
- [Protocol](research_mixed_cap_343_saved_height_protocol.md):
  \(\texttt{fd2117a883a3c8dfc54e1141bc3ca866b85351d0326a24308165eccd8c7653d0}\).
- [Checker](../experiments/check_mixed_cap_343_saved_height_comparisons.py):
  \(\texttt{521095d1d3b428c61777627f58b386c2a895b72ff37dc725b8e344821b67dfb8}\).

The result's validity is \(\texttt{provenance\_verified}\).
Its initial and final manifest hashes agree, and its claimed,
initial and final dependency maps agree with all 51 manifest
bindings, including all 45 inherited bindings. The complete
transitive inventory has 10 JSON records and 149 dependency
edges. Both exact-byte static approvals and root authorization
are retained.

A read-only metadata audit checked all 1,024 ordered cells,
all 2,048 comparison records, the unchanged rational centers
and preconditioners, every new cell's 20 passed checks and
each comparison's two passed checks. It also checked the
inherited 64-check inventories, both seven-row inclusions,
24-step histories, and all failure inventories and final hashes.
No margin, saved bound or extremum was recomputed in this audit.
The sole attempt records zero Newton steps, new root solves,
new inclusions, equation evaluations, matrix inversions, action
or dilogarithm evaluations, subdivisions and retries.

## 3. The separate outgoing-radius refinement needs \(m\ge5\)

One later finite-source application also needs a lower bound
for the folded outgoing radius. This does not follow merely
from (1), and no such bound on the whole independent disks
(3) is being claimed.

For an actual complete word as in Theorem 1 with \(m\ge5\),
[open-window inheritance, Theorem 1](research_mixed_open_word_window_inheritance.md)
applies its type-three row at \(j=3\), since
\(3\le j\le m-2\). Both \(s_3,t_3\) then lie in
\[
                    (.30,.39)+i(-.03,.02).
\tag{7}
\]
Consequently, with \(z=t_3\), \(Z=e^{-2\pi i z}\), and
\[
                 \rho=\min(|Z|,|Z|^{-1}),
\]
one has
\[
 \rho=e^{-2\pi|\Im z|}
      >e^{-3\pi/50}>\frac45.
\tag{8}
\]
For the last strict comparison, the elementary logarithm
inequality \(\log x>2(x-1)/(x+1)\), \(x>1\), gives
\[
            \frac{3\pi}{50}<\frac{33}{175}
                              <\frac29<\log\frac54.
\tag{9}
\]
This uses only \(\pi<22/7\). The \(m=4\) case remains within
Theorem 1 but is not included in this window refinement.

## 4. Consequence and remaining source obligations

Theorem 1 supplies exactly the two correlated geometric
hypotheses of
[last-row transport](research_mixed_next_three_correlated_last_row_transport.md),
without replacing \(r_s\ge(4/5)R\) by the stronger condition
\(r_s\ge R\). That theorem retains its own source factors,
reference allocation and contour hypotheses.
Equation (8), when needed elsewhere, has the additional
actual-word restriction \(m\ge5\).

The previously developed source estimates restricted to
\(R\le7/10\) remain inapplicable to this actual family.
The present result certifies geometric inputs for comparisons
on the actual larger-radius range; it does not itself pay a
complete conditional kernel, a first incoming cycle, or any
remaining signed Fourier contour.
