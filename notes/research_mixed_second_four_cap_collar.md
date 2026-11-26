# A calibrated first-collar comparison when the second type is four

Research deduction, 5 November 2026. This extends the calibrated first
collar comparison to prefixes \((3,4)\) and \((4,4)\), retaining the
coherent cap, the full first Fourier weight, the second Fourier
halfweight and every physical selection. The analytic input is a
one-sided extension of the cubic cotangent-root chamber. The focused
author check passed 31 exact/scalar comparisons and 405 current
bindings. No new conditional root or parameter cover is required.

## 1. Actual references and the literal allocation

Write the first type as \(3+\alpha\), \(\alpha\in\{0,1\}\),
and the actual first two retained references as
\(r_1=a+ih,r_2=b+ic\). The
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give
\[
\begin{array}{c|cc}
 \alpha&a&h\\\hline
 0&(.278,.391)&(-.072,.021)\\
 1&(.246,.350)&(-.108,-.020).
\end{array}                                                    \tag{1}
\]
The second type-four reference satisfies the common union
\[
                 .24<b<.363,\qquad -.102<c<-.001.             \tag{2}
\]
For length two this follows from the private-right rectangle
\((.333,.363)+i(-.051,-.019)\). Otherwise its ordinary block
has external legs in the original typed disks. Proposition 1 of
[the universal image theorem](research_mixed_cyclic_critical_height_bounds.md)
applies to the entire such input product and gives the disk centered
at \(.30-.052i\) with radius \(.060\), together with the
height bounds in (2). This use does not require a five-vertex
interior buffer or a periodic repetition of the open word.

Let \(\phi_{01}\) be the original conditional phase with its second
Fourier halfweight and no first halfweight, in the notation of
[the acute-gradient theorem](research_mixed_acute_gradient_height_transfer.md).
Set
\[
 \Phi_\alpha=\mathcal T_\alpha(r_1,-2)
                      +\phi_{01}(r_1,r_2)-\alpha g(r_1),
 \quad M_\alpha=\Re\Phi_\alpha,
 \quad P=\partial_2\phi_{01}(r_1,r_2).                      \tag{3}
\]
This equals \((\mathcal T_\alpha-\alpha g/2)+\phi_{\alpha1}\).
The exact first critical equation cancels the first tangent, so the
pair plane is
\[
                         M_\alpha+\Re[P(z_2-r_2)].           \tag{4}
\]

At the physical first collar let \(X=e^{-2\pi ix}\),
\(0\le x\le\rho\), \(Y=e^{-2\pi iz_2}\), and
\(z_2=b+ik\). The full allocated modulus is
\[
 \mathcal B_N=
 |U_{\alpha,N}(w,X)C_{1,N}(X,Y)
                d_N(X)^\alpha X^{-N\sigma_1}|
       |d_N(Y)Y^{-N\sigma_2}|^{1/2},                       \tag{5}
\]
where \(\sigma_1=0\) if \(\alpha=0\), and otherwise
\(\sigma_1\in\{0,1\}\). Its physical second heights obey
\[
 \sigma_2=0:\quad c\le k\le0,
 \qquad
 \sigma_2=1:\quad0\le k\le H=7/500.                        \tag{6}
\]
These are the actual open graph heights: Section 1 of
[the open boundary reduction](research_mixed_open_boundary_comparison_reduction.md)
uses the row-dependent hybrid formula, with a missing neighbor's
cutoff equal to one. Its selected base height is exactly \(H\),
as in equation (4) of
[the graph construction](research_mixed_split_cutoff_hybrid_contour.md).
Every own taper and neighboring cutoff belongs to \([0,1]\).
Thus (6) uses no cyclic reference-height bound for an endpoint.
The first selected monomial has modulus one because \(x\) is real.

## 2. A one-sided cubic chamber

