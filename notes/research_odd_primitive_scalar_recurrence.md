# A scalar equation and an explicit primitive odd source polynomial

Research note, 3 November 2026.

The original odd-run horizontal section admits a scalar equation of
order independent of the quantum level. Its boundary conditions are
the original cap, not an arbitrary solution of the classical curve.
For powers \(3\) and \(-3\), that section is explicitly polynomial:
its last coordinate has degree \(N-1\), and its reversed coefficients
are finite Gaussian-binomial sums. Discrete Parseval then gives an
exact positive formula for the original reflected closing scalar.

The exponential lower bound proved here is a source statement.
The [full three-crossing profile](research_three_crossing_full_coefficient_profile.md)
subsequently proves its sharp reflected norm; neither note identifies
that odd-link rate with a geometric volume. In particular a
constant selected odd monodromy eigenvalue does not bound the size
of its primitive normalized section.

## 1. Scalar elimination for every odd power

Fix \(N\ge2\) and \(p=\sigma(2k-1)\), where \(k\ge1\) and
\(\sigma\in\{1,-1\}\). Throughout this note use the signed clocks
\[
 q=e^{\sigma\pi i/N},\qquad Q=q^2,\qquad
 X=x^N,\qquad w(x)=(1-x)(1-x^{-1}).
 \tag{1}
\]
Let \(f=(f_1,\ldots,f_k)^T\) be the primitive polynomial section
of [the odd source theorem](research_odd_run_simple_spectrum_and_marked_kernel.md),
and put \(\phi=f_k\). Thus
\[
 T(x)f(x)=-q f(Qx),\qquad
 f_a(Q)=q^{k-a},\qquad
 (M^p e_0)_j=\kappa^p(-q)^j\phi(Q^{j+1}).
 \tag{2}
\]
The scalar \(\kappa\) in (2) is the original unsigned crossing
scalar; its signed power is exactly the one shown.

Write \(E^{-1}g(x)=g(Q^{-1}x)\). Define Laurent difference
operators, with multiplication coefficients always on the left,
by
\[
 \begin{split}
 \mathscr L&=q^{-1}x+qx^{-1}
                 +q^{-1}w(Q^{-1}x)E^{-1},\\
 \mathscr L_0&=qx^{-1}
                 +q^{-1}(1-Qx^{-1})E^{-1},\\
 V_r&=U_r(\mathscr L/2)-q^{-1}U_{r-1}(\mathscr L/2).
 \end{split}                                                    \tag{3}
\]
Here \(U_0=1,U_1(z)=2z\), and
\(U_{-1}=0,U_{-2}=-1\). In particular \(V_0=1\) and
\(V_{-1}=q^{-1}\). Powers in \(U_r(\mathscr L/2)\) are
compositions of the same operator; they do not commute the
multiplication coefficients past a shift.

**Theorem 1.** Every channel is recovered from the last one by
\[
 f_a=V_{k-a}\phi,\qquad
 \boxed{\quad(\mathscr L_0V_{k-1}-V_{k-2})\phi=0.\quad}
 \tag{4}
\]
The latter has shift order at most \(k\), with Laurent polynomial
coefficients whose degrees are bounded in terms of \(k\), not \(N\).
Conversely, a scalar solution of (4) whose reconstructed channels
are polynomial gives a polynomial horizontal section. The original
section is selected by the full cap conditions
\[
              (V_{k-a}\phi)(Q)=q^{k-a}\quad(1\le a\le k)
 \tag{5}
\]
and the requirement that the reconstructed vector be primitive.
These requirements have exactly one solution, by the odd source
theorem. No unspecified initial coefficient is discarded.

