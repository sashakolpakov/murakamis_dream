# One shared power deformation turns weak balance into a strict source gap

This is a theorem about the original shared coefficient problem on a matched simple triangulated sphere. The diagram, its matching, its marked MAIN edge, every face target, and every local sector are unchanged. Only the positive weights used in a coefficient estimate change.

The principal conclusion is that **nonstrict balance at the actual complete packing is sufficient for a strict complementary-source certificate**. This includes equality at any number of local middle targets. One common vector works for every genuine non-CROSS string. A quantitative extension allows a controlled positive balance defect. The proof does not assert that bounded vertex degree by itself enforces either hypothesis.

## 1. Original data and normalization

Let a simple triangulated sphere carry its original matching of the cubic dual and an adjacent protected MAIN pair. Let \(V\) be the ordinary white vertices and \(R=|V|\) the number of matched ports. Every ordinary coefficient target is \(d=N-1\); the two protected targets are zero. The complete marked circle packing gives ordinary curvatures
\[
 w_f^*>0,\qquad q_f=\log w_f^*,\qquad f\in V.
 \tag{1}
\]
The protected curvatures remain zero throughout this note. A common positive rescaling is an irrelevant gauge.

For a triangle \(t\), let \(I_t\subset V\) be its nonempty set of ordinary corners. Define its exact source-normalized potential by
\[
 Q_t(q)=
 \max_{\substack{a_f\ge0,\ f\in I_t\\
                  \sum_{f\in I_t}a_f=1/2}}
       \sum_{f\in I_t}\bigl(f(a_f)+a_fq_f\bigr),
 \qquad
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi}.
 \tag{2}
\]
Here \(\Lambda(\theta)=-\int_0^\theta\log|2\sin u|\,du\).
Protected coordinates have been deleted, not replaced by small weights.
For a singleton row \(I_t=\{f\}\), \(Q_t=q_f/2\).

For two or three positive weights the maximizing load is
\[
 a_{tf}=\frac1\pi\arctan(w_f/D_t),\qquad
 D_t^2=\sum_{\{i,j\}\subset I_t}w_iw_j .
 \tag{3}
\]
All its allowed entries are positive and their sum is \(1/2\).
In particular
\[
 E_t(q):=Q_t(q)-q\cdot\nabla Q_t(q)
              =\sum_{f\in I_t}f(a_{tf})
 \tag{4}
\]
is the row entropy. It is zero on a singleton row and strictly positive on every row with at least two ordinary corners. Indeed \(f(0)=f(1/2)=0\), while
\(f''(a)=-2\pi/\sin(2\pi a)<0\) on the open interval.

The complete action and face equations are
\[
 P(q)=\sum_t Q_t(q)-\sum_{f\in V}q_f,\qquad
 \nabla P(q)=0,\qquad P(q)=\Phi .
 \tag{5}
\]
Thus \(\sum_{t\ni f}a_{tf}=1\) at every ordinary face,
\(\Phi=\sum_tE_t(q)\), and \(2\pi\Phi\) is the actual complete augmented volume. Equations (2)–(5) use the original matched triangle incidences.

At a port \(e=(x,b,c,y)\), write
\[
 Q_b=Q(x,b,y),\quad Q_c=Q(x,c,y),\quad X_e=Q_b+Q_c,
 \qquad
 A_L=\max(q_c,Q_b+q_c/2),\quad
 A_R=\max(q_b,Q_c+q_b/2),\quad A_C=X_e .
 \tag{6}
\]
The letters in (6) mean the actual shared coordinates at this port. A one-sided label overloading a protected middle is absent. The outer pair is a MATCHING edge whereas the protected pair is MAIN, so \(x+y>0\). Consequently the triangle containing a positive overloaded middle always has at least two ordinary corners and positive entropy.

For a surviving side \(s\in\{L,R\}\), let \(z_{e,s}\) be its overloaded middle (\(c\) for LEFT and \(b\) for RIGHT), and let \(t(e,s)\) be the triangle containing that middle. Define
\[
 \epsilon_{e,s}=\max(0,q_{z_{e,s}}-X_e(q)),\qquad
 m_{e,s}=E_{t(e,s)}(q)>0.
 \tag{7}
\]
If no side survives, the complementary source is zero and no criterion is needed.

