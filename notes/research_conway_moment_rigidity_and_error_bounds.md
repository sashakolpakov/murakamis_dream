# The optimal Conway moments are uniquely determined by one packet field

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

Every moment in the order-two Conway semidefinite problem is determined
at its optimum: it is evaluation at the unique minimizing packet field.
Thus its optimal moment matrices have rank one. The ball localizers are
essential to this conclusion; positivity of the moment matrix and
vanishing second moments alone would not control the fourth moments.

We also give error estimates for a feasible near-optimal solution. They
control individual moments and the trace norms of whole local matrices,
with constants independent of the quantum level. The estimates apply to
the exact boundary problem of a connected short component as well.
They do not evaluate the source minimum or prove a volume lower bound.

## 1. The source problem and its local moment functionals

Use the actual normalized Conway source and its gate decomposition in
the [local semidefinite gluing theorem](research_conway_gate_local_semidefinite_gluing.md).
The variable at each proper vertex is its complete complex Newton
packet, written in real and imaginary coordinates. The feasible set
is the product of their unit balls. A gate bag contains its output
packet and its at most two input packets; the closing bag contains
the top packet. Thus a bag contains at most three packets.

Write \(g_w(x)=1-\|x_w\|^2\). With \(t=1/4\), the redistributed
local costs are
\[
 V_v=\|\Phi_v((x_c)_c)-x_v\|^2-t\|x_v\|^2
                  +t\sum_c\|x_c\|^2,\qquad
 V_\rho=|Lx_{v_0}|^2+t\|x_{v_0}\|^2.
 \tag{1}
\]
Their sum is the original energy \(E\). Its unique minimum and
minimizer will be denoted by \(e_*\) and \(x_*\). In particular
\(x_*\) is the minimizing field of the energy, not the exact open
recursion field \(a\) satisfying \(G(a)=0\). The
[convex source theorem](research_convex_normalized_conway_source.md)
gives
\[
 B_{\rm tot}^2e_*\le |K_N|^2\le(197/196)B_{\rm tot}^2e_*.
 \tag{2}
\]
All source phases, normal directions and budgets retain their stated
normalization.

At each bag \(C\), a feasible real functional \(\mathcal L_C\)
acts on polynomials of degree at most four and satisfies
\[
 \mathcal L_C(1)=1,\quad
 \mathcal L_C(p^2)\ge0\ (\deg p\le2),\quad
 \mathcal L_C(g_wp^2)\ge0\ (w\in C,\ \deg p\le1).
 \tag{3}
\]
Only the first moments of packets shared by adjacent bags are matched.
Its objective is \(P=\sum_C\mathcal L_C(V_C)\), using the
redistributed costs, and the exact minimum of this problem is \(e_*\).

We use the local polynomial supporting inequality already proved in
that theorem. If \(b\) is any feasible center in a bag and
\(\mu=31/128\), then
\[
 V_C(x)-V_C(b)-\nabla V_C(b)\cdot(x-b)
                     -\frac\mu2\|x-b\|^2\in Q_2(C).
 \tag{4}
\]
Here \(Q_2(C)\) consists of sums of squares of quadratics plus
the ball constraints times sums of squares of linear polynomials.
Every functional in (3) is nonnegative on this cone. No representing
measure for that functional is assumed.

## 2. What the ball localizers control

The following elementary facts concern one bag. Suppress its label,
let it contain \(r\le3\) packets, and let \(b\) be any point in
their unit balls. Put
\[
 p_i=x_i-b_i,\qquad v_i=\mathcal L(p_i^2),\qquad
                         S=\sum_i v_i=\mathcal L(\|x-b\|^2).
 \tag{5}
\]
Indices in this section run through real coordinates, including both
real and imaginary parts of each original Newton coefficient.

For polynomials of degree at most two, moment positivity gives the
Cauchy--Schwarz inequality
\[
 |\mathcal L(fh)|^2\le\mathcal L(f^2)\mathcal L(h^2).
 \tag{6}
\]
It follows by applying positivity to \((sf+h)^2\), with a real
parameter \(s\). In particular \(v_i\ge0\).

