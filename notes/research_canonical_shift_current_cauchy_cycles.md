# Cauchy cycles of the original color-shift endpoint current

Private written proof, 18 November 2026.

The actual shift endpoint in [B] has an exact meridian Cauchy
representation. It integrates the full shift semigroup, without
truncating its Borel or meridian derivatives. For one sufficiently
short cutoff, this gives a constructed contour decomposition of the
original complete-color scalar at every level: a bounded initial
integral, the scalar endpoint, an exponentially small outer contour,
and positively oriented contours around the logarithmic Alexander
roots. The coefficients of these last contours are exactly \(+1\).

The scalar endpoint remains in this short-cutoff identity. Its
large-cutoff estimate [E] cannot be applied by silently continuing the
other terms to that cutoff. General continued paths also retain their
hole boundaries and both banks of every meridian cut.

## 1. The canonical source and a common Cauchy domain

Use the original reduced, zero-framed color polynomials \(C_L(q)\)
and the natural coordinates
\[
 h=\log Q,\qquad q=e^{h/2},\qquad u=\log Y.
 \tag{1}
\]
Write the canonical Borel germ as
\[
 b(u,\xi)=\sum_{j\ge0}W_j(e^u)\frac{\xi^j}{j!},\qquad
 W_0(Y)=\Delta_K(Y)^{-1},\qquad \Delta_K(1)=1.
 \tag{2}
\]
By [G], this series is jointly holomorphic for small \(\xi\),
uniformly on every compact logarithmic meridian set avoiding
\[
                 \mathcal Z=\{u:\Delta_K(e^u)=0\}.
 \tag{3}
\]
Its coefficients are rational functions of \(e^u\), so these germs
glue and are \(2\pi i\)-periodic wherever their common series
converges. No simple-root or node hypothesis is used below.

First let \(\Omega\) be a bounded connected domain with piecewise
smooth boundary, possibly with finitely many holes, containing \(0\).
Assume \(b\) has been constructed jointly on a neighborhood of
\(\overline\Omega\) along a finite Borel path \(\gamma:0\to R\).
It is single-valued on that domain with those retained path histories.
The boundary \(\partial\Omega\) has its positive domain orientation:
outer boundaries counterclockwise and hole boundaries clockwise.

Let \(I\) be the primitive from zero along \(\gamma\). The actual
semigroup from [B] is
\[
 c_s(u,\xi)=e^{sI\partial_u}b(u,\xi)
       =\sum_{n\ge0}\frac{s^n}{n!}I^n\partial_u^n b(u,\xi).
 \tag{4}
\]
On every smaller meridian compact it is entire in \(s\), locally
uniformly. Indeed the derivative costs \(n!d^{-n}\), the primitive
contributes \(\operatorname{length}(\gamma)^n/n!\), and the
remaining \(1/n!\) makes an exponential series. The same argument
justifies an extra derivative and primitive.

Fix an integer \(L\ge1\) and \(a\in\Omega\setminus\{0\}\), and set
\(h=a/L\). Choose a piecewise smooth path \(s:0\to L\) such that
\(u=a-sh\) remains in \(\Omega\). Such a path exists because
\(\Omega\) is connected. Define the original continued shift current
by its actual transport integral
\[
 K_L(h;\gamma)=
       \int_{s:0\to L}(\partial_u I c_s)(a-sh,R)\,ds.
 \tag{5}
\]
It agrees with [B]'s current on the initial small disk. The formula
below shows that it is independent of this \(s\)-path inside the
specified single-valued Cauchy domain.

For an oriented contour \(C\) in that boundary define
\[
 \mathcal K_{L,a,\gamma}(C)=
 \frac{L}{2\pi i}\int_C\frac{dv}{v(v-a)}
            \int_\gamma e^{L(R-\xi)/v}b(v,\xi)\,d\xi .
 \tag{6}
\]
Neither \(0\) nor \(a\) is on \(C\).

**Exact Cauchy current.** With the original normalization,
\[
                   K_L(h;\gamma)
                       =\mathcal K_{L,a,\gamma}(\partial\Omega).
 \tag{7}
\]
The fixed-color comparison is consequently
\[
 C_L(e^{h/2})=
 U_\gamma(h,e^a)+e^{-R/h}A_L(h,R)
           -e^{-R/h}\mathcal K_{L,a,\gamma}(\partial\Omega),
 \tag{8}
\]
where
\[
 U_\gamma(h,e^a)=\frac1h\int_\gamma e^{-\xi/h}b(a,\xi)\,d\xi,
 \quad
 A_L(h,R)=\sum_{k,n\ge0}c_{L,k+n}h^k\frac{R^n}{n!},
 \quad C_L(e^{h/2})=\sum_{j\ge0}c_{L,j}h^j.
 \tag{9}
\]
The function \(A_L\) is the entire scalar endpoint from [E].
There is no dimension factor, adjustable period normalization, or
discarded meridian current in (8).

