# Actual circle coefficients: bulk asymptotics, exact central zeros, and resonances

Private written proof, 14 November 2026. The ordinary circle coefficients
of each fixed signed full twist have a uniform expansion retaining their
first nonzero endpoint term. For every power with \(|p|\ge2\), these
actual differences have infinitely many exact central zeros. The proof
classifies those zeros, gives a lower bound away from a finite structural
resonance set, and confines any other possible bulk zero to explicit
shrinking resonance neighborhoods. No numerical evaluation, mathematical
code, test, or frozen-manuscript change is used.

## 1. The actual coefficient and its source conventions

Fix \(p\in\mathbb Z\setminus\{0\}\), \(h=|p|\),
\(q=e^{\pi i/N}\), and \(\kappa=q^{(N-1)^2/2}\), with this
fixed logarithm. In the full algebra
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\), write
\[
 \operatorname{rem}(r_N^{2p})(z)
       =a_0+\sum_{n=1}^{N-1}a_n\,2T_n(z/2).
\]
The actual ordinary circle coefficients are
\[
 \beta_j=(-1)^j(a_j-a_{j+2}),\qquad
 a_N=a_{N+1}=0,\qquad 0\le j<N.
 \tag{1}
\]
Thus \(R^{2p}=\kappa^{2p}\sum_j\beta_jL_{j+1}\), with the
original pivotal circle operators \(L_{j+1}\). The unit scalar
\(\kappa^{2p}\) stays on the physical twist.

These conventions, including the last zero coefficients, are from
[the original circle kernel](actual_twist_circle_fourier_kernel.md).
The entire Weyl symmetry and the half weight at the final physical
color in [the coherent Gaussian note](actual_coherent_filling_gaussian_chirp.md),
Section 6, remain unchanged. In particular an integer interpolation
outside \(0\le n<N\) must not replace the zero coefficients in (1).
Our asymptotic statements concern a fixed bulk interval, where both
\(j\) and \(j+2\) lie in the canonical range for large \(N\).

Use the finite branch phases and constants
\[
 \begin{split}
 G_{p,N}&=\frac{e^{i\operatorname{sgn}(p)\pi/4}}{\sqrt{2hN}},\\
 C_0(N,n)&=\exp\left[-\pi in-\frac{\pi in^2}{2pN}\right],\\
 C_r(N,n)&=(-1)^r\exp\left[-\pi i(n+Nr)
                       -\frac{\pi i(n+Nr)^2}{2pN}\right],\\
 c_r&=\begin{cases}r+1,&0\le r<h,\\r+1-2h,&h\le r<2h,\end{cases}\\
 F_p(N,n)&=\sum_{r=0}^{2h-1}c_r(-1)^{(N+1)r}
       \exp\left[-\frac{\pi inr}{p}-\frac{\pi iNr^2}{2p}\right].
 \end{split}
 \tag{2}
\]
The finite factor \(F_p\) depends only on \(N\bmod4h\) and
\(n\bmod2h\). These are the actual phases from
[full-Hermite reciprocity](research_full_hermite_gauss_reciprocity.md)
and [the first-kind bulk estimate](research_fused_twist_real_branch_symbol.md).
No branch phase or normal term is chosen from a knot value.

## 2. One more controlled endpoint order

Put \(f(a)=\csc(\pi a)\). Uniformly over physical integers
\(n\) with \(\epsilon\le n/N\le1-\epsilon\), the full
first-kind coefficient has the expansion
\[
 \begin{split}
 a_n={}&\kappa^{-p}G_{p,N}C_0(N,n)F_p(N,n)\\
 &+q^{-p/2}\left\{
     \frac{ip}{N}f(n/N)
    +\frac{p^2}{2\pi N^2}f''(n/N)
    -\frac{ip^3}{8\pi^2N^3}f^{(4)}(n/N)\right\}
    +O_{p,\epsilon}(N^{-4}).
 \end{split}
 \tag{3}
\]

