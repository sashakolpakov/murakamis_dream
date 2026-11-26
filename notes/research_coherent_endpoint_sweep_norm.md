# Coherent endpoint transport through original crossings

Written proof, 24 November 2026.

A fixed positive sweep of overlapping original crossings preserves
the endpoint-to-bulk norm rate for every coherent input in a sublinear
endpoint box. The inputs may be entangled across all heads, with
arbitrary level-dependent coefficients. The proof uses bounded
conjugates of prefix Cartans rather than a possibly unbounded
conjugate of an individual second-head Cartan.

Every matrix entry of this sweep has one transfer path. Its column
norms can therefore be estimated exactly. Multivariate selected-root
filters then control cancellation between the columns. The full
outgoing packet is retained; no endpoint projection is inserted
between crossings. A separate exact returned block has a controlled
inverse and two explicitly specified positive incident metrics.
No original scalar closing is estimated below.

## 1. The original sweep and its endpoint inputs

Fix an integer \(b\ge2\), independently of the level \(N\ge2\), and put
\[
 r=b-1,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad \kappa=q^{d^2/2}.
 \tag{1}
\]
The balanced physical head basis is orthonormal. Use
\[
 E|a\rangle=(Q^{-a}-1)|a-1\rangle,\quad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\quad
 K|a\rangle=xQ^{-a}|a\rangle,
 \tag{2}
\]
with the missing endpoint arrows zero. Operator subscripts label
physical heads. All vector norms are product Hilbert norms in
these bases, not Newton coefficient norms.

Let \(R_j\) be the original checked positive crossing on heads
\(j,j+1\), including its Cartan scalar. Define
\[
 \mathsf W_{b,N}=R_r\cdots R_1,\qquad
 v_{\boldsymbol a}=|d-a_0,a_1,\ldots,a_r\rangle,\qquad
 \mathcal H_{m,b}=\operatorname{span}
       \{v_{\boldsymbol a}:0\le a_j<m\}.
 \tag{3}
\]
The \(a_j\) are independent integers. In particular the input
need not have one fixed total degree. The physical degree and
all finite head restrictions are nevertheless preserved by the
actual crossings.

Write
\[
 S_n=\prod_{\ell=1}^n2\sin(\pi\ell/N),\quad S_0=1,\qquad
 h(t)=\int_0^t\log(2\sin\pi y)\,dy,\quad
 h_*=h(5/6)=-h(1/6)>0,
 \tag{4}
\]
\[
                 \Lambda_{N,m}=m\log(eN/m)+\log N.
 \tag{5}
\]

**Theorem.** There is a constant \(C_b\) such that, for all
sufficiently large \(N\), every integer \(1\le m\le N/(24b)\),
and every \(v\in\mathcal H_{m,b}\),
\[
 e^{Nh_*-C_b\Lambda_{N,m}}\|v\|
 \le\|\mathsf W_{b,N}v\|
 \le e^{Nh_*+C_b\Lambda_{N,m}}\|v\|.
 \tag{6}
\]
Consequently, for every \(m_N=o(N)\), uniformly over nonzero
coherent inputs in these spaces,
\[
 \frac1N\log\frac{\|\mathsf W_{b,N}v_N\|}{\|v_N\|}
                             \longrightarrow h_*.
 \tag{7}
\]
The exponent is \(h_*\), not \(r h_*\). This is an open-packet
norm theorem for the specified fixed sweep and endpoint orientation.

## 2. Two good checked identities, directly at the finite endpoints

For one crossing, [G] gives the coefficient from \(|a,b_0\rangle\)
to \(|b_0+k,a-k\rangle\):
\[
 c_{a,b_0}(k)=
 \kappa x^{-a-b_0+k}Q^{(a-k)b_0}
 \frac{(Q;Q)_{b_0+k}(Q;Q)_a}
      {(Q;Q)_k(Q;Q)_{b_0}(Q;Q)_{a-k}} .
 \tag{8}
\]
Its support is \(0\le k\le a\), \(b_0+k\le d\).
Every displayed factorial is a unit. The checked identities are
\[
 RK_1R^{-1}=K_2-qE_2K_1F_1,\qquad
 RE_1R^{-1}=K_1E_2,\qquad
 R(K_1K_2)=(K_1K_2)R .
 \tag{9}
\]
The first is proved from these same entries in [E]. To fix its
operator order explicitly, the first matrix on the right acts on
\(|i,j\rangle\) with diagonal \(xQ^{-j}\) and coefficient
\[
 Q^{-i-1}(1-Q^{i+1})(Q^{-j}-1)
                         \quad\hbox{to }|i+1,j-1\rangle .
 \tag{10}
\]
The adjacent-transfer ratio in (8) is
\[
 \frac{c_{a,b_0}(k+1)}{c_{a,b_0}(k)}
   =xQ^{-b_0}
       \frac{(1-Q^{b_0+k+1})(1-Q^{a-k})}{1-Q^{k+1}} .
 \tag{11}
\]
Using \(x^2Q=1\), this is exactly the eigenvector recurrence
for (10) with eigenvalue \(xQ^{-a}\). Its initial diagonal
has that eigenvalue, and its last arrow vanishes at \(j=0\)
or \(i=d\). This verifies the first identity on every input.

