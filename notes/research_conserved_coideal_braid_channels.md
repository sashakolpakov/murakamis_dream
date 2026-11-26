# Conserved coideal channels with the original braid source

24 November 2026. Research note. Written proof.

A particular conserved combination of the actual total generators has
an exact degree-\(N\) polynomial on every complete-color tensor power.
Its full matrix is a repeated companion matrix, including the Jordan
directions at the exceptional parameters. For a stable exterior range
of the auxiliary parameter, its conserved channels can be made
orthogonal with metric logarithm of order at most the level. Pinching
the original closing into these channels is exact against the original
intertwining word. The closing is retained and is not made positive.

The corresponding classical Hamiltonian is an explicit simultaneous
conjugation flow. Its zero level gives the residual parabolic framing
motion. These facts do not identify a selected quantum channel with a
geometric period or establish a nonzero scalar coefficient.

## 1. Complete finite matrices and the conserved element

Fix \(N\ge2\), width \(b\ge1\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad h=2\pi i/N,\quad
 x=-q^{-1},\quad \gamma=x^N=(-1)^{N+1},\quad
 \sqrt q=e^{\pi i/(2N)}.
 \tag{1}
\]
Use the factorial basis of W, declared orthonormal for the estimates
below. At the complete meridian \(M=1\), its actual generators are
\[
 K e_a=xQ^{-a}e_a,\quad
 E e_a=(Q^{-a}-1)e_{a-1},\quad
 F e_a=(1-Q^{a+1})e_{a+1}.
 \tag{2}
\]
The absent arrows at \(a=0,N-1\) are zero. Here \(E\) is W's
scaled \(\mathcal E\), not an unscaled unrolled generator.
Retain the ordered coproducts
\[
 K_{12}=K_1K_2,\qquad E_{12}=E_1K_2+E_2,\qquad
 F_{12}=F_1+K_1^{-1}F_2.
 \tag{3}
\]
Write their width-\(b\) iterates as \(\mathsf K,\mathsf E,\mathsf F\).
Every literal unmarked checked braid word \(R\) commutes with all
three, including its original signed crossing scalars.

For an auxiliary scalar \(c\in\mathbb C\), define
\[
 B_c^{(b)}=\mathsf F-(\mathsf E-cI)\mathsf K^{-1},\qquad
 H_c^{(b)}=B_c^{(b)}-2I.
 \tag{4}
\]
These commute with \(R\). The order in (4) is fixed. In particular
\(H_c\mathsf K=-(2\mathsf K+\mathsf E-\mathsf F\mathsf K-cI)\);
replacing \(\mathsf F\mathsf K\) by \(\mathsf K\mathsf F\)
would change the finite operator. Direct substitution in (3) gives
\[
 B_c^{(b)}=(F_1-E_1K_1^{-1})\otimes I
                 +K_1^{-1}\otimes B_c^{(b-1)},\qquad B_c^{(0)}=c.
 \tag{5}
\]
Equivalently \(Y_c=B_c-cI\) satisfies
\(\Delta Y_c=Y_c\otimes1+K^{-1}\otimes Y_c\).
Since \(K\) is unitary and \(\|E\|,\|F\|\le2\),
\[
 \|\mathsf E\|,\|\mathsf F\|\le2b,\qquad
                         \|B_c^{(b)}\|\le4b+|c|.
 \tag{6}
\]

## 2. A finite cyclic determinant with all zero arrows retained

Define the monic polynomial
\[
 p_N(z)=\prod_{s^N=1}(z-s-q/s)
       =2q^{N/2}T_N\!\left(\frac{z}{2\sqrt q}\right),
 \qquad q^{N/2}=i.
 \tag{7}
\]
Here \(T_N\) is Chebyshev of the first kind. To verify (7), put
\(z=\sqrt q(v+v^{-1})\). Both monic sides vanish when
\(v=s/\sqrt q\), since \(v^N=-i\) and \(v^{-N}=i\).
These \(N\) values of \(z\) are distinct: a collision of two
different \(s,t\) would require \(st=q\), impossible after
taking \(N\)-th powers. Thus the monic polynomials agree.

On one head let \(S e_a=e_{a+1\bmod N}\) and
\(C e_a=Q^ae_a\). Formula (2) gives the exact identity
\[
 B_c^{(1)}=A(S)-T_c(S)C,\qquad
 A(s)=s+q/s,\qquad T_c(s)=Qs+q/s+cq.
 \tag{8}
\]
Indeed \(F=S(1-QC)\), \(-EK^{-1}=qS^{-1}(1-C)\), and
\(cK^{-1}=-cqC\). The two apparent cyclic boundary arrows vanish
individually. No wrap term was inserted or removed in (8).

