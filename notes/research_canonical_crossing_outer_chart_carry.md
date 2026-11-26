# The canonical crossing outside the spectrum and its retained carry

21 November 2026. The original positive and negative crossing polynomials
have the same variable leading action on a fixed outer spectral chart.
Their product is nevertheless the identity in the full physical algebra.
This note identifies the large polynomial carry that makes these two
statements compatible.

The estimate is uniform on compact subsets of \(\operatorname{Re}z<-6\).
It concerns actual canonical crossing polynomials, at both parities.
It also explains why their large off-spectrum values must be paired
with the original source before they are estimated: the full crossing
has a unit-modulus pairing with the actual recoupling polynomial.
No arbitrary-short-word continuation or volume theorem is inferred.

## 1. Original root polynomials

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and
\[
 \kappa=q^{d^2/2},\quad \eta=(-1)^d,\quad
 u_h=2\sin(\pi h/N),\quad S_j=\prod_{h=1}^ju_h,\quad S_0=1,
\]
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 P_N(z)=2T_N(z/2)+2=\prod_{j=0}^d(z-c_j).
\]
Here \(T_N\) is the ordinary Chebyshev polynomial. The canonical
Newton polynomials and the original signed crossings are
\[
 e_r(z)=S_r^{-2}\prod_{h=0}^{r-1}(c_h-z),\qquad
 R_N^\epsilon(z)=\kappa^\epsilon
                     \sum_{r=0}^d(-q)^{\epsilon r}e_r(z),
 \quad \epsilon\in\{1,-1\}.                              \tag{1}
\]
Each has degree below \(N\). The full algebra is
\(\mathcal A_N=\mathbb C[z]/(P_N)\), including all first normals
at the double roots. Its source and turn are
\[
 \phi_N(f)=\eta N^2[z^d]\operatorname{rem}_{P_N}f,\qquad
 \phi_N(e_i e_j)=\delta_{i+j,d},\qquad Je_r=e_{d-r}.       \tag{2}
\]
The original source theorem proves
\(R_N^+R_N^-=1\) in this full algebra and
\((R_N^+)^\sharp=R_N^-\), where the sharp operation conjugates
coefficients in the real Newton basis. These statements are stronger
than equality at the distinct roots. They and (1)--(2) are the
conventions of the [Newton source](actual_newton_turn_positive_gram.md).

Since \(S_d=N\) and \(c_d=c_0\),
\[
                       e_d(z)=
                \frac{\eta P_N(z)}{N^2(z-c_0)}.          \tag{3}
\]
The quotient in (3) is an ordinary polynomial.

## 2. A uniform outer expansion

**Theorem.** Let \(K\) be a compact subset of
\(\{\operatorname{Re}z<-6\}\). Uniformly for \(z\in K\) and both signs,
\[
 R_N^\epsilon(z)=
       \frac{\kappa^\epsilon q^{\epsilon d}P_N(z)}
                         {N^2(z-c_0)}(1+O_K(N^{-2})).  \tag{4}
\]
More generally, for every fixed integer \(J\ge0\), and \(N>J\),
its complete endpoint truncation is
\[
 \begin{split}
 R_N^\epsilon(z)
 =\frac{\kappa^\epsilon q^{\epsilon d}P_N(z)}
                         {N^2(z-c_0)}
 \left\{\sum_{j=0}^J(-q)^{-\epsilon j}
          \frac{S_j^2}{\prod_{h=1}^j(c_h-z)}
                              +O_{K,J}(N^{-2J-2})\right\}.
 \end{split}                                             \tag{5}
\]
The fixed derivatives in \(z\) of the normalized error obey the same
bound on smaller compact subsets.

