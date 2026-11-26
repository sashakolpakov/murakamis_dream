# A forced Rogers connection for the original multiplication tensor

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The original centered multiplication tensor satisfies three exact
inhomogeneous quantum difference equations. A finite telescoping
identity proves their forcing term, including the initialized normal
which would be lost by evaluating the hypergeometric sum only at the
root. No infinite Rogers sum is substituted.

On the full finite boundary coefficient space, a known cyclic
dilogarithm product removes the homogeneous part of the connection.
The remaining additive equations are compatible and have an explicit
finite Fourier solution. One universal scalar fixes their constant.
That scalar also has a direct finite factorial initializer.

These identities preserve the complete tensor and hence its original
assembled source. They do not prove noncancellation after arbitrary
short fillings.

## 1. The original source and its scalar factors

Fix \(N\ge2\), and put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\qquad
 D_N(t)=1-\eta t^N .
 \tag{1}
\]
All fractional powers mean the indicated exponential.
Use the original full Casimir algebra
\(\mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2)\), its positive
crossing \(R\), and its original Frobenius functional \(\phi\).
Here \(T_N(\cos\theta)=\cos(N\theta)\).
The finite source theorem fixes
\[
 \mathcal C_N(x,y,z)=
  \sum_{a,b,c=0}^{d}C_{abc}x^ay^bz^c
  =N^{-3/2}\phi\!\left(
       R^3G_N(x;\cdot)G_N(y;\cdot)G_N(z;\cdot)\right).
 \tag{2}
\]
The arguments \(x,y,z\) in this note are boundary generating
variables; the dot in (2) is the Casimir variable.
In particular \(\mathcal C_N\) is the entire original
three-boundary tensor, not an absolute-value envelope.

Define the analytic function in the open unit polydisk
\[
 \widehat{\mathcal C}_N(x,y,z)=
       \frac{\mathcal C_N(x,y,z)}{D_N(x)D_N(y)D_N(z)},\qquad
 \beta_N=\frac{(-1)^{N+1}\kappa^3}{N^{3/2}} .
 \tag{3}
\]
For \(i=x,y,z\), let \(T_i\) multiply that one argument by \(Q\).
For example \(T_xF(x,y,z)=F(Qx,y,z)\). Write
\[
 a_x=(1-Qxy)(1-Qxz),\qquad
 b_x=(1+qx)(1+qxyz),\qquad r_x=\frac{x}{1+qx},
 \tag{4}
\]
and define the other two triples by permutation.

**Theorem 1.** The exact original source satisfies
\[
 \boxed{\qquad
 a_xT_x\widehat{\mathcal C}_N-b_x\widehat{\mathcal C}_N
                         =\beta_N\frac{x}{1+qx},
 \qquad}
 \tag{5}
\]
and the two permuted equations. Equivalently, its polynomial
version retains every original norm factor:
\[
 a_xT_x\mathcal C_N-b_x\mathcal C_N
   =\beta_ND_N(x)D_N(y)D_N(z)\frac{x}{1+qx}.
 \tag{6}
\]
The right side has a removable denominator since \(1+qx\)
divides \(D_N(x)\).

## 2. A finite telescoping certificate and its initialized normal

This proof uses the auxiliary generic parameter \(\xi\) from
the finite source theorem. Put \(B=\xi^2\), and let
\[
 \begin{split}
 \tau_j(\xi;x,y,z)
  ={}&\frac{1-\xi^{4j+2}}{1-\xi^2}(-\xi)^j\\
   &{}\times
   \prod_{t\in\{x,y,z\}}
       \frac{\prod_{h=0}^{j-1}(t+\xi^{2h+1})}
            {\prod_{h=0}^{j-1}(1+\xi^{2h+3}t)},\qquad
 S_N(\xi)=\sum_{j=0}^{N-1}\tau_j(\xi).
 \end{split}
 \tag{7}
\]
Empty products are one. This canceled definition is regular at
zero boundary arguments. In a fixed closed unit subpolydisk it
is holomorphic for \(\xi\) sufficiently close to \(q\).

