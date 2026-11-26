# Newton coordinates at a degenerate edge: the original source with its crossing powers

Research note, 2 November 2026.

The square coordinates of the positive filling problem can reach a
corner while its linear constraints remain strictly feasible. This
is a degeneration of the original geometric subdivision. The finite
source itself has an exact alternative description that retains
arbitrary signed crossing powers. This note gives that description,
its local factorial phase and normalization, and a precise limitation
on transferring the existing zero-power asymptotic through it.

The algebraic ingredients are the original Newton pairing, turn and
crossing matrices. They were proved in
[the Newton calculus](../papers/newton-calculus/finite.tex) and compiled
for general expressions in
[the source compilation note](research_arbitrary_power_source_compilation.md).
The statements below apply these identities to the actual boundary
tensor at a potentially degenerate edge. They do not assert a new
topological move or a general asymptotic theorem for nonzero powers.

## 1. The two-vertex boundary tensor

Put \(D=N-1\), \(\eta=(-1)^D\), and use the original full algebra
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(F)=\eta N^2[z^D]\operatorname{rem}_{P_N}F.
 \tag{1}
\]
Here \(T_N\) is the ordinary Chebyshev polynomial. Let \(e_0,\ldots,e_D\)
be the real normalized Newton basis, with
\[
 \phi_N(e_i e_j)=\delta_{i+j,D},\qquad
 T e_i=e_{D-i},\qquad
 K(z,w)=\sum_{i=0}^{D}e_i(z)e_i(w).
 \tag{2}
\]
The full quotient is used throughout: equality includes the first
derivatives at double roots.

Consider two adjacent original vertices. Besides their common edge,
the first has \(p\) external legs and the second \(q\) external legs.
Initially keep the external variables \(u_1,\ldots,u_p\) and
\(v_1,\ldots,v_q\) independent. For arbitrary signed integers \(m,n\),
their original boundary tensor is
\[
 \begin{split}
 Z_{m,n}(\mathbf u,\mathbf v)
 =\phi_z\phi_w\bigg[
 R(z)^m R(w)^n K(z,w)
 \prod_{\alpha=1}^{p}K(z,u_\alpha)
 \prod_{\beta=1}^{q}K(w,v_\beta)\bigg].
 \end{split}
 \tag{3}
\]
The notation \(u_\alpha\) here denotes a spectral variable. When an
angle is used below, it is substituted as \(u_\alpha=-2\cos t_\alpha\).
Each external variable has degree below \(N\) in (3). After an exact
identity is established, external variables belonging to the same
outside vertex may be identified. Their resulting product is kept at
its full ordinary degree.

Let \(M\) be the original multiplication matrix of \(R\) in the Newton
basis, and let \(J\) be the coefficient reversal matrix. Set
\[
                  C_{n,N}=J M^n J.
 \tag{4}
\]
This notation denotes a linear operator, not the scalar Gaussian
normalization used elsewhere. Negative powers are the actual inverse
powers in the full algebra.

**Proposition 1.** If \(p,q\ge1\), then
\[
 \boxed{\quad
 Z_{m,n}
   =C_{m,N}^{(u_1)}\,C_{n,N}^{(v_1)}Z_{0,0}.
 \quad}
 \tag{5}
\]
The operators act on the indicated single external factors before
identifying boundary variables. They are invertible, with inverse
\(C_{-m,N}\) and \(C_{-n,N}\). All carrier scalars and normal data are
retained.

**Proof.** Multiplication is self-adjoint for the original Frobenius
pairing, so
\[
                    (M^n)^T J=J M^n,\qquad
                    (M^n)^T=J M^nJ=C_{n,N}.
 \tag{6}
\]
Expanding the kernel gives the identity
\[
 (C_{n,N}^{(u)}K)(z,u)=R(z)^n K(z,u)
                      \quad\text{in }\mathcal A_N\otimes\mathbb C[u]_{<N}.
 \tag{7}
\]
More explicitly, the coefficient of \(e_j(z)e_i(u)\) on either side
is \((M^n)_{ji}\). Multiply (7) by all the other factors in (3) and
apply the two original traces. This proves (5). Since
\(J^2=I\) and \(M\) is invertible, the inverse assertion follows.
No distinct-root evaluation has been used. \(\square\)

