# Exact transport between conditional messages and Fourier messages

Research deduction, 7 November 2026. The full conditional transfer and
the original Fourier attachment are exactly intertwined by an explicit
finite change of coordinates. This identifies where the proved
three-crossing source induction applies. It also retains the deleted
corner as an exact additional message, without asserting a mixed-source
estimate. No numerical evaluation is used.

## 1. The two finite message spaces

Keep the original conventions
\[
 q=e^{\pi i/N},\quad r=q^{-2},\quad D=N-1,\quad
 P_j=(r;r)_j,\quad \kappa=q^{D^2/2},\qquad N\ge2.
 \tag{1}
\]
Let \(\mathcal P_N\) be the polynomials of degree less than \(N\).
Let \(\mathcal H_N\) be the original Fourier space with frequencies
\(-D/2,-D/2+1,\ldots,D/2\). Its cardinal vector is \(h(x)\).
Use precisely the finite basis and matrices of
[exact wire contraction](research_mixed_wire_exact_contraction.md),
equations (3), (10)--(13):
\[
 f_j(x)=\frac{e^{-\pi iDx}}N
 X^j\prod_{a=j+1}^{N-1}(1-Xr^a),\qquad X=e^{2\pi ix},
 \quad f=Sh,\quad \Gamma=SS^T,
 \quad A_{3+\beta}=S^TB_{3+\beta}S.
 \tag{2}
\]
These are entire Fourier functions. All products and transposes below
are bilinear; no conjugation is introduced.

For \(\alpha=0,1\), define
\[
 (\mathcal E_\alpha F)(x)
   =\sum_{j=0}^{N-1}P_j^{1-\alpha}F(r^j)f_j(x).
 \tag{3}
\]
This is an isomorphism \(\mathcal P_N\to\mathcal H_N\): evaluation
at the \(N\) distinct roots is invertible, all \(P_j\ne0\), and
the \(f_j\) form a basis. Equation (3) is a global finite transform,
not substitution of a complex retained-leg coordinate for a Fourier
wire coordinate.

Retain the entire original conditional kernel \(C_{\beta,N}\) and
weight \(W_{\alpha,N}=[d_N(X)(1+X^{-N})]^\alpha\). Define
\[
 (\mathcal T_{\alpha\beta}F)(Y)
 =N\operatorname{CT}_X
       [F(X)W_{\alpha,N}(X)C_{\beta,N}(X,Y)]
 =\sum_{a<N}\frac{F(r^a)C_{\beta,N}(r^a,Y)}{P_a^\alpha}.
 \tag{4}
\]
Both equalities, the nonnegative output band, and the exact additional
frequency \(N\) when \(\alpha=1\) are proved in
[literal transfer](research_mixed_literal_transfer_norm_obstruction.md).
Thus \(\mathcal T_{\alpha\beta}\) maps \(\mathcal P_N\) to itself.
In particular (4) combines the two four-type Fourier alternatives
before any modulus is taken.

For an original matrix \(B\), write
\[
 (\mathcal A_B G)(y)=N\int_{x_0}^{x_0+1}
             G(x)h(x)^TBh(y)\,dx.
 \tag{5}
\]
The input period may have any fixed height. If \(G=\ell^Th\),
the exact cardinal identity gives \(\mathcal A_BG=\ell^TBh\).
At even levels both factors are antiperiodic and their product is
periodic, so the same identity and orientation apply.

## 2. The exact intertwiner and the actual prepared cap

**Proposition 1.** For every \(F\in\mathcal P_N\) and
\(\alpha,\beta\in\{0,1\}\),
\[
 \boxed{\quad
 \mathcal E_\beta\mathcal T_{\alpha\beta}F
   =\frac1{\kappa^{1+\beta}N^\beta}
          \mathcal A_{A_{3+\beta}}\mathcal E_\alpha F .
 \quad}
 \tag{6}
\]
This is a full-source identity, including the entire original matrix
\(A_{3+\beta}\), rather than a retained or principal kernel.

