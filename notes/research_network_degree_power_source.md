# Adjacent graph fillings controlled by degree and crossing power

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The original finite source has a nonzero geometric contribution on any
fixed graph of same-index edges if
\[
                    n_v^2+d_v^2\ge4096
                 \quad\hbox{at every selected vertex }v.
 \tag{1}
\]
Here \(d_v\) is the actual incidence degree, with loops counted twice,
and \(n_v\) is the original fixed integer crossing power. Signs may
differ and zero powers are allowed. Selected vertices may be adjacent;
all vertices may be selected. No edge is duplicated to increase a
degree.

This is a theorem for the specified original finite source. An
arbitrary graph is not thereby identified with a knot presentation.
For an original marked circle-tree realization, the positive shapes
and original period equations below supply the analytic input to its
separate marked-completion theorem.

## 1. The exact source and the conclusion

Let \(\Gamma=(V,E)\) be a fixed finite undirected graph, allowing
loops and repeated edges. Choose a nonempty selected set \(I\);
no selected vertex is isolated. Unselected angles are initially zero.
Use the full original Newton kernel and Hermite trace
\[
 \begin{split}
 K_N(t,u)&=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u),\\
 Z_{\Gamma,I,N}
   &=\left(\prod_{v\in I}\phi_N^{(w_v)}\right)
       \left[\prod_{v\in I}R(w_v)^{n_v}
                    \prod_{\{v,w\}\in E}K_N(t_v,t_w)\right],
                  \qquad w_v=-2\cos t_v .
 \end{split}
 \tag{2}
\]
Every product is formed before taking the trace in its variable.
All double-root first normals and the odd simple-root term are
retained. A loop contributes \(K_N(t_v,t_v)\) once.

Put \(m=|I|\), \(e=|E|\), \(R_v=(n_v^2+d_v^2)^{1/2}\), and
\[
 \Phi_{\boldsymbol\chi}(\mathbf t)
 =\sum_{\{v,w\}\in E}\psi(t_v,t_w)
       +\sum_{v\in I}
           \left(\frac{in_vt_v^2}{4\pi}-i\chi_vt_v\right).
 \tag{3}
\]
The edge phase has its original normalization
\(\psi(0,0)=M_\infty=4G/\pi\) and
\(\psi_t(t,u)=-\operatorname{asinh}(\tan(t/2)\cos(u/2))/\pi\).
The charge cube in (3) is used only to compare stationary actions;
no quantum source at nonintegral charge is assumed.

**Theorem 1.** Assume (1). The whole cube
\(\boldsymbol\chi\in[0,1]^I\) has a unique critical point in
\(|t_v|\le1/10\), continuing from the complete point. Its original
edge shapes are positive. At unit charges write \(t^*=\mathbf t(\mathbf1)\),
\(\Phi=\Phi_{\mathbf1}\), \(M=\Re\Phi(t^*)\), and
\(\mathcal H=-\Phi''(t^*)\). Along all sufficiently large integer
levels, at both parities,
\[
 \begin{split}
 Z_{\Gamma,I,N}
 &=\varepsilon_N N^{3(m-e)/2}
                    \mathcal A\,e^{N\Phi(t^*)}(1+O(N^{-1})),\\
 \varepsilon_N
 &=\prod_{v\in I}
       \exp\!\left(\frac{\pi i n_v(N-1)^2}{4N}\right),\\
 \mathcal A
 &=\left(\frac{i}{\pi}\right)^m(2\pi)^{m/2}
       \frac{\displaystyle\prod_{v\in I}\sin t_v^*
              \prod_{\{v,w\}\in E}a_e(t_v^*,t_w^*)}
                    {\sqrt{\det\mathcal H}}\ne0 .
 \end{split}
 \tag{4}
\]
The Gaussian branch is the one on complex symmetric matrices with
positive definite real part. The expansion has every fixed inverse-power
order. It continues to a fixed small complex neighborhood of all
complete outside colors, with all fixed ordinary spectral derivatives.

