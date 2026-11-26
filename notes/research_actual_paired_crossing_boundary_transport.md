# Paired boundary transport for actual short crossing powers

Research deduction, 6 November 2026.

A fixed signed power of the original two-strand crossing has uniformly
bounded microscopic transport in a paired, confluent boundary
observation. This observation retains the complete Casimir jets and
the signed contractions already performed inside an attached tangle.
It does not replace that tangle by its pathwise absolute values.
The original closing row has polynomial size in this observation.

The result is a boundary statement, not a comparison of an arbitrary
closed knot value with its complete value. As a brief actual closed
case, it gives a polynomial microscopic bound for every fixed
two-strand torus knot, without a lower bound for its complete value.
The final section identifies the extra central data in the second
even meridian derivative.

Polynomial bounds for every fixed signed twist, including the
confluent channels and fixed parameter derivatives, are already
proved in [the original source bounds](actual_main_meridian_source_bounds.md),
Section 1.3. The refinement here is the exact \(2\times2\) block,
its uniformly bounded inverse and derivatives in the scaled
observation, and the explicit differentiated closing row.
It does not enlarge the set of short twists already permitted.

## 1. The original spectral boundary and its confluence

Set
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad n=N-1,\quad
 M=e^{\zeta/(2N)},\quad Y=M^2=e^{\zeta/N},
             \qquad x=-M/q .
 \tag{1}
\]
The actual stripped checked crossing \(B_N(M)\), with the common
Cartan scalar removed before the matching framing correction,
has the spectral data proved from its highest vectors in
[the meridian Casimir source](meridian_casimir_source.md), Section 1:
\[
 c_j(\zeta)=q^{-2j-1}Y+q^{2j+1}Y^{-1},\qquad
 \lambda_j(\zeta)=\nu_jY^{-j},\qquad
 \nu_j=(-1)^jq^{j(j+1)},\quad 0\le j<N.
 \tag{2}
\]
The zero-framing-normalized power is \(C_{p,N}=x^{np}B_N^p\),
where the signed integer \(p\) is fixed. This is the same local
normalization as in the
[differentiated-coupon identity](research_actual_microscopic_derivative_coupons.md).
Negative powers retain the actual inverse crossing.

Let \(A_N(\zeta)\) be an actual holomorphic two-strand tangle
intertwiner on \(V_x\otimes V_x\), with its original internal
contractions and scalars. Its external ordered colors are fixed
as these two equal colors. On the generic fiber it is a polynomial
in the total Casimir. Its canonical coefficients extend holomorphically
through \(\zeta=0\), by the integral centralizer identity in
[the intrinsic cut theorem](intrinsic_cut_and_meridian_atlas.md),
Section 3. Write \(a_j(\zeta)\) for its value on the component
with Casimir \(c_j(\zeta)\).

Pair \(j\) with \(l=n-j\), taking \(2j+1<N\), and define
\[
 u_j(\zeta)=\frac{a_j(\zeta)+a_l(\zeta)}2,\qquad
 v_j(\zeta)=\frac{a_j(\zeta)-a_l(\zeta)}{2\zeta}.
 \tag{3}
\]
The second expression has its holomorphic continuation at zero.
Indeed \(\nu_l=\nu_j\), and, with \(d_j=q^{2j+1}-q^{-2j-1}\),
\[
 c_j-c_l=-2d_j\sinh(\zeta/N),\qquad
 u_j(0)=a(c_j(0)),\quad
 v_j(0)=-\frac{d_j}{N}\,\partial_\omega a(c_j(0)).
 \tag{4}
\]
Here \(a(\omega)\) is the canonical complete polynomial of the
actual tangle, not just its values on the reduced node set.
For odd \(N\), the unpaired channel \(j=n/2\) keeps its value.
There are no other node collisions in \(0<|\zeta|<\pi\).

Thus (3) retains every original complete spectral jet.
For all paired channels,
\[
 \frac4{N^2}\le \frac{|d_j|}{N}\le\frac2N .
 \tag{5}
\]
Consequently this complete observation and the unscaled
value-and-first-Casimir-derivative observation are equivalent
with polynomial factors in \(N\). No exponentially ill-conditioned
Vandermonde inversion is used to define (3).