## 2. Integrating the full semigroup exactly

For a boundary point \(v\), Cauchy's formula and the original
iterated primitives give
\[
\begin{split}
 (\partial_u I c_s)(u,R)
 &=\frac1{2\pi i}\int_{\partial\Omega}\frac{dv}{(v-u)^2}
       \int_\gamma
          (1+t)e^t b(v,\xi)\,d\xi,\\
 t&=\frac{s(R-\xi)}{v-u}.
\end{split}                                                    \tag{10}
\]
To check every factorial, the \(n\)-th term of (4) after
\(\partial_u I\) is \(s^nI^{n+1}\partial_u^{n+1}b/n!\).
The primitive kernel is \((R-\xi)^n/n!\), and the Cauchy derivative
is \((n+1)!/(v-u)^{n+2}\). The resulting series is
\(\sum_{n\ge0}(n+1)t^n/n!=(1+t)e^t\).
Compact path images have positive distance from the boundary, so
all these sums and finite integrals converge normally.

Put \(u=a-sh\), \(d_s=v-a+sh\), and \(y=s/d_s\).
Then
\[
 \frac{dy}{ds}=\frac{v-a}{d_s^2},\qquad
 \int_{s:0\to L}
       \frac{(1+(R-\xi)y)e^{(R-\xi)y}}{d_s^2}\,ds
     =\frac{L}{v(v-a)}e^{L(R-\xi)/v}.             \tag{11}
\]
This is the primitive \(y e^{(R-\xi)y}/(v-a)\), evaluated at
\(y=0\) and \(y=L/v\). It is single-valued: no logarithm or
winding constant appears. The boundary points \(v\) never meet
the chosen characteristic \(u=a-sh\). Substitution into (10)
proves (7), including both hole orientation and the factor \(L\).

For completeness, let \(v_s=\mathcal L_\gamma c_s\), where
\(\mathcal L_\gamma f=h^{-1}\int_\gamma e^{-\xi/h}f\,d\xi\).
The exact finite-primitive identity in [B] gives
\[
 \partial_s v_s=h\partial_u v_s
                       -e^{-R/h}\partial_u I c_s.
 \tag{12}
\]
Along the complex characteristic \(u=a-sh\), integration yields
\[
 U_\gamma(h,e^a)=\mathcal L_\gamma c_L(0,\cdot)
                         +e^{-R/h}K_L(h;\gamma).
 \tag{13}
\]
The actual formal color restriction in [B] identifies
\(c_L(0,\xi)\) with the entire scalar Borel transform of
\(C_L(e^{h/2})\). Their equality starts as an equality of convergent
germs and continues on the specified path. Its finite Laplace
integral is exactly
\[
       \mathcal L_\gamma c_L(0,\cdot)
                      =C_L(e^{h/2})-e^{-R/h}A_L(h,R).
 \tag{14}
\]
Initially [B] proves this for small \(h\). The finite exponential
sum \(C_L(e^{h/2})\), its entire endpoint from [E], and the finite
integral are holomorphic for every \(h\ne0\), so (14) holds there
by analytic continuation as well.
Equations (13)--(14) prove (8). Alternatively (7)--(8), initially
proved for small \(a\), continue analytically in \(a\) throughout
the specified domain. This explains why a straight characteristic
need not be forced through a removed Alexander neighborhood.

## 3. Constructed short-cutoff cycles at the physical sequence

Put \(a_*=2\pi i\). Choose any \(\rho>\pi\) for which the circle
\[
 C_\rho=\{v:|v-i\pi|=\rho\}
 \tag{15}
\]
avoids \(\mathcal Z\). Only finitely many points of \(\mathcal Z\)
lie in its closed disk. Surround them by disjoint small closed
disks \(D_\nu\), lying inside \(C_\rho\) and avoiding \(0,a_*\).
They can be chosen because \(\Delta_K(1)=1\). Let
\(\Omega_\rho\) be the large disk minus these closed disks.
It is connected and contains \(0,a_*\).

