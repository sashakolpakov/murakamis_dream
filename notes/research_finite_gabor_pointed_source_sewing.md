# Finite Gabor seams for the original pointed meridian source

Private written proof, 19 November 2026.

This note gives a finite packet expansion of the original all-width
pointed source, including its two pivotal carrier shifts and its true
meridian normals. Every physical occupation, closing factor, and
partial-label current remains. The complete seam sum removes the
additional packet damping exactly; a selected packet estimate is
therefore not a noncancellation estimate for the complete source.

The sole complete proof direct is J, pinned below. The earlier
research_gaussian_frame_newton_transport.md already gives a continuous
Gaussian resolution, exact Newton-word composition, and original
boundary functions. It also retains the inverse frame operator under
weights. The frame principle is not new here. The present calculation
records the finite all-width pointed closing row, its meridian
connection and relative Laurent terms, and its exact seam cancellation.
No assertion from that coverage note is used as a proof premise.

## 1. Physical space and a finite auxiliary frame

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(r\ge1\), \(m=r+1\), and \(x_0=-q^{-1}\). The physical remaining
space is \(U=V_N^{\otimes r}\), with occupation basis
\(e_{\mathbf n}\), \(0\le n_i\le d\). Write
\[
 J_{\rm occ}e_{\mathbf n}=|\mathbf n|e_{\mathbf n},\qquad
 K_0=x_0^rQ^{-J_{\rm occ}},\qquad
 K_{\rm r}(M)=M^rK_0,\qquad
 K_0^N=\varepsilon I,\quad \varepsilon=(-1)^{(N+1)r}.
 \tag{1}
\]
These are finite matrices. The last identity will only be used on
this physical space, never at a continued classical clock argument.

Choose any fixed Euclidean-unit vector \(g\in V_N\). One useful
choice, with \(0\le L<N\), is
\[
 g(n)=\frac{2^{-L}\binom Ln}{\nu_L}\quad(0\le n\le L),\qquad
 g(n)=0\quad(L<n<N),\qquad
 \nu_L^2=4^{-L}\binom{2L}L .
 \tag{2}
\]
The normalization follows by taking the coefficient of \(z^L\)
in \((1+z)^L(1+z)^L\). Define auxiliary cyclic translations and
modulations
\[
 (T_ag)(n)=g(n-a\bmod N),\qquad
 (M_sg)(n)=Q^{sn}g(n),\qquad
 g_{a,s}=M_sT_ag,\quad a,s\in\mathbb Z/N.
 \tag{3}
\]
Only these auxiliary labels and translations are cyclic. A physical
raising arrow at occupation \(d\) is not replaced by a wrap arrow.
For (2) all wrapped windows are included in (3), with their literal
entries; the unwrapped center is \(a+L/2\).

The exact identity is
\[
 \frac1N\sum_{a,s}|g_{a,s}\rangle\langle g_{a,s}|=I_{V_N}.
 \tag{4}
\]
Indeed its \(n,k\) entry is
\[
 \frac1N\sum_sQ^{s(n-k)}
       \sum_a g(n-a)\overline{g(k-a)}
 =\delta_{nk}\sum_a|g(n-a)|^2=\delta_{nk}.
 \tag{5}
\]
The star in this calculation is the fixed occupation-coordinate
Euclidean dual. It does not change the ordinary matrix trace or
replace J's coherent metric.

Choose one such window on each head, set
\(\Psi_\lambda=\bigotimes_i g^{(i)}_{a_i,s_i}\), and let
\(\mathcal L=(\mathbb Z/N)^{2r}\). Tensoring (4) gives
\[
 N^{-r}\sum_{\lambda\in\mathcal L}
       |\Psi_\lambda\rangle\langle\Psi_\lambda|=I_U.
 \tag{6}
\]
For an invertible diagonal holomorphic matrix \(D(M)\), the
corresponding exact resolution is
\[
 N^{-r}\sum_\lambda
 D(M)|\Psi_\lambda\rangle\langle\Psi_\lambda|D(M)^{-1}=I_U.
 \tag{7}
\]
Its row is the analytic algebraic row
\(\Psi_\lambda^*D(M)^{-1}\). It is generally not the Hermitian
dual of \(D(M)\Psi_\lambda\). The windows in (2)--(7) are fixed
in \(M\); no complex conjugation of a moving meridian is introduced.