The equality in (7) uses reduction only in the internal variable
\(z\). The operator \(C_{n,N}=T R^n T\) is the original turned
crossing; its full basis matrix acts on the external polynomial.

There is an exact formula even when one endpoint has no external
leg. For arbitrary internal coupons \(A,B\), expand them as
\(A=\sum_r a_re_r\), \(B=\sum_s b_se_s\). Then
\[
 \phi_z\phi_w[R(z)^m A(z)K(z,w)R(w)^n B(w)]
       =\sum_{r,s}a_rb_s H_{m,n}(r,s),
 \qquad H_{m,n}=J M^m J M^n .
 \tag{8}
\]
Indeed the two factors at the common index \(k\) are
\((JM^m)_{rk}\) and \((JM^n)_{sk}\); both matrices \(JM^j\)
are symmetric. In particular \(H_{0,0}=I\).
Formula (5) requires an external leg at both ends; (8) does not.

## 2. The finite tensor does not lose rank at the geometric corner

**Proposition 2.** If \(p,q\ge1\), the flattening of the full tensor
(3), with the \(p\) left legs on one side and the \(q\) right legs on
the other, has rank exactly \(N\), for every pair of signed powers.
In particular the entire boundary polynomial is nonzero.

**Proof.** Multiplication from \(\mathcal A_N^{\otimes p}\) to
\(\mathcal A_N\) is surjective: all but one factor can be the unit.
The same holds on the right. After these multiplication maps, the
central bilinear pairing is
\[
                 (A,B)\longmapsto
             \phi_N\bigl(R^m A\, T(R^n B)\bigr).
 \tag{9}
\]
The original Frobenius pairing is nondegenerate, multiplication by
either power is invertible, and \(T\) is invertible. Hence (9) is
nondegenerate and has rank \(N\). Pullback along two surjective maps
preserves that rank. \(\square\)

This is a statement about the full boundary tensor. It does not
prohibit a zero at a particular boundary value, nor give a lower
bound on its large-\(N\) leading coefficient. It does show that a
square-corner degeneration does not cause an algebraic rank loss of
the original finite object.

## 3. A precise factorial phase for the transported crossings

Write
\[
 q_N=e^{\pi i/N},\qquad \kappa_N=q_N^{D^2/2},\qquad
 S_k=\prod_{j=1}^{k}2\sin(\pi j/N).
\]
The original signed one-crossing operator in (4) has entries
\[
 \boxed{\quad
 (C_{\sigma,N})_{r,k}
   =\kappa_N^\sigma(-1)^k q_N^{\sigma k(r+1)}
       \frac{S_k}{S_rS_{k-r}},
 \qquad 0\le r\le k<N,\quad \sigma\in\{1,-1\}.
 \quad}
 \tag{10}
\]
Its other entries vanish. This is the transpose of the original
crossing matrix. For negative sign it is its coefficient conjugate,
as required in the real Newton basis. A power \(n\) is a chain of
\(|n|\) such factors, all of sign \(\operatorname{sgn}n\).
Every intermediate index is retained.

Let
\[
 J(x)=\int_0^x\log(2\sin\pi s)\,ds,\qquad
 h(x,y)=J(x)-J(y)-J(x-y)
 \tag{11}
\]
on the branch real for \(0<y<x<1\). Here \(x=k/N\) is the
incoming index and \(y=r/N\) the outgoing one. Define
\[
 F_\sigma(x,y)
   =h(x,y)+\sigma i\pi\left(\frac12+x+xy\right).
 \tag{12}
\]
The terms in the imaginary part include both the retained sign
\((-1)^k\) and the scalar \(\kappa_N^\sigma\). They cannot be
dropped when calibrating a geometric action.

The normalized factorial interpolation of (10) has, on every compact
complex neighborhood of a strict real point \(0<y<x<1\),
\[
 (C_{\sigma,N})_{Ny,Nx}
   =N^{-1/2}a_\sigma(x,y)e^{N F_\sigma(x,y)}
                                  (1+O(N^{-1})),
 \tag{13}
\]
where the left side denotes that specified interpolation and
\[
 a_\sigma(x,y)=
  -e^{\sigma i\pi x}
       \left[
        \frac{2\sin\pi x}
        {(2\sin\pi y)(2\sin\pi(x-y))}
       \right]^{1/2}.
 \tag{14}
\]
The square root is positive on the real strict triangle.
All fixed derivatives have the same uniform expansion.

