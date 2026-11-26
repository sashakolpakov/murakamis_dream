# The original pivotal source in the canonical coproduct Gram

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

The complete cyclic-source coproduct has an explicit spectral graph
frame. In that frame the original marked pivotal source is a specified
resolvent of the remaining coproduct, followed by its original pivot.
Its inherited graph Gram makes this density polynomially bounded,
together with its inverse. Consequently the unchanged original
co-source has polynomial dual norm in the sharp canonical coproduct
Gram of [C]. No comparison between two unestimated metrics is used.

The density is generally complex and has trace zero when there is a
tail. These are source and norm identities, not positivity of the
original scalar trace or a geometric noncancellation theorem.

## 1. Actual transported words and fixed root data

Fix \(b\ge1\), independently of \(N\ge2\), and put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \gamma=(-1)^{N+1},\quad x=-q^{-1},\qquad
 \alpha_a=Q^{-a}-1,\quad A_a=\prod_{h=1}^a\alpha_h,\quad A_0=1.
 \tag{1}
\]
The original physical head basis \(w_0,\ldots,w_d\) is orthonormal.
Use [B]'s regular E-semicyclic complete-color chart and its fixed line:
\[
 E_iw_a=\alpha_aw_{a-1}\ (a>0),\quad E_iw_0=\mu_iw_d,\quad
 K_iw_a=xQ^{-a}w_a,\qquad
 |\mu|=1/N,\quad \mu_i=\gamma^{1-i}\mu .
 \tag{2}
\]
The actual coproduct, in the convention of [M], is
\[
 E_\Sigma=\sum_{i=1}^b E_iK_{i+1}\cdots K_b,\qquad
 K_\Sigma=\prod_{i=1}^bK_i,\qquad
 E_\Sigma^N=bcI,\quad c=\gamma^bN\mu,\quad |c|=1.
 \tag{3}
\]
The last identity is proved in [C] by the root quantum multinomial;
it includes even and composite levels and every cyclic wrap.

An actual braid word below means the genuinely transported operator
\(W_\mu\) in [B], with every crossing's finite \(\mu\)-dependence
and original common Cartan scalar retained. On the fixed line it
commutes with \(E_\Sigma,K_\Sigma\). It is not the unchanged
nilpotent-head matrix \(W_0\), which need not commute with (2).
[B, Section 5] identifies the completed one-cut operator of
\(W_\mu\) with the original one. Its pivot, framing, whole meridian
line and assigned external dimension factors remain unchanged.

Write the physical space as \(\mathcal V=\mathcal V_1\otimes\mathcal V_{\rm t}\).
On the tail put
\[
 B=E_{\rm t}=\sum_{i=2}^bE_iK_{i+1}\cdots K_b,\quad
 K_{\rm t}=\prod_{i=2}^bK_i,\quad g_{\rm t}=K_{\rm t}^{\,1-N}.
 \tag{4}
\]
Thus \(E_\Sigma=E_1K_{\rm t}+B\),
\(B^N=(b-1)cI\), and \(K_{\rm t}B=QB K_{\rm t}\).
For \(b=1\), the tail is \(\mathbb C\), with \(B=0\) and
\(K_{\rm t}=g_{\rm t}=I\). In the physical metric,
\[
 K_{\rm t}^N=\gamma^{b-1}I,\qquad
 g_{\rm t}=\gamma^{b-1}K_{\rm t},\qquad
 g_{\rm t}Bg_{\rm t}^{-1}=QB .
 \tag{5}
\]
Both \(K_{\rm t}\) and \(g_{\rm t}\) are unitary.
The original marked pivotal functional from [R] is exactly
\[
 D_{\rm cut}=P_0\otimes g_{\rm t},\quad
 P_0=|w_0\rangle\langle w_0|,\qquad
 t_b(W_\mu)=\operatorname{Tr}_{\mathcal V}(D_{\rm cut}W_\mu).
 \tag{6}
\]
Any existing exterior scalar multiplies (6) as before. Nothing here
changes an invariant or asserts an identity for arbitrary inserted
exteriors that fail the stated intertwining conditions.

