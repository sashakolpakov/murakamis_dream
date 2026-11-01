# Notation and conventions

The calculations in this guide pass through three kinds of object: a finite quantum expression, a function describing its large-level growth, and a geometric structure on a specified link complement. A symbol does not acquire a geometric meaning merely because it occurs in a critical-point equation. The proof must identify the relevant matrix, path, or gluing map. This chapter gives the conventions needed to read those identifications and to compare the different approaches in the [mechanism](mechanism.md) and [geometry](geometry.md) chapters.

For a first reading, [From a knot diagram to a volume limit](starting.md)
defines the topological objects, writes out a finite contraction, and
derives the coefficient estimate. This chapter is a reference for the
notation used after those definitions.

Letters are reused in the technical archive. In particular, a tangle turn, a crossing matrix, and a shift of a meridian variable are different operations. Local definitions take precedence when a note uses another convention.

## The invariant and the order of limits

Fix the diagram, its ordered tangle construction, its integer twist powers, and any finite certificate used by a theorem. Then let the integer quantum level \(N\) tend to infinity. Statements for arbitrary finite trees or spheres allow arbitrarily large fixed diagrams; they do not allow the diagram to grow with \(N\). A universal sufficient twist bound and a uniform error estimate over all diagrams are different assertions.

| Symbol | Meaning |
| --- | --- |
| \(N\ge2\) | Quantum level. Unless a theorem states otherwise, the limit includes both parities and composite levels. |
| \(q_N=e^{\pi i/N}\), \(Q_N=q_N^2\) | The chosen root and its square. The methods chapter also writes \(\zeta_N=Q_N\). In a fixed-level calculation, the subscripts are often omitted. |
| \(d=N-1\) | Top index in the \(N\)-dimensional physical module. |
| \(\zeta\) | A generic quantum parameter when a derivative is taken before root specialization. |
| \([j]_\zeta=(\zeta^j-\zeta^{-j})/(\zeta-\zeta^{-1})\) | Symmetric quantum integer. |
| \(s_j=2\sin(\pi j/N)\), \(S_j=\prod_{a=1}^j s_a\), \(S_0=1\) | Root sine factors and their products. A normalizing factor \(S_j\) can have exponential size; it is not automatically absorbed into a polynomial error. |
| \(K_N(K)\) | The reduced complete-color Kashaev invariant of the oriented, zero-framed knot \(K\), with unknot value one in the stated convention. |
| \(n_i\) | The signed integer exponent of the physical checked crossing \(R\) in a fixed box. It is a twist count, not a level or a scaled color. |
| \(\epsilon_i\in\{-1,0,1\}\), \(p_i\in\mathbb Z\) | Retained half twist and integral disk-filling parameter, with \(n_i=\epsilon_i-2p_i\). |
| \(v_3,v_8\) | Volumes of a regular ideal tetrahedron and a regular ideal octahedron. |

The manuscript's Chapter 2 writes \(s_r\) for the sine **product**
that this guide calls \(S_r\). In formulas from that chapter, translate
\(s_r^{\mathrm{manuscript}}=S_r^{\mathrm{guide}}
=\prod_{a=1}^r2\sin(\pi a/N)\). The individual sine factor in this
guide is \(s_r=2\sin(\pi r/N)\). These are different quantities,
so a formula copied between the two conventions needs this translation.

The volume statement uses the rate
\[
 \frac{2\pi}{N}\log|K_N(K)|
       \longrightarrow \operatorname{Vol}(S^3\setminus K).
\]
The absolute value is taken after the entire complex scalar has been evaluated. A large summand or a large sum of absolute values supplies no lower bound for that scalar.

“Independently sufficiently long” means that a fixed presentation has a threshold and each surviving twist exceeds it in absolute value, with either sign and without a bound on ratios between twist lengths. In a net-twist reduction, the condition concerns the surviving signed sums, not each original summand. The [results chapter](results.md) states the separate long-filling, degree-and-twist, and decorated-planar hypotheses.

## Finite sums, colors and derivatives

A **color** specifies a representation on a physical strand or auxiliary circle. An internal **channel** is a representation label introduced by a decomposition of tensor products. A **head index** specifies a basis vector inside a representation. These are different finite indices.

The ordinary auxiliary color is \(j\in\{1,\ldots,N\}\), and its highest weight is \(j-1\). Complete color means \(j=N\), with highest weight \(d\). Its external deficit is \(h=N-j\), and the corresponding scaled deficit is \(\chi=h/N\). Some older formulas use \(n\) for this color; their \(n\) must not be confused with a crossing power \(n_i\).

