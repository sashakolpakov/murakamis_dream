# Recovering the knot volume from a pointed quantum \(A\)-operator

1 November 2026.

A recurrence operator does not determine a knot invariant by itself: a recurrence usually has many solutions. It must be supplied with initial values selecting the knot's solution. In this note, **pointing** means fixing that initial data once and for all from finitely many ordinary colors. The resulting operator period is an exact reconstruction of the reduced Kashaev invariant.

At a root of unity, some coefficients of the recurrence may have poles when solved in forward form. The reconstruction keeps the whole Laurent expansion, so those poles can cancel before evaluation. Only a bounded number of derivatives of the initial data is needed, with a bound determined by the fixed operator and independent of the quantum level.

For the knots of the [net-twist theorem](actual_conway_net_twist_volume.md) and its [closure extension](actual_conway_arbitrary_closure_volume.md), this exact reconstruction has exponential growth equal to the knot complement volume. Every admitted knot is isotopic to a sufficiently long strict Conway knot. The closure extension also allows cap closures and zero sums, retaining the connected-sum factors until the hyperbolic input is shown to equal one strict factor. The proof transfers the invariant-volume theorem through an exact identity. For the covered circle-tree presentations, the [geometric longitude theorem](actual_all_circle_geometric_characteristic.md) also identifies the selected classical geometric factor. Other strict presentations and full quantum-module comparisons require further work.

The same reconstruction and volume conclusion also apply to the
[quantitative circle-tree theorem](actual_all_circle_quantitative_volume.md),
under its explicit condition
\(\sum_vd_v/(d_v^2+n_v^2)\le2^{-25}\).
Alternatively, the [local tree criterion](actual_all_circle_local_message_volume.md)
\(\max_vd_v/(d_v^2+n_v^2)\le2^{-120}\) supplies the same conclusion.
The exact operator identity is valid for every knot; the new theorem
supplies its volume growth, including the short powers admitted by
that criterion. No long-twist assumption is added in this application.

## 1. The knot and the two meridian coordinates

Fix a knot supplied by either reduction theorem. Its original construction is isotopic to a strict presentation \(\tau=C(FG)\) whose combined twist numbers satisfy the long-twist bound. In what follows, \(\mathbf n\) denotes those combined numbers, and \(\tau\) denotes the reduced presentation. Its basic boxes are \(h_i=T(R^{n_i})\), where \(R^{n_i}\) is an integral two-strand braid and \(T\) turns a box through a quarter-turn. The actual closed link has one component, including the count of any circles closed inside intermediate boxes. Set

\[
 K=K_\tau(\mathbf n),\qquad
 V=\operatorname{Vol}(S^3\setminus K)>0,\qquad
 q_N=\exp(\pi i/N).
\tag{1}
\]

For the quantitative application, use the original ordered circle
tree and its powers satisfying either the summed or local criterion in place of the
long-twist presentation just described. The symbols \(K,V,q_N\) have
the same meanings in (1), and all subsequent recurrence constructions
are unchanged.

The expression and every integer weight remain fixed while \(N\) grows. All auxiliary crossing-circle cusps have been filled to insert these twists; the main knot cusp is unfilled. The theorem below includes all sufficiently large integer levels, both parities and composite levels.

We use the zero-framed reduced ADO family, named for Akutsu, Deguchi and Ohtsuki, defined by the specified unrolled crossings and pivotal trace. “Reduced” fixes the scalar normalization, with the ordinary unknot value equal to one. The [ADO pointing note](kashaev_ado_pointing.md) proves the comparison with the reduced enhanced Kashaev evaluation used for the volume theorem.

Two coordinates must be distinguished:

\[
 x=q_N^\alpha,\qquad M=-q_Nx,\qquad
 F_N(M)=f_N(-q_N^{-1}M),
\tag{2}
\]

The parameter \(\alpha\) is the unrolled color, \(x\) is its raw exponential coordinate, and \(M\) is the marked meridian coordinate. The change \(M=-q_Nx\) includes a sign and a quantum shift. In particular, the complete color \(\alpha=N-1\) gives \(x=-q_N^{-1}\) and \(M=1\). The quotient color \(\alpha=j-1\) gives \(x=q_N^{j-1}\) and \(M=-q_N^j\).

