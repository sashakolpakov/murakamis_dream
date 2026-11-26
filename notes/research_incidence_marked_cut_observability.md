# The exact marked-cut restriction of the incidence polynomial

Private written proof, 15 November 2026. The incidence cycle equations
determine the full coefficient array from one coefficient. This note
computes a particular observation of that array using the original
closing operator. For every complete braid intertwiner, its restriction
to the marked closing fugacity is the original scalar times a universal
geometric sum. This gives an exact transport with uniformly bounded
comparison factors, but also forced zeros at distance of order \(1/N\)
from the prescribed evaluation. All derivatives along this line still
contain the same unknown original scalar.

No numerical calculation, mathematical code, or saved numerical result
is used. The conclusion concerns an auxiliary closing fugacity, not the
meridian variable of the reduced ADO period.

## 1. The actual closing line

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
Use the original incidence polynomial of
[the cycle-equation theorem](research_incidence_cycle_difference_equations.md):
\[
 F_N(z)=\sum_{n\in\mathcal F_d}w_N(n)z^n,
 \qquad
 w_N(n)=\frac{q^{\Phi_N(n)}}{\prod_eS_{n_e}},\qquad
 S_a=\prod_{r=1}^a2\sin(\pi r/N),\quad S_0=1.
 \tag{1}
\]
Every incidence remains distinct. The complete quadratic phase,
including all closing pivots, is the phase in that theorem.
The original invariant is \(\gamma_NF_N(\mathbf1)\), where
\(\gamma_N\ne0\) is its specified external factor, independent of
the incidence state. It is not defined by division by the invariant.

At the unpivoted marked closing event the two incidence charges are
\((d-a_1,a_1)\). Let \(e_*\) be the second incidence, carrying the
transmitted physical degree \(a_1\). Define the actual one-variable
restriction
\[
 f_N(t)=F_N(z_e=1\ (e\ne e_*),\ z_{e_*}=t),
 \qquad D_N(t)=\frac1N\sum_{a=0}^{N-1}t^a.
 \tag{2}
\]
The marked incidence can be parallel to another incidence; it is not
merged with it. All other fugacities are set to their prescribed values.

**Theorem.** For every complete signed braid with its original closing,
\[
                  \boxed{f_N(t)=F_N(\mathbf1)D_N(t).}
 \tag{3}
\]
This is a polynomial identity, including when \(F_N(\mathbf1)=0\).
It remains true after any fixed signed tangle insertion assembled into
such an original intertwiner. The statement is about the complete
assembled operator, not an individual clock sector or an arbitrary
degree-changing coupon.

**Proof.** Let \(W_N\) be that operator on \(b\) original heads, and
let \(g\) be the actual pivotal matrix. The whole-source formula is
\[
 K_N=\frac{\chi_N}{N}
       \operatorname{Tr}[(I\otimes g^{\otimes(b-1)})W_N].
 \tag{4}
\]
The specified scalar \(\chi_N\ne0\) includes the exterior normalization.
The original partial trace
\[
 C_N=\operatorname{Tr}_{2,\ldots,b}
       [(I\otimes g^{\otimes(b-1)})W_N]
 \tag{5}
\]
is a Hopf endomorphism of the remaining head. The finite proof in
[the prescribed-cut theorem](research_rivin_jones_prescribed_cut_and_hermite_recovery.md),
Section 2, applies: cyclicity of the tail trace and the actual
coproduct make \(C_N\) commute with the first-head generators.
The Cartan eigenvalues are distinct and the adjacent raising/lowering
arrows are nonzero. Thus \(C_N=c_NI\). This also holds for one head.

Let \(A_t=\operatorname{diag}(1,t,\ldots,t^d)\). The alias-free
incidence expansion of (4), with this diagonal insertion on the first
head, multiplies every term by precisely \(t^{a_1}\). It does not
change its support or its coefficient normalization. Therefore
\[
 \gamma_N f_N(t)
   =\frac{\chi_N}{N}\operatorname{Tr}(A_tC_N)
   =\chi_Nc_ND_N(t).
 \tag{6}
\]
At \(t=1\), (4) gives \(\gamma_NF_N(\mathbf1)=\chi_Nc_N\).
Canceling only the known nonzero \(\gamma_N\) proves (3).
The argument never divides by \(c_N\) or the knot invariant. \(\square\)