**Proof.** Sine and root reflection give, exactly,
\[
 \frac{e_{d-j}(z)}{e_d(z)}
       =\frac{S_j^2}{\prod_{h=1}^j(c_h-z)}
       =\prod_{h=1}^j\frac{4\sin^2(\pi h/N)}{c_h-z}.     \tag{6}
\]
For example, the removed Newton roots are
\(c_{d-h}=c_h\), \(1\le h\le j\), and the removed terminal
factorial factors are \(u_{N-h}=u_h\).
Choose \(\delta>0\) with
\(\operatorname{Re}z\le-6-\delta\) on a neighborhood of \(K\).
Each denominator in (6) has modulus at least \(4+\delta\).
Every factor is therefore bounded by
\(\rho=4/(4+\delta)<1\). Its first \(J+1\) factors are, individually,
\(O_J(N^{-2})\), by \(\sin(\pi h/N)\le\pi h/N\).
Consequently
\[
 \sum_{j=J+1}^{d}\left|\frac{e_{d-j}(z)}{e_d(z)}\right|
                          \le C_{K,J}N^{-2J-2}
                                     \sum_{\ell\ge0}\rho^\ell.
\]
All coefficient ratios \((-q)^{-\epsilon j}\) have modulus one.
Factoring the \(r=d\) term in (1), and using
\(\eta(-q)^{\epsilon d}=q^{\epsilon d}\), proves (5).
Its \(J=0\) case is (4). The errors are holomorphic on the half-plane;
Cauchy's formula on slightly larger compact sets proves the derivative
assertion. \(\square\)

These are spectral-variable derivatives at the fixed original root.
No generic moving-\(q\) derivative is inferred from the reflection
identities used in the proof.

Let \(w(z)\) be the root of \(w+w^{-1}=z\) with \(|w|>1\).
It is holomorphic on this half-plane, and
\[
                    P_N(z)=w(z)^N(1+w(z)^{-N})^2.
\]
Hence, locally uniformly there,
\[
             \frac1N\log|R_N^\epsilon(z)|
                              \longrightarrow\log|w(z)|.      \tag{7}
\]
Both signs have the same variable rate. The retained unit phases
\(\kappa^\epsilon q^{\epsilon d}\) in (4) have not been suppressed.
For the actual geometric target \(z=2-4/c^2\), the real part of this
chart is \(0<c<1/\sqrt2\).

## 3. The inverse crossing word has a large exact carry

Define the ordinary quotient polynomial
\[
             C_N(z)=\frac{R_N^+(z)R_N^-(z)-1}{P_N(z)}. \tag{8}
\]
It is a polynomial of degree at most \(N-2\), because the crossings
are inverses in the full algebra. Formula (4) gives
\[
 C_N(z)=\frac{P_N(z)}{N^4(z-c_0)^2}
                                      (1+O_K(N^{-2}))           \tag{9}
\]
uniformly on each compact outer chart. To check the subtraction of
one, first multiply (4) for the two signs. Their phases cancel.
After division by \(P_N\), the omitted term \(1/P_N\) is
exponentially smaller than the displayed term, uniformly on \(K\),
since \(\inf_K|w|>1\).

Thus the canonical inverse word is exactly
\[
       \operatorname{rem}_{P_N}(R_N^+R_N^-)=1,
 \qquad R_N^+R_N^- -P_NC_N=1.                           \tag{10}
\]
The two large terms on the left have rate \(2\log|w|\), whereas
the remainder has rate zero. The carry itself has rate \(\log|w|\).
For real \(z<-6\), the unreduced product is also
\(|R_N^+(z)|^2\), by coefficient conjugation.

This is a literal positive crossing followed by its inverse, not a
modified test vector. It rules out continuing canonical multiplication
by replacing it with multiplication of off-spectrum scalar principal
branches. A rule retaining the global residue cycle and its carries
is a different proposal; (10) does not rule it out.

## 4. The fixed endpoint sector under the original source

The large factor \(P_N(z)\) has a useful source interpretation.
For a fixed \(j\), let
\[
          t_{j,N}^\epsilon
             =\kappa^\epsilon(-q)^{\epsilon(d-j)}e_{d-j}.
\]
Its rational density is exactly
\[
 \frac{t_{j,N}^\epsilon(z)}{P_N(z)}
       =\frac{\kappa^\epsilon q^{\epsilon(d-j)}S_j^2}
                           {N^2\prod_{h=0}^j(z-c_h)}. \tag{11}
\]
For fixed \(j\), all these poles approach the endpoint \(2\).
Repeated poles are interpreted with their actual first normals.

