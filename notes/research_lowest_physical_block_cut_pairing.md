# The lowest physical block and the original cut pairing

Private written proof, 19 November 2026. Author-final for independent review.

The operator dual to physical highest-block multiplication has a
literal endpoint interpretation: it takes an intertwiner to its
lowest diagonal block. This endpoint is another regular coordinate
on the whole intertwiner space. The original cut pairing is therefore
perfect in these coordinates, including at the complete meridian.

The abstract perfect cut form is existing coverage in
integral_projective_cut_duality.md. That result is not a premise
below. The present proof identifies the finite duality operator and
proves its invertibility directly, without projective-module or
fusion arguments. Its sole complete direct is H, the physical
highest-block reconstruction, pinned below.

This is a bilinear statement. It supplies neither a positive inner
product nor a lower bound for the closing of a specified knot word.

## 1. The two physical endpoints

Use H's actual fixed-root family. Thus
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad M=e^\mu,\quad x=-M/q,
 \qquad f_a=\prod_{j=1}^a(1-Q^j).
 \tag{1}
\]
There are \(m=r+1\) heads. The remaining tensor is \(U\), with
ordered total operators \(E,F,K\). The first head has
\[
 E_1w_a=e_aw_{a-1},\quad e_a=MQ^{-a}-M^{-1}\ (1\le a\le d),
 \qquad F_1w_a=(1-Q^{a+1})w_{a+1},
 \quad K_1w_a=xQ^{-a}w_a,
 \tag{2}
\]
and the actual zero outward arrows. The total generators are
\[
 E_\Sigma=E_1K+E,\qquad
 F_\Sigma=F_1+K_1^{-1}F,\qquad K_\Sigma=K_1K.
 \tag{3}
\]
Put
\[
 \mathcal A=\{H\in\operatorname{End}(U):[K,H]=0\},
 \qquad g=K^{1-N},\qquad \tau_0(H)=\operatorname{Tr}_U(gH).
 \tag{4}
\]
H proves that, whenever \(e_1\cdots e_d\ne0\), each
\(H\in\mathcal A\) extends uniquely to an actual total
intertwiner \(W_H\) with \((W_H)_{00}=H\). This includes
\(M=1\) and every strict collar \(|\mu|<\eta/N\), \(\eta<\pi\).
All spaces can alternatively be restricted to exact integer-degree
preservation. The root-weight condition is not substituted for that
restriction.

Write
\[
 C_a(H)=(W_H)_{a0},\qquad U_a(H)=(W_H)_{0a}.
\]
The exact endpoint recurrences in H are
\[
 C_0(H)=H,\qquad
 C_{a+1}(H)=-e_{a+1}^{-1}K^{-1}[E,C_a(H)],
 \tag{5}
\]
\[
 U_a(H)=\frac{x^{-a}}{f_a}\mathcal D_aH,\qquad
 \mathcal D_a=\prod_{j=0}^{a-1}(L_F-Q^jR_F).
 \tag{6}
\]
Here \(L_FT=FT\), \(R_FT=TF\); these two operators commute.
Empty products are identities. The transported product is
\[
 H\star J=\sum_{a=0}^d U_a(H)C_a(J),\qquad
 W_{H\star J}=W_HW_J.
 \tag{7}
\]
The actual pointed source of \(W_H\) is \(\tau_0(H)\).
Scalars included in a word remain in \(H\); a separately prescribed
scalar line remains separately prescribed.

## 2. The explicit duality operator

Define a finite linear operator on \(\mathcal A\) by
\[
 \mathscr L J=
 \sum_{a=0}^d\frac{x^{-a}}{f_a}
 \prod_{j=0}^{a-1}(Q^{-1}R_F-Q^jL_F)\,C_a(J).
 \tag{8}
\]
The factors act on the displayed \(C_a(J)\). Each summand has
total root weight zero. The formula also preserves exact integer
degree zero when that restriction is imposed.

The weighted ordinary trace gives the exact identity
\[
 \boxed{\qquad
 \tau_0(H\star J)=\operatorname{Tr}_U(gH\mathscr L J).
 \qquad}\tag{9}
\]
Indeed \(gF=Q^{-1}Fg\). Moving one left or right multiplication
under the ordinary finite trace shows
\[
 \operatorname{Tr}(g(FH)T)
       =\operatorname{Tr}(gH(Q^{-1}TF)),\qquad
 \operatorname{Tr}(g(HF)T)=\operatorname{Tr}(gH(FT)).
 \tag{10}
\]
Thus the bilinear adjoint of \(L_F-Q^jR_F\) is
\(Q^{-1}R_F-Q^jL_F\). Their factors commute, so applying
(10) to every factor of (6), and then (7), proves (9).
No complex conjugation has been taken.

## 3. The duality operator is the lowest block

