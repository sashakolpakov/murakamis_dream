# Exact charged leaf reductions with a low-degree budget

Private written proof, 16 November 2026.

The original zero and unit leaf reductions extend to polynomial
charge coupons of degree below half the level. A unit leaf passes
a polynomial of the same degree to its neighbor and changes that
neighbor's crossing power by one. A zero leaf gives an exact small
physical-color sum. These statements retain the original full
closing functional and every shared neighboring factor.

The quantitative consequence is a small exponential cost on a
near-unit lattice-charge window, not a polynomial bound on a window
of fixed positive width. No angle fiber, positive descendant, or
filled-source rate estimate is assumed or obtained.

## 1. Original algebra and the low-degree flag

Put
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 q=e^{\pi i/N},\quad \kappa=q^{D^2/2},\quad \eta=(-1)^D,
\]
\[
 s_j=2\sin(\pi j/N),\quad S_j=\prod_{h=1}^j s_h,\quad S_0=1,\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z).
 \tag{1}
\]
Use the original algebra and trace
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{2}
\]
The physical turn is \(Te_j=e_{D-j}\), with reversal matrix \(J\)
in this basis. Multiplication by the original positive crossing
\(R\) has Newton matrix
\[
 M_{ij}=\kappa(-1)^i q^{i(j+1)}
                  \frac{S_i}{S_jS_{i-j}}\quad(i\ge j).
 \tag{3}
\]
The negative crossing has the coefficient-conjugate matrix.
The exact turn/crossing relation, with multiplication operators
understood, is
\[
 T R^\sigma T=\kappa^\sigma R^{-\sigma}T R^{-\sigma},
                       \qquad \sigma\in\{1,-1\}.
 \tag{4}
\]
This is the full-algebra relation from the degree-two source
theorem, not an identity obtained after dropping nilpotents.

Fix \(0\le k<m\), and write
\[
 V_k=\operatorname{span}\{e_0,\ldots,e_k\}
       =\mathbb C[z]_{\le k},\qquad
 I_k=TV_k=\operatorname{span}\{e_{D-k},\ldots,e_D\}.
 \tag{5}
\]
The Newton recurrence
\[
 ze_j=c_je_j-s_{j+1}^2e_{j+1}
 \tag{6}
\]
has its last raised term zero modulo \(P_N\). Hence every terminal
Newton flag, and in particular \(I_k\), is an ideal. Since
\(k<m\), it lies in the physical radical and \(I_k^2=0\).
At odd levels this excludes the middle polynomial which is
nonzero at the simple node \(-2\).

For \(P=\sum_{s=0}^k p_s e_s\), set
\(\|P\|_{\rm New,1}=\sum_s|p_s|\).
All identities below also hold with ordinary free-boundary
polynomials as coefficients. A norm estimate with such coefficients
uses their supremum on the specified parameter set.

## 2. Unit leaves and a triangular coupon map

Define on \(V_k\)
\[
             U_\sigma P=\kappa^\sigma T(R^{-\sigma}TP).
 \tag{7}
\]

**Theorem 1.** For every \(P\in V_k\),
\[
 T(R^\sigma P)=R^{-\sigma}U_\sigma P,\qquad
 U_\sigma P\in V_k,\qquad U_\sigma1=1,
 \tag{8}
\]
and
\[
 [e_r]U_\sigma P
   =\sum_{s=r}^k p_s(-1)^s q^{-\sigma s(r+1)}
                         \frac{S_s}{S_rS_{s-r}},
 \qquad
 \|U_\sigma P\|_{\rm New,1}
             \le2^k\|P\|_{\rm New,1}.
 \tag{9}
\]

*Proof.* Apply (4) to \(TP\), using \(T^2=1\), to obtain (8).
Multiplication by \(R^{-\sigma}\) preserves the ideal \(I_k\);
the final turn therefore returns to \(V_k\).
For the coefficient formula, Frobenius self-adjointness of
multiplication gives \(JM^{-\sigma}J=(M^{-\sigma})^{\mathsf T}\).
Consequently the matrix of \(U_\sigma\) is
\(\kappa^\sigma(M^{-\sigma})^{\mathsf T}\), which gives (9)
from (3). Its zeroth column is the unit column.