The constants and first valid level may depend on the fixed graph
and powers. The explicit geometric and comparison bounds below do
not depend on graph size. In particular every selected vertex of
actual degree at least \(64\) permits any fixed integer power,
including zero, even next to other selected vertices.

## 2. Unit-charge contraction weighted by the actual degree

For one incidence define the removable holomorphic function
\[
 f(t,u)=\frac{2\operatorname{asinh}(\tan(t/2)\cos(u/2))}{t}-1.
 \tag{5}
\]
On \(|t|,|u|\le1/5\), elementary disk estimates give
\[
 \begin{split}
 |\tan(t/2)-t/2|&\le |t|^3/16,
       &|\tan(t/2)|&\le(51/100)|t|,\\
 |\cos(u/2)-1|&\le |u|^2/7,
       &|\cos(u/2)|&\le101/100,\\
 |\operatorname{asinh}z-z|&\le |z|^3/5
                              &&(|z|\le11/100).
 \end{split}
 \tag{6}
\]
For completeness, on the disk of radius \(1/10\),
\(|\tan z|\le(51/50)|z|\) follows from
\(|\sin z|\le\sinh|z|\) and
\(|\cos z|\ge2-\cosh|z|\). Integrating \(\tan^2z\) gives
the first bound. The positive cosh series gives the cosine
bounds. Finally integrate the binomial derivative bound
\[
 |(1+z^2)^{-1/2}-1|
       \le\frac{|z|^2}{2(1-(11/100)^2)^{3/2}}.
\]
The asinh argument in (5) has magnitude at most
\((51/100)(1/5)(101/100)<11/100\).
Consequently
\[
 |f(t,u)|
 \le\left[\frac18+\frac25
          \left(\frac{51}{100}\frac{101}{100}\right)^3\right]|t|^2
                      +\frac{51}{350}|u|^2
 <\frac13\max(|t|,|u|)^2 .
 \tag{7}
\]

Set \(r=1/10\), \(\epsilon=1/300\), and
\(C_v(\mathbf t)=\sum_{w\sim v}(1+f(t_v,t_w))\), with
one summand per incidence. On the polydisk \(|t_v|\le r\),
\[
 |C_v-d_v|\le d_v\epsilon,\qquad
           \sum_w|\partial_{t_w}C_v|\le\frac4{15}d_v.
 \tag{8}
\]
For the derivative apply Cauchy's inequality in each incidence
argument, using (7) on the doubled disk. Each partial derivative
is at most \(4r/3\). A loop adds both derivatives, exactly as
its two incidences require.

The stationary equations are precisely
\[
 t_v=\mathcal T_v(\mathbf t)
       =\frac{2\pi\chi_v}{n_v+iC_v(\mathbf t)}.
 \tag{9}
\]
By (1) and (8),
\[
 \begin{split}
 |n_v+iC_v|&\ge(1-\epsilon)R_v,\\
 |\mathcal T_v|&\le\frac{825}{8372}<\frac1{10},\\
 \|D\mathcal T\|_\infty
   &\le\frac{16500}{625807}<\frac1{32}.
 \end{split}
 \tag{10}
\]
These rational bounds use \(R_v\ge64\), \(d_v\le R_v\),
and \(\pi<22/7\). Banach's theorem proves uniqueness and
holomorphic local dependence on the charge parameters.

Write \(C_v=A_v+iB_v\). Since \(A_v\ge(299/300)d_v>0\),
\[
 \begin{split}
 H_v:=-\Im t_v
 &=\frac{2\pi\chi_v A_v}
            {(n_v-B_v)^2+A_v^2},\\
 0<H_v&<\frac{32}{5}\frac{\chi_vd_v}{R_v^2}
                                      \le\frac{\chi_v}{10}
                     \quad(\chi_v>0),\\
 t_v&=0\quad(\chi_v=0).
 \end{split}
 \tag{11}
\]
The coefficient before \(d_v/R_v^2\) is at most
\(567600/89401<32/5\).
For a subset \(S\subseteq I\), set its charges to zero.
The exact stationary derivative
\(\partial_{\chi_v}\Re\Phi_{\boldsymbol\chi}=\Im t_v=-H_v\)
then gives
\[
 0\le M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
 \le\frac{16}{5}\sum_{v\in S}\frac{d_v\chi_v^2}{R_v^2}
                 \le\frac1{1280}\sum_{v\in S}d_v.
 \tag{12}
\]

