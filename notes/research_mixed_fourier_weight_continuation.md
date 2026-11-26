# The reciprocal factorial in the exact Fourier integral

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The exact Fourier representation of a mixed three/four word contains a
polynomial whose values at the roots of unity are reciprocal quantum
factorials. A continuation of those factorials is available, but agreement
at the roots alone does not permit replacing the polynomial away from the
roots. This note proves that replacement, with exponentially small relative
error, throughout the rectangle containing the four-crossing critical
indices. The comparison retains the endpoint forcing of the polynomial.
It is an estimate for one factor, not a lower bound for the remaining
multiple integral.

## 1. The polynomial and the factorial

Fix an integer \(N\ge2\), and write
\[
 r=e^{-2\pi i/N},\qquad
 P_a=\prod_{h=1}^a(1-r^h),\qquad P_0=1.
 \tag{1}
\]
Let \(d_N\) be the unique polynomial of degree less than \(N\) with
\(d_N(r^a)=P_a^{-1}\), for \(0\le a<N\). Lagrange interpolation gives
\[
 d_N(X)=\frac{1-X^N}{N}
          \sum_{a=0}^{N-1}\frac{1}{P_a(1-Xr^{-a})}.
 \tag{2}
\]
The apparent singularities are removable. At \(X=r^a\), the corresponding
cardinal factor has limit one and all other factors vanish. Thus (2)
specifies the polynomial exactly, including its constant coefficient.

Use the sine-factorial interpolation \(G_N\) from
[the factorial construction](exact_factorial_interpolation_and_complex_contours.md).
The orientation of the root in (1) requires
\[
 \widehat P_N(v)
   =\exp\left(\frac{\pi iv}{2}
                 -\frac{\pi iv(v+1)}{2N}\right)G_N(v),
 \qquad f_N(s)=\widehat P_N(Ns)^{-1}.
 \tag{3}
\]
In particular,
\[
 \widehat P_N(a)=P_a,\qquad
 f_N(s+1/N)=\frac{f_N(s)}{1-e^{-2\pi i(s+1/N)}}.
 \tag{4}
\]
The reciprocal in (3) is holomorphic for \(-1<\Re(Ns)<N\).
This follows directly from the Gamma product for \(G_N\); in this strip
all its Gamma arguments have positive real part. Every rectangle used
below lies strictly inside that strip.

For reference, the polynomial itself obeys the forced equation
\[
 d_N(r^{-1}X)
  =(1-X)d_N(X)
     +\frac{X(1-X^N)}{N^2(1-X)}.
 \tag{5}
\]
The quotient is a polynomial. To prove (5), evaluate its difference
on the root grid. At \(X=r^a\), \(a\ne0\), (4) gives zero.
At \(X=1\), the difference is \(1/P_{N-1}=1/N\).
The top coefficient of \(d_N\) is \(1/N^2\): its Fourier formula is
\[
 [X^{N-1}]d_N=\frac1N\sum_{a<N}\frac{r^a}{P_a}=\frac1{N^2},
 \tag{6}
\]
where the last sum telescopes, or follows from the
[forced moment identity](research_mixed_conditional_leg_sum.md).
Subtracting the rightmost term of (5) therefore leaves a polynomial
of degree less than \(N\), zero at all \(N\) nodes. This proves (5).
The comparison below does not set this forcing to zero.

## 2. An exact residue formula

