# The actual Borel source on its analytic phase surface

Private written proof, 18 November 2026.

The original highest-cut source has a convergent Borel reconstruction
on an analytic phase surface at every simple Alexander zero. No
quadratic soft coefficient or scalar annihilator hypothesis is needed.
On that surface its pole divisor is exactly the critical divisor of
the phase. All primitives retain the original endpoint.

When the soft phase has any finite nonzero order at the limiting
meridian, the construction gives all nearby critical branches and
their nonzero local minors. It does not identify a hyperbolic
component or a coefficient in the physical root-of-unity cycle.

## 1. The literal source and the hypotheses actually used

Fix the original one-component braid and highest-cut source of [F].
Use its natural coordinate
\[
 Q=e^h,\qquad x=x_0e^{-h/2},\qquad x_0^2=Y,
 \qquad T_0=\operatorname{diag}(0,1,\ldots,1).
 \tag{1}
\]
Let \(\alpha\ne0,1\) be a simple zero of the original normalized
Alexander polynomial, and put \(z=Y-\alpha\). Choose a local
holomorphic square root \(x_0\). Independent stage marks are
\(e^{t_i}\); the original clocks are \(t_i=hm_i\), with the
same fixed linear specialization to matching-lattice clocks.

Move only the unmarked invertible classical substitutions to the
right of the actual finite word. Its exact coefficientwise trace is
\[
 \mathscr W_m(h,Y)=x_0^c
       \operatorname{Tr}\bigl[\mathcal A_h(Y,m)\Gamma(B(Y))\bigr],
 \qquad B=L_\beta(x_0)T_0.
 \tag{2}
\]
Here \(\mathcal A_h=1+O(h)\) at clock specialization, and it
retains the original pivot and framing correction. This is the
finite-word realization in [F] and [D]. The trace is initially
degree by degree before its coefficientwise rational grading
continuation. No inverse of \(T_0\) is used.

Write \(S_h(Z,P,m)\) for the ordinary normal symbol of
\(\mathcal A_h\). At every fixed order in \(h\) it is a balanced
polynomial in \(Z,P\), with polynomial clock dependence. The
balanced condition means equal total creation and differentiation
degrees in each monomial.

The determinant identity of [F] is
\[
 \det(I-B)=x_0^c\Delta_K(Y).
 \tag{3}
\]
Set \(C=B(I-B)^{-1}\). Simplicity of the zero in (3) implies
\[
 C(z)=\frac{uv^T}{z}+G(z),\qquad
 r(z)=\frac{z x_0^c}{\det(I-B)},\qquad
                    r(0)=\Delta_K'(\alpha)^{-1}\ne0,
 \tag{4}
\]
with constant vectors \(u,v\), nonzero rank-one product \(uv^T\),
and holomorphic \(G\). Indeed if \(I-B(\alpha)\) had corank at
least two, its adjugate would vanish and the determinant derivative
would be zero. Its adjugate therefore has rank one and is nonzero.
The Laurent expansion of \((I-B)^{-1}\), and
\(C=(I-B)^{-1}-I\), prove (4). Algebraic simplicity of an
eigenvalue is not required, nor is a normalization \(v^Tu=1\).

No condition on an actual quantum annihilator is imposed below.
In particular there is no assumption about \(P_{LL}\), a two-branch
classical crossing, or a nonzero quadratic soft coefficient.

## 2. Exact soft moments and a common analytic coefficient disk

For a polynomial normal symbol \(g\), the literal trace is
\[
 \operatorname{Tr}\bigl[:g(Z,\partial):\Gamma(B)\bigr]
       =\det(I-B)^{-1}\mathbb E_C g,
 \qquad \mathbb E_C(P_iZ_j)=C_{ij}.
 \tag{5}
\]
One direct verification uses the generating exponential. For one
diagonal eigenvalue \(b\), the trace of \(Z^d\partial^d\Gamma(b)\)
is \(d!b^d/(1-b)^{d+1}\), by differentiating the geometric
series. Products give
\(\det(I-B)^{-1}\exp(t^TCs)\) for the symbol
\(e^{s\cdot Z+t\cdot P}\) on diagonal matrices. Conjugation gives
the formula on a dense set of diagonalizable matrices, and clearing
determinants proves the rational identity for every matrix. Applying
it with a grading parameter first proves (5) for the original
coefficientwise trace, including the singular projector in \(B\).