The edge shapes are those continued from completeness.
For \(|t_v|\le1/10\), \(|\tan(t_v/2)|\le51/1000\).
Thus for each edge the branch
\(q_e=\sqrt{1+\tan^2(t_v/2)+\tan^2(t_w/2)}\)
has real part greater than \(99/100\), while the Euclidean norm
of the two real tangent parts is less than \(1/10\).
The [positive-edge criterion](research_positive_edge_global_monotonicity.md)
therefore proves positivity of all original edge shapes.
The continuation (9) fixes the original logarithmic periods,
including at zero powers and without a complete outside vertex.

## 3. Refined edge estimates on the actual contour heights

The retained contour uses the larger real range
\[
             |\Re t|,|\Re u|\le\pi/2,\qquad
                       |\Im t|,|\Im u|\le1/10 .
 \tag{13}
\]
Write \(w=\tan(t/2)\), \(z=\tan(u/2)\) and
\[
 K(t,u)=-2\pi\psi''(t,u)
 =\frac1s\begin{pmatrix}1+w^2&-wz\\-wz&1+z^2\end{pmatrix},
                      \qquad s^2=1+w^2+z^2.
 \tag{14}
\]
The branch continues from \(s=1\).
On (13), \(|w|,|z|\le1\) and
\(|\Im w|,|\Im z|\le1/10\). Also
\(|\partial_{\Im t}\tan(t/2)|\le1\).

Here is a direct quantitative comparison with real angles.
Put \(A=|w|^2\), \(B=|z|^2\). Differentiating (14) gives
\[
 \|\partial_wK\|_F^2
 \le\frac{A(1+A+2B)^2+(2B+A)(1+B)^2}{|s|^6}
 \le\frac{2}{(24/25)^3}<\left(\frac85\right)^2.
 \tag{15}
\]
Indeed \(|s|^2\ge(24/25)(1+A+B)\), and
\[
 \begin{split}
 2(1+A+B)^3
 &-\{A(1+A+2B)^2+(2B+A)(1+B)^2\}\\
 &=A^3+2A^2B+4A^2+AB^2+6AB+4A+2B^2+4B+2\ge0.
 \end{split}
\]
The same estimate holds for \(\partial_zK\).
Integrating the two vertical parameter changes gives
\(\|K(t,u)-K(\Re t,\Re u)\|_2\le8/25\).
At real angles the two eigenvalues of (14) are
\(s\) and \(1/s\), with \(1\le s\le\sqrt3\).
Since \(1/\sqrt3>4/7\) and \(\sqrt3<7/4\), we obtain
\[
 \Re K\succeq\frac14 I,\qquad
             \|\Re K\|_2<\frac{21}{10},\qquad
             \|\Im K\|_2\le\frac8{25}.
 \tag{16}
\]
These estimates hold for either sign of each angle and height.

Sum (16) over the actual edges and extend selected vectors by
zero at outside vertices. For real vectors \(a,b\), set
\(A_2=\sum_vd_va_v^2\), \(B_2=\sum_vd_vb_v^2\).
The same inequalities hold in this degree-weighted norm, by
Cauchy--Schwarz over incidences. Loops use the same coordinate
twice and are already included.

## 4. Every original mixed trace current has a gap

Choose the largest physical midpoint \(T_N\le\pi/2\).
For all sufficiently large \(N\), \(T_N\ge3/2\).
Apply the exact Hermite rectangle identity at each retained
selected variable, with lower height \(-H_v\).
For a vertical coordinate use the side \(\sigma_vT_N\), where
\(\sigma_v=\operatorname{sgn}(n_v)\) for \(n_v\ne0\) and
\(\sigma_v=1\) for \(n_v=0\).
The exact side-reflection factor \(\sigma_v\) is retained.

