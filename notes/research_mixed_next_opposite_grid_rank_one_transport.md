# Changing the spectral grid: the exact rank-one correction

Private finite-source deduction, 9 November 2026. Multiplication on the
opposite spectral grid differs from multiplication on the original grid
by a rank-one map. Transporting that map through the original turn and
crossing gives a precise correction to the cubic operator. This
transported operator is different from reducing the ordinary cubic
operator on the opposite grid: the two corrections have opposite signs.

Both characteristic polynomials and the complete source equations can
be computed exactly. In particular the ordinary opposite-grid operator
is invertible, but its inverse on the constant source has at least the
original inner exponential rate. Thus its small forcing cannot justify
a polynomial bound on its solution. No mathematical numerical evaluation
or change of a frozen source is used.

## 1. Canonical representatives and their common bilinear form

Fix \(N\ge3\), put \(D=N-1\), \(\eta=(-1)^D\), and write
\[
 P(X)=2T_N(X/2)+2,\qquad
 V=\mathbb C[X]_{\le D}.
 \tag{1}
\]
Here \(T_N\) in (1) is the Chebyshev polynomial; the original turn
operator will be denoted by \(T\). Use the canonical representative
of degree less than \(N\) to identify each of
\[
 \mathcal A=\mathbb C[X]/(P),\qquad
 \mathcal A^{\rm opp}=\mathbb C[X]/(P-4)
 \tag{2}
\]
with \(V\) as a vector space. This identification is not an algebra
isomorphism. Let \(Z_0,Z_4\) be their two multiplication-by-\(X\)
matrices on \(V\), and define
\[
 \phi(f)=\eta N^2[X^D]f\quad(f\in V),\qquad
 \gamma=\frac{4\eta}{N^2},\qquad
 \langle f,g\rangle=\eta N^2[X^D]\operatorname{rem}_{P}(fg).
 \tag{3}
\]
The same bilinear form is obtained using \(P-4\) in (3). Indeed,
if \(fg=PH+r\), then \(\deg H\le N-2\), and
\(fg=(P-4)H+(r+4H)\) is already its division by \(P-4\).
The top coefficient of the remainder has not changed.

The form is nondegenerate: if \(f\ne0\) has degree \(k\le D\),
then \(g=X^{D-k}\) gives a nonzero top coefficient without any
reduction. It is a bilinear Frobenius form, not a positive Hermitian
inner product. For example \(\langle1,1\rangle=0\).

For any vector \(a\in V\) and linear functional \(\ell\) on \(V\),
write \(a\otimes\ell\) for the map \(f\mapsto a\ell(f)\).
Polynomial division of \(Xf\) now gives
\[
 \boxed{\quad Z_4=Z_0+\gamma\,1\otimes\phi.\quad}
 \tag{4}
\]
In fact its quotient by either monic polynomial in (2) is exactly
\([X^D]f\), so the opposite remainder increases by
\(4[X^D]f\). No node or derivative data have been discarded in
this calculation.

## 2. The opposite multiplication transported through the turn

Keep the original Newton vectors \(e_j\), turn \(Te_j=e_{D-j}\),
and \(\mathcal L=TZ_0T\), with the full-source normalization of
[current-free transport](research_current_free_aw_crossing_transport.md).
In particular \(T^2=I\), \(T\) is self-adjoint for (3),
\(T1=e_D\), and \(Te_D=1\). Consequently
\[
 \widetilde{\mathcal L}_4:=TZ_4T
   =\mathcal L+\gamma e_D\otimes\langle e_D,\cdot\rangle.
 \tag{5}
\]
The characteristic polynomials are
\[
 \det(zI-\mathcal L)=P(z),\qquad
 \det(zI-\widetilde{\mathcal L}_4)=P(z)-4.
 \tag{6}
\]
This follows because multiplication on a monic polynomial quotient
has that polynomial as its characteristic polynomial, and \(T\)
is an involution. In particular no similarity can identify these
two matrices.

The ordinary Askey--Wilson operator \(\mathcal L\), applied to
a polynomial of degree at most \(D\), preserves that degree.
Its canonical matrix is therefore unchanged when reduced modulo
\(P-4\). Thus (5) is not the ordinary operator evaluated on the
opposite grid. It is the conjugate of opposite-grid multiplication
by the original turn. This distinction is already forced by (6).

