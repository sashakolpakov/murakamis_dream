# A signed contour bound for the one-wall ordinary block

Private written proof, 10 November 2026. When the first retained height
is nonpositive, the wrapped part of an own-three conditional sum has a
regular one-wall interpolation whose phase decreases at every upward
height. Its complete finite contour is bounded by its two real wall
rates, with an arbitrary prescribed tolerance. This is a bound for the
signed block, not for its sum of absolute rows.

The original period multiplier is retained. Small wall collars are
estimated before any contour change, and all remaining main, alias and
vertical terms are kept at fixed finite heights. Applied to the adopted
endpoint calibrations, the result completes the early first33 pair at
every actual negative first height. It does not assert a new first43
endpoint calibration or a whole-word asymptotic.

## 1. Literal rows and the one-wall source

Fix the compact parameter ranges
\[
 a=x+ic,\quad b=z+id,\qquad
 1/10\le x\le11/50\le z\le9/20,\qquad
 -27/250\le c\le0,\quad-13/200\le d\le17/250.
\tag{1}
\]
The nonpositive first-height restriction is essential below. The exact
identities hold beyond (1), but their asserted estimates do not.
Put \(q=e^{-2\pi i/N}\), \(P_j=(q;q)_j\),
\(p_j(X)=(qX;q)_j\), \(X=e^{-2\pi ia}\),
\(Y=e^{-2\pi ib}\). Retain the own-three rows
\[
 R_{j,N}(a,b)=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^2},
                    \qquad0\le j<N.
\tag{2}
\]
Let \(G_N\) be the original normalized Gamma product in the
[joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md),
Section 1. Its marked factorial and reciprocal are explicitly
\[
 \Pi_N(w)=G_N(Nw)
       \exp\!\left\{\frac{\pi i}{2}[N(w-w^2)-w]\right\},
 \qquad E_N(w)=\frac1{\Pi_N(w)}\quad(0<\Re w<1),
\]
with the original continuations specified there. The exact recurrence gives
\[
 \Pi_N(w+1)=(1-e^{-2\pi iNw})\Pi_N(w).
\tag{3}
\]
This follows by multiplying its \(N\) one-index recurrences; no new
periodic normalization is chosen. The original interpolation is
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+b)
                          E_N(a)E_N(b)E_N(s)^2.
\tag{4}
\]
It satisfies \(T_N(j/N)=R_{j,N}\).

On the open one-wall strip
\[
                         1-z<\Re s<1-x
\tag{5}
\]
define the regular function
\[
 F_N(s)=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+b-1)
                          E_N(a)E_N(b)E_N(s)^2.
\tag{6}
\]
Every real part of the factorial arguments in (6) belongs to
\((0,1)\). In particular \(\Re(s+a)>1/2\),
\(0<\Re(s+b-1)<1/2\), and \(\Re s>1/2\).
This remains true at every finite imaginary height. Thus (6) is
holomorphic and nonzero on (5), with the original regular-strip marks.
Equations (3)--(4) give the undivided identity
\[
 T_N(s)=(1-Y^N e^{-2\pi iNs})F_N(s),\qquad
 R_{j,N}=(1-Y^N)F_N(j/N)
                       \quad(1-z<j/N<1-x).
\tag{7}
\]
The second equality uses the physical index only after the first
equality has retained its two Fourier terms. In particular
\(Y^N=1\) makes this entire strict wrapped block vanish exactly.
No division by \(1-Y^N\) is used, including at that locus.

