# A finite-dimensional relative period for the original Borel source

Private written proof, 18 November 2026.

The original highest-cut source has an exact local Borel-period
representation before the finite Poisson, normal-product and hard
Wick operations are eliminated. The representation keeps the original
soft endpoint. Its amplitude is a finite product of literal scalar
defect factors, whose filtered Borel continuations are available.
The remaining global problem is transport of a specified relative
cycle in this finite-dimensional space.

No infinite Gaussian or Laplace integral is asserted to converge.
Gaussian integrals in the formal coefficient calculation mean Wick
functionals. The Borel chains constructed below are compact actual
chains, and their integrals are convergent analytic germs.

## 1. Source and statement

Use the finite word, highest-cut projector, pivot, framing and clocks
of [G]. Let \(\alpha\ne0,1\) be a simple Alexander zero and put
\[
 z=Y-\alpha,\qquad
 C(Y)=B(I-B)^{-1}=uv^T/z+G(Y),\qquad
 r(Y)=z/\Delta_K(Y).
 \tag{1}
\]
The fixed residue vectors and the holomorphic hard covariance are
the original ones. There is no eigenvector normalization or inverse
of the highest-cut projector. The exact source identity is
\[
 \mathscr W_m(h,Y)=r(Y)\mathfrak L_z[\mathcal H],
 \qquad \mathfrak L_z[t^n]=n!z^{-n-1}.
 \tag{2}
\]
The scaled soft variable is \(x=ht\). On the common coefficient
disk of [D,G], write
\[
 \mathcal H_{\rm scaled}
   =e^{\Psi_0(Y,x)/h}a(h,Y,x,m),\qquad
 f(Y,x)=zx-\Psi_0(Y,x),\qquad \Psi_0=O(x^2).
 \tag{3}
\]
All stage marks are first independent and are then specialized to
the original \(\mathbf t=hm\). Bounds below are uniform on any
prescribed compact clock set after shrinking the coefficient disks.

**Theorem.** A finite number \(2d\) of auxiliary variables \(X\),
a constant invertible symmetric cross covariance \(K\), and analytic
functions can be constructed directly from the literal word so that
\[
 \mathcal H_{\rm scaled}
   =\mathbb E_{hK}\!
       \left[e^{\mathcal P(Y,x,X)/h}
                         \mathcal A(h,Y,x,X,m)\right].
 \tag{4}
\]
The equality is the original formal coefficient identity, with its
small stationary branch. The raw amplitude
\(\mathcal A=\sum_{j\ge0}h^j\mathcal A_j\) obeys
\[
             \|\mathcal A_j\|\le MC^j j!
 \tag{5}
\]
on common disks. It is a finite product of literal scalar defect
exponentials and analytic-\(h\) factors. The phase is independent
of the fixed clocks \(m\).

Set
\[
 \mathcal F(Y,x,X)=zx+\tfrac12X^TK^{-1}X-\mathcal P(Y,x,X).
 \tag{6}
\]
Its small stationary point in \(X\) is nondegenerate; its critical
value is exactly \(f(Y,x)\). Fix the normalized Gaussian volume
form \(\Omega_K\) specified in Section 4, and put
\(\widehat{\mathcal A}(s)=\sum\mathcal A_js^j/j!\).
For each sufficiently small fixed \(z\ne0\), there is an explicit
local compact relative chain \(\mathcal D_\xi(Y)\), with boundary
on \(x=0\) and \(\mathcal F=\xi\), such that the original ordinary
Borel germ is
\[
 \boxed{\quad
 b_m(Y,\xi)=r(Y)\,\partial_\xi^{d+1}
   \int_{\mathcal D_\xi(Y)}
      \widehat{\mathcal A}
         \bigl(\xi-\mathcal F(Y,x,X),Y,x,X,m\bigr)
                         \,dx\wedge\Omega_K .
 \quad}
 \tag{7}
\]
The derivative acts on the whole analytic integral, including its
moving chain. It does not hold that chain fixed.

Formula (7) constructs the full local source, including its prefix,
not just the difference of two inverse branches. It gives no
automatic continuation to a large cutoff or through an escaping
fiber. Those require the continued integrand and the complete
relative chain on the same swept domain.

## 2. Zero-safe literal Poisson blocks