## 2. The source density and its quantitative statement

Choose \(e^N=bc\), set \(T=E_\Sigma/e\), and let
\(\lambda=eQ^j\), \(0\le j<N\). Define
\[
 \Pi_\lambda=\frac1N\sum_{k=0}^d\lambda^{-k}E_\Sigma^k,\quad
 Z=B/\lambda,\quad
 \mathcal P_a(Z)=(Z;Q)_a=\prod_{h=0}^{a-1}(I-Q^hZ).
 \tag{7}
\]
These are the actual spectral projectors and finite polynomials.
Since \(Z^N=(b-1)I/b\), one has
\(\mathcal P_N(Z)=I/b\), and \(I-Z\) is invertible.

Let \(\pi_0:\mathcal V\to\mathcal V_{\rm t}\) extract first color zero,
and \(\iota_0f=w_0\otimes f\). Define the specified graph map by
\[
 L_\lambda f=\sum_{a=0}^d w_a\otimes L_{\lambda,a}f,\qquad
 L_{\lambda,a}=\frac{\lambda^a}{A_a}
                       K_{\rm t}^{-a}\mathcal P_a(Z).
 \tag{8}
\]
Its inherited physical Gram is explicitly
\[
 G_\lambda=L_\lambda^*L_\lambda
     =\sum_{a=0}^d w_a^{(\lambda)}\mathcal P_a(Z)^*\mathcal P_a(Z),
 \qquad
 w_a^{(\lambda)}=\frac{|\lambda|^{2a}}{s_a^2},\quad
 s_a=|A_a|=\prod_{h=1}^a2\sin(\pi h/N).
 \tag{9}
\]
Here \(s_0=1\), and the scalar weights \(w_a^{(\lambda)}\) are distinct
from the physical vectors \(w_a\). Stars in (8)--(9) use the
specified physical metrics. In particular \(G_\lambda\succeq I\).
For an endomorphism \(F\) of the tail, write \(\|F\|_{G_\lambda}\)
for its operator norm in this Gram.

**Theorem.** The map \(L_\lambda\) is a bijection from the complete
tail onto \(\ker(E_\Sigma-\lambda)\), with inverse \(\pi_0\).
For \(W_\lambda=\pi_0W_\mu L_\lambda\), the original source is
\[
 t_b(W_\mu)=\operatorname{Tr}_{\mathcal V_{\rm t}}
                      (R_\lambda W_\lambda),\qquad
 R_\lambda=\sum_{k=0}^d\lambda^{-k}B^k g_{\rm t}
          =\frac1b(I-Z)^{-1}g_{\rm t}.
 \tag{10}
\]
Put \(\rho_{b,N}=b^{-1+1/N}\). The inherited, rather than a freely
substituted, graph Gram satisfies the two-sided inequality
\[
 \boxed{\quad
 \frac{\rho_{b,N}^2}{4}G_\lambda
       \preceq R_\lambda^*G_\lambda R_\lambda
       \preceq N^2\rho_{b,N}^2G_\lambda .
 \quad}                                                     \tag{11}
\]
Thus \(\|R_\lambda\|_{G_\lambda}\le N\rho_{b,N}\) and
\(\|R_\lambda^{-1}\|_{G_\lambda}\le2/\rho_{b,N}\).