## 2. A bounded exact block for a short crossing

Put
\[
 \chi_{p,N}=(-q^{-1})^{np},\qquad
 \kappa_j=\frac{p(n-2j)}{2N},\qquad |\kappa_j|\le |p|/2 .
 \tag{6}
\]
The two eigenvalues of \(C_{p,N}\) on a pair are exactly
\(\chi_{p,N}\nu_j^p e^{\kappa_j\zeta}\) and
\(\chi_{p,N}\nu_j^p e^{-\kappa_j\zeta}\).
Therefore stacking this actual crossing power with the attached
tangle gives
\[
 \binom{u_j^{\,\mathrm{new}}}{v_j^{\,\mathrm{new}}}
 =\chi_{p,N}\nu_j^p
 \begin{pmatrix}
  \cosh(\kappa_j\zeta)&\zeta\sinh(\kappa_j\zeta)\\
  \sinh(\kappa_j\zeta)/\zeta&\cosh(\kappa_j\zeta)
 \end{pmatrix}
 \binom{u_j}{v_j}.
 \tag{7}
\]
The lower-left entry is entire, with value \(\kappa_j\) at zero.
The matrix has determinant one; changing \(p\) to \(-p\)
gives its inverse, including the inverse unit phase.
On the odd-level unpaired channel the multiplier is the
constant \(\chi_{p,N}\nu_{n/2}^p\).

For every fixed disk and every fixed derivative order, the blocks
in (7), their inverses, and their derivatives are bounded by a
constant depending only on that disk, \(p\), and the order.
These bounds are independent of \(N\). They follow directly
from \(|\kappa_j|\le|p|/2\) and the entire power series.
They also control a finite composition of prescribed short
powers in this same two-strand channel.

At zero, the nontrivial nilpotent part has not been erased:
after removing the unit phase the block and its second derivative
are
\[
 \begin{pmatrix}1&0\\\kappa_j&1\end{pmatrix},
 \qquad
 \begin{pmatrix}
   \kappa_j^2&2\kappa_j\\
   \kappa_j^3/3&\kappa_j^2
 \end{pmatrix},
 \tag{8}
\]
and its first derivative is zero. These are the actual
meridian confluence of the crossing, not an assumed diagonal
complete crossing.

## 3. The original closing row and the retained derivative data

For a two-strand intertwiner, the exact intrinsic pivotal cut is
\[
       t_{V_x\otimes V_x}(A)
          =\sum_{j=0}^{N-1}\frac{d_{x^2Q^{-j}}}{d_x}\,a_j,
 \tag{9}
\]
with the original dimension
\[
 d_z=-q^{N(1-N)/2}\frac{qz-q^{-1}z^{-1}}{z^N-z^{-N}}.
 \tag{10}
\]
This is an identity proved from actual Casimir moments and
partial traces in the intrinsic cut theorem, Sections 1–3.
It is not an assumed positive trace. Direct substitution gives
\[
 \frac{d_{x^2Q^{-j}}}{d_x}
 =\frac{(-1)^N
        (q^{-2j-1}Y-q^{2j+1}Y^{-1})}
              {4\sinh(\zeta/(2N))\cosh(\zeta/2)}.
 \tag{11}
\]
The individual terms may have a pole at zero; their original
paired combination does not.

Write \(c_j^0=q^{2j+1}+q^{-2j-1}\). On the pair (3), the
exact contribution to (9) is
\[
 \frac{(-1)^N}{\cosh(\zeta/2)}
 \left[
  c_j^0\cosh\!\left(\frac{\zeta}{2N}\right)u_j
  -\frac{d_j\zeta\cosh(\zeta/N)}
                    {2\sinh(\zeta/(2N))}\,v_j
 \right].
 \tag{12}
\]
For odd \(N\), the unpaired contribution is
\(\cosh(\zeta/(2N))a_{n/2}/\cosh(\zeta/2)\).
Thus the apparent pole at zero cancels before any estimate.
At zero (12) is
\((-1)^N(c_j^0a+(d_j)^2\partial_\omega a)\),
the original complete spectral-jet trace, including its parity.