For \(q\) variables use
\[
 K_\times=\begin{pmatrix}0&I_q\\ I_q&0\end{pmatrix},
 \qquad
 \mathbb E_{hK_\times}e^{a\cdot X+b\cdot\Xi}
                                      =e^{h a\cdot b}.
 \tag{8}
\]
For a polynomial \(F\), direct differentiation gives the exact
identity
\[
 \mathbb E_{U/h}F(hN)
   =\mathbb E_{hK_\times}
       F(X)\exp\left\{\frac1h
                       \sum_i U_i(e^{\Xi_i}-1)\right\}.
 \tag{9}
\]
Indeed the right side applies
\(\exp\{\sum_i(U_i/h)(e^{h\partial_{X_i}}-1)\}\)
to \(F\) at zero. Equivalently, its generator at \(F=e^{aX}\)
is \(\exp\{\sum_iU_i(e^{ha_i}-1)/h\}\), the exact Poisson
moment generator. This proves (9) without dividing by any \(U_i\).
The minus one already includes the Poisson normalization; no
additional factor \(e^{-\sum U_i/h}\) is inserted.

The literal entry logarithms of [D] regroup as
\[
 \sum_{j\ge1}h^jv_j(N)
     =h^{-1}V_0(hN)+\sum_{a\ge1}h^{a-1}V_a(hN),
 \qquad \|V_a\|\le MC^a a!,\qquad V_0=O(s^2).
 \tag{10}
\]
The signed analytic \(V_0\)'s and the three bilinear means \(U\)
are those printed in [P, (15)--(18)]. Thus (9) turns each
normalized literal Poisson kernel into a finite cross-Wick block
with principal potential
\[
               V_0(X)+\sum_iU_i(e^{\Xi_i}-1)
 \tag{11}
\]
and scalar amplitude
\(\exp\{\sum_{a\ge1}h^{a-1}V_a(X)\}\).
The actual division by its classical kernel and the invertible
classical field substitutions are retained exactly as in [D,P].
They are not inferred anew from (9).

The formal topology is the original field/mean topology. At fixed
original quantum order the literal logarithm is a finite polynomial.
The Poisson generator identity therefore applies coefficientwise.
After regrouping, stationary translation and quadratic resummation
are the analytic continuations of those same coefficients from
[D]. A small value of a mean, including zero, causes no pole.
The stationary equations for (11) are
\[
             X_i=U_i e^{\Xi_i},\qquad \Xi_i=\partial_iV_0(X).
 \tag{12}
\]
Their Jacobian is a unit at \(U=0\). This also directly verifies
nondegeneracy of the auxiliary quadratic phase near that point.

## 3. Flattening the entire finite word

The scaled normal product is the exact cross-Wick operation
\[
 A\star_h B
  =\mathbb E_{hK_\times}^{\,r,s}
                  A(Z,P+r)B(Z+s,P).
 \tag{13}
\]
Introduce a separate pair \((r,s)\) at each multiplication.
Replace every local factor by (9), with its own variables.
The integrand becomes the product of finitely many scalar
amplitudes and the exponential of the sum of finitely many analytic
principal potentials. Their arguments are the actual shifted
fields and fixed classical linear substitutions.

Wick functionals in disjoint variable sets commute: on exponential
generators this says that their covariances add in separate blocks.
Differentiating the generators proves the coefficient identity
for polynomials. It consequently proves Fubini for these finite
formal constructions, first in the original field and mark
topologies. Thus nested operations can be flattened rather than
replaced by an independently chosen stationary model.

The hard covariance in the ordered \((Z,P)\) variables is
\[
 K_G=\begin{pmatrix}0&G^T\\G&0\end{pmatrix}.
 \tag{14}
\]
It need not be invertible. Use one further invertible cross block,
and in its arguments substitute
\[
              (Z,P)=(Z',GP'),\qquad
              T=\operatorname{diag}(I,G).
 \tag{15}
\]
Then \(TK_\times T^T=K_G\), so (15) reproduces every actual hard
Wick pair. No inverse or constant-rank assumption on \(G\) is used.
Taking the direct sum of all cross blocks gives the constant
invertible \(K\) in (4).

