# Complete-prefix collars at the ends of the second unselected plateau

Private written deduction, 11 November 2026. After the first summation
has been performed completely as the literal polynomial \(f_{44,N}\),
the second unselected plateau has a strict gap at both endpoints.
The exact Laurent degree transfers this gap to fixed short exterior
horizontal segments and transverse joins. The enlargement preserves
the original three-letter plateau coefficient.

The new regions are collars of the second plateau, not a continuation
over its whole period. Their widths may depend on the fixed actual
word and can be small. No estimate of a positive sum of the separate
rows of \(f_{44,N}\) is used.

## 1. Exact source and reference

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(443\) or \(444\). Its first three flags are
\((1,1,\beta)\), \(\beta\in\{0,1\}\). Keep the original coupled
reference \(r_j=a_j+ic_j\), following legs, logarithmic lifts and
ordinary incoming color \(w\). Put
\[
 \ell=11/50,\quad r=9/20,\quad P=[\ell,r],\quad
 \kappa_0=1/2500000,\qquad
 y=x+ic_2,\quad z=v+ic_3,\quad x,v\in P.
 \tag{1}
\]
In particular \(a_2\in P^\circ\) and \(c_2<0\). At \(m=4\) the
third conditional index is ordinary and its following external leg
is attached; the third factor is not replaced by a terminal cap.

For every \(N\ge2\), with \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), and
\(p_j(X)=(q_NX;q_N)_j\), retain
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i<N}H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j<N}
             X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon},\\
 f_N(w,Y)&=f_{44,N}(w,Y)\\
 &=N\operatorname{CT}_X
       [U_{1,N}(w,X)d_N(X)(1+X^{-N})C_{1,N}(X,Y)] .
\end{split}
\tag{2}
\]
The cap coefficient is complete. Both first Fourier terms are
inside \(f_N\). This is the exact normalization of
[pointwise prefix replacement](research_mixed_four_four_pointwise_prefix_replacement.md),
equations (2)--(5); in particular \(f_N\) has degree at most \(N-1\)
in \(w\) and \(Y\).

Write its exact decomposition as
\[
\begin{split}
 I_N(w,Y)&=N\int_{P+ic_1}
  U_{1,N}(w,e^{-2\pi ia})d_N(e^{-2\pi ia})
                       C_{1,N}(e^{-2\pi ia},Y)\,da,\\
 R_N(w,Y)&=f_N(w,Y)-I_N(w,Y).
\end{split}
\tag{3}
\]
The endpoints and heights in (3) are fixed. The notation for \(I_N\)
and \(R_N\) denotes their literal polynomials in \(Y\), not a
continuation inferred from a local packet.

Set \(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\) and define
\[
 \mathscr G_{A,N}(w;y,z)=A_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z),
                 \qquad A=f,I,R,
 \tag{4}
\]
\[
 D_{\beta,N}(Z)=
 \begin{cases}
  1,&\beta=0,\\
  |d_N(Z)|^{1/2},&\beta=1.
 \end{cases}
 \tag{5}
\]
There is no second selected monomial in (4). The first Fourier
sum is complete, and the second weight is the whole unselected
\(d_N(Y)\). The outgoing allocation (5) is retained even at zeros.

## 2. The complete product on the whole old second plateau

Use the original allocated phases
\[
 L_1=\mathcal T_1-\tfrac12g,\qquad
 \phi_2(a,y)=\psi_1(a,y)-\tfrac12g(a)-\tfrac12g(y),
\]
\[
 \phi_3(y,z)=\psi_\beta(y,z)-\tfrac12g(y)-\tfrac\beta2g(z).
 \tag{6}
\]
Here \(\psi_\epsilon\) is the original complete conditional
critical action, with its original constant. Put
\[
\begin{split}
 M_{12}&=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\},\\
 p_{12}&=\partial_2\phi_2(r_1,r_2),\\
 \gamma&=\min\{\kappa_0(a_1-\ell)^2,
                    \tfrac{\kappa_0}{2}(r-a_1)^2\}>0,\\
 \chi(x)&=\min\{\kappa_0(x-a_2)^2,\gamma\},\\
 \Lambda_{123}(z)&=M_{12}+\Re\phi_3(r_2,r_3)
                  +\Re\{\partial_2\phi_3(r_2,r_3)(z-r_3)\}.
\end{split}
\tag{7}
\]
The constant in the last line is the real part of
\[
 \mathcal T_1(r_1,-2)+\psi_1(r_1,r_2)+\psi_\beta(r_2,r_3)
             -g(r_1)-g(r_2)-\tfrac\beta2g(r_3).
 \tag{8}
\]
Thus (7) is the unchanged three-factor affine action. In particular
it agrees with the action used for the second selected sector.

