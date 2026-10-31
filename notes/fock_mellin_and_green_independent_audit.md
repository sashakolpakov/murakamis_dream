# Independent audit of the normal Mellin and full Green maps

Audit, 27 October 2026. The normal Mellin map and relative
connection are sound. The revised Mellin section 2 and residual
normal-current section 6 explicitly retain both pivot lifts and
both projector extensions, with their correct normal rows.
There is no outstanding correction. The full discrete
Green/current calculation is sound and does not assert cancellation
of the remaining geometric boundary terms. No test reruns were needed.

## 1. The strict normal Mellin map

For \(A^N=U\),
\[
 D_{\mathrm{phys}}=A\partial_A+NU\partial_U
\]
preserves the relation, and
\(\nabla=D_{\mathrm{phys}}/N\) has
\(\nabla\operatorname{Log} U=1\). With the marked \(\alpha^N=U\),
the elements \(A/\alpha\), hence every \(\epsilon_j\),
are horizontal. The map
\[
 v_{rN+j}\longmapsto\epsilon_j(\operatorname{Log} U)^r/r!
\]
is therefore a topological linear isomorphism carrying
\(B\) to \(\nabla\), \(T\) to multiplication by \(\operatorname{Log} U\),
and the coherent kernel to \(\epsilon_jU^s\).
The averaged trace and its \(U=1\) value give precisely
the stated original vacuum cut.

There is a useful projector distinction. The coefficientwise
extension \(e_H\otimes I\) maps to \(f\mapsto\tau(f)1\).
The finite-rank ambient coupon \(i e_H\pi_0\) instead maps
to \(f\mapsto[\tau(f)]_{U=1}1\). Both recover the same
head cut; their whole-normal extensions are different.
The revised finite-vacuum row is exactly
\[
 [\nabla,\Gamma_U]f=-[\tau(\nabla f)]_{U=1}1:
\]
the derivative of the constant output of \(\Gamma_U\) is zero,
while \(\Gamma_U\nabla\) is its displayed evaluated trace row.
The coefficientwise projector commutes with \(\nabla\).

For \(\partial_\sigma-T\), the compatible normal direction
is \(B-\sigma\):
\[
 [B-\sigma,\partial_\sigma-T]=0.
\]
The two scalar commutators cancel with opposite signs.
Endpoint evaluation gives the degree-two corrections
\((B-\sigma,B,B-1)\), and direct differentiation of
\(e^{-\sigma T}h\) proves the transgression formulas.
Under Mellin transport the endpoint is exactly \(U\);
no specialization to one occurs before this identity.

The algebraic primitive obstruction is also valid.
A vacuum-preserving intertwiner on an algebraic finite
cover would give \(df=c\,dU/U\), \(c\ne0\).
On the compact normalized curve the right side has
nonzero residues at zeros/poles of \(U\), whereas
an exact algebraic differential has zero residues.
Ramification multiplies rather than kills the residue.
The formal logarithmic torsor avoids, rather than
contradicts, this global algebraic obstruction.

## 2. Two whole-normal lifts of the finite pivot

The displayed formulas in
[the Mellin note](fock_cyclic_normal_mellin_map.md)
are correct for the **root-reduced lift**
\[
 g_{\mathrm{red}}=x^{1-N}A^{-1},\quad
 D_{\mathrm{red}}=g_{\mathrm{red}}^{-1}e.
\]
They have adapters \(\alpha^{-1}\) and \(\alpha\),
and physical derivatives \(-g_{\mathrm{red}}\) and
\(+D_{\mathrm{red}}\), respectively.

The revised note separately retains the literal power
of \(K_U=xA^{-1}\):
\[
 g_{\mathrm{lit}}=K_U^{1-N}
   =x^{1-N}A^{N-1}=U g_{\mathrm{red}}.
\]
Its matching defect is \(D_{\mathrm{lit}}=U^{-1}D_{\mathrm{red}}\).
The adapters are then \(\alpha^{N-1}\) and
\(\alpha^{1-N}\), and
\[
 D_{\mathrm{phys}}(g_{\mathrm{lit}})=(N-1)g_{\mathrm{lit}},\qquad
 D_{\mathrm{phys}}(D_{\mathrm{lit}})=(1-N)D_{\mathrm{lit}}.
\]
Both choices give \(gD=e\) and the same finite source at
\(U=1\), but their individual normal jets differ. The revised
proof now states this \(U^{\pm1}\) adapter explicitly.

Residual normal-current section 6 is consistent with these
formulas. The divided Frobenius shift is \(-D_{\mathrm{phys}}\),
the averaged trace satisfies
\(\tau D_{\mathrm{phys}}=NU\partial_U\tau\), and its paired
matrix row has the same covariance for either lift.
Its coefficientwise extension is explicitly separated
from \(\Gamma_U\), so the latter's extra finite-vacuum
normal derivative has not been dropped.

The physical \(2\pi i\) caveat is correct:
\(\tau_{\mathrm{geo}}\operatorname{Log} A/H_N=\tau_{\mathrm{geo}}\operatorname{Log} U/(2\pi i)\).
The bare kernel \(U^{s_{\mathrm{Fock}}}\) therefore needs
\(s_{\mathrm{Fock}}=\tau_{\mathrm{geo}}/(2\pi i)\); its unit
endpoint cannot silently be identified with the
geometric unit meridian interval.

## 3. The universal Green formula and its signs

For \(D_i=S_i-1\), the exact product rule is
\[
 pD_if=D_i[(S_i^{-1}p)f]+(S_i^{-1}p-p)f.
\]
Iterating it in the stated word order gives the
displayed current formula. For
\(p_\alpha=\prod_i\binom{k_i}{\alpha_i}\), backward
differences of total degree \(>|\alpha|\) vanish;
at degree \(|\alpha|\), only \(\beta=\alpha\)
survives, with value \((-1)^{|\alpha|}\).
Using \(PI=0\) moves the divergence sum to the other
side, producing exactly the negative sign in the
definition of \(J_i\).

These are identities on entire zero-extended arrays.
The polynomial moment does not lose a support boundary,
and all currents remain finite. External Ore operators
commute with the index polynomials and internal shifts.

## 4. Transverse pushforward and the unresolved relative boundary

The formal current identity follows from the already
established interior identity by the same algebraic
product rule, with \(k_i=u_i/H\). No separate density
argument for polynomial logarithms is needed.
The transverse Gaussian translation identity kills
the transverse differences even with their insertions;
external coordinate/base shifts commute with the
recentered Wick construction. Exactly the two stated
framing differences remain.

For a translated chain,
\(\int_\Gamma(F_H^*J-J)=\int_{F_H\Gamma-\Gamma}J\);
the Cartan homotopy therefore has the stated boundary
sign. Its logarithmic loop changes the index lift by
\(2\pi i/H_N=N\), preserving the polynomial-current
jump. The complete residual Ward ideal does not set
these relative endpoints or carries to zero.

Finally, on the actual diagonal one-cut array,
\(CW=C_{N-1,N-1}W\). Thus the ordered divided row is
exactly that endpoint value, as claimed. This does
not create an additional independent framing index.

The Green note correctly presents a full scalar
certificate with a two-current geometric defect,
not a full geometric annihilation or survival theorem.
