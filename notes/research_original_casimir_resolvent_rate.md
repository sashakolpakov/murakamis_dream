# The exponential resolvent rate of the original Casimir

Research deduction, 8 November 2026. No numerical evaluation is used.

The original Casimir matrix has only real eigenvalues. Nevertheless,
its inverse at a fixed nonreal parameter can grow exponentially with
the quantum level. The rate can be computed directly from its
bidiagonal entries. This gives approximate eigenvectors at every
nonreal point in a specified disk, independently of a knot source.

The distinction matters for the proposed use of almost-invariant
vectors. An approximate Casimir eigenvector does not by itself select
the quantum state supplied by a crossing word or its closing
coefficient. The calculation below describes the actual operator,
with all its original coordinates retained.

## 1. The operator and its exact inverse

Let \(N\ge2\), \(D=N-1\), and use the normalized Newton coordinates
of the original tangle algebra. Multiplication by the Casimir is
the lower bidiagonal matrix
\[
 (C_N v)_j=c_{j,N}v_j-s_{j,N}^{\,2}v_{j-1},\qquad
 c_{j,N}=2\cos\frac{(2j+1)\pi}{N},\qquad
 s_{j,N}=2\sin\frac{\pi j}{N},\qquad v_{-1}=0.
 \tag{1}
\]
This is equation (3) of
[the original Casimir insertion theorem](research_even_reflected_casimir_insertions.md).
In particular its final row is part of the original quotient
algebra; it is not an added boundary condition.

Fix \(z\in\mathbb C\setminus\mathbb R\), independently of \(N\).
All diagonal entries of \(C_N-zI\) are nonzero. Put
\(G_N(z)=(C_N-zI)^{-1}\). Solving its triangular equations gives
\[
 (G_N(z))_{ji}=
 \begin{cases}
 \displaystyle
 \frac{\prod_{\nu=i+1}^{j}s_{\nu,N}^{\,2}}
      {\prod_{\nu=i}^{j}(c_{\nu,N}-z)},&j\ge i,\\[6pt]
 0,&j<i.
 \end{cases}
 \tag{2}
\]
The empty numerator product for \(j=i\) equals one. Indeed the
\(i\)-th column has value \((c_{i,N}-z)^{-1}\) in row \(i\), and
each subsequent row is multiplied by
\(s_{j,N}^{\,2}/(c_{j,N}-z)\). This proves both the sign and
normalization in (2).

Define the real integrable function
\[
 f_z(x)=\log\frac{2-2\cos(2\pi x)}
                         {|2\cos(2\pi x)-z|},\qquad 0<x<1,
 \tag{3}
\]
and
\[
 I(z)=\max_{0\le a\le b\le1}\int_a^b f_z(x)\,dx.
 \tag{4}
\]
The integral is continuous in its two endpoints despite the
logarithmic singularities at zero and one. The maximum exists,
and \(I(z)\ge0\) because \(a=b\) is permitted.

## 2. A sharp rate, uniform over all matrix entries

**Theorem 1.** At every fixed nonreal \(z\),
\[
 \lim_{N\to\infty}\frac1N\log\|G_N(z)\|_2=I(z),\qquad
 \lim_{N\to\infty}\frac1N
       \log s_{\min}(C_N-zI)=-I(z).
 \tag{5}
\]
Here \(\|\cdot\|_2\) is the Euclidean operator norm and
\(s_{\min}\) is the smallest singular value. Both limits use all
integer levels.

*Proof.* Write
\[
 J(t)=\int_0^t\log(2\sin\pi x)\,dx.
 \tag{6}
\]
Uniformly for \(0\le m\le D\), the elementary sine-product estimate
is
\[
 \log\prod_{\nu=1}^{m}2\sin(\pi\nu/N)
                 =NJ(m/N)+O(\log N).
 \tag{7}
\]
For completeness, split
\[
 \log(2\sin\pi x)=\log x+\log(1-x)
           +\log\frac{2\sin\pi x}{x(1-x)}.
\]
The last summand extends smoothly to the closed interval. Its
Riemann sums have bounded error. Integral comparison for the two
monotone logarithms gives an \(O(\log N)\) error uniformly at
every partial sum, including the two ends. This proves (7).

The function \(x\mapsto\log|2\cos(2\pi x)-z|\) is smooth on
\([0,1]\), since its argument has modulus at least
\(|\operatorname{Im}z|>0\). Replacing \(c_{\nu,N}\) by
\(2\cos(2\pi\nu/N)\) changes its sum by \(O_z(1)\), and its
Riemann-sum error is also \(O_z(1)\), uniformly over partial
intervals. Equation (2) consequently yields
\[
 \log|(G_N(z))_{ji}|
       =N\int_{i/N}^{j/N}f_z(x)\,dx+O_z(\log N),
                   \qquad 0\le i\le j\le D.
 \tag{8}
\]
The extra denominator in row \(i\) is bounded above and below
by constants depending only on \(z\), and is absorbed in this
error. Thus (8) includes the diagonal entries.