*Proof.* The literal odd transfer satisfies
\[
 H(x)T(x)=D(x),\quad
 H(x)=(qx+q^{-1}x^{-1})I-T_k-qxE_{11}-q^{-1}E_{kk},
 \quad
 D(x)=\operatorname{diag}(1-x^{-1},w(x),\ldots,w(x)).
 \tag{6}
\]
Combining (2) and (6), then replacing \(x\) by \(Q^{-1}x\),
gives \(H(Q^{-1}x)f(x)=-q^{-1}D(Q^{-1}x)f(Q^{-1}x)\).
Starting at its last row gives
\[
 f_{k-1}=(\mathscr L-q^{-1})f_k,\qquad
 f_{a-1}=\mathscr L f_a-f_{a+1}\quad(2\le a<k).
 \tag{7}
\]
The Chebyshev recurrence proves the first part of (4). The first
row is \(\mathscr L_0 f_1-f_2=0\), proving its scalar equation.
For \(k=1\) the two boundary modifications occupy the same entry:
the equation is \((\mathscr L_0-q^{-1})\phi=0\), exactly the
formula in (4). All operations were identities over the Laurent
function field. The converse follows by reversing these row
identities; polynomial continuation supplies any removable point.
Finally (5) is the unchanged cap in (2), and primitive uniqueness
is precisely the cited source theorem. \(\square\)

The rational shifts in (3) are an elimination device. They are
not inverses of the nilpotent multiplication operator in a truncated
generating-function model.

## 2. Powers three: an explicit primitive polynomial

For \(k=2\), division of the actual transfer by \(-q\) gives
\[
 \frac{T(x)}{-q}=
 \begin{pmatrix}
  1-x+Qx^2&-qx(x-1)\\
  qx&1-x
 \end{pmatrix}.
 \tag{8}
\]
Its two rows eliminate to
\[
 (E-Q)\{E\phi-(1-x)^2\phi\}=0.
 \tag{9}
\]
For a polynomial section this means
\(E\phi-(1-x)^2\phi=xh(x^N)\), for some polynomial \(h\).
The original primitive cap fixes this central forcing exactly.

Define the finite polynomial
\[
 R_N(x)=\sum_{j=0}^{N-1}Q^j x
                      \prod_{m=j+1}^{N-1}(1-Q^m x)^2 .
 \tag{10}
\]

**Theorem 2.** The polynomial \(R_N\) is divisible by \(x^N\).
Put \(P_N(x)=R_N(x)/x^N\); the letter \(P_N\) here denotes
this scalar source polynomial, not the spectral quotient relation.
Then \(P_N\) is monic of degree \(N-1\), and the actual
primitive section for \(p=\sigma3\) is
\[
 \boxed{\quad
 f(x)=
 \begin{pmatrix}
 q^{-1}\{2-x^N-(1-x)P_N(x)\}\\
 P_N(x)
 \end{pmatrix},\qquad
 P_N(Qx)=(1-x)^2P_N(x)+x(2-x^N).
 \quad}                                                        \tag{11}
\]
In particular \(P_N(Q)=1\), \(f(Q)=(q,1)^T\), and the
central forcing in (9) is \(h(X)=2-X\).

*Proof.* Iterating the scalar equation
\(y(Qx)=(1-x)^2y(x)+x\), or shifting the finite sum (10),
gives the polynomial identity
\[
 R_N(Qx)-(1-x)^2R_N(x)=x^{N+1}(2-x^N).
 \tag{12}
\]
The constant coefficient of \(R_N\) is zero. If its first nonzero
term had degree \(d<N\), comparison of that term in (12) would
give \(Q^d=1\), a contradiction. Thus \(x^N\) divides \(R_N\).
Its highest degree is \(2N-1\); only \(j=0\) contributes there,
and its leading coefficient is
\(Q^{2(1+\cdots+(N-1))}=1\). This proves the degree and
monicity and, after division, the second identity in (11).
Substitution of the displayed vector into (8) verifies its full
horizontal equation. Evaluating the scalar equation at \(x=1\)
gives \(P_N(Q)=1\), and hence the stated cap.

