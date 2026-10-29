# All finite quantum-normal orders have bounded Frobenius degree

Research theorem and independent exact audit, 27 October 2026.
For the ACTUAL integral high-color R-matrices, the coefficient of
delta^j, after factoring the root signed block permutation, has
Frobenius PBW degree at most 2j. The bound is uniform in the level,
color multiplicity, number of crossings, and number of braid strands.
The canonical actual divided sources obey the same relative bound
after their root unipotent rotations. Orders two and three are sharp.

This extends the [first-normal theorem](high_color_first_normal_r_and_frobenius_degree.md)
using the original finite integral matrices, not an assumed formal
quantum group lift. It does not identify the two geometric framing
currents, bound the numerical coefficient sizes, or prove a regulator
norm of the selected period.

## 1. Actual family, frame and filtration

Fix N>=2 and r>=0. Use D_m(q), m=N(r+1)-1, in the constant sign frame
\(w_{a,s}=(-1)^{Na(a-1)/2+as}u_{aN+s}\) of
[the high-color source proof](high_integral_color_frobenius_wall_source.md).
Put q_N=exp(pi i/N), Q=q^2 and delta=1-Q^N. All quantum derivatives
below use the actual local branch

\[
             q=q_N(1-\delta)^{1/(2N)}.                 \tag{1.1}
\]

Retain its marked half-Cartan root. The root multiplicity generators
are e,f,h of Sym^r, with
\(ew_a=(r-a+1)w_{a-1}\), \(fw_a=(a+1)w_{a+1}\),
\(hw_a=(r-2a)w_a\). Write A=(r-h)/2 for the block number.
Give e,f,h degree one and arbitrary head matrices degree zero.
On b strands use total degree in U(sl2^b).

The root crossing is its original head matrix times the block flip
and parity \(\varepsilon^{A_1+A_2}\), \(\varepsilon=(-1)^m\).
This whole signed permutation is retained separately, not replaced
by a bounded-degree polynomial in A_1,A_2. Root conjugation by it
preserves the filtration: permutations exchange Lie factors, parity
changes the signs of e,f and fixes h, and heads only conjugate the
head matrix coefficients.

**All-order crossing theorem.** For
\(R(\delta)=\sum_{j\ge0}\delta^jR_j\), either crossing sign satisfies

\[
           R_0^{-1}R_j\ \in\
  U_{\le2j}(\mathfrak{sl}_2\oplus\mathfrak{sl}_2)
                      \otimes\operatorname{End}(\text{heads}).  \tag{1.2}
\]

Coefficients may depend on N,r and the marked root. There is no
uniform archimedean bound on their sizes in (1.2).

## 2. Quantum-integer jets have controlled polynomial block degree

Write an integer argument as l=AN+s, 0<=s<N. With
z=Log(q/q_N),

\[
 [AN+s]_q=(-1)^A
 \frac{q_N^s e^{(AN+s)z}-q_N^{-s}e^{-(AN+s)z}}{q-q^{-1}}.
                                                               \tag{2.1}
\]

The coefficient of z^j after the sign is a polynomial in A of
degree at most j. If s!=0, the constant coefficient is nonzero
and independent of A. If s=0, division by delta gives

\[
 \frac{[AN]_q}{\delta}=(-1)^{A+1}\frac{A}{\rho_N}
      \left(1+\sum_{j\ge1}\delta^jP_j(A)\right),
 \qquad \deg P_j\le j,\quad \rho_N=q_N-q_N^{-1}.       \tag{2.2}
\]

To prove (2.2), factor A z from the numerator sinh(ANz), and
factor z from delta=1-exp(2Nz). The other factors are formal units.
The remaining coefficient of z^j has A-degree at most j. Substitution
\(z=\operatorname{Log}(1-\delta)/(2N)\) preserves this bound.
This proves both statements without any unramified-root or
nonresonance hypothesis on an algebraic shape.

For a product of any number of such factors, its extra normal
order j has extra block-polynomial degree at most j: the orders
chosen from its factors sum to j. Denominator units depending on
k,N,r but not the input block do not change this conclusion.

