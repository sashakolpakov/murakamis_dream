# Recovering a short component from its open matrix contraction

Private research proof, 14 November 2026. The manuscripts remain frozen.

The purpose of this note is to compare two exact descriptions of the same
short component: the original Newton boundary polynomial and a contraction
in the basis used by Rivin's braid matrices. A short component may contain
any fixed signed crossing powers and any finite number of the original
Conway operations. No lower bound on those powers is assumed.

The comparison retains the open boundary, not just a closed invariant.
At a free vertex several polynomial factors can meet. Their ordinary
product can have degree at least \(N\), whereas a single pair Casimir
remembers a polynomial only modulo \(P_N\). We therefore give each free
incidence its own pair of matrix indices, recover those separate
polynomials, and only then identify their variables. This order is
essential.

## 1. The two pair descriptions

Fix \(N\ge2\), and put
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad
 \eta=(-1)^d,\qquad A_N=e^{-\pi i/(2N)}.
 \tag{1}
\]
Let \(T_N\) denote the Chebyshev polynomial of the first kind. The
original pair algebra and its normalized Newton basis are
\[
 \begin{split}
 \mathcal A_N&=\mathbb C[z]/(P_N(z)),&
 P_N(z)&=2T_N(z/2)+2,\\
 e_i(z)&=\frac{\prod_{a=0}^{i-1}(c_a-z)}{S_i^2},&
 c_a&=q^{2a+1}+q^{-2a-1},&
 S_i&=\prod_{a=1}^i2\sin(\pi a/N),
 \end{split}
 \tag{2}
\]
where empty products are one. Every class has a unique representative
of degree at most \(d\). The original trace \(\phi\), turn
\(\mathsf T\), and positive crossing \(R\) satisfy
\[
 \phi(e_i e_j)=\delta_{i+j,d},\qquad
 \mathsf T e_i=e_{d-i},\qquad R\in\mathcal A_N^\times.
 \tag{3}
\]
In particular, all signed integer powers of \(R\) are defined.

On the external \(N\)-dimensional space \(V_{\rm ext}\) use basis
\(u_0,\ldots,u_d\), pivot
\(K_{\rm ext}u_i=q^{-(d-2i)}u_i\), and positive braid matrix
\(R_{\rm ext}\) at \(A=A_N\). These are the conventions of
the external repository at commit
e956fb919ac7d1bbc7cb3d3873fbac993feb94b7.
The explicit comparison with the balanced physical basis is
\[
 T u_i=q^{-i(i-1)/2}|d-i\rangle,\qquad
 \Omega_{\rm ext}=(T\otimes T)^{-1}\Omega(T\otimes T).
 \tag{4}
\]
Here \(\Omega\) is the original physical pair Casimir. The local
crossing and prescribed-cut lemmas prove that
\[
 \begin{split}
 \iota:\mathcal A_N&\longrightarrow
       \operatorname{End}(V_{\rm ext}\otimes V_{\rm ext}),
       &\iota(f)&=f(\Omega_{\rm ext}),\\
 \iota(R)&=R_{\rm ext}^{-1},&
 L(\iota(f))&=\eta\phi(f),
 \end{split}
 \tag{5}
\]
and that \(\iota\) is injective. The functional in (5) is the
literal prescribed external cut
\[
 L(X)=\operatorname{Tr}[(P_0\otimes K_{\rm ext})X],
       \qquad P_0=u_0u_0^*.
 \tag{6}
\]
The row \(u_0^*\) is the coordinate dual. In particular, (6) is a
specified linear observation, not a positive norm. The sign reversal
in (5) is part of the comparison.

The pair algebra in (5) contains its nilpotents. A double root \(c\)
of \(P_N\) gives the local factor
\(\mathbb C[\epsilon]/(\epsilon^2)\), on which
\[
                  f(\Omega_{\rm ext})
                 \ \longleftrightarrow\ f(c)+f'(c)\epsilon.
 \tag{7}
\]
Thus the representation is not being replaced by its distinct
eigenvalues.

## 2. A partial source and its separate free incidences

Let \(\Gamma=(V,E)\) be one of the original finite circle trees.
Partition its vertices into the filled set \(S\) and the nonempty
free set \(U\). At every \(v\in S\), fix an arbitrary integer \(n_v\).
Write
\[
 K_T(z,w)=\sum_{i=0}^d e_i(z)e_i(w).
 \tag{8}
\]
The exact original partial source is the ordinary polynomial
\[
 B_N(\mathbf z_U)=
 \left(\bigotimes_{v\in S}\phi_v\right)
 \left[
   \prod_{v\in S}R(z_v)^{n_v}
   \prod_{e=vw\in E}K_T(z_v,z_w)
 \right].
 \tag{9}
\]
At filled vertices multiplication and \(\phi_v\) take place in
\(\mathcal A_N\). At free vertices the products are ordinary
polynomial products, with no reduction modulo \(P_N\).
In particular
\[
                 \deg_{z_u}B_N\le d\,\deg_\Gamma(u).
 \tag{10}
\]
Formula (9) is the original source-compilation identity. It includes
all crossing scalars and all first derivatives in the trace.