The highest cut remains in \(B=L_\beta T_0\), hence in (1).
Only unmarked invertible classical substitutions have been moved.
The pivot is its original \(I+O(h)\) substitution. Its relative
scaled symbol, the scalar framing, and the specialization
\(\mathbf t=hm\) all have analytic-\(h\) amplitude logarithms
on compact clock sets. They are included in \(\mathcal A\).
They do not change the clock-independent principal phase.

To write the result analytically in the single soft variable,
choose a fixed sufficiently small nonzero \(A_*\), and in the
soft means set
\[
                 Z_{\rm soft}=vA_*,
       \qquad P_{\rm soft}=u\,x/A_*.
 \tag{16}
\]
For small \(x\) both fields remain in the original common disks.
Balancedness makes the final contraction equal to the same function
of \(x=AB_s\) as [G]; (16) is a local field slice, not a new
endpoint or a change to the highest cut. In particular the
original soft endpoint remains exactly \(x=0\).

Every raw amplitude logarithm in this construction is a finite
sum of the defect terms in (10) and analytic-\(h\) corrections.
For its coefficient of \(h^j\), the bound on \(V_{j+1}\) is
at most \(M C_1^j j!\), after enlarging \(C_1\).
Exponentiation preserves this bound: in each ordered composition
of \(j\), the product of the factorials is at most \(j!\), and
the number of compositions is at most exponential in \(j\).
Finite products and analytic substitutions preserve common disks.
This proves (5) directly before any hard integration.

The flat phase has the same small stationary solution as the
successive local constructions in [D,P]. More explicitly, eliminate
the auxiliary blocks in their finite original order. Each eliminated
Hessian is a unit by the local Poisson and normal-product implicit
equations. The next Hessian is its Schur complement. Hence the
determinant of the full Hessian is the product of these unit
determinants and is a unit. The embedding (15) preserves this check:
\[
 \det(I-K_\times T^THT)=\det(I-TK_\times T^TH).
 \tag{17}
\]
The identity follows by evaluating the determinant of a two-by-two
block matrix in the two orders. Its right side is precisely the
old hard unit determinant. Consequently (6) has a unique small
analytic stationary point \(X_*(Y,x)\) with nondegenerate Hessian.
Its critical value equals \(f(Y,x)\), because finite stationary
elimination is the principal coefficient of the same formal source.
This uses only the small hard Jacobian, not \(f_{xx}\ne0\).

## 4. Gaussian normalization and an actual local relative chain

Choose a constant invertible complex matrix \(S\) with \(SS^T=K\).
For a cross block one may obtain it by a fixed linear diagonalization
and square roots of its nonzero diagonal entries. Define
\[
          \Omega_K=(2\pi)^{-d}(\det S)^{-1}
                                     dX_1\wedge\cdots\wedge dX_{2d}.
 \tag{18}
\]
The oriented Gaussian plane is \(S\mathbb R^{2d}\), with its
orientation transported from the usual real orientation. This
fixes the determinant sign. In the pure quadratic model its
normalized formal Gaussian value is one.

A parameter-dependent holomorphic change of variables near
\(X_*(Y,x)\) puts the phase in the form
\[
             \mathcal F(Y,x,X(Y,x,q))
                     =f(Y,x)+\tfrac12\sum_{\nu=1}^{2d}q_\nu^2 .
 \tag{19}
\]
For completeness this follows by completing one square at a time.
After a constant linear change some quadratic coefficient is a
unit; solve its first derivative for the critical coordinate,
subtract that coordinate, and absorb the remaining analytic
unit by its continued square root. Repeat on the nondegenerate
Schur complement. This is a finite analytic construction with
parameters, and its orientation is the continuation of (18).

The formal Gaussian calculation is invariant under this change.
For a linear change this follows on generators and determinants.
For the nonlinear part interpolate its convergent Taylor change
from the identity. Differentiation gives a total divergence of
the formal integrand. Gaussian integration by parts
\(\mathbb E_{hK}(X_iF)=h\sum K_{ij}\mathbb E_{hK}\partial_jF\)
annuls that divergence, with the Jacobian term included.
After stationary scaling, each fixed \(h\)-coefficient uses only
finitely many Taylor coefficients of the nonlinear change.
Thus this verification is coefficientwise and requires no
convergence of a Gaussian integral at infinity.