## 3. Every transfer has an exact valuation and divided factor

Write its transfer k=aN+b, 0<=b<N. For input heads s,t, put

\[
 c_E=a+\mathbf1_{s<b},\qquad
 c_F=a+\mathbf1_{t+b\ge N}.                            \tag{3.1}
\]

These are its actual E and F block changes. The E numerator of
E^(k)=E^k/[k]_q! crosses c_E multiples of N, while its denominator
crosses a. The corresponding F counts are c_F and a. Hence

\[
 \begin{split}
 E^{(k)}_{s',s}
   &=\delta^{c_E-a}e^{c_E}
                  \sum_{j\ge0}\delta^jP_{j,s}(A),\\
 F^{(k)}_{t',t}
   &=\delta^{c_F-a}f^{c_F}
                  \sum_{j\ge0}\delta^jQ_{j,t}(A),\\
 \deg P_{j,s},\deg Q_{j,t}&\le j,
 \quad s'=s-b\pmod N,\quad t'=t+b\pmod N.             \tag{3.2}
 \end{split}
\]

Constants depending on the recorded heads and parameters are
included in the polynomials. Their order is literal: the polynomial
is evaluated on the INPUT block before e^c or f^c acts.
Both exponents c_E-a,c_F-a are zero or one.

Here are the sign and boundary details. The zero numerator factors
in E supply
\(\prod_{h=0}^{c_E-1}(r-A+1+h)\), precisely the coefficient of
e^(c_E). Those in F supply \(\prod_{h=1}^{c_F}(A+h)\), precisely
f^(c_F). Every higher jet remains divisible by these products by
(2.2). Thus the expression vanishes at the actual finite boundaries;
it is not an interpolation outside the color.

The constant beta gauge also cancels ALL input-block signs, for
arbitrary k. For E, the sum of the integer parts in its k numerator
arguments is -kA plus an A-independent integer. Its beta quotient
has exponent

\[
                kA-Nc_E(c_E+1)/2+c_Es'.              \tag{3.3}
\]

For F the numerator sign has exponent +kA plus a constant, and its
beta quotient has exponent

\[
                -kA-Nc_F(c_F-1)/2-c_Ft'.             \tag{3.4}
\]

The block signs cancel in each case. All remaining signs are head
and transfer constants. Formula (2.1) shows the SAME sign accompanies
every jet, so no hidden parity character occurs in (3.2).

The actual nilpotent R term is

\[
 q^{k(k-1)/2}\rho^k[k]_q! E^{(k)}\otimes F^{(k)}.     \tag{3.5}
\]

Since [k]_q! has delta-order a, this term's exact possible starting
order is

\[
                  \nu=c_E+c_F-a
                    =a+\mathbf1_{s<b}+\mathbf1_{t+b\ge N}.
                                                               \tag{3.6}
\]

At total nilpotent order j>=nu, its PBW degree is at most

\[
               c_E+c_F+(j-\nu)=j+a\le2j.             \tag{3.7}
\]

In particular only k<(j+1)N can contribute to order j, however
large the actual color is. This includes all resonant tails and
all head boundary carries, not only the first one.

## 4. Cartan, inverses and arbitrary words

The output unrolled weights are affine in the two input blocks.
The varying part of the Cartan is
\(\exp(zH_1H_2/2)\). Its delta^j coefficient is a polynomial of
block degree at most 2j. Its ROOT value is the head Cartan times
the original parity \(\varepsilon^{A_{1,out}+A_{2,out}}\).
Relative to input parity this adds only
\(\varepsilon^{c_F-c_E}\), a head/transfer sign. Combining the
Cartan order j-l with (3.7) at nilpotent order l gives

\[
                      2(j-l)+(l+a)\le2j.
\]

This proves (1.2) for positive crossings. Multiplication by the
inverse root head matrix changes only head coefficients.

For the other sign, write R=R_0(I+sum_(j>=1)delta^j A_j).
The inverse interaction coefficients obey
\(B_j=-A_j-\sum_{l=1}^{j-1}A_lB_{j-l}\). Induction gives degree
at most 2j. The necessary root conjugations and checked flips
preserve the filtration by Section 1. Thus BOTH signs satisfy
the same theorem.

For every braid word W, product differentiation at any finite
order is a sum of products of root-conjugated local interactions.
Their normal orders add to j and their PBW degrees add to at
most 2j. Hence, on arbitrarily many strands,

\[
        W_0^{-1}W_j\in U_{\le2j}(\mathfrak{sl}_2^b)
                         \otimes\operatorname{End}(\text{heads}).\tag{4.1}
\]

No growing word length changes the degree bound, although it
changes its coefficients and number of terms.

## 5. Pivots, full scalar factors and knot closure

A whole pivot factor K(q)^c=q^(cH) has normal order-j coefficient
of block degree at most j, for any specified integer c, including
c=1-N. Thus ordinary and frozen ADO pivotal families and their
EXACT normal adapter K^(-N) satisfy the filtration. The matching
integral twist is a scalar and does not raise the degree. A regular
marked external scalar line, including the canceled complete germ
of d_N(M), likewise changes no Fr degree. If a retained scalar
has a genuine pole of normal order p, its Laurent coefficient at
order j instead uses the reduced bound 2(j+p); its valuation must
not be erased before applying the bound.

For a one-knot closure, the root Frobenius permutation has one
cycle. Its ordered partial trace multiplies all inserted Fr words
along that component. Their total degree stays at most 2j.
Moving them through the retained parity factors only changes signs;
the total uninserted parity on the knot is even. Thus the full
order-j long matrix is in End(head) tensor U_(<=2j)(sl2).

There is a corresponding exact hierarchy of Ward identities for
the ACTUAL ORDINARY integral ribbon family, with pivot K(q) and
matching twist: its generic long matrix is C_(N(r+1))(Q) times
identity, so every nonscalar Fr coefficient vanishes at every
normal order. For r>=2j the image of U_(<=2j)(sl2) has adjoint spins
0,1,...,2j, of dimensions 1,3,...,4j+1. Highest vectors e^l and
their successive commutators with f exhibit these summands;
their dimensions add to (2j+1)^2. Hence precisely

\[
                        (2j+1)^2-1=4j(j+1)           \tag{5.1}
\]

nonscalar head coefficient identities follow. For r<2j replace
2j by r in this count. Casimir powers only change the scalar part.
Frozen ADO auxiliary closures still satisfy the DEGREE bound, but
need not be generically scalar. Their scalar Ward hierarchy requires
the full pivotal/source adapter, not root pivot equality alone.

This is a finite exact hierarchy for every prescribed normal depth.
It is not the claim that the divided Hopf action on arbitrary tensor
products is primitive, or that its selected geometric image is nonzero.

## 6. The actual whole divided sources have the same relative bound

Set \(F_N(\delta)=F^{(N)}(q)\) and
\(E_N(\delta)=\tau E^{(N)}(q)\), where tau=(-1)^(Nr-1).
The case k=N of (3.2) has NO head carry and gives

\[
 F_N=f+\sum_{j\ge1}\delta^j F_j,\qquad
 E_N=e+\sum_{j\ge1}\delta^j E_j,\qquad
 F_j,E_j\in U_{\le j+1}(\mathfrak{sl}_2)
                                \otimes\operatorname{End}(\text{heads}).
                                                               \tag{6.1}
\]

The heads here are diagonal residue strings. Their exact source
operators are finite exponentials, as in the actual high-color note.
For a fixed source parameter t define

\[
              A(\delta,t)=e^{-tf}\exp(tF_N(\delta)).
\]

It satisfies A(0,t)=I and the exact interaction ODE

\[
 \partial_t A=e^{-t\operatorname{ad}f}(F_N-f)A.        \tag{6.2}
\]

Root adjoint unipotent conjugation preserves every PBW degree.
Its series is finite on each filtered piece, since ad f is
nilpotent there. At normal order l>=1 the coefficient on the
right of (6.2) has degree at most l+1<=2l. Solving its coefficient
recursion by integration and products therefore gives

\[
                     [\delta^j]A(\delta,t)\in U_{\le2j}.
                                                               \tag{6.3}
\]

The same proof applies to exp(-ue)exp(uE_N), and to the right
interaction exp(uE_N)exp(-ue). Consequently the ORIGINAL source
and co-source jets, after their recorded root unipotent rotations,
are obtained by degree-at-most-2j operators on their fixed rank-one
source and dual. This is an operator result, not a criterion which
assumes such jets exist.

There is a still more concrete finite source bound. Formula (3.2)
for k=N says F_j=f P_j(A) and E_j=e Q_j(A), with polynomial degree
at most j. The F interaction stays in the Borel algebra generated
by f,A, and the E interaction in that generated by e,A. On the
highest source v_0, A v_0=0. After the root unipotent rotation the
order-j source vector therefore lies in

\[
                   \operatorname{span}\{v_0,fv_0,\ldots,f^{2j}v_0\}.
                                                               \tag{6.4}
\]

The rotated dual is supported on the corresponding first 2j+1
dual descendants. To see it, order the Borel monomials with A
against the highest source or dual; the degree bound limits the
remaining raising or lowering power to 2j. Thus fixed quantum
depth B needs at most 2B+1 Fr source descendants, independently
of N and r, while the full root coherent/prequantum source is
retained by its exact unipotent frame.

The actual normalization units U_s(q;t,u) of the two-flag source
are still retained. Their inverses are head-diagonal scalar formal
series on 1+tu!=0, so they do not increase Fr degree. This does
not bound their coefficient norms or permit evaluating them at
the source wall 1+tu=0.

The rank-one root coupon itself is NOT asserted to lie in PBW
degree zero. The precise coupon statement is a sum of
left-degree-2a and right-degree-2b operators around that fixed
coupon, with a+b<=j. Conflating this relative bound with a
small-degree polynomial formula for the rank-one projector would
be false when r is large.

## 7. Clock gauges and the exact coherent source realization

The [actual coherent dictionary](high_color_two_clock_normal_source.md)
turns (1.2) and (6.3), at any fixed depth B, into differential
operators of order at most 2B. Its one-sided connection terms and
all finite polynomial endpoints remain exact.

A controlled gauge G=V^A, with V the cyclic HEAD shift, is not a
plain polynomial Fr operator. In a head Fourier basis it is a finite
sum of head projectors times clocks Q_N^(cA). Enlarge the filtration
by giving those clocks degree zero. Their conjugation rescales e,f
and fixes h, so this crossed-product filtration is multiplicative
and Ad G preserves it. The coherent source realizes these clocks
as the exact finite dilations and source characters of the two-clock
note, not as differential operators of falsely bounded order.

Thus after this controlled clock gauge the PBW part still has
degree at most 2j, but genuine whole dilation factors must be
retained. Arbitrary quantum-normal gauges or source-wall divisions
have NOT been declared filtration-preserving.

No assertion here bounds the number of dilation factors, gives a
fixed finite-type whole comparison, identifies the internal
framing-current image, or derives the volume limit from local jets.
The result supplies actual bounded-normal-order operators and source
jets for those further exact comparisons.

## 8. Independent exact checks

[The audit](../experiments/audit_high_color_all_normal_filtration.py)
uses polynomial Gaussian recursion and genuine truncated series
through delta^3, including the full half-Cartan phase. At N=2,3,4
and r=8 it checks 83,000 actual coefficient jets and 1,584
shiftwise PBW-polynomial membership conditions. The r=8 spaces
make the bounds at orders two and three nonvacuous. The k=0
Cartan component fails degree 2j-1 at both orders: 2j is sharp.

It also checks 48 actual source OPERATOR jets after root unipotent
rotation, rather than only their value on one vector, and verifies
the full actual positive/negative R inverse through order three
on a separate small high color. No division by a vanishing factorial
is used in the test: Gaussian entries are multiplied by [k]! before
specializing. [Results](../experiments/high_color_all_normal_filtration_results.json).