For the second identity one needs a different finite comparison:
\[
 \frac{c_{a-1,b_0}(k)}{c_{a,b_0}(k)}
       =xQ^{-b_0}\frac{1-Q^{a-k}}{1-Q^a},
                         \qquad 0\le k\le a-1 .
 \tag{12}
\]
Multiplication by \(Q^{-a}-1\) gives
\(xQ^{-a-b_0}(1-Q^{a-k})\). This equals
\(xQ^{-b_0-k}(Q^{-a+k}-1)\), the factor from applying
\(K_1E_2\) after the original crossing. The possible extra term
\(k=a\) is killed by \(E_2\) at its zero index; \(a=0\)
vanishes on both sides. Recipient upper endpoints agree as well.
Thus \(RE_1=K_1E_2R\) holds without adding any arrow or normal
coupon. Finally each output in (8) has the same total occupation
as its input, proving the last identity in (9).

The scalar \(\kappa\) was present in all these comparisons and
cancels equally. These are identities of the whole physical
matrices, not evaluations of commuting principal symbols.

## 3. Bounded commuting observables for the whole sweep

Let \(J_j=K_1\cdots K_j\), \(J_0=I\), and define
\(\mathcal A_j=\mathsf W_{b,N}J_j\mathsf W_{b,N}^{-1}\).
For \(1\le j\le r\), put
\[
 H_{j,r}=\sum_{\ell=j}^{r}
              (K_{r-1}K_{r-2}\cdots K_\ell)F_\ell .
 \tag{13}
\]
The product is empty at \(\ell=r\); all its Cartans stand to
the left of \(F_\ell\). Then, exactly,
\[
 \mathcal A_j
   =J_{j-1}\bigl(K_b-qE_bK_rH_{j,r}\bigr)\quad(j\le r),
 \qquad \mathcal A_b=J_b .
 \tag{14}
\]
Indeed crossings wholly inside the first \(j\) heads preserve
\(J_j\). The first crossing through its boundary gives the
first identity in (9), with \(J_{j-1}\) outside. Each later
crossing replaces the moving \(K\) by its good polynomial in
(9), and the moving \(E\) by \(KE\). Induction appends precisely
one term to (13), proving (14) in its displayed order.

There are \(r-j+1\) terms in (13), each of norm at most two.
Since all \(K_i\) are unitary and \(\|E_i\|,\|F_i\|\le2\),
\[
              \|\mathcal A_j\|\le1+4(r-j+1)\quad(j\le r),
                    \qquad \|\mathcal A_b\|=1 .
 \tag{15}
\]
No inverse of an individual conjugated second-head Cartan occurs.
All the \(\mathcal A_j\) commute exactly, as conjugates of the
original commuting prefix Cartans.

Let \(f_{\boldsymbol a}=\mathsf W_{b,N}v_{\boldsymbol a}\).
Its joint eigenvalue indices are
\[
 t_j(\boldsymbol a)=a_0-\sum_{\ell=1}^{j-1}a_\ell,\qquad
 \mathcal A_jf_{\boldsymbol a}
      =\zeta_{j,t_j(\boldsymbol a)}f_{\boldsymbol a},\qquad
 \zeta_{j,t}=x^jQ^{1+t}.
 \tag{16}
\]
This follows directly from the input prefix occupations.
The tuple of indices determines the input:
\(a_0=t_1\) and \(a_\ell=t_\ell-t_{\ell+1}\).

## 4. The joint selected Gram has subexponential cost

