# A complete lower outer-cap alias at fixed height

Research deduction, 8 November 2026. The original lower horizontal
cap alias at private height minus one has a small absolute upper
rate, uniformly at every real ordinary color. The proof keeps the
complete endpoint sum. In particular its auxiliary upper half,
which survives at nonphysical indices, is not removed.

This is a separate complete-current estimate. Long vertical sides,
the unweighted main path, and a whole-cap asymptotic do not follow.
No numerical evaluation or frozen-note edit is used.

## 1. Original finite row and lower-half primitive

Use exactly the source of
[the tall upper-alias theorem](research_mixed_cap_tall_upper_alias.md).
Its carrier cancellation is an exact identity:
\[
\mathscr A_N(e,a,w)=
\sum_{l=0}^{N-1}\frac{e_l(w)}{S_l}\,
 e^{i\pi Ne(l/N-a)}
\frac{G_N(N(a+e))}
     {G_N(Na)G_N(N(e-l/N))}.
                                                               \tag{1}
\]
Take
\[
\frac12\le a\le\frac7{10},\qquad e=E-i,\qquad
\frac18\le E\le\frac{49}{100}.
                                                               \tag{2}
\]
As before, bounded \(O(N^{-1})\) changes of the private real
endpoints are permitted. The exact finite expression has no
physical termination imposed at complex \(e\).

The canonical lower primitive is
\(J_-(z)=\overline{J_+(\bar z)}\), with the additive constant and
branches in
[the full half-plane factorial theorem](research_factorial_uniform_halfplane_continuation.md).
Its full factorial and reciprocal estimates apply on every
compact lower-half-plane set, irrespective of real part.
Conjugating the analytic bound in the upper-alias proof gives
\[
\left|\Re J_-(x-i)-\pi(x-\tfrac12)\right|
 \le\frac{\rho}{2\pi(1-\rho)},\qquad
\rho=e^{-2\pi}.
                                                               \tag{3}
\]
Thus, with \(u=l/N\),
\[
\Re J_-(a+E-i)-\Re J_-(E-u-i)
\le\pi(a+u)+\epsilon_0,\qquad
\epsilon_0=\frac{\rho}{\pi(1-\rho)}<\frac1{297}.
                                                               \tag{4}
\]
The elementary bound on \(\epsilon_0\) is the same finite
exponential-series witness as in the upper-alias theorem.
No primitive or finite sum is evaluated.

The carrier in (1) now has modulus
\(\exp\{\pi N(u-a)\}\). Its sign is the opposite of the
upper-line sign. Combining it with (4) gives \(2\pi u\),
not \(2\pi a\), in the resulting row rate.

## 2. The original all-real-color Newton envelope

For \(w=-2\cos\theta\), retain the zero-safe physical envelope
of
[the Newton color tube theorem, equations (4)--(7) and (11)](research_mixed_newton_color_tubes.md):
\[
 |e_l(w)|\le C N^B e^{N V_\theta(l/N)},\qquad
 S_l^{-1}\le C N^B e^{-NJ(l/N)}.
                                                               \tag{5}
\]
The precise comparisons needed here are
\[
\begin{array}{ll}
V_\theta(u)\le V_0(u)
 =-2J(1/2-u)-2J(u),&0\le u\le1/2,\\
V_\theta(u)\le0,&1/2\le u\le1.
\end{array}                                                     \tag{6}
\]
The second follows from that theorem's
\(V_\theta(1-u)=-V_\theta(u)\) and
\(V_\theta(u)\ge0\) below one half. It is not a pointwise
inequality between Newton polynomial values at different
colors. The finite polynomial factors and the ordinary
derivative statement include every exact zero and both parities.

After the lower cotangent remainder contributes its exact
penalty \(2\pi\), (1), (4), and (5) give the literal row
upper rate
\[
V_\theta(u)-J(u)-J(a)-2\pi(1-u)+\epsilon_0.
                                                               \tag{7}
\]
For \(u\le1/2\), the elementary bound \(-J\le1/6\) yields
\[
V_\theta(u)-J(u)-2\pi(1-u)
\le\frac56-\pi<0.
                                                               \tag{8}
\]
For \(u\ge1/2\), both \(V_\theta(u)\le0\) and \(J(u)\ge0\),
while \(-2\pi(1-u)\le0\). Therefore the same expression is
nonpositive on that whole half, including its limiting endpoint
at \(u=1\). Finally \(J(a)\ge0\) on (2).

Every row in the complete auxiliary sum consequently has
weighted rate at most \(\epsilon_0<1/297\). This is the step
that retains the full high-index source; the crude estimate
\(|e_l(w)|\le4^l/S_l^2\) would not establish it.

## 3. Complete lower-current theorem

Let \(c_N,d_N\) be the original half-grid cuts of any retained
private interval in the range (2). Denote its original lower
horizontal alias on \([c_N,d_N]-i\), with its original
orientation, by \(\mathcal H_N^-\). The exact cotangent
remainder has modulus at most
\[
\frac{2e^{-2\pi N}}{1-e^{-2\pi N}}.
                                                               \tag{9}
\]
The residue density remains \(+N\), and the constant mode is
kept separate. The \(N\) auxiliary terms, bounded contour
length, density and uniform factorial errors cost only
powers of \(N\).

**Theorem.** For every \(\tau>0\), along both level parities,
\[
\sup_{\substack{1/2\le a\le7/10\\-2\le w\le2}}
|\mathcal H_N^-(a,w)|
\le C_\tau N^{B_\tau}e^{N(1/297+\tau)}.
                                                               \tag{10}
\]
All fixed ordinary derivatives at every real color have the
same rate with polynomial costs.

The actual original cap action satisfies
\(\Re\mathcal T(a)>41/60\), by the wall-action and
wrapped-row theorems cited in the upper-alias proof.
Since \(1/297<1/8\), the raw reserve in (10) is greater
than \(41/60-1/8=67/120>1/2\).
One common tolerance and polynomial absorption therefore
give a finite own-action gap \(1/2\) for this whole current.

The tube estimate in the cited Newton theorem gives a rate
increase at most \(\sqrt{\delta}\) for ordinary-color
perturbations of radius \(\delta\); it does not divide by
a zero factor. The upper and lower factorial arguments
stay in fixed regular half-plane compacts under small
complex incoming perturbations. Hold the base cut endpoints
and contour fixed before making these perturbations.
The strict reserve then persists on fixed neighborhoods.
Normalize by the original holomorphic \(e^{N\mathcal T(a,w)}\)
near complete color and apply Cauchy's formula on smaller
neighborhoods. This gives every fixed mixed normalized jet,
for example with finite gap \(1/3\).

Equations (1)--(10) retain the complete original finite
source and all cyclotomic factors through the canonical
factorial theorem. They prove neither bounds on the
intervening long side currents nor a bound on a central
private path. Both of those tasks remain separate when
this line is used in an outer contour.