## 2. Exact open and closed words, including the pivotal carriers

Let \(B(M)=X_L(M)\cdots X_1(M)\), \(L\ge1\), be a literal
factorization on \(U\). Factors may include actual reduced
crossings, their scalars, turns, and prescribed framing coupons.
In particular \(\kappa(M)\) and the prescribed zero-framing factor
remain in \(B\). For seam frames \(D_0,\ldots,D_L\),
put
\[
 Y_j=D_j^{-1}X_jD_{j-1},\qquad
 \widetilde v=D_0^{-1}v,\qquad \widetilde\ell=\ell D_L.
 \tag{8}
\]
There is no commutation assumption on the \(X_j\)'s. Direct insertion
of (6) at the \(L-1\) internal seams gives
\[
 \begin{split}
 \ell Bv={}&N^{-r(L-1)}
 \sum_{\lambda_1,\ldots,\lambda_{L-1}}
 (\widetilde\ell Y_L\Psi_{\lambda_{L-1}})
 \prod_{j=2}^{L-1}
   (\Psi_{\lambda_j}^*Y_j\Psi_{\lambda_{j-1}})
 (\Psi_{\lambda_1}^*Y_1\widetilde v).
 \end{split}
 \tag{9}
\]
For \(L=1\) this means \(\widetilde\ell Y_1\widetilde v\), with
no inserted resolution. Thus the original open boundary vectors,
rather than arbitrarily chosen packets, are retained. On a tensor
network the coefficient is \(N^{-E}\), where \(E\) is the number
of resolved one-head internal edges.

For a closed word choose \(D_L=D_0\). Define
\[
 \mathcal T_\sigma(B)=\operatorname{Tr}(K_0^\sigma B),
                       \qquad \sigma\in\{+1,-1\}.
 \tag{10}
\]
The literal Cartan action is
\[
 K_0^\sigma\Psi_{\mathbf a,\mathbf s}
 =x_0^{\sigma r}\Psi_{\mathbf a,\mathbf s-\sigma\mathbf1},
 \qquad
 \Psi_{\mathbf a,\mathbf s}^*K_0^\sigma
 =x_0^{\sigma r}\Psi_{\mathbf a,\mathbf s+\sigma\mathbf1}^*.
 \tag{11}
\]
The coefficient in the row is \(x_0^{\sigma r}\), not its
conjugate: this is multiplication of a fixed row by the matrix
\(K_0^\sigma\). Since \(D_0\) is diagonal it commutes with \(K_0\).
Consequently the exact closed formula is
\[
 \boxed{\begin{split}
 \mathcal T_\sigma(B)
 ={}&x_0^{\sigma r}N^{-rL}
 \sum_{\lambda_0,\ldots,\lambda_{L-1}}
 \bigl(\Psi_{\mathbf a_0,\mathbf s_0+\sigma\mathbf1}^*
             Y_L\Psi_{\lambda_{L-1}}\bigr)\\
 &\hspace{10mm}\cdot
 \prod_{j=1}^{L-1}
       \bigl(\Psi_{\lambda_j}^*Y_j\Psi_{\lambda_{j-1}}\bigr).
 \end{split}}\tag{12}
\]
For \(L=1\) the first factor contains \(Y_1\Psi_{\lambda_0}\).
There are \(L\), not \(L+1\), resolutions. A choice \(D_L\ne D_0\)
leaves the actual closing coupon \(D_0^{-1}D_L\); it cannot be
reset by identifying the two seam labels.

For clarity about half-clock marks, let \(W e_n=e_{d-n}\).
For the symmetric window (2), direct substitution gives
\[
 Wg_{a,s}=Q^{sd}g_{d-a-L,-s}.
 \tag{13}
\]
The equality uses the periodic extension of
\(g(t)=g(L-t)\). A diagonal \(q^{J_{\rm occ}}\) gives instead the
literal entries \(q^nQ^{sn}g(n-a)\) on a head. This is a marked
half-frequency frame, not a reset integer modulation:
\(q^N=-1\). The corresponding inverse must remain in the dual
row, as in (7). Arbitrary balanced turnover coefficients are
similarly retained as actual matrices. Formula (12) requires
only the integer Cartan shifts (11), not an identification of
all other closing coupons with those shifts.

