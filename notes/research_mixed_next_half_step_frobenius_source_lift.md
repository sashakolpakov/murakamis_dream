# A full Frobenius half-step factor and its exact cubic source lift

Private exact-source deduction, 9 November 2026. The regular half-step
maps have explicit adjoints between the original and opposite-grid
Frobenius algebras. This gives an exact first-order factorization of
the original unweighted operator at its initial eigenvalue, and a
two-component lift of the complete cubic source. The original scalar
observation is expressed through the factor with precisely the original
parity forcing and no discarded endpoint normal.

The pairings are bilinear Frobenius forms, not positive Hermitian inner
products. The cubic conjugation in the lifted factor still contains the
full turn kernel. No local oriented factorization, coercive estimate,
or cancellation gain follows. No mathematical numerical evaluation or
frozen-source edit is used.

## 1. The two full trace pairings

Keep \(N\ge3\), \(D=N-1\), \(\theta=\pi/N\),
\(q=e^{i\theta}\), \(\eta=(-1)^D\),
\(P(X)=2T_N(X/2)+2\), and the exact doubled-grid algebras
from [the doubled-grid theorem](research_mixed_next_outer_doubled_grid_half_step.md):
\[
 \mathcal A_0=\mathbb C[X]/(P),\qquad
 \mathcal A_4=\mathbb C[X]/(P-4).
\tag{1}
\]
The original trace is \(\phi_0=\phi_N\). Choose the auxiliary
opposite-grid trace with the explicitly specified same normalization:
\[
 \phi_a(f)=\eta N^2[X^D]\operatorname{rem}_{P-a}f,
 \qquad \langle f,g\rangle_a=\phi_a(fg),
 \qquad a=0,4.
\tag{2}
\]
Both forms are nondegenerate. Indeed for any nonzero canonical
polynomial \(f\), of degree \(r\le D\), the product
\(X^{D-r}f\) has nonzero degree-\(D\) coefficient and requires
no reduction. These forms retain the full double-root first normals
and each parity's simple endpoint, as specified by (1).

Identify the two canonical representative spaces with
\(V_N=\mathbb C[X]_{<N}\), only as vector spaces. For
\(f,g\in V_N\),
\[
                         \langle f,g\rangle_0
                           =\langle f,g\rangle_4.
\tag{3}
\]
To see this, write \(fg=Ph+r\), where \(\deg h\le N-2\)
and \(\deg r<N\). Division instead by \(P-4\) has the same
quotient and remainder \(r+4h\). The change has degree at most
\(N-2\), so the top coefficient in (2) is unchanged. Equation
(3) is equality of pairings, not an isomorphism of the two algebras.

There is a useful exact angular expression. Write
\(X=-\zeta-\zeta^{-1}\), and let \(\operatorname{CT}\) denote
the constant coefficient of a Laurent polynomial. For \(f,g\in V_N\),
\[
 \langle f,g\rangle_a
    =N^2\operatorname{CT}\!\left[
       \zeta^{-N}(\zeta-\zeta^{-1})f(X)g(X)\right],
 \qquad a=0,4.
\tag{4}
\]
For a direct proof, the coefficient functional in (2) equals
\(\eta N^2[X^{-1}]fg/(P-a)\), using formal expansion at infinity.
Substitute \(X=-\zeta-\zeta^{-1}\) and its differential.
With \(\epsilon=(-1)^N=-\eta\), the denominators are
\[
 P(X)=\epsilon\zeta^N(1+\epsilon\zeta^{-N})^2,
 \qquad
 P(X)-4=\epsilon\zeta^N(1-\epsilon\zeta^{-N})^2.
\tag{5}
\]
Since \(\deg(fg)\le2N-2\), every term beyond the constant in
either parenthetical inverse square would require a Laurent
coefficient of degree at least \(2N-1\) in \(fg\). None exists.
The leading term and \(dX/d\zeta=-1+\zeta^{-2}\) give (4).
Thus (4) is exact, not a discarded high-degree approximation.

## 2. Exact cross-grid adjoints

Let \(\mathsf A,\mathsf D\) be the regular average and divided
difference from [the half-step calculus](research_mixed_next_outer_regular_half_step_calculus.md).
They exchange \(\mathcal A_0\) and \(\mathcal A_4\), with
their polynomial realizations on \(V_N\). Put
\(c=\cos\theta\), \(s=\sin\theta\). The cross-grid transpose
of a map \(H:\mathcal A_0\to\mathcal A_4\) is defined by
\[
       \langle g,Hf\rangle_4=\langle H^{\mathrm t}g,f\rangle_0;
\tag{6}
\]
use the analogous definition in the reverse direction. No scalar
conjugation is used.

**Proposition 1.** In either direction, the exact transposes are
\[
\boxed{\qquad
 \mathsf D^{\mathrm t}=\mathsf D,
 \qquad
 \mathsf A^{\mathrm t}=-c\mathsf A+s^2X\mathsf D.
\qquad}
\tag{7}
\]

