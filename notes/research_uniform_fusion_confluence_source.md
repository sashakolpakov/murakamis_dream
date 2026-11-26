# Uniform confluence depth for the original generic fusion source

Written research proof, 22 November 2026.

The generic fusion coordinates of the actual invariant source can be
regularized using a number of quantum-parameter jets bounded by tensor
width, independently of the level. An explicit Clebsch inclusion and
Casimir-projector dual give the pole bound. Finite coefficient equations
then recover the saturated root source without an unspecified large
minor inverse.

The saturated source and its divided-current characterization are
already known in [S,D]. The new assertion is an effective uniform
confluence budget for its actual generic fusion frames. This is not
an analytic norm bound or an identification with a formal cyclic
tetrahedron kernel.

## 1. The actual family and the statement

Fix \(N\ge2\), \(d=N-1\), \(q_0=e^{\pi i/N}\), and an even
number \(\ell\ge2\) of physical heads. Let
\[
 u=\zeta-q_0,\qquad
 \mathcal O=\mathbb C\{u\},\qquad
 \mathcal K=\operatorname{Frac}(\mathcal O),\qquad
 \rho=\zeta-\zeta^{-1},\quad
 [j]=\frac{\zeta^j-\zeta^{-j}}{\rho},\quad
 [j]!=\prod_{r=1}^j[r].
 \tag{1}
\]
All half-integral Cartan powers use the fixed analytic logarithm
of \(\zeta\) near \(q_0\). A pole bound \(J\) means that multiplying
every matrix entry by \(u^J\) makes it regular. The neighborhood
in \(u\) may depend on \(N\); no uniform analytic radius is asserted.

Use the actual generic balanced leaf family of [S], and put
\[
 \mathcal M_{\mathcal O}=V_d(\zeta)^{\otimes\ell},\qquad
 \mathcal I_{\mathcal K}
       =\operatorname{Inv}_{\mathcal K}
                    (\mathcal M_{\mathcal O}\otimes\mathcal K),
 \quad
 \Lambda=\mathcal I_{\mathcal K}\cap\mathcal M_{\mathcal O}.
 \tag{2}
\]
The lattice is saturated, free of rank
\(g=\dim_{\mathcal K}\mathcal I_{\mathcal K}\), and its root fiber
\[
                 \mathcal V=\Lambda/u\Lambda
                    \ \subset\ \mathcal M_{\mathcal O}/u\mathcal M_{\mathcal O}
 \tag{3}
\]
is embedded in the original physical root tensor.
These statements, and the fact that every original regular
braid/cup source lies in this fiber, are established in [S,D].
The entire raw root invariant space may be larger than (3).

**Theorem.** For every binary fusion tree \(T\) with the \(\ell\)
leaves labelled \(d\) and root label zero, there are explicitly
defined matrices
\[
 B_T:\mathcal K^g\longrightarrow
                   \mathcal M_{\mathcal O}\otimes\mathcal K,\qquad
 L_T:\mathcal M_{\mathcal O}\otimes\mathcal K
                   \longrightarrow\mathcal K^g
 \]
such that
\[
 \operatorname{im}B_T=\mathcal I_{\mathcal K},\qquad
 L_TB_T=I,\qquad
 u^{J_\ell}B_T,\ u^{J_\ell}L_T
                  \text{ have regular entries},\qquad
 J_\ell=(5\ell+4)(\ell-1).
 \tag{4}
\]
Consequently the intrinsic fusion-coordinate lattice
\(\Lambda_T=B_T^{-1}\Lambda\) satisfies
\[
          u^{J_\ell}\mathcal O^g
                   \subset\Lambda_T
                   \subset u^{-J_\ell}\mathcal O^g .
 \tag{5}
\]
All confluence depths are therefore bounded in terms of width,
independently of \(N\), including even and composite levels.

More explicitly, set \(J=J_\ell\), \(C_T=u^JB_T\). The full
physical source fiber is computed by the finite formula
\[
 \boxed{\quad
 \mathcal V=
 \left\{[u^{2J}](C_Tz):
 \begin{array}{l}
 z\in(\mathcal O/u^{2J+1})^g,\\
 [u^k](C_Tz)=0\quad(0\le k<2J)
 \end{array}\right\}.
 \quad}
 \tag{6}
\]
Thus the Laurent coefficients of \(B_T\) at orders
\(-J,\ldots,J\) suffice. No jet of an unknown knot value enters.

