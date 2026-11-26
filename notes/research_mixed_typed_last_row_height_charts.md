# Exact height charts for typed last-row support

Research design, 5 November 2026. This replaces the masked circle/polar
charts of the [28-case design](research_mixed_typed_last_row_support_design.md)
by exact height charts for the same
[typed domains](research_mixed_typed_last_row_envelopes.md).
The coverage and target-envelope reductions below are analytic.
A uniform last-row sign is not asserted. No new driver or full run is
part of this design.

## 1. The two typed domains

Put
\[
\begin{gathered}
m_3=7/20,\quad d_3=-1/100,\quad \rho_3=83/1000,\qquad
m_4=3/10,\quad d_4=-13/250,\quad \rho_4=3/50,\\
\ell_3=-9/125,\quad u_3=17/250,\qquad
\ell_4=-27/250,\quad u_4=-1/1000,\\
r_n(h)=\sqrt{\rho_n^2-(h-d_n)^2},\\
K_3=\{|z-(m_3+id_3)|\le\rho_3,\ \ell_3\le\Im z\le u_3,\
                         \Re z-3\Im z\le76/125\},\\
K_4=\{|z-(m_4+id_4)|\le\rho_4,\ \ell_4\le\Im z\le u_4\}.
\end{gathered}
\tag{1}
\]
The same actual-role inclusions \(O_3\cup A_3\subset K_3\) and
\(O_4\cup A_4=K_4\) remain in force. Private endpoint legs are not
new external inputs to an ordinary conditional factor.

Write
\[
h_*=-49/625+\sqrt{16906}/10000,\qquad
x_*=233/625+3\sqrt{16906}/10000,\qquad
h_4^\circ=-51/500=-.102 .
\tag{2}
\]
The typed-domain proof gives \(\ell_3<h_*<-13/200\). The slanted
line meets the right circle at \(x_*+ih_*\); its other circle
intersection is below the permitted height strip.

All radii in (1) are uniformly positive:
\[
r_3(h)\ge\frac{\sqrt{805}}{1000}>\frac1{40},\qquad
r_4(h)\ge\frac{\sqrt{29}}{250}>\frac1{50},\qquad
r_n'(h)=-\frac{h-d_n}{r_n(h)},\quad |r_n'(h)|<3 .
\tag{3}
\]
Indeed the largest absolute offsets from the circle centers are
\(78/1000\) and \(56/1000\); their squared ratios to the displayed
minimum radii are strictly below \(9\). Thus no circle extremum
or square-root singularity lies in these height intervals.

## 2. Four exact interior charts

For each row of the following table take \(u,v\in[0,1]\), put
\(h=a+(b-a)u\), and define
\[
 Z(u,v)=L(h)+vW(h)+ih,\qquad W(h)=U(h)-L(h).
\tag{4}
\]

| Chart | Height interval \([a,b]\) | \(L(h)\) | \(U(h)\) |
|---|---|---|---|
| \(D_3^-\) | \([\ell_3,h_*]\) | \(m_3-r_3(h)\) | \(76/125+3h\) |
| \(D_3^+\) | \([h_*,u_3]\) | \(m_3-r_3(h)\) | \(m_3+r_3(h)\) |
| \(D_4^-\) | \([\ell_4,h_4^\circ]\) | \(m_4-r_4(h)\) | \(m_4+r_4(h)\) |
| \(D_4^+\) | \([h_4^\circ,u_4]\) | \(m_4-r_4(h)\) | \(m_4+r_4(h)\) |

These charts cover precisely \(K_3\) and \(K_4\), respectively.
For the lower type-three interval the slanted line cuts the right
circle side; for the upper interval it is inactive. The left circle
side is retained throughout. At \(h=h_*\), the two upper endpoints
coincide exactly. The type-four split is an internal horizontal
partition, not an additional boundary of \(K_4\).