Here is a direct extension of the paired sawtooth proof, to specify
the remainder needed when taking the circle difference. Let
\(s(u)=1/2-\{u\}\), \(B\notin\mathbb Z\),
\(2pNB\in\mathbb Z\), \(b=\{B\}\), and
\(\delta=\operatorname{dist}(B,\mathbb Z)\). After pairing
positive and negative Fresnel variables, set
\[
 f_b(v)=s(b-v)+s(b+v)-2s(b),\qquad
 I_k=\int_0^\infty f_b(v)v^{-2k}e^{2\pi ipNv^2}\,dv.
\]
For \(k=0\) take the paired improper limit; for \(k\ge1\)
the integral is absolute. The amplitude is zero for \(v<\delta\),
is bounded by two, and has jumps \(+1\) at \(m+1-b\) and
\(-1\) at \(m+b\). All jumps have phase
\(e^{2\pi ipNB^2}\), by the original integer condition.

Write \(D=4\pi ipN\) and \(C(B)=\pi\cot(\pi B)\).
Integration by parts on the constant intervals, including every
jump, gives the exact recurrence
\[
 I_k=\frac{e^{2\pi ipNB^2}C^{(2k)}(B)}{D(2k)!}
                         +\frac{2k+1}{D}I_{k+1}.
 \tag{4}
\]
For \(k=0\) the jump sum uses the paired cotangent identity.
For \(k\ge1\) its absolute convergence follows from the powers
\(v^{-2k-1}\). Indeed the signed jump sum equals
\(-C^{(2k)}(B)/(2k)!\); this follows by differentiating the
paired partial fractions \(2k\) times. Boundary terms at zero
and infinity vanish.

Three substitutions in (4) yield
\[
 I_0=e^{2\pi ipNB^2}
       \left\{\frac{C(B)}D+\frac{C''(B)}{2D^2}
                                  +\frac{C^{(4)}(B)}{8D^3}\right\}
                                  +\frac{15}{D^3}I_3.
 \tag{5}
\]
One additional integration by parts bounds
\(I_3=O((hN\delta^7)^{-1})\): the jump sum has absolute
weights \(v^{-7}\), and the ordinary remainder has absolute
integral \(O(\delta^{-7})\). Thus the remainder in (5) is
\(O((h^4N^4\delta^7)^{-1})\).

For the actual branches
\(B_r=1/2-(n/N+r)/(2p)\), one has
\(\delta\ge\epsilon/(2h)\), and
\[
 C_r e^{2\pi ipNB_r^2}=(-1)^r e^{\pi ipN/2},\qquad
 \sum_r(-1)^r\cot(\pi B_r)=2p(-1)^{p+1}f(n/N).
 \tag{6}
\]
Differentiate the last identity \(2k\) times in the real variable
\(a=n/N\); each branch derivative supplies \(-1/(2p)\).
The three retained terms after summing (5) are exactly
\[
 \frac{ipq^{-p/2}}N
       \sum_{k=0}^2\frac1{k!}
          \left(\frac{p}{2\pi iN}\right)^k f^{(2k)}(a).
\]
This proves (3), with its uniform error and original phase.
Only a real-variable identity is differentiated here; this does
not analytically continue the sawtooth reciprocity to complex color.

## 3. Uniform expansion of the prescribed circle difference

Set
\[
 t=\frac{j+1}{N},\qquad
 A=F_p(N,j),\quad B=F_p(N,j+2),\qquad
 \Psi_{A,B}(t)=A-e^{-2\pi it/p}B.
 \tag{7}
\]
The pair \((A,B)\) ranges over a finite set specified by the two
residue classes in (2). In particular it does not vary continuously
with the normalized color \(t\).