If coordinate \(x_i\) belongs to packet \(w\), then for every
linear polynomial \(f\) on the entire bag,
\[
 \mathcal L(x_i^2f^2)\le\mathcal L(f^2).
 \tag{7}
\]
Indeed
\[
 (1-x_i^2)f^2=g_wf^2+
                      \sum_{j\in w,\ j\ne i}(x_jf)^2,
\]
and every term has nonnegative value under (3). The polynomial \(f\)
may involve another packet. This is why all packet localizers in a
bag are retained.

**Lemma 1.** For every raw monomial \(x^\alpha\) of degree
\(k\le4\),
\[
          |\mathcal L(x^\alpha)-b^\alpha|\le k\sqrt S.
 \tag{8}
\]

**Proof.** The seminorm \(\|f\|_{\mathcal L}
=\sqrt{\mathcal L(f^2)}\) obeys the triangle inequality on
quadratic polynomials, by (6). Every monomial of degree at most two
has seminorm at most one, by (7). For a quadratic monomial,
\[
 x_ix_j-b_ib_j=x_i(x_j-b_j)+b_j(x_i-b_i),
\]
so (7) and \(|b_j|\le1\) give seminorm at most
\(\sqrt{v_i}+\sqrt{v_j}\). The corresponding linear estimate
is \(\sqrt{v_i}\).

Factor a monomial of degree at most four as \(AB\), where each
factor has degree at most two. Write
\[
 AB-A(b)B(b)=(A-A(b))B+A(b)(B-B(b)).
\]
Apply (6), the seminorm bounds just obtained, and
\(|A(b)|\le1\). The result is at most the sum of
\(\sqrt{v_i}\) over its \(k\) coordinate occurrences, hence
at most \(k\sqrt S\). Repeated indices cause no difficulty.
\(\square\)

In particular, \(S=0\) forces the entire functional through degree
four to be evaluation at \(b\). No assertion about unrecorded moments
of higher degree is needed.
Without the localizer this would be false: in one real variable,
\(\mathcal L(1)=\mathcal L(x^4)=1\) and
\(\mathcal L(x)=\mathcal L(x^2)=\mathcal L(x^3)=0\)
give the positive moment matrix \(\operatorname{diag}(1,0,1)\),
but not evaluation at zero.

## 3. Uniform bounds for the whole local matrices

Let \(m_j(x)\) be the vector of distinct raw monomials of degree at
most \(j\), each appearing once with coefficient one. Define
\[
 M_2=\mathcal L(m_2m_2^{\mathsf T}),\qquad
 M_1(g_w)=\mathcal L(g_wm_1m_1^{\mathsf T}).
\]
The trace norm \(\|A\|_1\) of a real symmetric matrix is the sum
of the absolute values of its eigenvalues.

**Lemma 2.** With (5),
\[
 \begin{aligned}
 \|M_2-m_2(b)m_2(b)^{\mathsf T}\|_1
                              &\le26\sqrt S+13S,\\
 \|M_1(g_w)-g_w(b)m_1(b)m_1(b)^{\mathsf T}\|_1
                              &\le12\sqrt S+S.
 \end{aligned} \tag{9}
\]
The constants are independent of the number of real coordinates
inside each packet.

**Proof.** First use the redundant ordered-tensor feature vector
\(F(x)=(1,x,x\otimes x)\). Its quadratic coordinates include both
\(x_ix_j\) and \(x_jx_i\). The localizers give
\[
 \mathcal L(\|x\|^2\|p\|^2)\le rS,
\]
by summing \(\mathcal L(g_wp_i^2)\ge0\) over all packets and
coordinates. Since \(\|b\|^2\le r\), the identity
\(x\otimes x-b\otimes b=x\otimes p+p\otimes b\) yields
\[
 \mathcal L(\|F(x)-F(b)\|^2)\le(1+4r)S\le13S,
 \qquad \|F(b)\|^2\le1+r+r^2\le13.
 \tag{10}
\]
Here the first inequality uses the squared triangle bound
\(\|u+v\|^2\le2\|u\|^2+2\|v\|^2\).

