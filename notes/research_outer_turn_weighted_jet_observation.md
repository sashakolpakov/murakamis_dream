# The original outer observation and its sharp positive weighted norm

Private written proof, 16 November 2026.

The physical outer-collar observation can be moved across the
original bilinear Frobenius pairing without changing its normals
or scalar carrier. On the space of all canonical inputs, its
positive weighted local-jet norm is comparable, up to a polynomial,
to the positive physical-kernel sum. This gives an exact sufficient
kernel criterion whose exponential rate is optimal when only the
stated weighted physical value/normal bound is supplied.

The lower bound below uses freely chosen full Hermite jets.
It is not a lower bound for a received endpoint-product source.
No positivity of the original Frobenius closing is asserted.

## 1. Exact observation and adjoint placement

Put
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 P_N(C)=2T_N(C/2)+2,\qquad
 \mathcal A_N=\mathbb C[C]/(P_N),\qquad
 c_j=2\cos((2j+1)\pi/N).
 \tag{1}
\]
The distinct physical nodes have indices
\(0\le j\le J_N=\lfloor D/2\rfloor\). Let \(\mathcal D_N\)
be the double-node indices. At odd \(N\) the remaining index
\(j=J_N\) is the simple node \(c_j=-2\).
For a double node set \(a_j=4-c_j^2>0\).