**Theorem 1.** For every fixed \(p\ne0\) and
\(0<\epsilon<1/2\), uniformly over the physical bulk
\(\epsilon\le t\le1-\epsilon\),
\[
 \boxed{\begin{split}
 (-1)^j\beta_j={}&
   \kappa^{-p}G_{p,N}C_0(N,j)\Psi_{A,B}(t)\\
  &+q^{-p/2}\left\{-\frac{2ip}{N^2}f'(t)
                        -\frac{p^2}{\pi N^3}f'''(t)\right\}
       +O_{p,\epsilon}(N^{-4}).
 \end{split}}
 \tag{8}
\]

*Proof.* The quotient of the two exact phases in (2) is
\(C_0(N,j+2)/C_0(N,j)=e^{-2\pi it/p}\). For the endpoint
terms in (3), use the centered difference at \(t\pm1/N\).
The first term gives \(-2ipf'(t)/N^2+O(N^{-4})\), the
second gives \(-p^2f'''(t)/(\pi N^3)+O(N^{-5})\), and
the third contributes \(O(N^{-4})\). The two retained remainders
are each \(O(N^{-4})\). This proves (8). \(\square\)

In particular the compulsory endpoint term has leading coefficient
\[
 -2ipf'(t)=\frac{2\pi ip\cos(\pi t)}{\sin^2(\pi t)}.
 \tag{9}
\]
It vanishes only at the central normalized color \(t=1/2\).
Moreover
\[
 f'''(t)=\pi^2\{5+6\cot^2(\pi t)\}f'(t).
 \tag{10}
\]
Both endpoint terms in (8) therefore vanish at the center. On the
real bulk interval their coefficients before the common phase are
respectively imaginary and real. They cannot cancel one another.

## 4. Exact central arithmetic zeros

The full Fourier-Hermite aliases give the exact identity
\(H_n=a_n-a_{N-n}\) for \(1\le n<N\), where
\[
 H_n=q^{-n}\frac1N\sum_{k\bmod N}
          e^{2\pi i\{pk^2+(p-n)k\}/N}.
 \tag{11}
\]
For \(N=2m\) and \(j=m-1\), equation (1) thus gives
\[
                         \beta_{m-1}=(-1)^{m-1}H_{m-1}.
 \tag{12}
\]
At \(N=2\) this also follows from \(a_N=0\) and \(a_0=H_0\).

**Theorem 2.** At every even level \(N=2m\), for every signed
\(p\ne0\),
\[
 \boxed{\quad
 \beta_{m-1}=0\ \Longleftrightarrow\ \gcd(|p|,m)>1,
 \qquad
 |\beta_{m-1}|=m^{-1/2}\ \text{otherwise}.\quad}
 \tag{13}
\]

*Proof.* Put \(g=\gcd(|p|,N)\), \(L=N/g\).
Grouping the quadratic sum in (11) into cosets shows it is zero
unless \(g\mid n\). In that case reduce to the coprime
quadratic sum with \(p'=p/g\) and \(b'=(p-n)/g\) modulo
\(L\). Squaring its normalized modulus and summing the original
variable first leaves only differences \(u\) with \(L\mid2u\).
For odd \(L\) its squared modulus is \(1/L\). For even \(L\)
it is
\[
              \frac1L\{1+(-1)^{p'L/2+b'}\}.
 \tag{14}
\]
This proof includes negative \(p\), all parity cases, and \(L=1\).

At \(n=m-1\), the divisibility requirement implies
\(g\mid\gcd(2m,m-1)\), so \(g\) is one or two. If
\(g=1\), \(p\) is odd and the exponent in (14) is
\(pm+p-m+1\), which is even. Its squared modulus is
\(2/N=1/m\). If \(g=2\), divisibility requires \(m\) odd;
the reduced modulus \(m\) is odd and again gives squared modulus
\(1/m\). These two possibilities are exactly
\(\gcd(|p|,m)=1\). In all other cases the sum vanishes.
Equation (12) proves the result. \(\square\)

Thus every \(|p|\ge2\) has infinitely many levels with an exact
bulk circle zero. For example \(N\) divisible by \(2|p|\)
always has one. This disproves an all-bulk lower bound for these
actual circle coefficients, while preserving the earlier theorem
for the different coefficients \(a_n\).

## 5. Structural resonance classes and a proper-domain lower bound

The finite pair \((A,B)\) in (7) has the following exhaustive
classification for its Gaussian leading factor:

- If \(A=B=0\), the leading factor is identically zero.
- If exactly one is zero, or \(|A|\ne|B|\), it has no real zero.
- Otherwise its real zeros satisfy
  \(e^{-2\pi it/p}=A/B\). There is at most one such point in
  \(0<t<1\), and any such zero is simple, with
  \(\Psi'(t_0)=(2\pi i/p)A\ne0\).

These tests use the explicit finite sums (2), for arbitrary fixed
\(p\); no case enumeration or numerical root selection is needed.
Let \(\mathcal Z_p\) be the union of those nonidentical real
zeros over the finite residue pairs, together with \(1/2\).
It is a finite subset of \((0,1)\).

**Theorem 3.** Fix \(p\ne0\), \(0<\epsilon<1/2\), and
\(\delta>0\). On the physical colors satisfying
\[
 \epsilon\le (j+1)/N\le1-\epsilon,
 \qquad \operatorname{dist}((j+1)/N,\mathcal Z_p)\ge\delta,
\]
there is a uniform lower bound
\[
                         |\beta_j|\ge c_{p,\epsilon,\delta}N^{-2}
 \tag{15}
\]
for all sufficiently large \(N\), with both parities retained.

*Proof.* On every nonidentical branch pair, compactness away from
its zero and finiteness of the residue pairs bound \(|\Psi|\)
away from zero. The Gaussian term then gives a lower bound of
order \(N^{-1/2}\). On an identically zero pair, distance from
\(1/2\) bounds \(|f'|\) away from zero, and (8)--(10) give
a lower bound of order \(N^{-2}\). \(\square\)

Two useful refinements retain more physical colors. On an
identically zero pair, every noncentral bulk grid point has
\[
                         |\beta_j|\ge c_{p,\epsilon}N^{-3}.
 \tag{16}
\]
The same assertion holds at an exact noncentral zero of \(\Psi\).
Indeed a noncentral grid point has \(|t-1/2|\ge1/(2N)\),
and \(|f'(t)|\ge c_\epsilon|t-1/2|\). The two orthogonal
endpoint terms have modulus at least \(2h|f'(t)|/N^2\),
while the error in (8) is \(O(N^{-4})\).

## 6. Where any additional exact bulk zero could occur

For a nonidentical pair, equation (8) supplies a quantitative
necessary condition for a zero, with every phase retained:
\[
 \Psi_{A,B}(t)=
 \frac{q^{-p/2}}{\kappa^{-p}G_{p,N}C_0(N,j)}
       \left\{\frac{2ip}{N^2}f'(t)
                     +\frac{p^2}{\pi N^3}f'''(t)\right\}
       +O_{p,\epsilon}(N^{-7/2}).
 \tag{17}
\]
Thus any such zero must lie within \(O_{p,\epsilon}(N^{-3/2})\)
of that pair's simple resonance \(t_0\). If \(t_0=1/2\),
the more precise bound obtained from (10) is
\[
 |t-1/2|\le C_{p,\epsilon}|t-1/2|N^{-3/2}
                                      +C_{p,\epsilon}N^{-7/2}.
\]
For large levels this excludes every noncentral grid point.
Only the exact center remains, and its zero criterion is (13).

A noncentral exact resonance is also nonzero by (16). If that
resonance \(t_0\) is rational, every unequal physical grid point
is at distance at least \(1/(bN)\), where \(b\) is its fixed
denominator. This is larger than the allowed \(O(N^{-3/2})\)
neighborhood for all large levels. Therefore rational resonances
cause no additional eventual exact bulk zeros. Equivalently, this
applies whenever the unit ratio \(A/B\) defining the resonance
is a root of unity.

What remains unclassified is possible cancellation in the thin
neighborhoods of irrational noncentral resonances arising from
equal-modulus, nonzero finite sums \(A,B\). Formula (17) is its
explicit phase-sensitive necessary balance. Neither proximity to
such a resonance nor equality of the two Gaussian magnitudes is
asserted sufficient for an exact zero. No assertion that every
unit ratio \(A/B\) is a root of unity is used here.

## 7. Scope for short-filling composition

This result concerns the actual ordinary circle coefficients,
including their original normal terms, zero endpoint convention,
and central arithmetic zeros. It improves a bound on separate
first-kind coefficients by estimating their prescribed differences.
The proper-domain lower bound and the resonance criterion are
uniform statements for every fixed signed full-twist power.

They do not supply a complex geometric color continuation, control
a general exterior color sum, or establish survival of its
geometric period. In particular finite resonance sets of these
local coefficients are not the finite exceptional knots sought in
the original volume-conjecture goal.

## Direct source versions

- `research_fused_twist_real_branch_symbol.md`:
  `e569817c0444b41cdc1030c1e60a36567d6d83e7f2247dccd16c902705eb15ae`.
- `research_full_hermite_gauss_reciprocity.md`:
  `ccd241bfcd15e9855ea9aaa10e65c84697874c36149d894edf3ff8dfa2300ee1`.
- `actual_coherent_filling_gaussian_chirp.md`:
  `d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522`.
- `actual_twist_circle_fourier_kernel.md`:
  `1d93f6f13d271c56eee6e7ea8ddf5b9ea0eea92a2076ede7068df552bab94292`.
