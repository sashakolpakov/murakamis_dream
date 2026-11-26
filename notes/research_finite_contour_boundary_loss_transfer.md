# Boundary loss from an exact finite contour and its endpoint profiles

Private written deduction, 10 November 2026. A contour estimate at
complete boundary colors can sometimes supply the whole boundary estimate
without a new outside-angle cover. The relevant input is an absolute
estimate for the actual finite representation, not the value of its
possibly cancelling integral at completeness. This note gives an explicit
test for the omitted original rows, including rows above one half.

The retained-contour mechanism is already stated in the uniform factorial
theorem and in Section 5, Corollary 4, of the endpoint-extension criterion.
That corollary assumes an all-real bound for the omitted source. The
additional deduction here replaces that assumption by a complete-color
absolute profile comparison with a specified high-row cost. It allows
any fixed number of free boundaries, all original aliases and caps, and
both level parities. It does not construct a geometric contour for an
arbitrary short-filled component.

No mathematical numerical evaluation or frozen-source edit is used.

## 1. The two boundary factors and the exact high-row cost

Retain the original Newton polynomials
\[
 D=N-1,\qquad
 e_j(w)=S_j^{-2}\prod_{\ell<j}(c_\ell-w),\quad
 c_\ell=2\cos((2\ell+1)\pi/N),\quad
 S_j=\prod_{\ell=1}^j2\sin(\pi\ell/N).
 \tag{1}
\]
Put \(d(\theta)=1-\cos\theta\). With the original real primitive
\(J(x)=\int_0^x\log(2\sin\pi t)\,dt\), write
\[
 \begin{split}
 V_\theta(x)&=
 \int_{\theta/(2\pi)-x}^{\theta/(2\pi)+x}
                 \log(2|\cos\pi t|)\,dt-2J(x),\\
 \chi(x)&=
 \begin{cases}
 0,&0\le x\le1/2,\\
 V_0(1-x),&1/2<x\le1 .
 \end{cases}
 \end{split}                                                    \tag{2}
\]
The all-row real Newton theorem gives, uniformly in every original
integer row and every real \(|\theta|\le\pi\),
\[
 |e_j(-2\cos\theta)|\le CN^A e^{NV_\theta(j/N)},\qquad
 0\le V_\theta(x)\le V_0(x)\quad(0\le x\le1/2),\quad
 V_\theta(1-x)=-V_\theta(x).
 \tag{3}
\]
Consequently
\[
 \boxed{\quad V_\theta(x)\le V_0(x)+\chi(x),\qquad0\le x\le1.\quad}
 \tag{4}
\]
This is a bound by the complete-color *entropy*, not by the finite
number \(e_j(-2)\). No division by that number is made.

For \(x>1/2\), the cost in (4) is sharp at the level of these
profiles. Indeed
\[
 V_\pi(x)=0,\qquad
 \sup_{|\theta|\le\pi}\{V_\theta(x)-V_0(x)\}
                  =-V_0(x)=V_0(1-x)=\chi(x).
 \tag{5}
\]
The first identity follows by shifting the integral in (2) by
\(1/2\), which makes it \(2J(x)\). The second follows from
(3), since \(V_\theta(x)\le0\) above one half. In particular a
complete-color profile which uses a negative upper-half Newton
entropy cannot retain that favorable entropy at every real color.
At the midpoint \(\chi(1/2)=0\). At the true index ends, the
uniform estimate (3), rather than an interior factorial expansion,
is the input.