For \(0\le\alpha\le\lfloor d/2\rfloor\), retain the actual root
recoupling polynomial of
the [geometric target theorem](actual_matching_edge_geometric_target_polynomial.md):
\[
 p_{\alpha,N}(z)=
 \sum_{j=0}^{\alpha}\frac1{S_j^4}
       \prod_{r=0}^{j-1}(c_r-c_\alpha)(c_r-z)
             =\sum_{j=0}^{d}e_j(c_\alpha)e_j(z).        \tag{12}
\]
The equality follows from the Newton definition; terms \(j>\alpha\)
vanish. This is the full original turn kernel at the actual folded
node, not a value-only replacement of its Hermite data. Equations
(2) and (12) give, for every canonical \(g\),
\[
 \phi_N(p_{\alpha,N}g)=(Jg)(c_\alpha),\qquad
              \phi_N(p_{\alpha,N}e_{d-j})=e_j(c_\alpha).        \tag{13}
\]
In particular \(\phi_N(p_{\alpha,N}e_d)=1\) and \(Je_d=1\):
the leading endpoint polynomial is not source-null. Every fixed
endpoint term has a polynomial source cost:
\[
 0\le e_j(c_\alpha)\le C_jN^{2j}\quad(j\le\alpha),
 \qquad e_j(c_\alpha)=0\quad(j>\alpha).                 \tag{14}
\]
Indeed its numerator is a product of at most \(j\) numbers bounded
by \(4\), while \(S_j\) has size a fixed positive constant times
\(N^{-j}\). If \(\alpha/N\ge\xi_0>0\), then for each fixed \(j\)
and sufficiently large \(N\),
\[
                     c_{j,\xi_0}N^{2j}
                  \le e_j(c_\alpha)\le C_jN^{2j}.       \tag{15}
\]
The numerator factors are then bounded below: \(c_r\to2\) for fixed
\(r\), whereas \(c_\alpha\) stays separated from \(2\).
These are lower bounds for the single positive terms, not for arbitrary
complex sums of endpoint terms.

More precisely, on the finite endpoint space
\(V_{J,N}=\operatorname{span}\{e_d,e_{d-1},\ldots,e_{d-J}\}\),
\[
 \left|\phi_N\!\left(p_{\alpha,N}\sum_{j=0}^Ja_je_{d-j}\right)\right|
                        \le C_J\sum_{j=0}^J|a_j|N^{2j}.        \tag{16}
\]
There is no positive lower bound for every nonzero complex vector
in this space. For \(J\ge1,\alpha\ge1\), the nonzero vector
\(e_{d-1}-e_1(c_\alpha)e_d\) has zero pairing.

## 5. The entire single-crossing period has modulus one

The full source pairing is even smaller than a generic polynomial
endpoint bound. Direct reversal of (1) gives
\[
                              JR_N^\epsilon=R_N^{-\epsilon},
\]
because \(\kappa^2(-q)^d=1\). Thus (13) proves the exact identity
\[
 \boxed{\quad
 \phi_N(p_{\alpha,N}R_N^\epsilon)
       =R_N^{-\epsilon}(c_\alpha)
       =\left[\kappa(-1)^\alpha
                              q^{\alpha(\alpha+1)}\right]^{-\epsilon}.
 \quad}                                                        \tag{17}
\]
The last equality is the diagonal entry of the original triangular
crossing matrix. Its modulus is one. All original carriers and both
level parities remain in (17).

Thus a large canonical off-spectrum crossing value can have a unit-modulus
marked pairing with the actual recoupling polynomial. The endpoint expansion
cannot be paired term by term with an \(N\)-dependent exterior merely
from its relative outer error. Formula (13), or an equivalent exact
source contraction, must be retained before estimating that sector.

## 6. Scope

The new estimates give a source-exact outer continuation for a single
crossing and its inverse, with every fixed endpoint-tail order controlled.
They identify an actual short-word carry and a source-period cancellation.
They do not identify a contributing geometric contour for an arbitrary
short component. In particular they neither assert stability of a local
WKB class under arbitrary words nor make \(R\)-multiplication pointwise
away from the physical spectrum. The required source-compatible global
cycle and geometric lower estimate remain separate.

## Complete direct sources

Both complete matching texts were read. The first gives the exact
Newton/Frobenius algebra, signed crossings and physical turn; the second
gives the actual recoupling polynomial (12). The uniform outer estimates
and the retained carry/source consequences are proved above.

| Source | SHA-256 |
|---|---|
| [Actual Newton turn and crossing](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Actual geometric target polynomial](actual_matching_edge_geometric_target_polynomial.md) | c748f8f7fc35fc28e8d982772e5c13a41acc650d05bd8134465250072d9ec265 |

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical experiment, build, git operation,
previous-final edit or public-document change was performed.