Let
\[
 H=\{(e,u): e\in E,\ u\in U,\ u\hbox{ is an endpoint of }e\}
 \tag{11}
\]
be the set of free incidences. An edge joining two free vertices
contributes two members of \(H\). Give each \(h\in H\) an independent
variable \(z_h\). For an endpoint \(v\) of an edge \(e\), set
\[
 a(e,v)=
 \begin{cases}
   v,&v\in S,\\
   (e,v),&v\in U.
 \end{cases}
 \tag{12}
\]
Replace \(z_v\) in that edge factor by \(z_{a(e,v)}\), while keeping
a single variable \(z_v\) at each filled vertex. The result after
the filled traces is a polynomial \(C_N(\mathbf z_H)\), separately
of degree at most \(d\) in every free-incidence variable. By direct
substitution,
\[
 B_N(\mathbf z_U)=
        C_N\bigl(z_{(e,u)}=z_u\bigr).
 \tag{13}
\]
The substitution in (13) takes place in the ordinary polynomial
ring. An isolated free vertex contributes only a constant and
causes no difficulty.

## 3. The exact matrix contraction and its inverse

Assign an independent copy of \(V_{\rm ext}^{\otimes2}\) to every
member of \(S\sqcup H\). Let \(\Omega_a\) and \(R_{{\rm ext},a}\)
denote the operators (4)--(5) on that copy. Define the edge operator
\[
 \mathcal K_{ab}=\sum_{i=0}^d e_i(\Omega_a)e_i(\Omega_b).
 \tag{14}
\]
It is a specified sum of Casimir insertions, namely the image of
the original turn kernel. It is not being identified with a single
external crossing.

Form the open operator on the free pairs
\[
 X_{S,N}=
 \eta^{|S|}
 \left(\bigotimes_{v\in S}L_v\right)
 \left[
   \prod_{v\in S}R_{{\rm ext},v}^{-n_v}
   \prod_{e=vw\in E}\mathcal K_{a(e,v),a(e,w)}
 \right].
 \tag{15}
\]
Applying \(L_v\) here means contraction of just that pair's matrix
indices, leaving all other indices open. All factors within a pair
are polynomials in its Casimir, so the products in (15) are
unambiguous.

**Theorem 1 (boundary correspondence).** The operator (15) belongs to
\(\bigotimes_{h\in H}\iota(\mathcal A_N)\), and
\[
                  X_{S,N}=\iota^{\otimes H}(C_N).
 \tag{16}
\]
Every coefficient of \(C_N\) is recovered by the same prescribed
cuts with explicit insertions. More precisely, write
\[
 C_N(\mathbf z_H)=
    \sum_{\mathbf j\in\{0,\ldots,d\}^{H}}
       c_{\mathbf j}\prod_{h\in H}e_{j_h}(z_h).
 \tag{17}
\]
Then
\[
 c_{\mathbf j}=
   \eta^{|H|}L^{\otimes H}
       \left[
        \left(\prod_{h\in H}e_{d-j_h}(\Omega_h)\right)X_{S,N}
       \right].
 \tag{18}
\]
Equations (13), (17), and (18) recover the entire ordinary boundary
polynomial \(B_N\). They hold at every \(N\ge2\), for every choice
of signed integers \(n_v\), without a long-twist hypothesis.

**Proof.** Expand the finite edge sums in (9) before taking any
trace. Each summand is a tensor product of elements of the filled
pair algebras and canonical polynomials at the separate free
incidences. Under the algebra homomorphism \(\iota\), the crossing
factor becomes \(R_{\rm ext}^{-n_v}\), and the edge factors become
(14). At each filled pair, (5) gives
\(\phi_v=\eta L_v\iota\). Taking these finite contractions proves
(16) and the claimed membership. No pair has been projected onto
its distinct eigenspaces.

Apply the right-hand side of (18) to the expansion of (16)
obtained from (17). On each free pair, equations (3) and (5) give
\[
 \eta L\bigl(e_{d-j}(\Omega_{\rm ext})
                      e_i(\Omega_{\rm ext})\bigr)
       =\phi(e_{d-j}e_i)=\delta_{i,j}.
 \tag{19}
\]
The product of these equalities extracts precisely
\(c_{\mathbf j}\). Finally, substituting the common variable at
each free vertex gives (13), term by term in the ordinary
polynomial ring. This proves the theorem. \(\square\)

The same algebraic proof permits identity connections
\[
 K_I(z,w)=\sum_{i=0}^d e_i(z)e_{d-i}(w)
 \tag{20}
\]
in place of selected turn connections, and the corresponding
operator substitutions in (14). Which connection occurs is fixed
by the original Conway expression. More generally, the source
compiler writes every finite original Conway expression using
these kernels, multiplication, crossing powers, and \(\phi\).
Equation (5) intertwines multiplication and crossing powers, and
(19) intertwines the contractions. Induction on that expression
therefore proves the same boundary comparison. If a free ordinary
product has several factors, its incidences are kept separate
until the last substitution, exactly as above.

