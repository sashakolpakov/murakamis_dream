# A weighted actual Ward lift of the cut centralizer field

Private written proof, 18 November 2026.

Three original coproduct Ward generators span simultaneous infinitesimal
conjugation of the ordered classical meridians on every regular Gauss
chart. Explicit field-dependent coefficients select the centralizer of
the physical cut meridian. The same coefficients have ordered finite
matrix lifts, with an exact cut/pivot boundary and, for a marked word,
an exact internal defect. Neither boundary is discarded.

This identifies a principal geometric field of an actual sourced
current. It does not transport the highest-cut central augmentation
to a noncentral parabolic chart, construct a geometric relative cycle,
or establish a nonzero coefficient in the physical knot period.

## 1. The original finite matrices and source

Fix \(N\ge2\), \(q=e^{\pi i/N}\), \(Q=q^2\), \(h=2\pi i/N\), and
\(M\ne0\). Use the factorial boundary basis of [M] and put
\(x=-M/q\). On \(e_0,\ldots,e_{N-1}\), the actual matrices are
\[
\begin{split}
 K e_a&=xQ^{-a}e_a,\\
 \mathcal E e_a&=(MQ^{-a}-M^{-1})e_{a-1}\quad(a>0),
             &\mathcal E e_0&=0,\\
 F e_a&=(1-Q^{a+1})e_{a+1}\quad(a<N-1),
             &F e_{N-1}&=0.
\end{split}                                                     \tag{1}
\]
The zero arrows in (1) are part of the definition. In particular the
cyclic lower-vacuum arrow \(M-M^{-1}\) is not inserted. The whole
finite intertwining identities and the coproducts are those of [W]:
\[
 K_{12}=K_1K_2,\qquad
 \mathcal E_{12}=\mathcal E_1K_2+\mathcal E_2,\qquad
 F_{12}=F_1+K_1^{-1}F_2.                                      \tag{2}
\]
They iterate in the displayed order on \(b\) heads. Denote the resulting
three matrices by \(\mathsf K,\mathsf E,\mathsf F\). The literal
unmarked checked crossing word \(R_\beta\) commutes with all three.
Scalar crossing and zero-framing factors do not alter these
intertwining equations; they remain in the source.

Keep the original highest projector \(T_0=e_0e_0^*\) and the original
pivot
\[
 g=K^{1-N},\qquad
 g e_a=x^{1-N}Q^{(N-1)a}e_a,\qquad
 P=T_0\otimes g^{\otimes(b-1)}.                              \tag{3}
\]
For any whole marked word \(O\), define its literal functional by
\[
 \Phi_O(B)=\varkappa_\beta(M)\operatorname{Tr}(PBO).            \tag{4}
\]
Here \(\varkappa_\beta(M)\) is the unchanged original scalar
framing/peripheral line. All identities below hold before multiplying
by it. It is never divided out. Formula (4) keeps the actual highest
input and output, including when \(B\) or \(O\) is not an intertwiner.
No replacement of \(T_0\) by \(I/N\) is used.

The exact finite assertions below apply at this root with the whole
meridian \(M\) retained. Their principal-symbol assertions have a
different, explicit scope: the regular interior classical chart of
the actual coefficients in [M], with its specified logarithmic lifts.
In that chart the symbol of \([A,B]/h\) is \(\{a,b\}\). No uniform
symbol expansion at an endpoint row or for an arbitrary growing
finite matrix is asserted.

## 2. The coproduct fields on ordered meridians

Write \(K,e,f\) for the commuting principal symbols of
\(K,\mathcal E,F\). The actual generator relations give
\[
 \{K,e\}=Ke,\qquad \{K,f\}=-Kf,\qquad
                         \{e,f\}=K-K^{-1}.                   \tag{5}
\]
The different heads Poisson commute. Define
\[
 b_-=\begin{pmatrix}1&0\\-Kf&K\end{pmatrix},\qquad
 G=\begin{pmatrix}K&e\\Kf&K^{-1}+ef\end{pmatrix},\qquad
 D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]
