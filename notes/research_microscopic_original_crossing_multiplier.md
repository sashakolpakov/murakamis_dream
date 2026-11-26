# The original crossing multiplier on the full microscopic boundary

Private written proof, 23 November 2026.

The canonical polynomial of each signed original crossing has an entire
microscopic limit, with error \(O(N^{-1})\) and every fixed holomorphic
derivative. Both Newton endpoints and an oscillating bulk term survive.
The limit retains the true first spectral normal at every fixed physical
index. Its crossed Frobenius kernel also converges explicitly.

Canonical reduction remains essential: the two limiting multipliers are
inverse only modulo the limiting physical polynomial. An explicit nonzero
carry survives. These local results do not justify composing an arbitrary
short component by pointwise multiplication or limiting kernel integrals.

## 1. Original signed crossings and the limiting functions

Put \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and

\[
 \kappa=e^{\pi i d^2/(2N)},\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 s_m=2\sin(\pi m/N),\quad S_m=\prod_{r=1}^m s_r,\quad S_0=1,
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 e_m(z)=S_m^{-2}\prod_{j<m}(c_j-z),\qquad
 w_N(\alpha)=2\cosh(\alpha/N).
 \tag{1}
\]
Here \(T_N\) is the ordinary Chebyshev polynomial. All canonical
representatives have degree at most \(d\). The full repeated-root algebra
is \(\mathbb C[z]/P_N\), with its original functional
\(\phi_N(e_i e_j)=\delta_{i+j,d}\) and genuine turn
\(\mathsf T e_i=e_{d-i}\).

For \(\sigma\in\{+1,-1\}\), let \(R_N^\sigma(z)\) be the canonical
polynomial of the original signed crossing, including its Cartan scalar.
The exact full-Hermite alphabet [N] gives

\[
 r_{N,\sigma}(z):=\kappa^{-\sigma}R_N^\sigma(z)
       =\sum_{i=0}^{d}(-q)^{\sigma i}e_i(z),\qquad
 r_{N,+}r_{N,-}\equiv1\pmod {P_N}.
 \tag{2}
\]
Define \(E_{i,N}(\alpha)=(-1)^i e_i(w_N(\alpha))\). Then exactly

\[
 r_{N,\sigma}(w_N(\alpha))
                   =\sum_{i=0}^{N-1}q^{\sigma i}E_{i,N}(\alpha).
 \tag{3}
\]
Use the entire endpoint functions of [K]:

\[
 a=\tfrac12+\frac{i\alpha}{2\pi},\quad b=1-a,\quad
 c(\alpha)=\cosh(\alpha/2),\quad C(\alpha)=c(\alpha)/\pi,
\]
\[
 \mathsf E_m(\alpha)=\frac{(a)_m(b)_m}{(m!)^2},\qquad
 \mathsf H_m(\alpha)=\frac{c(\alpha)^2}
                              {\pi^2m^2\mathsf E_m(\alpha)}
 \quad(m\ge1),\qquad \mathsf E_0=1.
 \tag{4}
\]
The second expression means its entire continuation: every zero of
\(\mathsf E_m\) is simple and is a double zero of its numerator.

**Theorem 1.** The series and functions

\[
 D(\alpha)=1+\sum_{m\ge1}
                 [\mathsf E_m(\alpha)-\mathsf H_m(\alpha)],\qquad
 F_\sigma(\alpha)=D(\alpha)+\sigma i c(\alpha)
 \tag{5}
\]
are entire and even. For every fixed \(A<\infty\) and integer \(k\ge0\),

\[
 \sup_{|\alpha|\le A}
 \left|\partial_\alpha^k
       [r_{N,\sigma}(w_N(\alpha))-F_\sigma(\alpha)]\right|
                  \le C_{A,k}/N.
 \tag{6}
\]
The limit is through both parities. On the real axis \(D\) is real and

\[
 |F_\sigma(\alpha)|^2=D(\alpha)^2+c(\alpha)^2
                              \ge c(\alpha)^2\ge1.
 \tag{7}
\]
In particular the original microscopic crossing is uniformly nonzero
on each bounded real parameter interval for all sufficiently large \(N\).
The known unit scalar \(\kappa^\sigma\) has not been discarded from the
original crossing; (6) states its normalization explicitly.

## 2. A common bulk unit for the two Newton ends

