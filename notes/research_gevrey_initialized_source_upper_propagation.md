# Subexponential upper bounds for the initialized source

Private written proof, 22 November 2026.

The frozen all-plus contour source has an exponentially accurate
optimally truncated initializer. Its continued stationary coefficients
have Gevrey-1 bounds on compact regular charts. Consequently a complex
upper bound with subexponential loss suffices to propagate its initialized
expansion. A fixed polynomial loss is unnecessary.

This concerns the same ordinary-polynomial contour representative,
including its original currents. No action-relative upper estimate is
proved below. The conclusion applies only when that remaining estimate
and the stated marked regular continuation are supplied.

## 1. The same frozen source and its coefficients

Fix the finite original same-index graph and a nonempty set \(I\) of
selected nonisolated vertices. Put \(m=|I|\). Retain every original edge
in \(E\), put \(e=|E|\), and count loops twice in vertex incidences.
Outside angles remain complete. In particular an edge with both
endpoints outside \(I\) retains its exact complete-kernel factor, its
wire \(x=1/4\), its wire Hessian \(8\pi\), and its normalization.
Fix real powers \(\mathbf b\) before taking \(N\) to infinity.

Choose a small positive seed as in the pattern-adapted initializer.
Freeze its full table of heights, cuts and oriented currents once.
For a fixed holomorphic charge curve \(\boldsymbol\chi:D\to\mathbb C^m\)
on a connected domain \(D\subset\mathbb C\), use exactly
\[
 G_N(s)=\mathfrak Z_{N,\mathbf+}
               (\mathbf b,\boldsymbol\chi(s);\mathbf0),\qquad
 \beta=\frac{3(m-e)}2.
 \tag{1}
\]
Assume that the curve maps a nonempty open subset of \(D\) into the
original complex seed neighborhood.
No height is reselected as \(s\) changes. The function \(G_N\) is
holomorphic, since the original finite rows and compact contour pieces
are entire in the charges.

Use the full independent variables \(p=(x_e,t_v)\), the original phase
\[
 \Phi_s(x,t)=\sum_{(e,v)}b_0(x_e,t_v)
       +\sum_{v\in I}\left(\frac{ib_vt_v^2}{4\pi}
                                      -i\chi_v(s)t_v\right),
\]
\[
 b_0(x,t)=-J(\tfrac12-x+t/(2\pi))
          -J(\tfrac12-x-t/(2\pi))-2J(x),\qquad
 J'(z)=\Log(2\sin\pi z),\qquad J(1/2)=0.
 \tag{2}
\]
There are two incidence terms per edge. Suppose a marked full critical
point \(p(s)\) continues holomorphically over \(D\). The factorial and
incidence sine divisors must remain nonzero, as must
\(\Delta(s)=\det(-\Phi_s''(p(s)))\). Continue all logarithms and the
determinant root from the actual seed. Set
\[
 S(s)=\Phi_s(p(s)),\qquad
 f_N(s)=N^{-\beta}e^{-NS(s)}G_N(s).
 \tag{3}
\]
Here \(S\) is holomorphic on \(D\). These hypotheses can also be
imposed on a fixed lift of a charge curve to the marked cover.

Let \(a_j\) be the unnormalized full stationary coefficients of this
same seed, continued by the independent-variable Wick formula in the
formal-component source. In particular, with \(d=e+m\),
\[
 a_0(s)=\left(\frac i\pi\right)^m(2\pi)^{d/2}
  \frac{\displaystyle\prod_{v\in I}\sin t_v(s)
                  \prod_{e\in E}(4\sin^2\pi x_e(s))^{-1}}
       {\sqrt{\Delta(s)}}.
 \tag{4}
\]
The \(a_j\) are holomorphic on the chosen regular cover, including at a
projection fold when all these full-variable hypotheses hold. They are
not defined by dividing by \(a_0\). A zero of \(a_0\) at an intermediate
point therefore does not invalidate their continuation.

## 2. A growing-order estimate for the actual seed

