# Polynomial degree controls the terminal endpoint layer

Research deduction, 5 November 2026. The original terminal polynomial
has arbitrarily small exponential growth on a sufficiently small fixed
arc about its endpoint. The argument uses its degree and its already
proved asymptotics on compact arcs. It does not extrapolate a stationary
phase formula into a shrinking endpoint layer. As a consequence, the
joint terminal right-half comparison extends through the endpoint for
every fixed compact set of complex neighboring parameters.

## 1. An elementary estimate across a missing arc

Let \(P\) be a polynomial of degree at most \(D\), and suppose
\[
 |P(e^{it})|\le M\qquad(\alpha\le |t|\le\pi),
 \qquad 0<\alpha<\pi.
\]
Then
\[
 \max_{|Y|=1}|P(Y)|
 \le\sqrt2 M\exp\{D\operatorname{arcosh}(\sec(\alpha/2))\}.
                                                               \tag{1}
\]
Here \(\operatorname{arcosh}\) is the nonnegative real inverse
hyperbolic cosine. This slightly nonsharp estimate has an elementary
proof, which is useful because we need its dependence on the degree
and the missing arc.

Set
\[
 Q(t)=\tfrac12\bigl(|P(e^{it})|^2+|P(e^{-it})|^2\bigr).
\]
This is an even real trigonometric polynomial of degree at most
\(D\), so \(Q(t)=R(\cos t)\) for a real polynomial \(R\)
of degree at most \(D\). On \([-1,\cos\alpha]\),
\(0\le R\le M^2\). The elementary Chebyshev extrapolation
inequality therefore gives, for \(\cos\alpha\le x\le1\),
\[
 |R(x)|\le M^2 T_D\left(\frac{2x+1-\cos\alpha}{1+\cos\alpha}\right).
                                                               \tag{2}
\]
For completeness, after rescaling the interval to \([-1,1]\),
this inequality follows by comparing a polynomial bounded by one
with \(cT_D\), where \(c>1\). At the \(D+1\) successive
extrema of \(T_D\), their difference has alternating signs.
Equality with \(cT_D\) at a point beyond one would give another
zero, exceeding the degree. Changing the sign handles a negative
value. The constant case is immediate.

At \(x=1\), the argument in (2) is
\(1+2\tan^2(\alpha/2)\). Since
\[
 \operatorname{arcosh}(1+2\tan^2(\alpha/2))
      =2\operatorname{arcosh}(\sec(\alpha/2)),
\]
the formula \(T_D(\cosh v)=\cosh(Dv)\le e^{Dv}\),
together with \(|P(e^{it})|^2\le2Q(t)\), proves (1).
The assumed bound already covers the other angles. If \(M=0\),
the polynomial vanishes on an arc and is identically zero.