For the canonical Gram of [C] and the actual invariant source set
\[
 J_{\rm av}=\sum_{k=0}^d(T^k)^*T^k,\qquad
 D_{\rm inv}=\frac1N\sum_{k=0}^d T^kD_{\rm cut}T^{-k}.
 \tag{12}
\]
The subscript inv means invariant, not inverse. Then
\[
 \boxed{\quad
 \|D_{\rm inv}\|_{J_{\rm av}}\le\rho_{b,N},\qquad
 \|D_{\rm inv}^{-1}\|_{J_{\rm av}}\le2N/\rho_{b,N}.
 \quad}                                                     \tag{13}
\]
Its operator condition number is at most \(2N\), independently of
\(b\). This is the condition of the source operator, not the
condition number of \(J_{\rm av}\) relative to the physical metric.
With the unnormalized Hilbert--Schmidt norm in \(J_{\rm av}\),
\[
 \boxed{\quad
 |t_b(W_\mu)|\le
       \rho_{b,N}N^{b/2}\|W_\mu\|_{{\rm HS},J_{\rm av}}.
 \quad}                                                     \tag{14}
\]
All finite identities and inequalities hold at every \(N\ge2\).
More generally their linear-algebraic statements apply to matrices
commuting with both \(E_\Sigma,K_\Sigma\); the identification with
the original knot source uses the actual transported word above.

## 3. The complete eigenspace is the specified graph

For \(v=\sum_a w_a\otimes v_a\), its eigenvalue equation gives
\[
 \alpha_{a+1}K_{\rm t}v_{a+1}=(\lambda-B)v_a
       \quad(0\le a<d),\qquad
 \mu K_{\rm t}v_0=(\lambda-B)v_d.
 \tag{15}
\]
The first recurrence and \(BK_{\rm t}^{-1}=QK_{\rm t}^{-1}B\)
give (8), starting from the arbitrary vector \(v_0=f\).
The final equation also holds, including its wrap. Indeed
\[
 (\lambda-B)L_{\lambda,d}
 =\frac{K_{\rm t}^{-d}}{A_d}
       \prod_{h=0}^d(\lambda-Q^hB)
 =\frac{cK_{\rm t}^{-d}}{\gamma N}
 =\mu K_{\rm t}.
 \tag{16}
\]
Here \(A_d=\gamma N\), \(K_{\rm t}^{-d}=\gamma^{b-1}K_{\rm t}\),
and \(\lambda^N-B^N=cI\). This proves the last equality with
its exact sign, at both parities. Conversely (15) determines
every component from \(v_0\), proving the bijection and its inverse.

The map retains all \(N^{b-1}\) tail coordinates. It does not
specialize a total or intermediate Casimir to its nodal values.
Their full matrices, including any Jordan channels, remain in
the induced word \(W_\lambda\).

## 4. Compressing the original marked pivotal source

For \(0\le k<N\), the quantum multinomial for \(E_\Sigma^k\)
has the exact zeroth-head block
\[
                  \pi_0E_\Sigma^k\iota_0=B^k.
 \tag{17}
\]
An allocation using the first-head lowering operator \(u\) times
can return first color zero only if \(u\equiv0\pmod N\).
Its range \(0\le u\le k<N\) forces \(u=0\). Thus the pure tail
term, with coefficient one, is the only surviving allocation.
This argument includes every permitted cyclic wrap.

Since \(D_{\rm cut}L_\lambda=\iota_0g_{\rm t}\), the compressed
source on this eigenspace, in the graph coordinates, is exactly
\[
 \pi_0\Pi_\lambda D_{\rm cut}L_\lambda
       =\frac1N\sum_{k=0}^d\lambda^{-k}B^kg_{\rm t}
       =R_\lambda/N.
 \tag{18}
\]
The finite geometric sum uses
\((I-Z)\sum_{k=0}^dZ^k=I-Z^N=I/b\), proving the resolvent in (10).
It also fixes its forcing:
\((I-Z)R_\lambda=g_{\rm t}/b\).
No homogeneous solution or unknown knot value is chosen.