It remains to check primitivity. A common zero of its components
would satisfy \(x^N=2\) and \(P_N(x)=0\). At such a point the
transfer is invertible: \(\det T(x)=q^2(1-x)^2\).
The horizontal equation propagates a common zero around the
entire orbit of \(Q\). This would give \(N\) distinct roots
of the degree-\(N-1\) polynomial \(P_N\), which is impossible.
The vector is therefore primitive, so the unique original
normalization is exactly (11). \(\square\)

This proof retains the forcing \(2-X\). Dropping it would give
the homogeneous equation with period multiplier \((1-X)^2\),
which has no nonzero rational solution on the generic clock.

## 3. Coefficients, discrete Parseval, and an original positive source

Write the reversed coefficients as
\[
 P_N(x)=\sum_{j=0}^{N-1}b_jx^{N-1-j}.
 \tag{13}
\]
Comparing coefficients in (11) gives
\[
 b_0=1,\qquad b_1=2,\qquad
 b_{j+1}=2b_j-(1-Q^{-j})b_{j-1}\quad(1\le j\le N-2).
 \tag{14}
\]
For \(N=2\), only the first two values are needed.
Equivalently, with Gaussian binomial coefficients understood
polynomially,
\[
 b_j=\sum_{r=0}^j {j\brack r}_{Q^{-1}},
 \qquad 0\le j<N.
 \tag{15}
\]
To verify (15) directly, the usual finite product definition and
its elementary Pascal identity give
\[
 \sum_r {j+1\brack r}_z
  =2\sum_r{j\brack r}_z
                  -(1-z^j)\sum_r{j-1\brack r}_z.
 \tag{16}
\]
For example, subtract the weighted sum
\(\sum_r z^{j-r}{j\brack r}_z\) from the unweighted sum;
the difference is
\((1-z^j)\sum_r{j-1\brack r}_z\). The initial values are
one and two. At \(z=Q^{-1}\) no denominator in the product
definition vanishes for \(j<N\). This proves (15) without
an asymptotic or positivity assumption on its complex summands.