Lemma 1 of
[complete-prefix safe-middle propagation](research_mixed_complete44_prefix_safe_middle.md)
gives, uniformly on \(P+ic_2\), the three full-prefix rates
\[
 |A_N(w,Y)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{B_\tau}
  e^{N\{M_{12}+\Re p_{12}(x-a_2)-\lambda_A(x)+\tau\}},
 \tag{9}
\]
where
\[
 \lambda_f=\chi,\qquad
 \lambda_I=\kappa_0(x-a_2)^2,\qquad \lambda_R=\gamma .
 \tag{10}
\]
These hold on sufficiently small fixed ordinary-color disks about
\(-2\), through both parities. No all-real-color extension is
asserted here.

Theorem 1 of the
[complete ordinary-source assembly](research_mixed_three_row_source_assembly.md)
applies to the actual third block, including its attached following
leg at \(m=4\). It gives
\[
\begin{split}
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)|^{1/2}D_{\beta,N}(Z)
 \le C_\tau N^{B_\tau}\exp N\{&
 \Re\phi_3(r_2,r_3)
 +\Re\partial_1\phi_3(r_2,r_3)(x-a_2)\\
 &+\Re\partial_2\phi_3(r_2,r_3)(v-a_3)
 -\kappa_0[(x-a_2)^2+(v-a_3)^2]+\tau\}.
\end{split}
\tag{11}
\]
This input includes every physical row, both zero-mode joins,
all aliases and endpoint corrections. The two halves at \(Y\)
in (9)--(11) give exactly the integer weight in (4).
The original stationary equation is
\[
             p_{12}+\partial_1\phi_3(r_2,r_3)=0.
 \tag{12}
\]
Multiplication, without division at zeros, therefore proves
\[
 |\mathscr G_{A,N}(w;x+ic_2,z)|D_{\beta,N}(Z)
 \le C_\tau N^{B_\tau}
 e^{N\{\Lambda_{123}(z)-\lambda_A(x)
                -\kappa_0(x-a_2)^2-\kappa_0(v-a_3)^2+\tau\}} .
 \tag{13}
\]
This is a bound for the complete prefix and complete next factor,
not for individual positive rows of either one.

## 3. Fixed exterior collars and transverse joins

Define the strictly positive constants
\[
 d=\min\{a_2-\ell,r-a_2\},\qquad
 \eta=\min\{\kappa_0d^2/4,\gamma\},
 \tag{14}
\]
and the two old endpoint intervals
\[
 J_L=[\ell,\ell+d/4],\qquad
 J_R=[r-d/4,r].
 \tag{15}
\]
Every \(x\) in their union has \(|x-a_2|\ge d/2\). Hence
the \(f\) case of (13) has loss at least \(2\eta\), as well as
the retained outgoing quadratic:
\[
 |\mathscr G_{f,N}(w;x+ic_2,z)|D_{\beta,N}(Z)
 \le C_\tau N^{B_\tau}
 e^{N\{\Lambda_{123}(z)-2\eta-\kappa_0(v-a_3)^2+\tau\}} .
 \tag{16}
\]

**Proposition 1.** There is a fixed \(\rho>0\), chosen before \(N\),
such that throughout the two complex neighborhoods
\[
 \operatorname{dist}(y,J_L+ic_2)\le2\rho
 \quad\hbox{or}\quad
 \operatorname{dist}(y,J_R+ic_2)\le2\rho
 \tag{17}
\]
one has
\[
 |\mathscr G_{f,N}(w;y,z)|D_{\beta,N}(Z)
 \le C N^B
   e^{N\{\Lambda_{123}(z)-\eta-\kappa_0(v-a_3)^2\}},
       \qquad z=v+ic_3,\quad v\in P .
 \tag{18}
\]
The constants and a common fixed ordinary-color disk are independent
of \(N,v\). Fixed derivatives in \(y\), and in \(w\) on a smaller
color disk, satisfy the same rate on the neighborhoods with \(\rho\)
in place of \(2\rho\).

*Proof.* The exact \(Y\)-band of the holomorphic expression
\(\mathscr G_{f,N}\) is contained in
\[
                         [-N+1,\,2N-2].
 \tag{19}
\]
Indeed \(f_N\) and \(d_N\) have degree at most \(N-1\), while
each row \(Y^{-j}p_j(Y)p_j(Z)\) of \(C_{\beta,N}\) has \(Y\)-band
\([-j,0]\). This proof uses the complete finite polynomial,
including all revived rows.