Diagonalize the unitary cyclic shift \(S\). In that basis \(C\)
is a single cyclic permutation. The determinant of
\(z-A(S)+T_c(S)C\) has only its diagonal permutation and its
complete-cycle permutation. Since \(T_c(s)/q=A(s^{-1})+c\) and
\(q^N=-1\), this proves
\[
 \det(zI-B_c^{(1)})
   =p_N(z)+(-1)^{N-1}\prod_{s^N=1}T_c(s)
   =p_N(z)+p_N(-c).
 \tag{9}
\]
The argument is polynomial in \(c\); no coefficient is assumed
nonzero. It includes \(N=2\). For example then
\(p_2(z)=z^2-2i\) and \((B_c^{(1)})^2=(4i-c^2)I\).

Cayley--Hamilton and \(p_N(-z)=(-1)^Np_N(z)\) yield
\(p_N(B_c^{(1)})=\gamma p_N(c)I\). This is a polynomial
matrix identity in the scalar parameter. Substitute the commuting
tail matrix from (5) for that parameter and induct. The result is
\[
 \boxed{\quad p_N(B_c^{(b)})=\gamma^b p_N(c)I,\qquad
       q_{N,b,c}(z):=p_N(z)-\gamma^bp_N(c).\quad}
 \tag{10}
\]
This proof applies to the entire tensor power, without semisimplifying
its quantum-group module.

## 3. Exact free companion form and its cost

Put \(d_b=N^{b-1}\) and
\(\mathfrak f_k=(Q;Q)_k=\prod_{a=1}^k(1-Q^a)\),
\(\mathfrak f_0=1\). Consider the block Krylov matrix
\[
 \mathcal S_b=[\,e_0\otimes I_{d_b},\ B_c(e_0\otimes I_{d_b}),
                  \ldots,B_c^{N-1}(e_0\otimes I_{d_b})\,].
 \tag{11}
\]
To reach first-head index \(k\) from zero in \(k\) steps, every
step must use \(F_1\). Consequently (11) is block triangular
with diagonal blocks \(\mathfrak f_k I_{d_b}\), all nonzero.
Relation (10) now gives
\[
 \boxed{\quad \mathcal S_b^{-1}B_c^{(b)}\mathcal S_b
           =\operatorname{Comp}(q_{N,b,c})\otimes I_{d_b}.\quad}
 \tag{12}
\]
The companion convention is the basis \(1,z,\ldots,z^{N-1}\).
Thus \(q_{N,b,c}\) is the minimal polynomial, and the
characteristic polynomial is \(q_{N,b,c}^{\,d_b}\), for every
\(c\). Every Jordan block of the scalar companion occurs
\(d_b\) times. No normal channel is lost at a collision.

Equivalently the full head space is free of rank \(d_b\) over
\(A_{N,b,c}=\mathbb C[t]/q_{N,b,c}(t)\), and the full commutant
of \(B_c\) is
\[
 \operatorname{End}_{A_{N,b,c}}(V_N^{\otimes b})
                      \simeq\operatorname{Mat}_{d_b}(A_{N,b,c}).
 \tag{12a}
\]
Every original braid word lands in this algebra. If
\(\gamma^bp_N(c)=-2i\), the substitution \(t=\sqrt q\,z\)
identifies \(A_{N,b,c}\) with F's full Conway quotient
\(\mathbb C[z]/(2T_N(z/2)+2)\), retaining its double-root normals.
This does not identify the transported original closing with that
quotient's canonical Frobenius functional or with a knot A-polynomial.

There are controlled inverse bounds for (11), not merely a nonzero
determinant. For \(T=B_c^{(b-1)}\), let the monic polynomials with
commuting operator coefficients satisfy
\[
 D_0=I,\quad D_{-1}=0,\qquad
 D_{k+1}(z;T)=(z+qQ^kT)D_k(z;T)
                    -q(1-Q^k)^2D_{k-1}(z;T).
 \tag{13}
\]
The first-head tridiagonal entries give
\(D_k(B_c;T)(e_0\otimes I)=\mathfrak f_k(e_k\otimes I)\).
For fixed width and \(|c|\le C_*\), (6) and (13) bound the
sum of coefficient norms of \(D_k\) by \(C_1^k\).
Also sine complementation gives
\[
 |\mathfrak f_{N-1}|=N,\qquad
 |\mathfrak f_k|^{-1}
       =|\mathfrak f_{N-1-k}|/N\le2^{N-1-k}/N.
 \tag{14}
\]
Expanding the identities after (13) expresses each coordinate block
in the Krylov columns. Together with (6), this proves
\[
 \|\mathcal S_b\|+\|\mathcal S_b^{-1}\|
                           \le \exp(C_{b,C_*}N).
 \tag{15}
\]
All these bounds include the exceptional parameters. The recurrence
(13) is an Al-Salam--Chihara specialization; no new recurrence or
orthogonal-polynomial technique is claimed.