The [single-component quotient-color theorem](root_orbit_pointing.md) proves

\[
 F_N(-q_N^j)=C_j(q_N)\quad(1\le j\le N),\qquad
 F_N(1)=C_N(q_N)=K_N(K).
\tag{3}
\]

Here \(C_j(q)\) is the zero-framed reduced period of the ordinary \(j\)-dimensional color. For each fixed \(j\), it is a Laurent polynomial in the stated quantum parameter, is analytic at \(q=1\), and satisfies \(C_j(1)=1\). The equalities follow from the invariant quotient of the color and the single-cycle cut trace. The one-component hypothesis matters; the argument is not an extrapolation from an arbitrary component of a link.

An **annihilator** is a recurrence operator that sends this ADO family to zero. The all-level annihilator ideal consists of operators whose equations hold for the actual family at all but finitely many levels. This is the convention of [Brown–Dimofte–Garoufalidis–Geer, equation (1.5)](https://arxiv.org/html/2005.08176). Their holonomicity and ideal-comparison theorems are not inputs to the proof here; the finite cut-state argument gives existence directly.

## 2. A fixed recurrence exists for every knot

The [finite cut-state annihilator theorem](finite_sum_annihilator.md) constructs a nonzero level-independent operator for every knot, before any period is evaluated. Its auxiliary generic-\(q\), \(N\)-dimensional matrices specialize to the actual root-of-unity source. Away from the root they serve as algebraic tools and are not asserted to define a topological invariant.

The source is a finite sum over an integral support polytope. Its summands are proper \(q\)-hypergeometric products: shifting an index changes a summand by a rational expression in the relevant powers of \(q\). The proof must keep the boundary of the sum, since a recurrence for interior summands alone need not be a recurrence for the sum.

Here is the dimension argument, including those boundaries. Suppose there are \(s_0\) internal summation indices. The operators

\[
 x^a z^c T^b S_1^{\beta_1}\cdots S_{s_0}^{\beta_{s_0}},
 \qquad 0\le a,c,b,\beta_i\le R,\qquad z=q^N,
\tag{4}
\]

use \(T\) to shift the external variable and \(S_i\) to shift the internal indices. In this operator note, \(T\) denotes a shift operator; it is not the tangle quarter-turn used in the construction of the knot. The variable \(z=q^N\) keeps the level dependence algebraic, and the integer \(R\) in (4) is a degree cutoff for the counting argument, not a crossing operator.

The span of the actions in (4), including the zero-extended boundary values, has dimension \(O(R^{s_0+2})\). A boundary stratum of rank \(r\) has \(O(R^r)\) labels and remaining span \(O(R^{s_0+2-r})\), so it has the same total order. There are \(O(R^{s_0+3})\) formal operators. For large \(R\), linear dependence therefore gives a nonzero relation without internal multiplication variables.

Direct summation of that first relation can vanish identically. The proof avoids losing the relation by taking its first nonzero coefficient at \(S_i=1\), using finite exponential moments. Finally, a common factor \((z+1)^h\) is canceled over generic \(q\) before setting \(z=-1\). The generic lift is regular at \(q_N\). Thus neither the finite support nor a factor vanishing at the root is discarded by specialization.

Transport the raw-coordinate relation by \(x=-q^{-1}M\), choose a fixed genuine annihilator, and clear its rational denominators. It has the form

\[
 P(q,M,T)=\sum_{i=0}^{d}a_i(q,M)T^i,\qquad
 TM=qMT,\qquad
 a_i\in\mathbb C[q^{\pm1},M^{\pm1}],\qquad d\ge1.
\tag{5}
\]

The relation \(TM=qMT\) means that applying \(T\) shifts the meridian argument from \(M\) to \(qM\). It explains why the operator is noncommutative. Remove a common shift if necessary so that \(a_0a_d\ne0\). For all but finitely many levels,

\[
 \sum_{i=0}^{d}a_i(q_N,M)F_N(q_N^iM)=0.
\tag{6}
\]

An order-zero nonzero multiplication operator cannot annihilate the nonzero family, so \(d\ge1\) is automatic. In the localized skew polynomial ring over \(\mathbb C(q,M)\), division on the left gives a unique monic annihilator of least order. One may use this generator or any other specified genuine operator in what follows. The existence argument does not compute the minimal generator efficiently or identify its classical symbol. In particular, the operator is not chosen anew at each level as the ratio \(F_N(q_NM)/F_N(M)\).

## 3. Fixed small colors select the knot's solution

The [all-level finite-pointing theorem](all_level_a_period.md) reconstructs the complete color from the operator and a fixed initial window. First fix an ordinary color \(j\). Substituting the quotient-color identities (3) into (6) shows that

\[
 H_j(q)=\sum_{i=0}^{d}a_i(q,-q^j)C_{j+i}(q)
\tag{7}
\]

vanishes at every sufficiently large \(q_N\) with \(N\ge j+d\). This is a Laurent polynomial in \(q\). Multiplying by a power of \(q\) makes it a polynomial, and the infinitely many zeros accumulating at \(1\) force it to vanish identically. We therefore obtain a generic recurrence for the ordinary colors without assuming equality of ADO and colored-Jones recurrence ideals.

A forward recurrence divides by its leading coefficient. We choose a fixed starting color beyond which that coefficient is not identically zero along any generic trajectory. Write

\[
 a_d(q,M)=\sum_{(a,b)\in\mathcal S}c_{a,b}q^aM^b,\qquad
 A_q=\max_{\mathcal S}a-\min_{\mathcal S}a,\qquad
 D=\max_{\mathcal S}b-\min_{\mathcal S}b,\qquad
 s=|\mathcal S|.
\tag{8}
\]

with equal monomials already collected. Thus \(\mathcal S\) is the finite support, \(A_q\) is its spread in the exponent of \(q\), \(D\) is its spread in the exponent of \(M\), and \(s\) is the number of monomials. Set \(j_0=A_q+1\). For \(j\ge j_0\), the exponents \(a+bj\) in \(a_d(q,-q^j)\) are distinct: a collision with different \(b\)'s would imply \(j\le A_q\). Thus this denominator is a nonzero Laurent polynomial for every generic step we use, although it may vanish at an individual root of unity.

Let \(B_j(q)\) be the forward companion matrix of the recurrence. It sends the vector of \(d\) consecutive colors beginning at \(j\) to the vector beginning at \(j+1\). Its first \(d-1\) rows shift entries left; its final row is

\[
 -\frac{1}{a_d(q,-q^j)}
 \bigl(a_0(q,-q^j),\ldots,a_{d-1}(q,-q^j)\bigr).
\tag{9}
\]

The initial data and the row extracting the complete color are

\[
 \begin{aligned}
 c_0(q)&=(C_{j_0}(q),\ldots,C_{j_0+d-1}(q))^{\mathsf t},\\
 r_N(q)&=e_d^{\mathsf t}B_{N-d}(q)\cdots B_{j_0}(q).
 \end{aligned}
\tag{10}
\]

Here \(e_d\) is the last standard basis vector, and the product is ordered as displayed. The vector \(c_0(q)\) consists of a fixed finite set of small-color Laurent polynomials. This fixed choice is the pointing. The recurrence gives the exact generic identity \(r_N(q)c_0(q)=C_N(q)\).

### Evaluation when individual steps have poles

At \(q=q_N\), a companion matrix may have a pole because its leading coefficient vanishes. The product with the initial data is nevertheless the regular Laurent polynomial \(C_N(q)\). We must therefore evaluate the whole product, not substitute into each singular step separately. The precise period is

\[
 \boxed{\quad
 \mathscr P_N(P,c_0)
 =\operatorname{CT}_{t=0}
   \bigl[r_N(q_N(1+t))c_0(q_N(1+t))\bigr]
 =K_N(K).
 \quad}
\tag{11}
\]

The variable \(t\) measures displacement from the root, \(q=q_N(1+t)\). The notation \(\operatorname{CT}_{t=0}\) means the coefficient of \(t^0\) in the Laurent expansion. Negative powers may occur in individual factors, but they cancel in the complete scalar product. Equation (11) retains that cancellation and recovers the Kashaev invariant exactly.

### Why only finitely many derivatives are needed

The order of a pole determines how many Taylor coefficients of the initial data can contribute to the constant term. The total order is bounded independently of \(N\).

For sufficiently large \(N\), the polynomial \(a_d(q_N,M)\) is not identically zero. After removing a Laurent monomial, its degree in \(M\) is at most \(D\). It therefore vanishes at no more than \(D\) of the distinct points \(-q_N^j\) used in (10). At any such step, the moving-\(q\) polynomial \(a_d(q,-q^j)\) has at most \(s\) nonzero monomials with distinct exponents. Its vanishing order is at most \(s-1\): vanishing of its first \(s\) logarithmic derivatives would give a Vandermonde system with only the zero solution. Consequently

\[
 B_N:=\sum_{j=j_0}^{N-d}
       \operatorname{ord}_{q=q_N}a_d(q,-q^j)
 \le B:=D(s-1).
\tag{12}
\]

This counts the order along the moving trajectory \(M=-q^j\), not merely the number of meridian zeros with \(q\) fixed. Expand

\[
 \begin{aligned}
 r_N(q_N(1+t))&=\sum_{\ell\ge-B_N}R_{N,\ell}t^\ell,\\
 J_k(N)&=[t^k]c_0(q_N(1+t)).
 \end{aligned}
\]

The row vector \(R_{N,\ell}\) is a Laurent coefficient of the propagated recurrence, while \(J_k(N)\) is a Taylor coefficient of the initial vector. A finite Taylor list is also called a jet. Formula (11) now becomes

\[
 \boxed{\quad
 \mathscr P_N(P,c_0)=
       \sum_{k=0}^{B_N}R_{N,-k}J_k(N),\qquad B_N\le D(s-1).
 \quad}
\tag{13}
\]

The entries of \(J_k(N)\) are \(q_N^k C_j^{(k)}(q_N)/k!\), for finitely many fixed colors and \(0\le k\le B\). They are bounded as \(N\to\infty\), since the fixed small-color polynomials are analytic near \(q=1\). After the knot and its twist weights are fixed, so are the operator, its order, its support, the starting color and these polynomials. None is adjusted to fit a quantum level or a proposed asymptotic.

## 4. The operator period and the volume limit

**Pointed quantum \(A\)-period theorem.** For the fixed knot (1), choose any genuine all-level annihilator (5) and the pointing (10). Then

\[
 \boxed{\quad
 \lim_{N\to\infty}\frac{2\pi}{N}
   \log\left|
       \sum_{k=0}^{B_N}R_{N,-k}J_k(N)
       \right|
 =V.
 \quad}
\tag{14}
\]

The same statement holds for the localized minimum-order generator. The scalar inside the logarithm is nonzero for all sufficiently large \(N\).

The proof is the exact identity (11) followed by the strict Conway volume theorem on the reduced presentation. The tangle isotopy preserves the normalized invariant and the actual knot exterior, so the conclusion also holds for the original presentation. The identity retains the complete signed scalar at every sufficiently large level; the knot theorem supplies its nonzero asymptotic and its limit. No equality between operators computed from different presentations is required. This is an operator expression for the volume limit, obtained by reconstructing the selected invariant exactly.

For the quantitative circle-tree class, apply its volume theorem
directly to (11). This proves (14) under the summed criterion, with
the same fixed operator, initial data and singular-step treatment.
The peripheral formulas and determinant identity below are exact
knot identities and continue to apply without a new twist hypothesis.

### Restoring the full peripheral normalization

The reduced and full literature ADO states differ by an explicit factor:

\[
 \begin{aligned}
 \mathcal N_N(M)&=d_N(M)F_N(M),\\
 d_N(M)&=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}}
       =\eta_N\frac{M^{N-1}}{\displaystyle\sum_{r=0}^{N-1}M^{2r}},
       &\eta_N&=i^{N+3},\\
 d_N(1)&=\frac{\eta_N}{N},&
 \mathcal N_N(1)&=\frac{\eta_N}{N}\mathscr P_N(P,c_0).
 \end{aligned}