*Proof.* Let \(\tau f(\zeta)=f(q\zeta)\),
\(d=q-q^{-1}\), and \(h=\zeta-\zeta^{-1}\). On the
ordinary pullbacks,
\[
 \mathsf D f=-\frac{\tau f-\tau^{-1}f}{dh},
 \qquad \mathsf A f=(\tau f+\tau^{-1}f)/2.
\tag{8}
\]
The quotients here have their already proved polynomial meanings.
Use (4), constant-coefficient invariance under \(\tau\), and
\(q^N=-1\). Then
\[
\begin{split}
 \langle g,\mathsf Df\rangle_4
 &=-\frac{N^2}{d}\operatorname{CT}
           [\zeta^{-N}g(\tau f-\tau^{-1}f)]\\
 &=-\frac{N^2}{d}\operatorname{CT}
           [\zeta^{-N}(\tau g-\tau^{-1}g)f]
   =\langle\mathsf Dg,f\rangle_0.
\end{split}
\tag{9}
\]
All products to which (4) is applied have degree at most \(2N-2\).
For the average, the corresponding transposed numerator in (4) is
\[
 -\frac{\zeta^{-N}}2
       \{(q^{-1}\zeta-q\zeta^{-1})\tau^{-1}g
                         +(q\zeta-q^{-1}\zeta^{-1})\tau g\}.
\tag{10}
\]
Divide the braces by \(2h\) with the displayed negative sign.
The identities
\[
 q^{\pm1}\zeta-q^{\mp1}\zeta^{-1}
      =ch\mp dX/2,
 \qquad
 \tau^{\pm1}g=\mathsf A g\mp dh\mathsf D g/2
\]
reduce the result to
\(-c\mathsf A g-d^2X\mathsf Dg/4
  =-c\mathsf A g+s^2X\mathsf Dg\).
This is an ordinary polynomial of degree at most \(D\), proving
the second assertion. Equality of the two forms in (3) gives the
same calculation in the reverse direction. \(\square\)

The factor \(q^N=-1\) in (9)--(10) is essential. These are not
unweighted integration-by-parts formulas on a continuous interval.
They are exact finite full-Frobenius identities, including all
coalescing endpoints.

## 3. A trace-compatible half-step factor of the original operator

Define the regular map
\[
 B=(1-X/2)\mathsf D:\mathcal A_0\longrightarrow\mathcal A_4,
 \qquad b_c=1-cX/2.
\tag{11}
\]
Its transpose and the original unweighted operator satisfy
\[
\boxed{\quad
 B^{\mathrm t}=b_c\mathsf D-\mathsf A/2,
 \qquad
 \mathcal L-2cI=-16s^2 B^{\mathrm t}B.
\quad}
\tag{12}
\]

For the transpose, multiplication by \(1-X/2\) is self-adjoint
in \(\mathcal A_4\), so (7) gives
\(B^{\mathrm t}g=\mathsf D((1-X/2)g)\). If the product has
degree \(N\), its canonical reduction differs by a multiple of
\(P-4\), which \(\mathsf D\) kills exactly. Thus the regular
product rule applies without a hidden top-degree term and gives
the first identity in (12).

For the second, use the half-step product rules to obtain
\[
 B^{\mathrm t}B
     =\left[b_c^2+\frac{s^2(4-X^2)}4\right]\mathsf D^2
                                  -b_c\mathsf A\mathsf D.
\tag{13}
\]
The exact ordered reconstruction of \(\mathcal L\) in the cited
half-step calculus now gives (12). It is also an ordinary polynomial
identity before quotient reduction.

It is convenient to normalize
\[
 S=4sB,\qquad \mu=2\cos(\theta/2)>0.
\tag{14}
\]
Then the original full algebra has the exact factor identity
\[
                         \mathcal L+2I=\mu^2I-S^{\mathrm t}S.
\tag{15}
\]
The transpose is bilinear. In particular \(S^{\mathrm t}S\) is
not asserted to be a positive operator in a Hilbert-space metric;
the sign in (15) supplies no positive coercivity or singular-value
estimate.

## 4. Exact lift of the complete source and cubic transport

Retain the full original source, turn, crossing and scalar:
\[
 \begin{gathered}
 F=K_N^{\rm ord}(-2,\cdot),\qquad
 U=TR^3,\qquad U^{-1}=R^{-3}T,\qquad
 Q=Q_N^{\rm full}=UF,\\
 \kappa=q^{D^2/2},\qquad
 a_N=-\eta P_N(-2)/N^2,\qquad
 \mathfrak f_N=\kappa^3a_N.
 \end{gathered}
\tag{16}
\]
The original [complete kernel defect](research_edge_kernel_difference_and_endpoint_bound.md)
and [cubic recurrence](research_mixed_next_physical_inner_seven_term_recurrence.md)
give
\[
 (\mathcal L+2)F=a_Ne_D,\qquad
 Ue_D=\kappa^3\,1,\qquad
 \mathcal D_3=U(\mathcal L+2)U^{-1},\qquad
 \mathcal D_3Q=\mathfrak f_N\,1.
\tag{17}
\]
These equalities are in the specified full quotients and retain
their first normals. The adopted ordinary extension of the last
equation remains
\[
 \mathcal D_3Q(X)
      =-\frac{\eta\kappa^3}{N^2}\{P_N(-2)+P_N(X)\};
\tag{18}
\]
in particular it must not be replaced by constant forcing on the
opposite grid.

