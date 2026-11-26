# The integral marked logarithmic lattice of the reduced physical source

Private written proof, 17 November 2026. The original complete signed
source has an explicit integral logarithmic stationary presentation after
its finite singleton clocks are eliminated. Its rows, with their parity
constants and residual Fourier character, form a primitive Lagrangian
lattice for a **signed** shape symplectic form. The proof uses the actual
physical wire constraints and retains their closing degrees.

This concerns the complete fixed-root source and its marked leading
action. It is not a new exact quantum operator equation, a triangulation
identification, or a nonzero-period theorem. Full rank of the linear row
matrix does not assert transversality of the nonlinear critical equations.

## 1. Physical paths, action and branches

Use the original conventions of [Q] and [J]:
\(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and the balanced physical
crossing signs \(\sigma_j\). At crossing \(j\), the literal transfer and
over-output are \(u_j,v_j\); at closure \(i\), the degree is \(a_i\).
On each actual directed anchor segment,

\[
a_s+\sum_{j\text{ under on }s}u_j=b_s,
\qquad J_j=a_s+\sum_{\ell\text{ before }j\text{ on }s}u_\ell.
\tag{1}
\]

Here \(a_s\) is the starting \(v_j\) or closure degree, and \(b_s\)
is the ending \(u_j+v_j\) or closure degree. Write \(\Lambda\) for the
integer solutions of these homogeneous physical path equations. The
finite source uses the subset with
\(u,v\ge0\), \(u+v\le d\), \(0\le a_i\le d\); its exact clock
fibers are \(0\le h_j-v_j\le u_j\). Their full finite binomial sums,
including all endpoints and signs, are [Q, (10)--(11)]. They recover
the original physical matrices before taking a limit.

For scaled variables \(U=u/N,V=v/N,J=J_j/N\), that reduction has the
calibrated local primitive

\[
\begin{split}
G_\sigma={}&\mathcal J(U+V)+\mathcal J(J+U)
 -\mathcal J(V)-\mathcal J(J)-\mathcal J(U)+\pi i\sigma\psi,\\
\psi={}&-J-V+2VJ-U/2+U(J+V)+U^2/2,
\qquad \mathcal J'(t)=\log(2\sin\pi t).
\end{split}
\tag{2}
\]

The branch is calibrated on
\(U,V,J>0\), \(U+V<1\), \(U+J<1\), separately at each crossing,
and then continued on the same lifted regular clock graph. No global
real interior physical path is assumed for a closed diagram.
Set

\[
\alpha=(U+V,J+U,V,J,U),\quad
E_0=\operatorname{diag}(1,1,-1,-1,-1),\quad
z_a=e^{2\pi i\alpha_a},\quad \lambda_a=2\pi i\alpha_a,
\quad \mu_a=\Log(1-z_a).
\tag{3}
\]

The \(\mu_a\) start with their principal values on the displayed real
strip, then continue with the source. The symbols \(\lambda_a\) are
unwrapped logarithms of \(z_a\); they are not reset to principal values.
All subsequent logarithmic identities use these lifts. On that strip,
and hence by continuation,

\[
\log(2\sin\pi t)=\Log(1-e^{2\pi it})+\pi i(1/2-t).
\tag{4}
\]

We work away from the divisors where these logarithms or the regular
clock elimination fail. Such divisors and finite boundary states are
not removed from the original source by this restriction.

## 2. The complete local integer tables

In coordinate order \((U,V,J)\), let

\[
T_0=\begin{pmatrix}1&1&0&0&1\\1&0&1&0&0\\0&1&0&1&0\end{pmatrix},
\qquad
B_0=T_0E_0=
\begin{pmatrix}1&1&0&0&-1\\1&0&-1&0&0\\0&1&0&-1&0\end{pmatrix}.
\tag{5}
\]

The following matrices and column covectors include every constant:

\[
\begin{array}{c|c|c}
\sigma&A_\sigma&\nu_\sigma\\\hline
+1&\begin{pmatrix}0&0&0&0&0\\0&0&0&1&0\\0&0&1&0&0\end{pmatrix}
 &\begin{pmatrix}0\\-1\\-1\end{pmatrix}\\[3pt]
-1&\begin{pmatrix}-1&0&0&-1&0\\0&-1&0&0&0\\-1&0&0&0&0\end{pmatrix}
 &\begin{pmatrix}1\\1\\1\end{pmatrix}.
\end{array}
\tag{6}
\]

For any local tangent \(\ell=(\dot U,\dot V,\dot J)\), as a row,

\[
D_\ell G_\sigma
 =\ell A_\sigma\lambda+\ell B_0\mu+\pi i\ell\nu_\sigma.
\tag{7}
\]

Here and below \(\lambda,\mu\) are column vectors. To verify all signs,
put \(A_0=U^2/2+U(V+J)\). Then
\(\sum_a(E_0)_{aa}\alpha_a=U\) and
\(\frac12\sum_a(E_0)_{aa}\alpha_a^2=A_0\). Equations (2)--(4) give

\[
dG_\sigma=\sum_a(E_0)_{aa}\,d\alpha_a\,\mu_a+\pi i\,dQ_\sigma,
\quad
\begin{cases}
Q_+=2VJ-V-J,\\
Q_-=-U^2-2U(V+J)-2VJ+U+V+J.
\end{cases}
\tag{8}
\]

For the positive sign the extra terms are
\(\dot V\lambda_J+\dot J\lambda_V-\pi i(\dot V+\dot J)\).
For the negative sign they are

\[
-\dot U(\lambda_U+\lambda_V+\lambda_J)
-\dot V(\lambda_U+\lambda_J)-\dot J(\lambda_U+\lambda_V)
+\pi i(\dot U+\dot V+\dot J).
\tag{9}
\]

Using \(\lambda_1=\lambda_U+\lambda_V\),
\(\lambda_2=\lambda_U+\lambda_J\), and \(\lambda_4=\lambda_J\)
is exactly the integer choice (6). Thus no half-integer coefficient
has been hidden in a branch or parity convention.

## 3. The actual global shape embedding is primitive

Separate any closed wire component that never encounters a crossing.
Its original finite closing sum, pivot and mark remain a separate factor,
which need not be nonzero. The five crossing arguments do not see its
degree. In the following, \(\Lambda\) denotes the remaining physical
lattice, so every retained wire component encounters a crossing.

Let \(r=\operatorname{rank}\Lambda\), \(m=5c\). Choose an integral
basis of \(\Lambda\). The linear map

\[
\iota:\Lambda\longrightarrow\mathbb Z^m,
\qquad p\longmapsto
 (u_j+v_j,J_j+u_j,v_j,J_j,u_j)_{j=1}^c
\tag{10}
\]

has matrix \(T\) in row convention: a coordinate row \(y\) maps to
\(yT\). This map is injective and its image is primitive.

Indeed the columns of (10) recover every \(u_j,v_j,J_j\) integrally.
For any closure degree \(a_i\), follow its actual wire to a crossing.
Along under encounters the degree changes by the corresponding integer
\(u_j\); at an over encounter the input and output are \(u_j+v_j\)
and \(v_j\). Consequently \(a_i\) is one such known crossing degree
minus a signed integral sum of the intervening transfers. All closure
degrees are thereby recovered, with no division. This proves injectivity.
If \(\iota(p)=n z\), \(n\ne0\), those same recovery formulas show
that every coordinate of \(p\) is divisible by \(n\). The homogeneous
integer equations (1) then imply \(p/n\in\Lambda\), and
\(z=\iota(p/n)\). This is primitivity, including at even and composite
levels. It concerns the lattice; it does not replace the finite capacity
inequalities by a product box.

Let \(P_j\) be the integral \(r\)-by-3 matrix that sends a physical
tangent to its \((\dot U_j,\dot V_j,\dot J_j)\) increments. All prefix
histories and closing variables enter these matrices through (1). Put

\[
E=\operatorname{diag}(E_0,\ldots,E_0),\quad
T=(P_jT_0)_j,\quad A=(P_jA_{\sigma_j})_j,
\quad B=TE,\quad \nu=\sum_jP_j\nu_{\sigma_j}.
\tag{11}
\]

Then the exact differential of the reduced leading action
\(G=\sum_jG_{\sigma_j}\) is
represented by the column \(A\lambda+B\mu+\pi i\nu\) in this integral
basis: evaluation on a tangent row \(y\) is multiplication by \(y\).

## 4. The marked stationary system and its signed Lagrangian lattice

Let \(R\) be an integral basis of the annihilator of \(\iota(\Lambda)\).
It has \(m-r\) independent rows and satisfies \(RT^{\mathsf T}=0\).
The unwrapped physical shape coordinates obey \(R\lambda=0\).
On the same lifted regular clock graph, [Q, (17)] supplies the residual
integral character \(\bar\chi\in\Lambda^*\). In the chosen basis the
marked equations are exactly

\[
\boxed{\quad
\begin{pmatrix}A&B\\R&0\end{pmatrix}
\binom{\lambda}{\mu}
=\pi i\binom{2\bar\chi-\nu}{0},
\qquad z_a=e^{\lambda_a},\quad \mu_a=\Log(1-z_a).
\quad}
\tag{12}
\]

Thus their multiplicative equations are
\(\prod_a z_a^{A_{ia}}(1-z_a)^{B_{ia}}=(-1)^{\nu_i}\) and
\(\prod_a z_a^{R_{ka}}=1\), with precisely the lifts in (12).
Exponentiation alone loses \(\bar\chi\) and the monomial lifts.

On row pairs in \(\mathbb Z^m\oplus\mathbb Z^m\) use the unimodular
alternating form

\[
\omega_E((a,b),(a',b'))=aEb'^{\mathsf T}-bEa'^{\mathsf T}.
\tag{13}
\]

The rows of (12) span a primitive Lagrangian lattice for (13).
For isotropy, directly from (5)--(6),

\[
A_+T_0^{\mathsf T}=
\begin{pmatrix}0&0&0\\0&0&1\\0&1&0\end{pmatrix},\qquad
A_-T_0^{\mathsf T}=
\begin{pmatrix}-1&-1&-1\\-1&0&-1\\-1&-1&0\end{pmatrix}.
\tag{14}
\]

Both are symmetric. Hence
\(AEB^{\mathsf T}=AT^{\mathsf T}
=\sum_jP_j(A_{\sigma_j}T_0^{\mathsf T})P_j^{\mathsf T}\)
is symmetric, and \(REB^{\mathsf T}=RT^{\mathsf T}=0\).
The \((R,0)\) rows pair to zero with one another. These are all pairs.
In particular the sign matrix \(E\) is essential; it is not replaced
by the unsigned shape pairing.

The rows have rank \(m\): \(B=TE\) has rank \(r\), so a relation
among them first kills the stationary-row coefficients, then the
independent \(R\)-row coefficients. For saturation, suppose
\(n(a,b)=u(A,B)+v(R,0)\) with integral row coefficients. The row lattice
of \(B\) is primitive by Section 3, so \(b=u_0B\) for an integral
\(u_0\); its independence gives \(u=nu_0\). Thus
\(n(a-u_0A)=vR\). The row lattice of \(R\), being an integral
annihilator, is primitive,
so \(a-u_0A\) is an integral combination of its rows. Therefore
\((a,b)\) belongs to the displayed row lattice. This proves saturation.
An isotropic primitive half-rank lattice in (13) equals its integral
orthogonal complement, proving the assertion.

Locally the two monomial rows are explicitly
\((1,0,-1,0,-1)\) and \((0,1,0,-1,-1)\). Together with (6),
they give the rank-five version of this same proof. Globally \(R\)
also contains the actual port-gluing and closing relations from (1).

## 5. Exact finite marks and the remaining geometric comparison

The preceding matrices present the leading stationary equations of
the actual source. Their branch calibration does not change its finite
weights. In [Q] the canonical clock covector is
\(\chi_0=\sum_j(1+\sigma_j)h_j/2\), and
\(\chi-\chi_0=\pi^*\bar\chi\) on the same lifted clock graph.
For every literal finite incidence state \(n\) and its physical image
\(p\),

\[
q^{\Phi_N(n)-2N\chi_0(n)}=q^{\Phi_N(n)},\qquad
e^{-2\pi i\bar\chi(p)}=1.
\tag{15}
\]

After scaling, these are exactly the clock correction and the residual
Fourier correction \(-2\pi i\bar\chi\) to the leading primitive.
They are discrete character identities, not generic-meridian or
off-root quantum-normal identities.

All finite pivot terms remain: in the source exponent of [Q, (9)]
they include \(-2\sum_{i>1}a_i\). Their contribution is order one in
the total exponent rather than order \(N\), so they are absent from
the leading differential (7), not discarded from the source. The
state-independent \(\chi_N/N\), \(\kappa^{\sum\sigma_j}\), and
\(\eta^{b-1}\) also remain with the original marked first cut.
The calibration (2) preserves its specified additive constants.

The existing comparison is stronger than a purely formal resemblance:
[J, Section 5] identifies the regular reduced critical correspondence
with the actual marked meridian holonomy, retaining its momentum
normalization. [F] identifies its complete rational Bloch class with
the degree-one fundamental class and its regulator with volume.
Those facts give a geometric critical point in this source chart.
They do not identify the primitive lattice (12), its parity column,
and its character with the integral edge/peripheral flattening data of
an arbitrary positive triangulation.

Precisely, [F] passes through three five-term boundaries and the
rational cancellation \([z/(z-1)]=-[z]\). A stronger comparison must
transport the logarithmic lifts, the \(\pi i\) constants in (12),
and the marked peripheral correction through those steps and the
actual face pairings. The rational Bloch identity forgets that data.
Nor does it transport the original finite source or its relative
cycle. Thus the five formal arguments per crossing are not asserted
to be tetrahedra of a positive triangulation. Linear Lagrangian rank
does not remove nonlinear framing tangents or prove a nonzero
geometric coefficient. No new finite normal-ordering or quantum
annihilation equation is inferred from (12).

## Direct source versions

All three complete texts were read at these versions. No programs,
tests, numerical results, or public/frozen edits are used.

| Label | Source | SHA-256 |
| --- | --- | --- |
| Q | [Clock quotient and affine winding](research_original_clock_quotient_and_affine_winding.md) | 68166d94943bef0f0bddb6b284eae9a830d74978719f42f33d5d4f6175451138 |
| J | [Original joint clock phase](research_joint_clock_phase_equations.md) | 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867 |
| F | [Crossing fundamental cycle](crossing_fundamental_cycle.md) | 0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f |