Use the original primitive \(g\), with
\(g'(w)=\operatorname{Log}(1-e^{-2\pi iw})\) on
\(0<\Re w<1\), and define
\[
 Q(s;a,b)=g(s+a)+g(s+b-1)-2g(s)-g(a)-g(b)+2\pi ias.
\tag{8}
\]
On every fixed compact subset of (5) and every fixed bounded height
interval, the original factorial expansion gives
\[
                 |F_N(s)|\le C N^A e^{N\Re Q(s;a,b)}.
\tag{9}
\]
It also gives its holomorphic symbol, but no lower bound or nonzero
coefficient is needed here. All estimates below use only (9).

## 2. The exact all-height argument inequality

Write \(s=\sigma+iy\), \(v=1-\sigma\),
\(A=2\pi x\), \(V=2\pi v\), and \(R=e^{2\pi y}\).
Thus \(0<A<V<\pi\). For \(R>0\) and \(0<V<\pi\), put
\[
                  \theta(R,V)=-\arg(1-Re^{iV}).
\tag{10}
\]
The argument is the continuous one in \((-\pi,0)\). It is exactly
the original logarithmic argument for a regular real coordinate above
one half. The elementary identities are
\[
 \partial_V\theta(R,V)=
       \frac{R\cos V-R^2}{1-2R\cos V+R^2},\qquad
 \partial_R\theta(R,V)=
       \frac{\sin V}{1-2R\cos V+R^2}>0,
\tag{11}
\]
\[
 \theta(R,V)=\pi-V-\theta(R^{-1},V),\qquad
 0<\theta(R,V)\le(\pi-V)/2\quad(0<R\le1).
\tag{12}
\]
At \(R=1\), the last inequality is equality.

Set \(I(\sigma,y)=\Im Q_s(\sigma+iy;a,b)\).
The first shifted logarithm has argument
\(-\theta(e^{2\pi c}R,V-A)\). Since \(c\le0\), its
argument is at least \(-\theta(R,V-A)\).
The second shifted real coordinate is \(z-v\in(0,1/2)\),
so its original logarithmic argument is positive at every height,
regardless of the sign of \(d\). Consequently
\[
               I(\sigma,y)>
              A+2\theta(R,V)-\theta(R,V-A)>0.
\tag{13}
\]
Here is a proof of the final strict sign covering every radius.
For \(0<R\le1\), (11) gives the stronger identity
\[
 \partial_V\theta+\frac12=
       \frac{1-R^2}{2(1-2R\cos V+R^2)}\ge0.
\]
Integration from \(V-A\) to \(V\) implies
\(\theta(R,V-A)\le\theta(R,V)+A/2\), so the expression in
(13) is at least \(A/2+\theta(R,V)>\pi/10\).
For \(R\ge1\), put \(\rho=R^{-1}\le1\). By (12) that
same expression is
\[
 \pi-V-2\theta(\rho,V)+\theta(\rho,V-A)
                       \ge\theta(\rho,V-A)>0.
\tag{14}
\]
These are the original individual arguments; no argument of their
product has been reset.

There is also the upper bound needed below the real line. If
\(y\le0\), then \(R\le1\), the first argument is nonpositive,
the second is less than \(\pi(1-2z+2v)\), and
\(2\theta(R,V)\le\pi-V\). Hence
\[
                  I(\sigma,y)<2\pi(1+x-z)<2\pi.
\tag{15}
\]
This last strict inequality uses \(x<z\), which is automatic
when (5) is nonempty.

Fix any positive collar width \(\varepsilon\), and restrict to
\[
                 x+\varepsilon\le v\le z-\varepsilon.
\tag{16}
\]
The lower expression in (13) has a positive minimum on this compact
parameter set with \(R\in[0,\infty]\) compactified. At the two
radial ends its limits are \(A\) and \(\pi-V\), respectively;
both are bounded away from zero. Thus there is a constant
\(\delta_+(\varepsilon)>0\) such that
\[
 I\ge\delta_+(\varepsilon)\quad(y\in\mathbb R),\qquad
 2\pi-I\ge4\pi\varepsilon\quad(y\le0).
\tag{17}
\]
The second inequality follows directly from (15) and
\(z-x\ge2\varepsilon\). Since
\(\partial_y\Re Q=-I\), these imply
\[
 \Re Q(\sigma+iy)\le\Re Q(\sigma)-\delta_+y
                                                  \quad(y\ge0),
\tag{18}
\]
\[
 \Re Q(\sigma+iy)+2\pi y
           \le\Re Q(\sigma)+4\pi\varepsilon y
                                                  \quad(y\le0).
\tag{19}
\]
The compactification was used only for an elementary argument
function, not for a finite-level factorial asymptotic at infinity.

## 3. Matching the original continuous row rate

Let \(J(s)=\int_0^s\log(2\sin\pi t)\,dt\) for real
\(0\le s\le1\), and retain the full continuous rate of (2):
\[
 E_0(s;a,b)=
 \int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt+
 \int_0^s\log|1-e^{-2\pi i(b+t)}|\,dt
                          -2J(s)-2\pi cs.
\tag{20}
\]
All integrable zeros are retained. On the real part of (5),
\[
                E_0(\sigma;a,b)=\Re Q(\sigma;a,b)+2\pi d_+.
\tag{21}
\]
To check its constant, the second shifted integral traverses exactly
one positive wall, while the first traverses none. The real integral
of its periodic logarithm over one full period is
\[
 \int_0^1\log|1-e^{2\pi d-2\pi it}|\,dt=2\pi d_+.
\tag{22}
\]
For \(d<0\), expand the absolutely convergent logarithmic Fourier
series and integrate its nonconstant terms. For \(d>0\), extract
the radius and apply the same argument to its reciprocal. Continuity
at the integrable zero proves the result for \(d=0\). Integrating
the original regular-strip derivative in (8), with its two boundary
limits at real parts zero and one, now gives (21). Thus the exact
peripheral bound
\[
                         |1-Y^N|\le2e^{2\pi Nd_+}
\tag{23}
\]
restores precisely the original continuous rate, rather than an
additional uncharged boundary action.

The function (20) is jointly continuous on the compact real-index and
parameter domain, including its walls. One direct justification is to
truncate the logarithmic singularities: their integrals over a moving
interval of length \(\delta\) are uniformly
\(O(\delta(1+|\log\delta|))\). This is also the zero-safe
regularization in the original finite-product bound. That bound gives,
for every \(\tau>0\), uniformly in all physical rows,
\[
 |R_{j,N}(a,b)|\le C_\tau N^{A_\tau}
                            e^{N(E_0(j/N;a,b)+\tau)}.
\tag{24}
\]
No finite half-row, wall row or last row is divided out.

## 4. Every finite contour term and the signed block estimate

Define
\[
 B(a,b)=\max\{E_0(1-z;a,b),E_0(1-x;a,b)\},
\quad
 \mathcal W_N(a,b)=
       \sum_{\substack{0\le j<N\\1-z<j/N<1-x}}R_{j,N}(a,b).
\tag{25}
\]

**Theorem 1.** For every prescribed \(\tau>0\), uniformly on (1)
and at both level parities,
\[
                 |\mathcal W_N(a,b)|
                   \le C_\tau N^{A_\tau}e^{N(B(a,b)+\tau)}.
\tag{26}
\]
The conclusion concerns the literal signed block in (25).

*Proof.* Choose a small fixed \(\varepsilon>0\), using the uniform
continuity in Section 3, so that a row within \(3\varepsilon\)
of either of the two walls has rate at most \(B+\tau/8\).
If \(z-x\le6\varepsilon\), every row in (25) is in one of
these collars, and (24) proves the result directly.

Otherwise choose half-grid cuts \(\alpha_N,\beta_N\) within
\(1/(2N)\) of
\[
                     1-z+2\varepsilon,\qquad1-x-2\varepsilon,
\tag{27}
\]
respectively. For sufficiently large \(N\), they enclose a nonempty
core, lie strictly in (5), and satisfy (16), as do all real points
between them. The other wrapped rows lie within the already paid
\(3\varepsilon\) collars. Their exact rounded index sets are kept.
In particular both real cut rates are at most \(B+\tau/8\).

Take fixed finite heights \(-L<0<H<H+1\), to be selected below.
For \(\Delta F_N(y)=F_N(\beta_N+iy)-F_N(\alpha_N+iy)\),
the exact cotangent residue identity, followed by movement of its
zero mode to height \(H\), is
\[
\begin{split}
 \sum_{\alpha_N<j/N<\beta_N}F_N(j/N)
 ={}&N\int_{\alpha_N}^{\beta_N}F_N(u+iH)\,du\\
 &+N\int_{\alpha_N}^{\beta_N}
       F_N(u-iL)\frac{e^{-2\pi iN(u-iL)}}
                           {1-e^{-2\pi iN(u-iL)}}\,du\\
 &+N\int_{\alpha_N}^{\beta_N}
       F_N(u+i(H+1))\frac{e^{2\pi iN(u+i(H+1))}}
                           {1-e^{2\pi iN(u+i(H+1))}}\,du\\
 &+iN\int_{-L}^{H+1}
       \left\{\frac1{1+e^{2\pi Ny}}-\mathbf1_{\{y<H\}}\right\}
                          \Delta F_N(y)\,dy.
\end{split}
\tag{28}
\]
For the orientation, the bottom zero mode equals the upper zero mode
minus \(i\int\Delta F_N\) over their joining heights. This gives
the minus sign before the indicator in (28). It is the same exact
vertical regrouping as the original identity, with a positive rather
than negative chosen main height. Its derivation uses no sign estimate.
All factors are holomorphic on the intervening fixed rectangle by (6).
The original outside index density is \(+N\).

The vertical multiplier in braces has the bounds
\[
 \left|\frac1{1+e^{2\pi Ny}}-\mathbf1_{\{y<H\}}\right|
 \le
 \begin{cases}
  e^{2\pi Ny},&y<0,\\
  1,&0\le y<H,\\
  e^{-2\pi Ny},&y>H.
 \end{cases}
\tag{29}
\]
Equations (18)--(19) show that every vertical piece in (28) has
upper rate at most its own real-cut value \(\Re Q(\alpha_N)\)
or \(\Re Q(\beta_N)\). This keeps both cut signs and every
join, including the segment from zero to the positive main height.

For completeness, the horizontal parts can be paid without a limiting
contour. On the compact domain of the core, let
\[
 K=\max\left(0,\sup_{a,b,u}\{E_0(u;a,b)-B(a,b)\}\right)<\infty.
\tag{30}
\]
Choose fixed \(H,L\) so that
\(\delta_+H>K+1\) and \(4\pi\varepsilon L>K+1\).
The main line in (28), by (18) and (21), has rate after (23) at
most \(B-1\). The lower alias has the same bound by (19),
after its exact penalty \(2\pi L\). The upper alias is still
smaller by (18) and its penalty \(2\pi(H+1)\).
The residual horizontal denominators are bounded away from zero for
large \(N\). The heights may depend on the prescribed tolerance,
but are fixed before the level and uniform over (1).

Apply (9) on this single compact factorial rectangle. Multiply the
whole identity (28) by \(1-Y^N\), as required by (7), and use
(21)--(23). The vertical terms have rate at most \(B+\tau/8\);
the three horizontal terms have a fixed stronger reserve. Their finite
lengths and original \(N\) factors cost only a polynomial. Adding
the collar rows from (24), and assigning all finite-product tolerances
within \(\tau\), proves (26). If \(Y^N=1\), the core equality
in (7) gives zero directly; the proof never divides by it.
\(\square\)

No artificial wall pole is crossed: (28) stays inside the strip (5).
In particular neither Fourier term in the first equality of (7) is
continued by itself into the neighboring chamber. The physical sum is
not replaced by an entire homogeneous period or by a different
conditional polynomial.

## 5. Complete first33 consequence at all actual first heights

Return to the actual first33 references and the original complete cap
\(U_{0,N}(w,X)\). Use the unchanged allocated plane
\[
\begin{split}
 \Gamma(z)={}&\Re L_0(a_*)+\Re\phi_{00}(a_*,b_*)
 +\Re\partial_b\phi_{00}(a_*,b_*)(z-b_0)
                                  -\kappa(z-b_0)^2,\\
 \kappa={}&1/2500000,\qquad
 \gamma_* =\kappa(a_0-11/50)^2>0.
\end{split}
\tag{31}
\]
The actual first-three image has \(a_0>.278\). For every original
regular cap profile and each true-end profile, the unwrapped theorem
calibrates \(E_0(1-z)\) below \(\Gamma-2\gamma_*\).
Lemma 1 and the reflected late-tail inequality of the outer-high-block
theorem calibrate \(E_0(1-x)\) by the same bound. These statements
retain the complete fixed-height cap, its cuts and both aliases. At
\(c\le0\) its additional positive-height right-row allowance is zero.

Multiply (26) by that complete cap envelope. Its two endpoint rates
are calibrated separately, so their maximum is calibrated as well.
The unwrapped physical rows with \(1/2\le j/N\le1-z\) and the
late reflected rows with \(1-x\le j/N<1\) retain their old
absolute estimates. Together these three sets contain every index
\(\lceil N/2\rceil\le j<N\), including any physical wall rows.
Thus the entire signed high block satisfies
\[
 |U_{0,N}(w,X)|\left|\sum_{j=\lceil N/2\rceil}^{N-1}R_{j,N}(a,b)\right|
       \le C_\tau N^{A_\tau}
                      e^{N\{\Gamma(z)-\gamma_*+\tau\}}
                           \qquad(c\le0).
\tag{32}
\]
It is essential that (32), unlike the earlier outer-block bounds,
does not replace the wrapped signed sum by its sum of moduli.

**Corollary 2.** For every actual positive three/four open word of
length at least three beginning with \(3,3\), at its original fixed
heights and for \(x\in[.1,.22]\), \(z\in[.22,.45]\),
\[
 |U_{0,N}(w,X)C_{0,N}(X,Y)|
       \le C_\tau N^{A_\tau}
                       e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{33}
\]
There is no remaining sign restriction on the first or second retained
height, or on the private critical height of the ordinary factor.
Both level parities and all original finite rows are retained.

*Proof.* For \(c\le0\), the joint low theorem pays
\(0\le j\le\lfloor3N/20\rfloor\). The complete nonpositive-
private-height central theorem or the positive-private-height first33
theorem pays
\(\lfloor3N/20\rfloor<j<\lceil N/2\rceil\), according to the
actual private-height sign. They include every alias and cut of that
block with the same allocation (31). Equation (32) pays the remainder.
For \(c\ge0\), the adopted nonnegative-first-height theorem already
proves (33). Choose the total source tolerance within \(\tau\).

The cap bounds first hold on the whole real ordinary-color interval,
after dropping only their favorable angular losses and retaining their
separate true-end bounds. Nothing in (28) depends on that color. The
cap has degree less than \(N\), so interval polynomial continuation
gives a sufficiently small fixed complex neighborhood of \(w=-2\)
at any prescribed additional rate cost. Intersect it with the fixed
neighborhoods of the low and central sources. Cauchy's formula gives
every fixed color derivative with the same upper exponent on smaller
neighborhoods. No Fourier factor or possibly zero finite row is divided
out. The original external scalar and following factors are unchanged.
\(\square\)

The first43 conditional rows have the same own-three algebra (2), so
Theorem 1 also applies to their negative first heights whenever they
lie in (1). Turning it into a first43 pair theorem still requires its
own complete-cap calibration of the two wall rates, with the full
first type-four diagonal weight. That is not supplied by Corollary 2.
No selected first alternative, height-changing outer join, whole-word
asymptotic, closed-knot theorem or short-filling stability is inferred.

## Direct source versions

| Source | SHA-256 |
|---|---|
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| research_exact_vertical_current_regrouping.md | fbc3bfe6015cfbdfffb4c11d07738fd435b1ad1a871b6be29cee9c2ed5542ad7 |
| research_mixed_three_fourier_conditional_endpoint_current.md | 3875ef15c77bd4327eb496f8bc14cbc80ef88e3faef59ce3d9cad4a9db6cb96c |
| research_mixed_early_three_outer_high_blocks.md | ece4f34c6dbe288649ff45b54acb705e50b0dc0d63926263ff26eb644d694c3f |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_three_positive_private_central.md | d7f54fc0a20c5ccce15b028d16dbcaee2ef0eefbea70795089da097c9730635e |
| research_mixed_early_three_nonnegative_first_height.md | ffa42bf7baeafde8598b1ca87645e4a4069bd3381d80446db70e13d6cffeb5e8 |

The whole proof and directly used source implications were read back.
Only written analysis and source-hash metadata checks were used. No
mathematical numerical evaluation, saved-value arithmetic, import,
compilation, test or edit to a frozen source was performed.
