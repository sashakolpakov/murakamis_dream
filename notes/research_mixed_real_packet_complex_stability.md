# Complex-neighborhood stability of the complete real conditional packet

Research proof, 4 November 2026. This perturbs the literal finite
residue contour of the real-neighbor theorem. It does not continue
an unknown error term by holomorphy, and makes no claim on the
whole complex cotangent domain.

## 1. Statement for the original finite source

Use the marked factorial \(P_N\), its original regular-strip phase
\(g\), and the fixed canonical sum
\[
 \begin{split}
 {\cal L}_{\epsilon,N}(a,b)
 &=P_N(Na)P_N(Nb)
   \sum_{j=0}^{N-1}
   \frac{e^{2\pi iaj}(r^{Na+1};r)_j(r^{Nb+1};r)_j}
                          {(r;r)_j^{2+\epsilon}},\\
 Q_\epsilon(s;a,b)
 &=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
 \qquad r=e^{-2\pi i/N},\quad\epsilon\in\{0,1\}.
 \end{split}
 \tag{1}
\]
Every original row, including rows revived by moving a physical
neighbor off its grid, is part of (1).

**Theorem 1.** For every compact real \(K\subset(0,1/2]^2\) bounded
away from zero, there is an open complex neighborhood \(U\) of \(K\)
on which the original selected root and its action are holomorphic
and the complete source has the uniform expansion
\[
 {\cal L}_{\epsilon,N}(a,b)
 =N^{(1-\epsilon)/2}
   \frac{\sqrt{2\pi}\,A_\epsilon(s_*;a,b)}
        {\sqrt{-Q_{\epsilon,ss}(s_*;a,b)}}
      e^{NQ_\epsilon(s_*;a,b)}
                     \{1+O_U(N^{-1})\},
 \tag{2}
\]
where
\[
 A_\epsilon(s;a,b)=e^{i\pi(\epsilon s-a-b)/2}
 \frac{\sqrt{2\sin\pi(s+a)}\sqrt{2\sin\pi(s+b)}}
      {(\sqrt{2\sin\pi s})^{2+\epsilon}}.
 \tag{3}
\]
All branches are the original ones. After shrinking \(U\) with
compact closure, the coefficient is nonzero and bounded away from
zero. The normalized error and every fixed complex derivative
are \(O(N^{-1})\) on smaller neighborhoods. Both parities are included.

The neighborhood depends on \(K\). No uniform radius as a neighbor
tends to zero, prescribed taper-height width, or outer-word lower
bound is asserted.

## 2. Fixed real-reference contours and strict reserves

Fix \(p_0=(a_0,b_0)\in(0,1/2]^2\), and write
\(s_0=x_0+ih_0\), \(M_0=\Re Q_\epsilon(s_0;p_0)\).
The [closed-half-endpoint theorem](research_mixed_half_endpoint_conditional_packet.md),
Sections 1--3, proves a simple zero-lift root, strict local
coercivity, full-period horizontal and endpoint gaps, and a strict
alias reserve at this point, including either half endpoint.
The critical factorial arguments lie inside their regular strips.

Choose a fixed small \(d>0\), so the central segment
\([x_0-2d,x_0+2d]+ih_0\) and its shifted arguments are regular.
Choose a fixed small \(\tau>0\) and put
\[
 Y=|h_0|+\tau,\qquad l_N=-\frac1{2N},\qquad
 r_N=1-\frac1{2N}.
 \tag{4}
\]
Use the full rectangle with real sides \(l_N,r_N\) and heights
\(\pm Y\). Deform its zero mode to the selected side outside the
central segment: height \(-Y\) if \(h_0<0\), and \(+Y\) if
\(h_0\ge0\). Retain both central vertical joins and both midpoint
end joins.

The actual proofs of the
[lower packet](research_mixed_global_lower_conditional_packet.md)
and [all-real extension](research_mixed_all_real_conditional_packet.md)
give, for some \(\gamma>0\), a pointwise bound on every
complementary current:
\[
 |\text{original weighted row at }p_0|
       \le C N^B e^{N(M_0-4\gamma)}.
 \tag{5}
\]
These are both horizontal cotangent remainders, both halves of both
midpoint vertical remainders, the zero-mode exterior intervals and
joins, and the central regular portions outside a smaller critical
interval. The right midpoint bound comes from the exact period
multiplier. Bounded lengths and the residue scalar cost only
polynomial powers.

