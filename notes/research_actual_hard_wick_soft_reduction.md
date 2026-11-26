# Formal hard-Wick reduction of the actual marked source

Private written proof, 18 November 2026.

At a simple Alexander pole, the original highest-cut trace admits an
exact coefficientwise reduction to one soft moment variable. Taking
the logarithm only after the hard Wick contractions gives a sharper
degree bound. It separates a clock-independent formal phase from a
leading clock amplitude that is exponential in a linear clock form.

All statements below are formal in the quantum parameter. No
convergence of the phase, effective logarithm, or Laplace integral
is asserted. A formal stationary sector is distinguished from its
occurrence in an analytic source period.

## 1. The actual normal symbol and covariance

Use the original marked source and simple-node setup of [C].
Put \(z=Y-\alpha\) and \(h=\log Q\). Its exact formal expression is
\[
 \mathscr W_m(h,Y)=x_0^c
       \operatorname{Tr}_{\mathrm{Sym}}
          \left[e^{D(h,z,m)}\Gamma(B(z))\right],
 \quad D=\sum_{j\ge1}h^jD_j,\quad
 B=L_\beta(x_0)T_0 .
 \tag{1}
\]
The original pivot and zero-framing scalar are included as in [C].
The highest-cut projector \(T_0\) remains in \(B\), without an inverse.
All clock variables \(m\) remain independent.

Let \(S(h,Z,P,m)\) be the ordinary normal symbol of \(e^D\),
and put
\[
                 S=\exp(V),\qquad V=\sum_{j\ge1}h^jV_j .
 \tag{2}
\]
The exponential and logarithm in (2) are commutative formal operations
on symbols, not operator logarithms or trace logarithms.
For every monomial of \(V_j\), let \(d\) be its degree in \(P\)
and \(a\) its degree in \(m\). Then
\[
                    d+a\le j+1,\qquad a\le j.
 \tag{3}
\]
It has the same degree \(d\) in \(Z\). Its coefficients are
holomorphic in \(z\).

Here (3) follows from [C]'s joint filtration of \(D_j\) by the
forward normal-symbol calculation of [H, (13)--(15)].
For completeness, use the exact product
\[
 f\star g=\sum_\gamma
          \frac{\partial_P^\gamma f\,\partial_Z^\gamma g}{\gamma!}.
 \tag{4}
\]
If \(F_t=\log(\exp_\star(tD))\), then
\[
 \partial_t F_t=\sum_\gamma\frac{\partial_P^\gamma D}{\gamma!}
                           e^{-F_t}\partial_Z^\gamma e^{F_t}.
 \tag{5}
\]
A nonzero Bell term with \(r\) positive-order factors from \(F_t\)
has \(r\le|\gamma|\). At total \(h\)-order \(j\), its combined
\(P\)-plus-mark degree is at most
\(j+1+r-|\gamma|\le j+1\). Mark degrees add and cannot exceed
the total positive \(h\)-order. Induction proves (3), with homogeneous
degree zero retained. Every coefficient calculation is finite.

The exact covariance of the trace in [C] is
\[
 \mathcal C(z)=B(I-B)^{-1}=\frac{uv^T}{z}+G(z),\qquad
 r(z)=\frac{z x_0^c}{\det(I-B)},\qquad r(0)=r\ne0.
 \tag{6}
\]
Here \(u,v\) are fixed vectors, \(uv^T\ne0\), and \(G\) is
holomorphic. No algebraic simplicity of the eigenvalue one is needed:
the simple determinant zero gives the rank-one residue, as proved
in [C].

## 2. Algebraic hard contractions and their connected logarithm

Define the hard Wick functional on polynomial variables \(Z_h,P_h\)
by
\[
 \mathbb E_G f
  =\left.
    \exp\!\left(\sum_{i,j}G_{ij}
                     \partial_{(P_h)_i}\partial_{(Z_h)_j}\right)
                                f\right|_{Z_h=P_h=0}.
 \tag{7}
\]
The exponential in (7) is a finite sum on every polynomial.
It has no positivity requirement. Introduce two scalar soft variables
\(\mathfrak a,\mathfrak b\), put \(t=\mathfrak a\mathfrak b\),
and set
\[
 \mathcal H(h,z,m;t)
   =\mathbb E_G\!
       \exp V(h,v\mathfrak a+Z_h,u\mathfrak b+P_h,m)
   =\exp\!\left(\sum_{j\ge1}h^jU_j(z,m;t)\right).
 \tag{8}
\]
The notation \(t\) is justified below. The constant term in \(h\)
is one, so the last logarithm is uniquely defined.