\tag{15}
\]

The evaluation at \(M=1\) is taken in the whole regular germ. At the reference point \(M=-q_N\), the full state instead has the nonzero residue specified by the pointing theorem. Multiplying the state by an unspecified scalar would lose that normalization even if its exponential growth happened to remain the same.

Conjugation by the peripheral factor transports the shift according to

\[
 d_N^{-1}Td_N=g(q_N,M)T,\qquad
 g(q,M)=-q^{-1}\frac{q^2M^2-1}{M^2-1}.
\tag{16}
\]

This is the fixed Ore gauge: it changes the recurrence coefficients in the noncommutative shift algebra when the state is multiplied by \(d_N\). A full-state operator can first be transported to reduced coordinates and then used in (5). At \(M=1\), the correct period is given by (15), not by formally inserting that value into a meromorphic gauge coefficient. Since \(|\eta_N|=1\) and \(\log N/N\to0\), the full-state period has the same volume limit. The formula retains its peripheral factor and regular completion, rather than only asserting equality of exponential rates.

## 5. A positive determinant formula for the same limit

The scalar in (13) is signed and can involve substantial cancellation. There is also a positive algebraic formulation, supplied by the [pointed Gram-period theorem](pointed_a_gram_period.md). It is a different exact expression, not the result of taking absolute values of the summands in (13).