*Proof.* Set \(w_a=P_a^{1-\alpha}F(r^a)\). Equation (18) of
[conditional torus composition](research_mixed_conditional_torus_composition.md)
is the exact matrix identity
\[
 \frac{(\Gamma B_{3+\beta})_{ab}}
           {\kappa^{1+\beta}N^\beta}
       =\frac{P_b^{1-\beta}}{P_a}C_{\beta,N}(r^a,r^b).
 \tag{7}
\]
Equations (4) and (7) show that the row of \(f_b\)-coefficients
on the left of (6) is \(w^T\Gamma B_{3+\beta}/
(\kappa^{1+\beta}N^\beta)\). On the right it is the same row,
since \(SA_{3+\beta}=\Gamma B_{3+\beta}S\) and \(f=Sh\).
This proves (6). All triangular support zeros in (7) remain exact.
\(\square\)

Let \(U_{\alpha,N}(w,X)\) be the literal first cap. Equation (17)
of the same source theorem, with its whole ordinary-color extension,
gives
\[
 \mathcal E_\alpha U_{\alpha,N}(w,\cdot)
 =\frac{v(w)^TA_{3+\alpha}h}
              {\kappa^{1+\alpha}N^\alpha}.
 \tag{8}
\]
Consequently, for a word \(\epsilon_1,\ldots,\epsilon_m\),
start with \(F_1=U_{\epsilon_1,N}(w,\cdot)\) and set
\(F_{j+1}=\mathcal T_{\epsilon_j\epsilon_{j+1}}F_j\). Then
\[
 \mathcal E_{\epsilon_m}F_m
 =\frac{v(w)^TA_{3+\epsilon_1}\cdots A_{3+\epsilon_m}h}
         {\kappa^{m+\sum_j\epsilon_j}N^{\sum_j\epsilon_j}}.
 \tag{9}
\]
This preserves all ordinary color derivatives and their original
normalizations. In particular \(\kappa^2\mathcal E_0F_2\) for
the word \((3,3)\) is exactly the prepared cap
\(v(w)^TA_3^2h\), not a source with a substituted boundary vector.

## 3. What the existing source induction supplies