For a nonempty set \(S\) of vertical coordinates, write
\(t-t^*=a+ib\). Then \(b_v=0\) outside \(S\), while
\[
 |a_v|>7/5,\qquad 0\le b_v\le1/5,\qquad n_va_vb_v\ge0
                                                    \quad(v\in S).
 \tag{17}
\]
The last inequality follows from
\(|t_v^*|<1/10<T_N\); it does not require a sign assertion
for \(\Re t_v^*\), and it includes \(n_v=0\).

Let \(\mathcal E_S\) be the actual exponential modulus of
the mixed current. Its vertical trace penalty is \(-|h_v|\),
so \(\mathcal E_S\le\Re\Phi(t)\). Taylor's formula at the
full complex critical point, keeping the chirp exactly, gives
\[
 \begin{split}
 \mathcal E_S-M
 &\le\frac1{4\pi}
   \left[-\frac14A_2+\frac{21}{10}B_2
                         +\frac{16}{25}\sqrt{A_2B_2}\right]
                  -\frac1{2\pi}\sum_vn_va_vb_v\\
 &\le-\frac{A_2}{32\pi}+\frac{3B_2}{4\pi}
                  -\frac1{2\pi}\sum_vn_va_vb_v\\
 &<-\frac1{32\pi}\sum_{v\in S}d_v
                       <-\frac1{110}\sum_{v\in S}d_v.
 \end{split}
 \tag{18}
\]
The Young inequality used here is
\((16/25)\sqrt{AB}\le A/8+(512/625)B\), and
\(21/10+512/625<3\).
The final loss follows from \(49/800-3/100=1/32\).
The straight segment from \(t^*\) to every mixed point stays
in (13), so all averaged Hessian estimates used in (18) are
valid. No favorable chirp is needed at a zero-power vertex.

