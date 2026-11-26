# Complex color in the finite-branch twist formula

Private written proof, 14 November 2026. The manuscripts remain frozen.

The finite-branch reciprocity formula for a full twist was proved on
integer colors. Its bounded sawtooth integrals cannot simply be
continued by replacing that integer with a complex variable. The missing
factor is a character of the interval index. Here we retain that
character, specify the translated integration segments and their order
of summation, and prove that every resulting branch is entire.

There is also a finite formula for each branch. It uses a grid with
\(2|p|N\) points and the two original endpoint values with half weights.
This formula proves compatibility with differentiation and prescribed
finite exterior contractions. It does not select a geometric saddle
or supply an exponential bound at its complex color.

## 1. The specified entire coefficient

Fix \(N\ge2\), \(p\in\mathbb Z\setminus\{0\}\), and put
\[
 h=|p|,\qquad q=e^{\pi i/N},\qquad
 \kappa=q^{(N-1)^2/2},\qquad t_k=(k+\tfrac12)/N .
 \tag{1}
\]
All fractional powers use the displayed exponential. Let \(\zeta\)
be a complex color variable, independent of \(q\). Define
\[
 \begin{split}
 g_\zeta(t)
  &=[1-\zeta/N+2p(t-\tfrac12)]\\
  &\hspace{12mm}\cdot
      \exp\{2\pi ipN(t-\tfrac12)^2-2\pi i\zeta t\},\\
 a_N(\zeta)&=\frac{\kappa^{-p}}N
                         \sum_{k=0}^{N-1}g_\zeta(t_k).
 \end{split}
 \tag{2}
\]
This is the original entire coefficient interpolation in the coherent
Gaussian source formula. At integers \(0\le n<N\), it equals the
canonical coefficient \(a_n\) in
\[
 r_N(z)^{2p}\bmod P_N(z)
       =a_0+\sum_{n=1}^{N-1}a_n\,2T_n(z/2).
 \tag{3}
\]
The physical operator is \(R^{2p}=\kappa^{2p}r_N(\Omega)^{2p}\).
The normal derivative of the crossing contributes the linear factor
\(2p(t-\tfrac12)\) in (2). Thus (2) includes the repeated-root data.

Set
\[
 A_\ell(\zeta)=\int_0^1g_\zeta(t)e^{-2\pi iN\ell t}\,dt
                  \qquad(\ell\in\mathbb Z).
 \tag{4}
\]
Each integral is entire in \(\zeta\). The original midpoint Fourier
identity is
\[
 a_N(\zeta)=\kappa^{-p}
       \sum_{\ell\in\mathbb Z}^{\rm sym}(-1)^\ell A_\ell(\zeta).
 \tag{5}
\]
The symmetric prescription in (5) is part of the identity.

## 2. A finite formula for every residue branch

For \(0\le r<2h\), define the paired branch
\[
 Z_r(\zeta)=\lim_{M\to\infty}
                \sum_{m=-M}^{M}A_{r+2pm}(\zeta).
 \tag{6}
\]
Negative \(p\) merely reverses the order of a symmetric sum.

**Theorem 1.** Every branch (6) is entire. With \(L=2hN\), it has
the exact finite expression
\[
 \boxed{
 Z_r(\zeta)=\frac1L\left\{
       \frac{g_\zeta(0)+g_\zeta(1)}2+
       \sum_{j=1}^{L-1}
          g_\zeta(j/L)e^{-2\pi iNrj/L}
                    \right\}.}
 \tag{7}
\]
The original coefficient is
\[
                  a_N(\zeta)=\kappa^{-p}
                          \sum_{r=0}^{2h-1}(-1)^rZ_r(\zeta).
 \tag{8}
\]
The series (6) and all its fixed \(\zeta\)-derivatives converge
locally uniformly.

**Proof.** Periodically extend
\(g_\zeta(t)e^{-2\pi iNr t}\) from \([0,1]\). It is smooth on the
open interval, with finite one-sided limits at its endpoints.
Its symmetric Fourier series converges to its value at each interior
point and to the average of its endpoint limits at the identified
point \(0=1\). Averaging these Fourier series over the grid
\(j/L\), \(0\le j<L\), keeps precisely the Fourier modes divisible
by \(L\). Those Fourier coefficients are the integrals
\(A_{r+2pm}\), since \(2pN\mathbb Z=L\mathbb Z\).
The surviving endpoint value is the half sum in (7); its extra factor
at \(t=1\) is \(e^{-2\pi iNr}=1\). This proves (7) with the
symmetric summation prescription.