Let \(\mathbf a_N\) denote all the coordinates (3) and the
unpaired value, and let \(\Lambda_N(\zeta)\) be the row (12).
For \(0<r<R<\pi\), its coefficients and their fixed derivatives
are \(O_R(N)\); summing at most \(N\) coordinates gives
\[
 \|\Lambda_N\|_{\ell^\infty\to\mathbb C}
                       \le C_R N^2 .
 \tag{13}
\]
Together with (7), this proves an actual boundary-retaining bound
for the closed source obtained by attaching the crossing power:
\[
 \sup_{|\zeta|\le r}
  \left|\partial_\zeta^k
     t_{V_x\otimes V_x}(C_{p,N}A_N)\right|
       \le C_{p,r,R,k}N^2
              \sup_{|\zeta|\le R}\|\mathbf a_N(\zeta)\|_\infty .
 \tag{14}
\]
The entries on the right are the already contracted signed
boundary values of the remaining actual tangle. Cauchy's
formula supplies the derivative bound on the smaller disk.

If \(\mathbf C_{p,N}\) denotes the block map (7), the exact
first derivative before estimating is
\[
 \partial_\zeta(\Lambda_N\mathbf C_{p,N}\mathbf a_N)
  =\Lambda_N'\mathbf C_{p,N}\mathbf a_N
     +\Lambda_N\mathbf C_{p,N}'\mathbf a_N
     +\Lambda_N\mathbf C_{p,N}\mathbf a_N'.
 \tag{15}
\]
In particular the moving closing row and the boundary derivative
are retained. A derivative of a single raw matrix crossing is
not identified with the middle term alone: a moving fusion
frame redistributes its connection terms into the other
terms in (15).

Both \(\mathbf C_{p,N}\) and the exact closing row
\(\Lambda_N\) are even functions of \(\zeta\): this follows
entrywise from (7), (12), and the odd-level singleton formula.
The attached observation \(\mathbf a_N\) need not be even.
At completeness the second derivative therefore has the
particularly simple exact form
\[
 \left.\partial_\zeta^2
       (\Lambda_N\mathbf C_{p,N}\mathbf a_N)\right|_0
 =\Lambda_N''(0)\mathbf C_{p,N}(0)\mathbf a_N(0)
   +\Lambda_N(0)\mathbf C_{p,N}''(0)\mathbf a_N(0)
   +\Lambda_N(0)\mathbf C_{p,N}(0)\mathbf a_N''(0).
 \tag{15a}
\]
There is no first boundary-normal term. The first two terms
have polynomial size in the complete boundary observation,
using (8) and (13). The last term retains the even normal
of the actual attached source. No estimate of
\(\mathbf a_N''(0)\) by \(\mathbf a_N(0)\), or of either
by the final complete scalar, follows from this identity.

This supplies bounded short-power transport of the full
confluent boundary observation. It does not bound that
observation by the one final closing scalar. A physical
quarter-turn or a change of pairing also requires its actual
source adapter; (7) is not a free identification of different
pairings. These are precisely the additional steps needed
before (14) can prove a signed observation estimate for a
general attached source.

In particular the
[physical turn comparison](actual_main_meridian_turn_comparison.md),
Section 6, controls the meridian-dependent correction polynomially
relative to the original complete turn. Its complete coordinate
reflection and its carrier maps remain. Neither that comparison
nor (7) says that a quarter-turn preserves this paired observation
with bounded cost, or that its observation is controlled by a
single signed closing value.

## 4. Brief closed consequence: fixed two-strand torus knots

For \(A_N=I\), the boundary coordinates are \(u_j=1,v_j=0\)
and the unpaired value is one. If \(p\) is a fixed signed odd
integer, the closure is the zero-framed knot \(T(2,p)\).
Equations (7), (11) give its exact finite formula
\[
 \begin{split}
 F_{p,N}(e^{\zeta/N})
 ={}&\frac{(-1)^Nx^{np}}
          {4\sinh(\zeta/(2N))\cosh(\zeta/2)}
 \sum_{j=0}^{N-1}
 (q^{-2j-1}Y-q^{2j+1}Y^{-1})\,\nu_j^pY^{-pj}.
 \end{split}
 \tag{16}
\]
Every scalar and pivot is retained. As a normalization check,
at \(p=1\) the finite sum telescopes to
\(q^{-1}(Y-1)(1+Y^{-N})\), and (16) is exactly one.

