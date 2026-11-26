# A near-unit source bound for forests with an exact leaf reduction order

Private written proof, 16 November 2026.

A fixed closed forest which can be removed by the original zero and
unit leaf operations has a uniform near-unit charged upper bound.
The small charge defects produce low-degree coupons; their degree
and coefficient costs remain controlled through the whole prescribed
order. Zero-leaf steps retain one shared physical color across every
newly separated branch. Isolated vertices may have any fixed integer
power and are estimated using their original full Hermite trace.

This gives a source estimate for a specified class of reductions,
without positive intermediate geometry. It does not assert that
every empty-angle descendant has such an order, or that arbitrary
full endpoint coupons satisfy the required degree budget.

## 1. The exact source and a fixed reduction certificate

Let \(G=(V,E)\) be a fixed finite forest, all of whose vertices are
traced. There are no additional untraced kernel incidences. Fix signed
integer powers \(n_v\). At level \(N\ge2\), use the original full algebra
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\quad D=N-1,\quad
 \eta=(-1)^D,\quad m=\lfloor N/2\rfloor,
\]
\[
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad
 Te_j=e_{D-j},\qquad
 K_N(z,w)=\sum_{j=0}^D e_j(z)e_j(w).
 \tag{1}
\]
The original crossing \(R\), including its unit carrier, is retained.
For ordinary polynomial coupons \(P_v\), define
\[
 Z_{G,N}(\mathbf P)=
 \left(\prod_{v\in V}\phi_N^{(v)}\right)
 \left[\prod_v R(z_v)^{n_v}P_v(z_v)
                     \prod_{vw\in E}K_N(z_v,z_w)\right].
 \tag{2}
\]
The empty forest has source one.

A **reduction certificate** is a fixed sequence of the following
operations on the graph and its current powers, ending at the empty
forest:

* Remove an isolated vertex, with any current integer power.
* Remove a leaf \(v\) of current power \(\sigma=\pm1\), and subtract
  \(\sigma\) from the power of its neighbor \(w\).
* For a leaf \(v\) of current power zero, remove both \(v\) and its
  neighbor \(w\), and all incident edges. Other powers stay unchanged.

This is only a finite combinatorial hypothesis. Its graph and power
updates are independent of \(N\), of the charge coupons, and of the
physical colors later summed in the zero operation. It does not
assert a topological simplification of an unfilled exterior.

Write \(v_0=|V|\), and assume \(v_0\ge1\); the empty case is immediate.
Put
\[
 d=\max\{2,\max_{v\in V}\deg_G(v)\},\qquad
 B_G=v_0d^{v_0},\qquad
 n_*=\max_v|n_v|+v_0.
 \tag{3}
\]
All current powers in the certificate have absolute value at most
\(n_*\). Degrees in the graph do not increase.

For an ordinary polynomial \(P\) of degree \(k\), use
\[
 P(-2\cos t)=\sum_{j=0}^k p_j\cos(jt),\qquad
                       \|P\|_{\cos,1}=\sum_j|p_j|.
 \tag{4}
\]
This norm bounds \(\sup_{[-2,2]}|P|\) and is submultiplicative.

## 2. Statement and the elementary isolated estimate

Define, with their continuous values zero at \(x=0\),
\[
 g(x)=x\log2+2x\log\frac{e}{2x},\qquad
 h(x)=2x\log\frac{\pi e^2}{2x}.
 \tag{5}
\]
They are increasing for \(0\le x\le1/4\). Set
\[
 \Phi_G(\varepsilon)
   =v_0\left[g(B_G\varepsilon)
                       +(d-1)h(B_G\varepsilon)\right].
 \tag{6}
\]
In particular \(\Phi_G(\varepsilon)=O_G(\varepsilon\log(1/\varepsilon))\).

**Theorem.** Suppose \(G,\mathbf n\) have a reduction certificate.
There are constants \(C_{G,\mathbf n}\) and \(p_G\), independent of
the level and coupons, such that whenever
\[
 0\le\varepsilon\le\frac1{4B_G},\qquad
                       \deg P_v\le\varepsilon N,
 \tag{7}
\]
one has at both parities
\[
 \boxed{\quad
 |Z_{G,N}(\mathbf P)|
 \le C_{G,\mathbf n}N^{p_G}e^{N\Phi_G(\varepsilon)}
                            \prod_v\|P_v\|_{\cos,1}.
 \quad}                                                     \tag{8}
\]
One may take \(p_G=v_0(d+3)\). Consequently the actual near-unit
lattice coupons \(P_v=\mathcal C_{N,1-k_v/N}=T_{k_v}(-z/2)\),
\(0\le k_v\le\varepsilon N\), satisfy (8) without its final product.
If every \(k_v=o(N)\) uniformly, the source has subexponential upper
growth. At unit charge it has a polynomial upper bound. No lower
bound is asserted.