To prove this, replace the three \(S\)'s in (10) by \(G_N\).
Use
\[
 G_N(Nx+\delta)=N^{1/2}
       (2\sin\pi x)^{\delta+1/2}e^{NJ(x)}(1+O(N^{-1}))
\]
on its regular strip, and use the exact identity
\[
 \kappa_N^\sigma
 =\exp(\sigma i\pi N/2)\,
    \exp(-\sigma i\pi)\,
    \exp(\sigma i\pi/(2N)).
\]
For integer \(k\), either sign satisfies
\((-1)^k=e^{\sigma i\pi k}\). Continuing with this explicit
choice gives (12)--(14). In particular the minus sign in (14)
is the order-one scalar \(\exp(-\sigma i\pi)\), not a freely
chosen normalization.

If the reconstructed wires are
\(k=Nx+\delta_k\), \(r=Ny+\delta_r\), the density in (14) is
multiplied by
\[
             \exp\{\delta_k(F_\sigma)_x+
                        \delta_r(F_\sigma)_y\}.
 \tag{15}
\]
The shifts are the actual integer offsets from the original reversal
\(D-r=N(1-r/N)-1\). Thus (15) keeps the same endpoint convention
as the zero-subtree proof.

The real crossing phase has a simple geometric form:
\[
 h(x,y)=-J(1-x)-J(y)-J(x-y).
 \tag{16}
\]
The three arguments are positive and sum to one. If
\(\Lambda(\theta)=-\int_0^\theta\log(2\sin s)\,ds\), then
\(\pi h\) is the volume of an ideal tetrahedron with angles
\(\pi(1-x),\pi y,\pi(x-y)\). The identity (16) uses
\(J(1-x)=-J(x)\); the following Hessian calculation supplies
the needed concavity directly:
\[
 \begin{split}
 h_{xx}&=-\frac{\pi\sin\pi y}{\sin\pi x\,\sin\pi(x-y)},\\
 h_{yy}&=-\frac{\pi\sin\pi x}{\sin\pi y\,\sin\pi(x-y)},\\
 h_{xy}&=\pi\cot\pi(x-y),\qquad \det h''=\pi^2.
 \end{split}
 \tag{17}
\]
Both diagonal entries are negative. Thus a signed crossing adds a
regular concave real factorial block and a specified imaginary
quadratic phase. This does not make the complete complex source
positive.

## 4. The exact Newton expression at the zero-pair fold

Suppose \(p,q\ge2\), so both original degrees are at least three.
The all-zero source \(Z_{0,0}\) has the strict primitive Newton
expression and the full boundary asymptotic proved in
[the zero-subtree theorem](research_all_zero_subtree_newton_packet.md).
Its internal indices are not restricted to the low half.

For the minimal case \(p=q=2\), let the four external leaf indices
be \(a,b,c,d\). Resolve the two products using the original positive
coefficients \(\mu\). The unweighted source is exactly
\[
 Z_{0,0}(\mathbf u,\mathbf v)=
 \sum_{a,b,c,d,r}
       \mu_{abr}\mu_{cdr}\,
       e_a(u_1)e_b(u_2)e_c(v_1)e_d(v_2).
 \tag{18}
\]
All indices range from zero to \(D\), with the actual multiplication
support. The common output \(r\), rather than a complementary
constraint guessed from the angle chart, follows from \(H_{0,0}=I\).

The original trivalent zero-pair reaches a corner in the geometric
angle subdivision. In (18), its stationary point is regular:
\[
 a/N=b/N=c/N=d/N\longrightarrow
       \frac{\arctan\sqrt2}{\pi},\qquad r/N\longrightarrow\frac12.
 \tag{19}
\]
All seven factorial arguments of each gate have positive strict
slack. In particular \(r/N=1/2\) is not a boundary of this Newton
polytope. The primitive real Hessian is negative definite.
The [normalization calculation](../experiments/check_zero_subtree_newton_normalization.py)
records the full nonzero amplitude \(2^{-29/4}\).
This is an actual proved passage through the old angle fold.