This is stronger input than the real asymptotic alone. Its proof
supplies the needed piecewise gaps: the whole-period maximum and
endpoint monotonicity control the exterior; the opposite horizontal
costs \(C\tau^2\), while its retained alias gains at least
\(2\pi(1-\Lambda)Y\), \(\Lambda<1\); exact midpoint moduli control
the vertical finite rows. The central annulus has a strict
quadratic gap. The minimum of this finite list gives (5).
At \(h_0=0\), the exterior height is \(Y=\tau>0\); only the central
regular segment touches the real axis.

## 3. Direct parameter bounds for every original current

The actual interpolated row is
\[
 T_N(s;a,b)=e^{2\pi iNa s}
     \frac{P_N(N(s+a))P_N(N(s+b))}
                    {P_N(Ns)^{2+\epsilon}}.
 \tag{6}
\]
For all sufficiently small complex \(p=(a,b)\) near \(p_0\), it
is jointly holomorphic inside the whole midpoint rectangle.
Indeed \(-1<\Re Ns<N\) keeps the denominator nonzero, and the
shifted numerator arguments have real parts greater than \(-1\),
where their Gamma products are holomorphic. Their zeros beyond
one period are retained. The recurrence identifies each value
at \(s=j/N\) with the corresponding term of (1), so exactly
\[
 {\cal L}_{\epsilon,N}(p)
       =\frac{N}{2i}\oint T_N(s;p)\cot(\pi Ns)\,ds .
 \tag{7}
\]
This retains all \(N\) rows for complex parameters.

On the fixed horizontal sides, the shifted arguments at \(p_0\)
have imaginary parts \(\pm Y\). Restrict
\(\|p-p_0\|_\infty<\delta_0<\tau/2\); they then stay in fixed
compact upper or lower half-planes. The calibrated
[half-plane factorial expansions](research_lower_half_factorial_continuation.md)
and their exact upper reflection give
\[
 P_N(Nz)=\sqrt N\,a_\pm(z)e^{Ng_\pm(z)}(1+O(N^{-1})).
 \tag{8}
\]
In particular the upper phase retains its nonperiodic multiplier.
On the left midpoint and the regular central joining pieces,
the shifted real arguments instead stay in a compact part of
\(0<\Re z<1\); use the original strip expansion through height zero.

All symbols are nonzero. Let \(G_1\) bound the derivatives of the
appropriate \(g_-,g_+\), or regular-strip \(g\), on slightly enlarged
compact sets, and let \(R_s\) bound \(|s|\). Division of the
literal factorial expansions gives
\[
 |T_N(s;p)|\le C e^{N L_0\delta}|T_N(s;p_0)|,\qquad
 L_0=2G_1+2\pi R_s,\quad \delta=\|p-p_0\|_\infty .
 \tag{9}
\]
The denominator is parameter-independent. Each numerator phase
increment costs \(G_1\delta\), and the original chirp costs
\(2\pi R_s\delta\). The bounded symbol ratios cost only \(C\).
The comparison segments stay in their same half-plane or regular
strip. This bounds the actual row, not a formally continued error.

The right midpoint can have numerator zeros at \(p_0\), so no
ratio to its value is used. With \(t=e^{2\pi Ny}>0\), the exact
period recurrence gives instead
\[
 \frac{T_N(r_N+iy;p)}{T_N(l_N+iy;p)}
 =e^{2\pi iNa}
    \frac{(1+t e^{-2\pi iNa})(1+t e^{-2\pi iNb})}
         {(1+t)^{2+\epsilon}}.
 \tag{10}
\]
The elementary bound
\(|1+t e^{-2\pi iNa}|\le(1+t)e^{2\pi N(\Im a)_+}\) implies
\[
 \begin{split}
 |T_N(r_N+iy;p)|
 &\le (1+t)^{-\epsilon}
 e^{2\pi N\{(-\Im a)_++(\Im b)_+\}}|T_N(l_N+iy;p)|\\
 &\le e^{4\pi N\delta}|T_N(l_N+iy;p)|.
 \end{split}
 \tag{11}
\]
Here \(a_0,b_0\) are real. The entire multiplier, including zeros
and their off-grid revival, remains. Both midpoint cotangent
kernels are equal by period one in \(s\). Thus (9)--(11) transfer
the original left vertical bounds to the right with rate cost
at most \((L_0+4\pi)\delta\). They also control the zero-mode
end joins. No false off-real inequality comparing right to left
with unit constant is used.

All other cotangent remainder factors are unchanged. Consequently
(5) persists with added rate \(L\delta\), where initially
\(L\ge L_0+4\pi\). Both horizontal aliases are retained; no
complex-parameter Schwarz identity is used to remove either one.

## 4. Move only the central saddle