Fix small \(z\ne0\). Since \(f_x(Y,0)=z\), the map
\(t_0=f(Y,x)\) has the original local inverse \(x(Y,t_0)\).
In (19), define the chain \(\mathcal D_\xi\) by
\[
 t_0=\xi s,\qquad q=\sqrt{\xi}\,v,\qquad
 s\ge0,\quad v\in\mathbb R^{2d},\quad
                       s+\tfrac12|v|^2\le1 .
 \tag{20}
\]
Map it back using these local inverse coordinates. Its real
dimension is \(2d+1\), and its two genuine boundary portions are
\[
           x=0,\qquad \mathcal F=\xi.
 \tag{21}
\]
The lower total-energy end collapses. The square root and orientation
in (20) are initially fixed along a ray. A full turn of \(\xi\)
replaces \(v\) by \(-v\); in even dimension \(2d\) this preserves
the orientation. The period therefore has an ordinary analytic
germ at \(\xi=0\), not a new half-integer normalization.

More directly, expand the analytic integrand in \(t_0,q\).
Odd powers of any \(v_\nu\) integrate to zero. Every remaining
power of \(\sqrt{\xi}\) is even, and the chain volume contributes
\(\xi^{d+1}\). Uniform convergence on a smaller compact parameter
set proves holomorphy and the ability to differentiate the integral
in (7). By (5), \(\widehat{\mathcal A}\) converges on a common
small \(s\)-disk. On (20),
\(|\xi-\mathcal F|\le|\xi|\), so its substitution is legitimate.
The case \(d=0\) is simply the original inverse interval
\(0\le t_0/\xi\le1\), with no Gaussian sphere.

## 5. Exact coarea and Borel factorials

Let \(\delta_t\) be the top relative fiber in (20) at total energy
\(t\). If
\(d\mathcal F\wedge\Omega_{\mathcal F}=dx\wedge\Omega_K\),
use the induced orientation and define
\[
 G_j(Y,t,m)=\int_{\delta_t}
                  \mathcal A_j(Y,x,X,m)\,\Omega_{\mathcal F}.
 \tag{22}
\]
This is a relative fiber chain with boundary on \(x=0\), not an
unrestricted closed fiber cycle. Local coarea in the coordinates
of (20) gives the exact analytic identity
\[
 \int_{\mathcal D_\xi}\widehat{\mathcal A}(\xi-\mathcal F)
                              \,dx\wedge\Omega_K
       =\sum_{j\ge0}\int_0^\xi
                    \frac{(\xi-t)^j}{j!}G_j(Y,t,m)\,dt .
 \tag{23}
\]
The orientations make this an iterated integral in increasing
total energy. The power expansion has the form
\[
                    G_j(t)=\sum_{n\ge0}g_{j,n}t^{n+d}.
 \tag{24}
\]
In the pure quadratic model with amplitude one and \(f=zx\),
the sphere normalization (18) gives
\[
          G_0(t)=\frac{t^d}{z\,d!}.
 \tag{25}
\]
One can check this by the elementary Gaussian sphere integral:
in \(2d\) variables the normalized density is
\(t^{d-1}/(d-1)!\); integrating the soft variable adds one
power and divides by \(z\). Equation (25) also holds for \(d=0\).

For each term of (24), beta integration in (23) gives
\[
 \int_0^\xi\frac{(\xi-t)^j}{j!}t^{n+d}\,dt
             =\frac{(n+d)!}{(n+d+j+1)!}\xi^{n+d+j+1}.
 \tag{26}
\]
After \(d+1\) derivatives this is
\((n+d)!\xi^{n+j}/(n+j)!\).
The corresponding formal endpoint-Gaussian rule is
\[
 h^{-d-1}h^j\int_0^\infty e^{-t/h}t^{n+d}\,dt
                         =(n+d)!\,h^{n+j}.
 \tag{27}
\]
Here the integral sign in (27) denotes its factorial moment,
not an analytic infinite contour. Equations (26)--(27) are
exactly the ordinary Borel convention.

