# Uniform finite-factorial formulas on shrinking endpoint collars

Private written proof, 18 November 2026.

The actual factorial head gauges admit uniform finite-product
factorizations on both endpoint scales of E. The formulas retain
the two independent quantum/meridian normal parameters. On a collar
of width \(O(N^{3/4})\), a cubic occupation correction in the
exponent must be kept; after doing so the relative error is
\(O(N^{-1/4})\). On a collar of width \(O(\sqrt N)\), the simpler
quadratic formula has relative error \(O(N^{-1/2})\).

These are formulas for integer occupation indices, holomorphic in
the actual head parameters. They are not a noninteger-occupation
interpolant or a theorem about the neighboring network. No source
contour, packet coefficient or scalar lower bound follows here.

## 1. Actual parameters and finite products

Use the finite heads and gauges of E, and put
\(c_0=2\pi i\), \(h_N=c_0/N\).
For each fixed \(N\ge2\), introduce normal coordinates
\[
 h=\frac{c_0}{N-\kappa},\qquad Q=e^h,\qquad
 q=e^{h/2},\qquad M=e^{\nu h/2}.
 \tag{1}
\]
Fix a small radius \(r<1/16\). The estimates below hold on a doubled
polydisk \(|\kappa|,|\nu|\le2r\), with derivatives on smaller disks.
This is an actual two-parameter analytic family. Its central point
is the complete root, not a formal replacement for it.

For integers \(0\le a\le d=N-1\), let
\[
 F_a=\prod_{j=1}^a(1-Q^j),\qquad
 H_a=\prod_{j=1}^a\alpha_j,\qquad
 \alpha_j=M Q^{-j}-M^{-1},
 \tag{2}
\]
with empty products one. These are exactly the gauges
\(G_F=\operatorname{diag}(F_a)\) and
\(G_E=\operatorname{diag}(H_a^{-1})\) in E.
Also write
\[
 U_a^F=F_d/F_{d-a},\qquad U_a^H=H_d/H_{d-a}.
 \tag{3}
\]
All denominators here are units on this polydisk. For example
\(1-Q^j=0\) would force \(j=k(N-\kappa)\) for an integer \(k\);
none is possible for \(1\le j<N\) and small \(\kappa\).
Similarly \(\alpha_j=0\) would force
\(\nu-j=k(N-\kappa)\); its possible nearest endpoint equations
would be \(\nu=j\) or \(\nu-\kappa=j-N\), both excluded.
The other integers \(k\) are farther away. These observations also
verify the stated units without extending an arrow through index \(N\).

Define polynomials
\[
 {\cal P}_a(z)=\prod_{j=1}^a(j+z),\qquad
 S_1(a)=\frac{a(a+1)}2,
 \tag{4}
\]
\[
 S_2(a,z)=\sum_{j=1}^a(j+z)^2
  =\frac{a(a+1)(2a+1)}6+za(a+1)+az^2.
 \tag{5}
\]
Equivalently \({\cal P}_a(z)=\Gamma(a+1+z)/\Gamma(1+z)\);
the finite product (4) is its definition used below. No Gamma
asymptotic or branch choice in the occupation variable is needed.

## 2. Four uniform endpoint factorizations