Put \(z=F-F(b)\), \(h=\mathcal L(z)\), and
\(W=\mathcal L(zz^{\mathsf T})\). Moment positivity gives
\(W\succeq0\), \(\operatorname{tr}W\le13S\), and
\(\|h\|^2\le\operatorname{tr}W\). Expanding
\(\mathcal L(FF^{\mathsf T})\) about \(F(b)\) gives trace-norm
error at most
\(2\|F(b)\|\|h\|+\operatorname{tr}W\), proving the first
bound in this redundant frame. Selecting one copy of each quadratic
monomial is a coordinate projection of operator norm one. Compression
by that projection cannot increase trace norm: apply the spectral
decomposition to a symmetric matrix and the triangle inequality.
This proves the bound for the stated standard monomial matrix.

For the second bound, write \(v=(1,b)\) and \(z=(0,p)\).
The localizing conditions give
\[
 0\le\mathcal L(g_w)\le1,\quad
 C_g=\mathcal L(g_wzz^{\mathsf T})\succeq0,\quad
                         \operatorname{tr}C_g\le S.
 \tag{11}
\]
The last inequality follows since
\(\mathcal L(zz^{\mathsf T})-C_g
=\sum_{j\in w}\mathcal L(x_j^2zz^{\mathsf T})\succeq0\).
Weighted Cauchy--Schwarz for the positive localizer matrix implies
\(\|\mathcal L(g_wz)\|^2\le S\).

We also have
\[
                     |\mathcal L(g_w)-g_w(b)|\le2\sqrt S.
 \tag{12}
\]
To justify it with no dimension loss, restrict \(x,b,p\) in this
calculation to packet \(w\). Then
\(g_w(x)-g_w(b)=-\langle x+b,p\rangle\).
The identity
\[
 4-\|x+b\|^2=2g_w(x)+2(1-\|b\|^2)+\|p\|^2
\]
and the sum-of-squares Lagrange identity show that
\(4\|p\|^2-(g_w(x)-g_w(b))^2\) is a sum of squares plus
\(2g_w\|p\|^2\). Applying (3) and then (6) proves (12).

Finally expand the localizer about \(v\). Its error is the sum of
\[
 (\mathcal L(g_w)-g_w(b))vv^{\mathsf T},\quad
 v\mathcal L(g_wz)^{\mathsf T}
       +\mathcal L(g_wz)v^{\mathsf T},\quad C_g.
\]
Their trace norms total at most
\(2(1+r)\sqrt S+2\sqrt{1+r}\sqrt S+S\), which is bounded by
the second line of (9) for \(r\le3\). \(\square\)

## 4. Objective gap, unique optimal moments, and certified error

For a feasible local moment family put
\[
 \Delta=P-e_*\ge0,\qquad
 S_C=\mathcal L_C(\|x_C-x_{*,C}\|^2).
\]
Applying (4) at the restrictions of \(x_*\) and summing gives
\[
 \boxed{\qquad \sum_C S_C\le\frac{2\Delta}{\mu}
                                      =\frac{256}{31}\Delta.
 \qquad} \tag{13}
\]
Indeed the linear terms sum to
\(\nabla E(x_*)\cdot(m-x_*)=0\): shared first moments give a
single feasible mean field \(m\), and the source minimizer is
interior and stationary. No equality of shared second moments is used.

**Theorem.** The optimal local moment family is unique. Each functional
is evaluation at \(x_{*,C}\) on every polynomial of degree at most
four. Its order-two moment matrix has rank one, and every ball
localizer has rank one as well. For an arbitrary feasible family,
Lemmas 1--2 hold in each bag with
\(S_C\le256\Delta/31\).

**Proof.** At an optimum (13) gives \(S_C=0\) in every bag.
Lemma 1 determines every recorded moment, proving uniqueness.
The moment matrix is exactly
\(m_2(x_{*,C})m_2(x_{*,C})^{\mathsf T}\).
The localizer is its degree-one counterpart times
\(g_w(x_*)>0\), since the minimizing field is interior.
The constant monomial ensures that both matrices have rank one.
The quantitative assertion is (13) and the two lemmas. \(\square\)