The matrices \(W_\mu,D_{\rm cut}\) commute with \(K_\Sigma\).
Conjugation by \(K_\Sigma\) cycles the spectral projectors,
\(K_\Sigma\Pi_\lambda K_\Sigma^{-1}=\Pi_{\lambda/Q}\).
Therefore all \(N\) sector traces
\(\operatorname{Tr}(D_{\rm cut}W_\mu\Pi_\lambda)\) are equal.
Summing them and using (18) proves (10), including its factor \(N\).
The induced word is the entire restriction, not an intermediate
projection: \(W_\mu L_\lambda=L_\lambda W_\lambda\).

## 5. Exact Gram compensation by a shifted finite Pochhammer

The inherited Gram (9) follows directly from (8), since
\(K_{\rm t}\) is physically unitary and \(|A_a|=s_a\).
The relation \(g_{\rm t}Zg_{\rm t}^{-1}=QZ\) and
\(\mathcal P_N(Z)=I/b\) give the exact ordered identities
\[
 R_\lambda=g_{\rm t}\mathcal P_d(Z),\qquad
 \mathcal P_a(Z)R_\lambda
          =b^{-1}g_{\rm t}\mathcal P_{a-1}(Z)\quad(1\le a\le d).
 \tag{19}
\]
For the first, use
\((I-Z)^{-1}=b\mathcal P_d(QZ)\).
For the second, cancel the first factor of \(\mathcal P_a(Z)\)
against \(I-Z\), then move \(g_{\rm t}\) to the left. This order
retains the original pivot and is essential.

Taking squared norms in (19), with \(g_{\rm t}^*g_{\rm t}=I\), gives
\[
 R_\lambda^*G_\lambda R_\lambda
 =b^{-2}\sum_{a=1}^d w_a^{(\lambda)}
               \mathcal P_{a-1}(Z)^*\mathcal P_{a-1}(Z)
                    +\mathcal P_d(Z)^*\mathcal P_d(Z).
 \tag{20}
\]
The zeroth term of (9) has weight one; it becomes the last term
displayed here. Thus no endpoint term has been dropped.

Compare the coefficient of each positive summand in (20) with (9).
For \(0\le a<d\) the ratio is
\[
 \frac{w_{a+1}^{(\lambda)}}{b^2w_a^{(\lambda)}}
       =\frac{\rho_{b,N}^2}{|1-Q^{a+1}|^2},
 \qquad
 \frac1{w_d^{(\lambda)}}=N^2\rho_{b,N}^2.
 \tag{21}
\]
The last identity uses \(s_d=N\) and \(|\lambda|=b^{1/N}\).
The elementary bounds \(4/N\le|1-Q^\ell|\le2\), \(0<\ell<N\),
place every ratio between \(\rho_{b,N}^2/4\) and
\(N^2\rho_{b,N}^2\). For the lower sine bound, reflect \(\ell\)
to \(\min(\ell,N-\ell)\) and use concavity
\(\sin v\ge2v/\pi\) on \([0,\pi/2]\).
Positivity of all summands proves (11).
Invertibility follows already from (10); (11) then proves both
operator norm bounds without a comparison to the tail's flat metric.

## 6. The unchanged whole source in the sharp canonical Gram

By [C], the spectral sectors are orthogonal for \(J_{\rm av}\), and
\[
 J_{\rm av}=N\sum_\lambda\Pi_\lambda^*\Pi_\lambda,\qquad
 L_\lambda^*J_{\rm av}L_\lambda=NG_\lambda.
 \tag{22}
\]
The second identity uses
\(\Pi_{\lambda'}L_\lambda=\delta_{\lambda',\lambda}L_\lambda\).
Thus the graph metric used above is precisely the restriction of
the known canonical Gram, up to its stated scalar \(N\).