The roots of (10) are simple except when its right side is a critical
value of \(p_N\). For \(N\ge3\) these values are \(\pm2i\);
for \(N=2\) only \(-2i\) is critical. At a critical value all
multiple roots have multiplicity exactly two. Formula (12) therefore
specifies the whole exceptional Jordan form, with block length at
most two, rather than replacing it by its value quotient.
These normal channels are generalized eigenspaces; this does not
transport meridian or off-root quantum-parameter derivatives.

## 4. An orthogonal channel metric on a stable parameter range

Assume \(4\le|c|\le C_*\). Choose \(w\) with
\(w+w^{-1}=c/\sqrt q\) and \(|w|>1\), and choose
\(\varepsilon^N=\gamma^b\), \(|\varepsilon|=1\). The roots are
\[
 \lambda_j=\sqrt q(\varepsilon wQ^j+
                       \varepsilon^{-1}w^{-1}Q^{-j}),
       \qquad 0\le j<N,
 \qquad |w|\ge2+\sqrt3.
 \tag{16}
\]
They are distinct. For \(j\ne k\), factoring their difference gives
\[
 |\lambda_j-\lambda_k|
       \ge(|w|-|w|^{-1})|Q^j-Q^k|,
 \quad
 \prod_{k\ne j}|\lambda_j-\lambda_k|
       \ge N(|w|-|w|^{-1})^{N-1}.
 \tag{17}
\]
Use the full spectral idempotents
\[
 \Pi_j=\prod_{k\ne j}
                   \frac{B_c-\lambda_kI}{\lambda_j-\lambda_k},
 \qquad G_c=\sum_j\Pi_j^*\Pi_j.
 \tag{18}
\]
Equations (6), (16)--(17) prove \(\|\Pi_j\|\le e^{C_{b,C_*}N}\).
Their sum is the identity, so Cauchy--Schwarz also proves
\[
 N^{-1}I\le G_c\le N e^{C_{b,C_*}N}I,\qquad
                       \|\log G_c\|=O_{b,C_*}(N).
 \tag{19}
\]
Indeed \(G_c\Pi_j=\Pi_j^*\Pi_j=\Pi_j^*G_c\). The \(N\) full
eigenspaces have dimension \(d_b\) and are exactly orthogonal in
\(G_c\). Nothing inside a conserved eigenspace has been projected away.

The estimates survive the explicit factorial coordinate adapter.
If \(v_a=\mathfrak f_a e_a\), then
\(Fv_a=v_{a+1}\),
\(Ev_a=(1-Q^a)(Q^{-a}-1)v_{a-1}\), and \(K\) is unchanged.
This is the undivided complete module with its scaled \(E\).
The diagonal change and its inverse have norms \(e^{O(N)}\)
by (14) and \(|\mathfrak f_a|\le2^a\). On fixed tensor width,
transporting (19) to those raw physical coordinates still has
logarithmic radius \(O(N)\). This is an exponential controlled
adapter, not a polynomial equivalence of the two Hilbert metrics.
The original diagonal pivot and cut commute with that adapter.

For M's operator packets use the induced Hilbert--Schmidt metric
\(\|A\|_{{\rm HS}(G_c)}=\|G_c^{1/2}AG_c^{-1/2}\|_{\rm HS}\).
Its column-vectorization Gram is \(\overline{G_c}^{-1}\otimes G_c\),
with logarithmic radius at most \(2\|\log G_c\|=O(N)\).
Simultaneous conjugation transports multiplication and its original
root row exactly. Putting this packet metric on the complete-color
block and the identity metric on M's ordinary anchor block therefore
lies in a known color-preserving window of the same \(O(N)\) order,
enlarged if necessary. The
head metric and the operator-packet metric have different dimensions.
The polynomial (10) itself is asserted only
at the complete meridian. At other colors the deleted lower arrow
does not equal the corresponding cyclic coefficient; no ordinary-color
or whole-meridian polynomial identity is inferred from (8).

