# The calibrated upper physical triangle on the ordinary left taper

Research deduction, 7 November 2026. Retaining the actual first-cap
private height repairs the endpoint calibration of
[the earlier upper-triangle transport](research_mixed_three_four_upper_triangle_left_transport.md).
The entire original terminal sector \(i/N\ge1/2\), multiplied by
the complete first cap, now has a strict geometric gap on the early
incoming taper. No partial Newton estimate or numerical evaluation
is used.

## 1. The unchanged physical majorant and new cap envelope

Keep the original ordinary \((3,4)\) source and reference. Write
\[
 a=x+ih,\quad h=c(x-.1)/.12,\quad
 -.072<c<.021,\quad .1\le x\le.22,\quad \lambda=-c/.12,
 \qquad M=\Re\{T_0(a_*)+P_1(a_*)\}.                       \tag{1}
\]
The original upper-transform entropy theorem, with every private
and Newton index retained, gives the complete physical-sector
majorant with upper rate
\[
 G(a)=M_4(1/2)+Q_a(1/2),\qquad
 Q_a(1/2)=\Re\{g(a+1/2)-g(a)+\pi ia\}.                   \tag{2}
\]
More precisely its supported row rate at transform coordinate \(t\)
is at most \(G(a)-\log(80/63)(t-1/2)\).
This is the same literal positive majorant as in the earlier
transport theorem; all physical zeros, both parities and ordinary
color variables are unchanged.

Use the complete first-cap envelope from
[the early complex-profile theorem](research_mixed_cap_early_taper_complex_profiles.md)
at its original private height \(k_*\in(-.019,.037)\).
Its aliases are below the main by (17) of
[the private-height transport](research_mixed_three_four_private_height_left_transport.md).
The remaining regular profiles have \(e=u+ik\), with
\(.27\le u\le.49\) and \(k=k_*\) or \(0\).
The separate true-end alternative remains
\[
                    E_{\rm end}(h)=3/5+2\pi h_++(\log4)/100.
                                                               \tag{3}
\]

## 2. Every surviving cap alternative has positive coupled slope

**Lemma 1.** On (1), every regular profile just described satisfies
\[
 \frac d{dx}\{\Re\Psi_0(e,a)+Q_a(1/2)\}>\frac1{10}.
                                                               \tag{4}
\]
The same bound holds with \(E_{\rm end}(h)\) replacing
\(\Re\Psi_0(e,a)\).

*Regular profiles.* The exact derivative is
\[
 \Re\{(1-i\lambda)D\},\qquad
 D=g'(e+a)+g'(a+1/2)-2g'(a)+\pi i.                       \tag{5}
\]
The \(k\)-monotonicity and real-private endpoint argument in the
private-height theorem are independent of the second shift.
They reduce the lower bound to \(k=-.019\), \(u=.27,.49\).
Put \(r=e^{2\pi h}\); its original range and sign correlation are
\(3/5<r<23/20\), \(-7/40<\lambda<3/5\),
with \(r\le1\) for \(\lambda\ge0\) and \(r\ge1\) for
\(\lambda\le0\).

At fixed \(r\), the real part of (5) decreases with \(x\).
Indeed the own cotangent is greater than one, the first shifted
real cotangent is less than one, and the second shifted real
cotangent is negative on \(a_R+1/2\in[.6,.72]\).
Its lower bound is therefore at \(x=.22\), without resetting the
coefficient/radius correlation in the imaginary part.

The first squared modulus ratio is greater than \(13/10\), by
the exact quadratic witnesses in the private-height theorem.
For the second, use
\[
 -\cos(1.44\pi)=\sin(.06\pi)>9/50,\qquad
                    \cos(.44\pi)>9/50.
\]
The sine bound follows from \(157/50<\pi<22/7\) and the lower
sine polynomial. Its squared ratio is greater than
\[
       \frac{1+r^2+(9/25)r}{1+r^2-(9/25)r}
                 \ge\frac{197}{143}>\frac43.            \tag{6}
\]
The quotient increases up to \(r=1\), decreases afterward and
is invariant under reciprocation, so its minimum on the original
range is bounded by its value at \(r=3/5\).
Consequently
\[
             \Re D>\frac12\log(26/15)>11/41.             \tag{7}
\]
The last inequality is the first positive atanh term.