## 2. Power flattening and entropy monotonicity

For \(0<\beta\le1\), use the single shared vector
\[
 w_f(\beta)=(w_f^*)^\beta,\qquad
 q_f(\beta)=\beta q_f,\qquad f\in V .
 \tag{8}
\]
This is not a new circle packing or a diagram operation. It is an allowed positive coefficient torus; the original protected zeros and face targets stay fixed.

Put \(E_t(\beta)=Q_t(\beta q)-\beta q\cdot\nabla Q_t(\beta q)\).
Differentiation gives
\[
 \frac{dE_t(\beta)}{d\beta}
       =-\beta q^{\mathsf T}\nabla^2Q_t(\beta q)q\le0.
 \tag{9}
\]
The Hessian is positive semidefinite because (2) is a supremum of affine functions. For singleton rows both sides vanish. Thus
\(E_t(\beta)\ge E_t(1)\) when \(0<\beta\le1\).
Differentiating \(Q_t(\beta q)/\beta\) and integrating proves the exact identity
\[
 Q_t(\beta q)
   =\beta Q_t(q)+
          \beta\int_\beta^1\frac{E_t(u)}{u^2}\,du
   \ge \beta Q_t(q)+(1-\beta)E_t(q).
 \tag{10}
\]
No unmarked additive constant is used. The formula is invariant under replacing \(q\) by \(q+c\mathbf1\), since each row has degree \(1/2\).

For LEFT, the local loss is
\[
 X_e-A_L
   =\min\{X_e-q_c,\ Q_c-q_c/2\}.
 \tag{11}
\]
At the complete vector the second entry is strictly positive: in (2) its supported simplex contains another ordinary corner besides \(c\), and the finite maximizer is interior. Apply (10) to both entries of (11). With \(t=1-\beta\),
\[
 \begin{aligned}
 (X_e-q_c)(\beta q)
   &\ge-\beta\epsilon_{e,L}
              +t\bigl(E_{Q_b}(q)+E_{Q_c}(q)\bigr),\\
 (Q_c-q_c/2)(\beta q)&\ge tE_{Q_c}(q).
 \end{aligned}
\]
Therefore, for either surviving side,
\[
 \boxed{\quad
 (X_e-A_s)(\beta q)
       \ge t\,m_{e,s}-(1-t)\epsilon_{e,s}.
 \quad}
 \tag{12}
\]
In particular, weak balance at completeness, \(\epsilon_{e,s}=0\), becomes strict balance at every \(0<\beta<1\). This assertion concerns the local envelopes; the complete-action cost is accounted for next.

## 3. The entire complete-action cost

For two distinct ordinary corners of a triangle,
\[
 \partial_{q_i}\partial_{q_j}Q_t
    =-\frac{w_iw_j}{2\pi D_t(w_i+w_j)}
    =-\kappa^t_{ij},\qquad 0<\kappa^t_{ij}\le\frac1{4\pi}.
 \tag{13}
\]
The Hessian rows sum to zero. The formula also holds on a two-corner row, with \(D_t=\sqrt{w_iw_j}\); a singleton has zero Hessian. Define the nonnegative, gauge-invariant number
\[
 \mathcal E_D
   =\frac1{4\pi}
       \sum_t\sum_{\{i,j\}\subset I_t}(q_i-q_j)^2
   =\frac1{2\pi}
       \sum_{\substack{\{i,j\}\text{ white edge}\\i,j\in V}}
                      \left(\log\frac{w_i^*}{w_j^*}\right)^2 .
 \tag{14}
\]
The second equality retains both original triangles incident to each ordinary white edge. The complete stationary equations (5) and the Hessian bound (13) imply
\[
 0\le P((1-t)q)-\Phi\le\frac{t^2}{2}\mathcal E_D,
          \qquad 0\le t<1 .
 \tag{15}
\]
This is a cost for all original triangles and all shared faces at once. It is not a sum of independently optimized local budgets.