The [full wide-kernel theorem](research_bare_kernel_thin_rectangle.md#6-the-full-rectangle-through-real-angle-pi-over-two)
turns (18) into a bound for each actual finite mixed integrand.
The exact trace identity is applied to the whole incident
product, including loops, and carries all first normals.
No independent edge contour or discarded alias is introduced.

## 5. Removing original physical rows before the contour

Partition the original derivative-sampling trace by its set \(S\)
of vertices whose physical angles lie outside \((-T_N,T_N)\).
For a nonempty \(S\), keep its literal crossing values and normals,
and deform only the remaining traces at the stationary point
whose charges on \(S\) are zero.

The [centered incidence estimates](research_path_mixed_trace_currents.md#8-a-stronger-centered-loss-for-a-removed-incidence)
give a loss \(21/200\) at each removed incidence. They hold
on the full retained box, including all fixed ordinary derivatives.
When both endpoints of an edge are removed, their two losses are
both retained. The strict reserve in those estimates allows the
\(O(N^{-1})\) midpoint shift below \(\pi/2\).
A loop at a removed vertex likewise has both losses. Equivalently,
Markov's inequality can be applied to its diagonal polynomial,
whose degree is at most \(2(N-1)\).

After centering, the remaining upper phase is exactly (3) with
the removed vertices fixed at zero. The actual degrees retain
their incidences to these newly complete vertices. Equation (12)
therefore proves
\[
 \operatorname{rate}(S)
 \le M(\mathbf1)-\left(\frac{21}{200}-\frac1{1280}\right)
                                    \sum_{v\in S}d_v
 < M(\mathbf1)-\frac1{10}\sum_{v\in S}d_v.
 \tag{19}
\]
All crossing values on the physical real grid have modulus one,
and their first normals cost only powers of \(N\) for the fixed
integer powers. At zero power that crossing normal vanishes.
Every mixed ordinary derivative of the fixed incident products
also has only polynomial cost. These comparisons retain all
physical rows at both level parities.

## 6. The nonzero coefficient and the source scope

On the all-horizontal rectangle the real Hessian satisfies
\[
                  \Re[-\Phi''(t)]
                        \succeq\frac1{8\pi}
                                   \operatorname{diag}(d_v)>0.
 \tag{20}
\]
The real phase is therefore strictly concave, with its unique
maximum at \(t^*\). Every fixed complement of its neighborhood
has a strict gap. The full wide-kernel expansion supplies the
actual nonzero local edge amplitudes.

Each horizontal trace has exact prefactor \(iN^2C_{N,n_v}/\pi\)
and rational kernel
\[
           \frac{e^{-iNt_v}}
               {(1-(-1)^{N-1}e^{-iNt_v})^2}.
 \tag{21}
\]
All unit-charge heights in (11) are strictly positive for the
fixed graph and powers. Hence the leading Fourier term in (21)
has coefficient exactly one, and all its higher charges are
exponentially smaller on this same contour. There is no coupon
coefficient \(1/2\): the source (2) has no coupon.

The product of edge amplitudes and \(\sin t_v^*\) is nonzero.
The latter factors cannot vanish because \(H_v>0\) and
\(|t_v^*|<1/10\). Equation (20) gives a nonzero complex Gaussian
determinant. The powers of \(N\) are \(2m\) from the traces,
\(-3e/2\) from the edges and \(-m/2\) from the Gaussian,
giving (4). Bounds (18)--(19) prevent the rest of the original
source from canceling this term. Higher local expansion orders
follow from the same uniform holomorphic kernel expansion.

The outside continuation is an estimate on an actual complex
neighborhood, not continuation of a bound at one boundary value.
Allow each unselected angle to vary in a sufficiently small closed
disk \(|u_w|\le r_0<1/10\). The same incidence estimates (7)--(10)
apply with these angles fixed; thus the selected critical point is
jointly holomorphic, stays in \(|t_v|<1/10\), and has strictly
positive depth by (11). On each retained contour every selected
and outside argument is in the wide kernel box. The Hessian
comparison (16) still applies after putting the displacement zero
at the outside vertices.

For an edge meeting a removed physical row, the complex selected
endpoint in the centered incidence lemma may equally be an
unselected outside angle. Its bound is exactly
\(\Re\psi(0,u_w)-21/200\), with every fixed ordinary derivative.
Edges with two removed ends use the two-endpoint version.
Thus (19) holds with these actual complex outside parameters and
the corresponding continued stationary action. The charge
comparison (12) remains valid: \(A_v=\Re C_v>0\) also for these
complex fixed outside angles. No estimate is inferred merely
from the complete value. The same exact trace and normal
bookkeeping is recorded for the complementary power-degree
regime in
[the network source theorem](research_degree_controlled_network_source.md).

All inequalities have strict reserves. For the fixed graph and
powers, the unit-charge depths have a positive lower bound on
a smaller compact outside polydisk, so all Fourier-charge errors
remain exponentially small there. The resulting phase, amplitude
and normalized remainder are holomorphic and separately even
in every outside angle, by the exact source symmetry and uniqueness
of the small stationary branch. They therefore descend to
holomorphic functions of the ordinary colors \(-2\cos u_w\)
near \(-2\). Cauchy's formula on smaller ordinary-color disks
gives every fixed normal, including at the ramified complete
angle. It does not assert that a derivative of a nonzero amplitude
is itself nonzero.

The [exact scalar checker](../experiments/check_network_degree_power_source.py)
verifies the disk, contraction, matrix and current constants,
including the polynomial identity behind (15). Its
[saved record](../repro/results/research-network-degree-power-source.json)
records the proof and source dependencies. No numerical pattern
or norm-to-overlap assumption enters the proof.

This criterion extends the isolated high-degree mechanism to
adjacent selected vertices in the original finite source. It does
not identify arbitrary graphs with knot invariants, combine different
edge kernels, or settle all assignments having a vertex that fails
(1).

## 7. The original marked circle-tree consequence

Suppose now that the graph, page order, disk frames and carriers
come from the original ordered circle-tree exterior. Retain its
original meridians, disk longitudes, main components and marked
annular interfaces. For the actual integer filling coefficients
\(p_v\), impose
\[
 n_v=\eta_v-2p_v,\qquad n_v^2+d_v^2\ge4096,
 \qquad\hbox{primitive filled curve }
                     \mu_v+p_v\lambda_v^{\mathrm{disk}}.
 \tag{22}
\]
No change of peripheral basis is made, including when \(n_v=0\).

The positive shapes from Section 2 and the continued unit-charge
equations are precisely
\[
 n_vt_v^*+2i\sum_{w\sim v}r_{vw}(t^*)=2\pi,\qquad
                          \Im t_v^*<0.
 \tag{23}
\]
Their logarithmic lifts are fixed along the actual small solution
on the whole charge cube. The
[positive-point marked-completion theorem](research_positive_point_marked_completion.md)
therefore applies to this original marked presentation. If
\(Y(\mathbf p)\) is its partial exterior, every main cusp and
every unselected auxiliary cusp remains complete, and
\(\operatorname{Vol}Y(\mathbf p)=2\pi M\).
The edge constants in (3) are included in this absolute equality.

**Corollary 2.** If all auxiliary vertices are filled, the original
strand tracing gives one main component and no internal closed
component, and (22) holds, then the resulting knot satisfies the
original full-level Kashaev volume identity
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
                 \log|\langle K\rangle_N|
                    =\operatorname{Vol}(S^3\setminus K).
 \tag{24}
\]
The leading coefficient is nonzero by (4), with the original
carrier and zero-framing unit factors retained. This consequence
uses the original circle-tree source identification and literal
component tests. It attaches no knot interpretation to an arbitrary
graph in Theorem 1, and it does not assert finite exceptions for
templates having selected vertices outside (22).

## 8. Mixing the degree and power regimes at adjacent vertices

The hypotheses of the two network theorems can also be combined
vertex by vertex, with a larger degree-power threshold at vertices
of the second type. This is a new mixed statement, not an inference
from the two separate theorems.

**Theorem 3.** In the exact graph source (2), suppose each selected
vertex is assigned one of the following types:
\[
 \begin{array}{ll}
 P:& |n_v|\ge\max(8,4d_v),\\
 D:& R_v=\sqrt{n_v^2+d_v^2}\ge512.
 \end{array}
 \tag{25}
\]
Then the nonzero original source expansion (4), at both parities
and to every fixed order, holds. Its complex outside-color
continuation and all ordinary normals hold as well. The original
marked circle-tree conclusion of Section 7 holds with (25) in
place of (22)'s size condition. Degrees are always the original
incidence degrees. In particular a high-degree vertex with any
fixed power, including zero, can be adjacent to vertices satisfying
the first condition. No topology is changed to meet (25).

**A hybrid contraction.** Use the product domain
\[
 \mathcal B_v=
 \begin{cases}
 \{t:|\Re t|\le1,\ |\Im t|\le1/3\},&v\text{ of type }P,\\
 \{t:|t|\le1/40\},&v\text{ of type }D.
 \end{cases}
 \tag{26}
\]
Every incidence is in the first, larger box. On this box the
one-edge estimates in Section 2 of
[the power-dominated network proof](research_degree_controlled_network_source.md)
give \(|K_{vv}-1|<2/5\),
\(|K_{vv}|+|K_{vw}|<86/45\),
\(|\tan(t/2)|<3/5\), and
\(|\Im\tan(t/2)|<1/4\).
Define the removable quotient
\[
 C_v=\sum_{w\sim v}\int_0^1 K_{vv}(\sigma t_v,t_w)\,d\sigma,
              \qquad |C_v-d_v|<\frac25d_v.
 \tag{27}
\]
This is the same \(C_v=2\sum r_{vw}/t_v\) as in (9).

For a derivative bound, the polynomial calculation (15), now
using \(|\Im\tan(t/2)|<1/4\), gives
\(\|\partial_w K\|_F^2\le2/(3/4)^3<(9/4)^2\).
Also
\[
 |\partial_t\tan(t/2)|
    =\frac1{\cosh\Im t+\cos\Re t}<\frac23,
\]
since \(\cos1>1/2\). Hence \(\|\partial_t K\|_F<3/2\).
The two derivatives of an incidence in (27) are bounded by
\(3/4\) and \(3/2\), respectively, so
\[
             \sum_w|\partial_{t_w}C_v|<\frac94d_v.
 \tag{28}
\]
For a loop both derivatives are included in each of its two
incidences. This is also the correct row count for the original
period equation and its Hessian.

At a \(P\) vertex use the direct-return map
\(2\pi\chi_v/n_v-(2i/n_v)\sum r_{vw}\).
The cited proof maps into the interior of its box and bounds its
Jacobian row by \(43/90\), independently of the neighbor types.
At a \(D\) vertex use the quotient map (9). Equations (27)--(28)
give
\[
 \begin{split}
 |n_v+iC_v|&>\frac35 R_v,\\
 |\mathcal T_v|&<\frac{55}{2688}<\frac1{40},\\
 \sum_w|\partial_{t_w}\mathcal T_v|
    &<\frac{25\pi}{2R_v}
      \le\frac{550}{7168}<\frac1{12}.
 \end{split}
 \tag{29}
\]
Thus the hybrid map is a contraction on (26), for every
\(\boldsymbol\chi\in[0,1]^I\). Both formulas solve exactly
the same original period equations, not modified vertex equations.
They also give holomorphic dependence in a neighborhood of the
charge cube. Zero charge gives zero angle; positive charge gives
strictly positive depth because \(\Re C_v>3d_v/5\).

The \(P\)-vertex estimates remain
\(|t_v|<9/10\), \(H_v<3/10\), and
\(H_v\le U_{|n_v|,d_v}\chi_v\), with
\(U_{|n_v|,d_v}/(2d_v)<3/40\).
At a \(D\) vertex, besides \(|t_v|<1/40\),
\[
 H_v\le\frac{70\pi}{9}\frac{d_v}{R_v^2}\chi_v,
 \qquad
 \frac{35\pi}{9R_v^2}<\frac3{40}.
 \tag{30}
\]
Consequently completing any selected subset costs less than
\((3/40)\sum d_v\) in stationary real action. Positivity of
all original edge shapes follows on the larger box just as in the
cited network proof: the sum of the two squared imaginary tangent
parts is less than \(1/8\), so the positive-edge criterion holds.
Continuation from zero fixes all original logarithmic periods.

**A stronger wide-rectangle Hessian bound.** On
\(|\Re t|,|\Re u|\le\pi/2\),
\(|\Im t|,|\Im u|\le3/10\), one has
\[
                  \Re K\succ\frac13 I,
 \qquad \|\Re K\|_2,\ \|\Im K\|_2<\frac{10}{3}.
 \tag{31}
\]
Here is a direct proof. Put \(w=\tan(t/2),z=\tan(u/2)\),
\(X=(\Re w,\Re z)\), \(Y=(\Im w,\Im z)\),
\(x=|X|^2\le2\), \(y=|Y|^2<9/50\), and
\(\alpha=\Re\sqrt{1+w^2+z^2}>0\).
The exact determinant/trace formula in
[the edge-Hessian proof](research_edge_hessian_and_phase_response.md)
gives
\[
 \lambda_{\min}(\Re K)
 \ge\frac{\alpha^2-\{\Im(w\bar z)\}^2}
           {\alpha(|s|^2+1)}
 \ge\frac{(41/50)\sqrt{1+x}}{2+x+9/50}>
                                                      \frac13.
 \tag{32}
\]
Indeed \(\alpha^2\ge1+x-y\),
\(\{\Im(w\bar z)\}^2=xy-(X\cdot Y)^2\),
\(\alpha^2\le1+x\), and \(|s|^2\le1+x+y\).
The last one-variable ratio has a single interior maximum;
its values at \(x=0,2\) exceed \(1/3\).
At \(x=2\) it suffices that \(\sqrt3>209/123\), which
follows by squaring. Finally the numerator matrix in (14) is
\(I+(w,-z)^T(w,-z)\), of norm at most three, while
\(|s|^2>41/50>(9/10)^2\). Thus \(\|K\|_2<10/3\),
proving the other assertions in (31).

**Mixed currents.** Keep the exact trace rectangles and all their
orientations. For a \(P\)-type vertical coordinate the proof of
(19)--(21) in the power-dominated note gives
\(\partial_{h_v}\mathcal E<-4/5\), while every other coordinate
may be anywhere on its own wide rectangle. Lower each such height
to \(-H_v\) in this pointwise upper estimate. This is not a
change of the exact current; it bounds its integrand, retaining
the \(-|h_v|\) penalty and its corner at zero.

At the resulting point write \(t-t^*=a+ib\).
Only \(D\)-type vertical coordinates can have \(b_v\ne0\).
For them choose the side \(\operatorname{sgn}(n_v)T_N\), or
\(+T_N\) at zero power. Then
\[
 \begin{array}{c|c|c}
   \text{vertical type}& |a_v|&b_v\\ \hline
   P&>3/5&0\\
   D&>59/40&0\le b_v<1/20
 \end{array}
 \qquad n_va_vb_v\ge0.
 \tag{33}
\]
The entire straight segment from the saddle to this point is in
the wide rectangle. Using (31) in Taylor's formula, and the same
degree-weighted \(A_2,B_2\) as in Section 3, gives
\[
 \begin{split}
 \mathcal E-M
 &\le\frac1{4\pi}
    \left[-\frac13A_2+\frac{10}{3}B_2+
                           \frac{20}{3}\sqrt{A_2B_2}\right]
              -\frac1{2\pi}\sum_vn_va_vb_v\\
 &\le-\frac{A_2}{24\pi}+\frac{35B_2}{2\pi}
              -\frac1{2\pi}\sum_vn_va_vb_v.
 \end{split}
 \tag{34}
\]
The Young inequality here uses
\((20/3)\sqrt{AB}\le A/6+(200/3)B\).
The loss per \(D\)-vertical incidence is greater than
\(1801/(38400\pi)>1/70\); the loss per already lowered
\(P\)-vertical incidence is greater than
\(3/(200\pi)>1/220\). Including the favorable height changes,
every nonempty original vertical set \(S\) therefore satisfies
\[
 \mathcal E_S<M-\frac1{220}\sum_{v\in S}d_v
                   -\frac45\sum_{v\in S\cap P}(h_v+H_v).
 \tag{35}
\]
This bound includes currents containing both vertex types.
Loops use the same two-incidence quadratic-form pullback as in
Section 3. No assertion of entrywise positivity or of a norm
lower bound is used.

For removed physical rows, (30) and the \(P\)-vertex action
budget combine with the original centered loss to give
\[
 \operatorname{rate}(S)<M-
       \left(\frac{21}{200}-\frac3{40}\right)
                          \sum_{v\in S}d_v
        =M-\frac3{100}\sum_{v\in S}d_v.
 \tag{36}
\]
Every partial-charge retained graph has the same hybrid bounds.
First normals, including derivatives of loop factors, have the
same finite product-rule bookkeeping as in Section 5. The odd
simple node and all trace aliases are unchanged.

The remaining source calculation is now exactly Section 6:
strict horizontal concavity, the unit coefficient of the leading
trace charge, nonzero sine and edge factors, and a nonzero
Gaussian determinant give (4); (35)--(36) bound the rest of the
actual source. All inequalities have strict margins. Small fixed
complex outside angles stay in the larger incidence box, preserve
the hybrid contraction, and are covered directly by the original
complex centered-incidence estimates. Even descent and Cauchy's
formula give the ordinary outside-color statement. The marked
conclusion then follows from the same original slopes, positive
completion and component tests as in Section 7. This proves
Theorem 3. \(\square\)