Put
\[
 \ell_N=-\frac1{2N},\qquad u_N=1-\frac1{2N},\qquad
 K_N(s)=\frac1{1-e^{-2\pi iNs}}.
 \tag{7}
\]
Let \(H>0\), and orient the boundary of
\(\mathcal R_{N,H}=[\ell_N,u_N]+i[-H,H]\) counterclockwise.
For \(z\) strictly inside this rectangle, with
\(X=e^{-2\pi iz}\), the residue theorem gives
\[
 d_N(X)-f_N(z)
  =(1-X^N)\int_{\partial\mathcal R_{N,H}}
       \frac{K_N(s)f_N(s)}
            {1-e^{2\pi i(s-z)}}\,ds.
 \tag{8}
\]
Initially suppose \(z\) is not one of the physical nodes. The poles at
\(s=a/N\) have residues
\[
 \frac{f_N(a/N)}
       {2\pi iN(1-Xr^{-a})}.
 \tag{9}
\]
The additional pole at \(s=z\) has residue
\(-f_N(z)/(2\pi i(1-X^N))\). There are no other poles in the
rectangle. Multiplication by \(2\pi i\) and then by \(1-X^N\)
proves (8), with its displayed sign. Both sides extend holomorphically
across the physical nodes, so (8) holds there by continuity as well.
In particular, no singular estimate of \(K_N(z)\) is needed near a node.

## 3. The two vertical sides have polynomial size