Write \(\operatorname{sinc}z=\sin z/z\) and
\(\operatorname{sinhc}z=\sinh z/z\), with removable values one.
The exact product and complementary identities [K] are

\[
 E_{m,N}=\mathsf E_m U_{m,N},\qquad
 U_{m,N}=\prod_{r=0}^{m-1}
 \frac{\operatorname{sinhc}((\alpha+i(2r+1)\pi)/(2N))
       \operatorname{sinhc}((\alpha-i(2r+1)\pi)/(2N))}
      {\operatorname{sinc}(\pi(r+1)/N)^2},
\]
\[
 E_{N-m,N}=\mathsf H_m
            \operatorname{sinc}(\pi m/N)^{-2}U_{m,N}^{-1}.
 \tag{8}
\]
They hold through all apparent zeros. For \(1\le m\le N/2\), all
displayed unit factors are nonzero on a fixed bounded \(\alpha\)-disk
once \(N\) is sufficiently large. We prove the stronger comparison

\[
 V_{m,N}:=U_{m,N}\operatorname{sinc}(\pi m/N),\qquad
             V_{m,N}^{\ \pm1}=1+O_A(m/N^2).
 \tag{9}
\]

Set \(\Delta=\pi/N\) and \(f(v)=\log\operatorname{sinc}v\) on
a fixed neighborhood of \([0,\pi/2]\). At zero parameter,

\[
 \log U_{m,N}(0)+f(m\Delta)
 =\sum_{r=1}^m
 [2f((r-\tfrac12)\Delta)-f((r-1)\Delta)-f(r\Delta)]
                         =O(m/N^2).
 \tag{10}
\]
This is a telescoping identity followed by the bounded second derivative
of \(f\). For the parameter dependence let
\(g(z)=\log\operatorname{sinhc}z\), \(g(0)=0\), on a zero-free
neighborhood of the imaginary segment from \(-i\pi/2\) to \(i\pi/2\).
With \(v=(r+1/2)\Delta\), evenness of \(g\) gives

\[
 g(\alpha/(2N)+iv)+g(\alpha/(2N)-iv)-2g(iv)
                                                    =O_A(N^{-2}).
 \tag{11}
\]
Its first derivative in \(\alpha/(2N)\) vanishes at zero; its second
derivative is uniformly bounded. Summing (11) and using (10) bounds
\(\log V_{m,N}\) by \(C_A m/N^2\). Exponentiating both signs proves
(9). No logarithm of \(\mathsf E_m\) was taken.

## 3. Summation with the oscillating bulk retained

Uniformly on compact parameter disks, as \(m\to\infty\),

\[
 \mathsf E_m=\frac C m
       (1-ab/m+O_A(m^{-2})),\qquad
 \mathsf H_m=\frac C m
       (1+ab/m+O_A(m^{-2})).
 \tag{12}
\]
Here is also a direct way to check the opposite first corrections.
The Gamma product gives
\(\mathsf E_m=C\Gamma(m+a)\Gamma(m+b)/\Gamma(m+1)^2\),
using \(1/(\Gamma(a)\Gamma(b))=\sin(\pi a)/\pi=C\).
The normalized ratio \(u_m=m\Gamma(m+a)\Gamma(m+b)/\Gamma(m+1)^2\)
(equivalently \(m\mathsf E_m/C\), by removable continuation) tends to one and obeys
\(u_{m+1}/u_m=1+ab/[m(m+1)]\). The normalization follows, for example,
by scaling the beta integral for Gamma ratios and then shifting its
parameters; it is uniform on fixed compact sets. For sufficiently large
\(m\), take logarithms of its tail product:
\(\log u_m=-\sum_{j\ge m}\log(1+ab/[j(j+1)])
=-ab/m+O_A(m^{-3})\).
This proves the first expansion; the exact identity
\(\mathsf H_m=C^2/(m^2\mathsf E_m)\) proves the second.
The Gamma expressions extend through the finitely many exceptional
parameter values, so the estimates are uniform there as well. Thus

\[
 \mathsf E_m-\mathsf H_m=O_A(m^{-2}),\qquad
 \mathsf E_m+\mathsf H_m=2C/m+O_A(m^{-3}).
 \tag{13}
\]
The first bound proves normal convergence and entire evenness in (5).

For the positive sign, pair indices \(m,N-m\) in (3). Set
\(\tau_m=\pi m/N\) and \(M=\lfloor(N-1)/2\rfloor\). By (8)--(9),
their exact sum is