Fix \(C>0\). Uniformly for integer \(0\le a\le C N^{3/4}\)
and all sufficiently large \(N\), the following exact identities
define holomorphic remainder functions:
\[
 \boxed{\begin{aligned}
 F_a={}&(-h)^a a!\,
  \exp\left\{\frac h2 S_1(a)+\frac{h^2}{24}S_2(a,0)
                         +R_a^F\right\},\\
 H_a={}&(-h)^a{\cal P}_a(-\nu)\,
  \exp\left\{-\frac h2 S_1(a)+\frac{h^2}{24}S_2(a,-\nu)
                         +R_a^H\right\},\\
 U_a^F={}&h^a{\cal P}_a(-\kappa)\,
  \exp\left\{-\frac h2S_1(a)+\frac{ha\kappa}2
            +\frac{h^2}{24}S_2(a,-\kappa)+R_a^{UF}\right\},\\
 U_a^H={}&h^a{\cal P}_a(\nu-\kappa)\,
  \exp\left\{\frac h2S_1(a)-\frac{ha\kappa}2
            +\frac{h^2}{24}S_2(a,\nu-\kappa)+R_a^{UH}\right\}.
 \end{aligned}}
 \tag{6}
\]
For any of the four remainders,
\[
 |R_a|\le C_{C,r}|h|^4(a+1)^5=O(N^{-1/4}).
 \tag{7}
\]
The remainder is zero when \(a=0\); the displayed upper bound
is simply convenient for all indices. Thus replacing \(e^{R_a}\)
by one has uniform relative error \(O(N^{-1/4})\).

Here is a direct proof. Near zero the uniquely normalized
holomorphic logarithm
\[
 L(z)=\log\frac{e^z-1}{z},\qquad L(0)=0
 \tag{8}
\]
satisfies
\[
 L(z)=\frac z2+\frac{z^2}{24}+z^4 R(z),
 \qquad |R(z)|\le C_*
 \quad (|z|\le1/2).
 \tag{9}
\]
Indeed \(L(z)-z/2=\log(\sinh(z/2)/(z/2))\) is even, and
its quadratic coefficient is \(1/24\). Division by \(z^4\)
after subtracting that coefficient is removable and bounded
on a slightly larger disk. This proves the analytic remainder
claim, not only a formal expansion.

The exact factors in the four products are respectively
\[
 \begin{aligned}
 1-e^{hj}&=(-hj)e^{L(hj)},\\
 \alpha_j&=M^{-1}[-h(j-\nu)]e^{L(-h(j-\nu))},\\
 1-Q^{N-j}&=h(j-\kappa)e^{L(-h(j-\kappa))},\\
 \alpha_{N-j}&=M^{-1}h(j+\nu-\kappa)
                                      e^{L(h(j+\nu-\kappa))}.
 \end{aligned}
 \tag{10}
\]
In the last two lines use \(hN=c_0+h\kappa\).
All their arguments lie in (9) for large \(N\), uniformly on
the prescribed collar. Multiply these identities for \(1\le j\le a\).
For the second line, \(M^{-a}=e^{-a\nu h/2}\) cancels the
\(+a\nu h/2\) from the linear terms of \(L\).
For the fourth it cancels the analogous \(+a\nu h/2\),
leaving precisely \(-ha\kappa/2\).
This gives every sign and parameter in (6).
Finally
\[
 \sum_{j=1}^a |h|^4|j+z|^4
                  \le C_r |h|^4(a+1)^5
 \tag{11}
\]
for the bounded shifts occurring here, proving (7).
The only powers such as \((-h)^a\) are integer powers.

The upper gauges themselves are obtained by dividing the
unchanged units \(F_d,H_d\) by the last two expressions in (6).
Those full-head units have not been normalized away. At the root
they are \(F_d=N\) and \(H_d=(-1)^dN\), respectively.
The first equality follows from
\((z^N-1)/(z-1)\) at \(z=1\); the second follows from
\(H_d=Q^{-d(d+1)/2}F_d\) at \(M=1\).

## 3. The two scales and cancellation of the large linear phases

At \(a=O(\sqrt N)\), the terms \(h^2 S_2(a,z)\) are
\(O(N^{-1/2})\). Omitting them as well as the remainders gives
relative error \(O(N^{-1/2})\) in all four formulas, uniformly
in the normal parameters.

At \(a=O(N^{3/4})\), however,
\[
 hS_1(a)=O(N^{1/2}),\qquad
 h^2S_2(a,z)=O(N^{1/4}).
 \tag{12}
\]
Their exponentials cannot be replaced by one in a relative
matching estimate. In particular the cubic occupation
correction in (6) is necessary on this scale.

