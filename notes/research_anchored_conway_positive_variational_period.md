# A compact positive variational formula for Conway knot sources

21 November 2026. Research note; previous finals and public manuscripts
remain unchanged.

A finite Conway construction has an explicit tensor compiler with output
\((1,K_N)\), where \(K_N\) is its original reduced Kashaev invariant.
The constant coordinate is kept orthogonal to the physical boundary
space. It supplies an anchor even when \(K_N=0\), without introducing
ordinary main colors.

This note gives a compact quartic minimization whose value \(Q_N\) satisfies
\[
 1+|K_N|^2\le Q_N\le(1+1/N)(1+|K_N|^2).               \tag{1}
\]
For a fixed expression with \(m\) tensor vertices, the minimization has
\(2N(m-1)\) real variables, and its degree is at most four, independently
of \(m\) and \(N\). The objective is an explicit positive sum of
squared local transport residuals. The theorem is quantitative weighted
Cauchy--Schwarz; its proof does not require the reference-coordinate or
matrix interpretations. Those interpretations give an exact boundary
inner product and four positive local norm factors below. Joint convexity
and a hyperbolic-volume limit are not proved for the quartic problem.

## 1. The original complete boundary packet

Fix \(N\ge2\), and put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=q^{d^2/2},\quad c_j=q^{2j+1}+q^{-2j-1},
\]
\[
 s_0=1,\qquad s_r=\prod_{u=1}^r2\sin(\pi u/N).
\]
All fractional powers mean these displayed exponentials. Use the full
actual pair algebra and its normalized Newton basis
\[
 H_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 b_r=\frac{\prod_{j=0}^{r-1}(c_j-z)}{s_r^2},
 \quad 0\le r\le d.                                    \tag{2}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind. We identify
\(H_N\) with its \(N\)-dimensional coefficient space in (2), with
the Euclidean Hermitian norm. The quotient retains the value and first
derivative at every double root; no normal direction is discarded.

The actual turn and multiplication are
\[
 Jb_r=b_{d-r},\qquad M(f,g)=fg\pmod{2T_N(z/2)+2}.
\]
In coefficient coordinates,
\[
 M(b_i,b_j)=\sum_r\mu_{ijr}b_r,\qquad
 \mu_{ijr}=\frac{s_{i+j}s_r}
 {s_i s_j s_{r-i}s_{r-j}s_{i+j-r}}                       \tag{3}
\]
when \(i+j\le d\) and \(\max(i,j)\le r\le i+j\). All other
coefficients are zero, including products with \(i+j\ge N\).
The physical signed crossing coupons are
\[
 R^{\pm1}=\kappa^{\pm1}\sum_{r=0}^d(-q)^{\pm r}b_r.       \tag{4}
\]
These are the full repeated-root identities of the
[Newton source theorem](actual_newton_turn_positive_gram.md) and
[Conway compiler](research_conway_full_boundary_quotient_gram.md).

Take a fixed literal tangle expression made from these signed crossings,
identity coupons, products and quarter-turns. Its ordered, oriented
closure is assumed to be one knot, with the original reduced marking
and zero-framing convention. Let \(f_E\in H_N\) be its actual open
boundary packet. Write its exact original closing row as \(\ell_N\),
so that
\[
                              K_N=\ell_N f_E.            \tag{5}
\]
For the two normalized Newton closures, this is the appropriate row
\(e_0^{\mathsf T}\) or \(e_d^{\mathsf T}\), with the known framing
and normalization line retained in it. Framing contributes a root
phase. Any recorded fixed power of \(N\) is also kept in \(\ell_N\).
In particular \(\log^+\|\ell_N\|=O(\log N)\) for a fixed diagram,
where \(\log^+x=\max(0,\log x)\).

## 2. An orthogonal constant reference

Give every internal edge the space
\[
                  \widehat H_N=\mathbb C e_\star\oplus H_N,
\]
with its orthogonal direct-sum inner product. The symbol \(e_\star\)
denotes a separate reference coordinate. It is not the physical
algebraic unit \(b_0\): indeed \(Jb_0=b_d\).

Compile the expression using the following actual linear or multilinear
maps:
\[
 \widehat f=(1,f)\quad\hbox{at a leaf},\qquad
 \widehat J(a,u)=(a,Ju),                                \tag{6}
\]
\[
 \widehat M((a,u),(b,v))=(ab,M(u,v)),\qquad
 \widehat\ell_N(a,u)=(a,\ell_Nu)\in\mathbb C^2.           \tag{7}
\]
The mixed reference/physical input sectors of \(\widehat M\) are
zero. Thus induction through the tree gives open packet \((1,f_E)\)
and final output
\[
                      Y_N=(1,K_N),\qquad \|Y_N\|^2=1+|K_N|^2.
                                                               \tag{8}
\]
Every coefficient of these gates is prescribed before the closed
invariant is evaluated. The quantum invariant in the second coordinate
has not been changed.

Let the compiler tree have \(m\ge2\) vertices, including its closing
map. Its root has depth zero. For an edge \(e\), let \(r_e\) be the
depth of its child vertex. Let \(T_{v,N}\) be the coefficient tensor
at vertex \(v\). Its squared Hilbert--Schmidt norm is the sum of the
squared absolute values of all its coefficients. Put
\[
 B_N=\prod_v\|T_{v,N}\|_{\rm HS},\qquad
 t_N=B_N^2\sqrt{3mN/2}.                                 \tag{9}
\]
Each tensor has a reference coefficient equal to one, so \(B_N\ge1\).
Both numbers in (9) are explicit functions of the original local data.

## 3. Boundary translations and the corresponding inner product

For \(w\in H_N\), define
\[
 S(-w)(a,u)=(a,u-aw),\qquad
 D_r(t)(a,u)=(a,t^ru),\qquad
 g_e=D_{r_e}(t_N)S(-w_e).                               \tag{10}
\]
These are invertible for every \(w_e\); the inverse translation is
\(S(w_e)\). In fact \((S(-w)-I)^2=0\). At each edge apply \(g_e\)
to the child output and its inverse to the parent's argument. The
bilinear edge pairing and the output (8) are preserved exactly.

The positive inner product on that edge is particularly simple:
\[
 \boxed{\quad
 \|(a,u)\|_{e,w}^2
       =|a|^2+t_N^{2r_e}\|u-aw_e\|^2.
 \quad}                                                  \tag{11}
\]
Its Gram matrix is
\[
 \begin{pmatrix}
 1+t_N^{2r_e}\|w_e\|^2&-t_N^{2r_e}w_e^*\\
 -t_N^{2r_e}w_e&t_N^{2r_e}I_N
 \end{pmatrix}>0.
\]
The anchored line through \((1,w_e)\) is orthogonal to every physical
variation \((0,h)\). The physical space remains full dimensional.
When \(w_e\) is the true proper boundary packet, this is an exact
orthogonality adapted to that packet, with no normalization by \(K_N\).

## 4. Explicit positive local factors

For \(w\in H_N\), let \(M_w:H_N\to H_N\) be multiplication
by \(w\). Keep \(t=t_N\) in the following formulas. They give
the exact squared Hilbert--Schmidt norms of the gauged tensors.

At a leaf of depth \(r\), with its original packet \(f\) and
outgoing translation \(w\), the factor is
\[
                         1+t^{2r}\|f-w\|^2.             \tag{12}
\]
At a turn vertex of depth \(r\), write \(w_c\) for its child
translation and \(w_p\) for its outgoing translation. The factor is
\[
             1+t^{2r}\|Jw_c-w_p\|^2+t^{-2}\|J\|_{\rm HS}^2.
                                                               \tag{13}
\]
At a multiplication vertex of depth \(r\), the factor is
\[
\begin{split}
 1&+t^{2r}\|M(w_L,w_R)-w_p\|^2\\
  &+t^{-2}\bigl(\|M_{w_L}\|_{\rm HS}^2+
                         \|M_{w_R}\|_{\rm HS}^2\bigr)
       +t^{-2r-4}\|M\|_{\rm HS}^2.                     \tag{14}
\end{split}
\]
Here \(w_L,w_R\) are its two child translations. Finally the original
closing vertex contributes
\[
                    1+|\ell_Nw_c|^2+t^{-2}\|\ell_N\|^2. \tag{15}
\]

To check these identities, the incoming inverse at a child edge of
depth \(r+1\) is \(S(w_c)D_{r+1}(t)^{-1}\). It sends
\((a,u)\) to \((a,aw_c+t^{-r-1}u)\). Substitute this expression
into (6)--(7), then apply the outgoing map in (10). For a product,
the physical output is
\[
 ab\,t^r\{M(w_L,w_R)-w_p\}
 +t^{-1}\{aM(w_L,v)+bM(u,w_R)\}
 +t^{-r-2}M(u,v).
\]
The input sectors reference/reference, reference/physical,
physical/reference and physical/physical are orthogonal. Summing
their squared coefficient norms gives (14), with no discarded cross
term. The other formulas follow from the same substitution.

## 5. A compact quartic minimum

Write \(s=m-1\), the number of proper vertices, or equivalently edges.
Attach a variable \(w_v\in H_N\) to each proper vertex's outgoing
edge. Let \(v_0\) denote the root's unique child. The residual at a
proper vertex is
\[
 \mathcal R_v(\boldsymbol w)=
 \begin{cases}
 f_v-w_v,&v\text{ is a leaf with prescribed packet }f_v,\\
 Jw_c-w_v,&v\text{ is a turn with child }c,\\
 M(w_L,w_R)-w_v,&v\text{ is a product with children }L,R.
 \end{cases}                                             \tag{16}
\]
Every residual is known explicitly from the original operations. Put
\[
 c_v=B_N^{2r_v-1},\qquad
 \mathcal A_N(\boldsymbol w)=\sum_{v\ne\mathrm{root}}
                  c_v^2\|\mathcal R_v(\boldsymbol w)\|^2,
                                                               \tag{17}
\]
\[
 \mathcal J_N(\boldsymbol w)
       =1+|\ell_Nw_{v_0}|^2+Ns\mathcal A_N(\boldsymbol w),
 \qquad
 \boxed{\quad Q_N=(1+1/N)
      \min_{\|w_v\|^2\le B_N^2}\mathcal J_N(\boldsymbol w).\quad}
                                                               \tag{18}
\]
This is a positive real polynomial problem on \(2N(m-1)\) real
variables. Its degree is at most four: a product residual is bilinear
in its two child variables before its squared norm is taken. Its
coefficients and ball radii are algebraic at each level. The nonempty
compact domain makes the minimum exist. The factor \(t_N\) from the
inner-product construction is not used in (16)--(18).

**Theorem.** The quartic minimum (18) satisfies (1) for every \(N\ge2\).

**Proof.** Let \(f_v\) be the true open packet of the proper subtree
rooted at \(v\). Repeated Cauchy--Schwarz in its anchored compiler
gives \(\|(1,f_v)\|\le B_N\); every omitted vertex norm is at
least one. In particular \(\|f_v\|\le B_N\). At every product
vertex present, \(\|M\|_{\rm op}\le B_N\); also
\(\|\ell_N\|\le B_N\) and \(\|J\|_{\rm op}=1\).
These bounds are all that the proof
uses from the compiler. They can instead be checked directly for any
chosen larger bound \(B_N\ge1\).

For every allowed collection \(\boldsymbol w\), define
\(d_v=\|f_v-w_v\|\). At a leaf, \(d_v=\|\mathcal R_v\|\).
At a turn or product,
\[
 d_v\le\|\mathcal R_v\|+B_N^2\sum_{c\text{ child of }v}d_c.
\]
For a product, this follows from the exact bilinear identity
\[
 M(f_L,f_R)-M(w_L,w_R)
       =M(f_L-w_L,f_R)+M(w_L,f_R-w_R)
\]
and the bounds \(\|f_R\|,\|w_L\|\le B_N\). Following the
unique path from each vertex to the root and using \(\|\ell_N\|\le B_N\)
therefore gives
\[
 |K_N-\ell_Nw_{v_0}|
   \le\sum_{v\ne\mathrm{root}}B_N^{2r_v-1}\|\mathcal R_v\|
   \le\sqrt{s\mathcal A_N}.                            \tag{19}
\]
The weighted Cauchy inequality
\((a+b)^2\le(1+1/N)(a^2+Nb^2)\) for nonnegative \(a,b\)
now proves
\(1+|K_N|^2\le(1+1/N)\mathcal J_N(\boldsymbol w)\).
For the reverse bound choose \(w_v=f_v\). This is allowed, every
residual vanishes, and \(\mathcal J_N=1+|K_N|^2\).
This proves (1). No step divides by a closed invariant. \(\square\)

If two such compilers give the same original \(K_N\), then
\[
       |\log Q_N-\log Q_N'|\le\log(1+1/N)\le1/N.        \tag{20}
\]
Both logarithms lie in the same interval of that length. This includes
replacing a fixed proper subtree by its full open boundary packet and
retaining its original normalization. The raw polynomial objectives
need not agree pointwise. A different valid packet bound \(B_N\) also
changes the logarithmic minimum by at most the same amount.

## 6. The product of local norm factors

The four factors (12)--(15) give a second, less economical minimum.
Let \(\Phi_N(\boldsymbol w)\) be their product and define
\[
 P_N=\min_{\|w_e\|^2\le B_N^2}\Phi_N(\boldsymbol w).
\]
It has the same number of variables as (18), but degree at most \(4m\).
It satisfies the exact bounds
\[
             1+|K_N|^2\le P_N\le e^{2/N}(1+|K_N|^2).   \tag{21}
\]
For the lower bound, gauges preserve the original output \(Y_N\),
and leaf-by-leaf Cauchy--Schwarz bounds its squared norm by \(\Phi_N\).
For the upper bound, use \(w_e=f_e\). All transport residuals vanish.
Every original local norm is at most \(B_N\), and
\(\|M_{f_e}\|_{\rm HS}\le\|M\|_{\rm HS}\|f_e\|\le B_N^2\).
A leaf factor is one, a turn factor is at most \(1+B_N^2/t_N^2\),
and a product factor is at most \(1+3B_N^4/t_N^2\), because
\(r\ge1\) and \(t_N\ge1\). The root factor is at most
\(\|Y_N\|^2(1+B_N^2/t_N^2)\). Consequently
\[
 \Phi_N((f_e)_e)\le\|Y_N\|^2
       \exp(3mB_N^4/t_N^2)=e^{2/N}\|Y_N\|^2.
\]
Two exact presentations therefore have
\(|\log P_N-\log P_N'|\le2/N\).

The product lower bound has a polynomial sum-of-squares certificate.
For a leaf vector \(a\) and neighboring tensor \(T_{iI}\),
\[
 \|a\|^2\|T\|_{\rm HS}^2-\|a^{\mathsf T}T\|^2
   =\sum_{I,\,i<j}|\overline a_iT_{jI}
                         -\overline a_jT_{iI}|^2.       \tag{22}
\]
Apply (22) successively and multiply each defect by the squared norms
of the other vertices, themselves sums of squares. Telescoping gives
a real polynomial sum-of-squares expression for
\(\Phi_N(\boldsymbol w)-1-|K_N|^2\). The entries are polynomials
in \(w_e,\overline w_e\) with \(t_N\) fixed. This certifies the
finite lower inequality (21); it supplies no geometric lower bound.

## 7. Growth of the source constants

The elementary identities \(s_d=N\) and \(s_as_{d-a}=N\) imply
\(N2^{-d}\le s_a\le2^d\). Formula (3) consequently gives the coarse
bound \(\mu_{ijr}\le2^{7d}\), and hence
\(\|M\|_{\rm HS}\le N^{3/2}2^{7d}\). The crossing leaves in (4)
have norm \(\sqrt N\); the turn is unitary. Together with the
known closing row this proves, for each fixed literal construction,
\[
                         \log B_N=O(N),\qquad\log t_N=O(N). \tag{23}
\]
Fixed signed powers can first be expanded into signed crossing leaves.
The constants may depend on those fixed powers and on the construction.

## 8. The remaining geometric statement

For any \(V>0\), (1) gives
\[
 \lim_{N\to\infty}\frac\pi N\log Q_N=V
 \quad\Longleftrightarrow\quad
 \lim_{N\to\infty}\frac{2\pi}N\log|K_N|=V.              \tag{24}
\]
Indeed \(\log(1+|K_N|^2)\) differs from
\(\max(0,2\log|K_N|)\) by at most \(\log2\), including zeros
with \(\log0=-\infty\). A strictly positive limiting rate removes
that maximum and implies eventual nonvanishing.

This construction uses the complete physical packet and an orthogonal
constant reference. It requires no estimate for ordinary colors, and
no identification of an auxiliary-circle Fourier norm with a main-color
norm. All physical normal directions and the original closing row remain.
The translations form the additive group of \(H_N\), since
\(S(u)S(v)=S(u+v)\); their square-zero off-diagonal block supplies
the elementary boundary centering used in the proof.

To prove the proposed volume theorem one must still compare the leading
value of this actual positive polynomial problem with hyperbolic volume.
For the finite-exception program, that comparison is needed after every
required fixed short partial assignment and sufficiently long remaining
fillings which give hyperbolic knots. Fixed short subtrees can be
contracted exactly before applying the construction. No geometric
comparison, regulator identification, or new volume-equality class
is inferred from (24) alone.

## Complete direct sources

The complete matching texts were read. The first two give the actual
physical operations and source conventions; the third records the earlier
full-matrix filtering construction for comparison. The quartic theorem,
orthogonal reference, division-free translations and explicit polynomial
factors are proved above; the full-matrix argument is not a prerequisite.

* [Complete Conway compiler](research_conway_full_boundary_quotient_gram.md):
  `debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077`.
* [Actual Newton turn, crossing and source](actual_newton_turn_positive_gram.md):
  `d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3`.
* [Earlier quantitative metric bound](research_regularized_source_metric_compactness.md):
  `fd8dae7561eff37089e8481b4eb8c8344acb56da86b502350292f6d2be9c8818`.

Only written mathematics and text operations were used. No mathematical
program, test, build, git operation or public-document edit was performed.