This belongs to the classical Remez family of polynomial inequalities.
The sharper arbitrary-measurable-set theorem is due to
[Tikhonov and Yuditskii, *Sharp Remez inequality*](https://arxiv.org/abs/1809.09726).
Only the elementary single-arc proof above is used here.

## 2. A localization lemma for a sequence of polynomials

Let \(P_N(Y,w)\) be polynomials in \(Y\), of degree at most
\(dN\), holomorphic in an auxiliary parameter \(w\) near
\(w_0\). Suppose the following two upper bounds hold.

First, on one fixed parameter neighborhood and on the whole unit
circle,
\[
 |P_N(Y,w)|\le C N^A e^{MN}                               \tag{3}
\]
for a fixed finite \(M\ge0\). Second, let \(h\) be continuous
on \([0,1]\), with \(h(0)=h(1)=0\). For each compact
\(I\subset(0,1)\) and each \(\nu>0\), a smaller fixed
parameter neighborhood satisfies
\[
 |P_N(e^{2\pi ie},w)|\le C_{I,\nu}N^{A_{I,\nu}}
                         e^{N(h(e)+\nu)}\quad(e\in I).
                                                               \tag{4}
\]
The neighborhood in (4) may depend on \(I,\nu\).

**Lemma 1.** For every \(\eta>0\), there are fixed
\(\tau>0\), a parameter neighborhood of \(w_0\), and
constants \(C_\eta,A_\eta\) such that
\[
 |P_N(e^{2\pi ie},w)|\le C_\eta N^{A_\eta}e^{\eta N}
       \quad\bigl(\operatorname{dist}(e,\mathbb Z)\le\tau\bigr).
                                                               \tag{5}
\]
All choices are made before \(N\) tends to infinity.

*Proof.* Choose \(0<s<1/4\) so that
\(h(e)<\eta/8\) on the two end intervals of width \(s\).
Choose a positive integer \(K\) with
\[
                 M+K\log\cos(\pi s)<0.
\]
Introduce the polynomial
\[
 \widetilde P_N(Y,w)=P_N(Y,w)((1+Y)/2)^{KN},
 \qquad \deg_Y\widetilde P_N\le(d+K)N.                  \tag{6}
\]
On the middle interval \([s,1-s]\), (3) bounds this by a
polynomial prefactor, since the modulus of its extra factor is
\(|\cos\pi e|^{KN}\). Choose \(0<\delta<s\) so small that
\[
 (d+K)\operatorname{arcosh}(\sec\pi\delta)<\eta/4.
                                                               \tag{7}
\]
Apply (4) on \([\delta,1-\delta]\), with
\(\nu=\eta/8\). On its two end pieces the extra factor has
modulus at most one. Combining these pieces with the middle bound
gives
\[
 |\widetilde P_N(e^{2\pi ie},w)|\le C N^B e^{\eta N/4}
                     \quad(\delta\le e\le1-\delta).
                                                               \tag{8}
\]
The single-arc inequality (1), with \(\alpha=2\pi\delta\),
now bounds \(\widetilde P_N\) on the whole circle by
\(\sqrt2 C N^B e^{\eta N/2}\).

Finally choose \(0<\tau\le\delta\) so small that
\(-K\log\cos\pi\tau<\eta/4\). On the arc of width
\(\tau\) at either end we can divide (6) by its nonvanishing
extra factor. The resulting exponent is at most \(3\eta/4\),
which proves (5), with room to spare. All bounds are uniform on
the parameter neighborhood chosen for (8). \(\square\)

If the parameters range over a complex disk, fixed parameter
derivatives satisfy (5) on a smaller disk by Cauchy's formula.
This statement requires a uniform neighborhood in (4); a list of
pointwise asymptotics would not suffice.

In fact the same proof gives the bound on a fixed complex disk
\(|Y-1|\le\zeta\), for sufficiently small \(\zeta>0\).
For any polynomial \(Q\) of degree at most \(D\),
\[
 |Q(Y)|\le\max(1,|Y|)^D\max_{|Z|=1}|Q(Z)|.
\]
The maximum principle proves this inside the unit circle; applying
it to the reversed polynomial proves it outside. Apply this to
\(\widetilde P_N\) after (8). On \(|Y-1|\le\zeta<1\),
division by the multiplier adds at most
\[
 N\{(d+K)\log(1+\zeta)-K\log(1-\zeta/2)\}
\]
to the logarithmic bound. Choose \(\zeta\) so this is less
than \(\eta N/4\). This proves the same conclusion on that
complex disk. Fixed derivatives in \(Y\), as well as in
\(w\), follow on smaller disks by Cauchy's formula.

## 3. Application to the original terminal polynomial

Retain exactly the finite polynomial
\[
 H_N(w,Y)=\sum_{l=0}^{N-1}
           \frac{(-q)^{-l}e_l(w)}{P_l}(Y;r)_l,
 \qquad q=e^{\pi i/N},\quad r=q^{-2},\quad P_l=(r;r)_l.
                                                               \tag{9}
\]
Its degree in \(Y\) is at most \(N-1\). At odd levels
some coefficients at the complete color vanish; at even levels
they need not vanish. The argument uses the polynomial (9) at
both parities and never deletes its even-level difference-equation
forcing.

The global bound (3) follows directly from the literal formula.
Write \(S_l=|P_l|\). The complete product identity gives
\[
 S_l\ge N2^{-(N-1-l)},\qquad |(Y;r)_l|\le2^l
                                      \quad(|Y|=1).
\]
Consequently
\[
 |H_N(w,Y)|\le\frac{2^{N-1}}N\sum_{l=0}^{N-1}|e_l(w)|.
                                                               \tag{10}
\]
The [zero-safe Newton tube bound](research_mixed_newton_color_tubes.md)
bounds the sum in (10) by a polynomial times \(e^{(b_2+1)N}\)
on, for example, \(|w+2|\le1\), where \(b_2<.584\).
Thus any sufficiently large fixed \(M\), for example \(M=3\),
suffices. No favorable phase is needed for this coarse bound.

On compact subintervals of \((0,1)\), the
[whole-color endpoint theorem](research_complete_boundary_full_index_interval.md#7-the-whole-boundary-polynomial-near-the-complete-color)
and the exact identity
\(H_N(w,e^{2\pi ie})=G_N(Ne)\mathcal C_N(e,w)\)
give (4), with
\[
 h(e)=J(e)+\Re S(e),\qquad
 S(e)=F(e,u_c(e)).                                      \tag{11}
\]
These are the original functions and branches. The ordinary-color
action is holomorphic near each compact interval times \(\{-2\}\),
so a sufficiently small fixed color disk pays any prescribed
\(\nu\). The factorial symbol and Gaussian prefactors add only
powers of \(N\).

We check the endpoints of \(h\), rather than infer them from
\(H_N(w,1)=1\). In the notation
\(\sqrt{1-2e^{2\pi ie}}=a(e)+ib(e)\), the
[exact derivative calculation](research_mixed_cap_seam_source_bounds.md#2-both-real-row-maxima-reduce-to-fixed-scalars)
gives
\[
 h'(e)=\tfrac12\log\frac{1-b(e)}{1+b(e)},
 \qquad b(1-e)=-b(e).                                   \tag{12}
\]
Therefore the derivative of \(h(1-e)-h(e)\) is zero. Its
value at \(e=1/2\) is zero, and hence
\[
                            h(1-e)=h(e).                \tag{13}
\]
As \(e\downarrow0\), the prescribed square root tends to
\(-i\), so \(u_c(e)\to0\). The primitive \(J\) has a
continuous value zero at the origin, and \(J(1/2)=0\).
Substitution into
\[
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu
\]
therefore shows \(h(e)\to0\). Equation (13) proves the
same limit at one. Equivalently, continuity of \(J\) at the
origin follows from its local primitive \(z\log z+O(z)\)
on the prescribed regular sector. Thus (11) extends continuously
to \([0,1]\) with zero values at both ends.

**Theorem 2.** For each \(\eta>0\), there are fixed
\(\tau,\rho>0\) such that, for every fixed ordinary derivative
order \(k\),
\[
 \sup_{\substack{\operatorname{dist}(e,\mathbb Z)\le\tau\\
                   |w+2|\le\rho}}
 |\partial_w^k H_N(w,e^{2\pi ie})|
              \le C_{\eta,k}N^{A_{\eta,k}}e^{\eta N}.
                                                               \tag{14}
\]
Both level parities are included. The color radius may be chosen
once and then halved for all fixed derivative orders.

Lemma 1 proves the undifferentiated assertion; Cauchy's formula
proves its last statement. Its complex-disk extension also gives
the same exponential bound on a sufficiently small fixed disk
\(|Y-1|\le\zeta\), and for every fixed joint derivative in
\(w,Y\) on smaller disks. The radius depends on \(\eta\);
no specified larger complex neighborhood is asserted.

Combining (14) with the compact-interval estimate also gives the
following useful uniform envelope: for every \(\eta>0\), on
a sufficiently small fixed color disk,
\[
 |\partial_w^k H_N(w,e^{2\pi ie})|
       \le C_{\eta,k}N^{A_{\eta,k}}e^{N(h(e)+\eta)}
                           \quad(0\le e\le1).           \tag{15}
\]
Here \(h\ge0\): (12) is positive below one half and negative
above, and both endpoint values are zero. To prove (15), use
(14) on two small end intervals and the compact theorem on their
closed complement, allocating one total tolerance.

## 4. The joint right-half bound, including its endpoint

For the neighboring parameter \(a\), let
\(R_\epsilon(a,e)\) and \(R_\epsilon^{\rm seam}(a)\)
be the full row envelopes in equations (10) of
[the terminal right-sector reduction](research_mixed_terminal_right_endpoint_reduction.md#4-a-joint-comparison-without-a-neighboring-height-restriction).
All rows \(0\le u\le1\) and the signed chirp are retained.
The integrals defining these envelopes are continuous, including
at their logarithmic zeros. Their maxima are continuous as well.
In particular
\[
 R_\epsilon(a,1)=R_\epsilon^{\rm seam}(a).
                                                               \tag{16}
\]
One justification uniform in the row endpoint is translation
continuity in \(L^1\) of \(\log(2|\sin\pi t|)\) on a
period: the difference of every partial integral is bounded by
the full \(L^1\) difference. The corresponding integrals in
\(a\) are likewise continuous on compact sets, including the
real divisor.

Put
\[
 K(e)=-\int_{1/2}^{e}\log\sin\pi t\,dt,
 \quad K(1)=\tfrac12\log2,
 \quad K(e)\ge\tfrac{\pi^2}{6}(e-1/2)^3.
                                                               \tag{17}
\]
The proved joint compact comparison and continuity now give
\[
 h(e)+R_\epsilon(a,e)
       \le h(1/2)+R_\epsilon(a,1/2)-K(e)
                                  \quad(1/2\le e\le1).
                                                               \tag{18}
\]
In particular the seam envelope itself has the strict allowance
\[
 R_\epsilon^{\rm seam}(a)
       \le h(1/2)+R_\epsilon(a,1/2)-\tfrac12\log2.
                                                               \tag{19}
\]
This is stronger than the earlier generic comparison obtained by
bounding the two row potentials separately.

**Theorem 3.** Fix a compact set of neighboring parameters \(a\).
For every \(\eta>0\), a sufficiently small ordinary-color disk
and polynomial prefactors give
\[
 \begin{split}
 &\left|C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ie})
           \partial_w^k H_N(w,e^{2\pi ie})\right|\\
 &\qquad\le C N^A
   \exp\{N[h(1/2)+R_\epsilon(a,1/2)-K(e)+\eta]\}
                         \qquad(1/2\le e\le1).
 \end{split}                                                   \tag{20}
\]
The complete raw finite-row bound for \(C\), with an arbitrarily
small rate tolerance, combines with (15) and (18). Split \(\eta\)
between those two bounds. Their constants are uniform on the fixed
compact neighboring set. No restriction such as
\(|\Im a|\le.057\) is used.

The actual terminal Fourier polynomial has upper rate zero on
this real half-period, as in the right-sector reduction. The selected
factor \(X_e^{-N\sigma}\) has modulus one. Thus the same bound,
with one total tolerance and a changed polynomial prefactor, includes
these actual terminal factors. The neighboring allocations are left
unchanged. Replacing a real terminal angle by \(1/2\) also leaves
the neighboring hybrid height unchanged.

For every fixed \(\beta>0\), (20) has a uniform strict loss
on \([1/2+\beta,1]\) after taking \(\eta<K(1/2+\beta)\).
The comparison at \(e=1/2\) against the full geometric action
remains necessary. Formula (20) bounds the terminal part by a full
row envelope at that point; it does not replace this envelope by
the coherent conditional action. That distinction, the remaining
first-end comparisons, and the original middle completion remain
part of the open-source problem. No new knot volume theorem is
asserted here.

