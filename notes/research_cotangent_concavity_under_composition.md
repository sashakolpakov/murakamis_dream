# A cotangent criterion for concavity under composition

Private research proof, 8 November 2026. The pair estimate below
extends the fixed-rectangle argument in
[the open-word Hessian theorem](research_mixed_open_word_hessian.md).
It gives a direct criterion for the original logarithmic phase,
allows real coordinates as small as \(1/6\) at the heights used in
the current attachment problem, and is preserved when internal
critical variables are eliminated. The last property concerns
the phase and its local Gaussian coefficient. A separate estimate
is still needed for the original finite sum outside that local
contribution.

The determinant identity is already present in
[horizontal support, equation (6)](research_mixed_horizontal_zero_mode_support.md),
and preservation under a Schur complement is already used in
[the local attachment theorem, Lemma 1](research_mixed_three_four_next_local_source.md).
The extension here is the common domain for independently varying
coordinates, its quantitative bound on arbitrary graphs, and their
combined use under successive elimination. The older asymmetric
rectangle can reach a smaller private index and is not superseded
in every coordinate by this common domain.

No numerical evaluation is used. All inequalities are proved below.

## 1. The logarithmic primitive and its two-variable phase

Let
\[
 \mathcal S=\{z\in\mathbb C:0<\Re z<1\}.
\]
On this strip use the original analytic logarithm in
\[
 g'(z)=\operatorname{Log}(1-e^{-2\pi iz}).
 \tag{1}
\]
An additive constant in \(g\) is immaterial here. The logarithm
agrees with its real value at \(z=1/2\); it is single-valued on
\(\mathcal S\). Indeed its argument never lies on the nonpositive
real axis there. Differentiation gives
\[
 g''(z)=\pi\cot(\pi z)-i\pi .
 \tag{2}
\]
Consequently the real Hessian calculations below are also valid
for the primitive \(J\) with \(J'(z)=\operatorname{Log}(2\sin\pi z)\)
used in the open-word note.

For \(z,w,z+w\in\mathcal S\), define
\[
 V(z,w)=g(z+w)-g(z)-g(w).
 \tag{3}
\]
The real Hessian means the Hessian of \(\Re V\) as the real
parts of \(z,w\) vary with their imaginary parts fixed. It is
also the entrywise real part of the holomorphic Hessian.

Write
\[
 \cot(\pi z)=a+ib,\qquad \cot(\pi w)=c+id,\qquad
 C=\Re\cot(\pi(z+w)).
 \tag{4}
\]
Equation (2) gives
\[
 -\frac1\pi\Re V''=
 H=\begin{pmatrix}a-C&-C\\-C&c-C\end{pmatrix}.
 \tag{5}
\]

**Proposition 1.** If \(a,c>0\), then
\[
 \det H
 =\frac{(a+c)^2-(ad-cb)^2}
        {|\cot(\pi z)+\cot(\pi w)|^2}.
 \tag{6}
\]
In particular \(H\) is positive definite whenever
\[
                         |ad-cb|<a+c.
 \tag{7}
\]
A sufficient condition for (7) is \(|b|,|d|<1\).

**Proof.** The denominator in (6) is nonzero because its real
part before taking the modulus is \(a+c>0\). The cotangent
addition formula gives
\[
 C=\frac{(ac-bd-1)(a+c)+(ad+bc)(b+d)}
          {(a+c)^2+(b+d)^2}.
 \tag{8}
\]
Expanding \(ac-(a+c)C=\det H\) gives (6). If (7) holds,
\(\det H>0\), so \(C<ac/(a+c)<\min(a,c)\). Thus both diagonal
entries in (5) are positive and \(H\) is positive definite.
Finally
\[
 |ad-cb|\le a|d|+c|b|<a+c
\]
under the sufficient condition. \(\square\)

## 2. An explicit domain that reaches \(1/6\)

For \(0<x<1/2\) and real \(h\),
\[
\begin{split}
 \Re\cot\pi(x+ih)
   &=\frac{\sin(2\pi x)}
           {\cosh(2\pi h)-\cos(2\pi x)}>0,\\
 |\Im\cot\pi(x+ih)|
   &=\frac{|\sinh(2\pi h)|}
           {\cosh(2\pi h)-\cos(2\pi x)}.
\end{split}
 \tag{9}
\]
The second expression is less than one precisely when
\[
                  \cos(2\pi x)<e^{-2\pi|h|}.
 \tag{10}
\]
This equivalence follows by subtracting
\(|\sinh(2\pi h)|\) from \(\cosh(2\pi h)\).

Fix \(0<\alpha<1/2\) and \(H_0>0\) such that
\[
                       \cos(2\pi\alpha)<e^{-2\pi H_0}.
 \tag{11}
\]
On the convex rectangle
\[
 \mathcal B_{\alpha,H_0}
   =\{z:\alpha<\Re z<1/2,\ |\Im z|<H_0\},
 \tag{12}
\]
every pair satisfies Proposition 1. Both individual arguments
and their sum stay in \(\mathcal S\). The same conclusion holds
with \(\Re z=\alpha\) or \(|\Im z|=H_0\), as long as
\(\Re z<1/2\), because (11) is strict.

The particular values
\[
                       \alpha=\frac16,\qquad H_0=\frac{27}{250}
 \tag{13}
\]
satisfy (11). Here is an exact verification. The elementary
bound \(\pi<22/7\) gives
\[
 \frac{27\pi}{125}<\frac{594}{875}
                  <\frac{56}{81}<\log2.
 \tag{14}
\]
The middle comparison follows from \(48114<49000\). For the
last one, integrate the geometric series for \(1/(1-t^2)\)
from zero to \(1/3\):
\[
 \log2=2\sum_{j=0}^{\infty}\frac{(1/3)^{2j+1}}{2j+1}
       >\frac23+\frac2{81}=\frac{56}{81}.
 \tag{15}
\]
Thus \(e^{-27\pi/125}>1/2=\cos(\pi/3)\), as required.

At a regular limit with an individual real coordinate equal to
\(1/2\), continuity gives positive semidefiniteness. No assertion
about a holomorphic Hessian is made where \(z+w\) is an integer:
there the derivative in (1) is singular. Such boundary values
of the action must instead be treated by a separately justified
limit.

## 3. A quantitative form on compact subrectangles

Suppose, for both variables,
\[
 0<m\le\Re\cot(\pi z),\Re\cot(\pi w)\le M,\qquad
 |\Im\cot(\pi z)|,|\Im\cot(\pi w)|\le\rho<1.
 \tag{16}
\]
These constants exist on every closed subrectangle of (12)
whose right edge lies strictly below \(1/2\). They can be chosen
independently of the number of pairs to be combined.

Put
\[
 d_0=\frac{(1-\rho^2)m^2}{m^2+\rho^2},\qquad
 T_0=2M+\frac{M^2+\rho^2+1}{m},\qquad
                         \gamma_0=\pi d_0/T_0.
 \tag{17}
\]
Then
\[
                          -\Re V''\ \ge\gamma_0 I_2.
 \tag{18}
\]
To verify this, let \(S=a+c\) and \(T=b+d\). Formula (6)
and \(|ad-cb|\le\rho S\) imply
\[
 \det H\ge(1-\rho^2)\frac{S^2}{S^2+T^2}
          \ge d_0.
\]
Also the complex cotangent addition formula gives
\[
 |\cot\pi(z+w)|
 \le\frac{|\cot\pi z|\,|\cot\pi w|+1}{|\cot\pi z+\cot\pi w|}
 \le\frac{M^2+\rho^2+1}{2m}.
\]
Hence \(\operatorname{tr}H\le T_0\). A positive definite
two-by-two matrix has least eigenvalue at least its determinant
divided by its trace. Equations (17)--(18) follow.

## 4. Combining pairs on a graph

Let \(G=(\mathcal V,\mathcal E)\) be a finite graph without
loops; multiple edges are allowed. Assign a complex coordinate
\(z_v\) to each vertex. Some coordinates may be fixed boundary
data. Consider the holomorphic phase
\[
 \Phi(\mathbf z)=
 \sum_{e=uv}\lambda_e V(z_u,z_v)
       -\sum_v\mu_v g(z_v)
       +\frac i2\mathbf z^{\,T}B\mathbf z
       +\ell^T\mathbf z+c_0,
 \tag{19}
\]
where \(\lambda_e>0\), \(\mu_v\ge0\), \(B\) is real symmetric,
and \(\ell,c_0\) may be complex. The coefficients are fixed.
Every free coordinate must either be incident to an edge or
have \(\mu_v>0\).

**Theorem 2.** On the product of rectangles (12),
the negative holomorphic Hessian of (19) has positive definite
Hermitian part in the free coordinates. This conclusion holds
for every real symmetric matrix \(B\), with no bound on its size.

**Proof.** Each edge contributes the positive definite matrix
in Proposition 1 on its two endpoint coordinates. If one endpoint
is fixed, it contributes the corresponding positive principal
entry on the other coordinate. Each own term
\(-\mu_v g(z_v)\) contributes \(\pi\mu_v\Re\cot(\pi z_v)\ge0\)
to the negative real Hessian. Every nonzero free vector therefore
has a strictly positive contribution. The quadratic term
contributes \(-iB\) to the negative Hessian, with zero Hermitian
part. Linear terms contribute zero. \(\square\)

For a complex symmetric matrix its Hermitian part equals its
entrywise real part. Thus the conclusion applies to complex
vectors as well as to real horizontal variations.

If every free vertex is incident to an edge and
\(\lambda_e\ge\lambda_0>0\), the compact version (18) yields
\[
                         \Re[-\Phi'']\ge\lambda_0\gamma_0 I.
 \tag{20}
\]
This particular lower bound is independent of the number of
vertices and edges. It asserts uniform coercivity on the specified
domain; it does not assert that critical points for arbitrary
graphs or arbitrary quadratic coefficients lie in that domain.

## 5. Eliminating internal variables

Partition the free variables into internal variables \(\mathbf x\)
and retained boundary variables \(\mathbf y\). Suppose that a
critical point in \(\mathbf x\) exists at an interior point of
the domain:
\[
                    \partial_{\mathbf x}\Phi(\mathbf x_*,\mathbf y_*)=0.
 \tag{21}
\]
The internal Hessian is invertible by Theorem 2. The holomorphic
implicit function theorem therefore supplies a local function
\(\mathbf x(\mathbf y)\), with \(\mathbf x(\mathbf y_*)=\mathbf x_*\).
Define the conditional phase
\[
                    \Psi(\mathbf y)=\Phi(\mathbf x(\mathbf y),\mathbf y).
 \tag{22}
\]
Write \(A=-\Phi''\), evaluated on this critical graph. Direct
differentiation of (21)--(22) gives
\[
 -\Psi''=A_{yy}-A_{yx}A_{xx}^{-1}A_{xy}.
 \tag{23}
\]

**Theorem 3.** The matrix in (23) has positive definite Hermitian
part. If \(\Re A\ge\gamma I\), then
\[
                             \Re[-\Psi'']\ge\gamma I.
 \tag{24}
\]

**Proof.** For any complex boundary vector \(v\), set
\[
        u=\binom{-A_{xx}^{-1}A_{xy}v}{v}.
\]
Block multiplication gives
\[
 Au=\binom{0}{(-\Psi'')v},\qquad
 \Re(v^*(-\Psi'')v)=\Re(u^*Au).
 \tag{25}
\]
The latter is positive for \(v\ne0\). Under the quantitative
hypothesis it is at least
\(\gamma\|u\|^2\ge\gamma\|v\|^2\), proving (24).
\(\square\)

The same argument can be repeated for successive groups of
internal variables wherever their critical graphs exist inside
the domain. It does not require an additional estimate for the
Schur complement at each step.

There is at most one solution of (21) in each convex internal
fiber. Indeed the difference of the negative gradients at two
points, paired with the conjugate of their difference, has
strictly positive real part by integration of the Hessian along
the segment. It cannot vanish. This proves uniqueness, without
assuming existence.

The determinant identity
\[
           \det A=\det A_{xx}\,\det(-\Psi'')
 \tag{26}
\]
also retains nonvanishing of the local Gaussian determinant.
On a sufficiently small simply connected neighborhood its
square roots can be continued consistently. If the original
local amplitude is nonzero, elimination of these internal
variables cannot introduce a zero through this determinant.
The coefficient with which the original integration cycle
contains this local contribution is a separate question.

## 6. The phases in the present short-tangle attachment

For the original conditional phase
\[
 Q_\beta(t;y,z)
 =g(t+y)+g(t+z)-(2+\beta)g(t)-g(y)-g(z)+2\pi iyt,
 \qquad \beta\in\{0,1\},
 \tag{27}
\]
one has the exact decomposition
\[
 Q_\beta(t;y,z)-\frac12g(y)-\frac\beta2g(z)
 =V(t,y)+V(t,z)-\beta g(t)
             -\frac12g(y)-\frac\beta2g(z)+2\pi iyt.
 \tag{28}
\]
The first conditional phase after the cap has \(\beta=1\).
For the two adjacent conditional factors, the full shared weight
gives
\[
\begin{split}
 &Q_1(s;a,y)+Q_\beta(t;y,z)-g(y)-\frac\beta2g(z)\\
 &\quad=V(s,a)+V(s,y)+V(t,y)+V(t,z)\\
 &\qquad\quad-g(s)-\beta g(t)-g(y)-\frac\beta2g(z)
                         +2\pi ias+2\pi iyt.
\end{split}
 \tag{29}
\]
Thus all five variables in (29) have a strictly concave real
horizontal phase when their real parts lie in
\([1/6,1/2)\) and their heights have modulus at most \(27/250\).
The original shared weight has been retained in (29). No cap
term or finite endpoint term has been added or deleted.

There is a useful way to retain an older strict support bound.
For any real horizontal segment \(z_*+\tau d\) in a regular
domain of Theorem 2, Taylor's formula reads
\[
\begin{split}
 \Re\Phi(z_*+d)
  =\Re\Phi(z_*)+\Re(\nabla\Phi(z_*)^Td)
  -\int_0^1(1-\tau)\,
          d^T\Re[-\Phi''(z_*+\tau d)]d\,d\tau .
\end{split}
 \tag{30}
\]
If the negative real Hessian is at least \(\gamma I\) for
\(0\le\tau\le\theta\), and merely nonnegative afterward, then
\[
 \Re\Phi(z_*+d)
 \le\Re\Phi(z_*)+\Re(\nabla\Phi(z_*)^Td)
              -\gamma(\theta-\theta^2/2)\|d\|^2.
 \tag{31}
\]
This proves that extending a segment into the larger concavity
domain preserves the strict loss already accumulated near its
starting point. It does not require the target itself to remain
in the older smaller rectangle.

The conclusions concern the main holomorphic phases and the
local critical elimination. To obtain the original finite
attachment asymptotic, the real cuts, endpoint rows, other
Fourier terms, and connecting integrals must still be controlled.
Likewise, using (19) for other tangle compositions requires an
exact decomposition of their original phases and an existence
argument in the stated domain. Theorems 2 and 3 alone do not
establish the finite-exception theorem.