For arbitrary signed \(m,n\), replace \(e_a(u_1)\) in (18) by
\[
 \sum_{a=a_0\ge a_1\ge\cdots\ge a_{|m|}\ge0}
       \prod_{j=1}^{|m|}
          (C_{\operatorname{sgn}m,N})_{a_j,a_{j-1}}\,
       e_{a_{|m|}}(u_1),
 \tag{20}
\]
and make the analogous replacement for \(e_c(v_1)\).
For power zero this means the original leaf with no new sum.
Equations (5) and (10) prove that the resulting finite sum is
exactly \(Z_{m,n}\), not a zero-power approximation to it.

On a strict chain window, its phase is the sum of:
the two original gate phases; the original boundary phases at
the final leaf indices; and the crossing phases (12) along the
two chains. The boundary phase at an angle \(\theta\) is
\[
 B(x,\theta)=\int_0^x
      \log(2\cos2\pi s+2\cos\theta)\,ds-2J(x).
 \tag{21}
\]
For an unchanged leaf it has its original input index.
For a transported leaf it has its last chain index.
The gate densities, leaf densities, crossing densities (14), and
offset factors (15) give its complete amplitude. This is a
specified holomorphic factorial normal form with no occurrence of
the old singular variable \(q=\sqrt{1+\tan^2(t/2)+\tan^2(u/2)}\).

Strict windows exist for every fixed chain length: begin at any
strict zero-source state and choose strictly decreasing positive
chain labels below each affected leaf index. Every factorial then
has real normalized argument strictly between zero and one.
There is no parity restriction on approximating such a state by
original integer labels. These facts establish regularity of the
interpolation and the exact phase. They do not assert that the
critical point for a nonzero power lies in one of these windows.

The same construction applies to two vertices of any degrees
\(p+1,q+1\ge3\): use their original binary product expression
instead of the two gates in (18). No bound on the fixed signed
powers is needed for the identity or local interpolation.

## 5. Why the established zero-power packet does not yet transfer

For zero powers the Newton expression has positive complete
weights, a unique strict real maximum, and a strict bound for every
discarded band. Applying (20) changes all three parts of that
argument. The crossing phases are oscillatory; a new complex
critical point must be found; and high input indices must still
be included.

The operator cannot simply be applied to an exponentially small
remainder and assumed to have polynomial cost in the boundary
Newton coefficients. For \(N\) divisible by four, (10) gives
\[
 \left|(C_{1,N})_{N/4,N/2}\right|
 =\frac{S_{N/2}}{S_{N/4}^{\,2}}
 =N^{-1/2}\exp(NG/\pi)(1+O(N^{-1})),
 \tag{22}
\]
where \(G\) is Catalan's constant. The leading density is exactly
one, by (14), and \(J(1/4)=-G/(2\pi)\).
Thus even one transported crossing has an exponentially large
matrix entry. The tensor-rank theorem does not control this
cancellation. Nor does the old zero-source estimate on a small
boundary-angle disk determine the operator applied to that source.

For the nonzero powers, a whole-boundary asymptotic requires a
global estimate for the exact transformed sum (20), together with
a nonzero contribution at its selected point. The known positivity
proof for \(m=n=0\) cannot be invoked after adding the oscillatory
factors. This is the remaining step, rather than a missing
normalization or a disappearance of the finite source.

## 6. Which geometric corners have been addressed

One square corner need not mean the same degeneration as (19).
The original shape factorization in
[the corner geometry calculation](research_square_corner_flat_geometry.md)
shows that a single square corner flattens four tetrahedra,
interleaved between the two original octahedra. The other square
of that edge may remain positive. The trivalent zero-pair in
Section 4 has two corner squares and is covered by the established
zero-subtree construction.

Equations (3)--(20) remain exact for arbitrary powers and do not
depend on which geometric corner is being approached. What is
not established is that every one-corner or two-corner configuration
has a strict selected Newton critical point, or that a new positive
cell decomposition exists for it. In particular, a corner
subgradient of the closed variational problem need not itself be
a limit of the same flat geometric square.

The current proved coverage is therefore as follows. All-zero
selected subtrees of original degrees at least three have the
full nonzero Newton boundary asymptotic and the compatible
[Conway geometry](research_zero_subtree_conway_geometry.md).
The independently proved two-crossing boundary theorems and
[the adjacent two-crossing theorem](research_adjacent_two_crossing_boundary_theorem.md)
give additional specified nonzero-power cases, by their own
global estimates. The exact transport here includes arbitrary
fixed powers, but supplies no new general nonzero-power
asymptotic merely from those earlier cases.

