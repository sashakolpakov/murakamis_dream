# Physical charge pressure and its geometric excess

Private written proof, 16 November 2026.

The whole original charged source has a graph-dependent exponential
envelope sharper than a constant plus its exponential type. All
physical first normals are included. The envelope is the pressure of
the positive physical kernel values, and does not depend on the real
crossing powers. At a supplied positive complex-charge geometric point
its excess over the selected zero-power action is an explicit positive
convex-energy difference. The resulting Fresnel-tail bound retains that
excess rather than replacing the physical pressure by the filled action.

## 1. The original source and its real pressure

Fix a finite original circle tree, a nonempty selected set \(I\), and
all edges incident to \(I\), counted once. Write \(k=|I|\) and \(m\)
for the number of these edges. Every selected vertex has positive
degree. Outside endpoints of these edges are fixed at their complete
angle \(0\), hence spectral value \(-2\). This is the specified
complete-boundary source. Edges having neither endpoint in \(I\) are
not included; their independent factors in a larger contraction must
be restored. No arbitrary exterior is discarded.

Put \(D=N-1\), \(\eta=(-1)^D\), and
\[
 \begin{gathered}
 c_j=2\cos((2j+1)\pi/N),\qquad
 S_r=\prod_{\nu=1}^r2\sin(\pi\nu/N),\\
 e_r(z)=S_r^{-2}\prod_{\nu<r}(c_\nu-z),\qquad
 K_N(z,w)=\sum_{r=0}^{D}e_r(z)e_r(w),\\
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f .
 \tag{1}
 \end{gathered}
\]
The distinct physical roots have angles
\[
 \tau_j=\pi(D-2j)/N,\qquad c_j=-2\cos\tau_j,\qquad
 0\le j\le\lfloor D/2\rfloor .
 \tag{2}
\]
Every \(\tau_j>0\) represents a double root; at odd \(N\) the last
angle is zero and represents the simple root \(-2\). The full trace is
\[
 \phi_N(f)=\eta\sum_{\tau_j>0}
   \{4\sin^2\tau_j\,f'(c_j)-c_jf(c_j)\}
       +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{3}
\]
Use the canonical real-power element \(R_n\) and entire charge coupon
\[
 \begin{aligned}
 C_\chi(c_j)&=\cos(N(1-\chi)\tau_j),\\
 C_\chi'(c_j)&=-\frac{N(1-\chi)}{2\sin\tau_j}
                  \sin(N(1-\chi)\tau_j),\qquad \tau_j>0,\\
 C_\chi(-2)&=1\quad(N\ {\rm odd}).
 \end{aligned}
 \tag{4}
\]
For real \(n\), the physical values of \(R_n\) have modulus one and
its first normals have polynomial bounds uniform on bounded real
power intervals. At integral \(n\) it is the original signed crossing
power. Define
\[
 Z_N(\mathbf n,\boldsymbol\chi)=\phi_N^{\otimes I}
 \left[\prod_{e=vw}K_N(z_v,z_w)
              \prod_{v\in I}R_{n_v}(z_v)C_{\chi_v}(z_v)\right].
 \tag{5}
\]
The exact carriers \(C_{N,n}=\exp(\pi i nD^2/(4N))\) have modulus
one for real \(n\); all bounds also apply to
\(\widetilde Z_N=(\prod_vC_{N,n_v}^{-1})Z_N\).

Let \(\psi(t,u)\) be the canonical original edge action and
\(M_\infty=\psi(0,0)\). On \((-\pi,\pi)^2\) it is real and
separately even, and extends continuously to the closed real square.
Set
\[
 W(\mathbf s)=\sum_{e=vw}\psi(s_v,s_w),\qquad s_b=0\ (b\notin I),
 \qquad
 \mathcal P(\mathbf b)=\max_{\mathbf s\in[-\pi,\pi]^I}
                       \{W(\mathbf s)+\mathbf b\cdot\mathbf s\}.
 \tag{6}
\]
This finite convex function is even in every \(b_v\), with
\[
 |\mathcal P(\mathbf b)-\mathcal P(\mathbf b')|
                    \le\pi\|\mathbf b-\mathbf b'\|_1 .
 \tag{7}
\]
All included outside-edge constants occur in \(W\); in particular
\(W(\mathbf0)=mM_\infty\).
The same notation \(W(\mathbf t)=\sum_e\psi(t_v,t_w)\) denotes its
canonical holomorphic extension on the original positive edge chart,
with the complete logarithmic branches retained.

**Theorem 1.** For a fixed graph and bounded real power box, constants
\(C,a\) independent of \(N\), its parity, and \(\boldsymbol\chi\) satisfy
\[
 |Z_N(\mathbf n,\boldsymbol\chi)|
 \le C N^a\prod_{v\in I}(1+|\chi_v|)
                    e^{N\mathcal P(\operatorname{Im}\boldsymbol\chi)}.
 \tag{8}
\]
Every repeated-root normal and every mixed normal from the original
tensor trace is retained. Its positive physical partition
\[
 \mathcal M_N(\mathbf b)=\sum_{\mathbf j}
      \prod_{e=vw}K_N(c_{j_v},c_{j_w})
              e^{N\sum_{v\in I}|b_v|\tau_{j_v}},
 \qquad c_{j_b}=-2\ (b\notin I),
 \tag{9}
\]
has the sharp rate
\[
 \lim_{N\to\infty}N^{-1}\log\mathcal M_N(\mathbf b)
                                      =\mathcal P(\mathbf b).
 \tag{10}
\]
This is a rate for (9), not for the signed scalar (5).

**Proof.** At a physical root,
\[
 e_r(c_j)>0\ (0\le r\le j),\qquad e_r(c_j)=0\ (r>j).
 \tag{11}
\]
Also \(e_r(-2)\ge0\), so every kernel value in (9) is at least one.
The archived full-normal identities give
\[
 \begin{aligned}
 |K_z(c_j,w)|&\le N^{11}K_N(c_j,w)
                   &&(-2\le w\le c_0,\ c_j\text{ double}),\\
 |\partial_z\partial_w\log K_N(c_j,c_l)|&\le N^{16}
                   &&(c_j,c_l\text{ double}),\\
 |K_{zw}(c_j,c_l)|&\le(N^{16}+N^{22})K_N(c_j,c_l).
 \end{aligned}
 \tag{12}
\]
These are full polynomial derivative identities, not derivatives of
the terminating values (11). At odd simple roots only evaluation is
required, and the first bound handles the other endpoint. The same
bound handles outside endpoints \(-2\).

Expand (3) by Leibniz at every vertex. Each edge receives at most one
derivative at either selected endpoint, and there are only a fixed
number of derivative placements per assignment. Thus (12) costs a
fixed polynomial relative to the positive kernel product. Crossing
normals also have polynomial cost. Since
\(N\tau_j=\pi D-2\pi j\) and \(\sin\tau_j\ge2/N\) at double roots,
\[
 |C_\chi(c_j)|\le e^{N|\operatorname{Im}\chi|\tau_j},\qquad
 |C_\chi'(c_j)|\le C N^2(1+|\chi|)
                              e^{N|\operatorname{Im}\chi|\tau_j}.
 \tag{13}
\]
The finite \(N=2\) case is absorbed in the constant. Hence
\[
 |Z_N|\le C N^{a_0}\prod_v(1+|\chi_v|)
                       \mathcal M_N(\operatorname{Im}\boldsymbol\chi).
 \tag{14}
\]

For the real action, use the continuous primitives and entropy
\[
 \begin{gathered}
 J(x)=\int_0^x\log(2\sin\pi r)\,dr,\qquad
 L(x)=\int_0^x\log|2\cos\pi r|\,dr,\\
 V_t(x)=L(x+t/(2\pi))+L(x-t/(2\pi))-2J(x).
 \tag{15}
 \end{gathered}
\]
The uniform real Newton estimate is
\[
 |e_r(-2\cos t)|\le C N^a e^{NV_t(r/N)}.
 \tag{16}
\]
It follows from the shifted midpoint logarithmic sum with uniform
\(O(\log N)\) upper error and the two-sided sine-factorial estimate;
zero samples only improve the upper bound.
For \(0\le t,u<\pi\), the function \(V_t(x)+V_u(x)\) is strictly
concave on
\[
 0<x<(\pi-\max(t,u))/(2\pi).
 \tag{17}
\]
Indeed, with \(C_x=\cos(2\pi x)\), its derivative is
\[
 \log\frac{(C_x+\cos t)(C_x+\cos u)}{(1-C_x)^2}.
 \tag{18}
\]
This decreases from \(+\infty\) to \(-\infty\). Its unique maximum is
\[
 x_*=\pi^{-1}\arctan(1/q),\qquad
 q=\sqrt{1+\tan^2(t/2)+\tan^2(u/2)}>0,
 \tag{19}
\]
and its value is \(\psi(t,u)\) with the original complete constant.
This is the real restriction of the canonical unsummed-wire
critical-value identity.

Every actual nonzero term (11) lies inside the closed version of
(17); its cutoff is smaller by \(1/(2N)\). Thus
\[
 K_N(c_j,c_l)\le C N^{a_1}e^{N\psi(\tau_j,\tau_l)}
 \tag{20}
\]
uniformly, also with \(u=0\) at outside endpoints. Boundary limits
follow by continuity. There are polynomially many physical
assignments, so (6), (9), and (20) prove (8) and the upper half of
(10).

For the lower half, first fix any real angles strictly inside the
box and approximate their absolute values by the physical angles
(2). For every edge, an integer \(r\) nearest (19) lies in both
physical supports for large \(N\). Two-sided product estimates on
this strict region give that positive term rate \(\psi(t,u)\).
The corresponding single assignment in (9) therefore has rate
\(W(\mathbf s)+\sum_v|b_v||s_v|\). The continuous closed-box maximum
can be approximated by interior points, and separate evenness
chooses their signs. Taking the supremum proves the lower limit.
Both parity grids approximate the same points. This positive
partition argument uses no normal lower bound. \(\square\)

## 2. The exact excess at a positive target

Suppose the canonical positive original chart contains
\[
 t_v=s_v+i h_v,\qquad r_{v,e}=k_{v,e}+i g_{v,e},
                  \qquad t_b=0\ (b\notin I).
 \tag{21}
\]
At zero crossing powers define its induced charge by
\[
 P_{0,v}(t):=\sum_{e\ni v}r_{v,e}=-\pi i y_v,\qquad
                 y_v=A_v+iB_v .
 \tag{22}
\]
Thus \(\sum_e g_{v,e}=-\pi A_v\) and
\(\sum_e k_{v,e}=\pi B_v\), with the complete original logarithmic
periods. Its selected classical critical action is
\[
 S_0(\mathbf y)=W(\mathbf t)-i\mathbf y\cdot\mathbf t .
 \tag{23}
\]
No quantum asymptotic at this charge is assumed.

For an oriented edge \(e=(v,w)\), put
\[
 \begin{array}{ll}
 a_P=s_v/4-g_{w,e}/2,&a_Q=s_v/4+g_{w,e}/2,\\
 b_P=g_{v,e}/2+s_w/4,&b_Q=g_{v,e}/2-s_w/4 .
 \end{array}
 \tag{24}
\]
All four coordinates lie in \((-\pi/4,\pi/4)\). The square energy
\(E_\square(0,0)=0\) has derivatives
\[
 (E_\square)_a=\tfrac12\operatorname{arsinh}(\tan(2a)\cos(2b)),
 \qquad
 (E_\square)_b=\tfrac12\operatorname{arsinh}(\tan(2b)\cos(2a)).
 \tag{25}
\]
It is even in each variable, has positive definite Hessian, and
extends continuously and convexly to its closed square. Define
\[
 E_e=E_\square(a_P,b_P)+E_\square(a_Q,b_Q),\qquad
 \mathcal E(\mathbf s,\mathbf g)=4\sum_eE_e .
 \tag{26}
\]
The outside work term is zero here because the prescribed outside
imaginary angles are zero. It is not dropped for arbitrary complex
outside data.

**Theorem 2.** At every supplied point (21)--(22),
\[
 \begin{split}
 \mathcal P(\mathbf B)-\operatorname{Re}S_0(\mathbf A+i\mathbf B)
 ={}&\frac{\mathcal E(\mathbf s,\mathbf g)
                        -\mathcal E(\mathbf s,\mathbf0)}{\pi}\\
 &+\mathcal P(\mathbf B)-W(\mathbf s)-\mathbf B\cdot\mathbf s .
 \end{split}
 \tag{27}
\]
Both terms on the right are nonnegative, and the first is positive
if some \(h_v\ne0\). At a supplied positive target,
\(\mathbf A=0\) if and only if every \(h_v=0\); in that case both
terms vanish. Hence the excess is strictly positive at every
nonreal positive target, uniformly on compact sets avoiding the
real locus.

**Proof.** The globally calibrated edge identity is
\[
 \pi\operatorname{Re}\psi(t_v,t_w)+4E_e
              -g_{v,e}h_v-g_{w,e}h_w=\pi M_\infty .
 \tag{28}
\]
Sum it and use (22), retaining the real part of the charge term:
\[
 \operatorname{Re}S_0=mM_\infty-\mathcal E(\mathbf s,\mathbf g)/\pi
                                      +\mathbf B\cdot\mathbf s .
 \tag{29}
\]
At real angles all \(g\) vanish, so
\[
 W(\mathbf s)=mM_\infty-\mathcal E(\mathbf s,\mathbf0)/\pi .
 \tag{30}
\]
This proves (27), including all outside-edge constants.

Reverse every incidence \(g\), keeping \(\mathbf s\) fixed. On each
edge the pairs (24) transform as
\[
 (a_P,b_P)\mapsto(a_Q,-b_Q),\qquad
 (a_Q,b_Q)\mapsto(a_P,-b_P).
 \tag{31}
\]
Thus \(\mathcal E(\mathbf s,-\mathbf g)=\mathcal E(\mathbf s,\mathbf g)\).
The segment \((\mathbf s,\lambda\mathbf g)\), \(-1\le\lambda\le1\),
stays strictly inside the angle body, whose inequalities are
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad |s_w|+2|g_{v,e}|<\pi.
 \tag{32}
\]
Strict Hessian convexity gives a positive energy difference unless
\(\mathbf g=0\), explicitly
\[
 \mathcal E(\mathbf s,\mathbf g)-\mathcal E(\mathbf s,\mathbf0)
  =\int_0^1(1-\lambda)\,
       \mathbf g^{\mathsf T}\mathcal E_{gg}
                   (\mathbf s,\lambda\mathbf g)\mathbf g\,d\lambda .
 \tag{33}
\]
If \(\mathbf g=0\), the inverse square formulas give all matched
\(h_v=0\). The second term in (27) is nonnegative by (6).

The target is an interior stationary point, hence the unique global
minimizer, of
\[
 \mathcal E-\pi\mathbf B\cdot\mathbf s
        \quad\text{subject to}\quad
                 \sum_e g_{v,e}=-\pi A_v .
 \tag{34}
\]
Its incidence multipliers are the original \(h_v\), and its
\(\mathbf s\)-equations are the real parts of (22). Strict convexity
compares it strictly with boundary assignments as well.
When \(\mathbf A=0\), its reflected point and their midpoint
\((\mathbf s,\mathbf0)\) are feasible. Strict convexity forces
\(\mathbf g=0\), hence \(\mathbf h=0\). Conversely real original
angles have real returns, giving \(\mathbf A=0\). In that case (34),
restricted to \(\mathbf g=0\), says that \(\mathbf s\) maximizes
(6), so the second term vanishes too. Continuity and (33) prove
compact uniformity. \(\square\)

Equivalently, on the compact weak angle body define
\[
 \mathfrak m(\mathbf A,\mathbf B)
   =\min_{\sum_e g_{v,e}=-\pi A_v}
                    \{\mathcal E-\pi\mathbf B\cdot\mathbf s\}
 \tag{35}
\]
when this set is nonempty. Reflection gives
\(\mathfrak m(\mathbf A,\mathbf B)=\mathfrak m(-\mathbf A,\mathbf B)\).
Convex averaging allows the zero-charge minimum to be taken at
\(\mathbf g=0\). At the supplied positive target,
\[
 \mathcal P(\mathbf B)-\operatorname{Re}S_0
    =\{\mathfrak m(\mathbf A,\mathbf B)
                      -\mathfrak m(\mathbf0,\mathbf B)\}/\pi .
 \tag{36}
\]
This uses the original energy and charge rows, without changing any
filling or peripheral marking.

## 3. The exact pressure-sensitive Fresnel tail

Take the entire actual initial function
\(f_N(\boldsymbol\chi)=\widetilde Z_N(\mathbf n,\boldsymbol\chi)\).
Change the real powers by nonzero \(\delta_j\) in \(J\subset I\), and
let \(E_J\) insert these coordinates into the full charge vector. Put
\[
 v_j=e^{-i\,\operatorname{sgn}(\delta_j)\pi/4}.
 \tag{37}
\]
The exact heat representation uses product lines parallel to \(v_j\).
Entirety and finite exponential type allow arbitrary finite
translations; all normal data and closing operations are already
combined in \(f_N\).

For a holomorphic reference phase \(S\) near \(\boldsymbol\zeta\), put
\(a_j=\partial_jS(\boldsymbol\zeta)\) and choose
\[
 \chi_j=\zeta_j+i\delta_j a_j/(2\pi)\quad(j\in J),\qquad
 \chi_j=\zeta_j\quad(j\notin J).
 \tag{38}
\]
Translate to \(\mathbf y=\boldsymbol\zeta+E_J(v_jr_j)\) and set
\[
 T_*=S(\boldsymbol\zeta)+\sum_{j\in J}i\delta_j a_j^2/(4\pi).
 \tag{39}
\]
Define
\[
 \begin{split}
 \mathcal B_\delta(\mathbf r;\boldsymbol\zeta)
 ={}&\mathcal P\bigl(\operatorname{Im}\boldsymbol\zeta+
                        \operatorname{Im}E_J(v_jr_j)\bigr)
                          -\operatorname{Re}S(\boldsymbol\zeta)\\
 &-\operatorname{Re}\sum_j a_jv_jr_j
                          -\pi\sum_jr_j^2/|\delta_j|.
 \end{split}
 \tag{40}
\]

**Proposition 3.** Apart from fixed polynomial prefactors in \(N\)
and \(\mathbf r\), the absolute translated heat integrand divided
by \(e^{N\operatorname{Re}T_*}\) is at most
\(e^{N\mathcal B_\delta}\). If a closed tail region satisfies
\(\sup\mathcal B_\delta\le-\kappa<0\), its actual contribution is
\[
 O\bigl(N^a e^{N(\operatorname{Re}T_*-\kappa/2)}\bigr).
 \tag{41}
\]
The assertion is uniform on compact parameter sets with this strict
gap, with the nonzero heat steps fixed away from zero.

**Proof.** The Gaussian exponent is
\(-i\pi\sum_j(y_j-\chi_j)^2/\delta_j\). Its difference from its
value at \(\boldsymbol\zeta\) is exactly
\[
 -\sum_j a_jv_jr_j-\pi\sum_jr_j^2/|\delta_j|.
 \tag{42}
\]
Its constant is the second term of (39) and cancels in the relative
bound. Apply Theorem 1 at \(\mathbf y\) to obtain (40). By (7),
\(\mathcal B_\delta\le C_0+C_1|\mathbf r|-c|\mathbf r|^2\).
Split the tail into a fixed compact part and its complement; the
quadratic loss supplies an integrable Gaussian outside. The strict
supremum bound then gives (41), absorbing polynomial factors.
\(\square\)

At a nonreal positive zero-power target, Theorem 2 gives
\[
 \mathcal B_\delta(\mathbf0;\boldsymbol\zeta)
       =\mathcal P(\operatorname{Im}\boldsymbol\zeta)
                          -\operatorname{Re}S_0(\boldsymbol\zeta)>0.
 \tag{43}
\]
The sharper envelope therefore cannot by itself certify the local
target term or replace a known complex initializer. It can estimate
discarded parts once (40) is negative there. An actual nonzero local
expansion, with its original coefficient, remains necessary on the
retained region. No enlargement of its certified angle-label set,
filled geometric rate, or arbitrary-short-filling noncancellation is
proved. Complementary-index Conway edges and an arbitrary complex
uncontracted exterior are not silently included in (5).

## Pinned direct sources

* notes/research_all_color_path_normal_bound.md, SHA256
  08f8932c2cdee4c7afadbb4db3cd85480603f8adb4c936ce29a5517b2d4799c7:
  the full polynomial normal decomposition and Lemma 5's first and
  mixed-normal bounds, including the original endpoint source.
* notes/research_three_crossing_real_period_newton_bound.md, SHA256
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e:
  the uniform all-color real Newton entropy (16).
* notes/research_unsummed_network_phase_coercivity.md, SHA256
  b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e:
  the same-index wire phase and its canonical critical value
  \(\psi\), equations (25)--(28), without a global quantum estimate.
* notes/research_positive_filling_convex_variation.md, SHA256
  2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0:
  the square energy, original incidence coordinates, Hessian
  convexity, continuous extension, and variational equations.
* notes/research_positive_period_inverse_descent.md, SHA256
  b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565:
  the calibrated edge energy/action identity and complete constant.
* notes/research_entire_charged_source_heat_reduction.md, SHA256
  33213425be9cac699860a48b23830399c82cd89bea3140cc776274aafe115fba:
  the exact full-Hermite real-power/coupon source, carriers, entire
  Gaussian transform, and finite line translations.

The polynomial cost of physical normals and uniform real Newton
entropy are prior results. The additions are their joint pressure
bound, its exact geometric excess, and the pressure-sensitive
entire-source tail functional. Only written proofs, source-text reads,
and file hashes were used. No mathematical program, numerical test,
frozen manuscript, or other author's note was changed.