The [quantified prepared-cap theorem](research_three_prepared_cap_quantified_source.md)
therefore supplies a nonzero full-source packet for the image in (9)
at \(m=2\), on the genuine disk
\(|x-x_h|\le1/200\), where
\(x_h=1/6+i\log2/(2\pi)\). Its
[real extension](research_three_prepared_cap_real_extension.md)
also bounds the complete outgoing period. The
[first entrance](research_three_first_entrance_real_extension.md)
identifies the actual \(m=3\) message on
\[
 \mathcal U=\{|x-x_h|\le.005\}
          \cup\{x_h+t:|t|\le.009\}.
 \tag{10}
\]
It has the nonzero packet and whole-period envelope used by the
[larger source induction](research_three_larger_source_propagation.md):
\[
 \frac{S'(x_h+z)}{k_0}=-\sqrt{21}z+g(z),\quad
 |g(0)|\le.0057,\quad |g'|\le.18,
 \qquad
 |G_N(x_h+t)|\le CN^q
 e^{N\{M+|k_0|H v(t)-(29/20)v(t)^2\}},
 \tag{11}
\]
where \(v(t)=\min\{d_{\mathbb T}(t,0),.03\}\) and
\(k_0=4\pi(2\sqrt3-3i)/21\).
That theorem is a genuine operation-preserving source estimate: it
retains the central coefficient and bounds every input complement,
then resets (11). Its attachment is
\(\mathcal A_{\widetilde A_3}\), with
\(\widetilde A_3=A_3-E_{40}\), not the full operator in (6).
The [full-boundary restoration theorem](research_three_full_boundary_source_propagation.md)
now uses the existing corner estimate to restore every actual
homogeneous message \(v(w)^TA_3^mh\), \(m\ge3\), within
this same class. The full-minus-retained error has a rate gap
\(19/100\) from the center action on the entire real period and
a relative gap \(17/100\) on \(\mathcal U\).

**Corollary 2.** For the literal conditional messages
\(F_m=\mathcal T_{00}^{m-1}U_{0,N}(w,\cdot)\),
\(m\ge3\), the functions \(\kappa^m\mathcal E_0F_m\)
have the nonzero original packet and full real-period envelope (11),
with \(H=Z^{m-3}(.0057)\) and the original iterated action.
Here \(Z\) is the strict contraction constant of the cited
larger-source induction. Their exact next step is the full
\(\mathcal T_{00}\), not a corner-deleted conditional approximation.

*Proof.* Equation (9) identifies these functions with the actual
homogeneous messages. Apply the full-boundary restoration theorem
and then (6). \(\square\)

This proves positive compatibility for the prepared two- and
three-block messages and their entire fixed-length three-type orbit.
It concerns their \(\mathcal E_0\)-images, not a pointwise
retained-leg estimate for \(F_m\). It does not infer (11) from a pointwise
cap or terminal supporting plane on a retained-leg plateau. Such a
plane controls neither all physical arguments in (3) nor the
cancellation in their sum. The inherited complete-color whole-period
envelopes include fixed ordinary jets; they are not automatically
uniform envelopes on a fixed off-color disk. Nor is the actual-orbit
corollary an assertion about every input satisfying (11).

For mixed words the analytic chart also changes. The validated original
[three/four interface](research_three_four_source_interface.md),
equations (14)--(15), lies more than \(.035\) from \(x_h\), with
opposite nonzero momenta. It is outside (10). The
[full local power-four packet](research_power_four_source_packet.md)
does retain its complete finite source near that interface, but gives
no whole-input-period envelope or reset inequality there. Thus exact
regrouping and (6) identify the next operation; neither extends the
old source class to it by a change of notation.

## 4. An exact corner state with all returns retained

The deleted operator can be kept explicitly rather than discarded.
Put \(L=\lfloor N/40\rfloor\), let \(I_L\) include the first
\(L+1\) coordinate vectors, and define
\[
 U_L=M^TI_L,\quad V_L=I_L^TM,\quad C_L=I_L^TJM I_L.
 \tag{12}
\]
The exact deletion formula in the
[corner theorem](research_three_chain_fourier_corner_transfer.md) gives
\[
 E_{40}=U_LC_LV_L,\qquad U_L=V_L^T,\qquad
 \operatorname{rank}E_{40}\le L+1.
 \tag{13}
\]
Since the original \(M\) is lower triangular, the column image of
\(E_{40}\) is contained in the first \(L+1\) original coordinates.
This is finite rank at each level, but its rank bound grows with \(N\).

For any original row \(\ell_0\), put
\(\ell_n=\ell_0A_3^n\), \(z_n=\ell_nU_L\), and
\(\widetilde A=A_3-E_{40}\). Exact iteration gives
\[
 \begin{split}
 \ell_n&=\ell_0\widetilde A^n+
       \sum_{j=0}^{n-1}z_jC_LV_L\widetilde A^{n-1-j},\\
 z_n&=\ell_0\widetilde A^nU_L+
       \sum_{j=0}^{n-1}z_jC_L
                     (V_L\widetilde A^{n-1-j}U_L).
 \end{split}
 \tag{14}
\]
Indeed \(\ell_{n+1}=\ell_n\widetilde A+z_nC_LV_L\);
unroll and multiply by \(U_L\). The \(z_j\) are the full
messages at their creation times, so (14) retains every repeated
corner encounter, including feedback into the retained message.

For an arbitrary three/four word an equivalent ordered recurrence is
particularly simple. Set \(B_j=\widetilde A\) at a three letter,
\(B_j=A_4\) at a four letter, and \(E_j=A_{n_j}-B_j\).
Starting with \(f_0=\ell_0,e_0=0\), define
\[
 f_{j+1}=f_jB_{j+1},\qquad
 e_{j+1}=e_jB_{j+1}+(f_j+e_j)E_{j+1}.
 \tag{15}
\]
Then \(f_j+e_j=\ell_0A_{n_1}\cdots A_{n_j}\) exactly.
Every corner injection has the factorization (13); a four letter
propagates the existing error and is not silently replaced by a
three letter. Applying (3) inversely transfers these same recurrences
to conditional messages. No analytic smallness of \(e_j\), or
uniform fixed-dimensional compression, follows from (13)--(15).

The concrete mixed-source obligation is therefore to control the
full Fourier attachment identified by (6), including its complement
and normalization relative to its actual action, or to control the
coupled retained and corner states (15) in a compatible analytic
class. The exact source and closing functional remain unchanged.
None of the identities asserts a mixed-word whole-source asymptotic
or an all-but-finite filling theorem.