Introduce two scalar soft variables \(a,b\), put \(t=ab\), and
define the regular hard contraction
\[
 \mathcal H(h,z,m;t)
   =\mathbb E_G S_h(va+Z_h,ub+P_h,m).
 \tag{6}
\]
Balancedness implies that the result depends on \(a,b\) only
through \(t\). Splitting each Wick pair in (4) gives exactly
\[
 \mathbb E_C g
   =\mathbb E_{1/z}\mathbb E_G
                         g(va+Z_h,ub+P_h),
 \qquad
 \mathbb E_{1/z}(a^d b^e)=\mathbf1_{d=e}\,d!z^{-d}.
 \tag{7}
\]
This identity follows as well by evaluating both sides on the
generating exponential. Consequently the actual marked source is
\[
 \mathscr W_m(h,\alpha+z)=r(z)\mathfrak L_z[\mathcal H],
                    \qquad \mathfrak L_z[t^d]=d!z^{-d-1}.
 \tag{8}
\]
Every fixed original quantum coefficient in (8) involves a finite
polynomial. No integral or summation choice has replaced the trace.

Use \(x=ht\) for the scaled soft variable, distinct from \(x_0\)
in (1), and retain independent marks before setting
\(\mathbf t=hm\). The full hard-contraction estimate of [D]
gives
\[
 \log\mathcal H_{\rm scaled}
       =\sum_{a\ge0}h^{a-1}\Psi_a(z,x,\mathbf t),\qquad
                 \|\Psi_a\|\le MC^a a!
 \tag{9}
\]
on one common sufficiently small meridian, soft-field and mark
polydisk. Here and below logarithms and series in \(h\) are
formal; the individual coefficient functions in (9) are analytic.

The applicability of [D] here does not use its accompanying
two-branch calibration. Its literal Poisson estimates in Sections
2 and 4 are valid for \(Y\ne0,1\). Its finite-product estimate
uses only the small analytic stationary equations and a unit
quadratic inverse. For the hard contraction, (4) supplies a
holomorphic covariance. At zero marks the relative principal
phase is quartic at the field origin. Its hard stationary equation
has identity linearization there, so the quadratic inverse is a
unit on smaller disks, independently of any soft quadratic
coefficient. This verifies every hypothesis of [D, Section 3]
and of its common soft-disk conclusion (28a) in the present scope.

It also shows
\[
                  \Psi_0(z,x,0)=O(x^2).
 \tag{10}
\]
For clarity, if the relative principal field phase is
\(\mathcal P_0=O((Z,P)^4)\), the hard stationary solution is its
mean plus terms of field degree at least three. The effective
principal phase
\(\mathcal P_0(u)-\tfrac12\nabla\mathcal P_0(u)^TK\nabla\mathcal P_0(u)\)
therefore still has field degree at least four. Its balanced
restriction to the two soft fields has degree at least two in
their product. This is (10), without a nonvanishing assertion.

## 3. The source amplitude and its endpoint phase

For a prescribed compact set of clocks, substitute
\(\mathbf t=hm\) in (9). Cauchy extraction on the independent
mark disk gives
\[
 \log\mathcal H_{\rm scaled}
 =h^{-1}\Psi_0(z,x,0)+A_0(z,x)+m\cdot\Theta(z,x)
                                      +\sum_{n\ge1}h^nB_n(z,x,m),
 \tag{11}
\]
where
\[
 A_0=\Psi_1(z,x,0),\qquad
 \Theta=\partial_{\mathbf t}\Psi_0(z,x,0),\qquad
                         \|B_n\|\le M_1C_1^n n!.
 \tag{12}
\]
Indeed an order \(h^n\) term satisfies \(a+|\gamma|=n+1\)
in \(h^{a-1}\mathbf t^\gamma\). The factorial in (9) is at
most \((n+1)!\), and the finite multiindex count and compact
clock powers cost only an exponential in \(n\). Use
\((n+1)!\le2^n n!\) for \(n\ge1\). At order zero only
\((a,|\gamma|)=(1,0),(0,1)\) contribute.