The use of scalarity is legitimate before this one-parameter insertion:
the complete original \(W_N\) is an intertwiner. If other incidence
fugacities are left arbitrary, the resulting operator need not be an
intertwiner. In particular, (3) does not assert that \(D_N(t)\) divides
the full multivariable polynomial.

## 2. Exact transport and its source

The polynomial \(D_N\) has the whole expression
\[
 D_N(t)=\frac{1-t^N}{N(1-t)},\qquad D_N(1)=1.
 \tag{7}
\]
Its two exact shift laws give
\[
 \boxed{(1-Qt)f_N(Qt)=(1-t)f_N(t),}
 \tag{8}
\]
and
\[
 \boxed{(1-qt)f_N(qt)-(1-t)f_N(t)
                  =\frac{2t^N}{N}F_N(\mathbf1).}
 \tag{9}
\]
These follow by using \(Q^N=1\) and \(q^N=-1\) in (7).
There are no omitted endpoint terms. The right side of (9) contains
the unknown prescribed scalar itself. Thus (9) is not an affine
source equation with independently known forcing, of the type used
in [the affine quantum-A period theorem](affine_quantum_a_period.md).

There is nevertheless a useful uniformly bounded transport to the
midpoint between adjacent \(Q\)-orbit points:
\[
 f_N(q)=\frac{2F_N(\mathbf1)}{N(1-q)},\qquad
 \frac2\pi|F_N(\mathbf1)|\le |f_N(q)|\le |F_N(\mathbf1)|.
 \tag{10}
\]
Indeed the magnitude of the coefficient is
\(1/[N\sin(\pi/(2N))]\); the inequalities
\(2x/\pi\le\sin x\le x\) on \([0,\pi/2]\) prove (10).
The exact identity and both inequalities remain valid if the scalar
vanishes. They move the same unknown observation without an
exponential normalization cost; they supply no absolute lower bound.

Among polynomials of degree at most \(d\), equation (8) itself has
the one-dimensional solution space spanned by \(D_N\). In fact, if
\(f(t)=\sum_{a=0}^df_at^a\), comparing its coefficient at
\(t^a\), \(1\le a<N\), gives
\((Q^a-1)(f_a-f_{a-1})=0\), so all coefficients coincide.
The coefficients at zero and \(N\) give identities. This shows
explicitly how a rigid restricted equation can still leave its
original closing multiplier undetermined.

## 3. Forced zero locus and the exact scalar connection

If \(F_N(\mathbf1)\ne0\), the zeros of \(f_N\) are exactly the
simple points
\[
                   t=Q^j,\qquad 1\le j<N.
 \tag{11}
\]
If \(F_N(\mathbf1)=0\), the entire restriction is zero. In either
case all the nontrivial \(Q\)-orbit evaluations vanish. The closest
forced zeros have distance \(2\sin(\pi/N)\) from \(1\).
Hence even a nonzero original scalar does not produce an
\(N\)-independent zero-free complex neighborhood of the prescribed
point in this actual source direction.

For fixed derivative order \(r\ge0\), the logarithmic moments are
exactly
\[
 \left.(t\partial_t)^r f_N(t)\right|_{t=1}
       =\frac1N\sum_{a=0}^{N-1}a^r\,F_N(\mathbf1),
 \tag{12}
\]
where the \(r=0\) sum is \(N\). Thus even the entire germ on this
line vanishes when the original scalar vanishes. It cannot provide
an independent nonzero pointing for that scalar.

On its nonzero locus the exact logarithmic derivative is
\[
 \partial_t f_N(t)=a_N(t)f_N(t),\qquad
 a_N(t)=\frac1{1-t}-\frac{Nt^{N-1}}{1-t^N}.
 \tag{13}
\]
At \(t=1\) the apparent singularity is removable, with value
\((N-1)/2\). At every point in (11), \(a_N\) has a simple pole
of residue one. No holomorphic first-order scalar connection on a
fixed neighborhood of \(1\) can transport a nonzero \(f_N\) for
all sufficiently large \(N\): a nonzero solution of such a scalar
equation has no zeros in its connected domain. Equation (13)
identifies the required moving singularities explicitly.