\[
 U=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 V=\begin{pmatrix}0&0\\1&0\end{pmatrix}.                       \tag{6}
\]
For the first \(j\) heads set \(B_j=b_{-,j}\cdots b_{-,1}\),
\(B_0=I\), and retain the actual prefix convention
\[
 H_j=B_{j-1}^{-1}G_jB_{j-1},\qquad \mu_j=-H_j.                \tag{7}
\]
These are the ordered meridians of [M], not independently chosen
unprefixed matrices.

Let \((K_*,e_*,f_*)\) be the classical iterates of (2) on all \(b\)
heads. Then, for every \(j\),
\[
\begin{split}
 \{e_*,H_j\}&=[K_*V,H_j],\\
 \{K_*,H_j\}&=[(K_*/2)D,H_j],\\
 \{f_*,H_j\}&=[U-(f_*/2)D,H_j].
\end{split}                                                     \tag{8}
\]
The same identities hold for \(\mu_j\).

Here is a direct coproduct proof. On one head, differentiation of
(6) using (5) gives precisely the three commutators in (8). For two
blocks, write their variables as \((K,e,f)\) and \((L,a,b)\). The
new totals are
\[
             KL,\qquad eL+a,\qquad f+K^{-1}b.                 \tag{9}
\]
On the first block, (8) and the product rule immediately give the
claimed new matrices \(KLV,(KL/2)D,U-(f+K^{-1}b)D/2\).
On the second block its prefixed matrix is \(b_-^{-1}G_2b_-\).
If its unprefixed variation is \([X_2,G_2]\), the prefixed
variation is the commutator with
\[
                       b_-^{-1}X_2b_- -b_-^{-1}\dot b_-.
                                                               \tag{10}
\]
For the generators in the order \(eL+a,KL,f+K^{-1}b\), direct
substitution in (10) gives respectively
\[
 KLV+\frac{eL}{2}I,\qquad
 \frac{KL}{2}D,\qquad
 U-\frac{f+K^{-1}b}{2}D-\frac f2I.                            \tag{11}
\]
For example, in the first case
\(\dot K=-KeL,\ \dot f=L(K-K^{-1})\), and
\(X_2=(eL/2)D+LV\); these determine every term in (10).
In the third case
\(\dot K=Kf,\ \dot f=K^{-1}fb\), and
\(X_2=K^{-1}(U-bD/2)\). The scalar terms in (11) have zero
commutator. This proves the two-block assertion. Repeating it with
the preceding block proves (8) at every width. It also proves the
claim for meridians inside a preceding block, by the first-block
product calculation. No classical covariance theorem is being
substituted for this computation.

The positive and negative crossing maps of [M] preserve both ordered
triangular products, hence the totals in (9), and transport (7) by
their literal Hurwitz rules. Thus (8) is compatible with every
unmarked crossing and its inverse on the common regular chart.

## 3. Selecting the physical cut centralizer

For any traceless matrix of regular functions
\[
                       X=\begin{pmatrix}a&b\\c&-a\end{pmatrix}
\]
put
\[
 \alpha_E=c/K_*,\qquad \alpha_F=b,\qquad
                  \alpha_K=(2a+b f_*)/K_* .                  \tag{12}
\]
Only \(K_*\), already a Gauss unit, is inverted. Equations (8) imply
that the vector field
\[
 \mathscr V_X=\alpha_E\{e_*,\,\cdot\,\}
               +\alpha_F\{f_*,\,\cdot\,\}
               +\alpha_K\{K_*,\,\cdot\,\}                    \tag{13}
\]
satisfies \(\mathscr V_X(H_j)=[X,H_j]\) for every \(j\).
This is a linear combination of vector fields with function
coefficients. It is not asserted to be the Hamiltonian field of
\(\alpha_Ee_*+\alpha_Ff_*+\alpha_KK_*\); the latter would have
additional coefficient derivatives.