Choose the source allowance in (16) smaller than \(\eta/4\),
and fix a closed color disk inside the corresponding input disk.
For fixed \(z,w\), multiply that Laurent polynomial by the
nonnegative constant \(D_{\beta,N}(Z)\). It is still a Laurent
polynomial in \(Y\) with band (19), even when the multiplier is
zero. Its real bound is (16). Apply the finite-cover argument
and equation (8) in the proof of Theorem 1 of
[horizontal complex continuation](research_mixed_horizontal_complex_extension.md)
separately to the two nondegenerate intervals (15), with rate
\(\Lambda_{123}(z)-2\eta-\kappa_0(v-a_3)^2\) and a total
allowance smaller than \(\eta\). The parameters \(v\) and \(w\)
range over compact sets. This theorem requires no holomorphic
dependence on their labels for the bound.
Its proof uses only the one source allowance already fixed;
there is no requirement that the color disk stay unchanged as
that allowance is sent to zero.

The theorem first chooses small real covering intervals and a
fixed ellipse parameter, then obtains a positive complex radius.
Its cost is fixed before \(N\), not inferred by continuation from
one point. Taking a smaller common radius gives (17)--(18).
We may also require
\[
              \rho<\min\{d/16,\,-c_2/4,\,\ell/4,\,(1-r)/4\}.
 \tag{20}
\]
Cauchy's formula gives the stated derivatives. In the color
variable it is applied on a fixed slightly larger input disk.
The multiplier (5) is independent of \(y,w\) and is never
divided out or differentiated. This proves the proposition.
\(\square\)

In particular (18) pays both new exterior horizontal pieces
\[
 [\ell-\rho,\ell]+ic_2,\qquad [r,r+\rho]+ic_2.
 \tag{21}
\]
It also pays vertical joins of length at most \(\rho\) at their
outer endpoints and at the original endpoints. More generally,
any fixed finite-length path in the neighborhoods with radius
\(\rho\) is paid with the same exponential rate. Its original
density \(N\,dy\) adds only a polynomial factor. This is a
complete-source estimate on genuinely new second-coordinate
pieces.

## 4. The enlarged second plateau has the original packet

Let
\[
\begin{split}
 \mathcal J_N(w,z)
 &=N\int_{P+ic_2}\mathscr G_{f,N}(w;y,z)\,dy,\\
 \widetilde{\mathcal J}_N(w,z)
 &=N\int_{[\ell-\rho,r+\rho]+ic_2}
                              \mathscr G_{f,N}(w;y,z)\,dy,\\
 I_{123,N}(w,z)
 &=N\int_{P+ic_2}\mathscr G_{I,N}(w;y,z)\,dy .
\end{split}
\tag{22}
\]
All intervals have increasing-real orientation. Each expression
is a polynomial of degree at most \(N-1\) in \(w,Z\). The first
two integrate the literal complete first-period message; the
last reinserts the original first plateau (3).

Linearity gives the exact decomposition
\[
 \widetilde{\mathcal J}_N-I_{123,N}
 =N\int_{P+ic_2}\mathscr G_{R,N}\,dy
   +N\int_{([\ell-\rho,\ell]\cup[r,r+\rho])+ic_2}
                                      \mathscr G_{f,N}\,dy .
 \tag{23}
\]
The two exterior intervals in (23) are both oriented to the right.
The first term has gap \(\gamma\) by (13); the second has gap
\(\eta\) by Proposition 1. Since \(\eta\le\gamma\), for every
prescribed \(\tau>0\),
\[
 |\widetilde{\mathcal J}_N(w,z)-I_{123,N}(w,z)|
                  D_{\beta,N}(Z)
 \le C_\tau N^{B_\tau}
 e^{N\{\Lambda_{123}(z)-\eta-\kappa_0(v-a_3)^2+\tau\}} .
 \tag{24}
\]
The same assertion for \(\mathcal J_N-I_{123,N}\) has the
possibly larger gap \(\gamma\).

The integral \(I_{123,N}\) is exactly the three-letter instance
of equation (8) in
[retained-prefix calibration](research_mixed_retained_prefix_unselected_plateau.md),
at the actual following leg of this word. The identity includes
the original \(N^2\,da\,dy\) density and both full internal
diagonal polynomials. Its phase is
\[
 \mathcal P_{44(3+\beta)}(w,z)
  =\operatorname{stat}_{a,y}
    [\mathcal T_1(a,w)+\psi_1(a,y)+\psi_\beta(y,z)-g(a)-g(y)]
 \tag{25}
\]
on the original critical branch. In particular
\[
 \Lambda_{123}(r_3)+\tfrac\beta2\Re g(r_3)
              =\Re\mathcal P_{44(3+\beta)}(-2,r_3).
 \tag{26}
\]
There is no terminal correction inserted into (25).
The conditional/pre-Gram correction, when \(\beta=0\), is
already the one in equation (17) of retained-prefix calibration.