In fact
\[
 \boxed{\qquad \mathscr L J=(W_J)_{dd}.\qquad}\tag{11}
\]
We verify this with the actual finite prefix operator, so all caps
and root phases are visible. Put
\[
 c_j=(-1)^jQ^{j(j-1)/2},\qquad
 S=\sum_{j=0}^d\frac{x^{-j}L_1^jF^j}{f_j},\qquad
 S^{-1}=\sum_{j=0}^d\frac{c_jx^{-j}L_1^jF^j}{f_j}.
 \tag{12}
\]
H gives \(F_\Sigma=SF_1S^{-1}\), \(p_dS=p_d\), and
\[
 W_J=T_JS^{-1},\qquad
 T_Ji_b=f_b^{-1}F_\Sigma^b\sum_{a=0}^di_aC_a(J).
 \tag{13}
\]
For \(a\ge j\), expansion of
\(p_dF_\Sigma^{d-j}i_a=p_dF_1^{d-j}S^{-1}i_a\)
has precisely one surviving term, namely
\[
 p_dF_\Sigma^{d-j}i_a
 =\frac{c_{a-j}x^{-(a-j)}}{f_{a-j}}
                         \frac{f_d}{f_j}F^{a-j}.
 \tag{14}
\]
For \(a<j\) it is zero. Substituting (12)--(14) in
\(p_dW_Ji_d\) therefore gives
\[
 (W_J)_{dd}=
 \sum_{a=0}^d x^{-a}\sum_{j=0}^a
 \frac{c_jc_{a-j}f_d}{f_j^2f_{d-j}f_{a-j}}
                         F^{a-j}C_a(J)F^j.
 \tag{15}
\]
The elementary root product identities are
\[
 f_d=N,\qquad
 f_{d-j}=\frac{f_d(-1)^jQ^{j(j+1)/2}}{f_j}.
 \tag{16}
\]
The first follows from \((t^N-1)/(t-1)\) at \(t=1\).
For the second, separate the last \(j\) factors and use
\(1-Q^{-k}=-Q^{-k}(1-Q^k)\). In particular
\(c_jf_d/f_{d-j}=Q^{-j}f_j\).
Thus (15) becomes
\[
 \sum_{a=0}^d x^{-a}\sum_{j=0}^a
       \frac{Q^{-j}c_{a-j}}{f_jf_{a-j}}
                           F^{a-j}C_a(J)F^j.
 \tag{17}
\]
The ordinary commuting-variable quantum binomial expansion of
\(\prod_{k=0}^{a-1}(Q^{-1}R_F-Q^kL_F)/f_a\)
has exactly the coefficients in the inner sum of (17).
This proves (11) for the whole fixed-root meridian family.

## 4. Invertibility from the opposite endpoint

The lowest-block map is injective on the total intertwiner space.
To see this, let \(W_{dd}=0\). The physical raising equation gives
\[
 (1-Q^a)W_{a-1,d}
   =x^{-1}\bigl(Q^dW_{ad}F-Q^aFW_{ad}\bigr),
                      \qquad a=d,d-1,\ldots,1.
 \tag{18}
\]
All displayed denominators are nonzero, so the entire last column
vanishes. The maps
\[
 E_\Sigma^bi_d:U\longrightarrow V_1\otimes U,
                              \qquad 0\le b\le d,
 \tag{19}
\]
jointly form an invertible triangular coordinate system: their
lowest first-head row is \(d-b\), with coefficient
\((e_d\cdots e_{d-b+1})K^b\), an invertible operator.
Commutation with \(E_\Sigma\) and the vanishing last column now
give \(WE_\Sigma^bi_d=0\) for every \(b\); hence \(W=0\).

The highest-block map already identifies the whole intertwiner
space with \(\mathcal A\). The lowest-block map has the same
target and is injective, so it is an isomorphism. Its matrices
depend holomorphically on \(M\). Since its determinant is nonzero
wherever \(e_1\cdots e_d\ne0\), its inverse is holomorphic on
that same domain. The degree-zero argument is identical using
H's exact integer-degree restriction.

Together with (11), this proves that \(\mathscr L\) is an actual
holomorphic linear automorphism at \(M=1\), not just an invertible
principal symbol.

Both directions have controlled finite-cap conditioning. Here is an
explicit inverse construction, also proving the bound. Given
\(J=W_{dd}\), solve (18) downward with \(D_d=J\), and set
\(V_J=\sum i_aD_a\), \(F_{\rm top}=x^{-1}Q^dF\).
The only possible residual of the raising equation is
\(F_\Sigma V_J-V_JF_{\rm top}=i_0R\).
Telescope its \(N\)-th powers, which vanish by H, and apply \(p_d\).
Only the term with \(d\) first-head raisings survives, giving
\(f_dR=0\). Thus the terminal row holds as well.