The factorial quotient in (9) has modulus at most
\(\binom{s}{r}\). Indeed it differs by a unit phase from the
Gaussian binomial polynomial \({s\brack r}_{q^2}\). The latter
has nonnegative integer coefficients whose sum is
\(\binom{s}{r}\), as follows by its finite Pascal recurrence.
Evaluation on the unit circle proves the bound. Thus
\[
 \sum_{r=0}^k|[e_r]U_\sigma P|
 \le\sum_{s=0}^k|p_s|\sum_{r=0}^s\binom sr
 \le2^k\sum_s|p_s|.
 \tag{10}
\]
All factorial indices are less than \(N\), so this argument
introduces no singular root-of-unity specialization. \(\square\)

For the actual kernel \(K_N(z,x)=\sum_j e_j(z)e_j(x)\), the
leaf trace is exactly
\[
 \phi_N^{(z)}\!\left[R(z)^\sigma P(z)K_N(z,x)\right]
       =T(R^\sigma P)(x).
 \tag{11}
\]
If \(x\) is a traced neighbor with power \(n\), equations
(8)--(11) remove the leaf, replace \(n\) by \(n-\sigma\), and
insert \(U_\sigma P(x)\). Every other factor at that neighbor,
including its other edge kernels and any joint spectator,
remains in its original trace. There is no additional scalar.
In particular \(P=1\) recovers \(T(R^\sigma)=R^{-\sigma}\).

If \(x\) is an ordinary free variable, the right side of (8)
must first be taken in its canonical degree-less-than-\(N\)
representative. That representative equals (11) as an ordinary
polynomial. Only then may it be multiplied by other factors
or identified with another free incidence. The unreduced product
\(R^{-\sigma}U_\sigma P\) is not asserted to equal (11)
away from the physical spectrum.

For a joint insertion \(P(z;x,\mathbf u)\) of degree at most
\(k\) in the leaf variable, expand in \(e_s(z)\) first.
Apply (11) coefficientwise and retain every coefficient
polynomial in \(x,\mathbf u\). The transmitted coupon degree is at
most \(k\) in its independent incidence variable; after boundary
identification it adds to any degree already in those coefficients.
No shared spectator is factored or discarded.

## 3. Zero leaves, shared-neighbor annihilation, and isolated traces

The exact radical weights are
\[
 b_{sa}=(-1)^{s+a}
       \frac{s_{2a+1}S_s^2}{S_{s-a}S_{s+a+1}}
 \quad(0\le a\le s<m),\qquad |b_{sa}|\le2.
 \tag{12}
\]
The original full normal gives
\(\phi_N(e_{D-s}F)=\sum_{a\le s}b_{sa}F(c_a)\).
Therefore a zero leaf with coupon \(P\) transmits \(TP\), and
its traced neighbor satisfies the exact identity
\[
 \boxed{\quad
 \phi_N((TP)F)
       =\sum_{a=0}^k\beta_a(P)F(c_a),\qquad
 \beta_a(P)=\sum_{s=a}^k p_s b_{sa},\qquad
 \sum_a|\beta_a(P)|\le2(k+1)\|P\|_{\rm New,1}.
 \quad}
 \tag{13}
\]
Here \(F\) is the entire remaining neighbor factor, including its
crossing, charge, every incident edge, and its joint spectator.
Thus the other edges become \(K_N(c_a,z_w)\); they do not vanish
from the source. The neighbor's normal has been consumed by the
radical insertion in exactly the original trace formula.
The odd simple-node contribution is zero.
If the leaf coefficients themselves depend on the neighboring
variable, retain that dependence before taking the neighbor trace:
the right side is
\(\sum_{s,a}b_{sa}p_s(c_a;\mathbf u)F(c_a;\mathbf u)\).
No coefficient is moved past a trace in its own variable.
For \(N=2\) the only allowed \(k\) is zero, and (12)--(13)
reduce directly to \(b_{00}=1\), so both parities and all
levels are included.