The exponential image of a slightly enlarged compact collar of
\(\overline{\Omega_\rho}\) avoids zero and the Alexander roots.
The compact-meridian estimate [G] therefore supplies \(r_0>0\)
and \(M<\infty\) such that the *actual canonical series* (2)
is jointly holomorphic and bounded by \(M\) there for
\(|\xi|\le r_0\). In particular all the following contours are
constructed, with no global continuation assumption.

Fix \(0<r\le r_0\), set \(R=ir\), and take the straight path
\(\gamma_r(\xi)=i[0,r]\). Let each \(C_\nu=\partial D_\nu\)
be counterclockwise. For \(N\ge2\) put
\[
 h_N=\frac{2\pi i}{N},\qquad q_N=e^{\pi i/N},\qquad
 \mathcal E_{N,r}(C)=
       e^{-R/h_N}\mathcal K_{N,a_*,\gamma_r}(C).
 \tag{16}
\]
Then (8) is the exact original-source identity
\[
 \boxed{\quad
 C_N(q_N)=U_R(h_N,1)+e^{-R/h_N}A_N(h_N,R)
             -\mathcal E_{N,r}(C_\rho)
             +\sum_\nu\mathcal E_{N,r}(C_\nu).
 \quad}                                                        \tag{17}
\]
Here periodicity of the convergent canonical series identifies
\(b(a_*,\xi)=b(0,\xi)\). It is not used to erase any interior
cycle. Every hole has coefficient \(+1\) because it has negative
orientation in \(\partial\Omega_\rho\) and (8) has a minus sign.
There is no assumption that a hole contribution is a residue at
one simple pole or a geometric thimble.

The initial integral has the exact expression
\[
 U_R(h_N,1)=\frac{N}{2\pi}\int_0^r
                  e^{-Nt/(2\pi)}b(0,it)\,dt .
 \tag{18}
\]
It is bounded uniformly in \(N\). Since \(b(0,0)=1\) and its
first derivative is bounded on this compact segment,
\[
 U_R(h_N,1)=1+O(N^{-1})+O(e^{-Nr/(2\pi)}).
 \tag{19}
\]
All constants in this section may depend on the fixed braid,
chosen contours, and fixed \(r\), but not on \(N\).

The outer term is exponentially small. If \(v=x+iy\in C_\rho\),
then
\[
 |v|^2=2\pi y+\rho^2-\pi^2,\qquad
 \max_{C_\rho}\Re\frac{i}{v}=\frac1{\rho+\pi}.
 \tag{20}
\]
For example \(y/(2\pi y+\rho^2-\pi^2)\) is increasing on the
circle's range of \(y\), so its maximum is at \(v=i(\pi+\rho)\).
Also \(|v|,|v-a_*|\ge\rho-\pi\).
Using \(\xi=it\) and the literal exponent in (6), one obtains
\[
\begin{split}
 |\mathcal E_{N,r}(C_\rho)|
 &\le \frac{NM\rho}{(\rho-\pi)^2}
       \int_0^r
       \exp\!\left\{N\left(\frac{r-t}{\rho+\pi}
                                    -\frac r{2\pi}\right)\right\}dt\\
 &\le \frac{M\rho(\rho+\pi)}{(\rho-\pi)^2}
                         e^{-\gamma_\rho rN},\\
 \gamma_\rho&=\frac1{2\pi}-\frac1{\rho+\pi}>0.
\end{split}                                                    \tag{21}
\]
The primitive in \(t\) cancels the factor \(N\). This estimate
does not take absolute values of the hole terms in (17).

Thus (17) gives the constructed short-cutoff form
\[
 C_N(q_N)=1+e^{-R/h_N}A_N(h_N,R)
              +\sum_\nu\mathcal E_{N,r}(C_\nu)
              +O(N^{-1})+O(e^{-\gamma_\rho rN}).
 \tag{22}
\]
The scalar endpoint in (22) is retained exactly. At this short
cutoff it need not be small. If there are no Alexander roots,
the hole sum is empty; this does not discard that scalar term.
No pole multiplicity, positivity, or local node test was required.

## 4. Continued cuts and moving meridian boundaries