Multiplying the paired gauges does remove the large linear
terms exactly:
\[
 F_aH_a=(-h)^{2a}a!\,{\cal P}_a(-\nu)
 \exp\left\{\frac{h^2}{24}
       [S_2(a,0)+S_2(a,-\nu)]+R_a^F+R_a^H\right\},
 \tag{13}
\]
\[
 U_a^F U_a^H=h^{2a}{\cal P}_a(-\kappa){\cal P}_a(\nu-\kappa)
 \exp\left\{\frac{h^2}{24}
       [S_2(a,-\kappa)+S_2(a,\nu-\kappa)]
                              +R_a^{UF}+R_a^{UH}\right\}.
 \tag{14}
\]
This is an identity of these finite products, not permission
to cancel gauge factors belonging to unrelated source boundaries.
In a network they are inserted with their actual inverse factors,
rows, columns and interface arrows, as in E.

## 4. Normal derivatives and the ordinary head path

The normalized remainders in (6) are holomorphic on the doubled
fixed \((\kappa,\nu)\) polydisk. Cauchy's formula therefore gives,
for every fixed pair \(u,v\ge0\),
\[
 \sup_{|\kappa|,|\nu|\le r}
       |\partial_\kappa^u\partial_\nu^v R_a|
                     \le C_{u,v,C,r}N^{-1/4}.
 \tag{15}
\]
The same holds for \(e^{R_a}-1\). For the simpler
\(\sqrt N\) formulas the normalized relative errors and every
such fixed derivative are \(O(N^{-1/2})\).
The exact polynomial, power and exponential factors of (6)
remain differentiated; the bound concerns their normalized
remainder, not the entire factorial.

The coordinate change (1) has
\(|h-h_N|=O(N^{-2})\), \(|M-1|=O(N^{-1})\).
Smaller corresponding \(h,M\) disks lie in the prescribed
normal coordinate domain. Cauchy estimates there give the
bound \(O(N^{2j+\ell-1/4})\) for fixed
\(\partial_h^j\partial_M^\ell\) of the normalized remainder;
replace \(-1/4\) by \(-1/2\) on the smaller collar scale.

The actual ordinary-color head path has the particularly simple
equation
\[
                    M=-e^{Nh/2}\quad\Longleftrightarrow\quad\nu=\kappa
 \tag{16}
\]
on these local logarithmic branches, since
\(-e^{Nh/2}=e^{h\kappa/2}\).
Before restricting to that path, the two endpoint wall
coefficients are exactly
\[
 \delta=1-Q^N=1-e^{h\kappa},\qquad
 w=M Q^{-N}-M^{-1}
                  =M^{-1}(e^{h(\nu-\kappa)}-1).
 \tag{17}
\]
Thus \(w\) vanishes identically on (16), while the independent
quantum/meridian germ retains both walls. Neither wall was
divided out of a finite head identity.
These are head-parameter statements. Identifying closed
ordinary-color and ADO-pivot source derivatives would still
require their full pivot and twist comparison, which is not
asserted here.

## 5. Scope of the analytic bridge

Equations (6)--(17) provide a uniform normalization for actual
endpoint gauge factors and all their fixed parameter normals.
They retain the exact finite upper factors, empty products,
integer shifts and endpoint arrows of the source.

The occupation \(a\) has remained an integer throughout.
These formulas alone do not continue the source along a
complex occupation contour through a factorial wall. They
also do not supply the neighboring transfer-diagonal kernel,
its normal Hessian, its geometric coefficient, or control of
the complementary source. In particular the two-variable
Gaussian hypothesis in an endpoint packet is not proved by
these one-variable finite-product identities.

## Complete direct source

* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.

The entire direct text was read nontruncated in the current
author sequence. It is used for the literal head/gauge
definitions, normal-germ scope and the source-preserving
meaning of the basis changes. The finite products, bounds,
normal coordinates and error estimates above are proved here.
Only written mathematics and text/hash operations were used.
No frozen or public file was edited.