Put
\[
 h_b=e_d e_{d-1}\cdots e_{d-b+1},\quad h_0=1,
 \qquad A=EK^{-1},
 \qquad S_Ei_{d-b}=h_b^{-1}E_\Sigma^bi_dK^{-b}.
 \tag{19a}
\]
In reversed first-head indices its only nonzero blocks are
\[
 (S_E)_{b-j,b}=\frac{h_{b-j}}{h_b}{b\brack j}_Q
                          Q^{j(j-1)/2}A^j,\qquad 0\le j\le b.
 \tag{19b}
\]
Indeed the summands \(E_1K\) and \(E\) of \(E_\Sigma\)
\(Q\)-commute. Expand their \(b\)-th power with the tail \(E\)'s
to the left and use \(E^jK^{-j}=Q^{j(j-1)/2}A^j\).
The exact inverse is
\[
 (S_E^{-1})_{b-j,b}=\frac{h_{b-j}}{h_b}(-1)^j
                                      {b\brack j}_QA^j.
 \tag{19c}
\]
Multiplying the two finite triangular matrices reduces a block at
distance \(n>0\) to a nonzero common factor times
\(\sum_{j=0}^n(-1)^jQ^{j(j-1)/2}{n\brack j}_Q=(1;Q)_n=0\).
At distance zero the product is the identity. No denominator
\(1-Q^N\) occurs.

Each \(D_a\) has weight \(KD_a=Q^{a-d}D_aK\), by (18).
Define
\[
 T_Ei_{d-b}=h_b^{-1}E_\Sigma^bV_JK^{-b},\qquad
                              W=T_ES_E^{-1}.
 \tag{19d}
\]
This agrees with extension along the basis (19): it commutes with
\(E_\Sigma\), including its top row by \(E_\Sigma^N=0\), and
with \(K_\Sigma\). The already verified column equation makes
\([F_\Sigma,W]i_d=0\). Jacobi and Cartan commutation make that
commutator commute with \(E_\Sigma\); (19) therefore makes it zero
everywhere. Thus (19d) is the inverse endpoint reconstruction.

Fix \(|\mu|\le\eta/N\), \(\eta<\pi\), at fixed width. H's
prefix-product bounds also bound every reversed product \(h_b\)
and its reciprocal by \(e^{CN}\): each is a ratio of two complete
or prefix products. Downward recursion (18) costs at most a fixed
constant per step divided by a reversed prefix of \(f_d\), hence
\(\|V_J\|\le e^{CN}\|J\|\). In (19b)--(19c) use
\(|{b\brack j}_Q|\le\binom bj\), bounded \(\|A\|\), and those
product bounds. They give \(\|S_E^{\pm1}\|\le e^{CN}\).
Equation (19d) then gives \(\|W\|\le e^{CN}\|J\|\).
Together with H's forward bound this proves
\[
                   \|\mathscr L\|+\|\mathscr L^{-1}\|
                                      \le e^{CN}.
 \tag{19e}
\]
Constants can be enlarged to absorb all polynomial factors in
\(N\). True fixed-root meridian derivatives of either map cost at
most \(C_jN^je^{CN}\) on smaller scaled collars, by Cauchy's
formula. These are exponential bounds, not zero-exponential-rate
estimates or positivity statements.

## 5. The original cut is a perfect bilinear pairing

The ordinary form
\[
               (H,T)\longmapsto\operatorname{Tr}(gHT)
 \tag{20}
\]
is perfect on \(\mathcal A\). Indeed the actual Cartan is diagonal,
so its commutant is a direct sum of full matrix algebras on its
weight spaces. On each, \(g\) is a nonzero scalar. The ordinary
matrix trace pairing on each block is perfect. The same reasoning
works for the finer blocks of exact total occupation degree.

Equations (9) and (11), and invertibility of the lowest-block map,
therefore prove that
\[
                       B(H,J)=\tau_0(H\star J)
 \tag{21}
\]
is perfect. It remains perfect over the holomorphic meridian germ
and after specialization to \(M=1\). It is associative in the
Frobenius sense, since associativity of \(\star\) gives
\(B(H\star J,T)=B(H,J\star T)\).
No separate symmetry theorem is needed for these conclusions.

The conclusion is concrete: cut duality is realized by the opposite
physical endpoint, with the original pivot and every finite
coefficient retained. Nondegeneracy says a nonzero element has
some nonzero pairing. It does not say that its prescribed pairing
with the identity is nonzero. In particular it supplies no positive
norm, no subexponential conditioning statement, and no surviving
geometric contour coefficient for an actual knot word.

## Complete proof-source pin

* H: notes/research_physical_highest_block_endpoint_coordinates.md,
  453 lines, SHA256
  deaadaa899cdb08aefbbcb1e1ca87a40f84a1ade608fceeeaba6426027bd9b1b.

The complete matching direct was freshly read nontruncated in the
active author sequence and retained unchanged. The matching final
was read back in full, every used implication checked, and both
pins renewed before freezing. Only written mathematics and text/hash
operations were used. Frozen and public files were unchanged.
