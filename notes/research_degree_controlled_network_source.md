# Quantum sums on branching circle trees

The wide-rectangle edge theorem permits a complete source proof on
branching graphs. A sufficient local condition is
\(|n_v|\ge\max(8,4d_v)\), where \(d_v\) is the original degree
of the filled vertex. The condition allows unrelated powers and
independent signs. Every graph and every power are fixed before the
level tends to infinity.

The analytic theorem below concerns an explicit finite graph sum.
Its knot-volume consequence is restricted to graphs and markings
coming from the original ordered circle-tree construction. An
arbitrary graph sum is not declared to be a knot invariant.
Frozen manuscripts and public documentation are unchanged.

## 1. The source and the statement

Let \(\Gamma=(V,E)\) be a finite loopless graph, allowing repeated
edges. Choose a nonempty set \(I\subseteq V\), and let
\(d_v\ge1\) be the original incidence degree of each \(v\in I\),
including edges to unselected vertices and all multiplicities.
Suppose the fixed integers \(n_v\) obey
\[
                      |n_v|\ge\max\{8,4d_v\}.
 \tag{1}
\]
Unselected angles are zero. With the original Newton kernel,
crossing and full Hermite trace, define
\[
 Z_{\Gamma,I,N}=
 \left(\prod_{v\in I}\phi_N^{(t_v)}R(t_v)^{n_v}\right)
       \prod_{\{v,w\}\in E}K_N(t_v,t_w),
                   \qquad t_w=0\quad(w\notin I).
 \tag{2}
\]
This notation means that all edge factors are multiplied before
taking the traces. Only traced variables are reduced; any unselected
variables retain the literal polynomial representative in (2). Every
shared edge occurs once, and every first normal at a double spectral
root is retained.