## 4. A uniform criterion for every genuine non-CROSS string

For a genuine label string \(\sigma\in\{C,L,R\}^R\), let \(J_\sigma\) be its set of one-sided ports. Its shared envelope at the vector (8) is
\[
 \begin{aligned}
 G_\sigma((1-t)q)
  &=\sum_eA_{e,\sigma_e}((1-t)q)
                        -\sum_{f\in V}(1-t)q_f\\
  &\le\Phi+\frac{t^2}{2}\mathcal E_D
       -\sum_{e\in J_\sigma}
            \bigl(t m_{e,\sigma_e}-(1-t)\epsilon_{e,\sigma_e}\bigr).
 \end{aligned}
 \tag{16}
\]
There is no spectator maximum omitted from this formula. If
\[
 \gamma(t):=
       \min_{(e,s)\text{ surviving}}
             \bigl(t m_{e,s}-(1-t)\epsilon_{e,s}\bigr)
                -\frac{t^2}{2}\mathcal E_D>0 ,
       \qquad 0<t<1,
 \tag{17}
\]
then every non-CROSS string satisfies \(G_\sigma\le\Phi-\gamma(t)\).
The same vector certifies every anchored branch, because (17) makes all one-sided losses positive, so all unrestricted spectator maxima equal \(X_e\). This is a finite criterion involving the complete geometry alone.

**Weak-balance theorem.** Suppose
\[
 X_e(q)\ge q_b\quad(b>0),\qquad
 X_e(q)\ge q_c\quad(c>0)
 \tag{18}
\]
at every original port. Then (17) holds for some \(t>0\). More explicitly, put \(m=\min m_{e,s}>0\). If \(\mathcal E_D>0\), choose
\[
 t_0=\min\left(\frac12,\frac{m}{\mathcal E_D}\right).
 \tag{19}
\]
Then
\[
 G_\sigma((1-t_0)q)\le\Phi-\frac{t_0m}{2}
           \qquad(\sigma\ne C^R).
 \tag{20}
\]
If \(\mathcal E_D=0\), take \(t_0=1/2\); (16) gives the still stronger gap \(m/2\). Thus equality in (18) creates no exceptional source sector.

The theorem is valid on every fixed actual matched simple sphere with its original mark and packing. It places no restriction on the number of cycles or on the number of ports. It is a sufficient geometric class, not a claim that every complete packing satisfies (18).

## 5. Allowing an actual positive imbalance

Let \(\epsilon=\max\epsilon_{e,s}\). A convenient sufficient scalar test is
\[
 t(m+\epsilon)-\epsilon-\frac12\mathcal E_Dt^2>0
       \quad\text{for some }0<t<1 .
 \tag{21}
\]
It implies (17). In particular, use \(t_0\) from (19) and require
\[
 \epsilon<\frac{t_0m}{2}.
 \tag{22}
\]
Then the strict complementary gap is at least
\(t_0m/2-\epsilon>0\).
This allows genuine failure of complete-radius balance. It is a sufficient bound, not an equivalence: (17) retains the individual row entropies and defects and may succeed when (22) fails.

For a family of unchanged marked spheres, suppose uniformly that
\[
 \mathcal E_D\le E_0,\qquad
 m_{e,s}\ge m_0>0,\qquad
 \epsilon_{e,s}\le\epsilon_0
 \tag{23}
\]
and there exists one \(0<t<1\) with
\[
 t m_0-(1-t)\epsilon_0-\tfrac12t^2E_0>0.
 \tag{24}
\]
Then the same exponent \(\beta=1-t\) and the same positive action gap work for every member, regardless of its number of ports. The actual weight vectors are still the powers of each member's own complete curvatures. This is a uniform source-certificate theorem, not a uniform hyperbolic-filling threshold over the family.