For the uncharged zero leaf \(P=1\), (13) reads
\[
 \phi_N(e_D R^n A)=\kappa^n A(c_0),\qquad K_N(c_0,z)=1.
 \tag{14}
\]
It removes the neighbor's incident kernel factors after their
actual evaluation. Any additional spectator is still evaluated
at \(c_0\). This is the special top-mode rule; the other colors
in (13) retain their nonconstant row kernels.

If two zero-power leaves with degree budgets \(k_1,k_2<m\)
meet the same traced neighbor, their transmitted factors lie
in the square-zero radical. Their product, and hence the
whole source, is zero. The conclusion also holds for a joint
spectator of those two leaf variables with the stated separate
degree bounds: expand both Newton coordinates, and every
term has a product \(e_{D-r}e_{D-s}=0\) at the neighbor.
All other shared factors can remain arbitrary. This claim
requires a traced or canonically reduced neighbor; the
corresponding ordinary product at an unreduced free variable
need not vanish.

An isolated traced component with coupon \(P\in V_k\) obeys
\[
 \phi_N(P)=0,\qquad
 \phi_N(R^\sigma P)
   =\kappa^{-\sigma}(U_\sigma P)(c_0)
   =\kappa^{-\sigma}\sum_{s=0}^k p_s(-q^{-\sigma})^s,
 \tag{15}
\]
so \(|\phi_N(R^\sigma P)|\le\|P\|_{\rm New,1}\).
The first equality uses \(k<D\). For the second, use
\(\phi_N(F)=(TF)(c_0)\), (8), and \(R(c_0)=\kappa\);
then set \(r=0\) in (9).
In particular the uncharged isolated unit trace is
\(\kappa^{-\sigma}\), of modulus one.
When a joint spectator couples this variable to other components,
(15) is applied coefficientwise. It produces its actual remaining
coupon, not an independent scalar factor by assumption.

## 4. Quantitative conversion to charge shifts

For an ordinary degree-\(k\) polynomial \(Q\), define its cosine
coefficient norm by
\[
 Q(-2\cos t)=\sum_{j=0}^k a_j\cos(jt),\qquad
                         \|Q\|_{\cos,1}=\sum_j|a_j|.
 \tag{16}
\]
Its usual Fourier integrals give
\(\|Q\|_{\cos,1}\le(2k+1)\sup_{[-2,2]}|Q|\).
For \(r\le k<m\), the elementary sine and numerator bounds yield
\[
 \sup_{[-2,2]}|e_r|
       \le\frac{(N^2/4)^r}{(r!)^2}
       \le W_{N,k}:=\frac{(N^2/4)^k}{(k!)^2}.
 \tag{17}
\]
Indeed \(|c_a-z|\le4\), \(s_h\ge4h/N\) for
\(h\le N/2\), and the displayed upper sequence increases
up to \(k\). Combining (9), (16), and (17) gives
\[
 \boxed{\quad
 \|U_\sigma P\|_{\cos,1}
 \le(2k+1)2^k W_{N,k}\|P\|_{\rm New,1}.
 \quad}                                                     \tag{18}
\]
These are bounds for the literal polynomial \(U_\sigma P\).
Its fixed ordinary derivatives can also be retained, with
the polynomial degree factors from Markov's inequality.

The canonical coupon \(\mathcal C_{N,\chi}\) has the value and
first spectral derivative of \(\cos(N(1-\chi)t)\) at
\(z=-2\cos t=c_a\), using the positive angular preimage
at each double node; its odd simple-node value is one.
At a near-unit lattice charge, the actual full coupon is
\[
 P=\mathcal C_{N,1-k/N}=T_k(-z/2),\qquad
                    \|P\|_{\rm New,1}\le(k+1)(k+2).
 \tag{19}
\]
The bound follows directly from
\([e_s]P=\sum_{a\le s}b_{sa}P(c_a)\), since
\(|T_k(-c_a/2)|\le1\). More generally the same bound holds
for a product of real lattice cosine coupons of total ordinary
degree at most \(k<m\): its real-interval norm is at most one.
This degree is the sum before any quotient reduction.

