# The next conditional transfer as a dual observation of a lowered word

Research deduction, 7 November 2026. The factorial belonging to the
old last letter cancels exactly when its conditional message is fed
into the next transfer. What remains is a specified observation of
the original Newton coefficients of the word with its last power
lowered by one. For the prefix \(34\), that word is \(33\), whose
complete ordinary two-boundary source is already controlled.
The observation below retains the entire original Hermite trace.
It is not evaluation of that source at a new ordinary color.
No numerical evaluation is used.

## 1. Lower the last power before taking the next observation

Use the original Newton basis \(e_0,\ldots,e_D\), crossing \(M\),
reversal \(J\), and evaluation vector \(v(w)\), with
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 P_b=(r;r)_b,\quad \kappa=q^{D^2/2},\quad A_n=JM^n.
 \tag{1}
\]
The full Frobenius trace satisfies
\(\phi_N(e_i e_j)=J_{ij}=\mathbf1_{i+j=D}\).
Its repeated-root derivatives are part of this identity.

The exact basis change in
[wire contraction, equation (13)](research_mixed_wire_exact_contraction.md) is
\[
 S=LM,\qquad
 L=\operatorname{diag}\bigl(\kappa^{-1}(-q)^{-b}/P_b\bigr).
 \tag{2}
\]
Thus \(S^{-1}=M^{-1}L^{-1}\). In particular
\[
       A_nM^{-1}=A_{n-1}.
 \tag{3}
\]
This is an equality of the original matrices, including their
boundary markings and all normal data, not an assertion about an
unmarked tangle move.

Let \(n_j=3+\epsilon_j\), \(1\le j\le m\), put
\(k=\sum_j\epsilon_j\), \(\alpha=\epsilon_m\), and let \(F_m\)
be the literal conditional message initialized by its original
ordinary cap and iterated by the original conditional transfers.
Define the lowered-word row
\[
 \ell^{\downarrow}(w)
   =v(w)^T A_{n_1}\cdots A_{n_{m-1}}A_{n_m-1}.
 \tag{4}
\]
No restriction to a retained kernel is made.

**Proposition 1.** For every physical index \(0\le b<N\),
\[
 \boxed{\quad
 F_m(w,r^b)
   =\kappa^{1-m-k}N^{-k}(-q)^bP_b^\alpha
                       \ell_b^{\downarrow}(w).
 \quad}                                                        \tag{5}
\]
Consequently attachment of \(3+\beta\), \(\beta=0,1\), obeys
\[
 \boxed{\quad
 (\mathcal T_{\alpha\beta}F_m)(w,Z)
  =\kappa^{1-m-k}N^{-k}
       \sum_{b=0}^{D}(-q)^b\ell_b^{\downarrow}(w)
                                      C_{\beta,N}(r^b,Z).
 \quad}                                                        \tag{6}
\]
The old factorial has disappeared from (6), including when
the old letter was four.

*Proof.* The [message bridge, equation (9)](research_mixed_conditional_fourier_message_bridge.md)
identifies the original \(f\)-basis coefficient row as
\[
 \bigl(P_b^{1-\alpha}F_m(w,r^b)\bigr)_{b=0}^{D}
  =\kappa^{-m-k}N^{-k}
            v(w)^TA_{n_1}\cdots A_{n_m}S^{-1}.
 \tag{7}
\]
Substitute (2)--(3) into the right side. The \(b\)-th diagonal
entry of \(L^{-1}\) is \(\kappa(-q)^bP_b\). Division by
\(P_b^{1-\alpha}\) proves (5). All these factors are nonzero.
The exact physical transfer is
\(\sum_bF_m(w,r^b)C_{\beta,N}(r^b,Z)/P_b^\alpha\);
substitution gives (6). \(\square\)

For completeness, the entire old message is recovered without a
continuation choice:
\[
 F_m(w,Y)=\kappa^{1-m-k}N^{-k}
       \sum_{b=0}^{D}(-q)^bP_b^\alpha
                          \ell_b^{\downarrow}(w)\mathfrak l_b(Y),
 \qquad
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu .
 \tag{8}
\]
These are the original degree-\(D\) cardinal polynomials. In
particular (8) retains the finite Fourier forcing rather than
replacing \(d_N\) by a reciprocal-factorial continuation.

## 2. A full ordinary polynomial and its exact dual

Let
\[
 \mathcal E^{\downarrow}_N(w,t)
       =\ell^{\downarrow}(w)v(t)
       =\sum_{b=0}^{D}\ell_b^{\downarrow}(w)e_b(t),
 \tag{9}
\]
the ordinary two-boundary source of the lowered word. Define the
specified dual polynomial
\[
 \mathcal D_{\beta,N}(t,Z)
       =\sum_{b=0}^{D}(-q)^b C_{\beta,N}(r^b,Z)e_{D-b}(t).
 \tag{10}
\]
Its separate degrees in \(t,Z\) are at most \(D\). The coefficients
in (10) contain the whole conditional kernel
\[
 C_{\beta,N}(Y,Z)
       =\sum_{j=0}^{D}
          \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
 \qquad p_j(Z)=(rZ;r)_j.
 \tag{11}
\]