The entropy assumption can be bounded using local curvature ratios. If every pair of ordinary corners in one triangle has ratio at most \(K\ge1\), define
\[
 a_0(K)=\frac1\pi\arctan\frac1{\sqrt{K^2+2K}}.
 \tag{25}
\]
Every allowed load on a nonsingleton row is at least \(a_0(K)\). Indeed, normalize the smallest weight to one; its \(D_t^2\) is at most \(K^2+2K\), and the two-corner case is stronger. Every load is also at most \(1/2-a_0(K)\). Symmetry and concavity of \(f\) then imply
\[
 E_t(q)\ge2f(a_0(K))
 \tag{26}
\]
on every nonsingleton row. Thus one can take \(m_0=2f(a_0(K))\).
No circle-packing ratio bound is inferred from graph degree alone here.

## 6. What bounded degree and annular length do not automatically supply

Equation (14) makes the remaining geometric condition explicit. If the ordinary white graph has at most \(E\) edges and adjacent curvature ratios at most \(K\), then
\[
 \mathcal E_D\le\frac{E}{2\pi}(\log K)^2.
 \tag{27}
\]
A degree bound controls \(E\) by a constant times \(|V|\), but this estimate still grows with diagram size. The crude criterion (22) can consequently require an imbalance of order \(1/|V|\), even with uniformly bounded local ratios. It does not establish a size-independent tolerance for all bounded-degree spheres.

Long annular strips can instead be tested using their actual sum of squared logarithmic differences in (14). A bound on that sum is sufficient by (23)–(24); a bound on the width or on the degree alone is not substituted for it. Nor is insertion of a strip asserted to preserve the complete vector, the source targets, or the resulting knot. A separate geometric construction would be needed to establish (23) on a new combinatorially specified class.

The earlier cut-scaling estimate remains complementary. For a face set \(U\), its cost can depend only on complete angle mass across its boundary, even if (14) grows. That is why the all-even three-witness argument can be stronger than uniform power flattening. The present theorem gives a different, global criterion and closes the weak-balance equality case without a family-specific trigonometric analysis.

## 7. Exact source consequence and limits

The local bounds (6) are phase-uniform on the original shared face torus and uniform on the full real spectral cube. For each fixed source, there are only finitely many genuine strings. Therefore (17) gives
\[
 \|S_{N,\mathrm{full}}-S_{N,\mathrm{CROSS}}\|_{[-2,2]^R}
      \le \exp\bigl(N(\Phi-\gamma)+o(N)\bigr)
 \tag{28}
\]
for any fixed \(0<\gamma<\gamma(t)\), with every original target \(d=N-1\) retained. The difference is polynomial of degree at most \(d\) in each spectral variable.

The original full-Hermite filling bound transfers (28) to every fixed signed twist vector with no new exponential cost. The general-Morse all-CROSS period has a nonzero rate tending to \(\Phi\) as all fixed signed twists become independently long. Under its original knot pairing and primitive geometric hypotheses, sufficiently long fillings therefore have the full invariant's actual knot-complement volume rate. This application uses those separate exact-source, whole-period, and geometric theorems; the present note changes no normal, phase, framing factor, or endpoint convention.

It gives no estimate for a source violating (17), no universal success theorem for refined covers, and no moving-main-meridian or short-filling assertion. In particular it does not repair the established seventeen-port obstruction to universal anchored certificates. That example must fail the present sufficient test if it uses the same original mark.

## 8. Dependencies

The exact triangle Legendre normalization and its closed support are in
actual_triangle_entropy_algebraic_balance.md and
actual_fejer_half_block_entropy.md.
The original complete packing, shared face stars, and positive source capacity are in
actual_complete_source_cauchy_capacity_gap.md and the simple-white geometric source proofs.
The local CROSS/LEFT/RIGHT value bounds and genuine-sector interpretation are in
general_actual_sector_cover_filling_volume.md and
actual_global_left_weighted_spectral_envelope.md.
The full-source finite functional is in
actual_uniform_filling_supremum_bound.md.
The general Morse source and its nonzero all-CROSS filling period are in
research_matched_sphere_morse_source.md,
actual_morse_cross_filling_period.md, and
actual_morse_geometric_contribution.md.

The entropy identity (10), quantitative bounds (12) and (17), and weak-balance theorem (18)–(20) are proved above from these normalized inputs. Numerical sampling is not used in any implication.
