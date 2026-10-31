# Exact quantum polarization between diagonalizations of a MAIN quadrangulation

31 October 2026. research theorem; not published.
The full spectral source polynomials of all diagonal choices form an exact
Newton-reversal orbit. Sections 9--11 prove this identity and the corresponding
change of the original filled functional. Sections 1--6 distinguish it from
a transport of integer twist powers, and sections 7--8 give its full-Hermite
kernel and the remaining cancellation problem. Original terminal labels,
Cartan factors, and primitive disk framings are retained.

## 1. What the local change actually does

Keep one quadrilateral of the original MAIN quadrangulation fixed,
with cyclic white vertices \((x,b,y,c)\) and diagonal \(xy\). In the actual
inverse cut, its four cyclic terminals \(0,1,2,3\) have shaded groups
\((1,2),(3,0)\) and physical untwisted arcs \((0,1),(2,3)\). This is the
dictionary in [general Morse source](research_matched_sphere_morse_source.md), sections
1--2, and [original crossing-disk cut](general_augmented_plat_matching_geometry.md), sections
1--4.

Choosing the other diagonal \(bc\) rotates the local roles by one
cyclic step. With the SAME four exterior terminals, its physical
untwisted arcs are \((1,2),(3,0)\). Thus the zero-twist tangles already
have different boundary pairings. Their geometric quarter-turn is a
permutation of the boundary data, not an isotopy relative that boundary.

Write \(T(n)\) for the original two-strand box with full signed integer
power \(R^n\), including its recorded ribbon framing. Let \(r\) be the
genuine orientation-preserving quarter-turn, using the original turns.
In the unchanged exterior frame the two filled choices are \(T(n)\) and
\(r T(m)\). Reversing all convention signs together does not change the
obstruction below. Our sign is calibrated by the exact original
identity \(r T(-1)=T(1)\).

## 2. Exact fixed-boundary tangle obstruction

The double cover of a ball branched over a trivial two-string tangle
is a solid torus. Its boundary is the double cover of the sphere with
four marked branch points. Choose primitive boundary classes
\(\alpha,\beta\), with intersection one, so the meridian of \(T(0)\) is
\(\alpha\) and the lift of one positive half twist acts by
\(\alpha\mapsto \alpha+\beta\). The latter is the elementary annular picture:
the lift of an arc joining the two exchanged branch points is a simple
closed core, and the lifted half twist cuts and reglues its annulus by
one full turn. Induction, including inverse twists, gives

\[
       \mu_n=\alpha+n\beta.                         \tag{1}
\]

Represent the four-point sphere as the pillowcase quotient of a square
torus. A quarter-turn lifts, up to the deck involution, to
\(\alpha\mapsto \beta\), \(\beta\mapsto -\alpha\). Thus the turned tangle has