The microscopic behavior is equally explicit. Uniformly for \(s\)
in each fixed compact complex set,
\[
 D_N(e^{s/N})=\frac{e^s-1}{s}+O(N^{-1}),
 \tag{14}
\]
with the removable value one at \(s=0\). This follows by expanding
\(N(e^{s/N}-1)=s(1+O(N^{-1}))\), keeping the removable factor at
zero. Thus the nearby zeros belong to the actual source profile;
they are not an artifact of a norm estimate.

## 4. Relation to period rigidity and the remaining estimate

The earlier [general flow fusion](actual_general_flow_fusion.md),
Section 2, already gives the full-block geometric sum and its even/odd
root values. What is added here is its universal occurrence after
the entire intertwiner has been closed, as the exact restriction of
the new incidence polynomial. The statement is independent of braid
width, crossing signs and the chosen fixed short insertion.

The cycle theorem's normalized coefficient array is still unique.
Restriction (2) takes its one-dimensional solution line to
\(\mathbb C D_N\) with multiplier \(F_N(\mathbf1)\); that
restriction can be zero only if the actual prescribed observation
is zero. This makes no alternative choice of a source or an array.
It identifies the additional scalar whose estimate coefficient
rigidity does not supply.

This agrees with the distinction in
[the closed-braid period line](closed_braid_period_line.md), Section 2:
an invertible intertwiner frame and its evaluated cut are different
objects. It also agrees with the function-level source distinction in
[the global period audit](global_period_rigidity_function_audit.md).
Those general distinctions alone did not give (3) or (10).

The fixed-presentation hypothesis in
[whole-period cyclotomic rigidity](whole_period_cyclotomic_rigidity.md)
is relevant to (7). Its degree in \(t\) grows with \(N\), but retaining
the power coordinate \(w=t^N\) gives the fixed whole expression
\((1-w)/(N(1-t))\). Its value at \(t=w=1\) must be taken on that
power graph, with the removable germ retained. Dividing out this
known whole factor leaves exactly the constant \(F_N(\mathbf1)\),
not a new computation of it. Nor is this auxiliary \(t\) automatically
the meridian parameter of an actual quantum-A equation.

Consequently (10) is an exact controlled transport of the prescribed
observation, and (11)--(13) obstruct a particular zero-free scalar
transport argument. Neither proves or disproves nonvanishing of the
original invariant at any level. A phase-sensitive lower bound in a
transverse source direction, or a nonzero geometric projection of the
actual closing, is still required for the finite-exception target.

## Direct written source versions

All directly used implications were read at these SHA-256 versions.

| Source | SHA-256 |
| --- | --- |
| `research_incidence_cycle_difference_equations.md` | `8d9b4231b2f3a8795b857f361b2054d50a727392457a378a12adb4fe0430e618` |
| `actual_global_charged_bridge_flow.md` | `b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c` |
| `research_rivin_jones_prescribed_cut_and_hermite_recovery.md` | `1b0e105ffb67b2b8552f5fddc5f0a3ac009e9795b33e27599ac4726ebd74079e` |
| `closed_braid_period_line.md` | `cdb5cd8402f17d975a923951d156a6092a9cb5291e8348035fb81623d80f8529` |
| `affine_quantum_a_period.md` | `ea09b1967caa38c3b4c81cf01ee4a265142d874a37dd390be2cfbb59150f6819` |
| `global_period_rigidity_function_audit.md` | `d9cd5f85648be196cb803c2890848f7d5d38057f58e778a26ce5c377ffd8fd84` |
| `whole_period_cyclotomic_rigidity.md` | `587d7d39e13769159e8bc0c8fee4d45820216773797d7f0ef8776f875d720210` |
| `actual_general_flow_fusion.md` | `708929d138a1cdcadc74cfde2f7e0a6857f3a0cad63dfffa6de419a4098d65aa` |
