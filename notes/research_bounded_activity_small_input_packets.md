# Bounded-activity Euler packets near the physical vacuum

22 November 2026. Research note.
Earlier finals and public manuscripts remain unchanged.

Small physical inputs permit bounded Euler activities, including one,
in the full-norm packet construction. A fixed diagonal frame supplies
the local kernel, and a separate estimate in the original positive
head metric controls its whole complement. No norm is transported
back through the exponentially conditioned diagonal frame.

The statement concerns the actual capped-lowering Euler words defined
below, not arbitrary signed crossings or a nonzero closed knot source.

## 1. Actual operators and the statement

Fix \(r,\ell\ge1\) and \(i_1,\ldots,i_\ell\in\{1,\ldots,r\}\).
Use the full physical binomial head spaces
\[
 N\ge2,\quad d=N-1,\quad Q=e^{2\pi i/N},\quad x=-e^{-\pi i/N},
 \qquad \|w_a\|^2=\binom da^{-1},\quad
                  \mathcal V_N=V_N^{\otimes r}.
 \tag{1}
\]
The literal endpoint matrices and finite Euler factors are
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\quad Ew_0=0,\qquad
 Kw_a=xQ^{-a}w_a,\qquad F_n=(Q;Q)_n,
\]
\[
 X_i=E_iK_{i+1}\cdots K_r,\qquad
 U_{i,N}(\lambda)=\sum_{n=0}^{d}\frac{\lambda^nX_i^n}{F_n},
 \qquad
 W_N(\boldsymbol\lambda)
       =U_{i_\ell,N}(\lambda_\ell)\cdots U_{i_1,N}(\lambda_1).
 \tag{2}
\]
All zero arrows and all finite coefficients remain.
Let \(\psi_z\), \(z\in Y=(\mathbb P^1)^r\), be the normalized
product binomial coherent vector. In one affine head,
\[
 \psi_z=(1+|z|^2)^{-d/2}
          \sum_{a=0}^{d}\binom da z^a w_a,\qquad
 d\mu(z)=\frac{d\Re z\,d\Im z}{\pi(1+|z|^2)^2}.
 \tag{3}
\]
Write \(\mu^{[r]}\) for the product probability measure.
The physical input restriction below uses the original affine
coordinates near the vacuum \(w_0^{\otimes r}\).

Fix arbitrary finite \(L\ge0\) and \(R>0\), and put
\[
 \Omega_R=\{y\in Y:\ |y_j|<R\text{ for every }j\}.
\]

**Theorem.** There is \(\rho>0\) such that, uniformly for
\(|\lambda_j|\le L\), \(|z_j|\le\rho\), and all sufficiently
large integer \(N\), the actual vector \(v_N=W_N\psi_z\) has
an explicitly reconstructed polynomial packet \(v_N^{\mathrm{app}}\)
satisfying
\[
 \frac{\|v_N-v_N^{\mathrm{app}}\|}{\|v_N\|}
                              \le C/N+Ce^{-cN}.
 \tag{4}
\]
Its exact positive coherent mass outside the fixed output cap obeys
\[
 N^r\int_{Y\setminus\Omega_R}
       \frac{|\langle\psi_y,v_N\rangle|^2}{\|v_N\|^2}
                               \,d\mu^{[r]}(y)\le Ce^{-cN}.
 \tag{5}
\]
The activities and words may thus include activity one.
The input radius depends on the fixed word, \(L\), and \(R\),
but not on \(N\). Both quantum-level parities are retained.

The proof uses the exact all-activity budgets from the accepted
full-norm theorem. With \(B_L=(1+L)^\ell\), they give
\[
                 \|W_N^{\pm1}\|\le B_L^d,\qquad
                           \|W_N\psi_z\|\ge B_L^{-d}.
 \tag{6}
\]
Their binomial divided-power proof is valid at every \(N\ge2\).

## 2. A local kernel at bounded physical activity