Use the calibrated edge phase and amplitude \(\psi,a_e\) of
[the full wide-rectangle theorem](research_bare_kernel_thin_rectangle.md#6-the-full-rectangle-through-real-angle-pi-over-two).
Thus \(\psi(0,0)=M_\infty=4G/\pi\). Put
\[
 \Phi_\lambda(t)=\sum_{\{v,w\}\in E}\psi(t_v,t_w)
    +\sum_{v\in I}\frac{i n_vt_v^2}{4\pi}
    -i\sum_{v\in I}\lambda_vt_v,
                  \qquad \Phi=\Phi_{\mathbf1}.
 \tag{3}
\]
Complete edges outside the selected set remain in this sum; they
contribute their original constant.

**Theorem 1.** Under (1), \(\Phi\) has a unique critical point
\(t^*\) in the box \(|\Re t_v|\le1,|\Im t_v|\le1/3\).
It satisfies
\[
 |t_v^*|<9/10,\qquad 0<-\Im t_v^*<3/10,
 \qquad \operatorname{sgn}\Re t_v^*=\operatorname{sgn}n_v.
 \tag{4}
\]
Write \(m=|I|\), \(e=|E|\), and \(\mathcal H=-\Phi''(t^*)\),
with derivatives only in selected variables. Along all integer levels,
\[
 Z_{\Gamma,I,N}=
 \left(\prod_{v\in I}e^{\pi i n_v(N-1)^2/(4N)}\right)
 N^{3(m-e)/2}\mathcal A_{\Gamma,I}
        e^{N\Phi(t^*)}(1+O(N^{-1})),
 \tag{5}
\]
where
\[
 \mathcal A_{\Gamma,I}=
 \left(\frac{i}{\pi}\right)^m(2\pi)^{m/2}
 \frac{\displaystyle\prod_{v\in I}\sin t_v^*
          \prod_{\{v,w\}\in E}a_e(t_v^*,t_w^*)}
      {\sqrt{\det\mathcal H}}\ne0.
 \tag{6}
\]
The square root is the Gaussian branch for matrices with positive
Hermitian real part. The expansion continues to every fixed inverse
power of \(N\). It extends holomorphically to a neighborhood of
the complete unselected colors, with all fixed ordinary spectral
derivatives. Constants may depend on the fixed graph and powers;
there is no claim about a simultaneous growth of the graph with \(N\).

## 2. The complete charge cube on a branching graph

For an oriented incidence put
\[
 r_{vw}(t)=\operatorname{asinh}
       \{\tan(t_v/2)\cos(t_w/2)\}.
 \tag{7}
\]
All branches are continued from zero. The exact equations are
\[
             n_vt_v+2i\sum_{w\sim v}r_{vw}=2\pi\lambda_v.
 \tag{8}
\]
Multiplicity is retained in the sum. The following argument uses
only local degrees, not the order of vertices on a path.

On \(\mathcal B=\{z:|\Re z|\le1,|\Im z|\le1/3\}\),
the elementary calculations in Section 2 of
[the partial-charge proof](research_positive_path_partial_charge_bounds.md#2-the-exact-return-map-is-a-contraction)
give
\[
 \begin{split}
 |\tan(z/2)|&<3/5,& |\Im\tan(z/2)|&<1/4,\\
 |\Re r_{vw}|&<123/200,&|\Im r_{vw}|&<7/20,\\
 |K_{vv}|+|K_{vw}|&<86/45,&|K_{vv}-1|&<2/5,
 \end{split}
 \tag{9}
\]
where \(K=-2\pi\psi''\). These are estimates for one edge
on the displayed box. They do not assume a source expansion or
an existence theorem for this graph.

Rewrite (8) as
\[
 \mathcal T_v(t)=\frac{2\pi\lambda_v}{n_v}
                    -\frac{2i}{n_v}\sum_{w\sim v}r_{vw}(t).
 \tag{10}
\]
For real \(\lambda\in[-1,1]^I\), (1) and (9) give
\[
 |\Re\mathcal T_v|<\pi/4+7/40<1,
 \qquad |\Im\mathcal T_v|<123/400<1/3.
 \tag{11}
\]
The derivatives of one return are
\(\partial_{t_v}r_{vw}=K_{vv}/2\) and
\(\partial_{t_w}r_{vw}=K_{vw}/2\).
Therefore the supremum-norm Jacobian row bound is
\[
                  \frac{d_v}{|n_v|}\frac{86}{45}
                            \le\frac{43}{90}<\frac12.
 \tag{12}
\]
Repeated neighbors merely add their incidences to this row; complete
outside variables contribute no derivative columns. Banach's theorem
on the finite product box proves existence and uniqueness.
It also proves a common holomorphic extension to charges within
\(1/100\) of \([-1,1]^I\): the two bounds in (11) increase
by at most \(\pi/400\), still inside the box, and (12) is unchanged.

The removable quotient
\[
 Q_v=\sum_{w\sim v}\frac{r_{vw}}{t_v}
     =\frac12\sum_{w\sim v}\int_0^1
                          K_{vv}(\sigma t_v,t_w)\,d\sigma
\]
obeys \(|Q_v-d_v/2|<d_v/5\). Thus the exact equation factors as
\[
               t_v=\frac{2\pi\lambda_v}{n_v+2iQ_v}.
 \tag{13}
\]
For \(0\le\lambda_v\le1\), zero charge gives exactly zero angle.
At positive charge the real angle has the sign of \(n_v\), while
its imaginary part is negative. Also
\[
 |t_v|\le\frac{2\pi\lambda_v}{|n_v|-2d_v/5}
               \le\frac{5\pi}{18}\lambda_v<\frac9{10}.
 \tag{14}
\]

Write \(H_v=-\Im t_v\). The same quotient gives the componentwise
bound
\[
 0\le H_v\le U_{|n_v|,d_v}\lambda_v,
 \qquad U_{n,d}=
 \frac{14\pi d/5}{(n-2d/5)^2+(7d/5)^2}.
 \tag{15}
\]
Indeed, for \(Q_v=A+iB\),
\(H_v=4\pi\lambda_vA/[(n_v-2B)^2+4A^2]\).
On \(3d/10<A<7d/10,|B|<d/5\), its maximum is at the
upper \(A\)-corner and the \(B\)-corner with the sign of \(n_v\).
The required monotonicity uses \(|n_v|>9d_v/5\), which follows
from (1).

For \(d\ge2\), the worst allowed power is \(n=4d\), and
\(U_{n,d}\le70\pi/(373d)\). For \(d=1\), use \(n\ge8\)
to obtain \(U_{n,1}\le70\pi/1493\). Consequently
\[
 U_{n,d}\le\frac{35\pi}{373}<\frac3{10},
 \qquad
       \frac{U_{n,d}}{2d}\le\frac{35\pi}{1492}<\frac3{40}.
 \tag{16}
\]
These prove (4), throughout the entire nonnegative charge cube.

Let \(M(\lambda)=\Re\Phi_\lambda(t(\lambda))\).
Stationarity gives \(\partial_{\lambda_v}M=-H_v\).
For \(0\le\lambda\le\mu\le1\), integrate (15) to obtain
\[
 0\le M(\lambda)-M(\mu)
   \le\frac12\sum_v U_{|n_v|,d_v}(\mu_v^2-\lambda_v^2)
   <\frac3{40}\sum_vd_v(\mu_v^2-\lambda_v^2)
 \tag{17}
\]
when at least one coordinate changes. In particular, completing a
set of selected vertices costs less than \(3/40\) per incidence.
The vertices and all their original edges stay in the graph;
only their charges and angles are set to zero.

## 3. Every mixed vertical current

Choose the largest physical midpoint \(T_N\le\pi/2\).
For all sufficiently large levels, \(3/2\le T_N\le\pi/2\).
At a horizontal vertex use \(t_v=x_v-iH_v\),
\(-T_N\le x_v\le T_N\). At a vertical vertex use
\(t_v=\sigma_v T_N+ih_v\), \(-H_v\le h_v\le H_v\),
where \(\sigma_v=\operatorname{sgn}n_v\).
For a vertical subset \(J\), the exact exponential modulus is
\[
 \mathcal E_J=
 \Re\left\{\sum_e\psi(t_v,t_w)+
                      \sum_{v\in I}\frac{i n_vt_v^2}{4\pi}\right\}
    -\sum_{v\notin J}H_v-\sum_{v\in J}|h_v|.
 \tag{18}
\]
The degree sum is taken over the original graph even after some
coordinates have been completed.

Hold the other coordinates fixed. At a vertical vertex,
\[
 \partial_{h_v}\mathcal E_J
    =\frac1\pi\sum_{w\sim v}\Im r_{vw}
            -\frac{|n_v|T_N}{2\pi}-\operatorname{sign}h_v.
 \tag{19}
\]
This is the derivative of the original phase and its folded
vertical trace penalty. No Fourier coefficient has been discarded.
The one-edge estimates in the
[vertical-current proof](research_path_mixed_trace_currents.md#9-vertical-current-monotonicity-at-powers-of-at-least-seven)
apply with either sign of \(\sigma_v\). For \(h_v\le0\),
\(\Im\tan(t_v/2)\le0\), \(|\Re\tan(t_v/2)|\le1\),
\(\Re\cos(t_w/2)>7/10\), and
\(|\Im\cos(t_w/2)|<4/35\). A positive imaginary return
therefore satisfies \(\Im r_{vw}<5/42\).
The asinh argument stays in the right half-plane for \(\sigma_v=1\)
and the left half-plane for \(\sigma_v=-1\); the original branch
has \(|\Im r|<\pi/2\) in either case.

For \(h_v<0\) and \(d_v\ge2\), equations (1) and (19) give
\[
 \partial_{h_v}\mathcal E_J
 \le1+\frac{5d_v}{42\pi}-\frac{3d_v}{\pi}
       =1-\frac{121d_v}{42\pi}<-\frac56<-\frac45.
 \tag{20}
\]
For \(d_v=1\), use \(|n_v|\ge8\) to bound it by
\(1-247/(42\pi)<-4/5\).
For \(h_v>0\), the bound \(\Im r<\pi/2\) gives
\[
 \partial_{h_v}\mathcal E_J
       <d_v/2-3d_v/\pi-1<-1.
 \tag{21}
\]
Both one-sided comparisons hold at zero. Thus each vertical height
can be decreased to its bottom endpoint, with a loss of at least
\((4/5)(h_v+H_v)\) in the original direction of integration.
This estimate is valid while other vertices lie anywhere on their
horizontal or vertical segments.

On the whole wide rectangle the phase-only edge Hessian obeys
\(\Re[-2\pi\psi'']\succeq I_2/10\). Summing it over
edges gives, at every bottom horizontal point,
\[
 \Re\Phi(\mathbf x-i\mathbf H)
 \le M(\mathbf1)-\frac1{40\pi}
                       \sum_{v\in I}d_v(x_v-\Re t_v^*)^2.
 \tag{22}
\]
For a vertical vertex,
\(|\sigma_vT_N-\Re t_v^*|>3/5\), by (14).
Combining (19)–(22) proves, for every nonempty \(J\),
\[
 \mathcal E_J<M(\mathbf1)-\frac1{400}\sum_{v\in J}d_v
                         -\frac45\sum_{v\in J}(h_v+H_v).
 \tag{23}
\]
The same proof applies to any partial-charge source whose nonzero
charges are one. Zero-charge vertices are fixed at zero, with all
incident edge factors retained. No estimate introduces a factor
proportional to the total number of vertices.

## 4. The exact finite trace and its discarded rows

Apply the original derivative-sampling formula (12) and midpoint
identity (13) of
[the path-source assembly](research_uniform_path_trace_assembly.md#3-a-nonzero-coefficient-in-the-original-trace)
to each selected variable. These are one-variable identities in the
full Frobenius algebra and place no restriction on its degree in
the graph. Interchanging them is an operation on finitely many sums
and ordinary derivatives.

For the retained rows, the identity is a sum over every subset of
vertical vertices. A negative-side vertical contour retains its
extra factor \(-1\); the exact sign of a subset is their product.
The lower horizontal factor always has principal charge \(+1\),
with coefficient exactly one, for either sign of the crossing power.
The full wide-kernel theorem converts (23) into a bound for these
actual finite integrands and all their original normals.

The all-horizontal phase has its unique maximum at \(t^*\) and
\[
              \Re\mathcal H\succeq
                          \frac1{20\pi}\operatorname{diag}(d_v)>0.
 \tag{24}
\]
At each fixed graph all positive depths \(H_v\) are fixed.
The higher charges of the rational trace denominators are therefore
exponentially smaller. The original edge amplitudes and sine
factors are nonzero at the saddle. The Gaussian calculation is
exactly (6): there are \(N^{2m}\) from the trace prefactors,
\(N^{-3e/2}\) from all original edges, and \(N^{-m/2}\)
from the Gaussian. This gives the power in (5), with no new
normalization depending on the degree. Odd Gaussian moments vanish,
giving the stated \(O(N^{-1})\) error and all further fixed orders.

It remains to retain the rows outside the midpoint interval. Let
\(S\ne\varnothing\) be the set of vertices at those physical
rows. Keep their exact crossing values and first normals, and set
their analytic charges to zero. The full centered-incidence bounds
in Section 8 of the
[mixed-current note](research_path_mixed_trace_currents.md#8-a-stronger-centered-loss-for-a-removed-incidence)
give an exponent loss \(21/200\) for each incidence at a removed
vertex. An edge with both endpoints removed retains both losses.
The comparisons hold for all ordinary mixed spectral derivatives.
Their strict reserve permits the \(O(N^{-1})\) midpoint change
from \(\pi/2\), at both parities.

For the remaining exact traces choose the stationary heights of the
partial-charge solution. Their exponents are the original
partial-charge phase, with the removed coordinates zero, minus
\((21/200)\sum_{v\in S}d_v\). The wide-kernel theorem and
(23) apply to all of their horizontal and vertical terms.
The crossing values at removed real rows have modulus one;
their derivatives and all finite sampling weights cost powers of
\(N\) only. Distributing a first normal over arbitrarily many
incident factors is a finite product-rule expansion at a fixed
graph. It changes polynomial prefactors, not exponential rates.
By (17), the rate of the entire outside-row contribution is
\[
  <M(\mathbf1)
       -\left(\frac{21}{200}-\frac3{40}\right)
                         \sum_{v\in S}d_v
   =M(\mathbf1)-\frac3{100}\sum_{v\in S}d_v.
 \tag{25}
\]
If no trace remains, the same comparison retains the complete-edge
constants and needs no integral. There are finitely many subsets
and product-rule terms, so none can cancel the leading Gaussian.
This proves (5) for the complete outside colors.

The removed-incidence lemma already controls its other endpoint
throughout the complex wide rectangle. It therefore applies directly
to a small complex perturbation of an unselected angle near zero;
no inference from bounds only at its physical values is needed.
On every retained edge the full kernel bound and phase are holomorphic
on a fixed neighborhood of the contour. All the current and removed-row
comparisons have strict gaps, and there are finitely many subsets for
the fixed graph. A sufficiently small outside neighborhood preserves
them, while the implicit function theorem continues each required
stationary point inside the local kernel domain. The holomorphic
Gaussian expansion follows there. Separate evenness descends the
phases, amplitudes and normalized errors to ordinary spectral colors
near the ramified complete point; Cauchy's estimates then give all
asserted ordinary outside derivatives. This completes the analytic
proof of Theorem 1. \(\square\)

## 5. The original circle-tree geometry

Now suppose \(\Gamma\), its page ordering and carriers arise from
an original ordered circle-tree exterior. Retain its disk longitudes,
meridians, every main component and every marked annular interface.
Choose the original integer fillings \(p_v\) with
\[
                         n_v=\eta_v-2p_v
 \tag{26}
\]
satisfying (1). The angle solution just constructed supplies the
hypotheses of
[the positive marked-completion theorem](research_positive_point_marked_completion.md).
To see positivity directly, put \(w_v=\tan(t_v^*/2)\).
By (9), the sum of squared imaginary parts at either edge is
less than \(1/8\). On the branch
\(q_e=\sqrt{1+w_v^2+w_w^2}\),
\[
 (\Re q_e)^2\ge
      1+(\Re w_v)^2+(\Re w_w)^2
                      -(\Im w_v)^2-(\Im w_w)^2
          >(\Re w_v)^2+(\Re w_w)^2.
 \tag{27}
\]
This is positivity of all eight original tetrahedra on that edge.
The selected heights are strictly negative, and (8) at unit charge
is exactly the original full logarithmic period equation
\(\sum r_{vw}=i n_vt_v/2-\pi i\). There is no change of
peripheral basis or replacement of a slope by its absolute value.
The marked-completion theorem therefore proves
\[
                     \operatorname{Vol}Y(\mathbf p)
                               =2\pi\Re\Phi(t^*).
 \tag{28}
\]
Every main cusp and unselected auxiliary cusp remains complete.

**Corollary 2.** If all auxiliary vertices are filled, the original
strand tracing gives one main component and no internal closed
component, and (1), (26) hold, the resulting knot satisfies the
original full-level Kashaev volume conjecture:
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
                \log|\langle K\rangle_N|
                         =\operatorname{Vol}(S^3\setminus K).
 \tag{29}
\]
Its complete asymptotic has the nonzero leading coefficient (6),
with only the already retained unit carrier and zero-framing factors.

This conclusion uses the original circle-tree source identification
and the literal component test. No knot interpretation is attached
to an arbitrary graph in the analytic theorem. It also does not imply
finite exceptions in every original parameter template: assignments
with a short power at a fixed vertex remain outside (1), even when
other powers grow without bound.

The scalar margins are reproduced by
[check_degree_controlled_network_source.py](../experiments/check_degree_controlled_network_source.py),
with the
[saved record](../repro/results/research-degree-controlled-network-source.json).
These exact checks verify constants used above; the graph-independent
source decomposition and the marked geometry have written proofs.