**Corollary 2.** With every original normal retained,
\[
 \mathcal T_{\alpha\beta}F_m
   =\kappa^{1-m-k}N^{-k}
       \phi_N^{(t)}
          [\mathcal E^{\downarrow}_N(w,t)
                           \mathcal D_{\beta,N}(t,Z)].
 \tag{12}
\]
Indeed pairing the \(e_b\) in (9) with \(e_{D-b}\) in (10)
gives exactly (6). This proof uses a bilinear trace; it introduces
neither complex conjugation nor a positive inner product.

There is an entirely finite triangular source for the dual. Put
\(\nu_j=(-1)^jq^{j(j+1)}\). Then
\[
 \boxed{\quad
 \mathcal D_{\beta,N}(t,Z)
  =\sum_{\ell=0}^{D}(-q)^{D-\ell}P_\ell e_\ell(t)
       \sum_{j=0}^{\ell}
          \frac{\nu_j^{-1}p_j(Z)}
                        {P_{\ell-j}P_j^{2+\beta}} .
 \quad}                                                        \tag{13}
\]
To verify this, the physical incoming argument
\(Y=r^{D-\ell}\) in (11) leaves exactly \(j\le\ell\).
The complementary factorial identity
\[
 P_{D-h}=\frac{N}{\nu_hP_h}
 \tag{14}
\]
and the phase calculation
\[
 r^{-(D-\ell)j}\frac{\nu_\ell}{\nu_{\ell-j}}
       =(-1)^jq^{-j(j+1)}=\nu_j^{-1}
 \tag{15}
\]
give
\[
 C_{\beta,N}(r^{D-\ell},Z)
   =P_\ell\sum_{j=0}^{\ell}
        \frac{\nu_j^{-1}p_j(Z)}
                         {P_{\ell-j}P_j^{2+\beta}}.
 \tag{16}
\]
All factors in the denominators have index below \(N\).
For a physical output \(Z=r^a\), only the further exact zeros
\(j+a\ge N\) may be used. At an ordinary complex output none
of those rows may be discarded. The true indices \(\ell=0,D\)
are included; for example the coefficient of \(e_0(t)\) in
(13) is exactly \((-q)^D\), independent of \(Z\).

## 3. Specialization to the actual \(34\) prefix

Here \(m=2,k=1,\alpha=1\). The lowered word is \(33\), and
\[
 \begin{split}
 \mathcal E_{33,N}(w,t)&=v(w)^TA_3^2v(t),\\
 F_{34,N}(w,r^b)&=
       \frac{(-q)^bP_b}{\kappa^2N}
                         \bigl(v(w)^TA_3^2\bigr)_b,\\
 \mathcal F_{\beta,N}(w,Z)&=
       \frac1{\kappa^2N}
           \phi_N^{(t)}
               [\mathcal E_{33,N}(w,t)\mathcal D_{\beta,N}(t,Z)].
 \end{split}                                                   \tag{17}
\]
At the actual first physical node \(Y=1\),
\[
 F_{34,N}(w,1)
        =\frac{\mathcal E_{33,N}(w,c_0)}{\kappa^2N},
 \qquad c_0=q+q^{-1},\qquad v(c_0)=e_0 .
 \tag{18}
\]
The color in (18) tends to \(+2\). It is not the complete
ordinary color \(-2\).

The first-root deletion from
[the sectorwise end theorem](research_mixed_three_four_next_sectorwise_first_end.md)
changes \(F_{34,N}\) by its exact polynomial \(R_N\), with a paid
error in each whole Fourier sector. Therefore (17) also gives
an exact full-cycle representation of the sum of the two sectors
for the truncated prefix, after subtracting
\(\mathcal T_{1\beta}R_N\).
It does not identify the dual trace separately with either sector,
or turn a deleted physical index range into a contour arc.

## 4. A coefficient contour and the scope of the known \(33\) theorem

Use the monic original polynomial
\(\mathcal Q_N(t)=T_N(t)+2\), where
\(T_N(z+z^{-1})=z^N+z^{-N}\). The exact Frobenius formula is
\[
 \phi_N(f)=(-1)^DN^2[t^D]\operatorname{rem}_{\mathcal Q_N}f
   =\frac{(-1)^DN^2}{2\pi i}
          \oint_{\mathcal C}\frac{f(t)}{\mathcal Q_N(t)}\,dt,
 \tag{19}
\]
where \(\mathcal C\) is any positive closed contour surrounding
all physical roots and no other singularities. To prove the second
identity, divide \(f\) by the monic polynomial \(\mathcal Q_N\);
the polynomial quotient integrates to zero, and the residue at
infinity of the remainder quotient extracts its top coefficient.
The double roots and the odd-level simple root are all inside
the same contour.