## 3. The original pointed meridian functional

Let \(W(M)\) be an actual analytic total intertwiner in J, and
\(B(M)=q_F(M)W(M)i_F(M)\) its actual reduced matrix. J(21)
identifies the original highest-cut and pivotal functional:
\[
 \Phi_0(W(M))
 =\operatorname{Tr}_V((P_0\otimes K_{\rm r}^{1-N})W(M))
 =D_N(M)\operatorname{Tr}_U(H(M)^{-1}B(M)),
 \tag{14}
\]
where \(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\) and
\(H(M)=D_N(M^mK_0)\). By the physical identity (1),
\[
 H(M)^{-1}
 =\frac{M^mK_0-M^{-m}K_0^{-1}}
        {\varepsilon(M^{mN}-M^{-mN})}.
 \tag{15}
\]
The equality holds on the punctured meridian germ and with its
prescribed continuation. Combining (12)--(15) gives
\[
 \boxed{\displaystyle
 \Phi_0(W(M))
 =\frac{D_N(M)}
 {\varepsilon(M^{mN}-M^{-mN})}
 \left[M^m\mathcal T_+(B(M))-M^{-m}\mathcal T_-(B(M))\right].
 }\tag{16}
\]
Thus the all-width packet source has the exact coefficient
\(N^{-rL}\) and two opposite closing carrier shifts, with the
displayed original prefactor. Neither a normalized trace nor a
positive packet norm has replaced the source.

Put \(\mu=\Log M\), and \(B_j=\partial_\mu^jB(e^\mu)|_{\mu=0}\).
Analyticity of the left side of (14) implies
\[
 \mathcal T_+(B_0)=\mathcal T_-(B_0).
 \tag{17}
\]
Expanding \(D_N(e^\mu)=N+O(\mu^2)\) and the denominator in
(16) now gives the original first-jet row
\[
 \boxed{\displaystyle
 \Phi_0(W(1))
 =\frac{\mathcal T_+(B_0)+\mathcal T_-(B_0)}{2\varepsilon}
 +\frac{\mathcal T_+(B_1)-\mathcal T_-(B_1)}
             {2\varepsilon m}.
 }\tag{18}
\]
Every \(B_j\) is a true fixed-\(q\) meridian derivative, including
the derivatives of crossing scalars, framing, and the actual
quotient maps. Equations (17)--(18) are not imposed on an arbitrary
inserted mark which is not covered by (14).

All occupations remain physically capped. If \(P_T\) denotes
the actual integer-degree projection, \(0\le T\le rd\), then
\[
 N^{-r}\sum_\lambda
 P_T|\Psi_\lambda\rangle\langle\Psi_\lambda|P_T=P_T.
 \tag{19}
\]
There is no normalization of the projected vectors; in general
they are no longer products of one-head packets. When \(B\)
preserves degree, (16) is the sum of these exact sector traces,
with \(K_0|_{U_T}=x_0^rQ^{-T}\). For an actual braid word,
J(30b)--(30d) supplies the removable paired sector contributions.
Degree preservation alone does not imply that reciprocity.
An individual sector or
partial label set need not have a removable source term. No
noninteger degree projection is defined here.

## 4. Moving frames and restricted meridian currents