If \(W\) is any whole actual regular physical braid word, then
\[
                 L_{T'}WB_T
                    \text{ has pole order at most }2J .
 \tag{7}
\]
The bound does not grow with the number of letters in the word.
At the root its action on (3) is simply the restriction of
the original \(W(q_0)\); no positive-order jet of \(W\) is
needed for that root-value operation.

## 2. Generic modules and the actual balanced leaf gauge

For a nonnegative integer color \(A\), use the divided-\(F\)
basis \(v_j^{(A)}=F^jv_0^{(A)}/[j]!\), \(0\le j\le A\).
The matrices are
\[
 Fv_j=[j+1]v_{j+1},\qquad
 Ev_j=[A-j+1]v_{j-1},\qquad
 Kv_j=\zeta^{A-2j}v_j ,
 \tag{8}
\]
with the missing endpoint arrows zero. These matrices have
Laurent-polynomial entries for every color. Use
\[
 \Delta E=E\otimes K+I\otimes E,\qquad
 \Delta F=F\otimes I+K^{-1}\otimes F .
 \tag{9}
\]
The normalized Casimir is
\[
              \Omega=\rho^2FE+\zeta K+\zeta^{-1}K^{-1}.
 \tag{10}
\]
It has eigenvalue
\(\lambda_A=\zeta^{A+1}+\zeta^{-A-1}\) on a highest
weight \(A\) module.

For an actual leaf \(A=d\), define
\[
 s_a=(-\rho)^{-a}\zeta^{-a(a+1)/2},\qquad
                         w_a=s_av_a^{(d)} .
 \tag{11}
\]
Direct substitution gives
\[
 \begin{split}
 Fw_a&=(1-\zeta^{2a+2})w_{a+1},\\
 \rho^2Ew_a&=\zeta^{-N}
                 (1-\zeta^{2(N-a)})w_{a-1},\\
 Kw_a&=\zeta^d\zeta^{-2a}w_a.
 \end{split}
 \tag{12}
\]
These are exactly [S]'s actual balanced generic matrices,
including their zero endpoint arrows. Every \(s_a\) and its
inverse is a DVR unit at \(q_0\), because \(\rho(q_0)\ne0\).
The gauge and all its phases are retained on the physical
source, operators and rows. Its possible large complex norm
is not discarded or claimed bounded.

## 3. A literal Clebsch inclusion and an elementary generic decomposition

Take colors \(A,B\) and
\[
 C=A+B-2k,\qquad 0\le k\le\min(A,B).
 \]
There is a highest vector
\[
 h_C=\sum_{r=0}^k b_r\,
           v_r^{(A)}\otimes v_{k-r}^{(B)},\qquad b_0=1 .
 \tag{13}
\]
The equation \(\Delta E\,h_C=0\) gives exactly
\[
 \frac{b_{r+1}}{b_r}
   =-\zeta^{-B+2k-2r-2}
                   \frac{[B-k+r+1]}{[A-r]},
 \quad
 b_r=(-1)^r\zeta^{r(2k-B-r-1)}
          \frac{[B-k+r]![A-r]!}{[B-k]![A]!}.
 \tag{14}
\]
This follows by comparing the coefficient of
\(v_r^{(A)}\otimes v_{k-r-1}^{(B)}\).
Define
\[
       \iota_{A,B}^{C}(v_j^{(C)})
                        =\frac{(\Delta F)^j}{[j]!}h_C .
 \tag{15}
\]
This is the prescribed inclusion, with all normalization
phases fixed by (13)--(14).

For completeness these inclusions give the entire generic
pair tensor. The elementary commutator calculation gives
\[
 (\Delta E)(\Delta F)^j h_C
       =[j][C-j+1](\Delta F)^{j-1}h_C .
 \tag{16}
\]
It proves nonvanishing through \(j=C\). If \(F^{C+1}h_C\)
were nonzero, it would be a highest vector of negative
weight \(-C-2\). Its subsequent \(F\)-string could not
terminate: all the coefficients in (16), with that
negative highest weight, are nonzero over \(\mathcal K\).
This contradicts nilpotence of \(F\) on the finite tensor.
Hence (15) is an intertwiner from the full \(V_C\).
Its Casimir eigenvalue is \(\lambda_C\).

The eigenvalues for the distinct allowed colors \(C\) are
distinct over \(\mathcal K\). The images are therefore
independent, and
\[
       \sum_{k=0}^{\min(A,B)}(A+B-2k+1)=(A+1)(B+1)
 \tag{17}
\]
shows that they exhaust the tensor product. No
semisimplicity theorem at the root has been used.

## 4. An exact projector dual with a bounded pole order

Let \(\mathcal C(A,B)\) be the allowed color list in (13).
On the generic pair put
\[
 P_C(\Omega)=
   \prod_{\substack{D\in\mathcal C(A,B)\\D\ne C}}
                  \frac{\Omega-\lambda_DI}{\lambda_C-\lambda_D}.
 \tag{18}
\]
This is a generic projector, not a root specialization
of distinct Casimir values.
Let \(\varepsilon_{0,k}\) extract the coefficient of
\(v_0^{(A)}\otimes v_k^{(B)}\).
On the pair degree \(k+j\), define
\[
 \pi_{A,B}^{C}(y)=
   \frac{[C-j]!}{[C]!}\,
       \varepsilon_{0,k}(\Delta E)^jP_C(\Omega)y\,
                                      v_j^{(C)}
                    \quad(0\le j\le C);
 \tag{19}
\]
on the other degrees define it to be zero.
Since
\[
    E^jv_j^{(C)}=\frac{[C]!}{[C-j]!}v_0^{(C)},
       \qquad \varepsilon_{0,k}h_C=1 ,
 \]
the complete decomposition just proved gives
\[
 \pi_{A,B}^{C}\iota_{A,B}^{D}=\delta_{CD}I,\qquad
            \sum_C\iota_{A,B}^{C}\pi_{A,B}^{C}=I .
 \tag{20}
\]
The dual is therefore literal and explicit. No unknown
minor or favorable Hermitian form defines its normalization.

Every positive integer quantum factorial satisfies
\[
            \operatorname{ord}_{u=0}[m]!=\lfloor m/N\rfloor .
 \tag{21}
\]
Indeed \([j]\) has a simple zero precisely when \(N\mid j\);
its denominator \(\rho\) is a unit. All colors in a tree
with \(\ell\) leaves are at most \(\ell d<\ell N\).
Equation (14) is a regular numerator divided by the
product \([A][A-1]\cdots[A-r+1]\).
Its pole order is at most \(\lfloor A/N\rfloor\le\ell\).
The descendant denominator \([j]!\) in (15) contributes
at most \(\ell\). Thus every inclusion has pole bound \(2\ell\).

For the projector dual, the exact factorization
\[
 \lambda_C-\lambda_D
   =\zeta^{-C-1}(1-\zeta^{C-D})(1-\zeta^{C+D+2})
 \tag{22}
\]
counts all possible vanishing denominators.
The allowed \(D\)'s progress in steps of two over a list
of length at most \(\ell N+1\).
Each of the two congruences in (22) occurs at most
\(\ell+2\) times. Each vanishing factor is simple;
\(C-D\ne0\) and \(C+D+2>0\).
When both congruences hold they are counted twice.
The whole denominator of (18) consequently has valuation
at most \(2\ell+4\), in particular at most \(4\ell+4\).
Its numerator is a product of regular matrices.
The factorial ratio in (19) has pole order at most
\(\lfloor C/N\rfloor\le\ell\), and \((\Delta E)^j\)
is regular. Every dual therefore has pole bound \(5\ell+4\).

All estimates hold for each \(N\ge2\), with no prime-level
or parity assumption. They are valuations, not estimates
of the size of the nonzero factors.

## 5. Complete tree frames and whole physical words

Compose (15) at the vertices of a binary tree, with root
color zero and all admissible internal colors retained.
Each root vector \(1\in V_0\) gives one invariant column.
These columns form \(B_T\). Compose the duals (19) in the
reverse order to obtain the rows of \(L_T\).
Iterating (20) proves exactly that their columns form a
basis of the generic invariant space and \(L_TB_T=I\).
There are \(\ell-1\) internal vertices. A finite sum does
not worsen a pole bound, while product bounds add.
The local estimates therefore prove (4) with the stated
\(J_\ell=(5\ell+4)(\ell-1)\).
Conjugating the external leaves by the unit gauge (11)
gives the same bounds in the actual physical coordinates.

The lattice \(\Lambda\) is intrinsic, not chosen separately
by a tree or word. If \(z\in\mathcal O^g\), then
\(u^JB_Tz\) is regular and invariant, proving the first
inclusion in (5). Conversely, if \(B_Tz=\psi\in\Lambda\),
then \(z=L_T\psi\in u^{-J}\mathcal O^g\), proving the second.
This bounds the elementary lattice exponents without
inverting a determinant of growing size.

Every whole original physical braid matrix \(W\) and its
inverse are regular at \(q_0\): each individual physical
crossing has finite summation indices below \(N\), hence
only nonvanishing leaf factorial denominators.
The actual cups and ordinary dualities are regular as in [S,M].
Regular generic polynomial circle coupons are included as well.
Such maps preserve the generic invariant source and hence
the saturated lattices. For an endomorphism word,
\[
           \operatorname{ord}_{u=0}(L_{T'}WB_T)\ge-2J
 \tag{23}
\]
entrywise, no matter how many regular letters occur in \(W\).
This is a bound on the whole product, not a sum of the
apparent pole orders of sequential recoupling moves.

Between the intrinsic lattices \(\Lambda_T,\Lambda_{T'}\),
the generic change of tree is an isomorphism, with inverse
the reverse change. In any actual lattice bases its matrix
is unimodular over \(\mathcal O\). The generic coordinate
matrices before this regularization need not be regular.
Their root values must not be substituted for their
complete confluence data.

## 6. The finite jet construction and the literal root closing

Let \(C_T=u^JB_T\), a regular rectangular matrix.
For any \(\psi\in\Lambda\), set \(x=L_T\psi\in u^{-J}\mathcal O^g\)
and \(z=u^Jx\in\mathcal O^g\). Then
\[
                         C_Tz=u^{2J}\psi.
 \tag{24}
\]
Truncating \(z\) modulo \(u^{2J+1}\) does not change any
coefficient in (6). Thus every root source vector occurs
in its right side.
Conversely, a polynomial representative \(z\) satisfying
the equations in (6) gives
\[
                    \psi=u^{-2J}C_Tz\in\mathcal M_{\mathcal O}.
 \]
It is generically invariant, hence belongs to \(\Lambda\),
and its root is the displayed coefficient in (6).
This proves that finite formula in both directions.
In particular the jet budget is \(2J\) for the regular
matrix \(C_T\), or orders \(-J,\ldots,J\) for \(B_T\).

Choose \(g\) independent root vectors from (6). Their
integral lifts just constructed form a basis of \(\Lambda\):
their reductions form a basis of the embedded fiber,
so the assertion follows by the elementary local basis
criterion over a DVR. This also gives regularized
tree frames without choosing an unspecified generic minor.
The number of matrix entries and source coordinates
still grows with \(N\); only the required jet order
is bounded independently of \(N\).

For the original cup source \(b_N\), and any specified
original root co-source row \(\lambda_N\), including the
literal marked cap, the original scalar remains
\[
                         \lambda_N W(q_0)b_N .
 \tag{25}
\]
By [S,D], \(b_N\in\mathcal V\) and each regular original
gate preserves that source. Formula (6) computes the same
space in the actual physical tensor coordinates.
One may therefore restrict each root gate to \(\mathcal V\)
and restrict the very same row \(\lambda_N\), without
changing (25). All cup, pivot, framing and external
normalization factors remain in those specified data.
No trace average or unmarked cap replaces them.

For a root-value contraction this restriction needs
only the actual \(W(q_0)\) and the frame jets in (6).
There is no demand for positive-order jets of a long
word merely because its fusion coordinates have poles.
An independently prescribed quantum-normal source
still requires its own differentiated word and cap
data; these are not determined by \(W(q_0)\).

## Complete proof sources and scope

All three complete texts were read at renewed matching pins:

| Label | Complete source | SHA-256 |
|---|---|---|
| S | [Deformable original source, 327 lines](actual_six_port_deformable_source_and_recoupling.md) | e29acfe75fb61cead48a08691037d6b81041bb5115b6578c9d2b563c8664c049 |
| M | [Complete physical source module, 602 lines](actual_complete_source_multiplicity_module.md) | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| D | [All-width divided source filter, 204 lines](actual_all_width_divided_source_projection.md) | dc83b5e232a3d258f516a479d7257e85b9e5663a38e166f07c6ad9ae81004a68 |

The source lattice, its exact divided-current kernel,
and its source-preserving orthogonal compression were
already established in those notes. In particular this
does not identify the larger raw root Hom space with
the generic source. Generic Clebsch decompositions,
recoupling, and DVR saturation are also established
methods. The content here is the explicit dual and
uniform pole budget, the finite-jet realization, and
the whole-word bound with the original source retained.

No eigenprojector is specialized separately: the entire
frame confluence, including its Casimir Jordan normal
coefficients on the original source, is retained.
No analytic bound for the fusion matrices or their
positive Grams follows from a bounded valuation.
No equality with the earlier formal cyclic \(\Phi\),
its projected pentagon, or a geometric critical module
has been asserted. The familiar generic compatibility
of actual frame changes is not a new pentagon theorem.
The resulting sharp coherent word estimate, original
scalar lower bound, and finite-exception theorem remain
separate and unproved.

Only written mathematics and text/hash inspection were used.
No program, numerical experiment, test, build, git action,
or earlier-final file edit was performed.