The complete finite source theorem proves, with all root Hermite
data calibrated,
\[
 S_N(q;x,y,z)=0,\qquad
 \widehat{\mathcal C}_N=
 K_N^{\rm loc}
       \frac{\dot S_N(q;x,y,z)}
            {(1+qx)(1+qy)(1+qz)},\quad
 K_N^{\rm loc}=
      \frac{(-1)^N(q-q^{-1})\kappa^3}{2N^{5/2}} .
 \tag{8}
\]
Here the dot is \(\xi\partial_\xi\) with boundary arguments
fixed. The notation \(K_N^{\rm loc}\) denotes only the displayed
known local constant; it is not a knot invariant.

For the \(x\)-equation define
\[
 g_\xi(u)=
 \frac{(1+\xi^3x)\xi x(1-u)(1+\xi yu)(1+\xi zu)}
      {(1-Bu^2)(u+\xi x)} .
 \tag{9}
\]
For generic parameters the following rational identity holds:
\[
 \begin{split}
 &(1-Bxy)(1-Bxz)\tau_j(\xi;Bx,y,z)
       -(1+\xi^3x)(1+\xi xyz)\tau_j(\xi;x,y,z)\\
 &\hspace{25mm}=
   \tau_{j+1}(\xi;x,y,z)g_\xi(B^{j+1})
                  -\tau_j(\xi;x,y,z)g_\xi(B^j).
 \end{split}
 \tag{10}
\]
Products on the right are canceled before specialization.
This matters when the well-poised factor vanishes at an odd-level
middle index.

Here is a direct check, independent of an infinite summation.
Set \(u=B^j\). The two needed ratios are
\[
 \frac{\tau_j(\xi;Bx,y,z)}{\tau_j(\xi;x,y,z)}
   =\frac{u(1+\xi x)(1+\xi^3x)}
           {(u+\xi x)(1+\xi^3xu)},
 \tag{11}
\]
\[
 \frac{\tau_{j+1}}{\tau_j}
  =-\xi\frac{1-B^3u^2}{1-Bu^2}
       \prod_{t\in\{x,y,z\}}\frac{t+\xi u}{1+\xi^3tu}.
 \tag{12}
\]
Substitute (9) into (12), cancel the \(y,z\) denominators,
and use \(Bu+\xi x=\xi(x+\xi u)\). The remaining identity,
after multiplication by its denominators, is
\[
 \begin{split}
 &\xi x\bigl[
 (1-Bu)(y+\xi u)(z+\xi u)(u+\xi x)\\
 &\hspace{23mm}
 +(1-u)(1+\xi yu)(1+\xi zu)(1+\xi^3xu)\bigr]\\
 &=(1-Bu^2)\bigl[
 (1+\xi xyz)(u+\xi x)(1+\xi^3xu)
      -(1-Bxy)(1-Bxz)u(1+\xi x)\bigr].
 \end{split}
 \tag{13}
\]
Expansion verifies this polynomial identity, proving (10).

Since \(g_\xi(1)=0\), summing (10) gives exactly
\[
 \begin{split}
 &(1-Bxy)(1-Bxz)S_N(\xi;Bx,y,z)
       -(1+\xi^3x)(1+\xi xyz)S_N(\xi;x,y,z)\\
 &\hspace{35mm}=\tau_N(\xi;x,y,z)g_\xi(B^N).
 \end{split}
 \tag{14}
\]
The boundary at \(j=N\) has not been discarded.

At the root its canceled value is \(\tau_N(q)=-1\).
Indeed the well-poised prefactor equals one, \((-q)^N=\eta\),
and each of the three product ratios in (7) equals
\[
       \frac{t^N-\eta}{1-\eta t^N}=-\eta .
 \tag{15}
\]
At \(u=B^N\), only the factor \(1-u\) in (9) contributes
to its first derivative at the root. Thus
\[
 \left.\frac{d}{d\log\xi}\{
                  \tau_N(\xi)g_\xi(B^N)\}\right|_{\xi=q}
 =
 \frac{2N(1+q^3x)qx(1+qy)(1+qz)}
             {(1-Q)(1+qx)} .
 \tag{16}
\]
The numerator \(2N\) is the derivative of the finite endpoint,
with the sign from (15).

