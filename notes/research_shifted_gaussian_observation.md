# Gaussian observation after shifting the exact Fourier contour

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The original Fourier contraction is bilinear. Its lower bound cannot
in general be obtained from the positive norm on the original real
circle: that norm describes a different, reflected source. After a
complex contour shift, however, a Gaussian ground-state estimate gives
a precise sufficient observation bound. This note records that
standard estimate with the normalization needed by the original
source. It also identifies the inputs that the estimate does not prove.

The functional inequality below is the usual Gaussian Poincare, or
harmonic-oscillator gap, estimate. No novelty is claimed for it.
A classical primary reference is H. Chernoff,
[A note on an inequality involving the normal distribution,
Annals of Probability 9 (1981), 533--535](https://www.jstor.org/stable/2243541).
We give the proof of the version used here.

## 1. An annihilation estimate controls the Gaussian component

Let \(A=C+iD\) be a complex symmetric \(d\)-by-\(d\) matrix,
where \(C,D\) are real symmetric and \(C>0\). Define
\[
 g_A(y)=\left(\frac{\det C}{\pi^d}\right)^{1/4}
                  e^{-y^{\mathsf T}Ay/2},\qquad
 \mathscr D_A f=\nabla f+Ayf,\qquad c_A=\lambda_{\min}(C).
 \tag{1}
\]
Thus \(\|g_A\|_{L^2(\mathbb R^d)}=1\) and
\(\mathscr D_Ag_A=0\). The domain used below is
\[
 \mathcal Q=\{f\in L^2(\mathbb R^d):
       \nabla f\in L^2,\ |y|f\in L^2\},
 \tag{2}
\]
with weak derivatives. The norm of a vector-valued residual is the
sum of the squared \(L^2\) norms of its coordinates.

**Lemma 1.** For \(f\in\mathcal Q\), let
\(a=\int\overline{g_A}f\) and \(r=f-ag_A\). Then
\[
       \|r\|_2^2\le\frac{\|\mathscr D_A f\|_2^2}{2c_A}.
 \tag{3}
\]
In particular a nonzero vector with sufficiently small residual
relative to its norm has a nonzero Gaussian component.

**Proof.** Multiplication by
\(e^{-iy^{\mathsf T}Dy/2}\) is unitary and conjugates
\(\nabla+Cy\) to \(\mathscr D_A\). An orthogonal change of
coordinates diagonalizes \(C\), with eigenvalues \(c_j>0\).
For the real operator, integration by parts gives
\[
 (\nabla+Cy)^*(\nabla+Cy)
       =-\Delta+y^{\mathsf T}C^2y-\operatorname{tr}C.
 \tag{4}
\]
In each coordinate the normalized Hermite functions have eigenvalues
\(2c_j k_j\), \(k_j=0,1,\ldots\). This follows directly from
the operators \(\partial_j+c_jy_j\) and
\(-\partial_j+c_jy_j\), whose commutator is \(2c_j\);
their ground state is \(e^{-c_jy_j^2/2}\).
Expanding in the product Hermite basis, the ground coefficient has
eigenvalue zero and every other coefficient has eigenvalue at least
\(2\min_jc_j\). This proves (3) for finite Hermite sums and then
for the form domain (2) by approximation. Conjugate back to \(A\).
\(\square\)

This is stronger than small increments under ordinary translations.
The operator includes the restoring term \(Ay\). A nonzero Gaussian
is not invariant under ordinary translations in \(L^2\). Moreover,
\(\mathscr D_A\) is not a generator of a unitary action of the original
crossing matrices. Calling (3) almost-invariance is useful only when
this particular Gaussian normalization is specified.

## 2. The resulting bilinear lower bound

Let \(B=C_B+iD_B\) be another complex symmetric matrix with
\(C_B>0\). The bilinear Gaussian overlap is
\[
 \begin{split}
 \Gamma(A,B)&=\int_{\mathbb R^d}g_A(y)g_B(y)\,dy\\
 &=\frac{2^{d/2}(\det C\,\det C_B)^{1/4}}
                   {\sqrt{\det(A+B)}}\ne0.
 \end{split}
 \tag{5}
\]
The square root is the branch continued from positive real matrices.
The integral converges since \(\Re(A+B)>0\); the same positivity
implies that \(A+B\) is invertible. For the unnormalized Gaussian
integral, the formula follows first for positive real matrices and
then by holomorphic continuation through the accretive matrices.
Multiplying by the two real normalization factors in (1) gives (5).

**Proposition 2.** Let \(f,h\in\mathcal Q\) be nonzero. Set
\[
 \varepsilon_f=
 \frac{\|\mathscr D_A f\|_2}{\sqrt{2c_A}\|f\|_2},\qquad
 \varepsilon_h=
 \frac{\|\mathscr D_B h\|_2}{\sqrt{2c_B}\|h\|_2},
 \qquad \gamma=|\Gamma(A,B)|.
 \tag{6}
\]
If both errors are at most one, then
\[
 \begin{split}
 \frac{|\int fh|}{\|f\|_2\|h\|_2}
 \ge{}&\gamma\sqrt{1-\varepsilon_f^2}
                 \sqrt{1-\varepsilon_h^2}\\
      &-\varepsilon_f-\varepsilon_h-\varepsilon_f\varepsilon_h.
 \end{split}
 \tag{7}
\]
Consequently errors tending to zero give a lower bound
\(\gamma/2\) for all sufficiently large levels.

**Proof.** Normalize the two functions to have norm one. Lemma 1
gives decompositions
\[
 f=ag_A+r,\qquad h=bg_B+s,\qquad
 \|r\|\le\varepsilon_f,\quad \|s\|\le\varepsilon_h.
 \tag{8}
\]
Orthogonality gives
\(|a|\ge\sqrt{1-\varepsilon_f^2}\) and the analogous bound
for \(b\), while \(|a|,|b|\le1\).
Expand the bilinear integral. Its leading term is
\(ab\Gamma(A,B)\); Cauchy--Schwarz bounds the three remaining
terms by \(\varepsilon_h,\varepsilon_f,\varepsilon_f\varepsilon_h\).
This proves (7). \(\square\)

When \(A=B=C+iD\), the overlap has the especially simple modulus
\[
 |\Gamma(A,A)|
   =\det\!\left(I+(C^{-1/2}DC^{-1/2})^2\right)^{-1/4}>0.
 \tag{9}
\]
Quadratic phase variation therefore need not be small. It has a
nonzero Gaussian average. The constants may depend on the fixed
number of variables; this statement is not uniform for a number of
tangles growing with the level.

## 3. Application to an exact Fourier coefficient

Suppose the original finite source has the exact contour identity
\[
 Z_N=\rho_N\int_{\mathcal C}U_N(z)V_N(z)\,dz,
 \tag{10}
\]
where \(\mathcal C\) is a shifted \(d\)-dimensional Fourier cycle.
Any contours, branches and endpoint corrections needed to establish
(10) are part of the hypothesis. For the original internal pair,
\(d=1,\rho_N=N\), and (10) is the exact full-Hermite circle identity.

Choose a real local coordinate \(z=z_*+y/\sqrt N\) on this cycle
and a smooth cutoff \(\chi\), equal to one near zero and compactly
supported in that coordinate chart. Assume \(U_N,V_N\) are
holomorphic on a neighborhood of its support. For a fixed vector
\(\ell\), put
\[
 \begin{split}
 f_N(y)&=\chi(y/\sqrt N)e^{-\sqrt N\,\ell^{\mathsf T}y}
                          U_N(z_*+y/\sqrt N),\\
 h_N(y)&=\chi(y/\sqrt N)e^{+\sqrt N\,\ell^{\mathsf T}y}
                          V_N(z_*+y/\sqrt N).
 \end{split}
 \tag{11}
\]
The opposite linear gauges cancel in the product. They allow the
two individual phase gradients to be opposite at the common saddle;
when both individual gradients vanish, take \(\ell=0\).
Extend the cutoff functions by zero to \(\mathbb R^d\). They belong
to (2). With the actual complementary integral denoted by \(R_N\),
\[
       Z_N=\rho_NN^{-d/2}\int f_Nh_N+R_N.
 \tag{12}
\]

**Corollary 3.** Suppose the following three estimates hold:

1. For fixed \(A,B\) as above, the two relative residuals in (6),
   computed for the actual functions (11), tend to zero.
2. For some real \(M_1,M_2\),
   \(\log\|f_N\|_2=NM_1+o(N)\) and
   \(\log\|h_N\|_2=NM_2+o(N)\).
3. \(\log|\rho_N|=o(N)\) and
   \[
    |R_N|=o\!\left(
        |\rho_N|N^{-d/2}\|f_N\|_2\|h_N\|_2\right).
    \tag{13}
   \]

Then, for all sufficiently large levels,
\[
 |Z_N|\ge\frac{\gamma}{4}|\rho_N|N^{-d/2}
                             \|f_N\|_2\|h_N\|_2,
 \qquad
 \lim_{N\to\infty}\frac{\log|Z_N|}{N}=M_1+M_2.
 \tag{14}
\]
The lower bound follows from (7) and (13); the upper bound is
Cauchy--Schwarz in (12). Norm lower bounds alone, together with
(13), give the corresponding lower exponential bound.

The cutoff must not conceal a boundary error in the residual.
For example,
\[
 \mathscr D_A(\chi(y/\sqrt N)F_N)
 =\chi(y/\sqrt N)\mathscr D_AF_N
       +N^{-1/2}(\nabla\chi)(y/\sqrt N)F_N.
 \tag{15}
\]
The second term must be \(o(\|f_N\|_2)\). An individual strict
annular bound and an independent norm lower bound ensure this.
A bound only on the product \(U_NV_N\) does not by itself control
the individual commutator in (15). Likewise, local coercivity does
not imply (13): the other parts of the original cycle must be bounded.

## 4. What this says about the proved pair

For the [internal \(3,3\) source](research_internal_pair_three_full_boundary_packet.md),
the actual shifted state already has a nonzero local expansion
\[
 W_{3,N}(x,0)=C_{N,3}N^{-1}a(x)e^{NS(x)}(1+O(N^{-1})),
 \quad a(x_*)\ne0,\quad S'(x_*)=0,\quad \Re S''(x_*)<0.
 \tag{16}
\]
All complementary parts of its shifted circle have a strict gap.
Thus (11) with \(\ell=0\) and \(A=B=-S''(x_*)\) has vanishing
relative annihilation residual. Taylor expansion on the
\(N^{-1/2}\) scale gives this directly; the strict local real-part
bound controls the rescaled tails, and the annular gap controls (15).
Its norm is
\[
 \|f_N\|_2=
 N^{-1}e^{N\Re S(x_*)}
       \left(|a(x_*)|
          \left(\frac{\pi}{-\Re S''(x_*)}\right)^{1/4}
          +o(1)\right).
 \tag{17}
\]
The exact circle normalization in (12) is \(N^{1/2}\).
Consequently (14) recovers a positive constant times
\(N^{-3/2}e^{2N\Re S(x_*)}\), the already-proved lower bound.

Here the annihilation statement is a consequence of the established
packet. It is not an independent proof of its amplitude or norm.
In particular it does not prove a real-circle estimate for
\(|w_3^{\mathsf T}w_3|/\|w_3\|^2\). The
[actual long-pair comparison](research_complete_boundary_coefficient_transport.md#7-exponentially-small-coherence-in-an-actual-long-power-family)
shows exponential decay of that ratio for all sufficiently large
fixed same-sign powers. Multiplying by a scalar volume normalization
does not change the ratio.

## 5. The possible route for other short chains

There are two different ways to supply the residual in Corollary 3.
An already-proved nonzero holomorphic packet supplies it by Taylor
expansion, as in (16). Alternatively one could derive it directly
from the original finite quantum equations after localization at the
geometric characteristic point. The second route would be useful:
Lemma 1 then supplies a nonzero Gaussian component from the state
norm, without presupposing that component's coefficient.

The [exact Fourier difference equation](research_complete_boundary_coefficient_transport.md#8-an-exact-difference-equation-for-the-entire-fourier-interpolation)
is a concrete starting point. Its forcing, finite Fourier band and
endpoint normalization are fixed by the original source. A local
linearization must be justified as an operator estimate on that
actual state, including its higher derivative remainders. A formal
simple characteristic root does not justify this step or select the
globally continued solution.

The [mixed-phase concavity theorem](research_mixed_wire_phase_concavity.md)
supplies a strict quadratic real-part bound on its explicit convex
domain. It is useful for localization and, when a source-level
representation is available there, for estimating annular terms.
It does not by itself give the independent state-norm lower bound,
the relative residual of the actual solution, or the full-cycle
estimate (13). A joint positive Hessian also need not supply separate
positive matrices \(A,B\) in an arbitrary chosen factorization;
Corollary 3 explicitly requires those individual Gaussian bounds.

For a fixed longer chain, a proof may instead keep all shared wire
variables and seek one coercive multidimensional contour, while
retaining the exact trace currents and finite endpoint terms.
The known concavity region is a candidate for its central part.
To replace individual contour certificates by a general theorem,
one still needs uniform control of the parts outside that region
and a source normalization that forces the required norm growth.
The annihilation estimate makes the observation step precise; it
does not remove these remaining global requirements.