Consequently the actual next full source has the exact contour
\[
 \boxed{\quad
 \mathcal F_{\beta,N}(w,Z)
   =\frac{(-1)^D\kappa^{-2}N}{2\pi i}
       \oint_{\mathcal C}
        \frac{\mathcal E_{33,N}(w,t)\mathcal D_{\beta,N}(t,Z)}
                             {\mathcal Q_N(t)}\,dt .
 \quad}                                                        \tag{20}
\]
No spectral derivative has been replaced by a value. Equivalently,
the individual coefficient in (17) is
\[
 \bigl(v(w)^TA_3^2\bigr)_b
          =\phi_N^{(t)}[\mathcal E_{33,N}(w,t)e_{D-b}(t)].
 \tag{21}
\]
Equations (20)--(21) explain precisely which observation of the
ordinary kernel is required.

The [complete ordinary \(33\) theorem](research_internal_pair_three_full_boundary_packet.md)
proves a nonzero expansion for \(\mathcal E_{33,N}\) near
\((w,t)=(-2,-2)\), with all ordinary derivatives, and an upper
bound over both whole real angular periods and a fixed complex
strip. These are directly eligible estimates for the first factor
in (20). A contour \(t=-2\cos(u+i\eta)\), \(0\le u\le2\pi\),
with fixed small \(\eta>0\), surrounds the whole physical interval
and lies in that strip. Give it the positive orientation, which
is the reverse of increasing \(u\) in this parametrization;
it may then be used in (20).
The factor \(\mathcal D_{\beta,N}\) and the complete trace kernel
\(\mathcal Q_N^{-1}\) still remain.

In particular the \(33\) theorem is not missing an ordinary
boundary parameter, but its local evaluation expansion is not
an estimate for all coefficients in (21). The original exterior
color \(c_0\) in (18) is covered only by its whole-period upper
bound. A useful estimate for (20) must retain the dual polynomial
(13) and the trace kernel on a complete contour, including their
oscillation. No nonzero overlap or whole next-source asymptotic
is inferred from the \(33\) evaluation expansion.

All identities hold for both level parities, all ordinary colors,
all complex \(Z\), and every fixed ordinary or output derivative.
They do not change the original outgoing row scalar or its final
ordinary observation from the next-attachment theorem.

## 5. The dual for a next three is an exact mixed boundary function

Let \(h(z)\) be the original half-band cardinal vector. At every
physical output \(Z=r^k\), the coefficient column of the polynomial
\(\mathcal D_{\beta,N}(\,\cdot\,,r^k)\) is exactly
\[
 \boxed{\quad
  \kappa^{-\beta}N^{-\beta}(-q)^kP_k^\beta
                       M^{-1}JM^{1+\beta}e_k .
 \quad}                                                        \tag{22}
\]
Here \(e_k\) on the right is the coordinate vector, rather than
the Newton polynomial. To check this directly, the message bridge
equation (7) gives
\[
 C_{\beta,N}(r^b,r^k)
    =\frac{P_bP_k^{\beta-1}}{\kappa^{1+\beta}N^\beta}
                                      (\Gamma B_{3+\beta})_{bk}.
 \tag{23}
\]
Multiplying by \((-q)^b\), then reversing its coefficient column
as prescribed by (10), yields
\[
 \kappa^{-2-\beta}N^{-\beta}P_k^{\beta-1}
                          JM A_{3+\beta}S^{-1}e_k .
 \tag{24}
\]
Use the original braid identity \(JMJ=\kappa M^{-1}JM^{-1}\),
then (2), to reduce (24) to (22). Thus no matrix adjoint or
unprescribed boundary adapter enters.

The cardinal identity, including its parity-dependent chirp, is
\[
       (-q)^k\mathfrak l_k(e^{-2\pi iz})
                            =e^{-\pi iDz}h_k(z).
 \tag{25}
\]
Indeed expand \(h_k\) in the symmetric frequencies
\(-D/2,\ldots,D/2\), in descending order. The residual factor
at the node is \(e^{-\pi iDk/N}=(-q)^k\).
Cardinal interpolation of (22) therefore gives, for every complex
\(z\),
\[
 \begin{split}
 \mathcal D_{0,N}(t,e^{-2\pi iz})
    &=e^{-\pi iDz}\,v(t)^TM^{-1}JMh(z),\\
 \mathcal D_{1,N}(t,e^{-2\pi iz})
    &=\kappa^{-1}N^{-1}e^{-\pi iDz}\,
       v(t)^TM^{-1}JM^2
                      \operatorname{diag}(P_0,\ldots,P_D)h(z).
 \end{split}                                                   \tag{26}
\]
The second line retains its diagonal factorial. The first has
no such factor, but its matrix is \(M^{-1}JM\), not \(A_3\),
the identity, or an ordinary evaluation column.