An internal polynomial or head index \(r\in\{0,\ldots,d\}\) often gives a scaled variable \(x=r/N\). A different formula may use the half-shifted channel variable
\[
       a_j=\frac{j+1/2}{N},\qquad
       c_j=2\cos(2\pi a_j).
\]
For the folded spectral coordinate, set
\[
       \delta_j=\frac12-a_j,\qquad
       c_j=-2\cos(2\pi\delta_j).
\]
On the representative half of the spectrum, the continuous variable \(\delta\) near zero describes the internal endpoint near \(-2\); it is not the external color deficit \(\chi\). At odd levels the endpoint \(\delta=0\) is an actual simple node. At even levels the nearest representative has \(\delta=1/(2N)\). Those finite offsets are retained in the interpolation.

The choice \(r/N\), \(r/(N-1)\), or \((r+1/2)/N\) must remain visible. They have the same interior leading limit in suitable regimes, but different exact endpoints and first corrections. For example, \(r_1+r_2\le d\) becomes \(x_1+x_2\le1-1/N\) when \(x_i=r_i/N\). Replacing it by a closed limiting inequality is an estimate, not an exact source identity.

A **normal** is a derivative in a specified direction. At a repeated Casimir node \(c\), a polynomial operator can depend on both \(p(c)\) and \(p'(c)\); evaluating only \(p(c)\) loses its nilpotent part. This is the reason for Hermite data. A derivative in the generic parameter \(\zeta=q_Ne^t\), with \(N\) fixed, is another operation. A factor that vanishes at \(t=0\) can have a nonzero derivative there. Neither derivative is the next coefficient of an \(N\to\infty\) expansion.

The [physical polynomial compiler](../../notes/actual_main_meridian_newton_compiler.md) records the finite Casimir algebra and its repeated-root data. The [homogeneous face source](../../notes/actual_homogeneous_casimir_face_source.md) records how its polynomials become original matrix entries. Root-only identities must not be differentiated in a generic parameter without that additional source calculation.

For the complete Newton basis, the convention used in the moving-meridian bounds is
\[
 e_r(z)=\frac{\prod_{a=0}^{r-1}(c_a-z)}{S_r^2},
 \qquad 0\le r\le d,\qquad e_0=1.
\]
“Low” means \(r\le\lfloor d/2\rfloor\), and “high” means \(r>\lfloor d/2\rfloor\). These are ranges of an internal polynomial index, not small or large physical colors. A high basis polynomial vanishes at the complete spectral nodes but may have nonzero derivatives there.

For a polynomial \(F\), the coefficient trace in an equal-color channel with \(M=q_N^s\) is
\[
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F,\qquad
 P_s(z)=\mathsf T_N(z)+2\cos(2\pi s),
 \quad \mathsf T_N(u+u^{-1})=u^N+u^{-N}.
\]
Here \(\operatorname{rem}_{P_s}F\) is the unique remainder of degree less than \(N\) after polynomial division. This retains the full repeated-root data. The normalized polynomial \(\mathsf T_N(z)\) is \(2T_N(z/2)\) in the convention \(T_N(\cos\theta)=\cos(N\theta)\). Opposite-color channels use the constant quotient \(P_0\), with their original reference maps retained. The compiler fixes which channel occurs; one cannot move every quotient in a diagram indiscriminately.

Changing coordinates, changing the quotient product, and applying a physical turn are three different operations. In particular, an entry of a moving multiplication tensor need not be bounded by its complete value at the same indices. The [same-index obstruction](../../notes/actual_main_meridian_same_index_obstruction.md) disproves that estimate. The [reflected-trace bound](../../notes/actual_main_meridian_high_fourier_reflection.md) compares the change in the tensor with a different index and keeps the neighboring source profiles. Neither statement concerns a counterexample to a knot-volume limit.

## Source polynomials, sectors and the invariant

The **source** is the full prescribed expression: physical matrices, their index ranges, cups, caps, the marked cut, and every scalar factor. A **coupon** is one specified operator inserted in a tangle box. A source polynomial is a way of storing the matrix entries of such an operator or the coefficients of a whole contraction.

A **simple triangulated sphere** is a finite graph embedded in the
two-sphere with triangular complementary faces, with no loops or
multiple edges. Its dual has a vertex for each triangle and an edge
for each shared side. Every dual vertex has degree three. A **perfect
matching** of that dual chooses one incident edge at every dual
vertex, pairing all the triangles. Each pair gives one ordered
four-face crossing region. If there are \(R\) pairs, the sphere has
\(2R\) triangles, \(3R\) edges and \(R+2\) vertices: the first edge
count follows by counting three sides per triangle twice, and the
vertex count then follows from Euler's formula.

The marked main edge is an original strand edge, not one of the
white edges selected by this matching. Its two endpoints \(u,v\)
are the protected white vertices. Thus the same graph vocabulary
can refer to two different edges: a matched diagonal describes a
crossing region; a nonmatching marked edge records the cut in a
main strand. The cyclic orders and the terminal strand pairing
remain part of the source data. A matching alone does not establish
that the resulting link has one component.

A **Morse presentation** draws the original strands with respect to
a height function whose local maxima and minima are isolated and
nondegenerate. A horizontal slice between events has a fixed
number of strand intersections. A cup increases that number by
two, a cap decreases it by two, and a crossing acts on the strands
present at its height. A flat plat puts all upper cups and lower
caps outside one braid region; a general Morse presentation can
have cups and caps between crossing regions. The general source
identity retains these intervening maps. It does not replace the
diagram by a flat plat without proving such a transformation.

The face construction uses three successive operations. First multiply
the local polynomials, then extract one shared face coefficient, then
apply the functionals that insert the prescribed twists. The variables
have different roles at these stages:

| Symbol | What varies, and what is done with it |
| --- | --- |
| \(L_f\) | A formal variable for projection face \(f\). Its prescribed coefficient is extracted once from the whole product. |
| \(\rho_f>0\) | The radius of the integration circle \(\lvert L_f\rvert=\rho_f\) in a Cauchy coefficient estimate. It is a freely chosen weight for a bound. |
| \(\sigma_e\) | A spectral variable retained at crossing region \(e\) after the face extraction. |
| \(\mathcal L_N^{n_e}\) | A linear functional on the polynomial in \(\sigma_e\); it inserts the fixed signed crossing power \(n_e\). |
| \(S_N(\boldsymbol\sigma)\) | The polynomial after the common face coefficient has been taken. It is not yet the filled scalar. |

Thus the final step has the form
\[
 Z_N(\boldsymbol n)=
 \left(\mathcal L_N^{n_1}\otimes\cdots\otimes
       \mathcal L_N^{n_R}\right)S_N.
\]
Each functional acts on its own spectral variable. The exact source
identity specifies the exterior and framing factors relating \(Z_N\)
to \(K_N(K)\). A bound for a polynomial before coefficient extraction,
a bound for \(S_N\), and a bound for \(Z_N\) are therefore three
distinct statements.

In the homogeneous face description, a box has ordered faces \((x,b,c,y)\): \(b,c\) are its middle faces and \(x,y\) its outer faces. Its polynomial \(H_e(x,b,c,y)\) has total degree \(d\). For a diagram with \(R\) boxes, the product has degree \(Rd\). With two protected faces \(u,v\), the original marked contraction is expressed by
\[
 \left[\prod_{f\ne u,v}L_f^d\right]\!
       \left.\prod_{e=1}^R
       H_e(L_{x_e},L_{b_e},L_{c_e},L_{y_e})
       \right|_{L_u=L_v=0}.
\]
The brackets mean coefficient extraction, not substitution of face radii. There are \(R\) ordinary targets, each of degree \(d\), and two protected targets of degree zero. A shared face has one variable wherever it occurs. Giving separate occurrences unrelated values would change the problem.

For physical coupons this coefficient formula gives the original scalar with its stated exterior normalization. If \(H_e\) is instead a spectral numerator depending on a variable \(\sigma_e\), the extracted result \(S_N(\boldsymbol\sigma)\) is still a polynomial in those spectral variables. The original trace and filling functional remain to be applied. The [general Morse source theorem](../../notes/research_matched_sphere_morse_source.md) keeps the turns, mark, primitive face grid, and both level parities in this description.

Several decompositions of the source are used:

| Term | Exact meaning |
| --- | --- |
| Complete-color source | The original contraction with every designated auxiliary color equal to \(N\). |
| Color core | The term retaining the complete-circle part of each exact external-color identity. It can be an entire function of \(\chi\). |
| Color alias | A complementary small-color term in that identity. Its exponential smallness is a theorem to be proved, not part of its definition. |
| central sector | The specified central-cut support in a local continuant/cofactor spectral numerator. |
| left or right sector | One of the complementary one-sided supports in that same numerator. |
| All-central contraction | The coefficient or period obtained by selecting central at every box, while retaining the shared face targets and original trace. |
| Full contraction | The sum over all the prescribed sector choices, with their signs and normal data. |

These sector names describe finite subsets of the recurrence paths; central does not mean a physical crossing matrix. A color core and an all-central projection arise from different decompositions and must not be identified by their names. A nonzero all-central period with the correct geometric rate does not by itself prove the full invariant's rate: the other sectors might contribute or cancel it. The [cofactor theorem](../../notes/actual_cross_cofactor_factorization.md) defines that projection, and the [balanced planar theorem](../../notes/actual_balanced_terminal_fan_volume.md) explains a sufficient comparison with the remaining sectors.

A **finite-sector cover** groups genuine central/left/right choices for estimates. A branch has one full shared face-weight vector; it does not assign unrelated weights to the two occurrences of a face. The maxima inside a scalar upper bound are comparison terms, not additional quantum sectors. This combinatorial use of “cover” is different from a covering space of a link complement. The [methods chapter](methods.md#refining-the-coefficient-estimate-by-genuine-sectors) gives the cost and the remaining coverage question.

## Norms used in the estimates

The same notation for a norm can hide different mathematical objects.
These are the main choices in the guide:

| Expression | Definition and object being bounded |
| --- | --- |
| \(\|H\|_{[-2,2]^R}\) | \(\sup_{\boldsymbol\sigma\in[-2,2]^R}|H(\boldsymbol\sigma)|\), for the complex spectral polynomial after the shared face coefficient has been extracted. |
| \(\|v\|_2^2\) | \(\sum_j|v_j|^2\), for a specified finite vector and basis. |
| \(\|A\|_{2\to2}\) | \(\sup_{v\ne0}\|Av\|_2/\|v\|_2\), the largest singular value of the matrix in that basis. |
| \(\|v\|_G^2\) | \(v^*Gv\), where \(G\) is a specified positive definite Hermitian matrix. |
| \(\sum_\alpha|c_\alpha|\boldsymbol\rho^\alpha\) | The absolute coefficient sum of \(P(\boldsymbol L)=\sum_\alpha c_\alpha\boldsymbol L^\alpha\), evaluated at positive radii \(\boldsymbol\rho\); it is an upper bound on the face torus, not the original signed evaluation. |

In the last row, \(\alpha\) is a tuple of nonnegative integers and
\(\boldsymbol\rho^\alpha=\prod_f\rho_f^{\alpha_f}\). A star on a
vector or matrix denotes conjugate transpose. A nonunitary change
of basis changes matrix norms, even when it preserves an exact
contraction. The physical cup/cap pairing and the Frobenius
coefficient trace are also not automatically positive Hermitian
inner products. Their endpoint costs must be proved when a
positive norm is introduced. The
[weighted-Cauchy section](methods.md#weighted-cauchy-and-the-cost-of-joining-pieces)
shows those costs explicitly.

## Tangles and geometric variables

A tangle box has four ordered endpoints. A product stacks compatible boxes in their specified order. A **physical quarter-turn** bends an incoming strand into an outgoing one and changes the input/output presentation. Its evaluation includes the original duality maps. The cylindrical closure joins lower endpoints to upper endpoints outside the box; the cap closure joins the two upper endpoints and the two lower endpoints respectively. These closures can have different topology. The knot test counts both components formed at final closure and any circles already closed inside a tangle.

The guide usually writes \(R\) for a checked crossing operator, including the interchange of its two tensor factors, and \(T\) for a tangle turn. Some older notes call a turn \(R\). The shift called \(T\) in a quantum difference equation below is a third operation.

A construction tree records products and turns; it is not a knot projection. A **circle-marked junction** contains a crossing-circle operator. A **bare junction** is a maximal consecutive group of products without one. Resolving a high-valence product into binary products introduces internal bookkeeping variables, not new physical quarter-turn edges. For a vertex \(v\), \(d_v\) is its graph degree, including the specified boundary attachments. It has no relation to the quantum top index \(d=N-1\).

In strict-tree geometry, a physical turn edge has a normalized polynomial label \(x_e\). When exposed as the ordinary output of a rooted branch, that output angle is \(1-x_e\). The set \(\mathcal E_T\) in the longitude formulas consists of the original physical turn edges; hidden binary-resolution edges are excluded. The [strict-tree geometric theorem](../../notes/actual_strict_tree_geometric_characteristic.md) explains this convention and the case \(x_e=1/2\).

A geometric gluing face may be a quadrilateral with four ordered ideal vertices. “Ideal” means that its vertices lie on the sphere at infinity of hyperbolic space. The vertex order specifies the face identification. Some archive notes call such a boundary face a *port*; elsewhere that word refers to an external representation factor. It is necessary to check which meaning is intended.

## Circle packings, shapes and geometric actions

In the face-source geometry, a positive real \(L_f\) is the **curvature**, or inverse radius, of a finite white circle. A protected value \(L_u=0\) denotes a straight line, not a circle of radius zero. Sending the marked tangency to infinity gives two parallel protected lines. The remaining circles lie in their common strip. Shared positive radii used in a Cauchy estimate are choices of weights; only a separately proved stationary identification makes them the geometric packing.

A complex number \(z_\Delta\) attached to an ideal tetrahedron is its ordered cross-ratio shape. Its branch and orientation matter; a coordinate with positive imaginary part gives a positively oriented tetrahedron in the usual vertex convention. The same letter \(z\) can instead be a formal polynomial variable, a spectral variable, or the microscopic meridian coordinate below. These uses are unrelated.

The real factorial rate uses
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad 0\le x\le1,
\]
with the integrable endpoint limits. The Lobachevsky function is
\[
 \Lambda(\theta)=-\int_0^\theta\log|2\sin u|\,du.
\]
Thus \(J(x)=-\Lambda(\pi x)/\pi\) on that real interval. Complex continuations require a specified logarithm and path; the absolute value in the real definition of \(\Lambda\) is not a holomorphic prescription.

**Definition (triangle potential).** For three nonnegative weights
\(w_1,w_2,w_3\), not all zero, put
\[
\begin{aligned}
 f(t)&=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},
       &&0\le t\le\tfrac12,\\
 Q(w_1,w_2,w_3)
   &=\max_{\substack{\alpha_j\ge0\\\sum_j\alpha_j=1/2}}
       \sum_{j=1}^{3}\bigl(f(\alpha_j)+\alpha_j\log w_j\bigr).
\end{aligned}
\]
When \(w_j=0\), require \(\alpha_j=0\) and assign the corresponding
product \(\alpha_j\log w_j\) the value zero. The \(\alpha_j\) are
normalized angle variables in this maximization. This definition
fixes the additive constant: for example,
\(Q(w,0,0)=\tfrac12\log w\) for \(w>0\). Scaling all three weights
by \(c>0\) adds \(\tfrac12\log c\), because their normalized angles
sum to \(1/2\).

The **complete local rate** at an ordered quartet \((x,b,c,y)\) is
\(Q(x,b,y)+Q(x,c,y)\). A **capacity bound** sums these local rates,
subtracts the logarithmic cost of the required face powers, and
minimizes over one positive weight per ordinary face. Its value at
the stationary packing and its value at arbitrary trial weights
have different roles. The [methods chapter](methods.md#refining-the-coefficient-estimate-by-genuine-sectors)
gives the one-sided rates and explains the strict comparison needed
to control the remainder. The function \(Q\) is unrelated to the
quantum root \(Q_N=q_N^2\).

For a positive complete source, \(\Phi_D\) or \(F_0\) often denotes its maximal limiting action. Once the original geometry has been proved, its normalization is
\[
                  2\pi\Phi_D=\operatorname{Vol}(Y_D),
\]
where \(Y_D\) is the complete **augmented** exterior. A filled critical action is generally complex. Its real part is converted to the filled volume only after the original primitive peripheral equations and the regulator boundary correction have been checked.

A **boundary profile** maximizes an open tangle's action with one output index fixed. It retains that boundary constraint and its original joining terms. It is not an independent volume budget that can be added arbitrarily to a neighboring profile.

## Packets, gaps and finite actions

A **packet** is a local asymptotic formula which includes the critical action, its nonzero amplitude, and a controlled remainder. A typical notation is
\[
             \mathcal I_N
                =N^\beta a_N e^{NS_N}(1+O(N^{-1})).
\]
Here \(\mathcal I_N\) is the specified integral or sum, \(\beta\) is its level exponent, \(a_N\) is the amplitude, and \(S_N\) is the finite-level critical value. A nonzero lower asymptotic needs control of \(a_N\) and all contributions outside the packet. Merely knowing \(S_N\to S\) does not permit replacing \(e^{NS_N}\) by \(e^{NS}\) with relative error tending to zero.

A strict **exponential gap** at rate \(\Phi\) means an estimate such as
\[
       |\mathcal E_N|\le N^C e^{N(\Phi-\gamma)},
                    \qquad \gamma>0,
\]
uniformly on the parameter set stated in that theorem. A polynomial factor \(N^C\) does not change the rate. The constants and starting level may depend on the fixed diagram, fixed twists, compact domain, and derivative order. Uniformity through a complex neighborhood is stronger than a bound at physical integer samples.

A Hessian records second derivatives of the relevant phase. The face Cauchy integral and the spectral filling integral use different Hessians and different determinant branches. “Primitive lattice” means the retained integer summation coordinates have no hidden finite-index multiplicity. “First charge” refers to the unit Fourier magnitudes in the exact filling transform; other charges and endpoint currents remain part of the original period until estimated.

An estimate \(r_N(s)=O_C(N^{-k})\) on a compact parameter set \(C\)
means that one constant \(B_C\) bounds
\(|r_N(s)|\le B_CN^{-k}\) for every \(s\in C\) and all sufficiently
large \(N\). A statement to all asymptotic orders supplies such a
remainder after every prescribed finite truncation; it need not
give a convergent infinite series. The notation \(o(N)\), uniform
on \(C\), means that its supremum in absolute value divided by
\(N\) tends to zero. The relevant compact set and any derivative
order belong to the statement.

## Augmented and filled complements; peripheral coordinates

An **augmented exterior** \(Y_D\) is the complement of the main strands together with the auxiliary crossing circles. Filling an auxiliary cusp attaches a solid torus along the prescribed primitive slope and restores the twists. The resulting knot exterior is \(S^3\setminus K_{\boldsymbol p}\). Its volume generally differs from \(\operatorname{Vol}(Y_D)\). The main knot cusp remains unfilled.

On each auxiliary torus, \(\mu_i\) goes once around its crossing circle and \(\lambda_i\) is the recorded disk longitude. They form a primitive integral basis. Choose the specified matrix eigenline. Let \(m_i\) and \(\ell_i\) be the corresponding determinant-one eigenvalues divided by their values \(\pm1\) at completeness, so that both normalized eigenvalues equal \(1\) there. Continue their logarithms from that point and write
\[
       U_i=2\operatorname{Log}m_i,\qquad
       V_i=2\operatorname{Log}\ell_i .
\]
These are logarithms of **similarity multipliers**, equivalently twice the normalized eigenvalue logarithms. For example, if the chosen auxiliary longitude matrix in the Morse collar has eigenvalue \(J_i=-1\) at completeness, then \(\ell_i=-J_i\) and \(V_i=2\operatorname{Log}(-J_i)\). At the smooth unit-charge filling saddle the convention is
\[
                       U_i+p_iV_i=-2\pi i.
\]
The equation is an equality of the continued logarithms. Its exponential alone would allow a wrong winding, and at a parabolic longitude could permit a nontrivial filling holonomy. The [primitive collar calculation](../../notes/actual_deformed_circle_primitive_collar.md) fixes the paths; the [metric completion theorem](../../notes/general_source_regulator_hyperbolic_equality.md) checks the actual log-link periods and the smooth solid torus.

Two useful descriptions of the auxiliary deformation are
\[
 U_i=-2\pi i\chi_i
 \quad\text{in the external-color coordinate},\qquad
 V_i=-4\pi i\delta_i
 \quad\text{in the internal spectral coordinate}.
\]
They belong to the same selected branch only after the stationary equations and the marked geometric adapter identify them. In the angular circle-tree chart one instead writes \(V_i=2i\tau_i\). The angle \(\tau_i\) is therefore not a cusp shape.

For the main cusp, normalize a horospherical Euclidean coordinate so that the positive meridian translates by \(1\). The preferred longitude follows the knot once with zero linking number; its translation is the **cusp shape** \(\tau_K\). If \(U_K=2\log M\) and \(V_K=2\log(-L)\) are centered at the complete lift, then \(dV_K/dU_K=\tau_K\) there. The sign \(-L\) centers the negative-unipotent preferred longitude lift \(L=-1\).

Under surgery on the auxiliary circles, the image of the augmented main longitude need not remain preferred. If \(k_i=\operatorname{lk}(K,C_i)\) is the integer linking number with the \(i\)th crossing circle, the stated disk convention gives
\[
       \lambda_{\mathrm{fill}}
          =\lambda_{\mathrm{aug}}\,
                    \mu_K^{\sum_i p_i k_i^2}.
\]
This shear changes the marked basis on the filled cusp. The [preferred-longitude proof](../../notes/actual_main_meridian_preferred_cusp.md) tracks it independently of the quantum asymptotic.

## The main-meridian quantum \(A\)-period

The raw unrolled highest-weight coordinate is \(x=q_N^\alpha\). The marked meridian coordinate is
\[
                         M=-q_Nx.
\]
Thus complete weight \(\alpha=d\) gives \(M=1\), and quotient color \(\alpha=j-1\) gives \(M=-q_N^j\). For the reduced, zero-framed ADO family \(F_N(M)\),
\[
       F_N(1)=K_N(K),\qquad F_N(-q_N^j)=C_j(q_N).
\]
The ordinary reduced \(j\)-color period is \(C_j(q)\). This notation is distinct from a color core also called \(C_N\) in some notes. The [pointing theorem](../../notes/kashaev_ado_pointing.md) fixes these equalities and the component convention.

The microscopic variable is \(s\), defined by
\[
          M=q_N^s=e^{z/(2N)},\qquad z=2\pi i s.
\]
Bounded \(s\) describes an \(O(1/N)\) neighborhood of \(M=1\); it is not a fixed meridian neighborhood. The proved strict-tree profile uses \(|s|\le R<1\), before the first ordinary-color resonances at \(s=\pm1\). In particular \(F_N(q_N)=1\) even when \(F_N(1)\) has positive volume growth.

The exact finite sine factor and scalar in that profile are
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\quad H_N(0)=1,
 \qquad
 A_N^{\mathrm{sc}}(s)=q_N^{a(D)s^2/2},
 \quad a(D)=-w(D)-\sum_i n_i.
\]
Here \(w(D)\) is the oriented writhe. The superscript “sc” distinguishes this scalar from a finite critical action also often called \(A_N\). Its exponent uses the actual checked-crossing powers and framing convention. It is retained exactly even though it tends to one.

The full modified-trace invariant is another normalization:
\[
 \mathcal N_N(M)=d_N(M)F_N(M),\qquad
 d_N(M)=i^{N+3}\frac{M-M^{-1}}{M^N-M^{-N}}.
\]
Evaluating the entire germ gives \(d_N(1)=i^{N+3}/N\) and
\(d_N(q_N^s)/d_N(1)=H_N(s)^{-1}\). Thus its normalized profile cancels the reduced sine factor exactly. One must not set the numerator and denominator separately to zero.

For the covered moving-meridian knots, the first correction in the zero-framed convention is
\[
 \frac{F_N(q_N^s)}{F_N(1)H_N(s)}
 =1+\frac{\pi i s^2\tau_K}{2N}+O(N^{-2})
 =1+\frac{\tau_K z^2}{8\pi iN}+O(N^{-2}).
\]
The exact scalar contributes to this coefficient. The [scalar proof](../../notes/actual_main_meridian_exact_scalar.md) and [geometric cusp proof](../../notes/actual_main_meridian_preferred_cusp.md) are separate arguments. Their combination is the [filled profile theorem](../../notes/actual_main_meridian_filled_volume.md), with its stated domain and fixed-presentation hypotheses.

## Difference operators, classical curves and selected solutions

A quantum \(A\)-operator is a specified finite difference operator
\[
       P(q,M,T)=\sum_{j=0}^{r}a_j(q,M)T^j,\qquad
       (TF)(M)=F(qM),\qquad TM=qMT.
\]
Here \(r\) is the operator order, fixed independently of \(N\); it is not the top color index \(d\). The \(a_j\) are fixed rational functions in the formal quantum and meridian variables. A **genuine all-level annihilator** satisfies \(P(q_N,M,T)F_N(M)=0\) as an identity of meridian functions at every sufficiently large root level, with the original state and normalization. The finite-source theorem constructs such operators; the selected-factor theorem applies to any operator satisfying these hypotheses. Choosing a new ratio of two evaluated values at each level does not meet them.

The associated **Ore ring** is the ring of these difference
operators with the multiplication rule
\[
             T\,a(q,M)=a(q,qM)\,T.
\]
For example, \(T(MF)(M)=qM\,F(qM)\), which proves \(TM=qMT\)
directly from the action. The **annihilator left ideal** is the
set of operators killing the specified state. It is closed
under addition and under applying another operator on the left.
The side matters because the operators do not commute.

An equation \(PF=0\) does not select its solution by itself. The **pointed period** also retains a fixed vector \(c_0(q)\) of small-color Laurent polynomials and the prescribed companion transport row \(r_N(q)\). At a root pole its value is
\[
       K_N(K)=\operatorname{CT}_{t=0}
          \bigl[r_N(q_N(1+t))c_0(q_N(1+t))\bigr].
\]
The constant term is taken after multiplying the entire Laurent germs. The parameter \(t\) here is a local evaluation variable, not the geometric deformation \(M=e^{\pi it}\) used in another note. The [pointed operator theorem](../../notes/actual_conway_pointed_quantum_a_volume.md) explains the finite initial data and its volume statement.

To form a classical symbol, first clear the specified rational denominators and remove the common power of \(q-1\), then take the first nonzero specialization and replace the commuting shift variable by \(L\). The **geometric \(A\)-curve** records the meridian and preferred-longitude eigenvalues of the selected geometric representations of the knot group. An arbitrary eliminated source equation can contain other components or points excluded from its original chart.

A **germ** records a function or curve only in a neighborhood of
the specified point, with two representatives identified if they
agree on a smaller neighborhood. A **jet of order \(k\)** retains
only the derivatives through order \(k\); it is less information
than a germ. A selected irreducible Laurent factor is a polynomial
in \(M^{\pm1},L^{\pm1}\) which vanishes on the chosen algebraic
curve and does not split into two nonconstant factors over the
stated coefficient field. Multiplication by a nonzero constant
or a monomial does not change its zero set in
\((\mathbb C^\times)^2\). The field matters: a factor irreducible
over \(\mathbb Q\) can split over \(\mathbb C\).

Thus the assertion that the selected geometric factor divides
a classical symbol is a statement about one component. It does
not specify the symbol's other factors or their multiplicities,
and it does not identify the whole noncommutative annihilator
ideal. Scalar gauges, denominator factors and the selected
longitude lift are retained before making that comparison.

In the geometric convention, \(M\) is the eigenvalue of the positively oriented main meridian and \(L\) is the preferred-longitude eigenvalue on the same line. The word “positively” specifies the orientation of the curve; \(M\) is a nonzero complex number, not necessarily a positive real number. The source cut selects the \(M^{-1}\) line, so \(L\) is the inverse longitude eigenvalue there. At the complete filled knot, \(M=1\) and \(L=-1\). On the covered strict-tree germ,
\[
 L_{\mathrm{geom}}(M)
   =-M^{a(D)}
       \prod_{e\in\mathcal E_T}
           \frac{M^2-X_e(M)}{1-M^2X_e(M)},
 \qquad X_e=e^{2\pi ix_e}.
\]
The [full strict-tree longitude theorem](../../notes/actual_strict_tree_geometric_characteristic.md) identifies these source variables and paths, including bare product junctions. This replaces the earlier circle-tree-only identification. Its operator corollary, and the [directed all-orders theorem](../../notes/actual_all_circle_directed_all_orders.md), specify when the selected geometric irreducible factor divides the first nonzero classical symbol. Such divisibility does not identify every factor, its multiplicity, or the complete quantum recurrence ideal.

## What a torsor records

A **torsor** is a space with a free and transitive action of a group, without a preferred origin. Choosing one point identifies it with that group, but a formula using the chosen coordinate must record the choice. Several different torsors occur in the archive.

For auxiliary holonomy, a half-longitude eigenvalue satisfies \(\ell^2=e^V\), and the logarithm of \(\ell\) has integral-period ambiguity. The actual collar and complete anchor select the sheet and logarithm. A retained half twist changes
\[
                 U^\epsilon=U^0-\frac{\epsilon}{2}V^0,
                    \qquad V^\epsilon=V^0.
\]
On the selected double cover this is an integral monomial change of peripheral coordinates. It does not authorize a half-integer substitution into the pure-link filling formula.

For a regular quantum difference module at a root of order \(m\), a chosen scalar frame can satisfy a cyclic norm equation
\[
                  \prod_{j=0}^{m-1}\sigma^j(a)=v,
\]
where \(\sigma\) is the prescribed cyclic field automorphism and \(v\) a central eigenvalue. Replacing the frame by \(f\) changes \(a\) to \(a\,\sigma(f)/f\). This algebraic norm is not the absolute value of the knot invariant, nor an operator norm. The [intrinsic norm-torsor construction](../../notes/intrinsic_quantum_a_norm_torsor.md) states the additional hypotheses needed to compare its selected period with a regulator.

The gauge factor has cyclic product one:
\[
 \prod_{j=0}^{m-1}\frac{\sigma^{j+1}(f)}{\sigma^j(f)}
                     =\frac{\sigma^m(f)}{f}=1.
\]
This explains why the algebraic norm is unchanged. It gives no
bound for the complex absolute value of \(f\) or its inverse.
The [Hilbert-90 discussion](algebraic.md#hilbert-90-solves-a-transport-equation)
shows an actual finite gauge with exponential operator cost.

A third local example is the [Casimir transport conic](../../notes/actual_crossing_casimir_torus.md): after choosing a spectral sheet and a reference point, crossing powers act multiplicatively on its regular fibers. The endpoint fibers degenerate, and the original excluded divisors and boundary targets remain part of the problem. An abstract norm torus or a local conic does not by itself identify a knot's geometric longitude or prove a nonzero source asymptotic.

These distinctions explain why the guide keeps the operator, regulator, relative-cycle, and full-source methods separate. Each technical route states which object is constructed and which comparison is still required.

The [algebraic approaches chapter](algebraic.md) defines Hilbert 90 transport, Koszul differentials, cyclotomic root data and jets, and nilpotent groups with triangular transport. It distinguishes these algebraic structures from bounds on the original quantum state.