\[
 \tau_m\cot\tau_m
       (\mathsf E_m V_{m,N}-\mathsf H_m V_{m,N}^{-1})
 +i\tau_m(\mathsf E_m V_{m,N}
                              +\mathsf H_m V_{m,N}^{-1}).
 \tag{14}
\]
Replacing both \(V\)'s by one costs \(O_A(N^{-2})\) per pair,
since \(\mathsf E_m,\mathsf H_m=O_A(1/m)\), and the two displayed
weights are bounded. The real-weight error also costs \(O_A(N^{-2})\)
per pair, because
\(|\tau\cot\tau-1|\le C\tau^2\) for \(0\le\tau\le\pi/2\)
and the difference in (13) is \(O_A(m^{-2})\).
Its omitted infinite tail is \(O_A(1/N)\).

The imaginary part of (14), after this replacement, sums to
\(i\sum_{m=1}^M[2\pi C/N+O_A(1/(Nm^2))]
=ic+O_A(N^{-1})\).
The index zero contributes one. At even \(N\) the additional midpoint
is \(iE_{N/2,N}=O_A(N^{-1})\), by (8)--(9) and (12); at odd \(N\)
there is no unpaired index. This proves (6) for the positive sign and
zero derivatives. The negative sign reverses the imaginary part in
(14) with no other change. Applying the result on a larger parameter
disk and Cauchy's formula proves every derivative in (6).
The endpoint functions are real for real parameters, proving (7).

## 4. The original physical first normals

For a fixed integer \(j\ge0\), put \(\alpha_j=i\pi(2j+1)\) and
\(\nu_j=(-1)^j q^{j(j+1)}\). At all sufficiently large levels this
is a double physical node. The actual crossing data [W, equation (8)]
give exactly

\[
 r_{N,\sigma}(w_N(\alpha_j))=\nu_j^\sigma,\qquad
 \left.\partial_\alpha r_{N,\sigma}(w_N(\alpha))
                 \right|_{\alpha_j}
          =-\sigma\frac{d-2j}{2N}\nu_j^\sigma.
 \tag{15}
\]
Consequently (6) retains, with their original sign,