**Connected-degree assertion.** The actual coefficients in (8) obey
\[
 U_j\in\mathcal O_0[t,m],\qquad
               \deg_t U_j+\deg_m U_j\le j+1
 \quad\hbox{monomialwise},\qquad \deg_m U_j\le j.
 \tag{9}
\]
Here \(\mathcal O_0\) denotes holomorphic germs in \(z\);
the first degree bound is the sum of the degrees of each monomial,
not a sum of the separate maxima of the polynomial.

To prove this, expand the logarithm in joint cumulants of the
positive-order vertices \(V_{j_i}\). For a fixed Wick pairing graph,
its coefficient in the cumulant is zero unless its vertex graph is
connected. Indeed if it has \(c\) connected components, the coefficient
is
\[
       \sum_{r=1}^c {c\brace r}(-1)^{r-1}(r-1)!
                              =\mathbf1_{c=1}.
 \tag{10}
\]
This finite identity follows from the exponential generating series
\(\log(e^x)=x\). Pairings within one vertex are allowed; they
do not join distinct vertex components.

A connected graph with \(v_0\) vertices has at least \(v_0-1\)
hard contractions. If its vertices have degrees \(d_i,a_i\)
and orders \(j_i\), let \(c_h\) be its number of hard pairs.
After the hard expectation all remaining variables are soft.
Their creation and differentiation counts are equal and both equal
\(s=\sum d_i-c_h\). Thus the term depends on the two soft
variables only as \(t^s\), and has mark degree \(a=\sum a_i\).
By (3),
\[
 s+a
  \le \sum_i(j_i+1)-c_h
  \le \sum_i j_i+1,\qquad a\le\sum_i j_i .
 \tag{11}
\]
This proves (9). At any fixed total order, the vertices, monomials,
and pairings are finite; \(G\) and all vertex coefficients are
holomorphic in \(z\). No inverse power of \(z\) is introduced by
the hard functional.

## 3. Exact one-variable moment reduction

Define the soft functional by
\[
 \mathbb E_{1/z}(\mathfrak a^p\mathfrak b^q)
                         =\mathbf1_{p=q}\,p!\,z^{-p}.
 \tag{12}
\]
Splitting a Wick pair as \(uv^T/z+G\) gives the exact identity
\[
 \mathbb E_{\mathcal C} f(Z,P)
   =\mathbb E_{1/z}\mathbb E_G
                  f(v\mathfrak a+Z_h,u\mathfrak b+P_h).
 \tag{13}
\]
One may verify every coefficient at once on the polynomial generating
exponential: the right side gives
\(\exp(P_*^TG Z_*+(P_*^Tu)(v^TZ_*)/z)\), exactly the covariance
\(\mathcal C\). This is an algebraic pairing identity.

The actual trace Wick rule [C, (12)] therefore proves
\[
 \boxed{\displaystyle
 \mathscr W_m(h,\alpha+z)
   =r(z)\,\mathfrak L_z
        \left[\exp\!\left(\sum_{j\ge1}h^jU_j(z,m;t)\right)\right],
 \qquad
                 \mathfrak L_z[t^s]=s!\,z^{-s-1}.}
 \tag{14}
\]
Equation (14) is coefficientwise in \(h\), with meromorphic
\(z\)-coefficients and polynomial dependence on \(m\) at each order.
Each coefficient inside its brackets is a polynomial in \(t,m\).
Thus (14) is well defined without any convergence assumption.

Equivalently one may write
\[
 r(z)\int_0^\infty e^{-zt}
           \exp\!\left(\sum_{j\ge1}h^jU_j(z,m;t)\right)\,dt
 \tag{15}
\]
as formal notation for (14): integrate each polynomial coefficient
by its prescribed moment. Equation (15) is not an assertion that
the full integrand or integral exists at nonzero \(h\).
There has been no logarithm of the full trace, no new closing
functional, and no removal of a scalar framing contribution.

## 4. Formal phase and leading clock amplitude