For unnormalized binomial columns \(c(z)\) and evaluation rows \(v(w)\)
write
\[
 \mathcal K_{\boldsymbol\lambda,N}(w,z)
       =v(w)W_N(\boldsymbol\lambda)c(z),\qquad
 \sigma_{\boldsymbol\lambda,N}
       =\frac{\mathcal K_{\boldsymbol\lambda,N}}
                    {\prod_j(1+w_jz_j)^d}.
\]
For fixed \(s>0\), define \(D_sw_{\mathbf a}=s^{\sum a_j}w_{\mathbf a}\).
Direct substitution in (2) gives
\[
 D_s^{-1}X_iD_s=sX_i,\qquad
 D_s^{-1}W_N(\boldsymbol\lambda)D_s=W_N(s\boldsymbol\lambda),
\]
\[
 \boxed{\quad
 \mathcal K_{\boldsymbol\lambda,N}(w,z)
         =\mathcal K_{s\boldsymbol\lambda,N}(sw,z/s).
 \quad}
 \tag{7}
\]
The normalized symbol satisfies the same identity, since the
identity pairing \(1+w_jz_j\) is unchanged.

The choice of parameters is not circular. First fix the nonincident
compact transformed-pair set
\[
                  |w_j'|\le1,\qquad |z_j'|\le1/2.
\]
The compact composition theorem supplies a positive activity radius
on a finite cover. Choose one chart near \((w',z')=(0,0)\)
and smaller positive radii \(a\le1,b\le1/2\) within that chart.
Fix \(s>0\) so small that \(2sR\le a\) and \(sL\) lies strictly
inside its activity radius. Then require \(\rho\le sb\).
All choices precede \(N\), and the transformed compact was fixed
before \(s\).

On \(|w_j|\le2R,\ |z_j|\le\rho\), the actual local kernel theorem
and (7) therefore give
\[
 \sigma_{\boldsymbol\lambda,N}(w,z)
   =e^{N\mathcal S_L(\boldsymbol\lambda,w,z)}
              b_L(\boldsymbol\lambda,w,z)(1+O(N^{-1})),
 \tag{8}
\]
with uniform relative error. The phase and nonzero amplitude are
the initialized source functions evaluated at
\((s\boldsymbol\lambda,sw,z/s)\); no new normalization is chosen.
They are holomorphic on a neighborhood of the stated compact.

For example the one-head ratios
\[
 \theta=\frac{wz}{1+wz},\qquad t=\frac{\lambda z}{1+wz}
\]
are unchanged by (7). The present argument does not shrink an
unchanged physical interaction by gauge: the additional smallness
comes from restricting the original input \(z\).
No estimate below uses \(\|D_s\|\) or \(\|D_s^{-1}\|\).

## 3. An original-metric bound for the entire complement

Let \(P_m\) be the orthogonal projection onto the box of occupations
\[
                 a_j\le m\quad(1\le j\le r).
\]
Every factor in (2) lowers just its donor occupation and leaves the
others unchanged. Therefore \(\operatorname{ran}P_m\) is invariant
under every factor and under their whole word.

Set
\[
 p_R=\frac{R^2}{1+R^2},\qquad
 \eta=-\frac12\log[1-(1-e^{-1})p_R],\qquad
                         m=\lfloor\eta d\rfloor.
 \tag{9}
\]
Here \(0<\eta<1/2\), so \(m<d\).
Squared coherent coefficients are independent binomial probabilities
with parameters \(d,p_j\), \(p_j=|z_j|^2/(1+|z_j|^2)\).
For a binomial variable \(A\) with parameter \(p\), Markov's inequality
applied to \(e^{-A}\) gives
\[
 \mathbb P(A\le m)\le e^m(1-p+pe^{-1})^d.
\]
If \(y\notin\Omega_R\), at least one \(p_y\ge p_R\).
The preceding formula and (9) prove the all-output bound
\[
                        \|P_m\psi_y\|^2\le e^{-\eta d}.
 \tag{10}
\]
It includes projective infinity, where that head is exactly \(w_d\)
and its projection is zero.