Choose the first physical meridian \(\mu=\mu_1=-H_1\), and set
\[
                  X_{\rm cen}=-\left(\mu-\tfrac12
                                      \operatorname{tr}(\mu)I\right).
                                                               \tag{14}
\]
Then \([X_{\rm cen},\mu]=0\). The field (13) fixes the cut
meridian and simultaneously conjugates all the other meridians.
For a noncentral meridian, (14) spans its traceless centralizer:
a vector \(v\) for which \(v,\mu v\) are independent shows that
every commuting matrix is a linear combination of \(I,\mu\).
On an irreducible framed representation chart the resulting field
is nonzero, since a nonscalar matrix commuting with every holonomy
would supply a common invariant line. Word relations and the cut
eigenflag are preserved. No braid-axis product is identified with
the physical cut.

The complete-frame sign is explicit. Use
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\quad
 \mu=F^{-1}\begin{pmatrix}1&1\\0&1\end{pmatrix}F
       =\begin{pmatrix}1+s&-s\\s&1-s\end{pmatrix},\quad s\ne0 .
                                                               \tag{15}
\]
For every fixed reference holonomy \(H^0\), its framed version
is \(F^{-1}H^0F\). Direct multiplication gives
\[
 F^{-1}F_r=J,\qquad J=\begin{pmatrix}1&-1\\1&-1\end{pmatrix},
 \qquad \partial_r(F^{-1}H^0F)=[-J,F^{-1}H^0F].
                                                               \tag{16}
\]
Since \(\mu-I=sJ\), (14) is \(-sJ\). Hence (13) restricts
exactly to \(V_J=s\partial_r\), with the convention of [W].
The sign is fixed by (15)--(16), not by matching a scalar
Hamiltonian on a reduced two-form.

## 4. An ordered finite lift and its complete boundary

Here is one explicit quantization of (12)--(14). On the first head
use the ordered matrix
\[
 \widehat\mu=-\begin{pmatrix}
 K_1&\mathcal E_1\\K_1F_1&K_1^{-1}+\mathcal E_1F_1
 \end{pmatrix}.
\]
Define
\[
 \widehat a=-(\widehat\mu_{11}-\widehat\mu_{22})/2,\quad
 \widehat b=-\widehat\mu_{12},\quad
 \widehat c=-\widehat\mu_{21},
\]
\[
 A_E=\widehat c\,\mathsf K^{-1},\qquad
 A_F=\widehat b,\qquad
 A_K=(2\widehat a+\widehat b\,\mathsf F)\mathsf K^{-1}.
                                                               \tag{17}
\]
The displayed order is part of the definition. This auxiliary
two-by-two matrix need not satisfy a commutative determinant
identity: only its stated principal symbol is used. Every entry
of (17) is a literal finite matrix, without a division by a head
occupation, an \(E\)-arrow, or \(M-M^{-1}\).

For \(X_E=\mathsf E,X_F=\mathsf F,X_K=\mathsf K\) define
\[
 \mathcal D_N(B)=\frac1h\sum_{\iota=E,F,K}
                                      [X_\iota,A_\iota B].
                                                               \tag{18}
\]
For every finite \(B,O\), cyclicity of the ordinary trace proves
the exact sourced identity
\[
\begin{split}
 \Phi_O(\mathcal D_N(B))
 =\frac{\varkappa_\beta}{h}\sum_\iota
 \big\{&
 \operatorname{Tr}([P,X_\iota]A_\iota BO)\\
 &+\operatorname{Tr}(PA_\iota B[O,X_\iota])\big\}.
\end{split}                                                     \tag{19}
\]
Indeed
\(\operatorname{Tr}(P[X,Z]O)=
 \operatorname{Tr}([P,X]ZO)+\operatorname{Tr}(PZ[O,X])\);
apply this with \(Z=A_\iota B\). No intertwining or scalarity
of \(B\), the coefficients \(A_\iota\), or the marked \(O\)
was required.