Expand
\[
 U_j=\sum_{s,\gamma}u_{j,s,\gamma}(z)t^s m^\gamma,
             \qquad s+|\gamma|\le j+1,\quad |\gamma|\le j.
 \tag{16}
\]
Set \(x=ht\) only as a formal grading substitution in the exponent.
The exact degree bound separates it as
\[
 -zt+\sum_{j\ge1}h^jU_j
       =\frac{\Phi(z,x)}h+A_0(z,x)+m\cdot\Theta(z,x)
                           +\sum_{r_1\ge1}h^{r_1}V_{r_1}(z,x,m),
 \tag{17}
\]
where
\[
 \begin{split}
 \Phi(z,x)&=-zx+\sum_{j\ge1}u_{j,j+1,0}(z)x^{j+1},\\
 A_0(z,x)&=\sum_{j\ge1}u_{j,j,0}(z)x^j,\\
 \Theta_i(z,x)&=\sum_{j\ge1}u_{j,j,e_i}(z)x^j,\qquad
                \deg_m V_{r_1}\le r_1+1 .
 \end{split}
 \tag{18}
\]
All displayed series are formal in \(x\). For each fixed power
of \(h\) and \(x\) the expression is finite. There are no terms
below \(h^{-1}\). A term at \(h^{-1}\) has zero mark degree;
a term at \(h^0\) has mark degree at most one. This proves (17)
including all scalar amplitudes.

At order one the hard contraction cannot alter the top soft degree.
The actual calibration in [C, Section 4] gives
\[
 u_{1,2,0}(0)=\sigma\ne0,\qquad
                (u_{1,1,e_i}(0))_i=\mu .
 \tag{19}
\]
All lower-degree pieces of \(U_1\), including scalar and pivot
pieces, remain in (16); (19) does not discard them.
The formal implicit function theorem, or direct coefficient
recursion using \(2\sigma\ne0\), gives a unique
\[
 \partial_x\Phi(z,x_g(z))=0,\qquad
 x_g(z)\in z\mathbb C[[z]],\qquad
 x_g(z)=\frac z{2\sigma}+O(z^2).
 \tag{20}
\]
The critical Hessian is a formal unit with constant \(2\sigma\).
Substitution in (18) yields
\[
 \Phi(z,x_g(z))=-\frac{z^2}{4\sigma}+O(z^3),\qquad
 \Theta(z,x_g(z))=\frac{\mu z}{2\sigma}+O(z^2).
 \tag{21}
\]
These substitutions are well defined in the \(z\)-adic topology,
because \(x_g(0)=0\).

For the formal stationary expansion attached to this nondegenerate
critical point, with any common nonzero Gaussian normalization,
the leading marked-to-unmarked amplitude ratio is exactly
\[
                         \exp(m\cdot\Theta(z,x_g(z))).
 \tag{22}
\]
Indeed the leading factor after the formal substitution \(x=ht\)
is \(r(z)h^{-1}e^{\Phi/h}\exp(A_0+m\cdot\Theta)\).
Formal Gaussian contraction evaluates the last exponential at
the critical point in its leading term. The same nonzero Hessian
factor and \(r(z)e^{A_0(z,x_g)}\) occur with and without marks,
so they cancel in the ratio. Higher powers in (17) affect only
higher quantum orders.

Equation (22) describes the formal stationary sector of the exact
source-derived reduction (14). It does not assert that this sector
is selected by an analytic continuation, actual Borel minor, or
physical cycle. The endpoint moment identity (14) alone does not
supply that identification. Nor does (9) imply convergence of
the formal phase or clock map in (18).

## 5. Complete proof directs and scope

| Label | Complete proof direct | SHA256 |
|---|---|---|
| H | notes/research_actual_source_natural_log_filtration.md | 98c371fe71a210e9d886e30d60a487a3fe46599f1814c1b69229d829a1eb6f88 |
| C | notes/research_actual_clock_finite_core_volterra_carriers.md | 7c7630796cb2d7ee2e81d0efceb9c9008bbb5214169ce4da5b76f068c0341d9a |

H supplies the forward normal-symbol logarithm identity.
C supplies the actual joint operator filtration, highest-cut Wick
rule, rank-one pole decomposition and normalized soft coefficients.
The hard cumulant count, exact scalar moment identity and formal
phase/clock separation are proved above.

This construction uses every original source operation. It introduces
no internal Ward division, classical right-factor replacement,
positive integration measure, or unproved analytic Laplace contour.
Only written mathematics and source-text/hash operations were used.
Frozen proofs and public manuscripts are unchanged.