The Gamma product has a particularly useful exact modulus on the line
\(v=-1/2+it\). In each factor of the infinite product the numerator and
denominator Gamma functions are conjugates, and all powers of \(Nk\)
have modulus one. The identity
\[
 |\Gamma(1/2+it)|^2=\frac{\pi}{\cosh\pi t}
 \tag{10}
\]
therefore gives
\[
 |G_N(-1/2+it)|^2=\frac{N}{2\cosh\pi t}.
 \tag{11}
\]
Identity (10) follows from Gamma reflection; see
[DLMF, equation 5.4.4](https://dlmf.nist.gov/5.4.E4).
This use of the whole product fixes the modulus exactly.

Apply the exponential in (3) and the exact reflection
\(G_N(v)G_N(N-1-v)=N\). At the two sides of the rectangle,
\[
 \begin{split}
 |f_N(\ell_N+iy)|^2&=\frac{1+e^{2\pi Ny}}{N},\\
 |f_N(u_N+iy)|^2&=\frac1{N(1+e^{2\pi Ny})},\\
 K_N(\ell_N+iy)&=K_N(u_N+iy)=\frac1{1+e^{2\pi Ny}}.
 \end{split}
 \tag{12}
\]
Consequently \(|K_Nf_N|\le N^{-1/2}\) on both vertical sides,
including their portions above the real axis. The large values of
\(f_N\) at the upper left endpoint have already been cancelled by the
cotangent kernel; they have not been omitted.

If \(z\) ranges over a fixed compact subset with \(0<\Re z<1\),
the other denominator in (8) is bounded away from zero on the
vertical sides for all sufficiently large \(N\). Indeed its only
zeros have real part \(\Re z\) modulo one, separated from both sides.
Thus their combined contribution to the integral in (8) is
\(O_H(N^{-1/2})\), uniformly on that compact set.

## 4. The horizontal sides

Take \(H\) with \(\rho=e^{-2\pi H}<1/2\), and write
\[
                         b(H)=-\log(1-\rho).
 \tag{13}
\]
Uniformly for \(\ell_N\le x\le u_N\), we claim
\[
 \begin{split}
 |f_N(x-iH)|&\le C_H N^{-1/2}e^{Nb(H)},\\
 |K_N(x+iH)f_N(x+iH)|
                &\le C_H N^{-1/2}e^{-\pi NH}.
 \end{split}
 \tag{14}
\]
Here is a direct finite-product proof. Choose
\(j\in\{0,\ldots,N\}\) and \(0\le\theta<1\) so that
\[
 x=\ell_N+\frac{\theta+j}{N}.
 \tag{15}
\]
At the last endpoint take \(j=N,\theta=0\). Changing the real part
from \(\ell_N\) to \(\ell_N+\theta/N\), at height \(H\) or \(-H\),
changes \(|f_N|\) by a bounded factor independent of \(N,\theta\).
To justify this uniformly, apply the logarithmic derivative bound
\(\partial_s\log G_N(Ns)=O_H(N)\) on a compact neighborhood of
\(iH\) or \(-iH\), and include the explicit exponential in (3).
The differentiated convergent Gamma product proves this bound in
[the nonreal factorial estimate](research_mixed_three_conditional_complex_neighbors.md#2-a-bound-for-the-exact-factorial-away-from-its-real-divisors).
The real displacement is at most \(1/N\).

Now iterate the exact recurrence (4) \(j\) times. At height \(-H\),
each denominator has modulus at least \(1-\rho\), giving the first
line of (14) from (12). At height \(H\), each denominator has modulus
at least \(\rho^{-1}-1>1\). Thus the largest upper bound occurs at
the left endpoint and is \(C_HN^{-1/2}e^{\pi NH}\).
On this horizontal side
\[
 |K_N(s)|\le\frac1{e^{2\pi NH}-1}.
 \tag{16}
\]
This proves the second line of (14). On the lower horizontal side,
\(|K_N|\le(1-e^{-2\pi NH})^{-1}\).

Choose \(H>\sup|\Im z|\) on the compact set of interest. The remaining
denominator of (8) is then bounded away from zero on both horizontal
sides. Combining (12)--(16) yields
\[
 |d_N(e^{-2\pi iz})-f_N(z)|
 \le C_HN^{-1/2}
       \exp N\{2\pi\max(\Im z,0)+b(H)\}.
 \tag{17}
\]
All four sides of the original residue contour have been included.

## 5. A criterion for relative exponential accuracy

On \(0<\Re z<1\), let
\[
 J'(z)=\Log(2\sin\pi z),\qquad J(0)=0,\qquad
 g(z)=J(z)+\frac{i\pi}{2}(z-z^2),\qquad
 \nu(z)=-\Re g(z).
 \tag{18}
\]
The logarithm is the continuation from the positive real sine.
The previously proved uniform factorial expansion gives
\[
 f_N(z)=N^{-1/2}
    \frac{e^{i\pi z/2}}{\sqrt{2\sin\pi z}}\,
    e^{-Ng(z)}\{1+O(N^{-1})\}.
 \tag{19}
\]
The square root is the continuation of the positive real root.
Its coefficient is bounded above and away from zero on every fixed
compact set in this strip.

Even when relative approximation fails, the contour gives a useful
uniform absolute bound. For every compact \(E\) in the strip and every
\(\varepsilon>0\),
\[
 |d_N(e^{-2\pi iz})|
 \le C_{E,\varepsilon}N^{-1/2}
   \exp N\bigl(\max\{\nu(z),2\pi\max(\Im z,0)\}+\varepsilon\bigr),
       \qquad z\in E.
\]
Choose \(H>\sup_E|\Im z|\) with \(b(H)<\varepsilon\), and add the
bound (17) to (19). Thus the comparison never replaces a possibly
larger interpolation remainder by a small relative error outside
the domain specified next.

**Theorem 1.** Let \(E\) be a compact subset of \(0<\Re z<1\) such that
\[
 \eta=\inf_{z\in E}
             \{\nu(z)-2\pi\max(\Im z,0)\}>0.
 \tag{20}
\]
For every \(c<\eta\), uniformly on \(E\),
\[
 d_N(e^{-2\pi iz})=f_N(z)\{1+O(e^{-cN})\}.
 \tag{21}
\]
The assertion holds at both level parities. Every fixed derivative
of the relative error obeys the same bound after decreasing \(c\).

*Proof.* Increase \(H\) until \(H>\sup_E|\Im z|\) and
\(b(H)<\eta-c\). Divide (17) by (19). This proves (21).
Condition (20) is strict and continuous, so it persists on a small
fixed complex neighborhood of \(E\), with a slightly smaller margin.
The relative error is holomorphic there. Cauchy's estimates give
every fixed derivative, with any correspondingly smaller exponent.
\(\square\)

In particular (20) holds on every compact subset of
\(0<\Re z<1/2,\Im z\le0\). For \(z=x-iy\), \(y\ge0\), put
\(\theta=2\pi x\) and \(\rho=e^{-2\pi y}\). The dilogarithm integral
gives
\[
 g(z)=\frac{\operatorname{Li}_2(\rho e^{-i\theta})-\pi^2/6}{2\pi i},
 \qquad
 \nu(z)=\frac1{2\pi}
       \int_0^\rho\frac{\arg(1-te^{-i\theta})}{t}\,dt>0.
 \tag{22}
\]
The constant is fixed at \(z=0\), and differentiation verifies the
identity on the entire lower half of the strip. The integral used
here is the usual defining integral for the dilogarithm; see
[DLMF, equation 25.12.2](https://dlmf.nist.gov/25.12.E2).
The stated positivity follows because \(0<\theta<\pi\).

## 6. The whole four-crossing critical rectangle

The rectangle needed for the four-crossing disks is
\[
 E_4=[59/250,91/250]+i[-29/250,3/250].
 \tag{23}
\]
It contains the disk of center \(3/10-13i/250\) and radius \(8/125\).
Its small part above the real axis is also covered by Theorem 1.

**Corollary 2.** Uniformly on \(E_4\), and at both level parities,
\[
 d_N(e^{-2\pi iz})=f_N(z)\{1+O(e^{-N/200})\}.
 \tag{24}
\]
Every fixed derivative of the relative error is \(O(e^{-N/300})\).

*Proof.* For \(0<t\le1\) and \(0<\theta<\pi\),
\[
 \arg(1-te^{-i\theta})
 \ge \sin\arg(1-te^{-i\theta})
 =\frac{t\sin\theta}{|1-te^{-i\theta}|}
 \ge\frac{t\sin\theta}{1+t}.
 \tag{25}
\]
Thus (22) implies
\[
 \nu(x-iy)\ge
       \frac{\sin(2\pi x)}{2\pi}\log(1+e^{-2\pi y}).
 \tag{26}
\]
On the real interval in (23), \(\sin(2\pi x)>3/4\).
For \(0\le y\le29/250\),
\[
 e^{-2\pi y}>12/25,\qquad
 \log(37/25)>39/100,
 \qquad \nu(x-iy)>\frac{117}{800\pi}>\frac1{100}.
 \tag{27}
\]
This treats the lower part of the rectangle.

For \(0\le y\le3/250\), Schwarz reflection for \(J\) gives exactly
\[
 \nu(x+iy)=\nu(x-iy)+\pi y(1-2x).
 \tag{28}
\]
In this smaller range \(e^{-2\pi y}>23/25\) and
\(\log(48/25)>13/20\). Applying (26) and then (28) gives
\[
 \begin{split}
 \nu(x+iy)-2\pi y
   &=\nu(x-iy)-\pi y(1+2x)\\
   &>\frac{39}{160\pi}-\frac{324\pi}{15625}
    >\frac1{100}.
 \end{split}
 \tag{29}
\]
The focused checker verifies all the strict scalar inequalities.
They are uniform bounds, not evaluations at selected critical points.

For \(H=1\), \(b(1)<1/500\). Equations (17), (19), (27) and
(29) therefore leave a margin greater than \(1/100-1/500=1/125\),
which proves (24). Strictness supplies a slightly larger neighborhood;
Cauchy's estimates give the stated derivative bound. \(\square\)

This corollary justifies the factorial symbol for the exact Fourier
weight at every possible four-crossing critical index in the specified
disk. It does not discard the extra Fourier modes of the full cyclic
integral, control that integral away from its critical point, or prove
the nonvanishing of its closing coefficient.

## 7. Reproduction

Run the focused script
\(\texttt{python3 experiments/check_mixed_fourier_weight_continuation.py}\).
It checks the exact interpolation and forcing at both parities, the
phase and midpoint identities, and the outward scalar margins in
(27)--(29). Separate finite Barnes-product comparisons check the signs
and normalization of (12) and (24). Those finite comparisons are
diagnostics; the uniform estimate is the residue argument above.