Each index in (16) belongs to the consecutive integer interval
\[
 I_j=[-(j-1)(m-1),\,m-1]\cap\mathbb Z,\qquad
                         |I_j|=j(m-1)+1 .
 \tag{17}
\]
Its diameter is less than \(N/2\) in our range. Consequently
\[
 |\zeta_{j,t}-\zeta_{j,s}|\ge4|t-s|/N,\qquad t,s\in I_j .
 \tag{18}
\]
For each \(t\in I_j\), form the ordinary Lagrange polynomial
\[
 L_{j,t}(z)=\prod_{\substack{s\in I_j\\s\ne t}}
                       \frac{z-\zeta_{j,s}}{\zeta_{j,t}-\zeta_{j,s}} .
 \tag{19}
\]
The numerator factors evaluated at \(\mathcal A_j\) have norm
bounded by a constant depending only on \(b\). If \(n_j=|I_j|-1\),
the denominator in (19) is at least
\((4/N)^{n_j}(t-\min I_j)!(\max I_j-t)!\).
Using the binomial bound and \(n!\ge(n/e)^n\) gives
\[
 \|L_{j,t}(\mathcal A_j)\|
       \le\frac{(C_bN)^{n_j}}{n_j!}
       \le\exp\{C_bm\log(eN/m)\}.
 \tag{20}
\]
Empty products have value one. Since \(n_j\le bm\), the last
bound is uniform in every index. This is an operator-product
estimate, not a scalar spectral supremum.

The commuting product
\(\Pi_{\boldsymbol a}=\prod_{j=1}^b
L_{j,t_j(\boldsymbol a)}(\mathcal A_j)\) therefore has norm at
most \(\exp\{C_bm\log(eN/m)\}\). It recovers one selected
column and kills the other selected columns. The injectivity
following (16) proves this without an interpolation of degree
\(m^b\). No assertion about unselected joint eigenspaces is needed.

Normalize each actual column internally:
\(u_{\boldsymbol a}=f_{\boldsymbol a}/\|f_{\boldsymbol a}\|\),
and let \(V_mc=\sum_{\boldsymbol a}c_{\boldsymbol a}u_{\boldsymbol a}\).
All columns are nonzero because the original sweep is invertible.
Applying the selected filters and summing over \(m^b\) tuples yields
\[
       e^{-C_b\Lambda_{N,m}}I
               \preceq V_m^*V_m\preceq m^bI .
 \tag{21}
\]
For the lower bound use
\(|c_{\boldsymbol a}|\le\|\Pi_{\boldsymbol a}\|\|V_mc\|\).
The upper bound is triangle and Cauchy--Schwarz.
Thus all coherent cross terms are controlled.

## 5. Exact unique-path columns and their common norm rate

For an input in (3), write \(A_0=d-a_0\),
\(K_j=k_1+\cdots+k_j\), and \(A_j=A_0-K_j\).
The outputs are
\((a_1+k_1,\ldots,a_r+k_r,A_r)\), on the exact support
\[
 k_j\ge0,\quad K_r\le A_0,\quad a_j+k_j\le d .
 \tag{22}
\]
Each output fixes every \(k_j\), so there is no internal sum
at one matrix entry. The exact formula of [F] is
\[
 (\mathsf W_{b,N})_{\rm out,in}
     =\Xi_N\frac{S_{A_0}}{S_{A_r}}
               \prod_{j=1}^r\frac{S_{a_j+k_j}}{S_{a_j}S_{k_j}},
 \qquad
 \Xi_N=\prod_{j=1}^r\chi_N(A_j,a_j,k_j),\quad|\Xi_N|=1,
 \tag{23}
\]
where
\[
 \chi_N(j,a,k)=\kappa x^{-j-a}Q^{ja}(-i)^k
                     q^{k(j+a)+k(k+1)/2}.
 \tag{24}
\]
In particular every common Cartan scalar and entry phase is retained.

The endpoint-uniform factorial estimate proved in [E] gives
\[
 \log S_n=Nh(n/N)+O(\log N),\quad
 \max_n S_n,\ \max_n S_n^{-1}\le e^{Nh_*+C\log N}.
 \tag{25}
\]
Also \(S_{d-a}=N/S_a\), and, for \(1\le a\le m\),
\[
 S_a\ge(4/N)^a a!,\quad S_a\le2^a,\quad
                    S_{a+k}/S_k\le2^a .
 \tag{26}
\]
At \(a=0\) the corresponding factors equal one.
Equations (23)--(26) give the uniform entry upper bound
\(\exp\{Nh_*+C_b\Lambda_{N,m}\}\). There are at most \(N^r\)
outputs in one column, so the same form bounds its vector norm.