Use the fixed derivative bound \(B=D(s-1)\). At level \(N\), introduce the Taylor coefficients through order \(B\) of every color from \(j_0\) to \(N\). Put these unknowns into a vector \(y\). The square banded system \(\mathsf M_Ny=b_N\) fixes the first \(d\) color blocks to the actual jets of \(c_0\), and imposes the generic recurrence (7) modulo \(t^{B+1}\) at subsequent steps. The selector \(\mathsf R_N\) keeps the constant coefficient of each color block. Define

\[
 \begin{aligned}
 \mathsf H_N&=\mathsf M_N^\dagger\mathsf M_N,&
 v_N&=\mathsf M_N^\dagger b_N,&
 \beta_N&=b_N^\dagger b_N,&
 \nu_N&=\dim\ker\mathsf M_N,\\
 Q_N(\lambda)&=\det(\mathsf H_N+\lambda I),\\
 D_N(\lambda,z)&=
 \det\begin{pmatrix}
 \mathsf H_N+\lambda I+z\mathsf R_N^\dagger\mathsf R_N&v_N\\
 v_N^\dagger&\beta_N
 \end{pmatrix}.
 \end{aligned}
\tag{17}
\]

The dagger denotes conjugate transpose. Thus \(\mathsf H_N\) is a positive semidefinite Gram matrix. The variables \(\lambda,z\) in these determinants are ordinary polynomial variables, not meridian or longitude eigenvalues. The matrices have size \(O(N)\), with fixed bandwidth and fixed jet-block size.

