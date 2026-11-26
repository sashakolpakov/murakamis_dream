# Exact Gaussian windows for the original Newton operators

Research calculation, 3 November 2026. Frozen manuscripts are unchanged.

The Gaussian observation estimate already in the notes is conditional
on a localized source norm. Here we instead give an exact positive
frame for the full finite Newton space and compute how its windows
transform under the actual crossing and turn. A crossing image is a
Gaussian integral of a finite Pochhammer product. Its normalization
is explicit and does not involve an unknown knot invariant.

The resolution of identity is the elementary Gaussian version of a
finite Fourier frame. The source-specific calculation is the
Pochhammer formula for the original full crossing, with its scalar
and both endpoints retained. No general short-chain asymptotic is
inferred from the frame identity.

## 1. A positive frame with no discarded coordinates

Put
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \kappa=q^{D^2/2},\qquad N\ge2.
 \tag{1}
\]
Use the usual positive inner product on the full Newton coefficient
space \(\mathbb C^N\), conjugate-linear in its first argument.
For a fixed \(\sigma>0\), \(\xi\in\mathbb R\), and
\(z=e^{i\theta}\), define
\[
 \begin{split}
 c_N&=\left(\frac{N}{\pi\sigma}\right)^{1/4},\\
 g_{\xi,z}(k)&=c_N
       \exp\!\left[-\frac{(k-N\xi)^2}{2\sigma N}\right]
                        (z/q)^k,\qquad 0\le k\le D,\\
 (\mathcal F_N w)(\xi,\theta)&=\langle g_{\xi,e^{i\theta}},w\rangle,
 \qquad d\mu=d\xi\,\frac{d\theta}{2\pi}.
 \end{split}
 \tag{2}
\]
The center \(\xi\) ranges over the whole real line; it is not
truncated near either endpoint of the Newton index interval.

**Lemma 1.** There are exact identities
\[
 \int g_{\xi,z}g_{\xi,z}^*\,d\mu=I,\qquad
 \int|\mathcal F_Nw|^2\,d\mu=\|w\|_2^2,\qquad
 w=\int g_{\xi,z}(\mathcal F_Nw)(\xi,\theta)\,d\mu .
 \tag{3}
\]
In particular the range of \(\mathcal F_N\) is a positive
reproducing-kernel space of dimension \(N\).

**Proof.** Integrating \(\theta\) makes the \(j,k\) entry zero
unless \(j=k\). On the diagonal the remaining integral is
\[
 c_N^2\int_{\mathbb R}
       e^{-(k-N\xi)^2/(\sigma N)}\,d\xi
              =c_N^2\sqrt{\pi\sigma/N}=1.
 \tag{4}
\]
This proves all three formulas. Its reproducing kernel is
\[
 \begin{split}
 \mathcal K_N((\xi,\theta),(\eta,\varphi))
 &=\langle g_{\xi,e^{i\theta}},g_{\eta,e^{i\varphi}}\rangle\\
 &=c_N^2e^{-N(\xi-\eta)^2/(4\sigma)}
   \sum_{k=0}^D
       e^{-(k-N(\xi+\eta)/2)^2/(\sigma N)}
                         e^{ik(\varphi-\theta)}.
 \end{split}
 \tag{5}
\]
It is positive because it is a Gram kernel. \(\square\)

For the exact half-band Fourier interpolation \(W_N\) whose samples
are \(w_k=W_N(k/N)\), (2) is literally a Gaussian-windowed finite
Fourier transform of those samples. It changes neither the
interpolation nor its finite-dimensional normalization.

## 2. The turn and crossing on a Gaussian window

The original turn is \(Jw(k)=w(D-k)\). Direct substitution gives
\[
 Jg_{\xi,z}
        =(z/q)^Dg_{D/N-\xi,Q/z},\qquad
 \mathcal F_N(Jw)(\xi,\theta)
        =(q/z)^D
          \mathcal F_Nw(D/N-\xi,2\pi/N-\theta).
 \tag{6}
\]
The scalar has modulus one on the frame circle. Thus this
transport is exact, including the endpoint centers.

The full original crossing is the matrix
\[
 M_{jk}=\kappa(-1)^j q^{j+k^2}
                {j\brack k}_Q\quad(0\le k\le j\le D),
 \qquad M_{jk}=0\quad(k>j).
 \tag{7}
\]
These are the full Newton entries of
[the exact crossing equations](actual_newton_twist_canonical_graph.md),
not their values in a semisimple quotient.
For a polynomial in \(z\), let \(\mathscr E=z\partial_z\) and
define the finite heat operator
\[
 \mathscr H_{\xi,N}
       =\exp[-(\mathscr E-N\xi)^2/(2\sigma N)] .
 \tag{8}
\]
Thus its multiplier on \(z^k\) is the Gaussian in (2).
There is no convergence convention in this definition.

