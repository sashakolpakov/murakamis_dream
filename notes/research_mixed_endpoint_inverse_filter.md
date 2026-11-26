# A necessary adjacent-block filter for an endpoint input

Research deduction, 5 November 2026. This specializes the exact inverse
equations in [the terminal coupling lemma](research_terminal_coupling_barriers.md)
to either end of a four/four pair and gives a finite interval exclusion
test. It proves no new source comparison and does not assert that a
feasible input is realized by a word.

## 1. Original equations and necessary domain

At the left end of an actual word of length at least three whose first
two types are four, write
\[
 b=s_2,\quad a=t_1=E_4(b),\quad t=t_2,\quad c=s_3.
 \tag{1}
\]
The endpoint map \(E_4\) is its attached coordinate, namely its second
output, with the original certified logarithmic lift. Vertex 2 is
ordinary. At the right end use the reflected labels
\(b=t_{m-1},a=s_m,t=s_{m-1},c=t_{m-2}\).
Only symmetry of the original critical equations is used here; no
symmetry of a chirped finite kernel is asserted.

Put \(U=e^{-2\pi ib},A=e^{-2\pi ia},V=e^{-2\pi it},C=e^{-2\pi ic}\).
The original ordinary equations imply
\[
 (1-UV)(1-UA)=A(1-U)^3,\qquad
 (1-UV)(1-VC)=C(1-V)^3.
 \tag{2}
\]
Consequently define
\[
 \mathcal V(b)=\frac{1-A(1-U)^3/(1-UA)}{U},\qquad
 \mathcal W(b)=\mathcal V(b)+
                  \frac{(1-\mathcal V(b))^3}{1-U\mathcal V(b)}.
 \tag{3}
\]
Every actual reference satisfies
\[
                 \mathcal V(b)=e^{-2\pi it},\qquad
                 \mathcal W(b)=e^{2\pi ic}.
 \tag{4}
\]
The reciprocal convention \(\mathcal W=C^{-1}\) avoids dividing by a
function which may vanish away from actual references.

Both functions in (3) are holomorphic near the full original type-four
input disk. Indeed \(U,A,1-U\ne0\) and \(0<\Re(b+a)<1\), so \(1-UA\ne0\).
Moreover
\[
          1-U\mathcal V=\frac{A(1-U)^3}{1-UA}\ne0.
 \tag{5}
\]
The functions \(\mathcal V,\mathcal W\) themselves can have off-shell
zeros. These zeros are retained, not removed by inverse logarithms.

At an actual reference \(t\in D_4\) and \(c\in D_3\cup D_4\).
For \(m=3\), \(c\) is an attached endpoint leg, not a private leg.
The stronger necessary conditions
\[
 t\in P_4,\qquad c\in P_3\cup P_4,\qquad
 P_3=\{|z-(.35-.01i)|\le.083\},\quad
 P_4=\{|z-(.30-.052i)|\le.060\}
 \tag{6}
\]
follow from [the actual local-factor extraction](research_mixed_open_local_factor_coverage.md).
These statements yield necessary exponential-image tests without a
choice of logarithm. In particular every actual reference has
\(\Im\mathcal V<0\) and \(\Im\mathcal W>0\).

If interval enclosures are contained in these half-planes, principal
logarithms give the unique lifts with real part between zero and one half:
\[
       t(b)=-\frac{\operatorname{Log}\mathcal V(b)}{2\pi i},
       \qquad c(b)=\frac{\operatorname{Log}\mathcal W(b)}{2\pi i}.
 \tag{7}
\]
These are coordinates for exclusion, not a proof of the original
logarithmic equations at arbitrary auxiliary inputs.

**Necessary-domain filter.** A parameter box contains no actual reference
of length at least three if any of the following is certified throughout it:

* \(\Im\mathcal V\ge0\), or \(\Im\mathcal W\le0\);
* the valid lift \(t(b)\) is disjoint from \(P_4\) (or even \(D_4\));
* the valid lift \(c(b)\) is disjoint from both smaller typed disks
  (or even both original typed disks).

Distance tests use strict outward separation. Crossing boxes are
unresolved unless another sufficient exclusion succeeds. Equations
(2)--(6) prove the filter; feasibility is not a converse.

For \(m=2\), both blocks are endpoints, so (2) is not applicable.
Uniqueness of the original two-endpoint critical point and reflection of
the word \(44\) force its two attached legs to coincide. Thus its input
satisfies \(b=E_4(b)\). In addition the
[exact attached four/four extraction](research_mixed_first_cap_oriented_plateau_certificate.md)
gives \(\Re b>.276\). The union of this endpoint fixed-point set and the
set in (6) therefore contains every actual four/four endpoint input for
every \(m\ge2\). Both prescribed boxes below have \(\Re b<.276\), so the
simple attached bound already excludes their length-two case.

## 2. Two prescribed interval diagnostics

The [helper](../experiments/check_mixed_endpoint_inverse_filter.py) is
restricted to two immutable incomplete records: first-cap stage four,
job 19996, and terminal-four stage three, job 39335. It verifies their
hashes, source bindings, exact pending boxes and original endpoint cells.
It revalidates one inherited original root witness per box and applies
twelve same-inverse Taylor intersections. No root is proposed and no box
is subdivided. Equations (3) and (7) are then evaluated outward, recording
all half-plane and typed-disk tests.

An output of “excluded” proves only that the particular box contains no
actual reference; “unresolved” proves no exclusion. The helper does not
evaluate a cap or terminal source inequality and does not change either
incomplete certificate. No execution or successful exclusion is asserted
in this note.

