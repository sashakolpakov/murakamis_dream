# Growth contacts of the actual regularized meridian period

Research deduction, 6 November 2026. For every fixed zero-framed knot,
the existing exact finite source supplies a fixed finite-order meridian
equation for its whole regularized period. Its affine source has
polynomial growth, and its primitive principal symbol is nonzero.
An elementary bound on the original crossing products also gives a
locally uniform exponential upper bound for this period, including
across the ordinary-color quotient roots. Consequently every finite
first-order upper contact of its positive joint complex growth envelope
is characteristic for the actual operator. No WKB decomposition or
quantum-A identification is a premise.

## 1. The actual operator and the exact affine equation

Fix a braid presentation of a zero-framed knot. Use the original
root, squared meridian and reduced period from the
[regular-period theorem](regularized_kashaev_period.md):
\[
 q_N=e^{\pi i/N},\quad Q_N=q_N^2,\quad Y=M^2,\qquad
 F_N(Y)=S_N(Y)R_N(Y)+P_N(Y),\quad
 S_N(Y)=1+Y+\cdots+Y^{N-1}.
\tag{1}
\]
Here \(F_N,R_N\) are Laurent polynomials. The polynomial \(P_N\)
of degree at most \(N-2\) interpolates the actual ordinary colors
at all \(Y=Q_N^j\), \(1\le j<N\). Set
\(p_N=P_N/S_N\), and write \(b\) for the fixed braid strand count.
That theorem proves
\[
 D_N\le(N/2)^{b-1},\qquad
 |[Y^r]P_N|\le2D_N,\qquad
 |[Y^r]p_N|\le2D_N\quad(r\ge0).
\tag{2}
\]
The last expression is the Taylor coefficient at zero of the proper
polar function; it is not a polynomial truncation.

The [finite-sum annihilator proof](finite_sum_annihilator.md) establishes
existence of an actual nonzero all-level operator for \(F_N\).
Its filtered elimination has order independent of \(N\). It includes
every boundary stratum of the zero-extended finite array, uses finite
moments if direct summation kills an eliminating operator, and removes
a common central factor before the root specialization. Thus existence
does not assume an AJ theorem or discard a summation endpoint.
The [squared-meridian construction](even_meridian_norm_descent.md),
Section 2, also permits such an operator over \(\mathbb Q(Q,Y)\).

For the present application choose the already constructed primitive
minimal **normal-state** operator from
[actual Weyl descent](actual_weyl_descent.md), Sections 2--3:
\[
 B(q,Y,T)=\sum_{j=0}^d b_j(q,Y)T^j,\qquad
 TY=q^2YT,\qquad
 b_j\in\mathbb C[q^{\pm1},Y^{\pm1}],\quad
 \gcd(b_0,\ldots,b_d)=1.
\tag{3}
\]
Its order \(d>0\) is fixed for the knot. It annihilates the actual
normal state \(v_N=(Y-1)F_N\) at every sufficiently large level.
This is an existence and exact-identity result; no efficient formula
for the least-order coefficients of an arbitrary knot is asserted.

At the root, \(U=Y^N\) is invariant under \(T\), and
\[
 \frac{F_N}{S_N}=\frac{v_N}{U-1}=R_N+p_N.
\tag{4}
\]
Therefore the same operator, with no additional meridian gauge, gives
the exact whole-germ equation
\[
 B(q_N,Y,T)R_N=\beta_N(Y),\qquad
                 \beta_N=-B(q_N,Y,T)p_N.
\tag{5}
\]
The division by \(U-1\) is first a rational identity; (5) then holds
at every finite nonzero meridian by the Laurent continuation of its
left side. The poles of the individual shifted \(p_N\)'s cancel in
their complete combination. They have not been dropped.

