# A finite-branch period for the entire prescribed twist exterior

Private written proof, 14 November 2026. An arbitrary original exterior
can be contracted with a full twist before its Fourier charges are
regrouped. The result is exactly \(2|p|\) ordinary improper Fresnel
integrals, with the original exterior derivative and normal sawtooth
both retained. The original circle half weight makes their boundary
terms vanish. No analytic packet estimate or positivity assumption on
the exterior is needed for this identity.

This is a source-preserving composition formula, not a nonvanishing
theorem for its resulting period. In particular, the nonzero integer
charge at a local saddle does not prove a nonzero exterior amplitude
or a nonzero intersection with the original integration cycle.

## 1. Entire original exterior and its complete-color half weight

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and
\(\kappa=q^{d^2/2}\), with this logarithm. Let
\(p\in\mathbb Z\setminus\{0\}\). Keep the full original pair Casimir,
the original crossing \(R=\kappa r_N(\Omega)\), and the actual
ordinary-circle operators
\[
 L_j=(-1)^{j-1}U_{j-1}(\Omega/2),\qquad 1\le j\le N.
 \tag{1}
\]

Let \(\Lambda\) be the prescribed exterior contraction in this slot.
It may be scalar, vector, or operator valued. All other physical
tensors, ordering, cups, caps, pivots, and the marked closing row
remain in \(\Lambda\). Define
\[
 A_j=\Lambda(L_j),\quad
 Z_{N,p}=\Lambda(R^{2p}),\quad
 c_h=A_{N-h}\ (0\le h\le d),\quad c_{-h}=c_h.
 \tag{2}
\]
The last equality merely defines a reflected copy of the same
physical color list. It adds no hypothesis or new exterior state.
For example a retained half twist and an actual turn can be included
in the linear map \(\Lambda\), in their original order.

Let \(a_n,\beta_j\) be the full Hermite/Chebyshev and circle
coefficients of \(f_p=\operatorname{rem}(r_N^{2p})\), as in
[the original twist kernel](actual_twist_circle_fourier_kernel.md).
Then
\[
 Z_{N,p}=\kappa^{2p}\sum_{j=1}^{N}\beta_{j-1}A_j.
 \tag{3}
\]
No component-dependent or framing scalar is changed in (3).
Any scalar recorded outside the slot and outside \(\Lambda\) simply
multiplies every equality below.

The exact entire circle kernel \(K_p(h)\) in
[the coherent Gaussian source](actual_coherent_filling_gaussian_chirp.md),
Section 6, satisfies
\[
 K_p(h)=K_p(-h),\qquad
 \beta_{N-h-1}=K_p(h)\ (1\le h\le d),\qquad
 \beta_{N-1}=\tfrac12K_p(0).
 \tag{4}
\]
Consequently
\[
 \sum_{j=1}^{N}\beta_{j-1}A_j
       =\frac12\sum_{h=-d}^{d}K_p(h)c_h.
 \tag{5}
\]
This retains all physical colors, including the original half weight
at the complete color. There is no color-corridor cutoff.

Introduce the entire finite Fourier polynomial
\[
 F_N(z)=\sum_{h=-d}^{d}c_h e^{2\pi i h z},\qquad
 E_N(z)=\sinh(2\pi i z)F_N(z).
 \tag{6}
\]
Both functions are \(1\)-periodic. The first is even and the second
is odd. In particular
\[
 E_N(\tfrac12)=E_N(-\tfrac12)=0,\qquad
 E_N'(\tfrac12)=E_N'(-\tfrac12)
                   =-2\pi iF_N(\tfrac12).
 \tag{7}
\]
These statements use integer physical colors and the exact
circle difference, not a chosen continuation of an asymptotic packet.

## 2. Exact charge period and its convergence

Put
\[
 U_N(z)=e^{2\pi i pN z^2}E_N(z),\qquad
 z_k=(k+\tfrac12)/N-\tfrac12.
 \tag{8}
\]
The literal full-normal kernel gives
\[
 \sum_{j=1}^{N}\beta_{j-1}A_j
       =\frac{(-1)^d\kappa^{-p}}{2\pi iN^2}
                               \sum_{k=0}^{N-1}U_N'(z_k).
 \tag{9}
\]
This is the exact sampled derivative identity in
[the source Fourier theorem](actual_filling_source_fourier_endpoint_gap.md),
Section 4. Its proof is direct: the derivative of the chirp supplies
the unwrapped normal weight \(2pNz\); the derivative of \(F_N\)
supplies the original color weight \(h\); and the derivative of
sinh supplies cosh. These are precisely the three terms of the
original entire circle kernel. Formula (5) fixes the factor \(1/2\).