Here is the estimate needed at an isolated vertex. For every
ordinary \(P\) of degree \(k<N\) and every integer \(n\),
\[
                     |\phi_N(R^nP)|
               \le C(1+|n|)N^3\|P\|_{\cos,1}.             \tag{9}
\]
To verify it, the double nodes are
\(c_a=2\cos((2a+1)\pi/N)\), \(0\le a<m\), and the original trace is
\[
 \phi_N(F)=\eta\sum_{a<m}
       \{(4-c_a^2)F'(c_a)-c_aF(c_a)\}
                     +\mathbf1_{N\ {\rm odd}}F(-2).
 \tag{10}
\]
The original crossing has
\[
 |R(c_a)^n|=1,\qquad
 \frac{(R^n)'(c_a)}{R(c_a)^n}
           =\frac{in(D-2a)}{4\sin((2a+1)\pi/N)}.
 \tag{11}
\]
Since \(\sin(\pi/N)\ge2/N\),
\(|(R^n)'(c_a)|\le |n|N^2/8\).
The polynomial Markov inequality on \([-2,2]\) gives
\(\sup|P'|\le k^2\sup|P|/2\); it also holds for complex
coefficients by taking a real part with the phase of a derivative
at the point in question. Substitution into (10), with at most
\(N\) terms, proves (9). At the odd simple node the crossing value
also has modulus one. These identities include \(N=2\).
Thus the final isolated power need not belong to \(\{0,\pm1\}\).

## 3. One unit step and one zero step

Consider any intermediate forest with ordinary local coupons.
Suppose their total degree is at most \(K<N/2\), and each individual
degree is below \(m\). The latter will follow from (7) below.
In this section \(G,n_u\) denote this current graph and its current
powers. Put \(A_u=\|P_u\|_{\cos,1}\).

For a unit leaf \(v\) of power \(\sigma\), the exact charged leaf
theorem gives
\[
 T(R^\sigma P_v)=R^{-\sigma}U_\sigma P_v,\qquad
 U_\sigma P=\kappa^\sigma T(R^{-\sigma}TP).
 \tag{12}
\]
It removes that leaf and changes the neighboring coupon to
\(P_wU_\sigma P_v\). Its degree is at most \(k_w+k_v\).
The low divided-difference bound and the explicit cosine conversion
give
\[
 \|U_\sigma P_v\|_{\cos,1}
       \le2N^3 e^{Ng(k_v/N)}A_v.
 \tag{13}
\]
For completeness, the bound for a general \(P_v\) follows from
\(\|P_v\|_{\rm New,1}\le(k_v+1)(k_v+2)A_v\) and the conversion
formula in the pinned leaf theorem. It is not restricted to a
single cosine. The new neighboring coupon has norm at most
\(2N^3e^{Ng(k_v/N)}A_vA_w\); thus the total norm cost, relative
to \(\prod_u A_u\), is at most \(2N^3e^{Ng(k_v/N)}\).

For a zero leaf \(v\) with neighbor \(w\), write
\(P_v=\sum_{s\le k_v}p_s e_s\). Its exact evaluation coefficients
from the same source are
\[
 \beta_a=\sum_{s=a}^{k_v}p_s b_{sa},\qquad
 \sum_{a=0}^{k_v}|\beta_a|
       \le2(k_v+1)\|P_v\|_{\rm New,1}
       \le4N^3 A_v.
 \tag{14}
\]
After both traces have been taken, the full source is exactly
\[
 \sum_{a=0}^{k_v}
       \beta_a R(c_a)^{n_w}P_w(c_a)\,
 Z_{G\setminus\{v,w\},N}
 \left(\left\{
 P_u(z)F_{a,N}(z)\ \text{if }u\in N_G(w)\setminus\{v\};
 \quad P_u(z)\ \text{otherwise}
 \right\}\right),
 \tag{15}
\]
where \(F_{a,N}(z)=K_N(c_a,z)\). Current surviving powers are
unchanged. All original remaining edges stay in this source.
There is one and the same \(a\) in every newly inserted row in
each term of (15), including across disconnected branches.

The positive physical-row law proves
\[
 \deg F_{a,N}=a,\qquad
 \|F_{a,N}\|_{\cos,1}=F_{a,N}(-2)=M_{a,N},\qquad
 M_{a,N}\le N e^{Nh(K/N)}
                  \quad(0\le a\le k_v\le K<N/2).
 \tag{16}
\]
The bound at \(a=0\) uses \(M_{0,N}=1\).
Also \(|P_w(c_a)|\le A_w\), and the crossing in (15) has unit
modulus. There are at most \(d-1\) new row insertions.
Applying a uniform bound to the smaller sources in (15) and then
using (14) gives the one-step norm cost
\[
                   4N^{d+2}e^{N(d-1)h(K/N)}.              \tag{17}
\]
No remaining trace has been replaced by its physical supremum.
The only evaluated factors are exactly those in (15); the bound
for each smaller source is applied with its full coupled graph.

## 4. Degree propagation and completion of the estimate

Let \(K\) denote the sum of current coupon degrees in any branch
of the finite expansion. A unit step cannot increase \(K\).
An isolated removal decreases it. In a zero step, (15) gives
\[
 K_{\rm new}\le K-k_v-k_w+(\deg(w)-1)k_v\le dK.
 \tag{18}
\]
Initially \(K\le v_0\varepsilon N\), and there are at most \(v_0\)
steps. Therefore every branch at every time has
\[
                       K\le B_G\varepsilon N\le N/4.
 \tag{19}
\]
Because its degrees are integers, every individual degree is
strictly below \(m\), including at \(N=2,3\).
All uses of the radical and low-degree identities are justified
before quotient reduction. Nothing estimates a coupon degree
only after discarding a multiple of \(P_N\).

Apply the exact steps in the prescribed order. At every zero step
use the same bound for all its actual colors \(a\); the remaining
graph and powers, hence the rest of the certificate, do not depend
on that color. This is an induction on the certificate, and
justifies summing the coefficients in (14) without declaring the
branches independently optimized. All crossing phases remain in
the exact identity (15) until the upper estimate is taken.

By monotonicity of \(g,h\), each unit or zero exponential cost in
(13), (17) is bounded using \(K/N\le B_G\varepsilon\).
Multiplying at most \(v_0\) costs bounds their combined exponent
by \(N\Phi_G(\varepsilon)\). Equations (9), (13), and (17)
contribute at most \(N^{v_0(d+3)}\), after enlarging a constant
depending only on \(G,\mathbf n\). Their coupon norm factors
multiply to the original \(\prod_v A_v\).
If one \(A_v\) is zero, the source is zero; otherwise one can
normalize the initial coupons to norm one and restore this
product by multilinearity. This proves (8).

The proof also permits a specified finite sum of products of
local low-degree coupons: sum the resulting bounds with the
absolute coefficient weights of that decomposition. It does
not give such a decomposition with controlled cost for an
arbitrary joint spectator.

## 5. Scope and direct sources

The complete reduction certificate is essential. No claim is made
that terminal pruning removes every short component, or every
connected component with an empty weak-angle fiber. In particular
remaining branching contractions can be outside this class.
The theorem controls the actual closed source and can be applied
component by component when the inserted source really factors.
It does not assign a zero rate to a disconnected global fiber.

Full microscopic endpoint coupons \(K_N(2\cosh(\alpha/N),z)\),
partial high-band coupons, and ordinary complete-boundary kernels
generally have degree comparable to \(N\). They are not covered by
(7) without a separate source-preserving reduction. Untraced
boundary data cannot simply be replaced by a local low-degree
coupon in this theorem.

The earlier exact leaf theorem supplies each local identity and
cost. The additional statement here is the uniform completion
through an arbitrary fixed certified forest, with the shared
color sums and degree growth controlled and with arbitrary final
isolated powers. This supplies an upper bound only, not a
geometric coefficient, volume identity, or treatment of every
core occurring in a padding fiber.

All four complete direct sources were read at the following versions,
their used implications checked, and hashes verified:

* [Charged low-degree leaf reductions](research_low_degree_charged_leaf_reduction.md),
  SHA256 80df78ceafaa97182aebc6831651921f7f8040e1356ee07a3d0d3fbadd02846a:
  exact unit and zero operations, degree flags, full normals,
  and quantitative cosine conversion.
* [Positive physical-row charge transport](research_physical_row_charge_transport.md),
  SHA256 d09d5c669848f0389504cea613244570eca18be03f2b608a359773e423e97040:
  exact physical row, its cosine coefficient norm, support,
  and the coefficient-mass function \(h\).
* [Original arbitrary-power source compilation](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f:
  original full-algebra crossing values and every double-node
  normal for arbitrary signed powers.
* [Original full radical and trace](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  the local double-node trace, original normalization, and
  the distinct odd simple node.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Existing private notes and public files were unchanged.