**Lemma 1.** Suppose
\[
 P_0=p+i\xi,\quad Q_0=q+i\zeta,\qquad
 p,q>0,\quad -1<\xi<2/3,\quad0\le\zeta<1.                 \tag{7}
\]
Then
\[
 F_1(S)=(S+i)(S+P_0)(S+Q_0)-2i(P_0-i)(Q_0+i)              \tag{8}
\]
has exactly one root in \(\Re S>0,|\Im S|<1\). It is simple,
has the original zero logarithmic lift, and is holomorphic on a
neighborhood of each compact parameter set in (7). The original
allocated phase obeys \(-\Re\phi_{\eta1}''>0\) there for
\(\eta=0,1\).

*Proof.* On \(S=iv\), \(-1\le v\le1\), write
\[
 \Im F_1(iv)=(v-1)pq+E(\xi,\zeta,v),\qquad
 E=2(\xi-1)(\zeta+1)-(v+1)(\xi+v)(\zeta+v).              \tag{9}
\]
The coefficient of \(\xi\) is
\((1-v)(\zeta+v+2)\ge0\). The coefficient of \(\zeta\)
is at most its value at \(\xi=2/3\), namely
\[
 -v^2-5v/3-4/3=-(v+5/6)^2-23/36<0.
\]
Consequently
\[
 E\le E(2/3,0,v)=-2/3-v(v+1)(v+2/3)\le-2/9.             \tag{10}
\]
For the last inequality, the product is nonnegative on
\([-1,-2/3]\cup[0,1]\); on \([-2/3,0]\), its negative
is at most \((2/3)\cdot1\cdot(2/3)=4/9\).
This excludes the entire imaginary side, including its corners.

On \(S=u+i\), \(u>0\), the exact boundary identity in
[the closed-root theorem](research_mixed_closed_cotangent_roots.md),
equation (8), would force \(\Im P_0<-1\). On \(S=u-i\),
its equation (9) would require
\[
 \left(1+\frac{u}{P_0-i}\right)
            \frac{Q_0+u-i}{Q_0+i}=\frac{2i}{u}.            \tag{11}
\]
The first factor has argument in \((0,\pi/2)\), because
\(p>0\) and \(\xi<1\). The second has argument in
\((-\pi,0)\), because \(q>0\) and \(-1<\zeta<1\).
Their product's continuous argument belongs to \((-\pi,\pi/2)\)
and cannot equal \(\pi/2\) modulo \(2\pi\).
Thus both complete horizontal sides are excluded.

Continue from \(\xi=\zeta=0\) along their straight scaling
path. The polynomial is monic, its coefficients stay bounded on
each compact path, and the strip boundary is free of roots. The
original real-parameter theorem supplies exactly one root counted
with multiplicity. Thus the continued root is unique and simple.
All inverse-cotangent and original logarithmic arguments remain
in the same regular strips; the original logarithmic equation is a
continuous multiple of \(2\pi i\) and starts at zero. Local
holomorphic continuations therefore glue with that zero lift.

Finally, write \(S=u+iv\). For either outer cotangent
\(p+i\xi\), the exact triangle determinant is
\[
 \frac{(u+p)^2-(pv-u\xi)^2}{(u+p)^2+(v+\xi)^2}>0,        \tag{12}
\]
because \(u,p>0\), \(|v|<1\), \(|\xi|<1\). The analogous
formula holds for \(q+i\zeta\). Their diagonal entries are
positive; the remaining factorial terms have nonnegative real
diagonal coefficients. The original complex Schur identity then
proves the asserted negative real Hessian. This is the same
triangle proof as in the closed-root theorem, with its actual
determinant hypothesis \(|\xi|,|\zeta|<1\) retained.
\(\square\)

Every point of the full vertical segment
\((a,b)+i\lambda(h,c)\), \(0\le\lambda\le1\), belongs
to this chamber. Indeed, (1)--(2) give
\[
 |\Im\cot\pi r_1|<.61<2/3,\qquad
                   0\le\Im\cot\pi(b+i\lambda c)<.61.    \tag{13}
\]
The fixed upper bounds for the first type three, first type four,
and second type four are respectively
\[
 \frac{\sinh(.144\pi)}{\cosh(.144\pi)-\cos(.556\pi)}<.37,
 \quad
 \frac{\sinh(.216\pi)}{\cosh(.216\pi)-\cos(.492\pi)}<.61,
 \quad
 \frac{\sinh(.204\pi)}{\cosh(.204\pi)-\cos(.48\pi)}<.61.
                                                               \tag{14}
\]
The first bound covers both signs of its height. Cotangent imaginary
modulus decreases in the real coordinate on these intervals and
increases with absolute height. The latter follows from
\(\cos(.492\pi)\cosh(.216\pi)<1\) and
\(\cos(.48\pi)\cosh(.204\pi)<1\); in the first-three box
the cosine is negative. All outer cotangent real parts are positive.
At the actual point uniqueness identifies the root with the
already proved original conditional root. No new finite-source
packet is inferred elsewhere in the enlarged chamber.