These are usable a posteriori bounds without knowing \(e_*\).
If any feasible dual certificate has value \(d\le e_*\), the
computed primal--dual gap \(\widehat\Delta=P-d\) bounds \(\Delta\)
above. It can replace \(\Delta\) in (13) and every displayed error
bound. For example \(\widehat\Delta\le(\mu/2)\varepsilon^2\)
ensures error at most \(k\varepsilon\) for each degree-\(k\)
monomial in each bag.

## 5. The optimal forces and clamped short components

The affine-force dual in the local gluing theorem has proper-packet
forces \(p_v\), local adjusted costs
\(F_v=V_v-p_v\cdot x_v+\sum_cp_c\cdot x_c\), and root cost
\(F_\rho=V_\rho+p_{v_0}\cdot x_{v_0}\). It imposes
\(F_v-\alpha_v\in Q_2(C_v)\).
Its optimal forces and constants are also unique. To see this,
evaluate any optimal certificate at \(x_*\). Each
\(F_v(x_*)-\alpha_v\) is nonnegative, and their sum is zero.
Thus \(x_{*,C_v}\) minimizes every adjusted local cost. It is
interior, so its output derivative gives necessarily
\[
 p_v=\partial_{x_v}V_v(x_*),\qquad
                         \alpha_v=F_v(x_*;p).
 \tag{14}
\]
This argument does not assert uniqueness of the positive semidefinite
Gram matrices representing the local polynomial certificates.

The same moment conclusion holds at the minimum of a clamped connected
short-component problem from the local gluing theorem. Fix its boundary
first moments, and let \(b\) be the unique minimizing field of the sum
of its redistributed gate costs. Sum (4) at \(b\). The linear terms
are nonnegative by the minimizing variational inequality on the product
of internal balls; the boundary mean variations vanish and the internal
means match. Hence (13), with the same \(\mu\), holds with the
block's own objective gap. Lemmas 1--2 apply unchanged. In particular
the exact boundary epigraph at its minimal height has a unique moment
lift, namely evaluation at that minimizing block field.
At a boundary-clamped unit packet its localizer can be zero rather than
rank one; its moment matrix still has rank one. No internal packet or
first-normal direction is removed by this statement.

## 6. What has been simplified

The auxiliary moment variables have no independent freedom at the
optimum. They all describe one deterministic packet field, with the
quantitative bounds above for near-optimal data. Away from the optimum
the feasible semidefinite set still contains non-atomic moment data,
for example averages of evaluations at different feasible fields.
Thus the localizers cannot simply be discarded.

There is an exact deterministic rounding at every feasible point:
replace the local functionals by evaluation at their consistent first
means. The local Jensen inequality from the gluing theorem shows that
this preserves feasibility and cannot increase the objective. This is
a reduction to the point-valued convex minimization already known; it
does not make its objective linear.

Recovering the rank-one moments from their first moments uses the
nonlinear equations \(\mathcal L(x^\alpha)=\mathcal L(x)^\alpha\).
It does not turn the problem into linear transport. The minimizing field
solves the cubic stationary equations of \(E\), or the contracting
iteration already proved for that energy. It need not solve \(G(x)=0\).
The original source is still its prescribed coherent closing, with
the comparison (2).

Finally, all error bounds here are additive in the normalized objective
gap. If \(e_*\) is exponentially small, a small absolute gap need not
be small relative to \(e_*\). Neither atomicity nor uniform local
matrix control supplies the geometric exponential rate or the missing
finite-exception volume theorem.

## Complete direct sources

Both complete matching texts were read. Their local certificates,
exact moment formulation and source normalization are the inputs;
the moment-contraction, matrix error and uniqueness arguments are
proved above.

| Source | SHA-256 |
|---|---|
| [Gate-local semidefinite gluing](research_conway_gate_local_semidefinite_gluing.md) | 8b3241f9cc8a9e740aa4223345e39932f3a2096fcdab60f55458a6266857e8e9 |
| [Normalized convex source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

Only written mathematics and text/hash operations were used. No
mathematical program, numerical iteration, test, build, git operation
or earlier-final edit was performed.
