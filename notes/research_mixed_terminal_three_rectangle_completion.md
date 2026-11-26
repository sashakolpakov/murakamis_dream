# From the terminal rectangle to the full lower transform half

Research assembly, 5 November 2026. This note combines the original
residue identity with the completed zero mode and the twelve alias
comparisons. The exhaustive alias author and independent 320-bit
saved replay have both passed all 40,164 jobs. The exact central
rectangle and the entire lower transform half therefore have the
same original nonzero packet. A separately proved right-band bound
extends that retained packet through transform index \(.59\).
Every retained outer row includes its whole physical Newton sum.
No new numerical check is performed here, and the remaining right
triangle stays outside the conclusion.

## 1. Original source and the central rectangular packet

Use the exact type-three terminal transform
\[
 \mathcal V_{0,N}(w,X)=
 \sum_{i=0}^{N-1}\frac{X^{-i}p_i(X)}{P_i}
                       \mathcal U_{0,N}(w,r^i),
 \qquad r=e^{-2\pi i/N},\quad X=e^{-2\pi ia}.
\tag{1}
\]
The [literal Newton reduction](research_mixed_terminal_three_newton_reduction.md)
holds separately at each outer physical index. Its double summand is
\[
 F_N(i,l;a,w)=
 N\frac{(-q)^{-l}e_l(w)}{P_l}
       \frac{X^{-i}p_i(X)p_i(r^l)}{P_i^3},
 \qquad q=e^{\pi i/N}.
\tag{2}
\]
It vanishes exactly whenever \(i+l\ge N\), independently of
the ordinary color. On its physical support it equals the simultaneous
interpolation \(\mathcal I_N(a;i/N,l/N,w)\) from
[the joint zero-mode theorem](research_mixed_terminal_three_joint_zero_mode.md).
Both the original factor \(N\) in (2) and every diagonal/chirp
factor remain present.

Fix an actual type-three terminal reference \(a_*=A+iH\), with
its selected \((t_*,u_*)\), original action \(\mathcal P_0\),
and neighboring type \(\nu\in\{0,1\}\). For
\(a=y+iH\), \(y\in P=[.22,.45]\), define
\[
 B_\nu(a_*;y)=\Re\Pi_{0,\nu}(a_*)
     +\Re\Pi_{0,\nu}'(a_*)(y-A)-\kappa(y-A)^2,
 \quad \Pi_{0,\nu}=\mathcal P_0-\nu g/2,
 \quad \kappa=1/2500000.
\tag{3}
\]
At \(\nu=1\), the actual reference height is negative, so the
original unselected neighboring Fourier halfweight has rate
\(-\Re g(y+iH)/2\). Its negative convex remainder is favorable
relative to (3). No selected-neighbor or positive-height Fourier
extension is made.

Let \(a_N,b_N\) be the inward half-grid cuts of \([.15,.50]\),
and \(c_N^-,c_N^+\) those of \([.10,.40]\), in lower/upper
order. These are real cuts; \(d_N(X)\) below continues to mean
the original Fourier polynomial.
Each lies within \(1/N\) of its limiting endpoint. Set
\[
 \mathcal R_N(a,w)=
 \sum_{a_N<i/N<b_N}\ \sum_{c_N^-<l/N<c_N^+}F_N(i,l;a,w).
\tag{4}
\]
This rectangle lies strictly inside \(i+l<N\).

**Theorem 1.** The entire
finite rectangle (4), including every residue alias, has the
allocated upper bound
\[
 |\mathcal R_N(y+iH,w)|\,
 |d_N(e^{-2\pi i(y+iH)})|^{\nu/2}
 \le \exp\{N(B_\nu(a_*;y)+\varepsilon)\}
\tag{5}
\]
for every fixed \(\varepsilon>0\), on a sufficiently small fixed
ordinary-color disk and for sufficiently large \(N\). At the
actual target and complete color, before this external allocation,
\[
 \mathcal R_N(a_*,-2)=
 \frac{2\pi}{N}\,
 \frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
 e^{N\mathcal P_0(a_*)}(1+O(N^{-1})),
 \qquad H_*=-\mathcal T''_{(t,u)}(a_*;t_*,u_*).
\tag{6}
\]
The coefficient is nonzero and has the original Gaussian branch.

*Proof.* The [exact alias reduction](research_mixed_terminal_three_alias_reduction.md)
expresses (4) as the complete zero mode and the alias terms with
coefficient \(+N^2\). Deforming only the unaliased coordinate
in each one-index alias gives 72 alias currents, controlled by eight
single-height and four double-height families together with the
already completed mixed faces and corners. The exhaustive
alias author and replay in Section 5 establish the twelve defects below
\(-1/2000\). The exact reduction therefore bounds their sum
by \(\exp N(B_\nu-1/4000)\), after one common color, half-grid
and polynomial tolerance.