For any \(N\times N\) matrix,
\[
 \max_{i,j}|G_{ji}|\le\|G\|_2
                  \le N\max_{i,j}|G_{ji}|.
 \tag{9}
\]
The maximum of the integrals in (8) over the grid converges to
(4), by continuity of the integral in both endpoints and density
of the grids. Equations (8)--(9) prove the first limit in (5).
Invertibility gives \(s_{\min}(C_N-zI)=\|G_N(z)\|_2^{-1}\),
which proves the second. \(\square\)

## 3. The disk where exponential amplification occurs

The interval maximization in (4) can be evaluated without locating
any matrix eigenvectors.

**Theorem 2.** If \(|z+2|\ge4\), then \(I(z)=0\). If
\(|z+2|<4\), put
\[
 c_z=\frac{4-|z|^2}{2(2-\operatorname{Re}z)},\qquad
 x_z=\frac1{2\pi}\arccos(c_z/2).
 \tag{10}
\]
Then \(-2<c_z<2\), \(0<x_z<1/2\), and
\[
 I(z)=\int_{x_z}^{\,1-x_z}
        \log\frac{2-2\cos(2\pi x)}
                         {|2\cos(2\pi x)-z|}\,dx>0.
 \tag{11}
\]

*Proof.* For \(c=2\cos(2\pi x)\), the sign of \(f_z(x)\) is
the sign of
\[
 (2-c)^2-|c-z|^2
                  =4-|z|^2+2c(\operatorname{Re}z-2).
 \tag{12}
\]
If \(\operatorname{Re}z\ge2\), the maximum of the right side
over \(-2\le c\le2\) occurs at \(c=2\) and equals
\(-|z-2|^2<0\). If \(\operatorname{Re}z<2\), its maximum occurs
at \(c=-2\) and equals \(16-|z+2|^2\).
Thus outside or on the stated disk \(f_z\le0\), so (4) is zero.

Inside the disk, \(\operatorname{Re}z<2\). Equation (12) is
positive precisely when \(c<c_z\). The two strict bounds on
\(c_z\) follow respectively from
\(|z+2|^2<16\) and \(|z-2|^2>0\). The positive set of \(f_z\)
is therefore the single interval \((x_z,1-x_z)\). Including
any interval outside that set decreases the integral; omitting
any part of it also decreases the integral. This proves (11).
\(\square\)

There is an explicit approximate eigenvector attaining the rate.
For a point inside the disk choose \(i_N=\lfloor Nx_z\rfloor\)
and set
\[
 v_N(z)=\frac{G_N(z)\mathbf e_{i_N}}
                    {\|G_N(z)\mathbf e_{i_N}\|_2}.
 \tag{13}
\]
The entry in row \(\lfloor N(1-x_z)\rfloor\), which belongs to
\(\{0,\ldots,D\}\) for large \(N\), and (8) show that the
denominator has rate \(I(z)\). The operator upper bound (5)
gives the matching upper rate. Hence
\[
 \|v_N(z)\|_2=1,\qquad
 \|(C_N-zI)v_N(z)\|_2=e^{-NI(z)+o(N)}.
 \tag{14}
\]
For large \(N\), \(i_N>0\); lower triangularity in (2) then
also gives \(\mathbf e_0^\dagger v_N(z)=0\) exactly.
These are vectors for the actual Casimir, but they are constructed
from a resolvent column. They are not asserted to be the state of
any specified knot or tangle.

## 4. The location selected by the actual reflected source

The actual reflected crossing column
\(\alpha_N=M_N^{2k}\mathbf e_0\), for fixed \(k\ge2\), has
its norm concentrated near index \(j/N=1-x_k\).
Here \(x_k=\theta_k/(2\pi)\in(0,1/4)\), and the
[sharp growth theorem](research_even_run_sharp_reflected_growth.md)
gives
\[
 |\lambda_*(\theta_k)|=2-2\cos\theta_k.
 \tag{15}
\]
Its original geometric Casimir value, with the prescribed
conjugation, is
\[
 z_k=2\cos\theta_k-\lambda_*(\theta_k)
      =-2\cos(\varphi_k-i\eta_k),
 \qquad \eta_k>0,\quad0<\varphi_k<\pi.
 \tag{16}
\]
See equations (17)--(18) of
[the Casimir insertion theorem](research_even_reflected_casimir_insertions.md).
In particular \(z_k\) is nonreal.

Let \(c=2\cos\theta_k\in(0,2)\). Equations (15)--(16) give
\[
                         |c-z_k|=2-c.
 \tag{17}
\]
The triangle inequality yields \(|z_k+2|\le4\); equality would
force \(z_k\) to be real, so the inequality is strict. By the
unique zero in (12), equation (17) says \(c=c_{z_k}\).
Consequently,
\[
                              x_{z_k}=x_k.
 \tag{18}
\]
Thus the geometric value determines the macroscopic location
of the actual source maximum through this elementary operator
relation. The
[growing-observation theorem](research_original_growing_cap_observation.md)
describes which endpoint projections reach that location.

Equation (18) does not determine the coefficient of the actual
source along a closing observation. The resolvent rate \(I(z_k)\)
and the actual crossing-column rate
\(\operatorname{Vol}(S^3\setminus\mathcal K_k)/(4\pi)\) are
different quantities; no equality between them is inferred.
In particular an arbitrarily small Casimir residual, even an
exponentially small one as in (14), supplies no lower bound for
the first-cap observation. A composition theorem still needs
the original source and its specified closing functional.