On \(\mathcal A_0\oplus\mathcal A_4\), define
\[
 \mathbb D=
   \begin{pmatrix}\mu&-S^{\mathrm t}\\ S&-\mu\end{pmatrix},
 \qquad
 \widetilde{\mathbb D}=
   \begin{pmatrix}U&0\\0&I\end{pmatrix}
       \mathbb D
   \begin{pmatrix}U^{-1}&0\\0&I\end{pmatrix}
   =\begin{pmatrix}
       \mu&-US^{\mathrm t}\\ SU^{-1}&-\mu
     \end{pmatrix}.
\tag{19}
\]
Both are exact linear maps between the full finite component
algebras, not formulas for separated meromorphic coefficients.
Their squares and complete sources obey
\[
\begin{split}
 \mathbb D^2&=
  \operatorname{diag}(\mathcal L+2,\ \mu^2-S S^{\mathrm t}),\\
 \widetilde{\mathbb D}^{\,2}&=
  \operatorname{diag}(\mathcal D_3,\ \mu^2-S S^{\mathrm t}),\\
 \mathbb D\binom{F}{SF/\mu}
       &=\binom{a_Ne_D/\mu}{0},\qquad
 \widetilde{\mathbb D}\binom{Q}{SF/\mu}
       =\binom{\mathfrak f_N\,1/\mu}{0}.
\end{split}
\tag{20}
\]
This follows by multiplying the ordered blocks and using (15),(17).
It is a genuine doubled-source identity. The auxiliary component is
\(SF/\mu\), determined by the regular full-ideal map. It is not
the opposite-grid restriction of the canonical polynomial \(Q\).
Accordingly (20) does not discard or identify away the opposite-grid
forcing in (18); these are two different, explicitly defined lifts.

The block \(\mu^2-S S^{\mathrm t}\) is a specified partner operator.
It is not identified with the original opposite-grid cubic operator.
Likewise (19) contains the original full turn \(T\); it has not
been reduced to a fixed-width local angular half-step formula.

## 5. The original scalar observation and the exact retained source

For every original full test \(g\in\mathcal A_0\), including the
actual test \(g=R^3e_M H_N\), where \(M=\lceil N/2\rceil\)
and \(H_N\) is the polynomial in the
[exact outer observation](research_mixed_next_three_outer_casimir_observation.md),
the following identity holds:
\[
\boxed{\quad
 \phi_0(gQ)
   =\mu^{-2}\left\langle S U^{\mathrm t}g,
                                      S U^{-1}Q\right\rangle_4
       +\frac{\mathfrak f_N}{\mu^2}\phi_0(g).
\quad}
\tag{21}
\]
Here \(U^{\mathrm t}=R^3T\), without scalar conjugation, and
\(U^{-1}Q=F\). No replacement of full by shortened first normals
is made in (21).

*Proof.* Apply the original bilinear pairing to
\((\mu^2-S^{\mathrm t}S)F=a_Ne_D\), with test
\(U^{\mathrm t}g\), and use (6),(15). Its first term is
\(\mu^2\phi_0(gUF)=\mu^2\phi_0(gQ)\). The factored term is
the opposite-grid pairing in (21). Its source is
\[
 a_N\phi_0(U^{\mathrm t}g\,e_D)
     =a_N\phi_0(gUe_D)
     =\mathfrak f_N\phi_0(g),
\]
by the exact socle identity in (17). Divide by \(\mu^2\).
\(\square\)

The coefficient of the retained source in (21) is exactly
\[
 \frac{\mathfrak f_N}{\mu^2}
  =\begin{cases}
      \displaystyle\frac{\kappa^3}{N^2\cos^2(\theta/2)},
                                    &N\text{ even},\\[1mm]
      0,&N\text{ odd}.
    \end{cases}
\tag{22}
\]
Since \(N\ge3\) gives \(\mu^2\ge3\), its absolute contribution
is at most \(4|\phi_0(g)|/(3N^2)\). This quantifies only the
explicit coefficient; it does not estimate the source-dependent
trace \(\phi_0(g)\) or the remaining signed pairing.

Equation (21) answers the finite trace-compatibility question for
this regular factor: the transpose and forcing are exact. The
remaining locality question is also explicit. The transformed test
is \(S R^3Tg\), and the lifted off-diagonal maps are
\(TR^3S^{\mathrm t}\) and \(SR^{-3}T\). No local intertwiner
has been proved that replaces these full turns by the two oriented
degree-eleven principal factors. Their source ranges, odd reflection
data, and any adequate inverse or observation estimate remain to be
established. The bilinear identity alone cannot select the favorable
oriented roots or suppress the original signed observation.