Write \(A_j=D_j^{-1}\partial_\mu D_j\). Differentiating the actual
matrices (8), without differentiating the fixed packet rows, gives
\[
 \partial_\mu Y_j
 =D_j^{-1}(\partial_\mu X_j)D_{j-1}
       -A_jY_j+Y_jA_{j-1}.
 \tag{20}
\]
In the complete product every adjacent connection cancels:
the contribution \(Y_{j+1}A_jY_j\) from \(Y_{j+1}'\) cancels
the contribution \(-Y_{j+1}A_jY_j\) from \(Y_j'\).
The two endpoint terms are \(-A_LY_L\cdots Y_1+
Y_L\cdots Y_1A_0\). For a closed seam they form a commutator.
Cyclicity and \([A_0,K_0]=0\) make its pivotal trace zero.
For an open word they cancel with the derivatives of the two
boundary adapters in (8). All actual \(X_j'\) remain.

For a fixed subset \(\Lambda\subset\mathcal L\), put
\[
 Q_\Lambda=N^{-r}\sum_{\lambda\in\Lambda}
 |\Psi_\lambda\rangle\langle\Psi_\lambda|,\qquad
 P_\Lambda(M)=D(M)Q_\Lambda D(M)^{-1}.
 \tag{21}
\]
The matrix \(Q_\Lambda\) is a positive contraction, but need not
be idempotent. Its similarity need not be Hermitian. Exactly,
\[
 \partial_\mu P_\Lambda
 =[\partial_\mu D\,D^{-1},P_\Lambda].
 \tag{22}
\]
If an internal identity is replaced by \(Q_\Lambda\), the two
terms in the preceding cancellation leave
\(Y_{j+1}[A_j,Q_\Lambda]Y_j\). Equivalently this is the
moving-window current (22) in physical coordinates. Thus
normal connection cancellation belongs to the complete resolution,
not to a selected collection of labels.

For example, replacing \(B\) by a partially resolved analytic
matrix \(B^\Lambda\) in the right side of (16) defines an exact
meromorphic marked expression. Its residue is
\[
 \frac{\mathcal T_+(B^\Lambda_0)
                  -\mathcal T_-(B^\Lambda_0)}
                  {2\varepsilon m}.
 \tag{23}
\]
The complementary label terms cancel this residue when the
complete expression returns to (14). There is no assertion that
the selected part itself is an original analytic total-intertwiner
source. Moving windows in (23) carry (22).

The paired opposite-polarization source makes the retained
higher normal terms particularly explicit. With J's matrices
\(\mathcal J(\mu)=J(e^\mu)\), \(B^-(\mu)=B_-(e^\mu)\), its exact
complete finite frame period is
\[
 \begin{split}
 \Phi_0(W_\beta(e^\mu))
 ={}&s(\mu)N^{-3r}
 \sum_{\lambda_0,\lambda_1,\lambda_2}
 (\Psi_{\lambda_0}^*\mathcal J(\mu)\Psi_{\lambda_1})
 (\Psi_{\lambda_1}^*B^-(-\mu)\Psi_{\lambda_2})\\
 &\hspace{29mm}\cdot
 (\Psi_{\lambda_2}^*\mathcal J(-\mu)\Psi_{\lambda_0}),\qquad
 s(\mu)=D_N(e^\mu)/a_N(e^\mu).
 \end{split}
 \tag{24}
\]
This is J(23) with three complete insertions of (6); no order
is changed. Its entire scalar is
\(a_N(M)=(-1)^{d(m+1)}N(D_N(M)/N)^m\).
Independent seam frames telescope as before.
Restricting the three label sets gives exactly
\[
 s(\mu)\operatorname{Tr}
 (P_0(\mu)\mathcal J(\mu)P_1(\mu)
                B^-(-\mu)P_2(\mu)\mathcal J(-\mu)).
 \tag{25}
\]
Here \(P_i\) denote the partial resolutions (21), not highest-cut
projectors.

For fixed \(P_i\), write
\(\mathcal J(\mu)=R/\mu+J_0+\mu J_1+O(\mu^2)\) and
\(B^-(\mu)=B_0+\mu B_1+\mu^2B_2/2+O(\mu^3)\).
The trace in (25) has coefficients
\[
 \begin{split}
 C_{-2}&=-\operatorname{Tr}(P_0RP_1B_0P_2R),\\
 C_{-1}&=\operatorname{Tr}(P_0RP_1B_0P_2J_0
       -P_0J_0P_1B_0P_2R+P_0RP_1B_1P_2R),\\
 C_0&=\operatorname{Tr}(P_0J_0P_1B_0P_2J_0
       -P_0RP_1B_0P_2J_1-P_0J_1P_1B_0P_2R\\
 &\hspace{15mm}-P_0RP_1B_1P_2J_0
       +P_0J_0P_1B_1P_2R-\tfrac12P_0RP_1B_2P_2R).
 \end{split}
 \tag{26}
\]
J(28) gives
\[
 s(\mu)=\sigma+s_2\mu^2+O(\mu^4),\qquad
 \sigma=(-1)^{d(m+1)},\qquad
 s_2=-\sigma(m-1)(N^2-1)/6.
 \tag{27}
\]
The finite part of (25) is consequently
\(\sigma C_0+s_2C_{-2}\). For moving \(P_i\), their full Taylor
coefficients, including second derivatives against \(C_{-2}\),
are included before extracting that finite part. Formula (22)
determines those derivatives for the stated frame motion.

For complete resolutions \(P_i=I\), J(26) gives \(R^2=0\).
It kills the double trace pole and the \(B_2\) trace, while the
remaining terms give J(29)--(30), equivalently (18).
Intervening partial resolutions do not permit that simplification.
The finite sums commute with Laurent coefficient extraction;
there is no pointwise pole cancellation hypothesis.

The actual opposite-polarization window current is retained too.
For two packet partial resolutions \(P,Q\), let \(T(M)\) be J(9),
put \(B_{\rm ref}=B_-(M^{-1})\), and set
\(\Delta_{P,Q}=PT-TQ\). J(11),(19) give directly
\[
 J(M)Q B_{\rm ref}J(M^{-1})
 =a_N(M)H(M)^{-1}P B_+(M)
       -H(M)^{-1}\Delta_{P,Q}B_{\rm ref}J(M^{-1}).
 \tag{27a}
\]
Indeed \(B_+T=TB_{\rm ref}\); multiply
\(PB_+T-TQB_{\rm ref}=\Delta_{P,Q}B_{\rm ref}\)
by \(H^{-1}\) and \(J(M^{-1})\), then use
\(TJ(M^{-1})=a_NI\).
The defect is zero for the complete resolutions \(P=Q=I\).
No equation identifying two selected packet windows is assumed.
Their meridian derivatives include both (22) and the actual
derivative of \(T\). Formula (27a) is a marked matrix identity,
not an extension of (14) to arbitrary nonintertwining marks.

## 5. The complete seam removes the added damping

At any one-head seam the exact contraction is already (5):
\[
 \frac1N\sum_{a,s}
      g_{a,s}(n)\overline{g_{a,s}(k)}=\delta_{nk}.
 \tag{28}
\]
The frequency sum first enforces equality of the physical
occupations. The center sum then has value one. With the
analytic dual in (7), diagonal weights cancel on this diagonal
as well. Tensoring proves the same assertion on every wire.
Thus summing all packet centers and carriers restores the
original capped word, including its original signs and phases.
It does not leave four independent positive packet penalties
at each previously estimated local kernel.

There is a precise quadratic version of the same fact. Let
\(x\in\mathbb R^k\) denote physical seam variations and \(a\)
the corresponding free center variations. Suppose the original
real quadratic form is \(\tfrac12x^{\mathsf T}Hx\), and the
added packet penalty is
\(-\tfrac12(x-a)^{\mathsf T}C(x-a)\), \(C>0\). The combined
Hessian and its Schur complement in \(a\) are
\[
 \begin{pmatrix}H-C&C\\C&-C\end{pmatrix},\qquad
 (H-C)-C(-C)^{-1}C=H.
 \tag{29}
\]
The direction \(a=x\) displays the loss of the extra penalty
directly. Integrating the center Gaussian gives the same result,
up to its normalization. This calculation does not assert a
Gaussian approximation to every finite frame mode; (28) proves
the cancellation without such an approximation.

A prospective selected source contribution must therefore
specify compatible center and carrier labels, including (11),
an actual stationary cycle for the enlarged finite sum, and
the remaining normal and boundary coupons. It must control
all complementary labels, wrapped windows, and Fourier aliases
relative to that contribution. A local nonzero packet kernel,
or a positive frame operator, supplies none of these comparisons
by itself. The frame identity also does not select a geometric
relative cycle or make its coefficient nonzero.

The result here is the original finite source expansion
(12),(16),(24), its physical caps and boundary data, its true
moving-frame normal currents (20)--(27), and the exact seam
cancellation (28)--(29). No new volume-conjecture case, source
positivity, coherent inverse estimate, or geometric contribution
is claimed.

## Complete proof direct and author protocol

* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256
  d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44,
  complete 639 lines.

The complete direct was freshly read nontruncated in this author
sequence. All finite frame, coefficient, normal, and quadratic
calculations above are proved inline. Only written mathematics
and text/hash operations were used. Frozen and public files were
not changed.