Similarly, whenever the old word ends in a three, equation (8)
simplifies to
\[
 F_m(w,e^{-2\pi iz})
   =\kappa^{1-m-k}N^{-k}e^{-\pi iDz}
                  \ell^\downarrow(w)h(z).
 \tag{27}
\]
For example the next \(343\) message in (17) is exactly a chirped
Fourier boundary function of the lowered word \(342\).
This is not a statement that this Fourier observation has the
same estimates as an ordinary-color evaluation of that word.

Equations (20) and (26) give a complete finite alternative for
estimating the next three: the known ordinary \(33\) kernel is
paired with the specified mixed function \(v(t)^TM^{-1}JMh(z)\)
inside the original Hermite trace. The available whole-period
ordinary \(33\) bound controls its first factor. It does not by
itself control this mixed observation or its cancellations.
Thus these identities remove an unnecessary old factorial and
identify a concrete source for further analysis, without asserting
that the unselected far half-cycle has already been bounded.

## 6. The next-three dual retains the original endpoint polynomial

Let \(R_N(t)\) be the original crossing element, whose multiplication
matrix is \(M\). Its inverse below means its unique inverse in
\(\mathbb C[t]/(\mathcal Q_N)\), represented by a polynomial of
degree at most \(D\). Write the complete original endpoint polynomial
as in [the ordinary pair source](research_mixed_three_four_ordinary_pair_target.md):
\[
 H_N(t,W)=\sum_{\ell=0}^{D}
             \frac{(-q)^{-\ell}e_\ell(t)}{P_\ell}(W;r)_\ell .
 \tag{28}
\]
Then the dual for a next three satisfies the exact quotient identity
\[
 \boxed{\quad
 \mathcal D_{0,N}(t,Z)
   =\operatorname{rem}_{\mathcal Q_N}
                [\,\kappa^{-1}R_N(t)^{-1}H_N(t,rZ)\,].
 \quad}                                                        \tag{29}
\]
In particular the whole next-three source is
\[
 \boxed{\quad
 \mathcal F_{0,N}(w,Z)
    =\frac1{\kappa^3N}
        \phi_N^{(t)}
          [\mathcal E_{33,N}(w,t)R_N(t)^{-1}H_N(t,rZ)].
 \quad}                                                        \tag{30}
\]

Here is a proof that also checks all quotient normals. Since \(M\)
is multiplication by \(R_N\), componentwise in the quotient
\[
                  R_N(t)v(t)^TM^{-1}=v(t)^T .
 \tag{31}
\]
This is stronger than equality only at distinct spectral values.
The exact reversed basis identity, directly from the product in
wire contraction equation (3), is
\[
 f_{D-\ell}(z)
       =\frac{e^{\pi iDz}}N\nu_\ell p_\ell(Z),
                  \qquad Z=e^{-2\pi iz}.
 \tag{32}
\]
Indeed reversal of the \(\ell\) factors has carrier
\((-1)^\ell r^{-\ell(\ell+1)/2}=\nu_\ell\).
Consequently the original equality
\((Mh)_j=\kappa(-q)^jP_jf_j\), together with (14), gives the
ordinary polynomial identity
\[
 \begin{split}
 v(t)^TJMh(z)
   &=\kappa(-q)^D e^{\pi iDz}
       \sum_{\ell=0}^{D}
              \frac{(-q)^{-\ell}e_\ell(t)p_\ell(Z)}{P_\ell}\\
   &=\kappa^{-1}e^{\pi iDz}H_N(t,rZ).
 \end{split}                                                   \tag{33}
\]
The scalar identity used in the second line is
\(\kappa^2(-q)^D=1\), valid at either parity. Multiply the first
line of (26) by \(R_N(t)\), use (31)--(33), and invert \(R_N\)
in the quotient. This proves (29). Applying the full trace in
(17) proves (30).

Formula (30) uses the whole original endpoint polynomial rather
than a new arbitrary boundary vector. It preserves the exact shift
\(rZ\) and the inverse crossing. In a contour version of (30),
use the polynomial representative of \(R_N^{-1}\). It cannot
be replaced there by the pointwise rational function \(1/R_N(t)\)
without accounting for its other poles. Likewise its unit-modulus
spectral values do not give a unit-modulus bound on the complex
coefficient contour.

The local and whole-period ordinary \(33\) estimates thus have a
literal source to which they may be applied inside a complete
trace. The endpoint factor and inverse crossing still require
their coupled trace estimate at the actual next action. Neither
(29) nor (30) suppresses a part of the original Fourier period.