There is a relatively compact nonempty seed neighborhood \(U\Subset D\)
and constants \(C,A,a,\delta>0\) such that
\[
 \sup_U\left|f_N-\sum_{j=0}^{L-1}a_jN^{-j}\right|
       \le CA^L L!N^{-L}+Ce^{-\delta N},
       \qquad 1\le L\le aN.
 \tag{5}
\]
The constants are independent of \(L,N\). All sufficiently large levels
are included, with the literal parity conventions of the source.

Here are the quantitative steps connecting (5) to that actual source.
Only the generic factorial and Gaussian estimates in Sections 2--3 of
the exponential-remainder note are used; its zero-power full-grid theorem
and its \(N\)-dependent finite companion coefficients are not used.

Write \(H_N(u)=G_N^{\rm fac}(Nu-1/2)\) for the canonical centered
factorial, distinguishing it from the period in (1). Its exact
normalization and logarithmic derivative are
\[
 H_N(1/2)=\sqrt N,\qquad
 \partial_u\log H_N(u)=
   \sum_{k=0}^{N-1}\pi(u-(k+1/2)/N)
                      \cot\!\bigl(\pi(u-(k+1/2)/N)\bigr).
 \tag{6}
\]
On a buffered compact set of seed arguments in
\(\Omega=\mathbb C\setminus((-\infty,0]\cup[1,\infty))\),
the summand's \(r\)-th grid derivative is bounded by \(Cr!\rho^{-r}\).
Midpoint Euler--Maclaurin and the periodic Bernoulli bound therefore give
logarithmic coefficient and remainder bounds \(C A^j j!\) and
\(CA^L L!N^{-L}\), respectively, for \(L\le aN\).
The value in (6) fixes the integration constant. Fixed half-shifts,
finite products and inverses preserve these bounds.

For clarity, exponentiation here is quantitative. A truncated logarithm
\(Q_{L-1}(h)=\sum_{j<L}\ell_jh^j\), with
\(|\ell_j|\le CA^j j!\), is bounded on
\(|h|\le (A_1L)^{-1}\) for sufficiently large \(A_1\).
Cauchy's estimate bounds the exponential's Taylor tail at \(h=1/N\)
by \(C(A_1L/N)^L\). The inequality \(L^L\le e^L L!\)
turns this into the stated Gevrey bound. Reducing \(a\) bounds the
exact logarithmic remainder as well. No analyticity in \(1/N\) is assumed.

The actual halfwire interpolation near the original seed is
\[
 B_N(x,t)=
 \frac{N}
 {H_N(\tfrac12-x+t/(2\pi))
  H_N(\tfrac12-x-t/(2\pi))
  G_N^{\rm fac}(Nx)^2}.
 \tag{7}
\]
At the complete wire all its arguments are \(1/4\). The nonzero
small-charge seed and a fixed buffered neighborhood keep them in the
same regular compact set. Equation (7) therefore has an actual
Gevrey-1 amplitude after its exact exponential and powers of \(N\)
are extracted. Its finite-index interpolation remains the original
Newton polynomial, including every normal channel.

The local finite-index residue calculation has constant mode exactly
\(+N\) times the wire integral. Its other modes, index-end connectors
and omitted tails have a fixed exponential loss near this seed.
The pattern-adapted proof also gives fixed losses for every removed-row
pattern and mixed angular current. These estimates concern the exact
pieces and do not depend on the truncation order \(L\).

On the all-plus horizontal piece the exact trace factor is
\[
 W_N(t)e^{iN(1-\chi)t}
       =e^{-iN\chi t}(1-\eta e^{-iNt})^{-2},
       \qquad \eta=(-1)^{N-1}.
 \tag{8}
\]
On its fixed buffered lower strip, the difference of the last factor
from \(1\) is exponentially small. Keep that difference as an exact
remainder. It is not differentiated to order comparable with \(N\).
All other sign companions have their original strict seed loss.
Small complex charge perturbations cost \(e^{CN\varepsilon}\);
shrinking \(U\) preserves all these fixed losses.