The finite valuation argument gives \(\ker\mathsf M_N\subset\ker\mathsf R_N\) and \(\nu_N\le B\). In words, any ambiguity in the truncated derivative system has zero constant-color output. The exact ratio is

\[
 \mathscr G_N(P,j_0)=
 \frac{[\lambda^{\nu_N}z]D_N(\lambda,z)}
      {[\lambda^{\nu_N}]Q_N(\lambda)}
 =\sum_{j=j_0}^{N}|C_j(q_N)|^2.
\tag{18}
\]

The bracket extracts the indicated polynomial coefficient, and the denominator is positive. On the orthogonal complement of \(\ker\mathsf M_N\), the matrix \(\mathsf H_N\) is positive definite. The derivative in \(z\) of the bordered Schur complement is the squared norm of the unique constant-color output. The zero modes contribute precisely the common factor \(\lambda^{\nu_N}\). This proves the ratio, while Cauchy–Binet expresses its coefficients as nonnegative sums of squared minors with the source border retained.

For a fixed braid presentation of the knot with \(b\) strands, the [ordinary-color bound](regularized_kashaev_period.md) gives

\[
 \mathscr G_N(P,j_0)=|K_N(K)|^2+O_K(N^{2b-1}).
\tag{19}
\]

Only the colors \(j<N\) are polynomially bounded here. No such bound is asserted for the complete color, whose exponential growth is the subject of the volume theorem. Since \(V>0\), equations (14) and (19) imply