Differentiate (14). Derivatives of its scalar coefficients
multiply \(S_N(q)=0\). The chain term from the moving argument
\(B x\) is \(2Qx\,\partial_xS_N(q;Qx,y,z)=0\) for the same
reason: \(S_N(q;\cdot)\) is identically zero.
Consequently (16) is an equation for the specified initialized
\(\dot S_N\), with no extra parameter current.
Inserting (8) and canceling the three linear factors gives (5),
because
\[
       K_N^{\rm loc}\frac{2Nq}{1-Q}=\beta_N .
 \tag{17}
\]
The relation \(D_N(Qx)=D_N(x)\) then gives (6).
All canceled identities extend to zero boundary arguments.
Permutation proves the other equations.

## 3. The finite coefficient space and its homogeneous unit

The connection will now be solved on the full boundary coefficient
space
\[
 \mathscr R_N=
       \mathbb C[x,y,z]/(x^N,y^N,z^N).
 \tag{18}
\]
Each element has a unique representative of degree below \(N\)
in each variable. Thus it records all \(N^3\) entries of the
original tensor. This quotient concerns the auxiliary generating
powers, not a semisimple quotient of the physical Casimir module.
In particular all original repeated-root directions are retained.

The norm defect of the homogeneous connection is explicit:
\[
 \prod_{h=0}^{N-1}T_x^ha_x-\prod_{h=0}^{N-1}T_x^hb_x
                    =\eta x^ND_N(y)D_N(z).
 \tag{19}
\]
For example the two products are
\((1-x^Ny^N)(1-x^Nz^N)\) and
\((1-\eta x^N)(1-\eta x^Ny^Nz^N)\).
Consequently the cyclic product of \(b_x/a_x\) is one in
(18), though the off-quotient norm defect is nonzero.

For any nilpotent monomial \(u\) with \(u^N=0\), define
\[
 \mathsf e_N(u)=
       \exp\left(\sum_{n=1}^{N-1}
                         \frac{u^n}{n(1-Q^n)}\right).
 \tag{20}
\]
The exponential is a finite operation in the nilpotent ideal.
Its constant is one and
\(\mathsf e_N(Qu)/\mathsf e_N(u)=1-u\), by the finite
logarithm of \(1-u\).
Define the known unit
\[
 \boxed{\qquad
 H=
 \frac{\mathsf e_N(-qx)\mathsf e_N(-qy)
       \mathsf e_N(-qz)\mathsf e_N(-qxyz)}
      {\mathsf e_N(Qxy)\mathsf e_N(Qxz)\mathsf e_N(Qyz)} .
 \qquad}
 \tag{21}
\]
Every numerator and denominator has constant one.
Using (20) gives exactly
\[
                       a_iT_iH=b_iH\quad(i=x,y,z).
 \tag{22}
\]
This is the finite cyclic-dilogarithm version of the homogeneous
Rogers product, derived here by a finite logarithm.

## 4. Compatible forcing and an explicit Fourier potential

Put \(\delta_i=T_i-I\), and define three known elements of
\(\mathscr R_N\):
\[
 f_x=\frac{x}{(1+qx)^2(1+qxyz)H},\qquad
 f_y,\ f_z\text{ by permutation}.
 \tag{23}
\]
All inverses exist because their constants are one.
Dividing (5) by \(b_xH=a_xT_xH\) reduces its additive part to
\[
                  \delta_i(\widehat{\mathcal C}_N/H)
                                      =\beta_N f_i .
 \tag{24}
\]

The forcing is compatible independently of the already known
source. Indeed
\[
 a_y-(1+qy)(1+qQxyz)=-qy(1+qx)(1+qz).
 \tag{25}
\]
Apply \(T_y\) to (23), use (22), and subtract. This gives
\[
 \delta_yf_x=
 -\frac{qxy(1+qz)}
 {(1+qx)(1+qy)(1+qxyz)(1+qQxyz)H}
                         =\delta_xf_y .
 \tag{26}
\]
The other two identities follow by permutation.