The [completed zero-mode theorem](research_mixed_terminal_three_zero_mode_completion.md)
supplies the independent-target upper bound and the exact nonzero
coefficient in (6). Its powers are
\(N^2\cdot N^{-2}\cdot(2\pi/N)\): residue coefficient,
literal source symbol, and two-dimensional Gaussian integral.
At \(y=A\), every alias is exponentially smaller. This proves
(5)--(6) without replacing any inner error by an outer absolute
bound. Both parities are included. \(\square\)

## 2. An exact disjoint partition of the lower transform half

Define the literal outer half by
\[
 \mathcal L_N(w,X)=
 \sum_{0\le i\le\lfloor N/2\rfloor}
       \frac{X^{-i}p_i(X)}{P_i}\mathcal U_{0,N}(w,r^i).
\tag{7}
\]
It is important to remove its whole coherent end sector first.
Choose \(0<\delta<.001\) within the cutoff of
[the terminal end-tail theorem](research_mixed_terminal_transform_tails.md).
Its Lemma 2 bounds the positive **outer-row** majorant, with the
entire cap at each row, and explicitly bounds the two ends separately.
Thus the entire sum with \(i/N\le\delta\) in (7) has the
strict allocated loss \(1/50\). No restriction of its Newton
indices is made or inferred.

For the remaining outer rows \(\delta<i/N\le1/2\), use the
exact double sum (2). Put \(u_0=1/200\), and choose
\(0<\epsilon_0<1/10\) as in Lemma 2 of
[the Newton exterior-strip theorem](research_mixed_terminal_three_newton_exterior_strips.md).
Write \(u_1=1/2-\epsilon_0\). First remove the two sectors
\[
                    l/N\le u_0,\qquad l/N\ge u_1.
\tag{8}
\]
The low-Newton theorem, upper-Newton theorem, and the positive
near-half extension bound these sectors by positive double-sum
majorants. They therefore permit restriction to the remaining
outer rows and the exact support \(i+l<N\). Each retains
allocated loss \(1/100\). This restriction is justified by
positivity, not by cancellation of the full cap.

All remaining rows have \(u_0<l/N<u_1\). Partition them using
the actual half-grid cuts:

| Transform indices | Newton indices | Input controlling this exact sector |
|---|---|---|
| \(a_N<i/N<b_N\) | \(c_N^-<l/N<c_N^+\) | Central rectangle (4) |
| \(\delta<i/N<a_N\) | \(c_N^-<l/N<c_N^+\) | Left central-Newton strip |
| \(a_N<i/N<b_N\) | \(u_0<l/N<c_N^-\) or \(c_N^+<l/N<u_1\) | Newton exterior strips |
| \(\delta<i/N<a_N\) | \(u_0<l/N<c_N^-\) or \(c_N^+<l/N<u_1\) | Left real corner regions |
| \(b_N<i/N\le1/2\) | \(u_0<l/N<u_1\) | Upper-cut column described below |

No physical index equals a half-grid cut, so the displayed regions
are disjoint and exhaustive. For sufficiently large \(N\), their
ordering is \(\delta<a_N<b_N\) and
\(u_0<c_N^-<c_N^+<u_1\). On all five middle regions the physical
triangle is automatic, since \(i/N\le1/2\) and \(l/N<u_1<1/2\).

The [left-strip theorem](research_mixed_terminal_three_left_strip.md)
controls the second row once the two Newton single-alias comparisons
at zero other height have passed. Proposition 3 of the Newton
exterior-strip theorem controls the third row using the two transform
single-alias comparisons at zero other height. Both sets are included
in the full alias certificate. Proposition 4 of that theorem controls
the fourth row unconditionally by its positive real-corner majorant.
Their explicit \(O(1/N)\) extensions match the inward cuts, rather
than leaving small strips between the exact lattice partition and
the limiting rectangles. Each noncentral row of this table retains
loss \(1/4000\).

The last row deserves separate attention. It contains the physical
\(i=N/2\) row when \(N\) is even; it must not be silently
omitted by an inward upper cut.

**Lemma 2 (the upper-cut column).** The last row of the table has
allocated upper rate at most \(B_\nu-1/4000\), using only the
completed mixed/corner comparisons and the two Newton single-alias
comparisons with transform height zero.

*Proof.* Every such real \(t=i/N\) is within \(1/N\) of
\(1/2\). For \(c_N^-<l/N<c_N^+\), use one exact residue
identity in \(u\), retaining the physical \(i\)-sum. Deform
the \(u\) zero mode to its actual height. At the anchor
\(t=1/2\), its horizontal segment is the completed flattened
transform face. Its vertical joins reduce by height convexity to
that face and the completed real-real corners. The alias horizontal
segments are the two zero-other-height Newton single families at
\(t=1/2\); the vertical aliases reduce to these and the same
corners, with their exact half-grid penalties.

For the lower and upper middle Newton bands, keep both indices real.
Transport \(u\) to \(.1\) or \(.4\) by Lemma 1 of the
Newton exterior-strip theorem, then compare the real \(t\) to
\(1/2\). The anchor values are completed real-real corners.
All these bands are fixed regular compact sets because (8) was
already removed. The phase error from the real transform displacement
and the inward Newton cuts is uniformly \(O(N^{-1})\).
Thus the same fixed color neighborhood and source estimates leave
the stated finite gap. This argument introduces no transform
residue, no new target root, and no missing even-level row.
\(\square\)