## 3. A real phase floor from existing original-root values

Let \(f_{01}=\Re\phi_{01}\) on real arguments. It is jointly
concave. The original-root phase values already saved in
[the seam-run theorem](research_mixed_seam_run_connector_lower.md)
give the following lower bounds:
\[
\begin{array}{c|c@{\qquad}c|c}
 (a,b)& f_{01}>(\text{bound})&(a,b)&f_{01}>(\text{bound})\\\hline
 (.30,.27)&.805&(.10,.27)&.597\\
 (.30,.10)&.721&(.30,.33)&.789\\
 (.10,.33)&.564&(.30,.50)&.664\\
 (.39,.27)&.822&(.39,.10)&.725\\
 (.50,.27)&.804&(.39,.33)&.812\\
 (.50,.33)&.799&(.39,.50)&.703.
\end{array}                                                    \tag{15}
\]
No new root is evaluated. The four corners of
\([.246,.391]\times[.24,.363]\) are convex combinations
of these saved points as follows. The point order in each row
matches the coefficient order:

| Corner | Three saved points | Coefficients |
|---|---|---|
| \((.246,.24)\) | \((.30,.27),(.10,.27),(.30,.10)\) | \(941/1700,27/100,3/17\) |
| \((.246,.363)\) | \((.30,.33),(.10,.33),(.30,.50)\) | \(911/1700,27/100,33/170\) |
| \((.391,.24)\) | \((.39,.27),(.39,.10),(.50,.27)\) | \(1523/1870,3/17,1/110\) |
| \((.391,.363)\) | \((.39,.33),(.50,.33),(.39,.50)\) | \(149/187,1/110,33/170\) |

Each weighted bound from (15) is strictly larger than \(7/10\).
Concavity first at these corners and then across their rectangle proves
\[
                         f_{01}(a,b)>7/10.                   \tag{16}
\]

By Lemma 1, vertical convexity holds along the entire path in
(13). At the real starting point, the calibrated acute gradients give
\[
 0<\Im\phi_{01,a}<\pi/2,\qquad
 -\tfrac\pi2-\tfrac\pi2(1/2-b)<\Im\phi_{01,b}<0.
\]
Their affine lower support therefore yields
\[
 \Re\phi_{01}(r_1,r_2)
   \ge f_{01}(a,b)-\frac\pi2\{h_++(3/2-b)(-c)\}.        \tag{17}
\]
The [complete-cap theorem](research_mixed_complete_first_cap_packet.md)
gives \(\Re\mathcal T_\alpha>1\) on these actual references.
For \(\alpha=1\), the actual first height is negative and
the radial dilogarithm formula gives \(-\Re g(r_1)>0\).
Thus
\[
 M_\alpha>1.7-\frac\pi2\{h_++1.26\cdot.102\}.            \tag{18}
\]
Use \(h_+<.021\) for \(\alpha=0\), and \(h_+=0\)
for \(\alpha=1\).