One can also verify convergence directly. Two integrations by parts
in (4), using only the Fourier exponential for the integration, give
for \(\ell\ne0\)
\[
 A_\ell(\zeta)=
       \frac{g_\zeta(0)-g_\zeta(1)}{2\pi iN\ell}
          +O_{N,p,K}(|\ell|^{-2})
 \tag{9}
\]
uniformly for \(\zeta\) in any compact set \(K\). The same expansion
holds after any fixed number of \(\zeta\)-derivatives.
In the pair \(\ell=r+2pm,r-2pm\), the sum of reciprocal denominators
is \(O_p(m^{-2})\). Hence the paired tails and all fixed derivatives
are absolutely summable, uniformly on \(K\). The limit is entire.
A possible \(\ell=0\) is a single middle term, defined by (4).

Finally sum (7) with weights \((-1)^r\). The endpoint terms cancel,
because \(\sum_{r=0}^{2h-1}(-1)^r=0\). On the interior grid the
finite geometric sum is
\[
 \sum_{r=0}^{2h-1}(-1)^r e^{-2\pi irj/(2h)}
    =\begin{cases}2h,&j\equiv h\pmod{2h},\\0,&\text{otherwise}.
      \end{cases}
 \tag{10}
\]
The surviving points are precisely \(j/L=t_k\). This proves
(8) directly from (2), including its normalization. \(\square\)

The half endpoint values in (7) are necessary for an individual
branch. Their cancellation in the full sum is an exact Fourier
calculation, not an estimate of separately discarded endpoint terms.

## 3. The continued Fresnel formula and its compulsory character

Retain the branch parameters
\[
 b_r=\zeta+Nr,\qquad
 B_r=\frac12-\frac{b_r}{2pN},\qquad
 C_r=(-1)^r\exp\left(-\pi ib_r-\frac{\pi ib_r^2}{2pN}\right).
 \tag{11}
\]
For a real noninteger argument let \(s(u)=\tfrac12-\{u\}\).
The value at its integer jumps is immaterial.
For each integer \(m\), integrate along the horizontal segment
\[
                       v\in[B_r-1-m,B_r-m]
 \tag{12}
\]
from left to right. On that segment \(B_r-v\) is real; its fractional
part and hence \(s(B_r-v)\) are well-defined.

**Theorem 2.** For every \(\zeta\in\mathbb C\),
\[
 \boxed{
 \begin{split}
 (-1)^r Z_r(\zeta)=C_r\lim_{M\to\infty}
    \sum_{m=-M}^{M} e^{-2\pi i\zeta m}
     \int_{B_r-1-m}^{B_r-m}
       &[1-\zeta/N+2p\,s(B_r-v)]\\
       &\cdot e^{2\pi ipNv^2}\,dv .
 \end{split}}
 \tag{13}
\]
This paired segment limit is locally uniform in \(\zeta\) and
represents the entire branch in (7).

**Proof.** In the integral (4) with \(\ell=r+2pm\), set
\[
                  v=t-\frac12-\frac{\zeta+N\ell}{2pN}.
 \tag{14}
\]
This gives the segment (12). Completing the square gives the scalar
\(\exp(-\pi i(\zeta+N\ell)
-\pi i(\zeta+N\ell)^2/(2pN))\).
Its ratio to the corresponding scalar at \(\ell=r\) is
\[
 \exp\{-2\pi i\zeta m-2\pi iNr m
                  -2\pi ipN(m+m^2)\}=e^{-2\pi i\zeta m}.
 \tag{15}
\]
Here the last two terms are integral multiples of \(2\pi i\).
The factor \((-1)^\ell=(-1)^r\) is unchanged.

For an interior point of the segment, write \(B_r-v=m+u\)
with \(0<u<1\). Equation (14) gives \(t=1-u\), so
\[
                       2p(t-\tfrac12)=2p\,s(B_r-v).
 \tag{16}
\]
Thus every segment integral with its character and scalar in (13)
is exactly \((-1)^r A_{r+2pm}(\zeta)\).
The finite partial sums are equal before taking any limit.
The locally uniform convergence of (6), including its derivatives,
therefore proves (13). \(\square\)

At integer color the character in (15) is one, the segments lie
on the real axis, and (13) reduces to the real sawtooth principal
value of the finite-branch reciprocity theorem. For noninteger
color, retaining the same bounded sawtooth without the character
would give a different function.