For inputs \(|z_j|\le\rho\le1\), the elementary opposite tail estimate is
\[
 \mathbb P(A>m)
  \le\sum_{a=m+1}^{d}\binom da p^a
  \le2^d\rho^{2(m+1)}.
\]
A union bound over the heads yields
\[
               \|(I-P_m)\psi_z\|
                        \le\sqrt r\,2^{d/2}\rho^{m+1}.
 \tag{11}
\]
Choose \(\rho\) still smaller so that
\[
       2\log B_L+\tfrac12\log2+\eta\log\rho\le-\eta.
 \tag{12}
\]
This is a positive fixed input radius; also impose
\(\rho\le\min(1,R/2,sb)\), including the restriction from Section 2.

Decompose the exact output as
\[
 v_N=v_{\mathrm{low}}+v_{\mathrm{high}},\qquad
 v_{\mathrm{low}}=W_NP_m\psi_z,\qquad
 v_{\mathrm{high}}=W_N(I-P_m)\psi_z.
\]
The low part lies in \(\operatorname{ran}P_m\), while (6),
(11), \(m+1>\eta d\), and (12) give
\[
             \frac{\|v_{\mathrm{high}}\|}{\|v_N\|}
                                  \le\sqrt r\,e^{-\eta d}.
 \tag{13}
\]
In particular \(\|v_{\mathrm{low}}\|\le
(1+\sqrt r\,e^{-\eta d})\|v_N\|\).

The exact frame identity is
\[
                N^r\int_Y|\psi_y\rangle\langle\psi_y|
                                      \,d\mu^{[r]}(y)=I.
 \tag{14}
\]
It follows by angular integration and
\(\binom da\int_0^\infty t^a(1+t)^{-N-1}dt=1/N\),
using \(u=t/(1+t)\) and integration by parts.
By (10) the low part's outside squared frame norm is at most
\(N^re^{-\eta d}\|v_{\mathrm{low}}\|^2\).
By (14) the high part's entire squared frame norm is
\(\|v_{\mathrm{high}}\|^2\).
Apply \(|a+b|^2\le2|a|^2+2|b|^2\) and (13).
This proves (5), absorbing the fixed polynomial \(N^r\)
into a smaller positive exponential rate.
Thus the whole complement is estimated in the original metric.

## 4. The actual polynomial packet

Let \(\mathcal A_Nv(y)=\langle\psi_y,v\rangle\), with target measure
\(N^rd\mu^{[r]}\). Equation (14) says that \(\mathcal A_N\) is
an isometry and its adjoint is a contraction.
Put \(k_N(y,z)=\langle\psi_y,W_N\psi_z\rangle\).
Multiplying (8) by the exact coherent overlap supplies
\[
 k_N^{\mathrm{app}}(y,z)=
 \langle\psi_y,\psi_z\rangle
       e^{N\mathcal S_L(\boldsymbol\lambda,\bar y,z)}
                       b_L(\boldsymbol\lambda,\bar y,z).
\]
Its local relative error is \(O(N^{-1})\), uniformly on
\(\Omega_{2R}\). Choose \(0\le\chi\le1\), equal to one on
\(\Omega_R\), supported inside \(\Omega_{2R}\), and define
\[
              v_N^{\mathrm{app}}
                         =\mathcal A_N^*(\chi k_N^{\mathrm{app}}).
 \tag{15}
\]
This is a vector in the actual finite space, equivalently a polynomial
section of degree at most \(d\) on each head.

The exact error decomposition is
\[
 k_N-\chi k_N^{\mathrm{app}}
       =\chi(k_N-k_N^{\mathrm{app}})+(1-\chi)k_N.
\]
The first term has frame norm at most \(C\|v_N\|/N\), by
the local relative bound and the isometry. Formula (5) bounds
the second by \(Ce^{-cN}\|v_N\|\), after reducing \(c\).
Apply \(\mathcal A_N^*\) to obtain (4). No successive vector
errors are passed through large gate norms.