The simple root has a holomorphic implicit extension \(s(p)\),
also at the half endpoints. Shrink its neighborhood so that
\[
 |s(p)-s_0|\le L_s\delta,\qquad -\Re Q_{\epsilon,ss}>c>0
 \tag{12}
\]
on a common small regular critical disk. The symbol (3) remains
holomorphic and nonzero. Explicit response and action derivatives are
\[
 s_a=-\frac{g''(s+a)+2\pi i}{Q_{ss}},\quad
 s_b=-\frac{g''(s+b)}{Q_{ss}},\quad
 (Q(s(p);p))_a=g'(s+a)+2\pi is,\quad
 (Q(s(p);p))_b=g'(s+b).
 \tag{13}
\]
Compact derivative suprema and \(c\) bound \(L_s\) and
\[
 |Q(s(p);p)-Q(s_0;p_0)|\le L_{\rm act}\delta .
 \tag{14}
\]

Keep all exterior contours fixed. Replace the central segment by
\(s(p)+[-d,d]\), joining its endpoints to \(s_0\pm2d\) inside
the regular disk. If \(L_s\delta<d/4\), the connectors stay near
the original central annulus. Their phase variation is bounded
by compact suprema of \(Q_a,Q_b,Q_s\), times \(\delta\) and
\(L_s\delta\). Increase \(L\) to include this cost.
They retain the gap in (5).

For example any positive radius small enough for the stated
regularity and curvature conditions, and satisfying
\[
 \delta<\tau/2,\qquad L_s\delta<d/4,\qquad
                    (L+L_{\rm act})\delta<\gamma,
 \tag{15}
\]
leaves every complementary current bounded by a polynomial times
\(\exp N(\Re Q(s(p);p)-3\gamma)\).
These constants are real-reference phase reserves and suprema of
explicit derivatives on specified regular compact sets. An outward
certificate may quantify them; an unproved error continuation
is not a premise.

The exact cotangent decomposition still has zero mode
\(+N\int T_N\,ds\), since it only requires holomorphy of the
complete row in the rectangle. Every remainder was just bounded.
The moving central interval has a uniform original factorial
expansion and a left-to-right Gaussian through its simple root.
The accretive square root, symbol and powers are unchanged:
\[
 N\cdot N^{-\epsilon/2}\cdot N^{-1/2}=N^{(1-\epsilon)/2}.
 \tag{16}
\]
This proves (2) on a polydisk about \(p_0\).

When \(h_0=0\), the exterior height remains \(+\tau\), independent
of the perturbed root's sign. Only the regular central segment
and its connectors move. Thus (15) gives a genuine neighborhood
across zero height, not two estimates with diverging constants.

## 5. Compact gluing, derivatives, and the literal kernel

Cover \(K\) by finitely many sufficiently small complex polydisks
centered at its real points. Choose them so their roots stay in
the original selected cotangent strip and all critical factorial
arguments stay regular. The roots glue. A nonempty intersection
of two such polydisks is connected and contains real points:
project a common point to its real part and, if needed, clip
each coordinate at \(1/2\), moving it closer to both centers.
There is a real open subset of the intersection inside
\((0,1/2]^2\). Both roots there equal the unique closed-quadrant
selected root. The holomorphic identity principle in each
coordinate proves agreement throughout the intersection.
The original phases, sine-root symbols and accretive Gaussian
branches agree as well.

Shrink the finite union while retaining \(K\) with compact closure
inside the charts. Taking the largest finite constants proves
uniform (2). Only now, after the literal contour estimates, apply
Cauchy's inequality to the holomorphic normalized relative error;
this gives every fixed derivative on a smaller neighborhood.
Intersect the two neighborhoods if both types are required.

The literal Laurent kernel obeys the exact identity
\[
 C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ib})
 =\frac{{\cal L}_{\epsilon,N}(a,b)}{P_N(Na)P_N(Nb)}.
 \tag{17}
\]
Its external arguments remain in the original regular strip.
Division therefore gives power \(N^{-(1+\epsilon)/2}\), phase
\(Q(s_*)-g(a)-g(b)\), and the original nonzero symbol. This is
an identity of fixed canonical functions, not only agreement
on their physical grid.

The theorem permits small nonzero complex heights over any fixed
real compact. It supplies neither a numerical width for a
prescribed graph nor its supporting-plane loss. The
[broad cotangent obstruction](research_mixed_complex_horizontal_obstruction.md)
does not conflict with it: (15) restricts the neighborhood using
the actual real-reference current gaps.

## 6. Reproduction

    python3 experiments/check_mixed_real_packet_complex_stability.py

The checker verifies the exact residue, complex midpoint multiplier,
its four sign cases, critical-response formulas and scalar powers,
and binds the real and half-plane source inputs. The neighborhood
construction is the analytic proof above, not finite sampling.