For the original real-private argument at \(k=0\), the rotated
ratio gives
\[
 \Im D_0\ge\pi(1/2-u)\quad(r\le1),\qquad
 \Im D_0\le\pi(1/2-u)\quad(r\ge1).
\]
Its lift remains valid since
\(2\pi x+\pi/2<\pi\).
Moving \(k\) from zero to \(-.019\) changes this imaginary part
by a number in \((-.019\pi,0)\) for \(u=.27\), and
\((0,.019\pi)\) for \(u=.49\).
Thus it is positive when \(\lambda\ge0\).
When \(\lambda\le0\), it is at most \(.23\pi\) in either
endpoint case. The greatest possible debit is therefore
\[
 (7/40)(23/100)\pi<253/2000.
\]
Together with (7), this gives
\(11/41-253/2000>1/10\), proving (4).

*True-index profile.* Let
\(D_{\rm half}=g'(a+1/2)-g'(a)+\pi i\).
Its real part is greater than
\(\tfrac12\log(4/3)>1/7\), by the same fixed-radius
comparison and (6).
If \(c\le0\), its imaginary part is at least \(\pi/2\)
and \(E_{\rm end}'=0\). If \(c\ge0\), its imaginary part
is at most \(\pi/2\), whereas \(E_{\rm end}'=-2\pi\lambda\).
Thus the imaginary contribution after including this endpoint
derivative is nonnegative in both cases. The conclusion at \(c=0\)
follows by continuity. This proves the second assertion. \(\square\)

## 3. Calibration at the original half-row and finite consequence

At \(x=.22\), all five actual-private-height cap profiles have their
completed bare upper plane \(B_U(.22)\). The true-end ceiling (3)
is also below it, by the explicit floor (9) of
[the moving-left-boundary proof](research_mixed_three_four_left_moving_boundary.md).
The original terminal raw-half comparison applies at exactly this
incoming target:
\[
 G(.22+ic)
 <\Re P_1(a_*)+p(.22-A)-\kappa_*(.22-A)^2-1/20000,
 \qquad p=\Re P_1'(a_*).
                                                               \tag{8}
\]
This is the original raw-half family, discharged by the completed
terminal source theorem; it is not a new finite-function comparison.
Adding \(B_U\) cancels the stationary incoming marginals.
Integrating Lemma 1 before maximizing the cap profiles now yields
\[
 \text{complete cap-envelope rate}+G(a)
       <M-\frac1{20000}-\frac{.22-x}{10}.                \tag{9}
\]
Inactive cap aliases remain bounded by the same expression.

**Theorem 2.** Let \(\mathcal V^{\rm upper}_{1,N}\) denote the
literal terminal physical triangle with transform index \(i/N\ge1/2\),
retaining its complete private and Newton sums. Its positive
majorant multiplied by the whole first cap satisfies
\[
 |U_{0,N}(w_L,e^{-2\pi ia})|\,
       \mathcal V^{\rm upper,abs}_{1,N}(w_R,e^{-2\pi ia})
       \le C N^B e^{N(M-1/40000)}
                         \quad(.1\le x\le.22).           \tag{10}
\]
It holds on sufficiently small fixed ordinary-color disks,
at both parities and after every fixed ordinary-color derivative.

The proof combines the original zero-safe physical majorant (2)
with the complete cap envelope and (9), then spends part of the
fixed reserve on source and color tolerances. Exact physical
support and the even half-row assignment are unchanged.
Ordinary-color holomorphic extension and fixed derivatives use
the same original polynomial-degree and Cauchy arguments as the
source theorems. The scalar \(\kappa_N^3N^2\) of the outer
ordinary contraction is not altered.

This is a calibrated complete physical sector. It does not prove
the lower transform region, the new low-\(t\) complex currents,
the far incoming half-circle, or the whole ordinary-knot conclusion.