## 7. The exact cycle and the previously known crossing map

The transformation can be made before estimating any remainder.
Choose the primitive integer coordinates of the Newton expression,
including every new chain index. For each admissible integer state,
take a sufficiently small product of positively oriented circles
around its coordinates. Let \(\Gamma_N\) be the disjoint sum of
these product cycles. On each component use the exact factorial
interpolation of that summand, including the original shifts and
the crossing phases specified above. Denote it by
\(\mathscr F_N(\mathbf z;\mathbf u,\mathbf v)\). Then
\[
 Z_{m,n}
  =\frac1{(2\pi i)^K}
      \int_{\Gamma_N}
      \mathscr F_N(\mathbf z;\mathbf u,\mathbf v)
           \prod_{j=1}^{K}\pi\cot(\pi z_j)\,dz_j .
 \tag{23}
\]
Here the coordinates are unscaled integer labels; each cotangent
has residue one. All admissible states are included, including
support endpoints and high indices.

This identity is well defined locally without a global deformation:
all gate and crossing factorial arguments at an admitted state lie
between zero and \(N-1\). The boundary Newton factor has the exact
interpolation
\[
 \frac{G_N(D/2+N\theta/(2\pi))G_N(D/2-N\theta/(2\pi))}
 {G_N(D/2-r+N\theta/(2\pi))
  G_N(D/2-r-N\theta/(2\pi))G_N(r)^2}.
\]
At high \(r\), any negative-integer pole of a denominator factorial
is a zero of its reciprocal; it does not produce a pole of this
factor. For boundary angles in a fixed small complex neighborhood
of zero, its numerator is regular. Small enough circles therefore
meet no additional divisor. The recurrence of \(G_N\) gives the
original polynomial at every integer \(r\), including the removable
high-index cases. The residue theorem now proves (23) term by term.

Equation (23) preserves the whole exact source and supplies its
starting integration cycle. It does not replace that cycle by a
single saddle contour. In particular, the local regularity of the
strict windows in Section 4 does not control all the chains needed
to deform this union of cycles, or all the nonconstant lattice
modes arising in such a deformation. The positive edge criterion
and the negative real Hessian (17) are local geometric and analytic
inputs; neither bounds all these remaining terms.