The original factorial boundary interpolation is
\[
 B_N(x,\theta)=
 \frac{N}{
 G_N(N(1/2-x+\theta/(2\pi))-1/2)
 G_N(N(1/2-x-\theta/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{6}
\]
Its value at \(x=j/N\) is exactly (1). Let
\[
 \mathcal X=\{x:\alpha\le\Re x\le\beta,\ |\Im x|\le H\},
 \qquad0<\alpha<\beta<1/2,\quad H<\infty .
 \tag{7}
\]
At zero boundary angle put
\[
 b(x,0)=-2J(1/2-x)-2J(x).
\]
The original branches are holomorphic on a neighborhood of (7).
The uniform factorial theorem proves
\[
 |B_N(x,\theta)|\le CN^A
  e^{N\{\Re b(x,0)-c_0d(\theta)\}},\qquad
 c_0=\min_{\mathcal X}
       \frac{\sin(2\pi\Re x)}{4\pi\cosh^2(\pi\Im x)}>0 .
 \tag{8}
\]
Both reciprocal reflection terms and all moving zeros remain in
this bound. In particular it applies to both signs of the wire
height and to intermediate heights on a cap.

There is a second possible *literal* boundary factor. The canonical
ordinary polynomial
\[
 \widetilde B_N(x,w)
  =\sum_{j=0}^{D}
       \frac{\sin(\pi N(x-j/N))}
            {N\sin(\pi(x-j/N))}\,e_j(w)
 \tag{9}
\]
obeys a bound of the same form as (8), with a possibly smaller
positive coefficient, by the free-boundary cardinal comparison.
It also has the same nonzero local factorial phase.
The two functions (6) and (9) are not identified as ordinary
functions merely because they agree in the physical quotient.
The representation used below must specify which one actually
occurs.

For either permitted factor \(\mathcal B_N\), the same sources
give constants \(c_{\mathcal X},B_{\mathcal X},h_{\mathcal X}>0\)
such that
\[
 |\mathcal B_N(x,a+iv)|
 \le CN^A e^{N\{\Re b(x,0)
                 -c_{\mathcal X}d(a)+B_{\mathcal X}v^2\}},
 \quad |a|\le\pi,\quad |v|\le h_{\mathcal X}.
 \tag{10}
\]
For (9) its second argument in (10) means evaluation at
\(-2\cos(a+iv)\). For (6), this is the strip estimate proved
before Fourier projection in Section 2 of that comparison.
One may use a slightly larger rectangle than (7) throughout.
Then any fixed index derivatives of these factors have the same
real exponents at polynomial cost: apply Cauchy's formula on
index disks of radius \(N^{-1}\). The analytic zero-angle
exponent changes by \(O(N^{-1})\), and a common angular coefficient
is chosen on the larger rectangle. Thus first normals expanded
by the product rule do not require division by a boundary factor.

## 2. A complete finite-source criterion

Let \(F_N(w_1,\ldots,w_r)\) be an original finite boundary
polynomial, with separate degrees at most \(d_bN\), where
\(r,d_b\) are fixed. Suppose there is an exact decomposition
\[
 F_N(-2\cos\boldsymbol\theta)
   =\mathcal I_N(\boldsymbol\theta)
      +\sum_{a=1}^{A_0}\mathcal R_{a,N}(\boldsymbol\theta).
 \tag{11}
\]
The number \(A_0\) is fixed; polynomially many individual rows
may occur inside each group. All cuts and contours are chosen
independently of the free boundary colors. Every term of the
original full trace must occur in (11), with its original scalar
and orientation. This includes aliases represented by their full
rational denominators, connecting caps, omitted physical rows,
double-root normals and the odd simple-node contribution.

Here are sufficient, boundary-angle-independent tests.

**Retained currents.** The exact \(\mathcal I_N\) is a sum of
currents
\[
 \sum_\ell\int_{\Gamma_{\ell,N}}
 a_{\ell,N}(z)
 \prod_{\nu\in I_\ell}
       \mathcal B_{\ell,\nu,N}
          (x_{\ell,\nu}(z),\theta_{b(\ell,\nu)})\,d\mu_{\ell,N}(z).
 \tag{12}
\]
Each factor is literally one of (6),(9), its index lies in a
fixed compact set of the form (7), and each free boundary
\(b\in\{1,\ldots,r\}\) occurs at least once in every current.
There are boundedly many factors per current. Fixed derivatives
in the index variables may be included as explained after (10).
The coefficients and measures are independent of the free colors;
they include every original crossing, residue coefficient and
alias denominator.

Require the weighted **absolute** complete-color estimate
\[
 \sum_\ell\int_{\Gamma_{\ell,N}}|a_{\ell,N}(z)|
  \exp\!\left\{N\sum_{\nu\in I_\ell}
                         \Re b(x_{\ell,\nu}(z),0)\right\}
                 d|\mu_{\ell,N}|(z)
       \le CN^A e^{NM}.
 \tag{13}
\]
All polynomial factors from (8)--(10) and index derivatives
may be included by increasing \(A\). In particular (13) is
not inferred from \(|\mathcal I_N(\mathbf0)|\le CN^Ae^{NM}\).

**Omitted source groups.** Each \(\mathcal R_{a,N}\) is an
ordinary polynomial of separate degrees \(O(N)\). Its exact
finite representation may contain physical boundary factors
\(e_{j_\nu}(-2\cos\theta_{b(\nu)})\), \(0\le j_\nu<N\),
and compact factors (6) or (9). All other factors are
independent of the free colors. Fixed first normals are
expanded in that representation before estimating it.
The number of boundary factors and the orders of these
derivatives are bounded independently of \(N\), as they
are for a fixed original tangle.

For such a term let its complete-color boundary exponent be
\[
 H_a(z,\mathbf j)
    =\sum_{\nu\ {\rm physical}}V_0(j_\nu/N)
       +\sum_{\nu\ {\rm compact}}\Re b(x_\nu(z),0),
 \qquad
 X_a(\mathbf j)=\sum_{\nu\ {\rm physical}}\chi(j_\nu/N).
 \tag{14}
\]
Require, with some fixed \(\delta_a>0\),
\[
 \sum_{\mathbf j}\int
       |a_{a,N}(z,\mathbf j)|
            e^{N\{H_a(z,\mathbf j)+X_a(\mathbf j)\}}\,d|\mu|
        \le CN^A e^{N(M-\delta_a)} .
 \tag{15}
\]
The finite sums, prefactors and measures in (15) are those of
the actual group. No sign is assigned to their original values.
A common way to verify (15) is a complete-color pointwise
profile certificate
\[
 |a_{a,N}|e^{NH_a}\le CN^A e^{N\{M-g_a(z,\mathbf j)\}},
 \qquad
 g_a(z,\mathbf j)-X_a(\mathbf j)\ge\delta_a>0,
 \tag{16}
\]
with polynomial total counting and measure cost.
Thus the only additional profile charge in (16) is the explicit
function (2). In (15)--(16), \(a_{a,N}\) is bounded separately
from the free-color Newton factors. The function \(g_a\) is
certified for this coefficient majorant times the displayed
entropy exponential, not defined by taking a logarithm of
the literal complete-color summand. A zero of that summand
therefore gives no improvement of \(g_a\).
If every free physical row of the omitted group
is at or below one half, \(X_a=0\): its old absolute profile gap
already proves (15). This includes exact midpoint rows at the
two parities; a complete-color zero is never deleted on that basis.

**Theorem 1.** Under (11)--(15), there are \(c,B,h>0\) and
polynomial prefactors such that the complete original source has
\[
 |F_N(-2\cos\boldsymbol\theta)|
 \le CN^A e^{N\{M-c\sum_{b=1}^r d(\theta_b)\}}
 \quad(\boldsymbol\theta\in[-\pi,\pi]^r),
 \tag{17}
\]
and
\[
 |F_N(-2\cos(\mathbf x+i\mathbf y))|
 \le C'N^{A'}e^{N\{M-c'\sum_b d(x_b)+B\|\mathbf y\|_2^2\}}
 \quad(\mathbf x\in[-\pi,\pi]^r,\ |y_b|\le h).
 \tag{18}
\]
Both parities and all fixed ordinary boundary derivatives in
(17) are included, at polynomial cost. No lower bound or
nonzero coefficient for a signed source follows from this theorem.

*Proof.* Every current in (12) has a factor for each free
boundary. Equations (8),(13) therefore give, for some common
\(c_I>0\),
\[
 |\mathcal I_N(\boldsymbol\theta)|
 \le CN^Ae^{N\{M-c_I\sum_b d(\theta_b)\}}.
 \tag{19}
\]
Equations (3),(4),(8) prove directly from (15) that
\[
 \sup_{\boldsymbol\theta\in[-\pi,\pi]^r}
 |\mathcal R_{a,N}(\boldsymbol\theta)|
                  \le CN^Ae^{N(M-\delta_a)}.
 \tag{20}
\]
Use \(0\le\sum_bd(\theta_b)\le2r\), and take
\(c\le\min(c_I,\min_a\delta_a/(2r))\). Summing (19),(20)
proves (17). It uses the absolute original representation
throughout, so cancellation between aliases or endpoint rows
is not assumed.

For the strip, (10),(13) already give (18) for the retained
currents. Each omitted group is separately a genuine polynomial.
Tensor Laurent/Chebyshev continuation of (20), with separate
degree at most \(d_{a,b}N\), costs
\(\sum_b d_{a,b}|y_b|\) in its exponential rate and only a
polynomial prefactor. Choose \(h>0\) so this is at most
\(\delta_a/4\) for every group, and choose
\(c'\le\min(c_I,\min_a\delta_a/(8r))\), also below the
coefficient available from (10).
The surviving gap \(3\delta_a/4\) in each omitted group
absorbs the desired angular loss, which is at most
\(\delta_a/4\). This proves (18).

For fixed ordinary derivatives on the real cube, one can
use the sharper real bound (17) rather than spend its gap.
In each variable set \(z=e^{i\theta}\), let \(D_{b,N}\le d_bN\)
be the Laurent degree, and apply the maximum principle to
\[
 z^{D_{b,N}}F_N\,e^{-Ncz}.
 \tag{21}
\]
On the unit circle the \(b\)-th angular loss is cancelled
by the real part of \(-Ncz\); all other angular losses are
retained. Iteration in the boundary variables and separate
evenness give a linear height cost at most
\(\sum_b(d_b+c)|y_b|\), with the real angular losses unchanged.
An ordinary polydisk of radius \(N^{-2}\) about any real
spectral point changes each inverse-cosine angle by
\(O(N^{-1})\), uniformly at the two quadratic branch points
as well. The corresponding real-angle change also changes
each \(d(x_b)\) by \(O(N^{-1})\). Its total rate cost is
\(O(N^{-1})\).
Cauchy's formula gives only a fixed power of \(N\) for
every fixed ordinary multi-derivative. This proves the
derivative assertion without division by a possibly zero
factor. \(\square\)

## 3. Profile maxima and positive norm estimates

The endpoint test does not require a single uniform gap before
the known high-row cost is inserted. Suppose a complete-color
majorant has rate \(P(z,\mathbf x)\), with physical indices
\(\mathbf x=\mathbf j/N\). Then the relevant all-real omitted
profile is exactly bounded by
\[
             P(z,\mathbf x)+\sum_\nu\chi(x_\nu).
 \tag{22}
\]
It suffices that its supremum is strictly smaller than the
selected retained rate \(M\). The profile and the correction
must belong to the same finite source; a bound for one signed
contracted coefficient cannot be assigned to its positive
termwise majorant.

The same argument applies inside a positive norm estimate.
For example, let
\[
 Y_N(\boldsymbol\theta)
  =\left(\sum_j w_{j,N}|C_{j,N}(\boldsymbol\theta)|^p\right)^{1/p},
 \qquad1\le p<\infty,\quad w_{j,N}\ge0 ,
 \tag{23}
\]
where \(p\) is fixed and the weights are independent of the
free colors. Suppose that on a compact central index set
the actual factors obey
\[
 w_{j,N}^{1/p}|C_{j,N}(\boldsymbol\theta)|
 \le CN^A e^{N\{P(j/N)-c_I\sum_b d(\theta_b)\}},
 \qquad P\le M,
 \tag{24}
\]
and the remaining weighted quantities
\(w_{j,N}^{1/p}C_{j,N}\) have the endpoint test
(15), or the corresponding uniform bound \(M-\delta\), after
their own known high-row charges. If there are polynomially
many rows, summation and the \(p\)-th root show
\[
 Y_N(\boldsymbol\theta)
 \le CN^{A'}e^{N\{M-c\sum_b d(\theta_b)\}},
 \quad0<c\le\min(c_I,\delta/(2r)).
 \tag{25}
\]
This follows by applying (19)--(20) before taking the
positive sum; there is no further exponential cost.
It is the profile mechanism used for the all-real complete
column bound. It does not assert that a crossing matrix,
a Gram coefficient or an original Hermite pairing is positive.
If Cauchy--Schwarz produced (23), that preceding inequality
and all its metric factors must be retained.

## 4. What a local geometric packet additionally gives

Theorem 1 needs no nonzero saddle. If a source separately has
a proved original local Gaussian, its boundary Hessian has
a useful automatic form under the factorization above.
Suppose its leading phase near the selected internal point
\(z_*\) is
\[
 \mathcal F(z,\boldsymbol\theta)
   =\mathcal F_{\rm int}(z)
        +\sum_\nu b(x_\nu(z),\theta_{b(\nu)}),
 \tag{26}
\]
with all selected \(x_\nu(z_*)\) strictly in (7), and its
internal Hessian invertible. Each boundary occurs at least
once, and (26) contains every boundary-dependent term of
the leading phase. The original logarithms and additive constant are
fixed, and the actual local symbol and Gaussian coefficient
are assumed nonzero. These are additional source hypotheses,
not consequences of an upper estimate.

The implicit critical point \(z_*(\boldsymbol\theta)\)
exists near zero. Since every boundary factor is separately
even, \(\mathcal F_{z\theta_b}(z,\mathbf0)=0\);
hence \(\partial_{\theta_b}z_*(\mathbf0)=0\). For the
stationary phase \(W(\boldsymbol\theta)\), the exact derivative
of the same boundary primitive gives
\[
 \boxed{\quad
 W_{\theta_b\theta_c}(\mathbf0)
   =-\frac{\delta_{bc}}{2\pi}
          \sum_{\nu:\,b(\nu)=b}\tan(\pi x_\nu(z_*)).
 \quad}                                                         \tag{27}
\]
Indeed \(b_{\theta\theta}(x,0)=-\tan(\pi x)/(2\pi)\);
the internal critical drift contributes zero at this order.
For \(x=\xi+ih\) in (7),
\[
 \Re\tan(\pi x)
   =\frac{\sin(2\pi\xi)}
          {\cosh(2\pi h)+\cos(2\pi\xi)}>0 .
 \tag{28}
\]
Thus (27) has strictly negative real part. This supplies
the boundary curvature required by the existing kernel
closure theorem whenever the actual nonzero local packet
and exact normalization have been established.

If only the real conclusion (17) is needed from the
transplant, that local packet and (27) alternatively give
(18) by the general local-packet/real-gap lemma. Neither
route chooses a contributing cycle or proves that distinct
local coefficients fail to cancel.

## 5. Scope and failures of the automatic inference

The theorem removes a separate all-real boundary cover for
the following class: sources with a complete exact contour
inventory satisfying (12)--(13), low-strip boundary coverage
on every rate-\(M\) current, and omitted absolute profiles
which pass the explicit test (15) or (16). These conditions
are independent of the boundary angles being estimated.
They do not assert that an arbitrary short-filled tangle has
such an inventory or such a selected-rate absolute ceiling.

Three distinctions are necessary.

1. A small signed complete-color value is not (13) or (16).
   At odd levels high Newton rows can vanish at \(-2\) but
   be nonzero at other real colors. A value-only deletion
   therefore supplies no admissible endpoint certificate.
2. A low-strip condition cannot be extended around a full
   index circle without proof. The canonical comparison
   already shows at \(x=3/4\), \(N=4m+2\), a highest Fourier
   coefficient of magnitude at least \(N^{-3}\), whereas
   its complete factorial rate is \(4J(1/4)<0\). Thus even
   an angular-loss-free bound at that negative rate fails.
   Formula (5) describes the related physical-row cost
   exactly; it cannot simply be omitted.
3. The finite identity must remain valid at arbitrary free
   colors, including original normal data. Agreement in the
   physical quotient does not license replacing (9) by
   (6) on an unrestricted free boundary. Nor may caps or
   full rational aliases be suppressed because their
   complete-color sum is small.

The recently proved inner-three boundary theorem is an
instance with compact retained factorial paths, below-half
physical endpoint rows and separately paid all-real
restorations. The all-real column theorem uses (23)--(25)
after its actual cap estimates and true endpoint profiles.
Those source-specific checks remain essential. No theorem
for arbitrary adjacent short components, no signed overlap
lower bound, and no finite-exception conclusion is inferred
here.

## Frozen direct sources

| Source | SHA-256 |
|---|---|
| research_uniform_factorial_and_boundary_decay.md | 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11 |
| research_mixed_newton_color_tubes.md | 61f5d6ffe8571bf309c75cd3c74d8ffefedf997095aac7347cbbcc64e0a8c57d |
| research_free_boundary_cardinal_factorial_comparison.md | 9ed5b69bad33d7e62a7b40070d86d9d2233f2c34bc7674ddcf8a82e8e0091d5d |
| research_mixed_endpoint_packet_extension_criterion.md | 1c8dbffa027dda4da39d1e1d2954305520708cc413e1e1ae7bc46a2aa730d8bb |
| research_scaled_wire_contour_lifting.md | b1a9429031499098756b725757f54c46b7fdaa4033845f1dc56fa162ec80aa10 |
| research_mixed_open_source_stability_reduction.md | 5d501024dddb98ff28f1ae3d44110d4a34bfc82d8063ff01353315c3efbfc31c |
| research_mixed_symmetric_closing_incoming_angular_decay.md | 4fa4776cf2bd2f153be257c9e2c5aecc09d92f5e551073e9c3ce62e75dc7dd4e |
| research_mixed_symmetric_closing_all_real_column_bounds.md | 02a134c219a5da365316de633e9edc407fbcc3de512d0474888bf8722b1f1059 |