The full-width charts have \(W=2r_n\). On \(D_3^-\),
\[
W(h)=129/500+3h+r_3(h)>67/1000.
\tag{5}
\]
Here \(129/500+3h\ge21/500\), and (3) gives the strict inequality.
In particular every chart has strictly positive width. Its exact
derivatives are
\[
Z_u=(b-a)\{L'(h)+vW'(h)+i\},\qquad Z_v=W(h).
\tag{6}
\]
For a full-width chart the real expression in braces is
\((2v-1)r_n'(h)\). For \(D_3^-\) it is
\(3v+(v-1)r_3'(h)\). The full-width expression has absolute value
below \(3\); the lower type-three expression has absolute value at
most \(3\), with equality on its slanted side \(v=1\).
Consequently \(|Z_u|\le\sqrt{10}(b-a)\), while the absolute real
Jacobian determinant is exactly \((b-a)W(h)>0\).

Every parameter point is admitted by its defining formula. Closed
endpoints and common horizontal interfaces are retained. There is no
polar collapse at a center and no outside region to discard by masks.
Interval boxes enclosing a chart may still require subdivision for
the original root or deficit test; that numerical uncertainty is not
a geometric exclusion.

## 3. Exact boundary curves

For an interval \([a,b]\), always use \(h=a+(b-a)t\),
\(0\le t\le1\). The boundary lists are:

| Domain and curve | Formula | Height interval |
|---|---|---|
| \(K_3:L_3\) | \(m_3-r_3(h)+ih\) | \([\ell_3,u_3]\) |
| \(K_3:R_3\) | \(m_3+r_3(h)+ih\) | \([h_*,u_3]\) |
| \(K_3:S_3\) | \(76/125+3h+ih\) | \([\ell_3,h_*]\) |
| \(K_4:L_4\) | \(m_4-r_4(h)+ih\) | \([\ell_4,u_4]\) |
| \(K_4:R_4\) | \(m_4+r_4(h)+ih\) | \([\ell_4,u_4]\) |

Add the two horizontal boundary chords \(H_n^-,H_n^+\) for each
domain. Their real endpoints are \(L(\ell_n),U(\ell_n)\) at the
lower height and \(L(u_n),U(u_n)\) at the upper height, using
the appropriate row of (4). Each horizontal chord is parameterized
linearly from left to right.

There are therefore **five** curves for \(K_3\),
\((L_3,R_3,H_3^-,H_3^+,S_3)\), and **four** for \(K_4\),
\((L_4,R_4,H_4^-,H_4^+)\). No curved portion is masked.
At the finite intersections the closed descriptions may overlap;
no endpoint is omitted.

The exact derivatives are
\[
\beta_\pm'(t)=(b-a)\{\pm r_n'(h)+i\},\qquad
\beta_{S_3}'(t)=(h_*-\ell_3)(3+i),\qquad
\beta_H'(t)=U(h)-L(h).
\tag{7}
\]
The fixed height in the last formula is the relevant endpoint height.
Equations (3) and (7) bound all boundary derivatives.

## 4. Seventy-two three-parameter charts

For each own flag \(\epsilon=0,1\), combine one boundary curve
in one external slot with one of the two interior charts in the
other slot. The parameters are the boundary parameter \(t\) and
the other-input height/width parameters \(u,v\).

The local two-leg input/root swap preserves the homotyped products
and exchanges the two conditional orientations. Since both orientations
are compulsory, only boundary slot zero is needed on \(K_n\times K_n\).
This uses the original local-map symmetry, not a reversal of an open word.
The mixed product retains both boundary slots.

| External product | Boundary choices times other-input charts | Per own flag |
|---|---|---:|
| \(K_3\times K_3\) | Slot 0: \(5\cdot2\) | 10 |
| \(K_3\times K_4\) | Slot 0: \(5\cdot2\); slot 1: \(4\cdot2\) | 18 |
| \(K_4\times K_4\) | Slot 0: \(4\cdot2\) | 8 |

Both own flags give \(2(10+18+8)=72\) charts. This is a finer
parameterization of the same ordinary boundary covered by the previous
28 masked generators; it is not an enlarged source or reference domain.
The [interior-reference exclusion lemma](research_mixed_horizontal_tail_reference_boundary.md)
continues to justify ordinary-boundary reduction on these clipped products.
It does not reduce this three-real-parameter problem to two boundary circles.

## 5. One acceptance rule for both own types

For one orientation, let \((s;A,B)\) be the original conditional root,
external first argument, and other output of the same coupled map.
Let \(\eta\) be the first external type-four flag. The own flag
\(\epsilon\) determines both the index equation and the second allocation:
\[
\begin{split}
Q_\epsilon(s;A,B)&=g(s+A)+g(s+B)-(2+\epsilon)g(s)+2\pi iAs,\\
\phi(Z)&=Q_\epsilon(s;A,B)-(1+\eta/2)g(A)-(1+\epsilon/2)g(B),\\
P&=\phi',\qquad Z=(A,B)=U+iH .
\end{split}
\tag{8}
\]
All functions and logarithms use the original primitive and lift.
The type of the other external input chooses its parameter domain;
it never replaces the own flag in (8).

For \(X\in I^2\), \(I=[11/50,9/20]\), retain all four carriers:
\[
\begin{split}
R_{vw}(X,H)&=-2\pi vH_1+2\pi wH_2
       -\frac\eta2G_{H_1}(X_1)-\frac\epsilon2G_{H_2}(X_2),\\
D_{vw}(Z,X)&=R_{vw}(X,H)-\Re\phi(Z)
             -\Re P\cdot(X-U)+\kappa_0\|X-U\|^2,\\
&G_h(x)=\Re g(x+ih),\qquad \kappa_0=1/2500000 .
\end{split}
\tag{9}
\]
For an unweighted target coordinate its maximum is attained at an
endpoint of \(I\). For a weighted target coordinate, the derivative is
\[
b_i(x;Z)=-\tfrac12\Re g'(x+iH_i)-\Re P_i
                           +2\kappa_0(x-U_i),\qquad
\partial_xb_i<-\frac{9\pi}{140}+2\kappa_0<-1/5 .
\tag{10}
\]
The strict curvature follows from the same full-plateau factorial
bound as the previous design. It covers both weighted coordinates
when \(\epsilon=1\). Separability makes each unique clipped optimizer
independent of the other target and of the carrier.

Including both orientations, the number of carrier/endpoint envelopes
per parameter box is unchanged:

| Own flag | External \((3,3)\) | External \((3,4)\) | External \((4,4)\) |
|---|---:|---:|---:|
| \(0\) | 32 | 24 | 16 |
| \(1\) | 16 | 12 | 8 |

For each weighted coordinate choose a rational trial \(q_i\in I\).
If the whole-box slope enclosure is
\(b_i(q_i;Z)\in[\beta_i^-,\beta_i^+]\), its true optimizer lies in
\[
J_i=I\cap[q_i+5\min(0,\beta_i^-),\
                 q_i+5\max(0,\beta_i^+)].
\tag{11}
\]
This includes clipped endpoints. Compute these enclosures once per
orientation and parameter box, then reuse them across carriers and
unweighted endpoint choices.

The exact complex Schur Hessian is
\[
\begin{split}
\sigma&=g''(s+A)+g''(s+B)-(2+\epsilon)g''(s),\\
\omega&=(g''(s+A)+2\pi i,\ g''(s+B)),\\
\mathcal H_{ij}
&=\delta_{ij}\{g''(s+Z_i)-(1+\tau_i/2)g''(Z_i)\}
                         -\omega_i\omega_j/\sigma,
\qquad(\tau_1,\tau_2)=(\eta,\epsilon).
\end{split}
\tag{12}
\]
The original-root validation must retain the nonzero denominator.
The exact reference gradients, with \(d=X-U\), are
\[
\begin{split}
P^{\rm row}&=(2\pi iv-\eta g'(X_1+iH_1)/2,\
                   -2\pi iw-\epsilon g'(X_2+iH_2)/2),\\
D_U&=-\Re(\mathcal H d)-2\kappa_0d,\qquad
D_H=\Im(P-P^{\rm row}+\mathcal H d).
\end{split}
\tag{13}
\]
Contract (13) with the original coupled response and the exact chart
derivatives (6)--(7), evaluating each weighted target throughout its
whole-box optimizer enclosure (11).

The envelope theorem for a unique clipped maximizer removes its
derivative, including at clipping transitions. At the parameter midpoint
only, add the exact one-sided \(1/5\)-concavity gain for each weighted
coordinate. The full box upper bound is the midpoint trial deficit plus
these midpoint-only gains plus the parameter mean-value error from (13).
This is precisely the previously proved target-envelope rule, now with
zero, one, or two weighted coordinates. Fixed-trial derivatives cannot
replace the optimizer-enclosure derivatives in this rule.

No new root, independent output leg, carrier omission, or branch choice
is introduced by the change of input coordinates.

## 6. Exact reuse of the completed chart

The [completed low-cap record](../repro/diagnostics/2026-11-05-typed-last-row-low-cap/completion.md)
is exactly the chart with own flag zero, mixed external types, boundary
\(S_3\) in slot zero, and other-input chart \(D_4^-\).
Its boundary parameter \(t\), height parameter \(u\), and width parameter
\(v\) agree identically with (4) and (7). In particular
\[
S_3(t)=(1-t)(49/125-9i/125)+t(x_*+ih_*),\qquad
D_4^-(u,v)=3/10+(2v-1)r_4(h)+ih,\quad
h=-27/250+(3/500)u .
\tag{14}
\]
The phase, flags, target square, \(\kappa_0\), and all four carriers
also agree exactly. Thus its 402 accepted cells and original rational
witnesses can be imported unchanged; no coordinate conversion or new
proposal is needed. Its saved 320-bit replay already proves
\(D_{vw}<-1/1000000\) on that entire chart.

The other **71** charts remain outside this completed record.
Their signs are the remaining sufficient typed-domain comparison.
This design does not assert those signs or promote this auxiliary
comparison to a finite-source or actual-word noncancellation theorem.