Define
\[
 a(h,z,x,m)=\sum_{j\ge0}h^j a_j(z,x,m)
       =e^{A_0+m\cdot\Theta}\exp\left(\sum_{n\ge1}h^nB_n\right).
 \tag{13}
\]
On common smaller disks, and on a neighborhood of the prescribed
clock compact,
\[
 \|a_j\|\le M_2C_2^j j!,\qquad
                      a_0=e^{A_0+m\cdot\Theta}\ne0.
 \tag{14}
\]
To prove this, expand the exponential by ordered compositions of
\(j\). Each product of factorials is at most \(j!\), the number
of compositions is at most \(2^j\), and the exponential
coefficient \(1/k!\) only improves the bound. All vertex constants
are absorbed in \(C_2^j\).

Put
\[
                 f(z,x)=zx-\Psi_0(z,x,0).
 \tag{15}
\]
This analytic function satisfies
\(f(z,0)=0\) and \(f_x(z,0)=z\). It is independent of the
fixed clock values. The analytic surface used below is simply
the \((z,x)\)-bidisk with projection
\[
                      \pi(z,x)=(z,\xi=f(z,x)).
 \tag{16}
\]
The assertion concerns this source-derived surface; it is not
an assertion that the projection is globally a finite cover.

## 4. Exact canonical reconstruction on the phase surface

For fixed small \(z\ne0\), invert (15) near \(x=\xi=0\) and
write
\[
 g_j(z,\xi,m)
     =\frac{a_j(z,x(z,\xi),m)}{f_x(z,x(z,\xi))}.
 \tag{17}
\]
With \(I_\xi\) the primitive starting at the original
\(\xi=0\), the canonical Borel germ is exactly
\[
          b_m(z,\xi)=r(z)\sum_{j\ge0}I_\xi^j g_j(z,\xi,m).
 \tag{18}
\]
The series converges near the origin for fixed \(z\ne0\):
on a smaller inverse disk, (14) gives
\(\|g_j\|\le M_zC_2^j j!\), while \(j\) primitives divide
the bound by \(j!\) and add \(|\xi|^j\).

Here is an exact coefficient verification, so that (18) does not
introduce a new formal solution. Its order-\(h^N\) coefficient is
\[
 r(z)\sum_{j=0}^N(N-j)!
       \operatorname{Res}_{x=0}
              a_j(z,x,m)f(z,x)^{-N+j-1}\,dx.
 \tag{19}
\]
Expanding \(f=zx-\Psi_0\), the term with \(\ell\) powers of
\(\Psi_0/(zx)\) is
\[
 \frac{r(z)(N-j+\ell)!}{\ell!z^{N-j+\ell+1}}
              [x^{N-j+\ell}]a_j\Psi_0^\ell.
 \tag{20}
\]
Only \(\ell\le N-j\) contributes, by (10). Equation (20) is
precisely the original moment (8), using \(h^ja_j\), the phase
term \(\Psi_0^\ell/(\ell!h^\ell)\), and
the formal endpoint rule
\(h^{-1}\int e^{-zx/h}x^d dx=d!h^dz^{-d-1}\), with
\(d=N-j+\ell\). This rule is precisely (8) after \(x=ht\);
it is coefficient notation, not an analytic integral assumption.
All regroupings at order \(N\) are finite.