Keep the original turn, kernel, crossing and trace:
\[
 (Tf)(z)=\phi_N(K_N(z,C)f(C)),\qquad
 V_n=\kappa^nTR^{-n}T,\qquad U_\tau=V_\tau,\quad \tau=\pm1.
\]
The full trace is
\[
 \phi_N(f)=
 \eta\sum_{j\in\mathcal D_N}
                 \{a_j f'(c_j)-c_j f(c_j)\}
              +\mathbf1_{N\ {\rm odd}}f(-2).                 \tag{2}
\]
Every input is represented canonically. No free output is
reduced unless explicitly specified.

The original turn relation gives, with no remaining carrier,
\[
                       U_\tau=R^\tau T R^\tau.               \tag{3}
\]
Indeed \(TR^{-\tau}T=\kappa^{-\tau}R^\tau TR^\tau\).
Write \(r=R^\tau\), \(r_b=r(c_b)\), and
\(K_b(C)=K_N(c_b,C)\). At every physical output,
\[
       \mathcal L_b(f):=(U_\tau f)(c_b)
                         =r_b\,\phi_N(K_b r f).              \tag{4}
\]
At a double output its normalized first normal is
\[
 \mathcal N_b(f):=a_b(U_\tau f)'(c_b)
   =a_b r'(c_b)\phi_N(K_brf)
        +r_b\phi_N(a_b\,\partial_bK_N(c_b,C)\,r f).
 \tag{5}
\]
Thus (5) retains both the differentiated kernel and the
differentiated original crossing.

For an actual composed input \(f=\operatorname{can}((V_nQ)y)\),
bilinear self-adjointness of \(V_n\) gives exactly
\[
 \mathcal L_b(f)
       =r_b\,\phi_N\!\left(Q\,V_n(rK_b y)\right).              \tag{6}
\]
In (5) the same rule moves \(V_n\) to each of its two
observations. These are bilinear adjoints, without complex
conjugation. Every \(y\), including any shared parameters,
remains inside the observation. This does not bound the
new dual coupon \(V_n(rK_by)\).

Equations (4)--(6) hold coefficientwise with arbitrary
ordinary shared parameters, and after their fixed derivatives.
If another prescribed trace closes those parameters, it
must still be applied to these entire expressions.

## 2. The full jet matrix

At a double node use the two coordinates
\[
                    \mathbf j_j f=(f(c_j),a_jf'(c_j))^t.
 \tag{7}
\]
At the odd simple node use only its value.
The local Frobenius block on two double-node jets is
\[
                    B_j=\eta
                         \begin{pmatrix}-c_j&1\\1&0\end{pmatrix}.
 \tag{8}
\]
It has determinant \(-1\) and signature \((1,1)\).
In particular it is not a positive inner product.

For two double nodes define
\[
 E_{bj}=
 \begin{pmatrix}
 K_N(c_b,c_j)&a_j\partial_jK_N(c_b,c_j)\\
 a_b\partial_bK_N(c_b,c_j)&
             a_ba_j\partial_b\partial_jK_N(c_b,c_j)
 \end{pmatrix},
\]
\[
 M_j(r)=
 \begin{pmatrix}r(c_j)&0\\a_jr'(c_j)&r(c_j)\end{pmatrix}.
 \tag{9}
\]
Then the actual full output jet is
\[
             \mathbf j_b(U_\tau f)
                =M_b(r)\sum_j E_{bj}B_jM_j(r)\mathbf j_j f.
 \tag{10}
\]
For the odd simple input, its term means the column
\((K_N(c_b,-2),a_b\partial_bK_N(c_b,-2))^t\)
times \(r(-2)f(-2)\); its trace coefficient is \(1\).
At a simple output retain only the first row.

This proves (10) directly by (2) and the product rule.
For multiplication by a shared spectator \(y\), insert
\[
                  M_j(y)=
            \begin{pmatrix}y(c_j)&0\\a_jy'(c_j)&y(c_j)\end{pmatrix}
 \tag{11}
\]
on the right of each input block. It is the ordinary
shared-color product normal, not a product of separately
closed factors.

The pressure source supplies
\[
 K_N(c_b,c_j)>0,\qquad
 |\partial_j K|\le N^{11}K,\qquad
 |\partial_b\partial_jK|\le(N^{16}+N^{22})K                \tag{12}
\]
where the respective endpoint is double. The single-derivative
bound also applies when the other endpoint is the odd simple
node. The crossing values have modulus one and their first
normals have polynomial bounds. Consequently every entry
of the actual matrix in (10) is at most a fixed polynomial
in \(N\) times \(K_N(c_b,c_j)\). The finitely sized level
\(N=2\) is included by increasing the constant.

## 3. Exact weighted dual norm and its optimal exponential rate

Choose arbitrary positive numbers \(W_{j,N}\), with no
regularity assumption, and define a norm on \(\mathcal A_N\)
by
\[
 \|f\|_W=\max\left\{
   \max_{j\in\mathcal D_N}
      W_{j,N}^{-1}\max(|f(c_j)|,|a_jf'(c_j)|),
   \ \mathbf1_{N\ {\rm odd}}W_{J_N,N}^{-1}|f(-2)|
                              \right\}.                    \tag{13}
\]
The last entry is omitted at even levels.
Define the positive physical row sum
\[
              \mathcal P_{b,N}(W)
                   =\sum_{j=0}^{J_N}
                         K_N(c_b,c_j)W_{j,N}.                \tag{14}
\]

**Theorem.** Uniformly in the weights, the output row and
both level parities,
\[
 \boxed{\quad
 \mathcal P_{b,N}(W)\le\|\mathcal L_b\|_{W}^{*}
                       \le CN^p\mathcal P_{b,N}(W).
 \quad}                                                       \tag{15}
\]
At every double output,
\[
                   \|\mathcal N_b\|_{W}^{*}
                              \le CN^p\mathcal P_{b,N}(W).    \tag{16}
\]
Here the dual norms are suprema over all canonical complex
polynomials with norm at most one.

More precisely, set
\[
 d_{bj}=a_j\partial_jK_N(c_b,c_j)-c_jK_N(c_b,c_j)
                 +a_j\frac{r'(c_j)}{r(c_j)}K_N(c_b,c_j).
\]
Then
\[
       \|\mathcal L_b\|_{W}^{*}
        =\mathcal P_{b,N}(W)
                   +\sum_{j\in\mathcal D_N}W_{j,N}|d_{bj}|.
 \tag{17}
\]

*Proof.* At each double input, (4) has coefficients
\(\eta r_b r(c_j)d_{bj}\) on \(f(c_j)\) and
\(\eta r_b r(c_j)K_N(c_b,c_j)\) on \(a_jf'(c_j)\).
At the odd simple input its coefficient is
\(r_b r(-2)K_N(c_b,-2)\).
The value and first-normal data at the double nodes, and
the value at the odd simple node, are independent coordinates:
ordinary Hermite interpolation gives a unique polynomial of
degree less than \(N\) for any such prescribed data.
Thus the dual of (13) is exactly the weighted sum of the
absolute values of these coefficients. Since \(|r(c_j)|=1\),
this is (17).

For an explicit lower test, set all double-node values to
zero and choose
\[
  a_jf'(c_j)=
        \overline{\eta r_b r(c_j)}\,W_{j,N}.
 \tag{18}
\]
At the odd simple node choose
\[
               f(-2)=\overline{r_b r(-2)}\,W_{J_N,N}.
 \tag{19}
\]
The corresponding canonical polynomial has norm one and
its output in (4) is exactly (14). It does not require
any prescribed derivative at the odd simple node.
This proves the lower bound also at \(N=2\).
Equations (12) and the polynomial crossing-normal bounds
prove the upper bounds (15)--(16). \(\square\)

The saturating inputs (18)--(19) depend on the output and
the chosen weights. There is no assertion that they arise
from the endpoint products, positive-pole quotient packets,
or any specified partially filled graph.

For a continuous real profile \(A(t)\) on \([0,\pi]\), put
\[
 \theta_j=\pi(N-1-2j)/N,\qquad
                W_{j,N}=\exp\{NA(\theta_j)\}.
 \tag{20}
\]
If an output sequence satisfies \(\theta_{b_N}\to t\in(0,\pi)\),
the positive-kernel pressure calculation gives
\[
 \lim_{N\to\infty}\frac1N\log\mathcal P_{b_N,N}(W)
       =\max_{u\in[0,\pi]}\{\psi(t,u)+A(u)\}.                 \tag{21}
\]
The upper follows from its uniform physical-kernel estimate;
the lower uses its positive Newton term at the original
interior edge saddle, approximating a maximizing endpoint
by interior angles if necessary. This is the one-edge
weighted specialization of that existing proof, with its
original complete constant. Combining (15) and (21) gives
the same exact rate for the value-observation dual norm.
Equation (16) gives that rate as an upper bound for its
normalized first-normal observation. No first-normal lower
bound is needed or asserted.

## 4. What an energy-adapted weight would have to prove

For a proposed output rate \(B_b\), the explicit sufficient
positive-kernel estimate is
\[
                  \mathcal P_{b,N}(W)
                          \le e^{NB_b+o(N)}.                 \tag{22}
\]
It bounds both observations for every input with
\(\|f_N\|_W\le e^{o(N)}\). Conversely a uniform bound at
that rate for all inputs in the unit ball of (13) forces
(22), by (15). At the profile level its exact criterion is
\[
                 \max_u\{\psi(t,u)+A(u)\}\le B(t).             \tag{23}
\]
Thus a positive weight dictated by a conditional energy
must satisfy this actual kernel inequality. The choice of
weight does not supply it.

For example, supplied physical value and first-normal
profiles for several incoming coupons give a profile for
their shared product by the full product rule (11).
Using that profile in (13) is legitimate, but replaces the
actual correlated jets by the whole weighted unit ball.
Changing to another positive local-jet norm cannot prove
a smaller bound uniformly on that same ball: the exact
observation already attains (14) on (18)--(19).

The archived physical-pressure theorem identifies precisely
the energy relaxation made by positive absolute physical
sums. Its strict excess over the selected zero-power
complex-charge action at a supplied nonreal positive
target cannot be erased by relabeling such a sum as a
weighted norm. Nor does a real profile automatically
impose the retained receiving unit rows or their outside
work. Applying a convex-energy comparison requires those
original constraints and the correct transformed boundary
data, not just an infimum over the unconstrained physical
color in (23).

For the actual outer collars in projected recovery,
\(f_N=\operatorname{can}[(V_nP_j)y]\), the unresolved
alternative is therefore specific: prove (22) at the
required action for a justified incoming profile, or prove
a sharper coherent estimate for (4)--(6) on that actual
source family, using information absent from a positive
local-jet bound. The theorem does not exclude the latter.
All remaining original traces and joint spectators must
stay inside that coherent estimate. No actual source
growth lower bound, parent gap, or noncancellation statement
follows from the dual-norm lower bound.

## 5. Coverage and complete direct sources

Weighted observation norms and their matrix criteria already
appear in the earlier observation-composition notes. The
positive physical pressure and the polynomial cost of all
kernel normals are also prior results. The added statement
is the exact outer \(U_\tau\) full-jet row (4)--(10), its
sharp weighted dual formula (17), and the consequent
optimality of the positive-kernel criterion for this
original observation.

The following complete source texts were freshly read,
with every used implication and each hash checked:

* [Original unit-turn relation](research_low_degree_charged_leaf_reduction.md),
  SHA256 80df78ceafaa97182aebc6831651921f7f8040e1356ee07a3d0d3fbadd02846a.
* [Full-normal physical pressure](research_charged_source_physical_pressure.md),
  SHA256 1e127c0842c0d6d5727a517cc66c39e73baa2846848c284d257c1ebe49679091.
* [Original bilinear adjoint and closing](research_opposite_power_spectator_reduction.md),
  SHA256 f9a3a776a7a3d8def4cfba2ac13c65079626de6f3254e85ec6f9dce8700dc1a1.

Only written mathematics and source-text/hash reads were used.
No mathematical program, test, numerical experiment, build,
or compilation was run. Frozen notes and public manuscripts
are unchanged.