At the actual complex reference, the original gradient identity is
\[
 P=\log_{\rm R}(S+Q_0)-\log_{\rm R}(S+i)-\tfrac12g'(r_2).
                                                               \tag{19}
\]
The ratio's imaginary numerator is
\(u(\zeta-1)-q(v+1)<0\). Both logarithms are in the
right half-plane, so their imaginary difference is negative.
Also \(0<\Im g'(b+ic)<\pi(1/2-b)\), since \(c<0\),
\(0<b<1/2\), and the original factor \(1-e^{-2\pi i(b+ic)}\)
lies above the real axis. Hence \(\Im P<0\). Every height
in (6) satisfies \(k\ge c\), so its surviving tangent is favorable:
\[
                    \Re[P(z_2-r_2)]=-(k-c)\Im P\ge0.     \tag{20}
\]

## 4. The full selected finite source

The [cap seam theorem](research_mixed_cap_seam_source_bounds.md)
bounds the coherent cap in (5) by rate
\(b_\alpha+\Delta_\rho\), where
\(b_0=.808,b_1=.866\), with an arbitrary small color tolerance.
This retains its original endpoint sum and is not a private-row
triangle replacement near the critical cap.

Equations (5)--(6) and (17) of
[the boundary-strip theorem](research_mixed_boundary_strip_bounds.md)
give a whole-row source bound for the next kernel. For unselected
\(k\le0\), the actual \(d_N(Y)\) lies inside its unit circle
and has rate at most \(1/6\). For selected \(k\ge0\), the
degree \(N-1\) of the same polynomial gives
\[
 \sup_{|Y|=R}|d_N(Y)Y^{-N}|
   \le R^{-1}\sup_{|Y|=1}|d_N(Y)|\le N^A e^{N/6},
 \qquad R\ge1.                                            \tag{21}
\]
Thus the **halfweight** in (5) costs at most \(1/12\) for
both selections, without dividing by \(d_N\). The kernel product
bound retains every original row, with positive-height cost at most
\(2\pi H u=.028\pi u\). The fixed scalar bound already proved
in that theorem, Section 5, is
\[
                         M_1(.028\pi)+1/12<.57.           \tag{22}
\]
For the first real collar its numerator costs one
\(\Delta_\rho\); the cap costs the other. When \(\alpha=1\),
the full first \(d_N(X)\) has the vanishing collar upper rate
\(\omega(\rho)\to0\) from the same theorem's equation (8),
including its forcing term. Consequently (5) has rate at most
\[
 b_\alpha+.57+2\Delta_\rho+\alpha\omega(\rho)+\eta,       \tag{23}
\]
where \(\eta\) is one total finite-source and ordinary-color
tolerance. Negative second heights as low as \(-.102\) cause
no extra cost in this derivation: the all-row polynomial bound is
uniform inside the unit circle. No narrow cyclic height restriction
is silently enlarged.

The fixed phase reserves following from (18), (20), and (23) are
\[
\begin{split}
 1.7-.808-.57-\tfrac\pi2(.021+1.26\cdot.102)&>.087>3/50,\\
 1.7-.866-.57-\tfrac\pi2(1.26\cdot.102)&>.062>3/50.
\end{split}                                                   \tag{24}
\]
Choose a fixed \(0<\rho\le.001\) sufficiently small that
\(2\Delta_\rho+\omega(\rho)<1/200\), and spend
\(\eta<1/200\) once.

**Theorem 2.** For every fixed open word beginning \((3,4)\)
or \((4,4)\), a fixed collar and ordinary-color neighborhood
exist on which, uniformly for every selection in (5)--(6),
\[
 \mathcal B_N\le C N^A
    \exp N\{M_\alpha+\Re[P(z_2-r_2)]-1/20\}.            \tag{25}
\]
Both level parities and every fixed ordinary derivative of the cap
are included, on a smaller color neighborhood for derivatives.
The strict margin also permits a small fixed change of the second
real coordinate, with a decreased gap and the same reference tangent.
This is a calibrated first-pair comparison only. Its second tangent,
the remaining boundary completion, and the other endpoint remain
part of the full open-source problem.

## Reproduction

The focused checker
[`check_mixed_second_four_cap_collar.py`](../experiments/check_mixed_second_four_cap_collar.py)
verifies the exact cubic barriers, triangle identity, rational convex
combinations, current source bindings, and fixed outward scalar bounds.
It neither proposes nor recomputes a conditional root or a parameter
cell:

```sh
python3 experiments/check_mixed_second_four_cap_collar.py --precision 256
```

The canonical record is
[`research-mixed-second-four-cap-collar.json`](../repro/results/research-mixed-second-four-cap-collar.json).