Equations (7)--(8) give \(U_N(\pm1/2)=0\) and
\(U_N'(1/2)=U_N'(-1/2)\). Thus its periodic extension is \(C^1\)
and piecewise smooth. Its Fourier coefficients satisfy
\(\widehat U_N(k)=O_{N,\Lambda,p}(|k|^{-3})\): two integrations
by parts have zero boundary terms, and a third leaves a bounded
endpoint term and an integrable derivative. Equivalently the
periodic derivative \(U_N'\) has absolutely summable Fourier
coefficients.

Exact midpoint Fourier selection in (9), followed by one integration
by parts using \(U_N(\pm1/2)=0\), proves the full physical identity
\[
 \boxed{
 Z_{N,p}=(-1)^d\kappa^p
  \sum_{m\in\mathbb Z}(-1)^{dm}m
    \int_{-1/2}^{1/2}
      e^{2\pi iN(pz^2-mz)}E_N(z)\,dz .}
 \tag{10}
\]
The zero-charge term is exactly zero. The series is absolutely
convergent at every fixed \(N\), since its terms are
\(m\widehat U_N(Nm)=O_{N,\Lambda,p}(|m|^{-2})\).
These constants may grow with \(N\); no exponential estimate follows
from this fixed-level convergence.

## 3. Fold all charges into \(2|p|\) source branches

Use
\[
 s(u)=\tfrac12-\{u\}\quad(u\notin\mathbb Z),\qquad s(u)=0
       \quad(u\in\mathbb Z).
 \tag{11}
\]
For \(0\le r<2|p|\) put
\[
 \alpha_r=\frac{r}{2p},\qquad B_r=\frac12-\alpha_r,\qquad
 \chi_r=(-1)^{dr}e^{-\pi iNr^2/(2p)},
 \tag{12}
\]
and define the periodic real-line amplitude
\[
 \mathcal A_{N,r}(v)=
       \frac{E_N'(v+\alpha_r)}{2\pi iN}
       +2p\,s(B_r-v)E_N(v+\alpha_r).
 \tag{13}
\]
Although the sawtooth jumps, \(\mathcal A_{N,r}\) is continuous:
at every jump \(v=B_r-k\), its factor
\(E_N(v+\alpha_r)=E_N(1/2-k)\) is zero.
It is piecewise analytic, with bounded derivatives on each unit
interval at a fixed \(N\).

**Theorem.** For every prescribed exterior in (2),
\[
 \boxed{
 Z_{N,p}=(-1)^d\kappa^p
   \sum_{r=0}^{2|p|-1}\chi_r
       \int_{\mathbb R}
          e^{2\pi i pNv^2}\mathcal A_{N,r}(v)\,dv .}
 \tag{14}
\]
Each integral is an ordinary oscillatory improper integral: its
positive and negative halves converge separately. A symmetric
principal-value prescription is therefore unnecessary in (14).
Every \(\chi_r\) is an explicit unit. No gcd or parity restriction,
division by a Gauss sum, or replacement closing functional occurs.

*Proof.* Regroup the absolutely convergent series (10) as
\(m=r+2pk\), \(k\in\mathbb Z\). This parametrizes all integers for
either sign of \(p\). Complete the square by
\[
 z=v+\frac{m}{2p}=v+\alpha_r+k.
 \tag{15}
\]
Its scalar factor is
\[
 (-1)^{dm}e^{-\pi iNm^2/(2p)}=\chi_r.
 \tag{16}
\]
Indeed changing \(m\) by \(2p\) changes the right expression before
simplification by
\((-1)^{2pd}e^{-2\pi iNm-2\pi iNp}=1\).
The original interval becomes
\([B_r-1-k,B_r-k]\). Periodicity gives
\(E_N(z)=E_N(v+\alpha_r)\). These intervals tile \(\mathbb R\);
on their interiors \(k=\lfloor B_r-v\rfloor\), so the original
integer charge is
\[
 m=r+2pk=-2pv+2p\,s(B_r-v).
 \tag{17}
\]
This retains the charge rather than replacing it by its stationary
value.

On every complete tile the boundary term in the following integration
by parts is exactly zero, by (7):
\[
 \begin{split}
 &\int_{B_r-1-k}^{B_r-k}
      (-2pv)e^{2\pi ipNv^2}E_N(v+\alpha_r)\,dv\\
 &\qquad=
 \frac1{2\pi iN}\int_{B_r-1-k}^{B_r-k}
              e^{2\pi ipNv^2}E_N'(v+\alpha_r)\,dv.
 \end{split}
 \tag{18}
\]
Thus the charge integral on this tile becomes exactly the tile
integral of (13). There is no discarded endpoint or jump term:
the displayed zero is the original sinh zero, including the
complete-color half weight used in (9).

By (10), the sum of the absolute values of these tile integrals
converges. Hence the sums along the positive and negative tiles
converge separately. For arbitrary real cutoffs, the omitted partial
last tile has integral \(O_{N,\Lambda,p}(|v|^{-1})\). To see this,
split at a possible sawtooth boundary and integrate the Gaussian
once by parts; \(\mathcal A_{N,r}\) is bounded and has uniformly
bounded variation on a unit interval. Thus partial last tiles tend
to zero. This proves ordinary improper convergence and (14).
\(\square\)

## 4. Remaining boundary variables and exact composition

At a fixed \(N\), (14) is linear in the finite list \(A_1,\ldots,A_N\).
It therefore holds in any finite-dimensional space of original
boundary coefficients, including the ordinary polynomial space
obtained by keeping free incidences separate before identifying
their variables. It does not reduce those polynomials modulo the
Casimir relation at an already shared free vertex.

If the prescribed exterior depends holomorphically on further
parameters, its finite coefficients \(A_j\) do also. On compact
parameter sets the tile convergence and partial-tile bounds above
are uniform, because only finitely many \(A_j\) and their bounded
linear combinations occur. Consequently every branch in (14) is
holomorphic in those parameters. Fixed ordinary boundary derivatives
commute with the identity. The full external Hermite and prescribed
boundary-normal observations are retained in the same way. These
are derivatives in retained exterior variables at the fixed root;
no off-root quantum-parameter lift of (14) is asserted.

Several fixed twist slots may be replaced successively by (14).
Equivalently use iterated improper integrals or coefficientwise
rectangular limits. The intermediate exteriors remain their actual
finite-dimensional tensor contractions. This does not require an
absolute multiple integral and does not commute neighboring physical
Casimirs or move a quarter-turn through multiplication.

The theorem does not make the sawtooth a holomorphic function of
\(v\). Its branch amplitudes remain piecewise analytic in that
integration variable. Any complex contour deformation must keep
the joins between these pieces and their derivative data.

## 5. What its local saddle multiplier says

On a single open real tile, analytically continue the corresponding
linear expression for the sawtooth. The integer
\(m=r+2pk\) labels that tile. If, on a neighborhood of a proposed
critical point, a genuine exterior packet has
\[
 E_N(z)=N^\mu e^{N\Psi(z)}
                    [A(z)+O(N^{-1})]
 \tag{19}
\]
uniformly holomorphically, set
\[
 T_r(v)=2\pi ip v^2+\Psi(v+\alpha_r).
 \tag{20}
\]
The leading amplitude in (13), after extracting
\(N^\mu e^{N\Psi}\), is exactly
\[
 \left[m+\frac{T_r'(v)}{2\pi i}\right]A(v+\alpha_r).
 \tag{21}
\]
Indeed \(2p\,s(B_r-v)=m+2pv\) on this tile, and the
exterior derivative in (13) supplies \(\Psi'/(2\pi i)\).
At a stationary point the multiplier is therefore
\(mA(v+\alpha_r)\), the original charge and original exterior
amplitude. The derivative of \(A\) contributes at the next order.
This is a conditional evaluation of the exact source formula, not
an assumption that (19) holds for an arbitrary component.

There is also an exact identity on each tile, before any packet
assumption:
\[
 e^{2\pi ipNv^2}\mathcal A_{N,r}(v)
 =m e^{2\pi ipNv^2}E_N(v+\alpha_r)
  +\frac1{2\pi iN}\frac{d}{dv}
        [e^{2\pi ipNv^2}E_N(v+\alpha_r)].
 \tag{22}
\]
The \(r=0\) central tile is the original \(m=0\) term. Its entire
integral is zero by (7) and (22), even if the derivative density is
pointwise nonzero. Thus an isolated \(m=0\) stationary Gaussian would
miss the total-derivative source structure. For \(m\ne0\), the known
integer factor is nonzero, but \(A\), its saddle accessibility,
and cancellation with other tiles or branches still require proof.
The exact compression supplies none of those missing assertions.

The source Fourier endpoint theorem already controls those joins
under its stated uniform analytic packet and gap hypotheses. Formula
(14) does not weaken those hypotheses by itself. Its new content is
the exact finite-branch representation of an arbitrary prescribed
whole exterior, with ordinary improper convergence and every
normal derivative retained, before any such estimate is assumed.

## Direct source versions

The arguments use written mathematics only. Source versions are
recorded after full reads of the identities used above.

- actual_twist_circle_fourier_kernel.md:
  1d93f6f13d271c56eee6e7ea8ddf5b9ea0eea92a2076ede7068df552bab94292.
- actual_coherent_filling_gaussian_chirp.md:
  d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522.
- actual_filling_source_fourier_endpoint_gap.md:
  1f03f69212b1fee6dceb6315b9582acb56aa647e4893ee3483113eff142ad982.