There is a precise extension of the identity, but not an automatic
construction of its source. Suppose a finite continued Borel path
is supplied with a common meridian corridor joining \(0\) to \(a\).
In each \(\xi\)-fiber suppose the chosen source is single-valued
and holomorphic on a bounded cut domain \(\Omega_\xi\) containing
that corridor, with continuous piecewise smooth boundary chains,
uniformly separated from the corridor. Assume the source and
boundary integrals have finite bounds on this compact family.
Joint analytic neighborhoods on the retained sheets are required
along the corridor and boundary chains. Their histories are those
continued from the original germ.

Cauchy's formula can then be applied inside each primitive integral
in (10). The same exact calculation proves
\[
 K_L=\frac{L}{2\pi i}\int_\gamma d\xi
          \int_{\partial\Omega_\xi}
             \frac{e^{L(R-\xi)/v}b(v,\xi)}{v(v-a)}\,dv .
 \tag{23}
\]
This includes moving holes and cut banks. No derivative of a moving
boundary is being silently dropped: (23) is Cauchy's identity in
each fixed fiber followed by a finite integral. Equivalently the
mixed displacement term in \(dv\wedge d\xi\) vanishes on pullback.
Deforming these chains *through* singularities is a different
operation and is not permitted by (23).

To specify the signs, orient a cut \(\sigma\) arbitrarily and denote
its boundary values by \(b_{\rm left},b_{\rm right}\), relative to
that orientation. The positively oriented cut boundary has the left
bank forward and the right bank backward. Its contribution to \(K_L\)
is therefore
\[
 \frac{L}{2\pi i}\int_\gamma d\xi\int_{\sigma_\xi}
  \frac{e^{L(R-\xi)/v}
          (b_{\rm left}-b_{\rm right})(v,\xi)}{v(v-a)}\,dv .
 \tag{24}
\]
Holes give minus their counterclockwise integrals in \(K_L\).
The signs of all these contributions reverse in the color formula
(8): counterclockwise holes have coefficient \(+1\), and cut jumps
have the negative of (24). These are ordinary Cauchy boundary
cycles with the original source values, not substituted principal
symbols or a proposed positive-cycle basis.

For such a continued family the term \(U_\gamma(h,e^a)\) also keeps
its specified branch. A periodicity assertion about formal rational
coefficients alone does not delete a cut-bank difference on a
continued branch. When the two endpoint germs have actually been
continued along the same common \(\xi\)-path from the same
\(Y=1\) germ, their equality follows by uniqueness; even then the
interior boundary terms (23)--(24) remain.

## 5. What the large-cutoff estimate does and does not pay

[E] proves directly from the finite-color polynomial that, for any
prescribed \(\Lambda>0\), one finite \(r\) can be chosen so that
\[
                 |e^{-ir/h_N}A_N(h_N,ir)|\le e^{-\Lambda N}
 \tag{25}
\]
for all sufficiently large \(N\). This is the same \(A_N\) as in
(17), with every source normalization retained.

The short \(r_0\) constructed in Section 3 is not asserted to exceed
that choice. To use (25) together with (23), one must construct the
canonical source on the requisite finite Borel path and retain its
meridian boundary chains. Even if such a construction keeps a bounded
source on the outer circle for the straight path, so that (21)
continues to apply, the interior hole and cut contributions remain
in the exact color formula. They have not been bounded or identified
with a selected geometric contribution here.

The unconditional result is (17)--(22), for an actual common short
cutoff and all physical levels. The new source operation is the
exact integration of the shift semigroup into (6), with its
constructed positive hole coefficients and outer loss. No infinite
Laplace contour, nonzero geometric intersection, complete-source
lower bound, or arbitrary-short-filling conclusion follows.

## 6. Complete proof sources and coverage

| Label | Complete source | SHA256 |
|---|---|---|
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |
| G | notes/research_classical_verma_borel_pole_profile.md | 6ba957d7a521524f370cb3bdd90ab30338bff8c13960ae6ca1825d08260c77d2 |
| E | notes/research_scalar_color_endpoint_large_cutoff_bound.md | 02d37d7334ca4d585d8b9e2387862b3384f3fa2dfa4259031d6a082151571384 |

B supplies the literal semigroup, finite-primitive transport, and
original fixed-color restriction. G supplies only the rational
coefficients and compact-meridian Borel germ, without its optional
node assumptions. E supplies the entire scalar endpoint and (25).
The previous uniform small-meridian comparison bounds the same
semigroup on an initial disk; it does not contain the integrated
Cauchy kernel or the complete-color hole decomposition above.
All new contour identities and estimates are proved here. Only
written mathematics and source-text reads were used. Frozen notes
and public manuscripts are unchanged.