\[
 \boxed{\qquad
 \lim_{N\to\infty}\frac{\pi}{N}\log\mathscr G_N(P,j_0)=V.
 \qquad}
\tag{20}
\]

Two genuine operators with a common sufficiently large fixed starting color give exactly the same expression (18). Changing the fixed starting color changes that sum only by finitely many bounded terms.

The [marked regulator norm](intrinsic_quantum_a_norm_torsor.md) is normalized by \(\log\|\mathcal P_{\mathrm{hyp}}\|=2V/\pi\), where \(\mathcal P_{\mathrm{hyp}}\) is the selected hyperbolic regulator period. In that convention, the two operator limits read

\[
 \frac4N\log|\mathscr P_N(P,c_0)|
       -\log\|\mathcal P_{\mathrm{hyp}}\|\longrightarrow0,
 \qquad
 \frac2N\log\mathscr G_N(P,j_0)
       -\log\|\mathcal P_{\mathrm{hyp}}\|\longrightarrow0.
\tag{21}
\]

These are norm equalities for the selected periods. They do not identify an entire unpointed space of solutions, or assert an isomorphism of quantum modules.

## 6. The selected geometric factor and the remaining questions

For the knots in the theorem, three objects are available: a genuine all-level ADO annihilator, fixed finite data selecting its solution, and an exact complete period with the knot-volume limit. The operator exists before the period is evaluated. Its initial jets contain no level-dependent exponential normalization, and (11) shows that a different invariant has not been substituted.

The [full microscopic expansion](actual_main_meridian_filtered_characteristic.md), combined with the [geometric longitude theorem](actual_all_circle_geometric_characteristic.md), identifies the selected geometric factor for the covered circle trees. Comparing the entire pointed quantum module with the marked regulator germ remains a stronger problem. The crossing-circle deformation used to prove the volume theorem keeps the main meridian complete. It is not by itself a semiclassical theorem for varying that main-meridian ADO coordinate. Likewise, a rational root-state solution always gives a central monodromy eigenvalue \(1\); this does not identify its central spectral curve with the classical knot \(A\)-polynomial.

The [complete-meridian zero theorem](actual_ado_complete_meridian_zero_accumulation.md) gives an explicit restriction on that comparison. Exactly \(F_N(q_N)=1\), whereas \(F_N(1)=K_N(K)\) has positive volume growth. Actual zeros therefore approach \(M=1\) within \(O(1/N)\), and a uniform nonzero scalar branch for the unchanged state across completeness is impossible. The full modified state has a pole at \(M=q_N\).

The ordinary-color argument also forces every polynomial annihilator in the squared coordinate to have the right factor \(Y-1\), as proved in the [peripheral normal-period theorem](peripheral_normal_period.md). This condition now holds for all knots covered here. It retains a boundary module and a normal derivative of the state; it does not identify the geometric longitude factor. The [regular-period construction](regularized_kashaev_period.md) subtracts the ordinary-color polar data and gives an affine equation for the resulting regular remainder. Its neighborhood asymptotics remain an additional problem.

No equality of full annihilator ideals with another knot recurrence ideal, equality of classical symbols, or efficient minimal-order algorithm is asserted here. Nor does the corollary enlarge the knot class to arbitrary short twists, trees growing with \(N\), or all arborescent presentations. None of these additional statements is needed for the exact reconstruction and limits (14), (20) and (21).