\[
       \mu'_m=\beta-m\alpha,
       \qquad \det(\mu_n,\mu'_m)=1+nm.              \tag{2}
\]

A homeomorphism of tangles equal to the identity on the original
boundary lifts to a homeomorphism of their branched solid tori equal
to the identity or deck involution on the boundary. It must preserve
the rational line of the meridian. Equations (1)--(2) therefore give

\[
       T(n)\simeq_{\partial}rT(m)\quad\Longrightarrow\quad nm=-1.
                                                               \tag{3}
\]

For integer \(n,m\), the only possibilities are \((1,-1)\) and \((-1,1)\);
they are indeed the two original single-crossing turn identities.
No classification theorem is needed for the obstruction: the kernel
of boundary homology into the solid torus is enough. In the usual
rational-tangle fraction convention this is the negative-reciprocal
rule, also proved in Kauffman--Lambropoulou,
[On the classification of rational tangles](https://arxiv.org/pdf/math/0311499),
sections 2 and 6.

Consequently there is no universal portwise substitution of long
integer crossing powers that reverses a diagonal flip while leaving
the exterior tangle fixed. This is a general local theorem, not a
test of a particular closed knot. It does not say that two specially
chosen exteriors can never have isotopic closures.

## 3. The two different peripheral tori must not be confused

The torus in (1)--(2) is the branched cover of the four-point boundary
sphere. It is NOT the crossing-circle cusp torus. The genuine spatial
quarter-turn moves the auxiliary circle and its twice-punctured disk
together. It preserves that disk's preferred zero-self-linking
longitude and carries its meridian to the corresponding meridian.
This is the actual turn statement of
[original preferred disk longitude](actual_mixed_crossing_circle_preferred_longitude.md), section 5.
One must not install the matrix of (2) as an unproved cusp basis change.

For the original integer surgery coordinate, the primitive killed
curve is \(\mu+p \lambda\), and the inserted exponent is
\(n=\epsilon-2p\). In the flipped standard box, obtaining the old tangle
would instead require the rational exponent \(m=-1/n\). Formally this
would ask for

\[
            p'=\frac{\epsilon'+1/n}{2}.             \tag{4}
\]

For \(|n|>1\) and \(\epsilon'\) in \(\{-1,0,1\}\), (4) is not an integer.
This formal expression is not a valid replacement by the already
proved integer Gaussian filling functional.

Even allowing surgery on that same unknot with \(p'=a/b\) in lowest
terms does not give the original local ball move. Its primitive
filling curve is \(b \mu+a \lambda\). If the other components are ignored,
the filled ambient manifold has first homology \(\mathbb Z/|b|\mathbb Z\), whereas the
original integer full-twist fillings have \(|b|=1\) and ambient \(S^3\).
The crossing circles in this construction bound mutually disjoint
disks when the MAIN strands are ignored. For several such rational
fillings the same homology calculation is the diagonal presentation
with summands \(\mathbb Z/|b_e|\mathbb Z\). It supplies no cancellation of these ambient
obstructions. A rational-tangle replacement in a ball is a different
operation and would require additional tangle data, not the single
original crossing-circle filling at that port.

More generally a fixed integral peripheral matrix sends a slope
\((1,p)\) to \((a+bp,c+dp)\), giving
\(p'=(c+dp)/(a+bp)\) when the result can be normalized. If \(b\) is nonzero,
\(p'\) stays bounded as \(|p|\) tends to infinity, and it cannot be integral
for infinitely many such \(p\): a bounded integral subsequence would be
constant, contradicting the nonzero determinant. Thus a fixed cusp
map sending a cofinal integer long-filling family to another such
family must preserve the longitude line and have affine slope action.
This is only a necessary condition; (2) does not itself assert a map
of the augmented exteriors.

## 4. A source-preserving finite cover does not erase this local kernel

Suppose one proposes a common finite cover of the branched boundary
torus, with the SAME fixed boundary identification used for the two
solid tori. Let its integral inclusion be \(A:L'\longrightarrow H_1(T^2;\mathbb Z)\).
Over the rationals, \(A\) is an isomorphism. The lifted meridian lines
are \(A^{-1}(\mathbb Q\mu_n)\) and \(A^{-1}(\mathbb Q\mu'_m)\). They coincide only when
the original lines coincide, hence only when \(nm=-1\).

This excludes a repair by such a source-preserving pullback cover.
It does not exclude unrelated covers with different boundary maps,
branched covers of the full link, or changes of chamber/wiring. Those
would need new peripheral and original quantum source adapters.
There is no general Kashaev descent identity supplied by a cover.

## 5. An exact original nilpotent quantum obstruction

This is a separate finite check with a proof for all integer exponents,
not a numerical sample. At \(N=2\), put \(d=1\), \(q=i\), and
\(\lambda=\exp(\pi i/4)\). The actual full pair algebra is
\(\mathbb C[\Omega]/(\Omega^2)\). In the Newton basis put

\[
       B=\widehat B_1=-\Omega/4,\qquad B^2=0.
\]

The original crossing Hermite data give
\(r_2(0)=1\), \(r'_2(0)=i/4\), and retain the Cartan scalar
\(\lambda=q^{d^2/2}\). Consequently

\[
 R=\lambda(1-iB),\qquad
 R^n=\lambda^n(1-inB).                              \tag{5}
\]

The genuine unscaled original turn satisfies
\(\mathscr R(1)=B\), \(\mathscr R(B)=1\); these are the \(N=2\) cases of the
full physical Newton turn theorem, not an eigenvalue-only transform.
Thus

\[
        \mathscr R(R^m)=\lambda^m(B-im).              \tag{6}
\]

For any nonzero scalar \(a\), equality
\(\mathscr R(R^m)=a R^n\) forces \(m\) nonzero and, by comparing the two
coefficients, \(nm=-1\). In those two integer cases (5)--(6) give the
original exact equalities with \(a=1\). In particular allowing an
unknown normalization scalar cannot remove the local obstruction.
Discarding the nilpotent coefficient would lose exactly this test.

Equations (5)--(6) rule out a coupon-uniform all-level original tensor
identity of the proposed power-substitution kind. The topological
argument of section 2 is independent of this small-level witness and
continues to rule out the relative-boundary move without any level
restriction. We do not infer distinguishability of all closed knots
from their level-two invariant.

## 6. A global long-filling obstruction when capacities differ

Let \(T,T'\) be two simple choices on the same MAIN quadrangulation,
with their actual complete hyperbolic augmented exteriors and knot
parity patterns. Suppose \(\Phi(T)<\Phi(T')\). Their complete volumes
are \(2\pi \Phi(T)\) and \(2\pi \Phi(T')\). The [proved independent long-filling geometry](general_augmented_plat_long_filling_quantifiers.md) makes the filled volumes converge to these respective
values as the minimum absolute integer filling coordinate tends to
infinity.

Choose each geometric filling threshold so that the volume error is
less than one-third of the positive difference between the two
complete volumes. The two resulting volume intervals are disjoint.
No pair of knots in these two cofinal all-long families can have
homeomorphic complements, and in particular they cannot be the same
knot. This obstructs ANY proposed global transport between these
families that keeps all new coordinates independently long. It does
not assume a local tangle substitution. It applies in particular to
a strictly lower-capacity simple chart and a maximal chart.

Equal-capacity ties, transports involving short slopes, and changed
rational tangles are not settled by this argument. It is not an
obstruction to representing the same knot by arbitrary turned coupons,
as in the next section.

## 7. What does transport exactly: full turned coupons

There is a useful positive finite statement. For any set of changed
diagonals, put the genuine turned OLD coupon in every changed disk
of the new chart, using the inverse of its local frame rotation.
On the original Hopf polynomial algebra the two quarter-turn directions
agree, since the genuine turn squares to the identity. Each physical
local tangle is then exactly the old tangle in the original exterior
frame. Outside arcs and the actual reduced marked closure stay fixed.
Morse bends use the original snakes; no ribbon twist or Cartan scalar
is discarded. Thus the whole contraction is the SAME original filled
knot source, but the new local coupons at flipped ports are
\(\mathscr R(R^n)\), not new integer powers \(R^m\).

By the full pair-commutant theorem these turned coupons are polynomials
in the new ordered pair Casimir, with all root Hermite data. Therefore
the new general Morse coefficient compiler applies to them. This is
not sector transport, multiplicativity of the turn, or transport of a
Gaussian filling theorem. The original final knot-framing character
must be retained; it is not reset using a fictitious new braid exponent.

Here is the exact spectral kernel of that change of polarization.
For all \(N\geq 2\), let

\[
\begin{gathered}
 c_j=2\cos((2j+1)\pi/N),\quad
 \chi_N(z)=\prod_{j=0}^{d}(z-c_j)=2T_N(z/2)+2,\\
 S_r=\prod_{j=1}^r2\sin(\pi j/N),\qquad
 B_r(z)=\prod_{j=0}^{r-1}(c_j-z),\qquad
 \widehat B_r=B_r/S_r^2.
\end{gathered}
\]

The original exact turn is
\(\mathscr R\widehat B_r=\widehat B_{d-r}\). Newton division of the resolvent
numerator, keeping repeated nodes, gives

\[
 V_N(\sigma;z)=
 \sum_{r=0}^{d}(-1)^rS_r^2
       \prod_{j=r+1}^{d}(\sigma-c_j)\widehat B_r(z).
                                                               \tag{7}
\]

This is a polynomial identity representing
\(\chi_N(\sigma)/(\sigma-\Omega)\). Since \(c_{d-j}=c_j\) and
\(S_r S_{d-r}=N\), applying the turn and changing \(k=d-r\) yields

\[
 \boxed{\quad
 \mathcal K_N(\sigma,\zeta)
 :=(\mathscr R V_N(\sigma))(\zeta)
 =(-1)^dN^2\sum_{k=0}^{d}
                  \widehat B_k(\sigma)\widehat B_k(\zeta).
 \quad}                                                     \tag{8}
\]

No simple-node interpolation or root-normal deletion was used. This
is a polynomial of degree at most \(d\) in each variable, symmetric
in them, and it is the exact Newton reproducing kernel times the
displayed original factor.

Let \(f_n(\sigma)=\exp[nN\operatorname{arccosh}(-\sigma/2)^2/(4\pi i)]\) in the original
slit branch. Choose a contour enclosing every actual spectral node,
within its analytic domain and avoiding the cut starting at \(+2\).
The original full power is \(q^{n d^2/4} f_n(\Omega)\). Thus the turned
power is exactly \(q^{n d^2/4} g_n(\Omega)\), where

\[
 g_n(\zeta)=\frac1{2\pi i}\oint
     \frac{f_n(\sigma)}{\chi_N(\sigma)}
                       \mathcal K_N(\sigma,\zeta)\,d\sigma.
                                                               \tag{9}
\]

This is equivalent to the full confluent Newton formula

\[
 g_n(\zeta)=\sum_{r=0}^{d}(-1)^r S_r^2
       f_n[c_0,\ldots,c_r]\widehat B_{d-r}(\zeta).    \tag{10}
\]

Finally any polynomial \(g_n\) can itself be inserted against the SAME
new-chart numerator by its Cauchy/Hermite functional

\[
 g_n(\Omega)=\frac1{2\pi i}\oint
             \frac{g_n(\zeta)}{\chi_N(\zeta)}
                         V_N(\zeta)\,d\zeta.          \tag{11}
\]

Multilinearity makes (9)--(11) exact for the whole marked source and
all its original face targets. Unchanged ports retain their ordinary
Gaussian functional. These equations supply the promised actual
transformed functional at changed ports; they do not make it Gaussian.

## 8. The known maximal-chart gap does not alone control this kernel

Even its pointwise absolute size is not subexponential. At the real
corner \(\sigma=\zeta=-2\), every square in (8) is nonnegative. Take
\(k_N=\lfloor N/4\rfloor\). For both parities this index precedes any vanishing
factor. The original sine products give

\[
 \widehat B_{k_N}(-2)=
  \prod_{j=0}^{k_N-1}
   \frac{\cos^2((j+1/2)\pi/N)}{\sin^2((j+1)\pi/N)},
\]
\[
 \lim_{N\to\infty}\frac1N
        \log\widehat B_{k_N}(-2)
 =2\int_0^{1/4}\log\cot(\pi t)\,dt
 =\frac{2G}{\pi}>0,                                  \tag{12}
\]

where \(G=\int_0^{\pi/4}\log\cot t\,dt\) is Catalan's constant. The
logarithmic endpoint singularity is integrable; splitting off the
first fixed small interval and comparing monotone log-sine sums to
their integrals proves the displayed Riemann-sum limit. Consequently

\[
 \liminf_{N\to\infty}\frac1N
      \log|\mathcal K_N(-2,-2)|\geq\frac{4G}{\pi}.     \tag{13}
\]

The maximal-chart non-CROSS estimate supplies a strict source gap,
not a bound that automatically pays the exponential size in (13).
Thus no inference of its preservation follows by taking absolute
values of the transformed kernel. The large kernel is itself
compatible with cancellations: at \(n=1\), (9) produces the exact
opposite single crossing. We have not claimed the transformed period
actually has excessive growth, or that a cancellation-aware estimate
cannot use the maximal chart.

The precise remaining problem is a uniform cancellation-aware estimate
for (9)--(11) applied to the complete maximal-chart source, together
with identification of its actual filled action. The former Gaussian
H1/H2 period argument does not already supply that estimate. The exact
topology says which old knot such a successful new argument would
concern; no rational-power or sector equality is needed.

## 9. Exact local homogeneous covariance, with canonical physical lifts

This strengthens section 7 to a polynomial identity before any shared
coefficient is extracted. Denote the original complete root turn scalar
by \(x_0=q^d\) to distinguish it from a face variable. For an arbitrary
full Casimir polynomial \(f\), the actual unscaled turn has entries

\[
 (\mathscr R f)_{r,s;u,v}
     =q^{d(r-v)} f_{d-r,u;s,d-v}.                    \tag{14}
\]

At the new box let the homogeneous face tuple be \((X,B,C,Y)\). On
canonical physical support the new input/output clocks are

\[
 Q^u=-q^{-1}X/B,\quad Q^v=-q^{-1}B/Y,\quad
 Q^r=-q^{-1}X/C,\quad Q^s=-q^{-1}C/Y.
\]

The old matrix entry on the right of (14) has the literal face tuple
\((C,Y,X,B)\): its inputs are \(s,d-v\) and outputs \(d-r,u\).
Use centered physical face-log differences
\(\operatorname{Log}(L_{\mathrm{left}}/L_{\mathrm{right}})=2\pi i(i-d/2)/N\). They are the original clocks
because \(-q=\exp(-\pi i d/N)\). Complementing a head is then literal log
negation. In particular

\[
 \operatorname{Log}(XY/(BC))=2\pi i(r-v)/N.
\]

The actual old adapter has denominator \((XY)^{d/2}\), while the new
one has denominator \((BC)^{d/2}\). Equation (14) cancels their ratio
exactly. There is no extra scalar or parity sign:

\[
 \boxed{\quad
 H_{\mathscr R f}(X,B,C,Y)=H_f(C,Y,X,B).
 \quad}                                             \tag{15}
\]

Here canonical physical support is imposed FIRST. On the remaining
modular grids, a wrong unwrapped total makes both matrix entries zero;
no individual head is reset by \(N\). For supported states the centered
lift calculation just made applies. After fixing a common face scale,
the original local Fourier adapter samples all three independent root
grids (with the actual even-level cosets). Both homogeneous polynomials
have degree \(d<N\), so the difference has degree below \(N\) in each
normalized variable. Product-grid uniqueness proves the formal identity
(15), not merely an equality on supported individual heads.

For clarity the two reflection symmetries used in comparing cyclic
frames are also exact. Outer symmetry follows from the source operator
depending only on \(X+Y,XY\). For middle symmetry, its diagonal is \(c_j\)
and its downward coefficients are \(-s_j^2(X+Y)\) and
\(-s_j s_{j-1}XY\), where here \(s_j=2\sin(\pi j/N)\). With the bilinear
pairing \([z^d]uv\), reflection gives
\(c_j=c_{d-j}\), \(s_j^2=s_{N-j}^2\), and
\(s_j s_{j-1}=s_{N+1-j}s_{N-j}\). Thus the source Casimir, and every
polynomial in it, is selfadjoint for that pairing. Equivalently its
entries obey \(F_{i,j}=F_{d-j,d-i}\), proving
\(H_f(X,B,C,Y)=H_f(X,C,B,Y)\).

In particular the flipped frame \((b,y,x,c)\) satisfies

\[
 H_f(b,y,x,c)=H_{\mathscr R f}(x,b,c,y),\qquad
 H_{\mathscr R f}(b,y,x,c)=H_f(x,b,c,y).             \tag{16}
\]

All four variables in (16) are the same original labeled white faces.
It is the coupon that changes. There is no assertion that \(H_f\) alone
is invariant under a cyclic permutation.

## 10. The exact spectral action of all independent diagonal flips

Fix the MAIN quadrangulation, one MAIN mark, and a reference choice
\(D\) of all diagonals. For any choice let \(S_D(\sigma_1,\ldots,\sigma_R)\)
be its original full marked spectral polynomial, with \(V_N(\sigma_e)\)
at every port and all ordinary face targets retained. Each spectral
degree is at most \(d\). There is no geometric or simplicity hypothesis
in the following finite statement; the general Morse realization
retains any parallel diagonal edges as incidences.

Let \(\mathscr R_e\) denote the full Newton reversal on the degree-at-most-\(d\)
polynomial in its spectral variable \(\sigma_e\), fixing all other
variables. The numerator itself has the useful symmetric form

\[
 V_N(\sigma;z)
   =(-1)^dN^2\sum_{r=0}^{d}
             \widehat B_{d-r}(\sigma)\widehat B_r(z).
                                                               \tag{17}
\]

It follows directly from (7) and the same reflected products as (8).
Hence \(\mathscr R_zV_N=\mathscr R_\sigma V_N=\mathcal K_N\). Applying (16) at one disk and then
taking the unchanged full marked coefficient proves

\[
 \boxed{\qquad
 S_{D^e}=\mathscr R_e S_D,
 \qquad
 S_{D^A}=\left(\prod_{e\in A}\mathscr R_e\right)S_D
 \quad(A\subseteq\{1,\ldots,R\}).
 \qquad}                                             \tag{18}
\]

Indeed (16) holds already for the product of local face polynomials,
and the spectral reversal commutes with the original shared coefficient
extraction. Independent reversals commute and each squares to the
identity. A second flip returns a local frame rotated by a half turn;
the exact outer and middle reflection symmetries above return the same
polynomial, with no newly chosen gauge.

The diagonal choices form the ordinary binary cube with its free
\((\mathbb Z/2\mathbb Z)^R\) action. Equation (18) is an equivariant assignment into the
tensor product of the FULL Hermite algebras. Its image need not be a
free orbit: some polynomials may have stabilizers. Thus no stronger
torsor or freeness assertion about quantum states is being made.

If

\[
 S_D=\sum_{\mathbf r}\tau_D(\mathbf r)
                         \prod_e\widehat B_{r_e}(\sigma_e),
\]

then flipping \(e\) replaces \(r_e\) by \(d-r_e\) in this same coefficient
tensor. In particular the finite positive norm

\[
                    \sum_{\mathbf r}|\tau_D(\mathbf r)|^2
                                                               \tag{19}
\]

is invariant under all choices. This is the already specified Newton
tensor norm. It is not a bound of the complete geometric rate, and
does not transport CROSS/LEFT/RIGHT restrictions or their positive
envelopes. Such restrictions are not invariant under (15).

## 11. Filled functionals transform contragrediently

Define the exact original single-port functional on spectral
polynomials by

\[
 \mathfrak F_{n,N}(p)
   =\frac{q^{nd^2/4}}{2\pi i}\oint
              \frac{f_n(\sigma)}{\chi_N(\sigma)}p(\sigma)\,d\sigma.
                                                               \tag{20}
\]

It is the original Gaussian/Hermite functional before its equivalent
whole-interval Fourier deformation. Thus its usual sine, integer
charges, and endpoint terms have not been altered or dropped.
The original raw filled contraction is
\(I_D(\mathbf n)=(\bigotimes_e\mathfrak F_{n_e,N})(S_D)\).

For \(A\) the set of flipped disks, (18) gives the exact equality

\[
 I_D(\mathbf n)
  =\left(\bigotimes_e
       [\mathfrak F_{n_e,N}\circ\mathscr R_e^{\mathbf1_{e\in A}}]
        \right)S_{D^A}.                              \tag{21}
\]

The changed local functional is exactly (9)--(11), with the turned
polynomial \(g_n\) and the same external Cartan scalar. To see its
adjoint convention directly, the coefficient Cauchy pairing is
\([z^d](uv\bmod\chi_N)\). On the normalized Newton basis it equals
\((-1)^dN^{-2}\delta_{i+j,d}\). Newton reversal is selfadjoint for
this pairing. Therefore \(\mathfrak F_{n,N}(\mathscr R p)\) is the Cauchy functional with
\(\mathscr R f_n\) in its first slot, precisely \(g_n\), rather than a guessed
reciprocal Gaussian.

Equations (18)--(21) resolve the exact source relation between charts.
They do not contradict the topology of sections 1--6: keeping the
old knot on the new chart changes its filling functional. Applying
the ordinary Gaussian functional on both sides would instead give
the two different integer-twist diagrams. The complete and filled
geometric actions of those two procedures must not be conflated.

The preserved quantity (19) does not bypass the exponential kernel
in (13). A proof of the general volume conjecture from a maximal
chart still needs a cancellation-aware analysis of (21), with the
actual old peripheral action and its full source normalization.

## Dependencies

The finite source inputs are the notes
[general Morse realization](research_matched_sphere_morse_source.md),
[full pair commutant and original turn](actual_pair_casimir_commutant_and_rotated_trace.md),
[full Newton turn and metric](actual_newton_turn_positive_gram.md),
[original signed crossing powers](actual_direct_long_power_source.md), and
[original Gaussian/resolvent functional](actual_gaussian_resolvent_numerator_and_cap.md) in the notes directory.
The geometric obstruction uses only the already identified complete
volumes and the proved long-filling convergence, not a Kashaev
asymptotic for a lower-capacity chart.