## 5. The original closing and its exact channel sum

Retain W's whole original source at this complete root:
\[
 P=T_0\otimes g^{\otimes(b-1)},\qquad
 T_0=e_0e_0^*,\quad g=K^{1-N},\qquad
 \Phi(O)=\varkappa_\beta\operatorname{Tr}(PO).
 \tag{20}
\]
The framing/peripheral scalar \(\varkappa_\beta\) is unchanged.
For a simple spectrum define
\(P^{\rm diag}=\sum_j\Pi_jP\Pi_j\). Whenever \([O,B_c]=0\),
cyclicity and \(\Pi_j\Pi_k=0\) give the exact identity
\[
 \boxed{\quad
 \operatorname{Tr}(PO)=\sum_j\operatorname{Tr}(\Pi_jP\Pi_jO)
                     =\operatorname{Tr}(P^{\rm diag}O).
 \quad}
 \tag{21}
\]
In particular this applies to the literal unmarked braid word.
All its conserved channels and every compressed closing remain.
At exceptional parameters the primary idempotents, rather than
individual eigenvalue quotients, give the same identity. The size-two
blocks from (12) stay inside them. No near-collision version of (19)
is claimed without a separate separation bound.

For (19), the \(\Pi_j\) are orthogonal projections in the indicated
head metric. Thus pinching also has the exact observation-norm consequences
\[
 \|P^{\rm diag}\|_{G_c\to G_c}\le\|P\|_{G_c\to G_c},\qquad
 \|P^{\rm diag}\|_{{\rm HS}(G_c)}\le\|P\|_{{\rm HS}(G_c)}.
 \tag{22}
\]
The second inequality is the corresponding contraction of root-row
dual norms. For the original row it is usable on the commuting
subalgebra in (21), where the two rows agree.
Neither matrix is asserted positive. General inserted clocks need not
commute with \(B_c\); their off-diagonal channel terms must then be
retained. Equation (21) is not an equality of all marked-current
functionals. This distinction is essential at the original cut.

In the simple-spectrum case there is nevertheless an exact source
advantage: \([P^{\rm diag},B_c]=[P^{\rm diag},H_c]=0\).
Thus its inner Ward boundary vanishes, while its pairing with every
unmarked original braid is unchanged. For a general inserted \(O\),
the exact correction is still
\[
 \operatorname{Tr}(PO)=\operatorname{Tr}(P^{\rm diag}O)
                         +\operatorname{Tr}((P-P^{\rm diag})O).
 \tag{22a}
\]
At a collision, primary pinching alone need not commute with the
nilpotent part. The invariant-probe assertion is not extended to it.

## 6. The classical Hamiltonian and the finite flow

Use W's regular Gauss symbols and ordered meridians \(H_j\). Their
product is
\[
 G=H_b\cdots H_1=
 \begin{pmatrix}K&e\\Kf&K^{-1}+ef\end{pmatrix},\qquad
 J=\begin{pmatrix}1&-1\\1&-1\end{pmatrix},\qquad
 B_0=\operatorname{Tr}((I+J)G)=2K+e-Kf.
 \tag{23}
\]
The ordered product follows directly from the triangular factors in W
and G. For the scalar Hamiltonian
\[
 H_c=f-2-(e-c)/K=-(B_0-c)/K
 \tag{24}
\]
its derivatives, inserted in W's three exact principal Ward fields,
give simultaneous conjugation by
\[
 X_H=-J-\tfrac12H_cD,\qquad D=\operatorname{diag}(1,-1).
 \tag{25}
\]
Indeed the coefficients are \(-1/K,1,(e-c)/K^2\); their
commutator matrix has lower entry \(-1\), upper entry \(1\),
and diagonal entries \(-1-H_c/2,1+H_c/2\).

The Hamiltonian is conserved. On its level \(H_c=a\), put
\(\lambda=a+2\) and
\(M_\lambda=\left(\begin{smallmatrix}\lambda&-1\\1&0\end{smallmatrix}\right)\).
Then
\[
 \operatorname{Tr}(M_\lambda G)=c,\quad
 X_a=-M_\lambda+\lambda I/2,\quad
 X_a^2=a(a+4)I/4,\quad
 H_j(r)=e^{rX_a}H_j(0)e^{-rX_a}.
 \tag{26}
\]
This is the Hamiltonian trajectory while the required Gauss entries
remain nonzero; the matrix-conjugation expression itself extends farther.
On \(H_c=0\), this is conjugation by \(e^{-rJ}\). For the
complete frame with cut meridian \(\mu=I+sJ\), it fixes that
meridian and is precisely the \(r\)-translation of W. Multiplying
the Hamiltonian by the fixed \(s\) gives W's normalization
\(s\partial_r\). The other parabolic level is \(a=-4\).