For a lower bound choose
\[
 n_*=\lfloor N/6\rfloor,\qquad
 k_1=d-a_0-n_*,\qquad k_j=0\quad(j>1).
 \tag{27}
\]
For sufficiently large \(N\) and \(m\le N/(24b)\), this is
a legal transfer in (22). The factors in
\(S_{k_1+a_1}/S_{k_1}\) all lie on a fixed compact sine
interval around \(5/6\), so this ratio is at least \(c^{a_1}\)
for a fixed \(c>0\). All other recipient ratios in (23) equal
one. Using \(S_{d-a_0}=N/S_{a_0}\), \(S_a\le2^a\), and
\(S_{n_*}^{-1}=\exp\{Nh_*+O(\log N)\}\), this one entry has
modulus at least \(\exp\{Nh_*-C_bm-C\log N\}\).
Consequently every column obeys
\[
 e^{Nh_*-C_b\Lambda_{N,m}}\le\|f_{\boldsymbol a}\|
                       \le e^{Nh_*+C_b\Lambda_{N,m}} .
 \tag{28}
\]
For the vacuum tuple \(\boldsymbol a=0\), (23)'s modulus is
\(N/S_{d-K_r}=S_{K_r}\). Different compositions of the same
total transfer give only a polynomial multiplicity at fixed \(b\).
This explains why the column exponent does not add across crossings.

Finally write
\(\mathsf W_{b,N}v
 =V_m(c_{\boldsymbol a}\|f_{\boldsymbol a}\|)_{\boldsymbol a}\).
Combining (21) and (28) proves (6), after increasing \(C_b\).
Since \(\Lambda_{N,m_N}/N\to0\) for every \(m_N=o(N)\), it also
proves (7).

## 6. An exact returned block and its incident metrics

There is also a source-specific estimate when one explicitly observes
the original endpoint band after a single crossing. Extend [E]'s
definition to every \(1\le m\le N\):
\(H_m^+=\operatorname{span}\{|d-\alpha,\alpha\rangle:0\le\alpha<m\}\)
and \(H_m^-=\mathsf P H_m^+\). Let \(\mathcal Q_m^\pm\) be their
orthogonal projections and
\(\mathcal B_m^\pm=\mathcal Q_m^\pm R_N^\pm\mathcal Q_m^\pm\)
on the indicated band. The exact identities below hold for all
\(1\le m\le N\). The positive matrix is
\[
 (\mathcal B_m^+)_{\beta\alpha}
   =\kappa N x^{-\alpha-\beta}
       \frac{f_{\alpha+\beta}}{f_\alpha^2f_\beta^2},
 \qquad f_j=(Q;Q)_j,\qquad 0\le\alpha,\beta<m .
 \tag{29}
\]
This is the literal checked entry (8), with output first index
\(d-\beta\). To simplify it, retain the exact reflection
\(f_t f_{d-t}=N(-1)^tQ^{t(t+1)/2}\). Its phase \(Q^{-\alpha\beta}\)
cancels the original \(Q^{\alpha\beta}\). The same cross-collar
kernel and its full normal-source conventions are given in [L].
When \(\alpha+\beta\ge N\), its numerator \(f_{\alpha+\beta}\)
is zero, exactly as the original support requires. Its denominators
are still units, since \(\alpha,\beta<N\); no \(f_N\) is divided out.

Define the Gaussian polynomials by
\({n\brack0}_Q={n\brack n}_Q=1\), zero outside \(0\le k\le n\),
and
\({n+1\brack k}_Q={n\brack k}_Q+Q^{n+1-k}{n\brack k-1}_Q\).
Equivalently the coefficient of \(t^k\) in
\(\prod_{j=0}^{n-1}(1+Q^jt)\) is
\(Q^{k(k-1)/2}{n\brack k}_Q\). They can be specialized at the
root for every \(n\), including \(n\ge N\).
Put \(D_{\alpha\alpha}=x^{-\alpha}/f_\alpha\),
\(L_{\alpha k}={\alpha\brack k}_Q\) for \(k\le\alpha\), and
\(J_{kk}=Q^{k^2}\). The exact finite factorization is
\[
                 \mathcal B_m^+=\kappa N D L J L^{\mathsf T}D .
 \tag{30}
\]
Here transpose does not conjugate coefficients. The identity
\({\alpha+\beta\brack\alpha}_Q
=\sum_kQ^{k^2}{\alpha\brack k}_Q{\beta\brack k}_Q\)
proves (30). Its left side equals
\(f_{\alpha+\beta}/(f_\alpha f_\beta)\), also when the
numerator vanishes, since these two denominator factors are units.
To verify the identity directly, expand
\(\prod_{j=0}^{\alpha+\beta-1}(1+Q^jt)\), split after its
first \(\alpha\) factors, and compare \(t^\alpha\). Setting
\(k=\alpha-j\) in that coefficient gives exponent \(k^2\)
after dividing the common \(Q^{\alpha(\alpha-1)/2}\).

