# A positive boundary partition minimized over orthonormal frames

21 November 2026. A finite source on a tree has a positive partition
function after choosing orthonormal bases on its internal edges. The
partition sums squared path amplitudes, whereas the original source
adds those amplitudes coherently. Minimizing the positive partition over
the bases recovers the squared source norm within the product of the
edge dimensions. For a fixed Conway construction that loss is only a
power of the quantum level.

This formulation needs no positive metric eigenvalues, regularization
or unbounded filters. It does retain an optimization over orthonormal
frames. Its geometric asymptotic is not established here.

## 1. The complete Conway source with a constant reference

Fix \(N\geq2\), \(d=N-1\), \(q=e^{\pi i/N}\), and
\(s_r=\prod_{u=1}^r2\sin(\pi u/N)\), with \(s_0=1\).
The actual boundary space is
\[
 H_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 b_r=\frac{\prod_{j<r}(q^{2j+1}+q^{-2j-1}-z)}{s_r^2},
 \quad 0\leq r\leq d.                                \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial. Use the Euclidean coefficient
inner product in this full Newton basis. Repeated-root derivatives remain
part of the algebra. The actual product \(M(f,g)=fg\), genuine turn
\(Jb_r=b_{d-r}\), and original closing rows are the full identities in
[the Conway compiler](research_conway_full_boundary_quotient_gram.md) and
[the Newton source theorem](actual_newton_turn_positive_gram.md).
In particular both original Newton closures are coordinate rows, with
their recorded framing or normalization line retained. The elementary
signed crossing packets are
\[
 R^{\pm1}=\kappa^{\pm1}\sum_{r=0}^d(-q)^{\pm r}b_r,
 \qquad \kappa=q^{d^2/2}.                              \tag{2}
\]
Fractional powers mean the displayed exponential.

Take a fixed literal Conway expression, with its ordered original
closure giving one knot. Let its open packet be \(f_E\), and retain
its original row \(\ell_N\), so that \(K_N=\ell_Nf_E\).
On each edge add an orthogonal reference coordinate:
\[
 \widehat H_N=\mathbb C e_\star\oplus H_N.
\]
This reference is separate from the physical algebraic unit \(b_0\).
Replace each actual gate by
\[
 \widehat f=(1,f),\quad
 \widehat J(a,u)=(a,Ju),\quad
 \widehat M((a,u),(b,v))=(ab,M(u,v)),
\]
and close by \(\widehat\ell_N(a,u)=(a,\ell_Nu)\in\mathbb C^2\).
Mixed reference/physical inputs of \(\widehat M\) are zero.
Induction through the original expression gives exactly
\[
                  Y_N=(1,K_N),\qquad \|Y_N\|^2=1+|K_N|^2.
                                                               \tag{3}
\]
All gates are prescribed before evaluating the invariant. No mark,
ordinary cap, physical normal or framing factor has been replaced.

## 2. Orthonormal edge frames and a positive path partition

The following argument applies to any finite tree, not just this compiler.
Root the tree at its vector output \(Y\in F\), and let \(T_v\) be
its local coefficient tensors. An edge \(e\) has vector space
\(H_e\cong\mathbb C^{n_e}\) at its child end and its bilinear dual
at the parent. Put
\[
                      D=\prod_e n_e.
\]
Assume \(Y\ne0\), as is automatic in (3).

Choose a unitary matrix \(U_e\) whose columns are a new orthonormal
vector basis. The child coordinates transform by \(U_e^*\); the
parent covector coordinates transform by \(U_e^{\mathsf T}\).
Their bilinear evaluation is unchanged because
\(\overline U_eU_e^{\mathsf T}=I\). The output basis of \(F\)
is kept fixed. Write \(T_v(U)\) for the transformed tensors.

A path assignment \(k\) chooses one index \(k_e\) per edge. For
each output index \(o\), its amplitude is
\[
 A_o(k;U)=\prod_v T_v(U)_{\alpha_v(k,o)},\qquad
                         Y_o=\sum_k A_o(k;U).
\]
Here \(\alpha_v\) lists the indices incident at \(v\), together
with \(o\) at the root. Define the positive partition
\[
 Z(U)=\sum_{o,k}|A_o(k;U)|^2
     =\sum_{o,k}\prod_v|T_v(U)_{\alpha_v(k,o)}|^2.
                                                               \tag{4}
\]
These are squared coefficients of the actual transformed tensors.
They are not absolute values taken before the coordinate change.
Thus their dependence on \(U\) retains the original complex phases.
The product of unitary groups is compact and \(Z\) is continuous,
so its minimum is attained.

**Theorem.** For every such finite tree,
\[
 \boxed{\qquad
 \frac{\|Y\|^2}{D}\leq\min_U Z(U)\leq\|Y\|^2.
 \qquad}                                                   \tag{5}
\]

*Proof of the lower bound.* For each output \(o\), Cauchy--Schwarz
on its \(D\) path amplitudes gives
\(|Y_o|^2\leq D\sum_k|A_o(k;U)|^2\). Sum over \(o\).
This holds for every choice of frames, proving the lower bound.

*Proof of the upper bound.* Contract the proper subtree below edge
\(e\) in the original coordinates and call its vector \(a_e\).
It is nonzero: a zero proper message would make \(Y=0\). Put
\(n'_e=\|a_e\|\), and choose
\(U_ee_0=a_e/n'_e\). This uses only proper open messages and
does not divide by an output component.

In these frames a leaf has only its zero output index, with coefficient
\(n'_e\). At a proper vertex \(v\), setting all child indices to
zero leaves the outgoing vector
\[
 c_ve_0,\qquad c_v=\frac{n'_{\rm parent}}
                                    {\prod_{e\text{ child of }v}n'_e}.
                                                               \tag{6}
\]
This follows by multilinearity and the definition of the messages.
Every other outgoing coefficient on that slice is zero. Starting at
the leaves, any nonzero path must therefore have every internal index
zero. At the root, the corresponding vector is
\(Y/\prod_{e\text{ child of root}}n'_e\). The factors (6),
including the leaf factors, telescope to that same denominator.
Consequently the only surviving internal path has amplitude \(Y_o\)
at output \(o\). Thus \(Z(U)=\|Y\|^2\) in these adapted frames.
This proves the upper bound; it does not assert equality for the minimum.
\(\square\)

## 3. The leading rate for Conway sources

For the compiler (3) with \(m\) vertices, every internal dimension is
\(N+1\), and a tree has \(m-1\) internal edges. Write
\(Z_N^{\rm orth}=\min_U Z(U)\). Equation (5) becomes
\[
 \frac{1+|K_N|^2}{(N+1)^{m-1}}
       \leq Z_N^{\rm orth}\leq1+|K_N|^2,              \tag{7}
\]
or equivalently
\[
 0\leq\log(1+|K_N|^2)-\log Z_N^{\rm orth}
                                  \leq(m-1)\log(N+1).
\]
For each fixed expression and \(V>0\), this proves
\[
 \lim_N\frac\pi N\log Z_N^{\rm orth}=V
 \quad\Longleftrightarrow\quad
 \lim_N\frac{2\pi}N\log|K_N|=V.                       \tag{8}
\]
The positive limiting rate implies eventual nonvanishing on the right;
none is assumed. The same abstract conclusion holds for any fixed tree
whose edge dimensions grow polynomially: its logarithmic loss in (5)
is \(O(\log N)\). No additional physical compiler is inferred from
that dimension statement.

There is also a literal minimum/maximum version, without entropy.
Let \(r_{\rm out}=\dim F\), and put
\[
 P(U)=\max_{o,k}\prod_v|T_v(U)_{\alpha_v(k,o)}|^2,
 \qquad P_*=\min_U P(U).
\]
There are \(r_{\rm out}D\) paths including the output index, so
\(P(U)\leq Z(U)\leq r_{\rm out}D P(U)\). The same adapted
frames and Cauchy estimate as above give
\[
 \boxed{\quad
 \frac{\|Y\|^2}{r_{\rm out}D^2}\leq P_*\leq\|Y\|^2.
 \quad}                                                   \tag{9}
\]
Thus on a fixed tree with polynomial-dimensional edges and output,
\(\log P_*\) has the same leading rate too. Equivalently it is
the minimum over frames of the maximum compatible sum of the local
logarithmic squared coefficients, with \(\log0=-\infty\).
For (3), \(r_{\rm out}=2\). This minimum/maximum identity retains
the frame optimization; it does not identify it with the classical
angle optimization.

## 4. The exact entropy formula on the tree

Fix the frames \(U\). Put \(a_{v,\alpha}=|T_v(U)_\alpha|^2\),
and retain only its positive finite support. Let \(p_v\) be a
probability on that support. At the root its variables include the
output index. A family is balanced if its two marginals on every
edge agree; denote the common edge distribution by \(p_e\).
Use \(H(p)=-\sum p\log p\), with \(0\log0=0\), and put
\[
 S_U(p)=\sum_v\left[H(p_v)+\sum_\alpha
                                      p_{v,\alpha}\log a_{v,\alpha}\right].
\]
Equivalently one can include zero coefficients by requiring zero
probability there. Then
\[
 \boxed{\qquad
 \log Z(U)=\max_{p\ \rm balanced}
                      \left[S_U(p)-\sum_eH(p_e)\right].
 \qquad}                                                   \tag{10}
\]
The feasible set is compact and nonempty: \(Y\ne0\) implies at
least one nonzero compatible path in (4).

Here is a proof covering zero marginals. A joint probability on the
nonzero global paths has local marginals \(p_v\) that are balanced.
The chain rule for entropy, followed by conditioning only on the parent
edge instead of all preceding variables, gives
\[
 H(\text{joint probability})
                      \leq\sum_vH(p_v)-\sum_eH(p_e).
\]
Conversely, every balanced family has a joint probability attaining
equality. Start with \(p_{\rm root}\), and at a nonroot vertex
use the conditional probability \(p_v/p_e\) given its parent-edge
index. On a zero marginal that conditional is immaterial: the event
has probability zero. Induction down the tree recovers all the stated
marginals and stays on valid coefficient supports. The chain rule gives
the claimed equality of entropies for this joint probability.

Finally the finite Gibbs identity says that the logarithm of a sum of
positive weights is the maximum of entropy plus mean logarithmic weight.
It follows directly by subtracting relative entropy from the normalized
weight distribution. Apply it to the global weights in (4), use the
preceding upper bound for arbitrary joint probabilities, and the
constructed joint probability for the reverse inequality. This proves
(10) with all support restrictions retained.

For comparison, the same local expression without the edge-entropy
subtraction is a different optimization. Give each fixed-frame edge a
positive diagonal gauge \(\operatorname{diag}(e^{x_{e,k}/2})\) at
the child and its inverse at the parent. If \(F_U(x)\) is the logarithm
of the product of the squared local norms, then
\[
 \inf_xF_U(x)=\max_{p\ \rm balanced}S_U(p).             \tag{11}
\]
Indeed the local Gibbs identities give
\(F_U(x)=\max_p[S_U(p)+x\cdot b(p)]\), where \(b\) is the
list of edge marginal differences. To see strong duality without a
strict-support hypothesis, the set
\(\{(b(p),z):z\leq S_U(p)\}\) is closed and convex. Separate the
point \((0,\beta+\eta)\), where \(\beta=\max_{b=0}S_U\) and
\(\eta>0\). Its separating coefficient of \(z\) is positive:
downward closure makes it nonnegative, and zero would contradict
feasibility at \(b=0\). Division by that coefficient supplies an
\(x\) with \(F_U(x)<\beta+\eta\). Let \(\eta\downarrow0\).

In particular (10)--(11) differ by at most \(\sum_e\log n_e\).
The true positive path partition is (10), not (11). Neither permits
discarding the optimization over frames when seeking a lower bound
for the original source.

## 5. Where the geometric comparison remains

The adapted frames in the proof of (5) also explain the limitation
of a fixed angle-entropy argument. In those frames balanced local
probabilities are forced from the leaves to have every internal edge
distribution equal to \(\delta_0\). Their internal entropies vanish.
The logarithms of (6) telescope, and the root Gibbs expression is
exactly \(\log(1+|K_N|^2)\). These frames are legitimate members
of the compact minimization; the construction has not produced a
geometric lower estimate for that last quantity.

There is a second distinction in the original Newton frame. For an
expanded expression with elementary signed crossing leaves, all the
coefficients of \((1,R^{\pm1})\) have modulus one by (2).
The product and turn tensors are independent of those signs, and a
root framing phase changes no squared coefficient. Thus the fixed
Newton-frame partition, and its entropy problem, are unchanged by
flipping those crossing signs at fixed leaf positions. The dependence
on their phases remains in the transformed coefficients as the
orthonormal frames vary.

To prove a volume theorem from (8), one must bound the positive
partition uniformly over those frames, or prove that a suitable
geometric class of frames already attains its leading minimum. The
choice of one geometrically favorable frame gives an upper bound on
the minimum. Positivity allows a single-path lower bound at that frame;
an eventual volume lower bound requires such control uniformly under
the frame infimum, or a different dual certificate. The
ordinary and marked closing rows, the complete-color derivatives and
the actual short tangle packets cannot be omitted in that comparison.
No such bound, new volume identity or finite-exception theorem is
claimed here.

## Direct sources and written proof check

Both complete matching sources were read. The anchor construction,
finite-tree estimate, adapted frames and entropy arguments are proved
explicitly above. No mathematical program, test, build, git operation
or numerical sample was used.

| Source | SHA-256 |
|---|---|
| [Actual complete Conway compiler](research_conway_full_boundary_quotient_gram.md) | `debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077` |
| [Newton turn and original source](actual_newton_turn_positive_gram.md) | `d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3` |