The sums (15) are the classical Rogers--Szegő polynomials at
argument one, also called Galois polynomials. Their definition and
recurrence are recorded, for example, in C. Ryan Vinroot,
[Multivariate Rogers--Szegő polynomials and flags in finite vector spaces,
Section 1, equation (1.1)](https://arxiv.org/pdf/1011.0984).
These polynomial identities are not new. Here they arise as the
exact coefficients of the primitive original source, with the cap
normalization and Fourier factor in (17) fixed.

**Corollary 3.** The literal reflected closing source is
\[
 \boxed{\quad
 \phi_N(R^{-3}T(R^3))
   =\sum_{j=0}^{N-1}|(M^3e_0)_j|^2
   =N\sum_{j=0}^{N-1}|b_j|^2 .
 \quad}                                                        \tag{17}
\]
The same formula holds after reversing both signs.

*Proof.* The original crossing satisfies
\(\overline M=M^{-1}\), and the original turned closure
is the bilinear coefficient pairing. Formula (2), with
\(|\kappa|=|-q|=1\), identifies its reflected value with
\(\sum_j|P_N(Q^{j+1})|^2\). Since \(P_N\) has degree \(N-1\),
the finite Fourier orthogonality is exact and has no aliased
coefficient sums. It gives (17). \(\square\)

The literal two-run closure with two odd powers has two
components. Thus (17) is an original positive link source;
it is not being relabeled as a knot result.

## 4. A quantitative lower bound and its limit

Let \(G=\int_0^{\pi/4}\log(\cot u)\,du\), Catalan's constant.

**Theorem 4.** For every fixed \(0<\delta<1/2\), uniformly for
\(0\le j\le\delta N\),
\[
 \log|b_j|
   =N\int_0^{j/N}\log\!\left(2\cos\frac{\pi t}{2}\right)\,dt
                   +O_\delta(1).
 \tag{18}
\]
In particular these coefficients are nonzero for all sufficiently
large \(N\), and the actual source satisfies
\[
 \liminf_{N\to\infty}\frac1N
       \log\phi_N(R^{-3}T(R^3))\ \ge\ \frac{2G}{\pi}>0.
 \tag{19}
\]

*Proof.* Conjugation handles \(\sigma=-1\). For positive sign,
(14) is the exact transfer with
\[
 K(t)=\begin{pmatrix}2&-(1-e^{-2\pi it})\\1&0\end{pmatrix},
 \qquad
 \lambda_\pm(t)=1\pm e^{-\pi it}.
 \tag{20}
\]
On \(0\le t\le\delta\), the eigenvectors
\((\lambda_\pm(t),1)^T\) form a uniformly invertible smooth
frame. Moreover
\[
 \frac{|\lambda_-(t)|}{|\lambda_+(t)|}
       =\tan(\pi t/2)\le\tan(\pi\delta/2)<1.
 \tag{21}
\]
The initial vector \((b_1,b_0)^T=(2,1)^T\) is exactly the
positive eigenvector at zero. Consecutive frames differ by
\(I+O_\delta(N^{-1})\). In this frame the ratio of the other
coordinate to the positive one stays \(O_\delta(N^{-1})\):
the ratio recurrence has contraction factor bounded strictly
below one, with forcing \(O_\delta(N^{-1})\); induction from
ratio zero proves the claim. Its dominant coordinate is
therefore multiplied at step \(j\) by
\(\lambda_+(j/N)(1+O_\delta(N^{-1}))\). All these factors
are nonzero for large \(N\). The first coordinate observation
also remains bounded away from zero relative to that dominant
coordinate. Taking logarithms, summing the bounded per-step
errors, and using the smooth Riemann sum proves (18).

In (17), keep the single nonnegative term with
\(j=\lfloor\delta N\rfloor\). This proves the lower bound
twice the integral in (18). Letting \(\delta\uparrow1/2\)
gives (19), since
\[
 \int_0^{1/2}\log(2\cos(\pi t/2))\,dt
       =\frac2\pi\int_0^{\pi/4}\log(2\cos u)\,du
       =\frac G\pi .
 \tag{22}
\]
The last equality follows by adding the sine and cosine
integrals and using \(2\sin u\cos u=\sin(2u)\), together
with the defining difference for \(G\). \(\square\)

Thus the primitive vector's norm on its actual color orbit is
exponentially large in at least this odd example, despite its
constant selected forward eigenvalue. The polynomial normalization
and exact full-period identity alone cannot supply a uniform
subexponential frame bound. Equations (4)--(5) give the corresponding
scalar framework at every odd power. For powers three, the
[full coefficient profile](research_three_crossing_full_coefficient_profile.md)
now proves the sharp reflected norm by a separate argument.
The coherent joining with another nonreflected run and a whole-boundary
asymptotic still require further estimates. Neither is inferred
from (19).

## 5. Finite reproduction

Run

    .venv/bin/python experiments/check_odd_primitive_scalar_recurrence.py \
      --precision 120 \
      --output repro/results/research-odd-primitive-scalar-recurrence.json

The [checker](../experiments/check_odd_primitive_scalar_recurrence.py)
starts with the original crossing matrices. It checks all channel
reconstructions in (4) and their actual caps for \(N=2,\ldots,12\),
both signs, and \(k=1,\ldots,5\), including \(k>N\).
For powers three it independently builds (10), checks its vanishing
low coefficients against (14), compares all physical values with
the original columns, and verifies the exact Parseval normalization.
The [record](../repro/results/research-odd-primitive-scalar-recurrence.json)
contains 110 signed scalar cases and 22 polynomial cases at 120
decimal digits, with maximum error below \(6.7\cdot10^{-117}\).
The script and direct and nested project dependencies are hashed.
These finite checks supplement the identities; the proof of
(18)--(19) does not use sampled growth.
