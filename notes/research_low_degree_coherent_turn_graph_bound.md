# Low-degree physical jets and coherent turn graphs of half-charge coupons

Private written proof, 17 November 2026.

The original turn has an exponential all-input physical norm.
Its restriction to the ordinary outside polynomials of the actual
half-charge coupons has a different bound. Their degrees are at most
half the level. In that range the original Newton coefficients are
obtained from physical values, and at even levels one central normal,
by an explicit matrix with polynomial entries. The turn pairing is
its bilinear Gram matrix. This pays every internal turn of a fixed
tensor graph of those coupons before absolute values are taken.

The coefficient pairing and the below-middle radical reduction are
already part of the original Newton calculus and the low-degree leaf
reduction. The addition here is the explicit middle-coefficient
adapter at both parities, and the resulting independent-slot graph
bound, including its remaining physical Gaussian losses and original
exterior row. No comparison with a filled parent action or selected
scalar lower bound is asserted.

## 1. The original pairing and its short physical data

Put \(N\ge2\), \(D=N-1\), \(m=\lfloor N/2\rfloor\),
\(\theta=\pi/N\), and
\[
 c_a=2\cos((2a+1)\theta),\quad
 s_j=2\sin(j\theta),\quad S_j=\prod_{b=1}^j s_b,\quad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z).
 \tag{1}
\]
The full algebra and original operations of [C] are
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\quad P_N=2T_N(z/2)+2,
 \qquad \phi(e_i e_j)=\delta_{i+j,D},\quad Te_j=e_{D-j}.
 \tag{2}
\]
For \(f\in\mathcal A_N\), let \(a_r(f)\) be its canonical
Newton coefficient. Thus
\[
 \phi(f\,Tg)=\sum_{r=0}^D a_r(f)a_r(g).
 \tag{3}
\]
This is the actual turn pairing. Ordinary multiplication followed
by \(\phi\) is a different pairing.

Use the following vector of short physical data:
\[
 u_N(f)=
 \begin{cases}
 (f(c_0),\ldots,f(c_{m-1}),f(-2))^t,&N=2m+1,\\
 (f(c_0),\ldots,f(c_J),f'(c_J))^t,&N=2m,\ J=m-1.
 \end{cases}
 \tag{4}
\]
The derivative in the second line is the ordinary spectral
derivative. The node \(c_J=-2\cos\theta\) is double.
At odd levels \(-2\) is simple and has no normal.
Every entry of (4) is defined for the original full Hermite class.

For \(0\le r<m\), [H] gives, for arbitrary \(f\in\mathcal A_N\),
\[
 a_r(f)=\sum_{a=0}^r b_{ra}f(c_a),\qquad
 b_{ra}=(-1)^{r+a}
 \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}},\qquad |b_{ra}|\le2.
 \tag{5}
\]
All denominators here are nonzero. Missing entries of this row are
zero. In particular (5) is an identity for an arbitrary exterior
class, not only for a polynomial of degree below \(m\).

**Proposition 1.** The remaining coefficient is exactly
\[
 a_m(f)=f(-2)+
       2\sum_{a<m}(-1)^{m+a}\sin((2a+1)\theta/2)f(c_a),
                   \qquad N=2m+1,
 \tag{6}
\]
and, at \(N=2m\),
\[
 \begin{split}
 a_m(f)={}&
 \sum_{a<J}\frac{4(-1)^{m+a}\sin((2a+1)\theta)}
                         {c_a-c_J}\,f(c_a)\\
 &-\cot\theta\,f(c_J)-4\sin\theta\,f'(c_J).
 \end{split}
 \tag{7}
\]
These formulas hold for every full class \(f\).
Consequently a real matrix \(B_N\), of size \(m+1\), satisfies
\[
 (a_0(f),\ldots,a_m(f))^t=B_Nu_N(f).
 \tag{8}
\]
At odd levels every entry of \(B_N\) has modulus at most \(2\);
at even levels every entry has modulus at most \(C N^2\).

**Proof.** At odd levels put
\[
 Q_o(z)=U_m(z/2)-U_{m-1}(z/2),\qquad
 e_m=(-1)^mQ_o/N.
 \tag{9}
\]
The first \(m+1\) Newton nodes are precisely the \(m\) double
nodes and \(-2\), all distinct. The monic node polynomial is
\((z+2)Q_o(z)\). The leading coefficient of their degree-\(m\)
interpolant is therefore the sum of its nodal values divided by
the derivatives of this node polynomial. Multiplying that leading
coefficient by \((-1)^mN\) gives \(a_m(f)\); later Newton
terms vanish at all these nodes.