By Sections 2--3 the formal Gaussian part of (27) is the original
finite word. Its remaining soft factorial is precisely (2).
Thus all coefficients of (7) equal the original source coefficients.
Both sides are analytic Borel germs for fixed small \(z\ne0\);
they are therefore the same germ. In the pure model (7) is
\(r/z\), fixing the scalar normalization as well as the sign.
For \(d=0\), differentiation of (23) gives
\[
 r\left[
 \frac{\mathcal A_0(Y,x)}{f_x(Y,x)}
 +\int_0^x
   \partial_s\widehat{\mathcal A}
       (f(Y,x)-f(Y,t),Y,t)\,dt\right],
 \tag{28}
\]
which is exactly [G]'s full-prefix reconstruction.

## 6. What the raw amplitude can already continue

Before Wick integration, the logarithm of \(\mathcal A\) is a finite
sum of literal interval defect logarithms, with the original upper
and lower endpoint branches, plus functions analytic in \(h\).
The latter include the retained pivot, framing, and fixed-clock
factors; their ordinary Borel derivatives are entire in the Borel
variable on each buffered parameter chart.

Consequently [C] applies directly to this finite scalar sum.
For a fixed compact endpoint/field chart, let \(\Omega\) be the
union of its candidate scalar Borel poles at a parameter base.
For finite length bound \(L\), retain the finite filtered sums
\[
 \Sigma_L=\{0\}\cup
 \left\{\sum\omega_i:\omega_i\in\Omega,\
                              \sum|\omega_i|\le L\right\}.
 \tag{29}
\]
The original initial segment and every subsequent path satisfying
[C]'s positive length margin and separation from the appropriate
\(\Sigma_{L+\varepsilon}\) give actual continued germs of
\(\widehat{\mathcal A}\). The convolution simplices, their endpoint
constants and their primitive histories are carried unchanged.
Shrinking a parameter chart retains the common pole buffers and
gives joint continuation. The unfiltered additive set is not
assumed locally finite.

This is a continuation statement for the raw integrand in (7),
before stationary elimination. It does not say that all differences
\(\xi-\mathcal F(Y,x,X)\) swept out by a global relative chain
automatically satisfy these conditions. Such a chain must remain
in the joint continued domain of that integrand, with its chosen
lifts. Finite source dimension alone does not supply compactness.

## 7. Boundary and global scope

Formula (7) supplies an exact finite-dimensional relative model for
the actual source. The lower boundary is \(x=0\); the upper boundary
is \(\mathcal F=\xi\). Both survived the flattening and the Borel
transform. A subsequent finite cutoff also retains its prescribed
\(\xi=0,R\) endpoints. Changing a primitive base or replacing the
relative chain by a local vanishing cycle would change these data.

For a compact deformation on a common continued integrand domain,
ordinary holomorphic-chain transport and Stokes preserve the
continued period, with all swept boundary portions included.
This elementary observation does not construct such a deformation
to the geometric observation point. Critical fibers, coefficient
divisors, other action branches and escape of the relative chain
must all be controlled for that purpose.

In particular the local model is not a proof that the original
cap has nonzero intersection with a geometric thimble, nor that
large positive damping cutoffs can be reached on this source.
No root-of-unity scalar lower or finite-exception statement is
inferred. The new construction identifies the exact integrand
and relative cycle whose global transport is still required.

## 8. Complete proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| D | notes/research_actual_symbol_factorial_deficiency.md | a757e1ac8f6e62268cd7c2d681758a0258394661181026aace2cd516f4ca3359 |
| P | notes/research_actual_analytic_principal_phase.md | 9ae7b5df2dbd955ee6ac4580590d9f21d1b1750bcdd6c5085e7322251ab70bcb |
| G | notes/research_actual_borel_phase_surface.md | ba682a18ac0ae3efa05ffbc7e6fef02c128800ccbbffda1867756ba5a8275429 |
| C | notes/research_filtered_scalar_borel_convolution_flow.md | a3f29d80d3b5388a88d889de5903d155357c580d573018f952e0fd2bace4d825 |

All four complete sources were read and their used implications
checked. D and P supply the literal kernel and finite Wick identities;
G supplies the actual soft functional and Borel normalization;
C supplies filtered scalar exponentiation with original histories.
The finite flattening, relative coarea chain and factorial adapter
are proved above. Only written mathematics and source-text/hash
operations were used. Frozen notes and public manuscripts are unchanged.