For \(k\ge1\), \(k!\ge(k/e)^k\), and hence (18)--(19) imply
\[
 \|U_\sigma\mathcal C_{N,1-k/N}\|_{\cos,1}
 \le(2k+1)(k+1)(k+2)2^k
                          \left(\frac{eN}{2k}\right)^{2k}.
 \tag{20}
\]
For \(k=0\) the norm is exactly one.
If \(0<\varepsilon<1/2\) and \(k\le\varepsilon N\), then
\[
 \|U_\sigma\mathcal C_{N,1-k/N}\|_{\cos,1}
 \le2N^3 e^{N g(\varepsilon)},\qquad
 g(\varepsilon)=\varepsilon\log2+
                2\varepsilon\log\frac{e}{2\varepsilon}
                  \longrightarrow0.
 \tag{21}
\]
Monotonicity of \(2x\log(e/(2x))\) on \((0,1/2)\)
justifies using \(x=\varepsilon\). Thus \(k=o(N)\)
gives a subexponential cost. For a fixed positive window width
the bound in (21) is exponential, with a rate tending to zero
as the width shrinks.

If the neighbor already has its canonical entire cosine coupon
\(\mathcal C_{N,\chi}\), then each term of (16) has the exact
full-Hermite multiplication rule
\[
 T_j(-z/2)\mathcal C_{N,\chi}
       =\tfrac12\bigl(\mathcal C_{N,\chi-j/N}
                      +\mathcal C_{N,\chi+j/N}\bigr).
 \tag{22}
\]
This is the entire cosine product identity differentiated at
every double spectral root; at the odd simple node both
sides have their same value. Therefore (18) is precisely a
bound on the total absolute coefficient mass of charge
shifts of size at most \(k/N\), inside the original neighboring
trace. These coefficients can be complex; no positive law
is asserted for \(U_\sigma P\).
At unit neighbor charge, the exact symmetry
\(\mathcal C_{N,1+u}=\mathcal C_{N,1-u}\) folds this support
to the below-unit window \([1-k/N,1]\).

For successive unit-leaf reductions, the transmitted ordinary
degree adds to the existing coupon degree at the receiving
vertex. Cosine coefficient norms are submultiplicative,
by \(\cos jt\cos\ell t=(\cos(j+\ell)t+\cos(j-\ell)t)/2\).
Each individual use of (13) or (18)--(21) requires the
current total degree to remain below \(m\).
No degree bound is inferred for an arbitrary high partial
coupon or arbitrary spectator. A zero-leaf evaluation keeps
its entire remaining graph source as in (13), so its
subsequent scalar rate is not bounded by the coefficient
mass alone.

## 5. Coverage, limits, and source versions

The original terminal identities \(T1=e_D\) and
\(T(R^\sigma)=R^{-\sigma}\), the degree-two zero/unit
relations, and the triangular turned crossing were already
available. The latter is explicitly written in
[the degenerate-edge source transport](research_corner_newton_source_transport.md),
Sections 1 and 3. That coverage is credited rather than
claimed as a new operator.
The additional statement here is their charged low-degree
leaf assembly, exact shared-neighbor and isolated-component
consequences, and quantitative near-unit cosine conversion.

Every reduction is an original finite-algebra identity,
including all repeated-root normals. It requires no
intermediate hyperbolicity. It does not identify every
remaining short branching contraction with a scalar or a
positive-angle source. Disconnected components are simplified
by their actual functionals, not by assigning rate zero to
an empty global angle fiber. No new topological identification,
finite-exception conclusion, or general descendant rate
estimate is supplied.

The following complete direct sources were read at the pinned
versions, and the directly used statements and hashes checked:

* [Original zero/unit turn relation](research_degree_two_short_reductions.md),
  SHA256 d90f9be0155e9c9cf217d48c1b00733bb5c4b98a159cfceeeb0e0fc0d3473f20:
  the original normalization, full crossing matrix, Frobenius
  self-adjointness, and exact relation (4).
* [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  square-zero radical, the exact original normal functional
  (12)--(13), coefficient bound, odd simple node, and top mode.
* [Actual near-unit charged closing rows](research_near_unit_charged_high_sector_gap.md),
  SHA256 dc707bc52cacc2ce507d9d6c55129b3a378c2a104b2116d14ff42ecc0d312637:
  the canonical lattice coupon and its exact low-degree
  Newton coefficient bound, with full normal data.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build
was run. Existing private notes and public files were unchanged.