The classical crossing correspondence is already in
[the exact Newton twist equations](actual_newton_twist_canonical_graph.md)
and [the crossing Casimir torus](actual_crossing_casimir_torus.md).
There is no new general torsor theorem here. The relevant convention
for (20) is worth specifying. If an input coefficient has action
\(S(x)\), a crossing step has joint phase
\(S(x)+F_\sigma(x,y)\). Put \(z=e^{2\pi ix}\) and
\(p=e^{S'(x)}\). Stationarity in \(x\), followed by the output
derivative, gives the positive-step map
\[
 (z,p)\longmapsto
 \left(\frac{z}{1+p(1-z)},-\frac{zp}{1+p}\right).
 \tag{24}
\]
The negative step is its inverse on the regular locus.
The conserved function is
\[
                  c=(1+p)(z+z^{-1})-2p.
 \tag{25}
\]
It is the classical symbol of the transpose of the Newton
multiplication-by-\(z\) matrix, which commutes with \(C_{\sigma,N}\).
On a fixed level of (25), (24) reduces to
\[
                    z\longmapsto\frac{z-1}{z+1-c}.
 \tag{26}
\]
For \(c=-2\), the coordinate \(1/(z+1)\) changes by \(1/2\).
These formulas retain the interpretation and exceptional sets
explained in the cited earlier work; they do not supply the
contour deformation missing from (23).

There are two different actions at an evaluated boundary. If
\(B(x,\theta)\) itself is the input action, then
\[
 e^{B_x}=\frac{z+z^{-1}+2\cos\theta}{2-z-z^{-1}}
 \quad\Longrightarrow\quad c=-2\cos\theta.
 \tag{27}
\]
In the actual contraction of a transported coefficient with its
output evaluation factor, however, the phase is
\(S(x)+F_\sigma(x,y)+B(y,\theta)\). Its output equation is
\[
                  e^{(F_\sigma)_y}=e^{-B_y}.
 \tag{28}
\]
Thus one must not insert \(e^{B_y}\) into the output coefficient
momentum in (25). The boundary evaluation is paired contragrediently
with that coefficient action.

The exact finite version of this distinction also retains an
endpoint term. If \(Z\) is the Newton multiplication matrix of the
spectral variable and \(v(\xi)=(e_0(\xi),\ldots,e_D(\xi))^T\), then
\[
 (Z^T-\xi I)v(\xi)
       =\frac{(-1)^N P_N(\xi)}{N^2}\,\mathbf e_D.
 \tag{29}
\]
For rows below \(D\) this is the Newton recurrence. The last row
follows from
\((c_D-\xi)e_D(\xi)=(-1)^NP_N(\xi)/S_D^2\) and \(S_D=N\).
At the physical roots (29) gives the spectral values; its derivative
at a double root gives the full first normal relation. At an arbitrary
free boundary value the displayed term must be retained.

There is an exact arbitrary-power extension of (29). Let \(r_{n,N}\)
denote the canonical polynomial in the spectral variable representing
\(R^n\), and define its polynomial divided difference
\[
 D_{r_{n,N}}(t,c)=\frac{r_{n,N}(t)-r_{n,N}(c)}{t-c}.
\]
This is a polynomial, including at \(t=c\). Since
\(C_{n,N}=r_{n,N}(Z^T)\), polynomial factorization of (29) gives
\[
 \boxed{\quad
 C_{n,N}v(c)=r_{n,N}(c)v(c)
   -\frac{\eta P_N(c)}{N^2}
       D_{r_{n,N}}(Z^T,c)\,\mathbf e_D .
 \quad}                                                   \tag{30}
\]
This is an identity for the entire free-boundary vector. For negative
powers, \(r_{n,N}(c)\) means evaluation of the canonical quotient
polynomial; it is not an off-spectrum rational power of a chosen
representative.

At \(c=-2\), the defect in (30) vanishes at odd levels, whereas
\(P_N(-2)=4\) at even levels. Even at odd levels it cannot be removed
from a boundary neighborhood. Since \(P_N'(-2)=N^2\), differentiation
gives the surviving defect
\[
 \left.
 \frac{d}{dc}\{C_{n,N}v(c)-r_{n,N}(c)v(c)\}
 \right|_{c=-2}
   =-\eta D_{r_{n,N}}(Z^T,-2)\,\mathbf e_D
                         \qquad(N\text{ odd}).             \tag{31}
\]
For \(c=-2\cos\theta=-2+\theta^2+O(\theta^4)\), it first appears
in the coefficient of \(\theta^2\). At a double physical root,
both \(P_N\) and \(P_N'\) vanish, and (30) instead gives the
corresponding value and first-normal Jordan relations.

The vector \(C_{n,N}v(c)\) in (30) is the result of treating the
Newton values as an input coefficient column. Evaluation after
applying \(C_{n,N}\) to an arbitrary polynomial coefficient column
uses the different row
\[
                     v(c)^T C_{n,N}=(M^n v(c))^T.
 \tag{32}
\]
Equations (30)--(32) specify the endpoint contribution and the two
operator roles; they provide no exponential bound or saddle
identification.

## 8. Exact algebra and normalization checks

Run

~~~sh
python3 experiments/check_corner_newton_source_transport.py --output repro/results/research-corner-newton-source-transport.json
~~~

The script checks every coefficient of the four-leg tensor at levels
\(3,4,5,8\), for powers
\((0,0),(1,-1),(2,-3),(-2,2)\), against the original crossing and
Newton multiplication matrices. It also checks both signed entries
(10) and the transpose identity (6). This is the bilinear matrix
transpose, not complex conjugate transpose; replacing it by a
Hermitian adjoint changes the original source.

At three larger levels it checks the leading phase and density
(12)--(15), for both signs and with input offsets zero and minus one.
The [saved results](../repro/results/research-corner-newton-source-transport.json)
contain sixteen full-tensor comparisons and twelve normalization
ratios. They also include fifty-six full-vector checks of (30) and
its boundary derivative: levels \(2,\ldots,8\), powers
\(-3,0,1,2\), and boundary values \(-2\) and \(0.37+0.12i\).
The divided difference is evaluated by its polynomial Newton
recurrence, without inverting \(Z^T-cI\) at a root.
These checks support the exact implementation and constants; they
are not evidence for an unproved general asymptotic or cycle
replacement.