The actual finite generator in (4) is an inner derivation, unlike
the different field-dependent current in I. Its exact flow is
\[
 U(r)=\exp(rH_c^{(b)}/h),\qquad P_r=U(r)PU(r)^{-1},\qquad
 \operatorname{Tr}(P_rR)=\operatorname{Tr}(PR),\qquad
 \|U(r)\|,\|U(r)^{-1}\|\le e^{C_{b,C_*}|r|N}.
 \tag{27}
\]
This preserves the whole cut and tail pivot by transporting them.
It does not make them invariant as individual matrices. In fact W's
endpoint and pivot relations give, at this complete root,
\[
 \|[P,H_c]\|\le(4b-2)|Q-1|,\qquad
 ([P,H_c])_{10}=-(1-Q)g^{\otimes(b-1)}\ne0.
 \tag{28}
\]
Here \(10\) denotes the first-head block. To check the bound,
use \([P,K_*^{-1}]=0\),
\([P,H_c]=[P,F_*]-[P,E_*]K_*^{-1}\), the two cut arrows of
size \(|Q-1|\), and tail norms at most \(2(b-1)\).
Thus \(\|[P,H_c]/h\|\le4b-2\). Every meridian derivative and
marked internal defect would still require its own retained source.

## 7. Coverage and remaining comparison

Coideal minimal-polynomial and semisimplicity questions are already
treated at odd-order roots by Shimizu--Sugitani, *Coideal subalgebras
of quantum SL2 at roots of unity*, introduction and Theorem 4.10
([primary text](https://arxiv.org/html/2410.10064v2)). No formula
identification or proof technique from that paper is a premise here.
The standard recurrence also appears in a different Casimir problem
in F. The source-specific assertions proved here use the literal
complete matrices at every \(N\), their free companion form with
controlled cost, and the unchanged braid closing.

G already constructs a different collective trace-Hamiltonian graph,
with an initialized factorial kernel. W already supplies the weighted
centralizer field, and C supplies a finite additive E-flow and relative
endpoints. The present autonomous Hamiltonian does not identify those
different finite currents or import their selected coefficients.

In particular (26) is a principal interior statement, not a whole
finite Egorov estimate through the highest-cut wall. It neither
transports the central highest-cut augmentation to a noncentral
parabolic point nor identifies a relative geometric framing chain.
The auxiliary \(c\), the classical level \(a\), and a quantum
eigenvalue \(\lambda_j\) are distinct data. No projection to
\(\ker H_c\) is made. The full sum (21) can cancel. The metric
cost is controlled exponential, not asserted negligible at the volume
scale. No original scalar lower bound or finite-exception theorem
is inferred.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| W | [Actual weighted Ward lift](research_actual_weighted_ward_centralizer_lift.md) | 345 | e689364ab8e756ef51f8da43a7ea86d84086afd6bf57ffbe0af1a4f508c2648a |
| I | [The different nonderivation current](research_weighted_centralizer_current_and_inner_gauge.md) | 149 | 0e8f912fe7eff45b9a499619286988b47f5d8e2986b01b3cb8c0d52b5524d568 |
| M | [Bounded two-color source metrics](research_main_color_block_regularized_compactness.md) | 357 | 34639ac940ec4b4cd2d290757b378ac846139c2e581e63410d9c5d627c822e1e |
| C | [Original cut and relative E-Ward class](coherent_cut_obstruction_and_ward_relative_class.md) | 336 | 28141e28d4bc08a8acfa4cef9a8549ed7aadb1344f8796617e68282f7b351e4d |
| G | [Initialized collective Gauss graph](research_actual_gauss_collective_canonical_graph.md) | 532 | 8ca0a51e9c2f3c11854e33809a349772d373b3da555286109acdbbc122e6b9bb |
| F | [Earlier centered Fourier recurrence](research_centered_fourier_conway_compiler.md) | 405 | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

Only written mathematics, source reads and text/hash operations were
used. Earlier final notes, public manuscripts and the ledger are unchanged.