Its theorem supplies on a fixed neighborhood of \((-2,r_3)\)
the nonzero packet
\[
 I_{123,N}(w,z)
 =N^{-3-\beta/2}\mathcal A_{44(3+\beta)}(w,z)
   e^{N\mathcal P_{44(3+\beta)}(w,z)}
       (1+O_{\rm hol}(N^{-1})),\qquad
                      \mathcal A_{44(3+\beta)}\ne0 .
 \tag{27}
\]
This is the conditional-prefix normalization. Its two densities
are \(N^2\,da\,dy\); no original whole-word exterior scalar has
been changed.
The actual first44 inverse condition and the ordinary/attached
following roles are exactly those verified in pointwise prefix
replacement; at \(m=4\) the final following leg is attached,
which the retained-prefix theorem permits.

**Corollary 2.** Both integrals \(\mathcal J_N\) and
\(\widetilde{\mathcal J}_N\) have the same packet (27), with its
original action, nonzero coefficient, power and branches, on
smaller fixed neighborhoods of \((-2,r_3)\).

*Proof.* If \(\beta=0\), the multiplier (5) is one. If \(\beta=1\),
the outgoing third plateau lies in
\(0<\Re z<1/2,\Im z<0\). The strict criterion in
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md),
Theorem 1 and equation (22), makes this particular outgoing
\(d_N(Z)\) zero-free for large \(N\), with
\[
 d_N(e^{-2\pi iz})=
 N^{-1/2}\mathcal D(z)e^{-Ng(z)}(1+O(N^{-1})),\qquad
                             \mathcal D(z)\ne0 .
 \tag{28}
\]
Remove only this proved outgoing modulus half from (24).
The resulting continuous rate is
\[
 B(v)=\Lambda_{123}(v+ic_3)+\tfrac\beta2\Re g(v+ic_3),
 \qquad
 |\widetilde{\mathcal J}_N-I_{123,N}|
 \le \operatorname{poly}(N)e^{N(B(v)-\eta+\tau)} .
 \tag{29}
\]
The polynomial factor includes \(N^{\beta/4}\). For \(\beta=0\)
the same formula has no division and no such factor.

The difference in (29) is a polynomial of degree at most \(N-1\)
in \(Z\). Fix its source allowance and color disk first, and
apply the same finite-cover continuation proof with a separately
reserved allowance, treating \(w\) on a smaller compact color
disk as a parameter. By (26), \(B(a_3)\) is the real part of
the original action at complete color. Shrink the color and
outgoing disks so that the difference between \(B(v)\) at the
nearby horizontal anchor and
\(\Re\mathcal P_{44(3+\beta)}(w,z)\) is smaller than \(\eta/8\).
Allocate less than \(\eta/8\) each to the source and continuation
errors. After absorbing the polynomial, the normalized error
is \(O(e^{-\eta N/4})\) on these disks. Cauchy's formula gives
all fixed normalized derivatives on smaller disks.

Adding this exponentially small difference to (27) preserves
its original coefficient and relative \(O_{\rm hol}(N^{-1})\)
error. The proof for \(\mathcal J_N\) is identical, using its
gap \(\gamma\). No other source factor or internal Fourier
polynomial has been divided out. \(\square\)

The same conclusion holds if either added segment in (22) is
replaced by any fixed finite-length connector within its paid
endpoint neighborhood. The difference remains bounded by (18).

## 5. Exact limitation

This result completes the first period, retains the whole second
unselected plateau, and adds fixed exterior collars and short
joins at its two endpoints. It does not reach the real axis
from height \(c_2\), pay the distant second real arcs, or
complete either second Fourier period. The radius in (20) can
be small because the inherited \(\gamma\) can be small.

In particular, the separate selected estimate at height \(H>0\)
does not by itself give the missing vertical connection. Writing
\(\mathscr G_1(y)=\mathscr G_0(y)Y^{-N}\), one has exactly
\[
             |\mathscr G_0(x+iH)|
                  =e^{2\pi NH}|\mathscr G_1(x+iH)|.
 \tag{30}
\]
A selected gap cannot be transferred to the unselected entire
product while dropping this factor. No such interpolation,
whole-period inference or general operator norm is asserted here.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_prefix_safe_middle.md | 267f567ac50ff87ad738a5ac260a9d525a021eafcf566221667d5beaa7447913 |
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_retained_prefix_unselected_plateau.md | 4f8be2ee4fd0aceda28ad4d96bb4b57d864765438183563c34db070823d6d72b |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The author read back the complete proof and all six directly used
source implications, and checked their hashes. Independent full proof
and direct-source review is required before adoption. No mathematical
numerical evaluation, saved-value arithmetic, test, import,
compilation or frozen-source edit is used.