## 5. Exponential accuracy of an exact quantum-polynomial truncation

Fix any \(\Lambda,\delta>0\). Replace each factor in (2) by its
sum over \(0\le n\le m_\delta=\min(d,\lfloor\delta d\rfloor)\),
and denote the resulting ordered word by \(W_N^{[\delta]}\).
After decreasing the input radius further,
\[
 \boxed{\quad
 \frac{\|(W_N-W_N^{[\delta]})\psi_z\|}{\|W_N\psi_z\|}
                                  \le Ce^{-\Lambda N}.
 \quad}
 \tag{16}
\]
If \(\delta\ge1\), the words coincide. Otherwise both preserve
\(\operatorname{ran}P_{m_\delta}\) and agree there exactly,
because every omitted lowering power annihilates this box.
Thus
\[
          (W_N-W_N^{[\delta]})P_{m_\delta}=0.
\]
The same coefficientwise binomial budget as in (6) also bounds
the truncated word by \(B_L^d\). Formula (11), with \(m_\delta\)
instead of \(m\), proves
\[
 \frac{\|(W_N-W_N^{[\delta]})\psi_z\|}{\|W_N\psi_z\|}
 \le2\sqrt r\,
   \exp\{d[2\log B_L+\tfrac12\log2+\delta\log\rho]\}.
\]
Choose the bracket at most \(-2\Lambda\) and use
\(d=N-1\ge N/2\). This proves (16).

There is also an exact output endpoint identity. Let \(Q_{m_\delta}^+\)
project onto the box in which every output occupation is at least
\(d-m_\delta\). Then, for all inputs and activities,
\[
                    Q_{m_\delta}^+(W_N-W_N^{[\delta]})=0.
 \tag{17}
\]
Every monomial removed by the per-factor cutoff contains an
\(X_i^n\) with \(n>m_\delta\). Immediately after that factor its
donor occupation is at most \(d-m_\delta-1\), and every subsequent
factor only lowers occupations. Such a monomial cannot reach the
displayed high box. Together with the input-box identity above,
this is exact preservation at the two endpoint corners, not an
asymptotic removal of their atoms. Neither box is identified with
the original pivotal or Frobenius closing. The cutoff here is
per factor, throughout.

All coefficients kept here are exact quantum coefficients.
Their truncation degree grows with \(N\). This is not an
exponentially accurate classical WKB expansion; (4) still has
the stated \(O(N^{-1})\) error.

## 6. Source and geometric scope

The filtration and the coherent resolution retain both physical
endpoint atoms and all zero extreme arrows before estimating errors.
The estimates include their absolute norm contributions; they do
not give relative accuracy for an exponentially smaller prescribed
closing. No meridian or quantum-normal wall is deleted by
differentiating this fixed-root, complete-meridian statement.

The input neighborhood is at the actual lowering vacuum. It has
not been identified with the boundary data of a generic geometric
short component. The operators are the fixed \(X_i\)-Euler alphabet;
flips, turnovers, arbitrary signed crossings and opposite-source
quotients are not silently added. The binomial head norm is not
the Newton pair-algebra coefficient norm of the quartic. No uniformly
conditioned reconstruction between those metrics, nonzero original
source after branching, or new volume-conjecture class is proved.

## Complete proof sources

Both entire matching sources were read:

| Source | SHA-256 |
|---|---|
| [All-activity norms and full-norm coherent reconstruction](research_small_activity_full_norm_packet_transport.md) | 18968c9cb75e415d2eff5c68a506e8fa719fa3b909e6e98b1bfa527f68707c72 |
| [Actual compact coherent composition](research_capped_coproduct_compact_coherent_composition.md) | c54ba609e91ca18193ac9c9d7e7b32f0d0b39c00b3ff36bdf830184f8ad24d2b |

The exact gauge, binomial tails, original-metric localization and
quantum-polynomial truncation are proved inline. Only written
mathematics and text/hash operations were used; no code, mathematical
test, build, git operation or earlier-final edit was performed.