On a fixed circle avoiding the zeros of \(\cosh(\zeta/2)\)
and zero itself, the prefactor in (16) is \(O_{p,R}(N)\)
and each of its \(N\) summands is \(O_{p,R}(1)\).
The actual reduced invariant is entire in \(\zeta\).
Choosing a larger such circle and applying the maximum
principle and Cauchy's formula therefore gives, for every
fixed disk and fixed derivative order,
\[
       \sup_{|\zeta|\le R}
        |\partial_\zeta^kF_{p,N}(e^{\zeta/N})|
                              \le C_{p,R,k}N^2 .
 \tag{17}
\]
This includes the canceled confluences and both level parities.

The canonical ordinary-color interpolant has the same \(O_R(N^2)\)
bound, since this is a two-strand braid. Subtract it and divide
by \(S_N(e^{\zeta/N})=Ne^{(N-1)\zeta/(2N)}H_N(\zeta)\)
only on a larger fixed circle avoiding the zeros of \(H_N\).
The regular quotient already exists, so the maximum principle
across all interior resonances proves
\[
 \sup_{|\zeta|\le R}
       |\partial_\zeta^k R_{p,N}(e^{\zeta/N})|
                              \le C_{p,R,k}N .
 \tag{18}
\]
No lower bound or division by \(K_{p,N}\) occurs. In particular
the signed insertion condition (21) of the differentiated-coupon
note holds here with \(a_N=0\) and \(B_N=O(N^2)\).
This is a nonhyperbolic closed calibration of the source
estimate; it does not advance the hyperbolic filling class
by itself.

## 5. What the second even normal of a central source retains

There is a precise reason not to replace all second derivatives
by multiplication with a Casimir element on the complete fiber.
In the actual equal-color algebra, put
\[
 P_0(\omega)=\mathcal T_N(\omega)+2,\qquad
 \Delta(\zeta)=2\cosh\zeta-2,\qquad
 P_\zeta=P_0+\Delta(\zeta),\qquad s_0=(-1)^{N-1}N^2 .
 \tag{19}
\]
After separating the original scalar cut factor, the primitive
closing functional of the
[actual Newton compiler](actual_main_meridian_newton_compiler.md),
Section 5, is
\[
 \phi_\zeta(F)=s_0[\omega^{-1}]
                      \frac{F(\omega)}{P_0(\omega)+\Delta(\zeta)}.
 \tag{20}
\]
The coefficient is at infinity. This is polynomial division
and retains repeated-root derivatives. For a holomorphic
polynomial family \(F_\zeta\), direct differentiation gives
\[
 \left.\partial_\zeta^2\phi_\zeta(F_\zeta)\right|_0
  =\phi_0(\ddot F_0)
          -2s_0[\omega^{-1}]\frac{F_0(\omega)}{P_0(\omega)^2}.
 \tag{21}
\]
The first term includes the actual variation of the attached
coupon. The second term is a functional on the first
thickening \(\mathbb C[\omega]/(P_0^2)\), rather than on
\(\mathbb C[\omega]/(P_0)\): it does not vanish on
\(P_0\omega^{N-1}\). Hence no fixed complete Casimir multiplier
represents it on all unreduced products.

For an immediate product of two fixed degree-\(<N\)
polynomials, this second term vanishes by degree. Subsequent
multiplication need not preserve that vanishing. The actual
nine-input junction in the
[same-index trace calculation](actual_main_meridian_same_index_obstruction.md)
has
\(\mathcal Z_a(\zeta)=\mathcal Z_a(0)
       +(-1)^a\Delta(\zeta)\mathcal B_a\);
its second normal has the exponentially large ratio
\(2\mathcal B_a/\mathcal Z_a(0)\) already quantified there.
This is a tensor-entry fact, not a failure of a whole-knot
bound. Formula (21) identifies the additional boundary data
which that actual source calculation retains. Paired Weyl
symmetry kills the first odd normal but does not remove
this even conormal term.