These identities can be integrated with no unspecified coefficient.
Write \(x^\alpha=x^{\alpha_1}y^{\alpha_2}z^{\alpha_3}\)
for \(0\le\alpha_i<N\), and \(f_i=\sum_\alpha f_{i,\alpha}x^\alpha\).
For a nonzero multiindex put
\[
 d_{i,\alpha}=Q^{\alpha_i}-1,\qquad
 \lambda_\alpha=\sum_i|d_{i,\alpha}|^2>0 .
 \tag{27}
\]
Define a zero-constant polynomial \(A\) by the explicit diagonal
formula
\[
 \boxed{\qquad
 A_0=0,\qquad
 A_\alpha=
       \frac{\sum_i\overline{d_{i,\alpha}}\,f_{i,\alpha}}
                    {\lambda_\alpha}\quad(\alpha\ne0).
 \qquad}
 \tag{28}
\]
The bar in this formula conjugates the known root-of-unity scalar.
It is not conjugation of a generating variable.

To prove \(\delta_iA=f_i\), take coefficients in (26).
They say \(d_{j,\alpha}f_{i,\alpha}
=d_{i,\alpha}f_{j,\alpha}\).
For \(\alpha\ne0\), choose an index \(j\) with
\(d_{j,\alpha}\ne0\). All \(f_{i,\alpha}\) are then
\(d_{i,\alpha}\) times the same scalar, and (28) recovers
that scalar. At \(\alpha=0\), every \(f_i\) is zero because
its numerator contains its own variable. This proves the equations.
It also proves uniqueness with \(A_0=0\): common invariance
under \(T_x,T_y,T_z\) leaves only the constant coefficient.

For clarity the finite Fourier inverse has a polynomial norm
bound. Give coefficients in the displayed monomial basis their
Euclidean norm, and give triples the sum-of-squares norm.
The \(T_i\) are unitary for this particular norm. Equation (28)
and compatibility give
\[
       \|A\|\le\frac{\|(f_x,f_y,f_z)\|}{2\sin(\pi/N)}
                              \le\frac N4\|(f_x,f_y,f_z)\|.
 \tag{29}
\]
Indeed every nonzero multiindex has
\(\lambda_\alpha\ge4\sin^2(\pi/N)\); equivalently,
\(\sum_i\|\delta_iA\|^2
\ge4\sin^2(\pi/N)\|A\|^2\).
This is only a bound for the additive Fourier inverse.
Multiplication by \(H\) or \(H^{-1}\) need not be
polynomially conditioned in this norm.

## 5. One scalar anchor and its finite initializer

**Theorem 2.** Let \(a_N=\mathcal C_N(0,0,0)
=N^{-3/2}\phi(R^3)\). In \(\mathscr R_N\),
\[
 \boxed{\qquad
            \mathcal C_N=a_NH+\beta_NHA .
 \qquad}
 \tag{30}
\]
More generally, the complete set of solutions of the three forced
equations (5) in this finite coefficient space is
\(aH+\beta_NHA\), with one arbitrary constant \(a\in\mathbb C\).

In fact \(D_N=1\) in this quotient, so
\(\widehat{\mathcal C}_N=\mathcal C_N\).
Equation (24), the defining equations of \(A\), and the
common-invariant observation after (28) prove the assertion.
The physical constant is exactly \(a_N\), since \(H(0)=1\)
and \(A(0)=0\). No knot-dependent scalar is used to define
the tensor.

The universal anchor itself has the following finite initializer.
Set
\[
 F_0=1,\qquad F_r=(Q;Q)_r=\prod_{h=1}^r(1-Q^h)
                         \quad(1\le r<N).
 \tag{31}
\]
Then
\[
 \boxed{\qquad
                   a_N=-\frac{\beta_N}{q}
                                  \sum_{r=0}^{N-1}F_r .
 \qquad}
 \tag{32}
\]
Here is a proof using the terminal coefficient, rather than an
infinite sum. Set \(y=z=0\) in the polynomial equation (6):
\[
 \mathcal C_N(Qx,0,0)-(1+qx)\mathcal C_N(x,0,0)
       =\beta_N\sum_{a=1}^{N}(-q)^{a-1}x^a .
 \tag{33}
\]
Write \(\mathcal C_N(x,0,0)=\sum_{a=0}^{N-1}v_ax^a\).
The coefficients below \(N\) give
\[
 (Q^a-1)v_a-qv_{a-1}=\beta_N(-q)^{a-1}
                                  \quad(1\le a<N).
 \tag{34}
\]
Iteration, starting with \(v_0=a_N\), yields
\[
 v_a=\frac{(-q)^a}{F_a}
       \left(a_N+\frac{\beta_N}{q}
                            \sum_{r=0}^{a-1}F_r\right).
 \tag{35}
\]
The terminal coefficient of (33) is
\(-qv_{N-1}=\beta_N(-q)^{N-1}\).
Using \(F_{N-1}=N\) in (35) proves (32).
Thus the anchor is initialized by a known finite factorial sum,
with its full original phase.