The separately proved cup and cap formulas provide the explicit
external boundary extension for a physical turn. They give
\(\mathcal T_{\rm ext}(e_i(\Omega_{\rm ext}))
=e_{d-i}(\Omega_{\rm ext})\), with the original cup and cap
normalizations. Thus (20) and (14) encode the actual identity and
turn operations. This does not assert that the external repository
already implements arbitrary open Conway tangles.

## 4. Derivatives and the eventual closing functional

The reconstruction includes the repeated-root derivatives in every
independent variable by (7). It also determines derivatives of any
fixed order of the unreduced ordinary polynomial in (13). Indeed,
ordinary polynomial differentiation gives, for \(k\ge0\),
\[
 \partial_{z_u}^{\,k}B_N=
 \left.
  \left(\sum_{h=(e,u)}\partial_{z_h}\right)^k C_N
 \right|_{z_{(e,v)}=z_v}.
 \tag{21}
\]
For an empty incidence set the right-hand side is zero when \(k>0\).
The multinomial expansion in (21) includes every way of distributing
the derivative among factors at \(u\). Derivatives at several free
vertices follow by taking the product of these commuting differential
operators.

There is no ambiguity about subsequent filling. If the remaining
signed powers are \(m_u\), apply the original remaining functional
\[
 \mathcal C_{\mathbf m}(B)=
       \left(\bigotimes_{u\in U}\phi_u\right)
       \left[\prod_{u\in U}R(z_u)^{m_u}\,B(\mathbf z_U)\right].
 \tag{22}
\]
At this final step its arguments are passed to \(\mathcal A_N\),
as required by the original trace. Since (13), (17), and (18)
recover \(B_N\) as an ordinary polynomial, (22) is exactly the
original completed source scalar. Any prescribed exterior
functional applied to that polynomial likewise agrees.

If the completed diagram is instead evaluated as a braid in the
external convention, the separate cut lemma gives its exact
comparison: the physical word has reversed crossing signs, and
the pivot and writhe factors are those of that lemma. They are
not absorbed into a positive amplitude. For an exterior that is
not an intertwiner, the unrestricted highest-head matrix
functional must be retained; its replacement by an averaged trace
is not justified.

## 5. Why a single boundary matrix would have lost information

At one free vertex the map from ordinary polynomials to a single
pair operator has kernel \((P_N)\). The nonzero ordinary polynomial
\(P_N(z)\) is sent to zero. Therefore a boundary product of degree
at least \(N\) cannot in general be recovered from one pair
operator, even if its values and first derivatives at all Casimir
roots are known. Those data recover its class, not the whole
ordinary polynomial.

The separate-incidence construction avoids this loss because each
of its variables has degree below \(N\). The tensor product of the
faithful maps (5) is injective on that space, and (18) is its
explicit inverse. The ordinary diagonal substitution is performed
only after this inverse.

For \(h=|H|\) free incidences there are \(N^h\) coefficients in
(17). Thus the representation has polynomial dimension in \(N\)
for each fixed component, with no restriction on its fixed powers.
This dimension count is not a bound on the condition number of
the reconstruction.

## 6. What this gives the noncancellation problem

The boundary correspondence removes a concrete ambiguity: the
external matrix presentation, its specified closing trace, and
the original Newton boundary source now agree exactly, including
the derivatives that would be lost by diagonalizing the pair
Casimir. The theorem applies to arbitrary fixed short components
in the original compositional calculus.

It does not give a lower bound for the geometric contribution
after closing. The coefficient observations in (18) form a
separating family; the required volume identity uses one prescribed
completed contraction. A nonzero vector can have zero value under
that contraction. Also, although the single-head change of basis
(4) is unitary in the coordinate norms, the Newton reconstruction
and the inserted dual observations need not have uniformly
bounded condition numbers.

The next analytic statement must therefore control the original
geometric observation of (15), with its phases and the original
closing functional retained. Exact recoverability of the boundary
is available for that statement; a nonzero geometric asymptotic
coefficient is not yet a consequence.

## 7. Direct proof dependencies

The original pair algebra, its faithful physical realization, dual
Newton basis, and full turn are proved in
[the finite Newton calculus](../papers/newton-calculus/finite.tex),
SHA256 2db2d7e15df0210c32bace4c761bdabadbb5d67140473a61425dac4d1e382f8e.
The source (9) and the extension to finite Conway expressions are
proved in [the arbitrary-power source compiler](research_arbitrary_power_source_compilation.md),
SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f.

The external representation and sign in (5) are proved in
[the local crossing comparison](research_rivin_jones_local_crossing_adapter.md),
SHA256 c4a9a92ec22f31a035036642e0621ef9abe569646b2488dbac2d2add786500f0.
The prescribed cut and reconstruction used in (5), (18), and (22)
are proved in [the cut and Hermite recovery note](research_rivin_jones_prescribed_cut_and_hermite_recovery.md),
SHA256 1b0e105ffb67b2b8552f5fddc5f0a3ac009e9795b33e27599ac4726ebd74079e.
The turn is realized by the explicit regular bends in
[the boundary-extension note](research_rivin_jones_regular_bends_and_newton_turn.md).
These are written algebraic identities; no numerical checks or
external code execution are used here.