The triangular inverse is
\[
 (L^{-1})_{\alpha k}
 =(-1)^{\alpha-k}Q^{(\alpha-k)(\alpha-k-1)/2}
                                  {\alpha\brack k}_Q .
 \tag{31}
\]
Multiplication uses
\({\alpha\brack j}_Q{j\brack k}_Q
={\alpha\brack k}_Q{\alpha-k\brack j-k}_Q\);
the remaining finite sum is \((1;Q)_{\alpha-k}\), which
vanishes for \(\alpha>k\) and equals one for \(\alpha=k\).
Thus this is an exact inverse before any norm estimate.

The finite \(q\)-Pascal recursion and \(|Q|=1\) imply
\(|{\alpha\brack k}_Q|\le\binom{\alpha}{k}\).
Both \(L,L^{-1}\) have row sums at most \(2^{m-1}\) and
column sums at most \(2^m\), so their operator norms are at most
\(2^m\). Also \(\|D^{-1}\|\le2^{m-1}\) and
\(\|D\|\le H_N(m):=(eN/m)^m\) when \(m\le N/2\), by (26).
Consequently
\[
 \begin{split}
 \|(\mathcal B_m^+)^{-1}\|&\le16^m/N,\quad
 |\det\mathcal B_m^+|
       =\frac{N^m}{\prod_{\alpha=0}^{m-1}S_\alpha^2}
                                      &&(1\le m\le N),\\
 \|\mathcal B_m^+\|&\le N4^mH_N(m)^2 &&(1\le m\le N/2).
 \end{split}
 \tag{32}
\]
At \(m=N\), reflection gives \(\prod_{\alpha=0}^dS_\alpha^2=N^N\),
so the full degree-\(d\) block has determinant of modulus one.
The reflected negative block is its entrywise conjugate by
\(R_N^-=\mathsf P\overline{R_N^+}\mathsf P\), so the same
bounds hold on \(H_m^-\).
The inverse in (32) is the inverse of the returned compression.
It need not equal \(\mathcal Q_m^+R_N^{-1}\mathcal Q_m^+\);
at \(m=N\) these do agree on the invariant degree block.
The mirrored negative block must not be identified with that
inverse. Complementary excursions distinguish compression and
inversion in general.
In particular every nonzero vector in a sublinear selected band
has returned-vector norm with logarithmic rate zero:
\[
 \frac1N\log
     \frac{\|\mathcal Q_{m_N}^\pm R_N^\pm v_N\|}{\|v_N\|}
                 \longrightarrow0,\qquad m_N=o(N).
 \tag{33}
\]
This differs from the positive rate of its entire outgoing packet.

The factorization also specifies a genuine orthogonality relation
with two incident metrics. Set \(U=DL\) and
\[
 G_{\rm out}=(U^{-1})^*U^{-1},\qquad
 G_{\rm in}=(U^{\mathsf T})^*U^{\mathsf T}.
 \tag{34}
\]
Both are positive definite for all \(m\le N\), and (30) gives exactly
\[
                 (\mathcal B_m^+)^*G_{\rm out}\mathcal B_m^+
                                      =N^2G_{\rm in}.
 \tag{35}
\]
Indeed the middle \(J\) is diagonal unitary.
When \(m\le N/2\), \(\|U\|\le2^mH_N(m)\) and \(\|U^{-1}\|\le4^m\).
Thus the two metrics and their inverses have norms at most
\(\exp(C\Lambda_{N,m})\). They are two specified incident
metrics, not one preserved inner product for the full crossing.