The remaining joint phase in the independent wire and angular variables
has a uniformly nondegenerate analytic Morse chart. Its exact amplitude
has the bounds furnished by (6)--(7). In Morse coordinates, expand the
amplitude symbol at order \(j\) through spatial degree \(2(L-j)\).
The Gaussian moment of degree \(2q\) is bounded by \(C^q q!N^{-q}\).
Thus \(j!q!\le(j+q)!\) gives the first term of (5).
Outside the fixed Morse ball split the Gaussian into two equal factors:
one supplies \(e^{-cN}\), while the other bounds every polynomial
moment of degree at most \(2L\). Choosing \(a\) sufficiently small
absorbs the growing-degree factors into the fixed loss.
This is the growing-order argument of the generic Gaussian lemma.

The coefficients are precisely the \(a_j\) in Section 1. Completing the
wire Gaussian first or integrating all variables together gives the
same inverse quadratic form and determinant; expansion against an
auxiliary linear exponential proves equality of every Gaussian moment.
The same argument retains the exact wire constant \(+N\), sine factors,
trace constants, and outside-only complete edges. The powers combine
to \(\beta\) in (1). The two parities differ in the exponentially small
trace corrections, not in these stationary coefficients.
Absorb polynomial prefactors multiplying the fixed losses by decreasing
\(\delta\). This proves (5) for the same frozen source.

## 3. Compact Gevrey bounds for the continued formal coefficients

For every compact \(K\Subset D\) there are constants \(C_K,A_K\) with
\[
                         \sup_K|a_j|\le C_K A_K^j j!,
                         \qquad j\ge0.
 \tag{9}
\]
This assertion is formal away from the initialized neighborhood:
it does not assert a one-phase asymptotic of the exact factorials there.

To prove it, cover \(p(K)\) by finitely many buffered regular charts in
the independent variables of (2). Local sine logarithms are analytic on
each larger chart. Bernoulli bounds and Cauchy estimates give
Gevrey-1 bounds for their formal factorial amplitudes, uniformly on
the smaller chart. Finite products, inversion of the nonzero leading
factors and exponentiation preserve the bound by the auxiliary-variable
argument following (6).

The full Hessian is invertible on these charts. The analytic Morse
coordinate changes and their Jacobians are uniformly analytic after
shrinking the buffers. Composition preserves the symbol bounds on a
smaller fixed spatial polydisk. A coefficient of order \(j\) in that
symbol is bounded there by \(CA^j j!\). Its Taylor terms of spatial
degree \(2q\), after normalized Gaussian integration, contribute at
most \(C^{j+q+1}j!q!\). One can see the Gaussian bound directly from
\((2q)!/q!\le4^q q!\); the number of multivariate monomials is at most
exponential in \(q\) in fixed dimension.
At total order \(r=j+q\), sum the finitely many terms and use
\(j!q!\le r!\). This gives (9).

All derivatives were taken before imposing any wire relation.
No eliminated-wire Hessian or division by the leading density is used.
Consequently a projection fold with regular full Hessian causes no
additional problem for this bound. A factorial divisor or a zero of
the full determinant is excluded by the hypotheses.

## 4. Propagation through a subexponential complex upper bound

The analytic statement needed here is the following. Suppose
holomorphic \(f_N,a_j\) on connected \(D\) satisfy (5) on a nonempty
seed and (9) on every compact set. If
\[
 \limsup_{N\to\infty}\frac1N\log\sup_K|f_N|\le0
                        \qquad(K\Subset D),
 \tag{10}
\]
then throughout \(D\), locally uniformly and after every fixed complex
derivative,
\[
                  f_N\sim\sum_{j\ge0}a_jN^{-j}.
 \tag{11}
\]
In particular \(a_0(s_*)\ne0\) gives a nonzero leading term at \(s_*\).