For \(z=2\cos t\),
\[
 Q_o(z)=\frac{\cos(Nt/2)}{\cos(t/2)}.
 \]
At \(t_a=(2a+1)\theta\), direct differentiation gives
\[
 Q_o'(c_a)=\frac{N(-1)^a}{4\sin t_a\cos(t_a/2)},\qquad
 Q_o(-2)=(-1)^mN.
 \]
The resulting weights are exactly (6).

At even levels let \(Q_e(z)=2T_m(z/2)\), a monic polynomial,
and let \(A=e_{m-1}\). Direct products in (1) give
\[
 e_m=\frac{(-1)^m}{2N}Q_e,\qquad
 A(z)=\frac{(-1)^{m-1}Q_e(z)}{m(z-c_J)},\qquad
 A(c_J)=\frac1{\sin\theta}.
 \tag{10}
\]
By (2), \(a_m(f)=\phi(Af)\). The original trace is
\[
 \phi(h)=\eta\sum_{a<m}\{(4-c_a^2)h'(c_a)-c_ah(c_a)\}
              +\mathbf1_{\mathrm{odd}}h(-2),\quad
 \eta=(-1)^D.
 \tag{11}
\]
The value of \(A\) vanishes at every \(c_a\) except \(c_J\).
For \(a<J\), (10) gives
\[
 A'(c_a)=
 \frac{(-1)^{m+a-1}}{\sin t_a(c_a-c_J)}.
 \]
The Chebyshev equation gives
\[
 A'(c_J)=\frac{c_J}{2(4-c_J^2)\sin\theta}.
 \]
Substitution in (11), with \(\eta=-1\), gives (7).
This retains the central normal, rather than replacing it by a
distinct-node value. It also proves the formula for arbitrary
classes and at \(N=2\), when the first sum is empty and
\(a_1(f)=-4f'(0)\).

Finally
\[
 |c_a-c_J|\ge16(J-a)^2/N^2,\qquad a<J.
 \]
Indeed, with \(k=J-a\), the difference is
\(4\sin(k\theta)\sin((k+1)\theta)\), and both sine arguments
lie in \([0,\pi/2]\). Apply \(\sin x\ge2x/\pi\).
The other factors in (7) are
bounded by \(4\), \(1/\sin\theta\le N/2\), or \(4\).
The stated polynomial entry bound follows. \(\square\)

The map (8) is invertible on \(\mathbb C[z]_{\le m}\):
the data (4) determine a degree-\(m\) polynomial, by ordinary
interpolation at odd levels and by confluent interpolation at even
levels. No polynomial bound for \(B_N^{-1}\) is needed or claimed.

## 2. The coherent Gram and an arbitrary one-sided exterior

Write \(\mathcal P_m=\mathbb C[z]_{\le m}\) and define
\[
                    \Gamma_N=B_N^tB_N .
 \tag{12}
\]
For \(p\in\mathcal P_m\) and arbitrary \(E\in\mathcal A_N\),
(3) and (8) imply the exact original identity
\[
 \boxed{\quad
          \phi(E\,Tp)=u_N(E)^t\Gamma_Nu_N(p).
       \quad}
 \tag{13}
\]
All coefficients \(a_r(p)\) with \(r>m\) vanish. This explains
why only the short data of the possibly unrestricted exterior
are used. At odd levels no exterior first normal survives.
At even levels precisely the central first normal may survive.
All other normal terms cancel in the original trace.

In particular, for two degree-\(m\) polynomials the actual bilinear
turn is (12). With complex conjugation in the first argument,
\(\phi(\overline p\,Tp)=\sum_{r\le m}|a_r(p)|^2\);
thus \(\Gamma_N\) is positive definite. This does not make the
unconjugated original closing positive.
Its entries and operator norm have polynomial upper bounds:
\[
 \max_{i,j}|(\Gamma_N)_{ij}|\le
 \begin{cases}4(m+1),&N\text{ odd},\\ C N^5,&N\text{ even}.
 \end{cases}
 \tag{14}
\]
No uniform lower eigenvalue bound is inferred.

If \(\deg p<m\), its middle coefficient is zero. Then (13)
reduces to the particularly simple value-only formula
\[
 \phi(E\,Tp)=\sum_{a,b<m}W_{ab}E(c_a)p(c_b),\qquad
 W_{ab}=\sum_{r<m}b_{ra}b_{rb},\qquad |W_{ab}|\le4m.
 \tag{15}
\]
This is the original radical consumption of the normal.
It applies at both parities, with no derivative or odd simple
value of \(E\).

A fixed signed edge crossing can be retained as well. Define
\(U_{k,N}\) by \(u_N(R^k f)=U_{k,N}u_N(f)\).
At odd levels it is diagonal, with entries \(R(c_a)^k\),
including the simple node. At even levels its value rows are
the same diagonal rows, and its last row is
\[
 (R^kf)'(c_J)=R(c_J)^k
       \{f'(c_J)+k\alpha_J f(c_J)\},\qquad
 \alpha_J=\frac{i}{4\sin\theta}.
 \tag{15a}
\]
The original crossing values have modulus one. Thus \(U_{k,N}\)
and its inverse have polynomial bounds for fixed signed \(k\).
In the stated left-to-right convention,
\[
 \phi(R^kp\,Tq)=u_N(p)^t U_{k,N}^t\Gamma_Nu_N(q),
                  \qquad p,q\in\mathcal P_m .
 \tag{15b}
\]
The matrix is no longer asserted positive. Equation (15b) is a
specified edge insertion; it does not commute \(R^k\) through
the turn or declare \(R^kp\) an ordinary degree-\(m\) polynomial.

The identities hold coefficientwise with arbitrary joint ordinary
spectator parameters and with all their fixed derivatives.
For example \(E(z,\lambda)\) need not factor in \(z,\lambda\).
A different situation is an extra factor depending jointly on
both independent incidences before a turn contraction. It cannot
be moved through the kernel by (13); if present, it must be kept
inside the relevant tensor and satisfy the degree hypotheses below.

There is also an actual upper bound on the turned polynomial itself.
For \(\deg p\le m\),
\[
 Tp=\sum_{r<m}a_r(p)e_{D-r}+a_m(p)e_{D-m}.
 \tag{16}
\]
The radical polynomials in the sum have real-interval norm at most
\(\sqrt{N-1}\) by [H]. At odd levels
\(e_{D-m}=e_m=(-1)^mQ_o/N\) has norm at most one. At even
levels (10) and the mean-value bound
\(\sup_{[-2,2]}|Q_e'|\le m^2\) give
\(\sup|e_{D-m}|=\sup|A|\le m\).
Equations (8), (14), and ordinary polynomial derivative bounds
therefore give, for each fixed \(k\),
\[
 \sup_{[-2,2]}|\partial_z^k Tp|
       \le C_kN^{b_k}\max_i|u_N(p)_i|.
 \tag{17}
\]
This is a restriction on an actual source class, not a new norm
chosen to make the full turn unitary.

## 3. Independent-slot tensor graphs

Let a fixed finite graph have a polynomial tensor \(P_{v,N}\) at
each vertex, one independent ordinary variable for each incident
port, and possibly additional unpaired ordinary ports and
parameters. Assume the degree in each port to be paired is at
most \(m\). An edge pairs its two ports by the original operation
\[
             (f,g)\longmapsto\phi(f\,Tg).
 \tag{18}
\]
Equivalently it uses \(K_T\) and the two original traces of [C].
Loops join two distinct ports of one tensor; parallel edges are
allowed. No port variable is identified with another before its
specified pairing.

Index the \(m+1\) functionals in (4) by \(i\), writing them
\(\mathcal E_i\). Thus all are values except for the one even
central derivative. For a choice \(\boldsymbol i\) on all paired
ports let
\[
 P_{v,N}[\boldsymbol i_v]
       =\left(\prod_{h\text{ paired at }v}\mathcal E_{i_h}^{(h)}
                                                    \right)P_{v,N}.
 \]
The exact contracted ordinary tensor is
\[
 \boxed{\quad
 Z_N=
 \sum_{\boldsymbol i}
     \prod_{\{h,h'\}\text{ edge}}\Gamma_N(i_h,i_{h'})
     \prod_v P_{v,N}[\boldsymbol i_v].
       \quad}
 \tag{19}
\]
Proof: expand each port in its Newton basis. Every edge contracts
equal coefficients by (3), with no phase or scalar removed.
Apply (8) in each port. The maps commute because the port variables
are independent. This also proves (19) for loops and arbitrary
joint dependence among a tensor's other variables.

For an oriented edge carrying the literal contraction
\(\phi(R^{k_e}p\,Tq)\), replace its factor \(\Gamma_N\) in
(19) by \(U_{k_e,N}^t\Gamma_N\), with \(p\) on the left.
Equation (15b) proves this version with every scalar phase and
central normal retained. Fixed signed edge powers only change
the polynomial constants below.

There are polynomially many summands for a fixed graph, and all
edge weights have polynomial size by (14). Hence
\[
 |\partial^\alpha Z_N|
 \le C_\alpha N^{b_\alpha}
       \prod_v\max_{\boldsymbol i_v,\ \alpha_v}
           |\partial^{\alpha_v}P_{v,N}[\boldsymbol i_v]|,
 \tag{20}
\]
with the finite allocations of the specified exterior derivatives
understood. The sharper version is the actual finite sum (19).
Contraction does not raise the degree in any remaining independent
port. It therefore applies simultaneously to every edge of the
fixed graph, not just along a tree or a chosen elimination order.

An arbitrary joint co-source on the remaining ports is retained
after (19). A new multiplication or branching identification in a
paired port can raise its degree above \(m\). In that case this
theorem is not applied to the enlarged tensor without checking
the degree again. In particular, (19) is not an all-input estimate
for a kernel with an arbitrary two-incidence insertion.

## 4. Actual A/B coupon graphs and the remaining Gaussian loss

Use the original source coupons of [A, B],
\[
 \mathcal C_{r,n,N}(\boldsymbol\zeta)
   =\phi[R^n e_{D-m}\prod_{i=1}^rK_N(\,\cdot\,,\zeta_i)],
 \qquad
 \mathcal D_{r,n,N}(\boldsymbol\zeta)
   =\phi[R^n e_{D-m+1}\prod_{i=1}^rK_N(\,\cdot\,,\zeta_i)].
 \tag{21}
\]
Here \(r\ge1\) and \(n\in\mathbb Z\) are fixed.
Their degrees in every outside port are at most \(m\) and
\(m-1\), respectively. For \(r+|n|>1\), let \(M_{r,n}\)
be their proved complete half-charge action in [A, B].
Both have the full physical mixed-jet bound
\[
 |\partial^\alpha P_{v,N}(c_{\boldsymbol a})|
 \le C_\alpha N^{b_\alpha}
    \exp\left\{N M_v-c_vN
       \sum_{h:\alpha_h=0}g_{a_h}\right\},
 \quad g_a=1-\cos\tau_a,\quad
 \tau_a=\arccos(-c_a/2).
 \tag{22}
\]
The ordinary derivative in a hit slot loses only that slot's
Gaussian. It does not remove the losses at other ports.

Apply (19) to any fixed graph of these actual coupons.
For every fixed multi-index \(\alpha\) on its remaining distinct
ordinary ports, (22) and (14) give
\[
 \boxed{\quad
 |\partial^\alpha Z_N(c_{\boldsymbol a})|
 \le C_\alpha N^{b_\alpha}
   \exp\left\{N\sum_v M_v-cN
            \sum_{h\text{ unpaired}:\alpha_h=0}g_{a_h}\right\}.
       \quad}
 \tag{23}
\]
Here \(c>0\) can be any sufficiently small common lower bound
for the finitely many constants in (22).
All internally sampled values and central normals were summed
in (19). Their nonnegative Gaussian losses can be dropped.
The normal required at an even internal port is among the
mixed jets already covered by (22). A B-coupon has zero middle
Newton coefficient, so an untwisted edge incident to it needs only
the value-only contraction (15). The same simplification holds
for \(\phi(R^kp\,Tq)\) when the B-coupon is \(q\). In the other
orientation the full adapter (15b) is retained; no crossing is
commuted through \(T\).

The exceptional \((r,n)=(1,0)\) can also be included at rate zero:
its two coupons are exactly \(e_m\) and \(e_{m-1}\).
At odd levels \(e_m\) vanishes at all double nodes and is one
at the simple node; \(e_{m-1}\) can be nonzero only at the last
double and simple nodes. At even levels \(e_m\) vanishes at all
physical values, and \(e_{m-1}\) can be nonzero only at \(c_J\).
These nonzero values lie at \(\tau\le2\pi/N\); the real norms
and all fixed ordinary derivatives are polynomial, by (9),
(10), [H], or polynomial differentiation. Thus (22) holds
for these exceptions as well, with \(M_v=0\).
No saddle or nonzero Gaussian is assigned to them.

This proves a coherent polynomial turn cost on the stated coupon
graphs. The exponential cost is \(\sum_vM_v\), with no additional
\(M_\infty\) per internal turn. It is an upper bound, not the
action or a lower bound of the joined source.

## 5. The original joint exterior trace

After internal contractions, identify remaining outside slots
with retained traced variables \(z_1,\ldots,z_s\).
Let \(q_j\) count the slots identified with \(z_j\), including
repetitions. Denote the resulting polynomial by \(F_N\).
For a full physical trace jet \(\alpha_j\in\{0,1\}\),
the repeated-slot chain rule and (23) give
\[
 |\partial^\alpha F_N(c_{\boldsymbol a})|
 \le CN^b\exp\left\{N\sum_vM_v
            -cN\sum_j(q_j-\alpha_j)_+g_{a_j}\right\}.
 \tag{24}
\]
A derivative in \(z_j\) hits at most one of its \(q_j\) slots.
All mixed derivatives in different retained variables are included.

Let \(E_N\) be any specified ordinary joint exterior, holomorphic
at all physical nodes, and let \(p_j\) be fixed signed integers.
With \(\nu_a=\operatorname{mult}_{c_a}P_N\), define
\[
 \|E_N\|_{N,c,\boldsymbol q}
 =\max_{\boldsymbol a,\ 0\le\beta_j<\nu_{a_j}}
 |\partial^\beta E_N(c_{\boldsymbol a})|
 \exp\left\{-cN\sum_j(q_j-1+\beta_j)_+g_{a_j}\right\}.
 \tag{25}
\]
The original full closing satisfies
\[
 \boxed{\quad
 \left|\phi^{\otimes s}
    \left[E_N\prod_jR(z_j)^{p_j}F_N\right]\right|
 \le CN^b e^{N\sum_vM_v}\|E_N\|_{N,c,\boldsymbol q}.
       \quad}
 \tag{26}
\]
Indeed expand the original trace (11) in every variable and
then apply the product rule. If \(\beta_j\) derivatives hit
the exterior, at most \(1-\beta_j\) can hit \(F_N\).
Its loss in (24) is therefore at least
\((q_j-1+\beta_j)_+g_{a_j}\). The actual crossing values
have modulus one. Their first normals have polynomial cost,
since [C] gives
\[
 \frac{R'(c_a)}{R(c_a)}
       =\frac{i(D-2a)}{4\sin((2a+1)\theta)}.
 \]
There is no derivative at an odd simple node. The finite number
of physical sums and all factors in (11) cost only a polynomial.
This proves (26), including arbitrary mixed exterior normals.

The exterior norm in (25) has not been estimated by a geometric
parent action. Nor does (26) imply a relative scalar estimate
when the original terms cancel. The local period ratio of A/B
coupons supplies a selected saddle coordinate at complete color;
it is not needed for this exact graph contraction and is not
substituted for a joint covariance or source coefficient.

## Complete direct sources and coverage

All four complete direct texts were read in the active source
review sequence, retained unchanged, and their used implications
checked at the following renewed pins:

* [C] [Original source compiler](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f:
  original turn, bilinear trace, free-port convention and signed
  crossing jets.
* [H] [High Newton radical contraction](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  exact physical coefficient rows, their bound \(2\), and original
  radical real-period bounds.
* [A] [Multi-leg half-charge source](research_multileg_half_charge_source_bound.md),
  SHA256 df85063947dc52c876d1cb810208e4da725517b7556661e3ddb21a3de7f0f8d2:
  actual A-coupon outside degrees, whole-source action bounds and
  the unhit-slot mixed-jet estimate.
* [B] [Mixed low/radical coupons](research_mixed_low_radical_coupon_trace_bound.md),
  SHA256 5e347ad0b8fb1a31415344eac6c2c3dea3b4b4d8b39dc0d76b1eb47a62d382e6:
  actual B-coupon degree, sharp action and mixed jets, including
  the exceptional one-port source.

Coverage antecedents are the positive Newton coefficient pairing,
the low-degree charged-leaf reductions, and the product/full-trace
coupon estimate. The present graph bound is compatible with the
sharp exponential norm of the unrestricted turn kernel: it uses
the specified degree restriction before taking absolute values.
Only written mathematics and source reads were used. Frozen
source files and public manuscripts are unchanged.