\[
 F_\sigma(\alpha_j)=(-1)^j,\qquad
 F_\sigma'(\alpha_j)=-\frac\sigma2(-1)^j,\qquad
 D(\alpha_j)=(-1)^j,\quad D'(\alpha_j)=0,
\]
\[
 \frac{r_{N,\sigma}'(c_j)}{N^2}
      =\frac{\sigma i(-1)^j}{4\pi(2j+1)}+O_j(N^{-1}).
 \tag{16}
\]
The last derivative is the ordinary fixed-root Casimir derivative;
it follows from \(w_N'(\alpha_j)=2i\sin((2j+1)\pi/N)/N\).
It is not a genuine-\(q\) normal or a changed-meridian derivative.
The estimates concern fixed \(j\), not indices proportional to \(N\).

## 5. The surviving inverse-pair carry

The exact inverse identity (2) defines an ordinary polynomial

\[
 Q_N(z)=\frac{r_{N,+}(z)r_{N,-}(z)-1}{P_N(z)}.
 \tag{17}
\]
Since \(P_N(w_N(\alpha))=4c(\alpha)^2=:P(\alpha)\) exactly,
Theorem 1 implies

\[
 Q_N(w_N(\alpha))\longrightarrow
 Q_\infty(\alpha)=\frac{D(\alpha)^2+c(\alpha)^2-1}
                                      {4c(\alpha)^2},
 \tag{18}
\]
with \(O_A(N^{-1})\) error and every fixed holomorphic derivative.
The quotient is entire and even: (16) makes its numerator vanish to
order at least two at every zero of \(c\). For the convergence through
those zeros, choose a larger circle avoiding them. Division on that
circle gives the \(O(N^{-1})\) bound, the maximum principle carries it
inside, and Cauchy's formula gives the derivatives.
For real \(\alpha\ne0\), (18) is strictly positive, because \(D\) is
real and \(c^2-1>0\). Thus the carry is not zero.

In particular \(F_+F_-\ne1\) as ordinary functions, whereas their
classes modulo \(P\) are inverse. Pointwise multiplication of limiting
crossing values would miss this explicit order-one source correction.

## 6. The actual crossed Frobenius kernel

Put \(\eta=(-1)^d\). The original reverse Newton kernel satisfies

\[
 B_N(z,w)=\sum_{i=0}^d e_i(z)e_{d-i}(w)
       =\frac\eta{N^2}\frac{P_N(z)-P_N(w)}{z-w}.
 \tag{19}
\]
For completeness, use \(z e_i=c_i e_i-s_{i+1}^2 e_{i+1}\) for
\(i<d\), the top identity \((z-c_d)e_d=\eta P_N/N^2\), and
\(c_{d-i}=c_i\), \(s_{N-i}=s_i\). All interior terms in
\((z-w)B_N\) telescope. The original Frobenius identity in section 1
also gives \(\phi_{N,z}[B_N(z,w)f(z)]=f(w)\) for canonical \(f\).

For \(r=r_{N,\sigma}\), its canonical multiplication kernel is

\[
 C_{r,N}(z,w)=\operatorname{can}_z[r(z)B_N(z,w)]
 =\frac\eta{N^2}
       \frac{P_N(z)r(w)-P_N(w)r(z)}{z-w}.
 \tag{20}
\]
The expression is canonical in both variables. Subtracting it from
\(r(z)B_N\) leaves a multiple of \(P_N(z)\), which proves (20), and
\(\phi_{N,z}[C_{r,N}(z,w)f(z)]
=\operatorname{can}(rf)(w)\).
Its full microscopic limit is

\[
 \eta C_{r_{N,\sigma},N}(w_N(\alpha),w_N(\beta))
 \longrightarrow
 \frac{P(\alpha)F_\sigma(\beta)-P(\beta)F_\sigma(\alpha)}
                                      {\alpha^2-\beta^2}.
 \tag{21}
\]
The error is \(O_A(N^{-1})\), including every fixed mixed holomorphic
derivative on bounded bidisks. Indeed
\(N^2(w_N(\alpha)-w_N(\beta))/(\alpha^2-\beta^2)
=\operatorname{sinhc}((\alpha+\beta)/(2N))
 \operatorname{sinhc}((\alpha-\beta)/(2N))=1+O_A(N^{-2})\).
Every numerator is even in each variable and antisymmetric under their
exchange, so division by \(\alpha^2-\beta^2\) is removable. Buffered
Cauchy estimates preserve the error in (6): write each even function
as an entire function of \(u=\alpha^2\), and use its divided difference
at \(u,v=\beta^2\). This is the integral of its first derivative on the
segment from \(u\) to \(v\); a larger disk controls that derivative.
Another buffered Cauchy estimate gives all mixed derivatives.

These are original atomic multiplication and inverse-pair gluing data.
No estimate for iterated canonical reductions, whole-kernel contractions,
escaping Newton mass, or the original closing after an arbitrary fixed
short component follows. Such estimates are required before interchanging
this limit with arbitrary Conway compositions or turns.

## Complete sources and coverage

The entire matching texts were read; [K], [N], and [W] are proof inputs.
[G] concerns a different coherent boundary source with an affine Gamma
extension, not this microscopic crossing multiplier. [T] already shows
why a local germ estimate does not control the complementary source after
a genuine turn. No novelty is claimed for those cautions.

| Label | Complete text | SHA-256 |
|---|---|---|
| K | [Two-ended kernel, 331 lines](research_two_ended_wilson_source_kernel.md) | 625bdb6f767c1676b5377eae92a47edd1e87f19db31febef27cf259270b1f7e9 |
| N | [Original Newton turn, 434 lines](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| W | [Signed Gaussian first normals, 503 lines](research_signed_gaussian_ward_endpoint_packet.md) | 6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191 |
| G | [Exact coherent Gamma extension, 632 lines](research_crossing_exact_gamma_source_extension.md) | f19221b384ae9c2de47beee8460df4eee30f3419df6cf0478c18569b3f464495 |
| T | [Germ and turn remainder, 185 lines](research_source_germ_truncation_and_turn_remainders.md) | ed1390c5c2e2bf3dddd29f5b161c4cbfcec9ba4e9c7a22ab0d446ea40d14330b |

Only written mathematics and source-text/hash operations were used.
No mathematical program, numerical experiment, test, build, git operation,
or earlier-final edit was performed. No knot-volume, whole-short-component,
or finite-exception theorem is asserted.