## 3. The full lower-half coefficient

**Theorem 3.** The
literal half (7) has the same original nonzero packet as (6):
\[
 \mathcal L_N(-2,e^{-2\pi ia_*})=
 \frac{2\pi}{N}\,
 \frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
 e^{N\mathcal P_0(a_*)}(1+O(N^{-1})).
\tag{9}
\]
It has the independent-plateau allocated upper bound (5), with
\(\mathcal R_N\) replaced by \(\mathcal L_N\). Its ordinary
color germ is holomorphic, and for every fixed \(j\ge0\),
\[
 \left.\partial_w^j\mathcal L_N(w,e^{-2\pi ia_*})\right|_{w=-2}
 =2\pi N^{j-1}\,
  \frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
  \left(-\frac{\tan\pi u_*}{4\pi}\right)^j
  e^{N\mathcal P_0(a_*)}(1+O(N^{-1})).
\tag{10}
\]
The coefficient of every fixed ordinary jet is nonzero.

*Proof.* The partition above expresses (7) exactly as (4) plus a
fixed finite list of discarded sectors. The lower end tail is bounded
with its complete Newton sum; every later restriction of a low, high
or near-half Newton majorant is positive. All remaining strips have
their literal contour or positive-row bounds, including Lemma 2.
After reserving a common smaller color disk, their sum is bounded
by \(\exp N(B_\nu-1/8000)\) for large \(N\). The finite
number of sectors and their polynomial factors are paid once; no
error proportional to a word length is introduced.

At the actual target these sectors are exponentially smaller than
the nonzero central Gaussian. The uniform holomorphic color packet
of the central rectangle and Cauchy's formula transfer it, with
its relative error, to (7). The ordinary-color marginal is the
original \(-\tan(\pi u_*)/(4\pi)\); it is nonzero on the
selected endpoint range. This proves (9)--(10) and the independent
target upper bound. Both level parities and physical zeros are
retained in the exact decomposition. \(\square\)

## 4. Extending the retained packet through the proved right band

The [right-band theorem](research_mixed_terminal_three_right_band.md)
uses the exact external product and only a Newton-index contour.
It proves, using the same two zero-other-height Newton aliases,
that the band \(1/2\le i/N\le59/100\), with every permitted
Newton index, has a strict supporting-plane loss. Its proof bounds
each entire coherent outer row before summing. We may therefore
restrict it to \(1/2<i/N\le59/100\) to avoid counting the
even-level \(i=N/2\) row twice. This is a restriction in the
outer physical index, not an arbitrary truncation of an inner
coherent Newton sum.

**Corollary 4.** Define
\[
 \mathcal L_N^{.59}(w,X)=
 \sum_{0\le i\le\lfloor59N/100\rfloor}
       \frac{X^{-i}p_i(X)}{P_i}\mathcal U_{0,N}(w,r^i).
\tag{11}
\]
Then (9)--(10) and the independent-plateau allocated upper bound
hold with \(\mathcal L_N\) replaced by \(\mathcal L_N^{.59}\).

Indeed the difference between (11) and (7) is the disjoint suppressed
right band just described. The alias gap \(1/2000\) permits
its finite loss \(1/4000\), with all original colors, parities
and fixed ordinary jets. It is exponentially smaller at the actual
reference, so it changes neither the coefficient nor the relative
error of the retained packet. No holomorphic primitive is continued
across the possible divisor \(a+t=1\): the right-band input
keeps that external product literal and uses its zero-safe integrated
rate.

## 5. Certificate evidence and the remaining right triangle

The completed alias author is
[attempt01](../repro/results/research-mixed-terminal-three-aliases-attempt01.json),
SHA-256
`fc04d56f297524fc252dd0e0f131db11000d7490ec77a3b5300811cebb8e41cf`.
It contains 40,164 accepted jobs, one leaf each, all 3,347 original
own-three root contexts, and no reference refinement or new root
proposal. The [independent 320-bit saved replay](../repro/results/research-mixed-terminal-three-aliases-replay.json)
has SHA-256
`3b2b017023020d8ea2dce6ff7e5a429f87a0871a339467a2f0734454af4523f5`.
It revalidated every saved job and all 3,347 original root contexts,
with no target or root proposals and no refinements. Its completed
trees, rational targets and family definitions agree exactly with
the author. The input hash, all 60 current dependencies, and the
proof/driver bindings agree. Every outward upper is strictly below
\(-1/2000\); displayed approximate margins are not used here.

This note concerns the exact rectangular sum and the retained outer
indices through \(.59\). The original terms with \(i/N>.59\),
except independently suppressed sectors, remain outside its
conclusion. The result does not assert the full terminal
transform's leading coefficient, ordinary-knot noncancellation, or
stability for arbitrary short fillings. A nonzero lower-half packet
or its extension (11) cannot by itself rule out cancellation with
the surviving right triangle.