Finite cyclic averaging gives
\(D_{\rm inv}=\sum_\lambda\Pi_\lambda D_{\rm cut}\Pi_\lambda\).
Its block in each graph frame is \(R_\lambda/N\), by (18).
Taking the maximum of the block norms in the orthogonal sum (22)
proves (13) and the condition-number bound.
If \(W_\mu\) commutes with \(T\), cyclicity of the ordinary trace gives
\[
 \operatorname{Tr}(D_{\rm cut}W_\mu)
                 =\operatorname{Tr}(D_{\rm inv}W_\mu).
 \tag{23}
\]
In a \(J_{\rm av}\)-orthonormal basis the ordinary matrix trace
is unchanged. Its Hilbert--Schmidt Cauchy inequality and
\(\dim\mathcal V=N^b\) give
\[
 |\operatorname{Tr}(D_{\rm inv}W_\mu)|
 \le\|D_{\rm inv}\|_{{\rm HS},J_{\rm av}}
                         \|W_\mu\|_{{\rm HS},J_{\rm av}}
 \le\rho_{b,N}N^{b/2}\|W_\mu\|_{{\rm HS},J_{\rm av}},
 \tag{24}
\]
as claimed. An assigned external scalar line multiplies both sides.

For \(b=1\) the formulas give \(R_\lambda=I\) on the scalar tail
and \(D_{\rm inv}=I/N\); all assertions include this case.
For \(b\ge2\), each tail contains a pivot of trace zero. Equation (10)
with \(W_\mu=I\) and cyclic averaging therefore give
\(\operatorname{Tr}R_\lambda=\operatorname{Tr}D_{\rm inv}
 =\operatorname{Tr}D_{\rm cut}=0\).
The invariant density is invertible but not a positive trace density.
The reflection obstruction [R] is therefore not contradicted.

## 7. Quantitative scope and closest coverage

The sharp theorem [C] computes the exponential physical conditioning
of \(J_{\rm av}\). The present proof adds polynomial original
co-source control in that same Gram. Its compensation is the exact
identity (20), including its final term, rather than permission to
ignore the graph frame. Indeed \(G_\lambda\) need not be polynomially
equivalent to the physical tail metric.

[S] already factors genuine braided source charts into total and
multiplicity operators, and [M] already gives complete multiplicity
reductions with original caps and Jordan data. [P] constructs positive
source Grams from specified terminal packets. The new assertion here
is the explicit density (10) and the two-sided bounds (11)--(14)
in the inherited canonical coproduct Gram, at arbitrary fixed width.

Every actual fixed short-filled braid component can retain its genuine
transported crossings in these identities; no sign or word-length
condition has been introduced. They do not bound the resulting word
energy by a geometric partition or compare it with hyperbolic volume.
A trace may cancel even for an invertible, well-conditioned density.
The norm bounds are at the complete roots; no uniform off-root
derivative estimate is asserted.
No positive scalar trace, nonzero geometric cycle coefficient, source
relative precision, or finite-exception volume theorem follows here.

## Complete inputs and coverage

All six complete matching texts were read. Only written mathematics
and text/hash operations were used. No earlier final was edited.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| B, source, 247 lines | [Balanced cyclic source](balanced_verma_coherent_braiding.md) | 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4 |
| M, source, 602 lines | [Complete actual multiplicities](actual_complete_source_multiplicity_module.md) | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| R, source, 212 lines | [Original marked pivotal source](original_reflection_gram_obstruction.md) | 98263806bbbb5d69a9c595d0bba5e9a653063bc306c36f5b75bb482427e7ce85 |
| C, source, 376 lines | [Sharp physical coproduct Gram](research_sharp_physical_coproduct_gram.md) | 6fcdfbece5d9f06c541649926345876aab8daf6dee09022160e79d99a02bafeb |
| S, coverage, 240 lines | [Braided source groupoid](braided_source_groupoid.md) | 81d4cded5dd44b1a256dd84c69a18f4460fc5539c1035d449b64c588fa4a611f |
| P, coverage, 216 lines | [Terminal packet Gram](actual_terminal_packet_positive_gram.md) | dd711ed55c72b926d0302f9cf5da5b7a43bf46080abaf01a6aaa735131f09557 |