The resolvent in (5) is explicit. For \(P(z)\ne0\), let
\[
 R_0(z)=(zI-\mathcal L)^{-1},\qquad
 H_z(X)=\frac{P(z)-P(X)}{z-X}.
 \tag{7}
\]
The divided difference \(H_z\) is an ordinary polynomial, monic
of degree \(D\) in \(X\). Since
\((z-X)H_z=P(z)-P(X)\), one has
\[
 R_0(z)e_D=\frac{T H_z}{P(z)},\qquad
 \langle e_D,R_0(z)e_D\rangle=\frac{\eta N^2}{P(z)}.
 \tag{8}
\]
For \(P(z)\ne0,4\), direct rank-one inversion gives
\[
 (zI-\widetilde{\mathcal L}_4)^{-1}
 =R_0(z)+\frac{\gamma P(z)}{P(z)-4}
       R_0(z)e_D\otimes\langle e_D,R_0(z)\cdot\rangle.
 \tag{9}
\]
To check (9), multiply by
\(zI-\mathcal L-\gamma e_D\otimes\langle e_D,\cdot\rangle\)
and use (8); the denominator is exactly
\(1-\gamma\langle e_D,R_0e_D\rangle=1-4/P(z)\).
The formula is an identity of rational matrices. At roots of \(P\),
the separate terms on its right are not assigned finite values.

The original ordinary kernel also has a useful divided-difference
description:
\[
 K_N^{\rm ord}(z,X)=\frac{\eta}{N^2}T H_z(X).
 \tag{10}
\]
Indeed its original full-kernel equation is
\((zI-\mathcal L)K_N^{\rm ord}(z,\cdot)
=\eta P(z)e_D/N^2\). For \(P(z)\ne0\), (8) proves (10);
both sides of (10) are polynomial in \(z\), so it holds at every
\(z\). In particular
\[
 \langle e_D,K_N^{\rm ord}(z,\cdot)\rangle=1,
 \qquad
 (zI-\widetilde{\mathcal L}_4)K_N^{\rm ord}(z,\cdot)
   =\frac{\eta}{N^2}(P(z)-4)e_D.
 \tag{11}
\]
These formulas retain the original kernel normalization. They do not
replace its final scalar evaluation by a different period.

## 3. The two cubic operators on the opposite grid

Write \(q=e^{i\pi/N}\), \(\kappa=q^{D^2/2}\), and let \(R\)
be multiplication by the original crossing on \(\mathcal A\).
Set
\[
 U=TR^3,\qquad
 \mathcal D_0=U(\mathcal L+2I)U^{-1},\qquad
 F=K_N^{\rm ord}(-2,\cdot),\qquad Q=UF.
 \tag{12}
\]
Thus \(\mathcal D_0\) is the original seven-term cubic operator
on its original quotient, and \(Q=Q_N^{\rm full}\).
All matrices in (12) are on the canonical space \(V\).

The original socle relations give
\[
 R^3e_D=\kappa^3e_D,\quad Ue_D=\kappa^3\,1,
 \quad\langle e_D,U^{-1}g\rangle=\kappa^{-3}\phi(g).
 \tag{13}
\]
For the last equality use \(U^{-1}=R^{-3}T\), the
self-adjointness of multiplication by \(R^{-3}\), and \(Te_D=1\).
Conjugating (5) consequently gives the transported matrix
\[
 \widetilde{\mathcal D}_4
 :=U(\widetilde{\mathcal L}_4+2I)U^{-1}
 =\mathcal D_0+\gamma\,1\otimes\phi.
 \tag{14}
\]

In contrast, let \(\mathcal D_4^{\rm ord}\) mean the original
ordinary seven-term operator, applied to \(f\in V\) and then
reduced modulo \(P-4\). The
[doubled-grid source proof](research_mixed_next_outer_doubled_grid_half_step.md)
establishes
\[
 \deg(\mathcal D_{3,N}^{\rm ord}f)\le N,\qquad
 [X^N]\mathcal D_{3,N}^{\rm ord}f=-[X^D]f.
 \tag{15}
\]
Here its unweighted Askey--Wilson operator preserves degree and its
weighted factor raises degree by at most one. Only the top input
monomial reaches degree \(N\), with coefficient \(-1\).
Reducing that output modulo \(P-4\), rather than \(P\), changes
its remainder by \(-4[X^D]f\). Therefore
\[
 \boxed{\quad
 \mathcal D_4^{\rm ord}=\mathcal D_0-\gamma\,1\otimes\phi,
 \qquad
 \widetilde{\mathcal D}_4-\mathcal D_4^{\rm ord}
      =2\gamma\,1\otimes\phi.
 \quad}
 \tag{16}
\]
This is an exact difference between two possible constructions, not
an asymptotic error or a choice of notation.