Pulling (18) back to (16) now gives the exact formula
\[
 \boxed{\displaystyle
 \mathfrak b_m(z,x)=r(z)\left[
 \frac{a_0(z,x,m)}{f_x(z,x)}+
 \sum_{j\ge1}\frac1{(j-1)!}
  \int_0^x\bigl(f(z,x)-f(z,t)\bigr)^{j-1}a_j(z,t,m)\,dt
                         \right].}
 \tag{21}
\]
Indeed \(g_j\,d\xi=a_j\,dx\); substituting this in the repeated
primitive kernel proves (21) on the initial inverse branch.
Every integral in (21) starts at the original \(x=0\). Its
integrand is holomorphic in \(t\), so it is path-independent
inside the chosen small \(x\)-disk. No primitive base is moved
to a critical point. Continuation along paths in the surface
away from \(f_x=0\) gives exactly this same formula.

Shrink a fixed \((z,x)\)-bidisk so that, for \(t\) on the
straight segment from \(0\) to \(x\),
\[
 |x|\le R,\qquad |f(z,x)-f(z,t)|\le\varepsilon,
                                    \qquad C_2\varepsilon<1.
 \tag{22}
\]
This is possible by continuity at the origin, using the fixed
constants from (14). The \(j\)-th integral in (21) is bounded by
\[
                         RM_2\,j C_2^j\varepsilon^{j-1}.
 \tag{23}
\]
It follows that their sum \(H_m(z,x)\) is jointly holomorphic,
including at \(z=x=0\), uniformly on smaller products and on
the prescribed clock compact. Thus
\[
       \mathfrak b_m=r(z)\left(\frac{a_0}{f_x}+H_m\right).
 \tag{24}
\]
This proves the surface assertion without a Morse coordinate or
a nondegenerate critical-point hypothesis.

## 5. Exact pole divisor and leading clock character

The numerator in
\[
       \mathfrak b_m=\frac{r(z)(a_0+f_xH_m)}{f_x}
 \tag{25}
\]
restricts to the nonzero function \(r(z)a_0\) on \(f_x=0\).
After shrinking the product it is a unit. Therefore the pole
divisor on the phase surface is exactly the divisor of \(f_x\),
with its multiplicities. No higher quantum term can cancel it.
This statement includes zero occupation coordinates and all
retained stage or matching-lattice clocks.

The critical divisor itself is smooth at the origin:
\(\partial_z f_x(0,0)=1\), by (10). Thus it has a unique
analytic graph \(z=\zeta(x)\) near the origin. Higher
multiplicities below concern its restriction to a fixed meridian,
not a singularity of this two-variable divisor. Moreover
\(\zeta\equiv0\) holds exactly when
\(\Psi_0(0,x,0)\equiv0\). Both implications follow from
\(f_x(0,x)=-\partial_x\Psi_0(0,x,0)\), the zero value at
\(x=0\), and uniqueness of the graph.

For example, fix \(z=z_*\) and let \(x_*\) be a critical point
of finite multiplicity \(q\ge1\):
\[
 f(z_*,x)-f(z_*,x_*)
          =c_*(x-x_*)^{q+1}+O((x-x_*)^{q+2}),\qquad c_*\ne0.
 \tag{26}
\]
On the local inverse cover the leading singularity of the actual
Borel source is nonzero and has exponent \(-q/(q+1)\). This
follows directly from the first term of (24); the remaining
terms are holomorphic in \(x\). On a fixed choice of inverse
branch its leading marked/unmarked coefficient ratio is exactly
\[
                         e^{m\cdot\Theta(z_*,x_*)}.
 \tag{27}
\]
The local inverse geometry and \(r(z_*)e^{A_0(z_*,x_*)}\)
cancel in that ratio. For \(q=1\) this is the nonzero
square-root minor; the same argument gives the higher ramified
exponents in (26). It does not sum different inverse branches
or assert that their coefficients in a physical cycle are known.

## 6. Any finite soft order gives nearby nonzero fold branches