If the Laurent supports of the coefficients in (3) lie in
\([r_-,r_+]\), then
\[
 \beta_N\in\operatorname{span}\{Y^r:r_-\le r\le r_+-1\},
 \qquad |[Y^r]\beta_N|\le C_B D_N.
\tag{6}
\]
Indeed (5) makes \(\beta_N\) Laurent polynomial. Each shifted
\(p_N\) is regular at zero and is \(O(Y^{-1})\) at infinity,
which gives its two support endpoints. Its coefficients are bounded
using (2), the fixed number of coefficient monomials in (3), and
\(|Q_N|=1\). In particular \(\beta_N\) has joint exponential
growth at most zero on every compact subset of \(\mathbb C^*\).
The source coefficients need not be specializations of one rational
function of \(q,Y\); that extra claim is unnecessary here.

Primitivity supplies a stable, nonzero principal polynomial:
\[
 B_{\rm cl}(Y,L)=\sum_{j=0}^d b_j(1,Y)L^j\ne0.
\tag{7}
\]
Otherwise \(q-1\) would divide every coefficient in (3).
On fixed meridian compacts, \(b_j(q_N,Y)=b_j(1,Y)+O(N^{-1})\)
with all fixed holomorphic derivatives. The specialized degree in
\(L\) can be smaller than \(d\). Nor does (7) assert that
\(B_{\rm cl}(1,L)\) is nonzero as a polynomial in \(L\).

## 2. A finite local growth bound from the original crossing weights

For clarity, this bound concerns the complete original finite sum;
it is not obtained from cancellation in a selected sector. Put
\[
 \mathcal P_k=\prod_{j=1}^k|1-Q_N^j|,\qquad 0\le k<N.
\tag{8}
\]
Uniformly in this entire range,
\[
                  \mathcal P_k\le2^N,\qquad
                  \mathcal P_k^{-1}\le2^N.
\tag{9}
\]
Indeed the full cyclotomic product has modulus \(N\), and
\(|1-Q_N^{N-j}|=|1-Q_N^j|\). Thus for every \(0\le k<N\),
\(\mathcal P_k\mathcal P_{N-1-k}=N\), and more precisely
\(\mathcal P_k^{-1}=\mathcal P_{N-1-k}/N
\le2^{N-1-k}/N\). The direct upper bound uses only
\(|1-Q_N^j|\le2\). No factor with index \(N\) is inverted.

The exact positive and negative crossing formulas in
[the relative octahedral source](relative_octahedral_period.md),
equations (1.1)--(1.2), are monomials times
\[
 \frac{(Q_N;Q_N)_a}
      {(Q_N;Q_N)_k(Q_N;Q_N)_{a-k}}
                   (YQ_N^{-a};Q_N)_k
\tag{10}
\]
or the identical expression with the other input index.
All factorial lengths are below \(N\). The crossing derivation
has already canceled the apparent powers of \(q-q^{-1}\);
no inverse of such a scalar is raised to an uncontrolled growing
power in (10). On a compact meridian annulus the last product is
bounded by \((1+\sup|Y|)^N\). The remaining meridian monomial
has exponent \(O(N)\), and the root phases have modulus one.
The same statements hold for the fixed pivotal and framing factors.