If \(O=R_\beta\), the second line of (19) vanishes by (2).
For a whole marked word \(O=O_m\cdots O_1\), it is instead
retained by the exact product rule
\[
 [O,X_\iota]=\sum_{\nu=1}^m
 O_m\cdots O_{\nu+1}[O_\nu,X_\iota]O_{\nu-1}\cdots O_1 .
                                                               \tag{20}
\]
Unmarked crossing defects vanish; arbitrary clocks and coupons
need not. This keeps their positions and all noncommutative orders.
It does not assume a coupled word is a quantum-group intertwiner.

The first line of (19) is also concrete. At the root,
\[
 [T_0,\mathcal E]=(MQ^{-1}-M^{-1})E_{01},\quad
 [T_0,F]=-(1-Q)E_{10},\quad [T_0,K]=0,
\]
\[
 g\mathcal E=Q\mathcal E g,\qquad
 gF=Q^{-1}Fg,\qquad [g,K]=0.                                \tag{21}
\]
Expand (2) and apply (21) on each tensor leg to obtain every
term of \([P,X_\iota]\). In particular \([P,\mathsf K]=0\);
the \(E,F\) terms retain both the cut arrows and all tail-pivot
commutators. At \(M=1\) the cut \(E\)-coefficient is
\(Q^{-1}-1\), not zero. Values at completeness therefore do not
justify deleting this boundary or its meridian derivatives.

Finally (18) has the exact quantum product decomposition
\[
 \mathcal D_N(B)=
 \sum_\iota A_\iota\frac{[X_\iota,B]}h+
 \sum_\iota\frac{[X_\iota,A_\iota]}h\,B.                       \tag{22}
\]
On the interior principal chart its symbol is
\[
 \mathscr V_{X_{\rm cen}}(b)
                   +\left(\sum_\iota\{x_\iota,\alpha_\iota\}\right)b,
 \qquad (x_E,x_F,x_K)=(e_*,f_*,K_*).                         \tag{23}
\]
Thus the coefficient-commutator or divergence term is paid explicitly.
One cannot keep only the first summand and still call (19) the
original Ward identity. In local symplectic coordinates (23) is the
divergence of the density \(b\) along (13), since each Hamiltonian
field separately preserves Liouville measure.

## 5. Scope and the remaining source comparison

Equations (8), (12), and (17)--(23) supply an actual weighted Ward
current whose principal bulk field is the physical cut centralizer.
They hold with the original marked word and finite endpoint data.
They do not identify its finite boundary with a particular
geometric relative-chain endpoint, nor show its pairing vanishes.
No finite flow or group-scheme isomorphism is inferred from the
field-dependent linear combination.

The noncentral condition matters. At the literal highest complete
classical augmentation the cut meridian is \(I\), so (14) is zero.
The theorem does not manufacture a noncentral parabolic limit from
that augmentation. On an irreducible framed representation with
noncentral parabolic cut it instead gives the nonzero vector
\(s\partial_r\) of (15). Relating these source situations remains
an additional boundary transport problem.

All finite wall matrices in (1), (3), (19)--(21) precede the
principal comparison and remain whole in \(M\). The interior
symbol argument is not an estimate of those walls, a Gaussian
pushforward of the full current, or a lower bound for the selected
knot coefficient. The original closing, peripheral line, and
highest cut have not been replaced.

## 6. Complete direct sources

| Label | Complete written source | SHA256 |
|---|---|---|
| W | notes/coherent_cut_obstruction_and_ward_relative_class.md | 28141e28d4bc08a8acfa4cef9a8549ed7aadb1344f8796617e68282f7b351e4d |
| M | notes/marked_braid_holonomy.md | eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f |

W supplies the actual finite \(E\), its endpoint and coproduct
intertwining, and the centralizer convention. M supplies the
factorial basis, original pivots, actual interior Gauss symbols,
and ordered meridian/Hurwitz map. Its averaged presentation of
the uninserted scalar is not used to alter (3)--(4). The
coproduct field calculation, coefficient inverse, complete-frame
sign, and ordered sourced trace identity are proved here.

Only written mathematics, source reads, and hash checks were used.
No programs, numerical tests, builds, or frozen/public edits were made.