Here is a proof with the required uniform truncation. Fix a compact
target \(K\). Join a closed seed disk to a finite disk cover of \(K\)
inside \(D\), and take a compact buffered neighborhood \(K'\) of these
finitely many paths. Use (9) on \(K'\) and (5) on the seed disk.
Choose
\[
 0<c<\min\{a,\,(8A)^{-1},\,(8A_{K'})^{-1}\},\qquad
 L_N=\lfloor cN\rfloor,\qquad
 P_N(s)=\sum_{j=0}^{L_N-1}a_j(s)N^{-j}.
 \tag{12}
\]
For large \(N\), successive majorant terms on \(K'\) have ratio
at most \(A_{K'}L_N/N<1/8\). Consequently
\(P_N=a_0+O_{K'}(N^{-1})\), uniformly in \(N\).
For every fixed \(M\), its tail after order \(M-1\) is \(O_{K',M}(N^{-M})\).
Also \(L_N\ge cN/2\), so \(L_N!\le L_N^{L_N}\) and (5) give
\[
 \sup_{\rm seed}|f_N-P_N|\le C e^{-\kappa N}
 \tag{13}
\]
for a fixed \(\kappa>0\). The extra \(e^{-\delta N}\) in (5) is included.

Let \(R_N=f_N-P_N\), a holomorphic function. By (10) and boundedness
of \(P_N\), it has upper bound \(C_\epsilon e^{\epsilon N}\) on \(K'\)
for every \(\epsilon>0\). Choose a common disk radius \(r\) so that
all radius-\(4r\) disks of a finite chain remain in \(K'\), consecutive
centers are at distance at most \(r\), and its first radius-\(r\)
disk lies in the seed. On each such disk the three-circles inequality is
\[
 \sup_{|s-s_0|\le2r}|R_N|
 \le
 \left(\sup_{|s-s_0|\le r}|R_N|\right)^{1/2}
 \left(\sup_{|s-s_0|\le4r}|R_N|\right)^{1/2}.
 \tag{14}
\]
It follows by applying the maximum principle to the harmonic function
affine in \(\log|s-s_0|\) on the annulus. Zeros cause no difficulty
for the subharmonic logarithm.
After at most \(J\) steps, with \(\theta=2^{-J}>0\), (13)--(14) imply
\[
 \limsup_N\frac1N\log\sup_K|R_N|\le-\kappa\theta.
 \tag{15}
\]
Indeed the prelimit exponent is
\(-\kappa\theta+\epsilon(1-\theta)\), and \(\epsilon\) is arbitrary.
Adding back the fixed-order tail of \(P_N\) proves (11).
Apply the same proof on a slightly larger target and use Cauchy's
formula for any fixed derivatives.

Thus even a bound \(e^{\sqrt N}\), for example, is allowed in (10).
The bound is uniform on complex compact sets. Pointwise or real-axis
upper information does not imply the hypothesis.

A local complex-area version suffices:
\[
 \limsup_N\frac1N\log\int_K|f_N(s)|^2\,dA(s)\le0
                         \qquad(K\Subset D).
 \tag{16}
\]
Enlarge a target compact inside \(D\) and use the holomorphic submean
inequality on disks of a fixed buffered radius. It bounds the squared
supremum on the smaller compact by a fixed constant times that integral,
which gives (10). This requires area on complex disks.

## 5. A quadratic upper trial and the original endpoint

The source-faithful quadratic in the earlier polynomial criterion can
supply (16). Keep the actual unreduced ordinary polynomial numerator
\(F_N(\mathbf z)\), \(z_v=-2\cos t_v\), with
\(\deg_{z_v}F_N\le d_v(N-1)\). Let \(\mathbf F_N\) be its ordinary
monomial coefficient vector. Apply the exact frozen finite row and
contour formula to those monomials to obtain \(\ell_N(s)\). Thus
\(G_N(s)=\ell_N(s)\mathbf F_N\), with no physical-quotient reset.
Define
\[
 r_N(s)=\|\ell_N(s)\|^2,\quad \lambda_N(s)=1+r_N(s),\qquad
 J_{N,s}(x)=\lambda_N(s)\|x-\mathbf F_N\|^2+|\ell_N(s)x|^2.
 \tag{17}
\]
Completion of the rank-one square gives
\[
 \min_xJ_{N,s}(x)=\frac{|G_N(s)|^2}{1+r_N(s)/\lambda_N(s)},
 \qquad |G_N(s)|^2\le2J_{N,s}(x).
 \tag{18}
\]
Its coefficient matrix has condition number below \(2\).
The input vector and row are specified without the unknown closed
period. This does not make their construction or a successful trial easy.

In particular any measurable trials for which the following integrals
exist and satisfy
\[
 \limsup_N\frac1N\log
 \int_K2N^{-2\beta}e^{-2N\Re S(s)}J_{N,s}(x_N(s))\,dA(s)
 \le0\qquad(K\Subset D)
 \tag{19}
\]
prove (16) and hence (11). The trials need not be holomorphic.
This is a degree-two upper problem for the literal initialized source;
no lower witness in a uniform coefficient basis is needed for this route.
No trials satisfying (19) are constructed here.

If \(\boldsymbol\chi(s_*)=\mathbf1\), the exact frozen-source endpoint is
\[
 Z_N^{\rm original}=\varepsilon_N G_N(s_*),\qquad
 \varepsilon_N=\prod_{v\in I}e^{\pi ib_v(N-1)^2/(4N)}.
 \tag{20}
\]
For integral powers this is the prescribed original physical source.
Real fixed powers retain the exact prescribed real-power extension.
Since \(|\varepsilon_N|=1\), (10) or (19), the regular continuation,
and \(a_0(s_*)\ne0\) give
\[
 Z_N^{\rm original}=\varepsilon_N N^\beta e^{NS(s_*)}
                            \{a_0(s_*)+O(N^{-1})\}.
 \tag{21}
\]
The actual source phases, aliases, first normals, odd simple-root
channel, and frozen current pieces have not been discarded.
For a supplied positive unit-charge primitive target the formal-component
proof constructs an appropriate marked curve and a target leading unit.
It does not assert that every short hyperbolic filling has such a lift.

The new analytic requirement is weaker than a fixed-polynomial upper
bound, but it remains relative to the marked geometric action.
A complete-action majorant with a fixed positive exponential excess
does not satisfy (10). There is no sharp quantum upper estimate,
global source-cycle selection, or new volume class in this note.
For a volume conclusion the original source normalization and peripheral
marks, together with \(2\pi\Re S(s_*)=\operatorname{Vol}\), are still
required. Any additional rate-neutral factor must be nonvanishing
and have logarithmic modulus \(o(N)\).
Outside data stay complete; no open free-boundary initializer is inferred.

## Complete direct sources and scope

The four complete matching texts below supply the exact frozen source,
its seed decomposition, the generic quantitative local lemmas, and the
continued full stationary coefficients. The proof above upgrades the
same seed and performs the optimal truncation and propagation.

| Complete source | SHA-256 |
|---|---|
| [Generic factorial and Gaussian estimates, Sections 2--3](research_full_charge_grid_exponential_remainder.md) | 4a33f24addd11b31a400e4c62ff96f337436fdb1aecd44c34380f635985faad2 |
| [Pattern-adapted initialized source](research_pattern_adapted_polarized_heat_initializer.md) | a27c25dae7f3be3f1ef52fb369ecca822b0896a4b034450131e05b12423c2694 |
| [Full marked formal component](research_positive_source_formal_component.md) | 08b41e17dbdcfe6df800fe257fa6bb590f2e580e11f2ff2b4e1b7541919494f4 |
| [Polynomial upper criterion and exact quadratic](research_polarized_polynomial_upper_criterion.md) | 1a7ca165e0bc3b6e115566859e2a780079389d3004e6915ff396eb7c9ca47d9a |

The zero-power domain of the first source's full-grid theorem is not
used as a theorem about nonzero powers. Its finite companion sums do not
replace the holomorphic \(a_j\) in (12).
Optimal Gevrey truncation and three-circles propagation are standard
analytic tools; no novelty is claimed for those methods.