The sum in (32) is the root-of-unity value of the classical
Kontsevich--Zagier series
\(\sum_{r\ge0}(Q;Q)_r\); see
[Zagier (2001), introduction and equation (1)](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1016/S0040-9383(00)00005-7/fulltext.pdf).
That citation identifies the familiar series only. No radial-limit,
strange-identity, modularity or asymptotic theorem from it is used.

The forcing cannot be absorbed into a scalar normalization of \(H\).
For example (5) gives the universal first-coefficient identity
\[
                  (Q-1)C_{100}-qC_{000}=\beta_N\ne0 .
 \tag{36}
\]
A pure homogeneous product would give zero on its right.
This is an exact source obstruction, not an estimate based on a
small selection of knots or levels.

## 6. Exact use in the original Conway assembly

Equation (30) gives every original tensor entry by taking the
unique representative of degree below \(N\) in each variable.
Alternatively, choose any nonnegative-power Taylor sections for
its right side agreeing with that representative modulo
\((x^N,y^N,z^N)\). Use coefficient-conjugate sections for
the conjugate vertices.

The complete generating-section theorem proves the required
whole-source rule: first reverse the finite indices along a
Conway tree so every internal contraction is anti-diagonal.
With the original leaves, turns and both actual closing arrays
retained, the scalar is the coefficient
\[
                   [\,\prod_e t_e^{N-1}\,]\prod_v V_v .
 \tag{37}
\]
Every vertex section has nonnegative powers on every incident edge.
Replacing a vertex by (30) changes it by a sum of terms containing
an incident \(t_e^N\). Such a term cannot contribute to (37).
Telescoping the replacements over the finitely many vertices
therefore preserves the original scalar exactly.

This order is essential. Reverse the finite tensors before
choosing their Taylor extensions. A reversed untruncated series
or a ratio of edge variables may introduce negative powers and
does not satisfy the rule. No physical meridian power or
Casimir normal is declared invisible. The final coefficient
functional has not been replaced by a norm, and no physical
source direction is discarded.

The result reduces the universal tensor to a finite cyclic
product, a completely specified additive potential, and the
universal initializer (32). It does not estimate the coherent
coefficient (37) at a geometric contour. In particular the
small prefactor \(\beta_N\), the Fourier bound (29), or the
one-constant description does not supply a lower bound after
arbitrary short fillings. Contributions from the homogeneous
and forced terms may still cancel in the assembled source.

## Complete proof sources and coverage

Both complete proof texts were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Initialized finite tensor source](research_centered_tensor_finite_6phi5_source.md) | 238b5fd4daeca0293ae705d1a4c1189824129a0278e086e250207e8d51ed3f53 |
| [Full-degree generating section](research_full_degree_centered_generating_section.md) | 6fbef2085aca79503518745a08d3466ec84cd337ec8131944e2aebb9c95c2f6b |

The first supplies the complete physical source and its calibrated
initialized normal. The second supplies the exact full-tree
coefficient rule. The finite telescoper, forcing compatibility,
Fourier potential and terminal initializer are proved above.
The existing generating-section theorem already has a homogeneous
finite cocycle for a single leg. No novelty is claimed for
telescoping, cyclic dilogarithms, finite Fourier inversion, or
the classical factorial series. No infinite Rogers summation
or unverified root limit is an assumption here.

Only written mathematics, text/hash operations and the stated
primary-source lookup were used. No mathematical program,
numerical experiment, test, build, git operation or earlier-final
edit was performed.