For clarity their characteristic polynomials can all be computed.
Equation (8), conjugation by \(U\), and (13) imply
\[
 \phi((zI-\mathcal D_0)^{-1}1)
             =\frac{\eta N^2}{P(z-2)}.
 \tag{17}
\]
The rank-one determinant identity now gives
\[
 \boxed{\begin{aligned}
 \det(zI-\mathcal D_0)&=P(z-2),\\
 \det(zI-\widetilde{\mathcal D}_4)&=P(z-2)-4,\\
 \det(zI-\mathcal D_4^{\rm ord})&=P(z-2)+4.
 \end{aligned}}
 \tag{18}
\]
For example the last determinant, initially away from the roots of
\(P(z-2)\), is \(P(z-2)(1+4/P(z-2))\); polynomial identity
extends it everywhere. This calculation uses no diagonalizability
assumption and therefore retains all Jordan data at double roots.

The complete source has \(\phi(Q)=\kappa^3\) and
\(\mathcal D_0Q=-\eta\kappa^3P(-2)1/N^2\), by the adopted
source equations. It follows that
\[
 \begin{aligned}
 \widetilde{\mathcal D}_4Q
   &=-\frac{\eta\kappa^3}{N^2}(P(-2)-4)\,1,\\
 \mathcal D_4^{\rm ord}Q
   &=-\frac{\eta\kappa^3}{N^2}(P(-2)+4)\,1.
 \end{aligned}
 \tag{19}
\]
The first forcing is zero at even levels and \(4\kappa^3/N^2\)
at odd levels. The second is \(8\kappa^3/N^2\) at even levels
and \(-4\kappa^3/N^2\) at odd levels, exactly as in the
ordinary doubled-grid theorem. The auxiliary transported construction
does not erase the latter forcing.

## 4. Invertibility does not make the complete opposite-grid solution small

Since \(P(-2)\) is either zero or four, the last line of (18)
shows that \(\mathcal D_4^{\rm ord}\) is invertible for every
\(N\ge3\). Equation (19) then determines its constant-source solution:
\[
 \boxed{\quad
 (\mathcal D_4^{\rm ord})^{-1}1
       =-\frac{\eta N^2}{\kappa^3(P(-2)+4)}Q.
 \quad}
 \tag{20}
\]
This gives a concrete lower bound on the inverse in the norm of
canonical polynomials
\[
                    \|f\|_\infty=\max_{-2\le X\le2}|f(X)|.
 \tag{21}
\]
Let \(j_N=\lfloor N/2\rfloor-1\). Its original double node
\(c_{j_N}=-2\cos u_N\) has \(u_N=\pi/N\) at even levels and
\(u_N=2\pi/N\) at odd levels. The
[physical inner-source theorem](research_mixed_next_inner_three_physical_outgoing_packet.md)
gives, uniformly at those nodes,
\[
 Q(c_{j_N})=C_{N,3}N^{-3/2}\mathcal A(u_N)e^{NS(u_N)}
                      (1+O(N^{-1})),\qquad |C_{N,3}|=1.
 \tag{22}
\]
Its full and shortened outgoing kernels coincide at this actual
double node by their exact terminating zeros. Thus (22) really
concerns the complete polynomial \(Q\) of (12).
The amplitude is uniformly nonzero. The adopted local action is
even and analytic at zero, so
\(S(u_N)=S(0)+O(N^{-2})\). With the original
\(\mathfrak M_3=\Re S(0)\), (20)--(22) imply that there is
\(c>0\), independent of the parity, such that for all sufficiently
large \(N\),
\[
 \boxed{\quad
 \|(\mathcal D_4^{\rm ord})^{-1}\|_{\infty\to\infty}
 \ \ge\ \|(\mathcal D_4^{\rm ord})^{-1}1\|_\infty
 \ \ge\ cN^{1/2}e^{N\mathfrak M_3}.
 \quad}
 \tag{23}
\]
Here \(\|1\|_\infty=1\), \(|\kappa|=1\), and
\(4\le P(-2)+4\le8\). This is an inverse lower bound in the
specified norm of canonical polynomials. It is not a norm comparison
with values alone on the opposite grid, and it is not a lower bound
for the remaining signed scalar observation.

The original observation still pairs \(Q\) against the complete
outgoing factor with its crossing and trace. Cancellation in that
pairing may be substantial even though (23) is large. What (23)
excludes is a direct argument that the opposite-grid equation, merely
because it has a small constant forcing and an inverse, produces a
polynomially bounded solution. An estimate exploiting the outgoing
factor and the scalar evaluation together remains necessary.

## Frozen sources

- Original turn, crossing, and full bilinear adjoints:
  f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a.
- Ordinary full-kernel equation:
  5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da.
- Original seven-term conjugation and complete source:
  49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
- Doubled grid, ordinary top-degree coefficient and source trace:
  0cc541295d0562af9d235e4d27f7e1cb329a2fdc14569629ef76b3b0cccbaa37.
- Nonzero physical inner-source asymptotic:
  c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3.
- Original selected action and its even local continuation:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