One associated quadratic minimization can be evaluated completely:
\[
       \min_{\substack{c\in\mathbb C^m\\c_0=1}}
                \|\mathcal B_m^+c\|_{G_{\rm out}}^2
                            =\frac{N^2}{m}\qquad(1\le m\le N).
 \tag{36}
\]
Here \(\|z\|_G^2=z^*Gz\). Set \(y=U^{\mathsf T}c\).
Then \(c_0=\sum_k a_ky_k\), where
\(a_k=(U^{-1})_{k0}=(-1)^kQ^{k(k-1)/2}\) has modulus one.
Equation (35) makes the objective \(N^2\|y\|^2\).
Cauchy--Schwarz gives its minimum \(N^2/m\), attained at
\(y_k=\overline{a_k}/m\). This is the weighted returned-block
quadratic problem with one fixed endpoint coefficient; it is not
the whole source quartic.

There is an exact scalar linear-elimination consequence. Formulae
(30)--(31) give
\[
 ((\mathcal B_m^+)^{-1})_{00}
    =\frac1{\kappa N}\sum_{k=0}^{m-1}Q^{-k},\qquad
 \operatorname{Schur}_{00}\mathcal B_m^+
    =\frac{\kappa N}{\sum_{k=0}^{m-1}Q^{-k}}
                                    \quad(1\le m<N).
 \tag{37}
\]
Indeed the squared inverse-Pascal first-column phase times \(J^{-1}\)
is \(Q^{-k}\). For \(m<N\) the geometric sum is nonzero, so the
cofactor proves that the trailing principal submatrix is invertible;
eliminating those indices gives the displayed Schur complement.
Its modulus is \(N\sin(\pi/N)/\sin(\pi m/N)\), asymptotic to
\(N/m\) when \(m=o(N)\). At \(m=N\) that cofactor is zero and this
elimination is not available. This is a linear reduction of the
specified returned block, not an evaluation of a whole Conway
minimum or a closed knot scalar.

The ordinary cap is not a Hermitian dual merely by (35).
Inserting \(\mathcal Q_m^\pm\) into an internal network would
change it unless all complementary excursion blocks and the
original transported exterior were also retained.

## 7. Coverage, phases, and the original closing

[F] already proves the exact unique-path sweep coefficient and
its whole Hilbert--Schmidt Gaussian asymptotics. It also constructs
one nonzero coefficient between prepared product Gaussian vectors.
The present estimate instead controls every coherent endpoint
input, using its actual joint column Gram and the bounded prefix
observables (14). The single-crossing selected-filter method and
endpoint column rate were proved in [E]; no general novelty is
claimed for polynomial interpolation.
[L] already evaluates the actual long-transfer endpoint kernel,
its signed phases, factorial gauges and compensated Pascal limit.
The exact returned-block inverse and the incident metrics above
are additional source-specific consequences; the factorization
is not a positivity claim for the original complex scalar.

The width \(b\) and the crossing sweep are fixed. This proof does
not cover a growing number of heads, an arbitrary sequence of
crossing signs, repeated arbitrary sweeps, or a change of pairing
by a Conway quarter-turn. Such operations have their literal
matrices and currents; none is replaced by an endpoint projection.
The theorem is at the original complete root and asserts no
uniform moving-meridian or quantum-normal derivative estimate.

The original cups, caps, pivots, marks and framing factors remain
those of [P]. A subsequent prescribed closing may cancel a large
open packet. Neither the joint Gram lower bound nor its common
outgoing rate supplies a lower bound for that scalar, identifies
a selected geometric framing cycle, or proves a new knot-volume
or finite-exception statement.

## Complete chosen texts

All five complete matching texts were read. The new estimates are
proved above in the uniform physical metric.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| G, direct | [Actual physical crossing entries](research_full_physical_crossing_gaussian_packet.md), 306 lines | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| P, direct | [Original uniform physical source](research_conway_uniform_physical_quartic.md), 477 lines | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| E, direct and coverage | [Coherent single-crossing endpoint transport](research_coherent_endpoint_to_bulk_crossing_norm.md), 392 lines | a860255c704f55bf252ed2c77a7d463661f652550ff1f5fdeaedce90495b7a02 |
| F, direct and coverage | [Exact physical fan and its Gaussian packet](research_full_physical_fan_gaussian_packet.md), 501 lines | 1e89a7f8e4bf948fa8ffdd3e6314a01541af3177901747ece8274baf871dd83e |
| L, direct and coverage | [Actual long-transfer cross-collar kernel](research_actual_long_transfer_cross_collar_kernel.md), 454 lines | 4639b15a335a0d0813d30f0ee2e9f84b5fa15fce3ea93b34d05f181805a39d90 |

Only written mathematics, complete source reads and metadata hashes
were used. No mathematical program, numerical test, build, git
operation, prior-final edit or public-manuscript change was made.