**Lemma 2.** For every \(j=0,\ldots,D\),
\[
 \begin{split}
 (Mg_{\xi,z})_j
   &=c_N\kappa(-q)^j
                    \mathscr H_{\xi,N}(-z;Q)_j,\\
 (M^{-1}g_{\xi,z})_j
   &=c_N\kappa^{-1}(-q^{-1})^j
                    \mathscr H_{\xi,N}(-z/Q;Q^{-1})_j.
 \end{split}
 \tag{9}
\]
Both are polynomial identities in \(z\), so their validity is not
restricted to \(|z|=1\). Here
\((a;Q)_j=\prod_{\nu=0}^{j-1}(1-aQ^\nu)\).

**Proof.** First omit the Gaussian multiplier and put
\(r_z(k)=(z/q)^k\). The finite binomial theorem gives
\[
 \begin{split}
 (Mr_z)_j
 &=\kappa(-q)^j\sum_{k=0}^j
              {j\brack k}_Q Q^{k(k-1)/2}z^k\\
 &=\kappa(-q)^j(-z;Q)_j .
 \end{split}
 \tag{10}
\]
Apply (8) coefficientwise to obtain the first identity in (9).
The exact relation \(M^{-1}=\overline M\) replaces \(q,Q,\kappa\)
by their inverses. Its natural input is
\((z'/q^{-1})^k\); choosing \(z'=z/Q\) gives the original
\((z/q)^k\). This proves the second identity. All factorial
indices in the finite binomial theorem are below \(N\);
no root-of-unity denominator is introduced. \(\square\)

Equivalently, the first formula has the entire integral form
\[
 (Mg_{\xi,z})_j
 =c_N\kappa(-q)^j\sqrt{\frac{\sigma N}{2\pi}}
       \int_{\mathbb R}
       e^{-\sigma N t^2/2-iN\xi t}
                     (-ze^{it};Q)_j\,dt .
 \tag{11}
\]
Indeed the Gaussian Fourier integral multiplies the \(k\)-th
monomial by \(e^{-(k-N\xi)^2/(2\sigma N)}\).
The integral is absolutely convergent, and its integrand contains
only a Gaussian and a finite product. Equation (11) is therefore
an exact one-crossing source representation with a specified
coefficient, suitable for a subsequent contour estimate.

## 3. Exact words and their original boundary data

For any original matrix \(V\), define
\[
 \mathcal V_N(\alpha,\beta)
           =\langle g_\alpha,Vg_\beta\rangle,
              \qquad \alpha=(\xi,\theta).
 \tag{12}
\]
The frame resolution gives
\[
 \mathcal F_N(Vw)(\alpha)
     =\int\mathcal V_N(\alpha,\beta)
                          \mathcal F_Nw(\beta)\,d\mu(\beta),
 \qquad
 \langle g_\alpha,UVg_\beta\rangle
     =\int\mathcal U_N(\alpha,\gamma)
                \mathcal V_N(\gamma,\beta)\,d\mu(\gamma).
 \tag{13}
\]
These are exact identities for arbitrary signed words in
\(M,J\). Substituting (9) into (12) gives their one-crossing
kernel explicitly; (6) handles every turn without approximation.

The original rational-word source matching identifies the physical
four-plat scalar, with its prescribed external framing factor,
with \(\mathbf e_D^*V\mathbf e_0\); see Section 4 of
[the source intertwiner](actual_newton_twist_canonical_graph.md).
The two frame coefficients are explicitly
\[
 \begin{split}
 \mathcal F_N\mathbf e_0(\xi,\theta)
     &=c_Ne^{-N\xi^2/(2\sigma)},\\
 \mathcal F_N\mathbf e_D(\xi,\theta)
     &=c_Ne^{-(D-N\xi)^2/(2\sigma N)}
                              e^{-iD(\theta-\pi/N)} .
 \end{split}
 \tag{14}
\]
Hence the same original scalar is
\[
 \mathbf e_D^*V\mathbf e_0
      =\int\overline{\mathcal F_N\mathbf e_D(\alpha)}
                     \mathcal F_N(V\mathbf e_0)(\alpha)\,d\mu(\alpha).
 \tag{15}
\]
No unknown period was used to choose the frame or normalize its
two boundary functions. Those functions are concentrated near
opposite index endpoints and are not concentrated at a single
Fourier angle. The original cap is consequently still a boundary
family; it has not become a chosen interior geometric state.

## 4. What positive windows do not establish

The full norm in (3) is independent of \(\sigma\). Applied to the
actual complete-boundary vector \(w_n=JM^n\mathbf e(-2)\), it is
exactly the reflected source
\[
           \int|\mathcal F_Nw_n|^2d\mu
                 =\|w_n\|_2^2=\mathcal P_{n,-n,N}(0,0),
 \tag{16}
\]
whereas the same-sign source is \(w_n^{\mathsf T}w_n\).
The actual long-power examples in
[the coefficient transport theorem](research_complete_boundary_coefficient_transport.md)
give different exponential rates for these two expressions.
Thus choosing a Gaussian width cannot turn this full positive
norm into the desired same-sign rate.

A positive weight \(e^{-2N\varphi(\alpha)}\) may depend on a
proposed geometric action, but then the frame operator becomes
\[
 H_{\varphi,N}
   =\int e^{-2N\varphi(\alpha)}g_\alpha g_\alpha^*\,d\mu(\alpha).
 \tag{17}
\]
Whenever the integral is finite and the weight is positive almost
everywhere, this matrix is positive definite. Exact reconstruction
uses \(H_{\varphi,N}^{-1}\), or the corresponding normalized dual
frame. It cannot keep (3) unchanged after simply inserting the
weight. Bounds on that inverse, the original boundary cost, and
the mass outside the selected region remain necessary.

Equations (6), (9), (13), and (14) supply concrete finite operators
and boundary data for such a weighted construction. They do not
prove its geometric localization or a norm lower bound at the
required exponential rate. In particular, positive definiteness
of the reproducing kernel does not make the crossing kernel
\(\mathcal V_N\) entrywise nonnegative.
The useful next analytic statement would estimate (11) on an
explicit positive branch and propagate that estimate through (13),
including the complementary frame region and the two boundary
functions (14). That statement has not been assumed here.

The [finite checker](../experiments/check_gaussian_frame_newton_transport.py)
builds \(M\) from its original sine-factorial entries and the
features from independent Pochhammer coefficient multiplication.
Its [saved result](../repro/results/research-gaussian-frame-newton-transport.json)
contains 972 diagnostics at 65 digits, for levels \(2\) through
\(10\), including both signs, centers outside the index interval,
and parameters off the frame circle. These checks concern the
exact crossing and turn formulas, not an asymptotic coefficient.

## 5. Diagonal weights cannot make the original Gram matrix nonnegative

The positivity of a Hilbert-space norm must be distinguished from
entrywise positivity of its matrix kernel. For the original crossing,
an exact obstruction to the latter survives every positive diagonal
weight.

**Proposition 4.** Let \(N\ge3\), let
\(W=\operatorname{diag}(\omega_0,\ldots,\omega_D)\) with every
\(\omega_j>0\), and put \(G=M^*WM\). Then
\[
 G_{0,D-1}G_{D-1,D}G_{D,0}
       =\omega_D^2(\omega_D-\omega_{D-1}Q).
 \tag{18}
\]
Its imaginary part is strictly negative. Consequently no diagonal
phase change makes \(G\) entrywise real and nonnegative. The same
conclusion holds after arbitrary invertible diagonal input and output
scalings of \(M\).

*Proof.* The last two rows in (7) have the entries
\[
 \begin{array}{lll}
 M_{D,0}=\kappa(-1)^Dq^D,&
 M_{D,D-1}=\kappa(-1)^Dq^{D^2},&
 M_{D,D}=\kappa,\\
 M_{D-1,0}=\kappa(-1)^{D-1}q^{D-1},&
 M_{D-1,D-1}=\kappa(-1)^{D-1}q^{D(D-1)}.&
 \end{array}
 \tag{19}
\]
Their moduli are one. In the off-diagonal entry involving the last
two columns, use
\({D\brack1}_Q=(1-Q^D)/(1-Q)=-Q^{-1}\)
and \(q^N=-1\). Triangularity now gives
\[
 \begin{split}
 G_{0,D-1}&=\omega_{D-1}q^{(D-1)^2}
                         +\omega_Dq^{D(D-1)},\\
 G_{D-1,D}&=\omega_D(-1)^Dq^{-D^2},\\
 G_{D,0}&=\omega_D(-1)^Dq^D.
 \end{split}
 \tag{20}
\]
Multiplication proves (18), because
\(q^{1-D}=q^{2-N}=-Q\).
Since \(N\ge3\), one has \(\sin(2\pi/N)>0\); the imaginary
part is \(-\omega_D^2\omega_{D-1}\sin(2\pi/N)<0\).

A diagonal phase conjugation leaves every cyclic product of
matrix entries unchanged. More generally, replacing \(G\) by
\(C^*GC\), with \(C\) invertible and diagonal, multiplies the
product in (18) by the positive number
\(|C_{00}C_{D-1,D-1}C_{DD}|^2\).
An arbitrary diagonal output scaling of \(M\) merely replaces
\(W\) by another strictly positive diagonal matrix. These facts
prove the final assertion. \(\square\)

Thus an exact Perron--Frobenius argument cannot be obtained by
making this original Gram matrix entrywise nonnegative with diagonal
weights and phases. Its quadratic form is still positive definite.
The proposition does not exclude non-diagonal positive forms,
approximately positive kernels after a justified localization, or
a global contour construction. In particular, an approximation
which discards the endpoint rows would need its own error bound
for the actual cap; the one-crossing norm estimate alone does
not provide that bound.