There are finitely many crossings and contractions, fixed before the
level varies, and at most a fixed power of \(N\) finite index states.
Equations (9)--(10) therefore prove, on every compact annulus,
\[
                    |F_N(Y)|\le C N^a e^{C' N}
\tag{11}
\]
for constants depending on the braid and annulus. Zeros of an
external Pochhammer factor cause no difficulty for this upper bound.
The state is even in \(M\), so choosing either square root when
estimating the original monomials gives the same function of \(Y\).

This also bounds \(R_N\) across the dense ordinary-color orbit.
Given a compact subset of \(\mathbb C^*\), enclose it in an annulus
whose boundary radii satisfy \(0<\rho<1<\mathcal R\). On these
two circles, respectively,
\[
 |S_N(Y)|\ge1-\rho,\qquad |S_N(Y)|\ge\mathcal R-1
                    \quad(N\ge2).
\tag{12}
\]
Use \(S_N=(Y^N-1)/(Y-1)\) to obtain these bounds. Equation (2)
bounds \(P_N\) exponentially on the same circles. Thus (1) and
(11) give an exponential bound for \(R_N\) on both boundaries.
The Laurent polynomial \(R_N\) is holomorphic throughout the
annulus, so the maximum principle extends it across every root of
\(S_N\). Consequently
\[
 \text{for every compact }K\Subset\mathbb C^*,\qquad
                 \sup_K|R_N|\le C_K N^{a_K}e^{C_K' N}.
\tag{13}
\]
There is no pointwise division estimate at an ordinary-color zero.

## 3. The actual characteristic constraint on positive growth

Choose a local logarithmic meridian chart \(Y=e^x\), with complex
coordinate \(x\). Define the joint upper-regularized envelope
\[
 \mathcal U(x)=\lim_{\varepsilon\downarrow0}\limsup_{N\to\infty}
   \sup_{|y-x|<\varepsilon}\frac1N\log|R_N(e^y)|,
                       \qquad \log0=-\infty.
\tag{14}
\]
Equation (13) proves that it is locally bounded above. It need not
be finite everywhere; for example, no assertion of a nonzero
regular remainder for every knot is needed.

**Theorem.** At any point \(x_0\) with finite
\(\mathcal U(x_0)>0\), if there is a first-order upper contact
\[
 \mathcal U(x)\le\mathcal U(x_0)+\Re\{p(x-x_0)\}
                                      +o(|x-x_0|),
\tag{15}
\]
in both real coordinates of this complex chart, then
\[
                 B_{\rm cl}(e^{x_0},e^{2\pi i p})=0.
\tag{16}
\]
In particular this applies at every finite differentiability point
of positive envelope value, with
\(p=\partial_{\Re x}\mathcal U-i\partial_{\Im x}\mathcal U\).

*Proof.* In this chart the \(j\)-th term of (5) shifts by
\(2\pi i j/N\). Its coefficients have the fixed analytic limits
in (7), and the joint source envelope is at most zero by (6).
Apply the [whole-kernel upper-contact theorem](research_quantitative_power_ward_exclusion.md),
Section 7, to the exact whole equation (5). All its finite-growth
and source-separation hypotheses are now supplied by (6), (13),
and \(\mathcal U(x_0)>0\); (15) is its remaining contact hypothesis.
Its symbol is precisely the left side of (16). \(\square\)

**Corollary.** Every point with finite positive \(\mathcal U(x_0)\)
is approached by positive upper-contact points satisfying (16), with
their envelope values converging to \(\mathcal U(x_0)\). No
differentiability assumption at \(x_0\) is required for this statement.

Indeed, on a sufficiently small closed disk of radius \(r\), choose
\(C>0\) with \(Cr^2>\sup_{|x-x_0|\le r}\mathcal U(x)-\mathcal U(x_0)\).
Upper semicontinuity makes \(\mathcal U(x)-C|x-x_0|^2\) attain
its maximum at an interior point \(x_r\). Its value there is at
least its value at \(x_0\), so \(\mathcal U(x_r)\ge\mathcal U(x_0)>0\).
The maximizing inequality gives a quadratic upper support at \(x_r\),
with first-order slope \(p_r=2C\overline{x_r-x_0}\). Apply (16).
As \(r\downarrow0\), \(x_r\to x_0\), and upper semicontinuity
together with the preceding lower bound gives
\(\mathcal U(x_r)\to\mathcal U(x_0)\). This argument supplies
neither bounded contact slopes nor a chosen characteristic branch
at the limiting point.

There is a further local consequence on a region where the actual
envelope is \(C^1\) and positive. Suppose the nonzero roots in \(L\)
of (7) are simple and remain distinct there, with constant degree.
On a sufficiently small simply connected chart they form holomorphic
branches \(L_j(x)\). The continuous function
\(e^{2\pi i p(x)}\), where
\(p=\mathcal U_{\Re x}-i\mathcal U_{\Im x}\), must select one
of these branches by (16). A local holomorphic logarithm then gives
\[
 p(x)=\frac{\Log L_j(x)}{2\pi i}+n,
 \qquad
 \mathcal U(x)=\Re\left\{
       \frac1{2\pi i}\int^x\Log L_j(\xi)\,d\xi+n x\right\}+C,
 \qquad n\in\mathbb Z,\ C\in\mathbb R.
\]
The integer is constant by continuity. The second equality follows
by equality of real differentials, so this \(C^1\) envelope is in
fact harmonic and real analytic on the smaller chart. The integer
is invisible to the principal shift multiplier; at a fixed root,
\(Y^{nN}\) is the corresponding homogeneous difference-constant
character. This observation does not authorize rescaling the actual
affine source or its pointed period. The real constant \(C\) is an
undetermined exponential normalization. Neither the assumed \(C^1\)
regularity nor identification of \(L_j\) as a geometric longitude
is supplied by this corollary.

This is a constraint on the growth of the actual regularized scalar
period, not on an assigned WKB component. It applies on every local
logarithmic chart of \(\mathbb C^*\). If all coefficients of
\(B_{\rm cl}\) vanish at the chosen meridian, the assertion there
can be vacuous. No division by such a meridian factor is performed.
In particular the theorem does not assert a nontrivial longitude
constraint at \(Y=1\) without checking that specialized symbol.

For comparison with the complete value, the exact pointing is
\[
 K_N=F_N(1)=N R_N(1)+P_N(1),\qquad |P_N(1)|\le N D_N.
\tag{17}
\]
A positive exponential subsequential rate for \(K_N\) gives the
same rate for \(R_N(1)\), and hence a positive lower bound for
\(\mathcal U(0)\). This does not provide a first-order upper
contact there, choose a root of (16), or prove that rate.

## 4. Full-state normalization and the limits of the application

The regular full ADO summand is exactly
\(\mathscr R_N(M)=\eta_N M^{N-1}R_N(M^2)\), with
\(|\eta_N|=1\). On \(M=e^m\), its joint envelope is
\[
               \mathscr U(m)=\Re m+\mathcal U(2m).
\tag{18}
\]
The shift \(M\mapsto q_NM\) acts on the displayed monomial by
\(q_N^{N-1}=-q_N^{-1}\). Thus its exact conjugated equation has
coefficients \(b_j(q_N,M^2)(-q_N)^j\) and source
\(\eta_NM^{N-1}\beta_N(M^2)\). Its source envelope is at most
\(\Re m\), not zero. At a finite upper contact with
\(\mathscr U(m)>\Re m\), its characteristic statement is
\[
 B_{\rm cl}(M^2,-e^{\pi i p_m})=0,
                  \qquad d\mathscr U=\Re(p_m\,dm).
\tag{19}
\]
Equations (18)--(19) agree with (16), since
\(p_m=1+2p\). The original monomial and cyclic sign have therefore
not been erased in passing to a regular period.

The [integral-color global model](integral_color_global_q_difference_source.md)
is a different exact statement. Its first-order operators act on
the polynomial head charts of \(\mathcal O(N-1)\), along
\(q_\lambda=e^{\pi i\lambda/N}\), \(M=-q_\lambda^N\).
They are generator actions, not scalar annihilators of the contracted
knot period. Changing the head frame by spectral interpolation can
have order growing with \(N\). Neither that interpolation nor the
polynomial head dimension is used to obtain the fixed order in (3).
After contraction, head Ward identities must still retain the cut,
cup, cap and boundary currents; their vanishing cannot be inferred
from the existence of the head realization.

Likewise that simultaneous quotient path has derivative
\(d\log M=N\,d\log q\). It is not the fixed-root meridian chart
used in (14). Its literal auxiliary pivot and its ordinary closure
require the recorded off-root route adapter. The rootwise operator
(3) has not been asserted to annihilate either scalar all along
that off-root path. In the scaled coordinate \(N\log Y\), its
shifts are fixed rather than of size \(1/N\), so the contact theorem
must not be reapplied there with the same semiclassical symbol.

Finally, (7) and (16) do not identify \(B_{\rm cl}\) with a knot
A-polynomial or a colored-Jones AJ specialization. The original
meridian shift is a proved peripheral insertion, but survival of
the desired geometric component in the annihilator and calibration
of the selected growth are separate assertions. No nonzero saddle
coefficient, volume comparison, outside-color stability, or finite
exception theorem follows from characteristicity alone.

## 5. Comparison with the whole reduced meridian family

Define \(\mathcal U_F\) by (14) with \(F_N\) in place of
\(R_N\), and put
\[
                         \varphi(x)=\max(0,\Re x).
\tag{20}
\]
Both envelopes are locally bounded above by Section 2. The exact
regularization gives a comparison of their positive growth, including
on the unit circle:
\[
       \boxed{\quad
       \max\{\mathcal U_F(x)-\varphi(x),0\}
                          =\max\{\mathcal U(x),0\}.
       \quad}
\tag{21}
\]
Here the positive part of \(-\infty\) means zero. This is an
identity of joint upper envelopes, not of pointwise limits of the
two finite families.

First suppose \(\Re x\ne0\). On a sufficiently small compact
logarithmic neighborhood, \(S_N(e^x)\) has no zeros and
\[
 \frac1N\log|S_N(e^x)|\longrightarrow\varphi(x)
                                      \quad\hbox{uniformly}.
\tag{22}
\]
This follows from \(S_N=(e^{Nx}-1)/(e^x-1)\). Equation (2)
gives a joint upper rate at most \(\varphi\) for \(P_N(e^x)\).
Apply the triangle inequality both to \(F_N=S_NR_N+P_N\) and
to \(S_NR_N=F_N-P_N\). Their envelope consequences are
\[
 \mathcal U_F\le\max\{\mathcal U+\varphi,\varphi\},
 \qquad
 \mathcal U+\varphi\le\max\{\mathcal U_F,\varphi\}.
\tag{23}
\]
These prove (21) off the unit circle, without assuming that either
family has a pointwise limit.

For \(x_0=it_0\), the forward inequality still gives
\(\mathcal U_F(x_0)\le\max\{\mathcal U(x_0),0\}\):
use \(|S_N(e^x)|\le N e^{N\varphi(x)}\) and then shrink the
neighborhood. The reverse inequality requires whole-function division
across the root orbit, rather than division at individual points.

Fix small \(\delta>0\). Choose real numbers \(t_{N,-},t_{N,+}\)
within \(\pi/N\) of \(t_0-\delta,t_0+\delta\), respectively,
such that
\(Nt_{N,\pm}\in\pi(2\mathbb Z+1)\). Let \(\mathcal Q_N\)
be the rectangle with real sides \(\Re x=\pm\delta\) and
these two horizontal sides. For large \(N\) it contains
\(|x-x_0|\le\delta/2\) and lies in \(|x-x_0|<2\delta\).
On its horizontal sides and vertical sides, respectively,
\[
 \begin{split}
 |e^{Nx}-1|&=1+e^{N\Re x}\ge1,\\
 |e^{Nx}-1|&\ge1-e^{-N\delta}\ge1/2.
 \end{split}
\tag{24}
\]
Consequently \(|S_N(e^x)|^{-1}\le C_\delta\) on the whole
boundary, with \(C_\delta\) independent of \(N\). The numerator
\(|e^x-1|\) in that inverse is bounded on the fixed surrounding
chart. The analytic quotient \(R_N(e^x)\) already exists throughout
the rectangle, so the maximum principle and (2) give
\[
 \sup_{|x-x_0|\le\delta/2}|R_N(e^x)|
 \le C_\delta\left\{
       \sup_{|x-x_0|<2\delta}|F_N(e^x)|
                                  +C N^b e^{N\delta}\right\}.
\tag{25}
\]
All quotient zeros remain inside this exact estimate. Take the
normalized logarithmic limsup and then \(\delta\downarrow0\)
to obtain
\(\mathcal U(x_0)\le\max\{\mathcal U_F(x_0),0\}\).
Together with the forward inequality this proves (21) on the unit
circle. In particular its positive joint rates agree there.

Away from \(\Re x=0\), first-order upper contacts at a positive
branch of (21) transfer in both directions. The affine upper support,
including its \(o(|x-x_0|)\) remainder, stays positive near the
contact point. It therefore also bounds the maximum with zero in
(21). This proves both directions without assuming that the envelope
itself stays positive nearby or is lower semicontinuous.
Their differentials differ by
\(d\varphi=0\) or \(d\varphi=d\Re x\), so their complex
slopes differ by zero or one. Hence
\(e^{2\pi i p}\) is unchanged. The actual characteristic constraint
(16) therefore also holds for these positive-growth contacts of the
original reduced family \(F_N\).

At the unit circle, equality of positive joint values alone does not
transfer a first-order contact across the kink of \(\varphi\).
Nor does it give a pointwise lower bound for \(R_N(1)\), a limit
of \(K_N\), or a selected geometric coefficient. All operator orders
and growth constants above belong to the fixed knot and presentation;
no uniform bound over changing filling words has been established.

## 6. Regularity consequences and the remaining observation

On a disk where the characteristic has constant degree and simple
nonzero holomorphic roots, the contact theorem now implies continuity
of \(V=\max(\mathcal U,0)\). The proof in
[vertical regularity](research_regularized_growth_vertical_regularity.md)
first bounds its vertical upper-test slopes by the finite analytic
functions \(0,\log|L_j|/(2\pi)\). This gives vertical Lipschitz
continuity. Vertical mollification, together with subharmonicity,
then gives horizontal continuity (in fact a local Holder estimate
of exponent \(2/3\)). Consequently the positive locus is open
inside the regular-root region; it need not be assumed open.
Each compact vertical interval has finitely many analytic action
pieces. This last statement concerns individual slices, not a
finite decomposition on a two-dimensional neighborhood.

When the roots have a common modulus throughout that neighborhood,
[the common-modulus theorem](research_regularized_growth_single_modulus.md)
does give such a finite decomposition, with the integer logarithmic
translates retained. It proves local finite maxima of harmonic
actions, not a selected single action or its additive constant.
Neither result removes a degenerate characteristic fiber at \(Y=1\).

The [two-modulus theorem](research_regularized_growth_two_moduli.md)
extends the finite harmonic maximum conclusion to two strictly
separated modulus classes. A vertical slice can switch between those
classes only once. Continuity and quantitative buffers turn the pure
parts of that slice into open strips; subharmonicity then controls
their horizontal residuals and integer lifts. The theorem does not
cover a point where distinct modulus functions cross.

For any finite number of roots, the
[null-support theorem](research_regularized_growth_null_riesz_support.md)
proves a weaker but general two-dimensional conclusion. On every
regular-root disk, the support of \(\Delta V\) has area zero.
On each component of its complement, \(V\) is either zero or
the real part of an actual characteristic action, with one fixed
integer logarithmic lift and one additive real constant. The proof
includes modulus crossings and the zero-growth locus. It does not
bound the integers or constants across components accumulating at
the exceptional set. No finite branch family is inferred there.
Taking the squarefree nonzero classical root set over \(\mathbb C(Y)\)
makes this argument applicable away from finitely many exceptional
meridians even when the original symbol has repeated factors.
Including those isolated fibers gives area-zero Riesz support on
the whole logarithmic meridian plane. This last support statement
does not give continuity or recurrence regularity at those fibers;
no exact quantum factor or peripheral value has been canceled.

The observation required for the knot invariant is separate. The
[exact root-orbit identity](regularized_kashaev_period.md), Sections
5--6, gives
\[
 H_N:=\frac1N\sum_{Y^N=1}|F_N(Y)|^2
      =\frac{|K_N|^2}{N}+O(D_N^2).
\tag{26}
\]
Thus a positive exponential lower bound for this particular norm
would imply a positive exponential lower bound for the complete
value. None of the regularity conclusions above compares nearby
meridian growth to (26). Moreover \(\mathcal U\) is defined with
a limsup over levels: even such a comparison would first recover
a complete-value limsup, whereas the volume limit also requires
an all-level lower-growth argument.

There is a quantitative intermediate observation when both end
coefficients of the actual recurrence satisfy
\(b_0(1,1)b_d(1,1)\ne0\). The
[orbit-jet theorem](research_regularized_orbit_jet_growth.md)
derives a fixed linear Laurent-degree bound from the original
crossings. It then combines Hermite Fourier reconstruction, recurrence
transport and a polynomial localization to show
\[
 \max(0,\mathcal U(0))
 =\sup_{K\ge1}\limsup_{N\to\infty}\frac1N
 \log\!\left(1+
   \max_{\substack{0\le i<d\\0\le r<K}}
   |(N^{-1}Y\partial_Y)^rR_N(Q_N^i)|\right).
\tag{27}
\]
Every prescribed error in the rate is achieved by a finite jet
order independent of the level. Its order may depend on that error.
This retains central aliases and gives actual finite observations
approaching the joint rate. It does not identify the zero-jet value
at \(Y=1\), replace the \(d\) nearby points by a jet at that one
point, or prove that one fixed order attains the supremum.

The [singular-arc extension](research_regularized_singular_orbit_jet_growth.md)
retains vanishing complete-meridian end factors under an explicit
analytic-divisor hypothesis. Its rate loss is
\(O(\alpha(1+|\log\alpha|))\), and exact zeros consume a bounded
additional number of initial meridian jets. The actual figure-eight
operator satisfies this condition through its displayed monomial
divisors. Combining that extension with its previously proved
microscopic profile gives \(\mathcal U(0)=\operatorname{Vol}(4_1)/(2\pi)\).
The actual color pointing also forces a double root \(L=1\) in
\(B_{\rm cl}(1,L)\), unless that whole polynomial vanishes.
Nonvanishing end coefficients therefore would not by itself make
the complete fiber a simple-root chart.

One source-specific comparison does reach the complete value.
[Unnormalized Weyl jets](scaled_meridian_regular_profile.md),
Section 4.1, prove without a growth premise that
\[
 \mathscr D_NR_N(1)
 =-\frac{N-1}{2N}R_N(1)-\frac{P_N'(1)}{N^2},
 \qquad \mathscr D_N=N^{-1}Y\partial_Y,
 \qquad |P_N'(1)|/N^2\le D_N.
\tag{28}
\]
Thus the complete value and this first scaled derivative have
the same positive limsup and liminf rates, separately. All fixed
odd derivatives of the balanced regular function are polynomially
bounded. Higher even derivatives and the neighboring orbit
observations are not controlled by (28).

The subsequent [microscopic-disk theorem](research_regularized_microscopic_disk_growth.md)
gives an exact function-level observation under the weaker classical
end condition \(b_0(1,Y)\not\equiv0\), \(b_d(1,Y)\not\equiv0\).
It does not assume analytic splitting of either quantum divisor.
For the single fixed radius \(R_*=3+2\pi(d-1)\), it proves
\[
 \max(0,\mathcal U(0))
 =\limsup_{N\to\infty}\frac1N\log\!\left(
  1+\sup_{|\zeta|\le R_*}|R_N(e^{\zeta/N})|\right).
\tag{29}
\]
The proof transfers whole functions on a common microscopic circle
which avoids all shifted divisor roots, and only then uses Cauchy's
formula. The spacing of those roots gives a factorial bound for the
complete leading product, even for ramified roots or arbitrarily
close approaches to the orbit. No singular factor is canceled from
the exact equation. A bound of that microscopic norm by
\(e^{o(N)}(1+|K_N|)\) would identify the positive complete-value
limsup with (29). Such a bound is still an actual source requirement;
ordinary colors and the first-derivative identity (28) do not supply it.

The [radius comparison](research_subexponential_variation_meridian_observation.md),
Lemma 1, permits any fixed positive microscopic radius in (29): the
norms on two such disks differ by a subexponential factor. For the
existing strict long-twist Conway class, its Corollary 3 supplies
the actual microscopic norm bound and its all-level volume rate on
every fixed disk. This extends the observation domain of an existing
source theorem; it does not remove that class's long-twist hypotheses.

The end condition remains distinct. By
[the operator reduction](research_actual_operator_end_loss_and_coefficient_space.md),
a classical end loss of the actual primitive minimal normal operator
persists in every finite exact homogeneous annihilator of the same
normal-state family. Its coefficient-space solution set nevertheless
has bounded dimension under the original linear Laurent-degree bound.
Neither finite dimension nor formal reduction to the classical order
provides the missing quantitative observation estimate.