For complex color the character and the Gaussian must be estimated
together. If \(\zeta=x+iy\), the line (12) has imaginary part
\(-y/(2pN)\). On a segment (14), their product with \(C_r\) is
the original exponential in (4), whose modulus is
\(e^{2\pi yt}\). Separate absolute estimates of the character and
Gaussian would introduce spurious growth at the two infinite ends.
The paired segment prescription already accounts for those ends.

## 4. Uniform control of the paired tails

The preceding convergence has a useful quantitative form. Put
\[
 B=1+|p|+|\zeta|/N,\qquad
 E=\exp\{2\pi\max(\operatorname{Im}\zeta,0)\}.
 \tag{17}
\]
For every fixed derivative order \(j\), there is \(C_{p,j}\),
independent of \(N,\zeta,M\), such that for \(M\ge2\)
\[
 \left|
 \partial_\zeta^j
 \left[Z_r(\zeta)-\sum_{m=-M}^{M}A_{r+2pm}(\zeta)\right]
 \right|
       \le \frac{C_{p,j}B^3E}{M}.
 \tag{18}
\]

Indeed, on \(0\le t\le1\), direct differentiation of (2) bounds
\(\partial_\zeta^j g_\zeta\) by \(C_jBE\), and its first two
\(t\)-derivatives by \(C_jNB^2E\) and \(C_jN^2B^3E\).
In (9), the first boundary term is therefore \(O_j(BE/(N|\ell|))\);
the remaining boundary and integral terms after the second
integration are \(O_j(B^3E/|\ell|^2)\).
Pairing the two class indices gives a bound
\(C_{p,j}B^3E/m^2\). Summing for \(m>M\) proves (18).

For \(\zeta=N\beta\) in a fixed compact complex \(\beta\)-set,
(18) has exponential cost at most
\(e^{2\pi N\max(\operatorname{Im}\beta,0)}\).
This is an endpoint growth estimate, not a comparison with the
filled hyperbolic volume. Taking \(M\) large at fixed \(N\) is
legitimate; an exponential geometric error in \(N\) does not
follow merely from local uniform convergence.

## 5. The original endpoint current and closing remain present

Define the entire finite-interval integral
\[
 I(b)=\int_0^1
        e^{2\pi ipN(t-\tfrac12)^2-2\pi ibt}\,dt
 \tag{19}
\]
and the original endpoint current
\[
 J(\zeta)=
       \frac{e^{\pi ipN/2}(1-e^{-2\pi i\zeta})}{2\pi iN}.
 \tag{20}
\]
Integrating the phase derivative on the same interval gives
\[
                    A_\ell(\zeta)
                      =(\ell+1)I(\zeta+N\ell)-J(\zeta).
 \tag{21}
\]
Indeed the amplitude in (4) is the phase derivative divided by
\(2\pi iN\), plus \(\ell+1\); its integrated derivative is
exactly \(-J(\zeta)\).
Equations (6) and (13) sum the whole expression (21).
They do not sum its constant \(J\)-part separately.
In particular the term with \(\ell=-1\) is not absent at complex
color: it is \(-J(\zeta)\).

On the physical range \(0\le n<N\), substituting (8) into (3)
gives the same full pair operator. Every specified finite linear
exterior contraction commutes with this equality. Fixed
\(\zeta\)-derivatives commute with (6) by (18). The formula thereby
retains the original coefficient interpolation and its normal data;
it supplies no new rule for continuing an arbitrary exterior.

The ordinary-circle coefficients still use the original conversion
\(\beta_j=(-1)^j(a_j-a_{j+2})\) and the canonical zero convention
\(a_N=a_{N+1}=0\). Values of the entire function (2) outside its
physical range must not replace these two zero coefficients.

This construction closes the continuation-prescription gap in the
finite-branch formula. It does not turn the branches into positive
integrals or establish the geometric contribution after closing.
That problem still requires estimates for the actual exterior and
for the combined original period.

## Direct proof dependencies

The entire coefficient, midpoint source identity, and endpoint
current in (2), (5), and (20)--(21) are those of
[the coherent Gaussian source](actual_coherent_filling_gaussian_chirp.md),
SHA256 d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522.
The original full-Hermite interpolation is in
[the twist-kernel calculation](actual_twist_circle_fourier_kernel.md),
SHA256 1d93f6f13d271c56eee6e7ea8ddf5b9ea0eea92a2076ede7068df552bab94292.
The integer-color specialization is compared with
[finite-branch reciprocity](research_full_hermite_gauss_reciprocity.md),
SHA256 ccd241bfcd15e9855ea9aaa10e65c84697874c36149d894edf3ff8dfa2300ee1.
All arguments here are written mathematics. No numerical evaluation,
mathematical code execution, test, or compilation was used.