Suppose the first nonzero term of the limiting soft phase is
\[
              \Psi_0(0,x,0)=\tau x^{p+1}+O(x^{p+2}),
                    \qquad p\ge1,\quad \tau\ne0.
 \tag{28}
\]
Because (10) holds jointly, set \(z=s^p\), \(x=sX\). Then
\[
 s^{-p} f_x(s^p,sX)
                =1-(p+1)\tau X^p+O(s).
 \tag{29}
\]
This is a holomorphic identity near bounded \(X\); the apparent
division by \(s^p\) is removable. Terms vanishing at \(z=0\)
in \(\Psi_0\) are \(O(zx^2)\), so their differentiated scaled
contribution is \(O(s)\).

Equivalently the graph just proved satisfies
\(\zeta(x)=(p+1)\tau x^p+O(x^{p+1})\). Taking an analytic
\(p\)-th root of its nonzero unit factor makes a local coordinate
\(y\) in which \(z=y^p\). Thus the following branches exhaust
the nearby critical divisor over a punctured meridian disk.

Let \(\lambda_1,\ldots,\lambda_p\) be the distinct roots of
\((p+1)\tau\lambda^p=1\). The implicit function theorem gives
\(p\) analytic branches
\[
 x_j(s)=sX_j(s),\qquad X_j(0)=\lambda_j,\qquad
                         f_x(s^p,x_j(s))=0.
 \tag{30}
\]
For small \(s\ne0\) each is simple, since
\[
 f_{xx}(s^p,x_j(s))
   =-p(p+1)\tau\lambda_j^{p-1}s^{p-1}+O(s^p)\ne0.
 \tag{31}
\]
Their critical values are distinct for small \(s\ne0\):
\[
 \xi_j(s)=f(s^p,x_j(s))
        =\frac{p}{p+1}\lambda_j s^{p+1}+O(s^{p+2}).
 \tag{32}
\]
Each therefore gives an actual nonzero local fold minor of
(21), with leading clock ratio
\(\exp(m\cdot\Theta(s^p,x_j(s)))\).
On a consistent square-root convention its leading coefficient is
\[
 \frac{r(s^p)a_0(s^p,x_j(s),m)}
                         {\sqrt{2f_{xx}(s^p,x_j(s))}},
 \tag{33}
\]
so it has the expected nonzero scale \(s^{-(p-1)/2}\).
The branches are all accessible from the original endpoint by
paths in the small \(x\)-disk avoiding the finitely many critical
points. The assertion is a continuation of the source germ, not
a newly normalized period.

If \(\Psi_0(0,x,0)\) vanishes identically, no finite \(p\) is
asserted. The exact phase-surface reconstruction and pole-divisor
theorem (21)--(25) still hold. Nor is a common positive minor
radius as \(s\to0\) claimed by the separate fold coordinates;
the common analytic object is the original phase surface.

## 7. Scope and complete proof directs

Only a simple Alexander zero, the original finite word and its
literal clocks are required for (21)--(25). The finite-order
condition (28) is a condition on the analytic phase derived from
that same source; it does not invoke a chosen scalar annihilator.
This is broader than assuming a transverse quadratic node, while
making no assertion that every simple Alexander zero has a finite
nonzero soft order.

The result does not create an Alexander seed for knots with
\(\Delta=1\), identify a hyperbolic representation component,
continue through arbitrary global meridian domains, or compute
the coefficient of these local branches in the original physical
cycle. The arbitrary-short-filling and finite-exception targets
remain separate.

| Label | Complete proof direct | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| D | notes/research_actual_symbol_factorial_deficiency.md | a757e1ac8f6e62268cd7c2d681758a0258394661181026aace2cd516f4ca3359 |

F supplies the literal source, classical substitutions, determinant,
original cut, pivot and framing. D supplies the full ordinary-symbol
and regular hard-contraction coefficient estimate, whose hypotheses
are checked explicitly in Section 2 without a soft nondegeneracy
assumption. The Wick moment identity, amplitude, canonical coefficient
reconstruction, exact origin histories, pole divisor and finite-order
critical branches are proved above. No literature proof, mathematical
program, numerical case, test or build is used. Frozen notes and
public manuscripts are unchanged.
