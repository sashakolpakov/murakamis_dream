# A full-height angle envelope for saturated currents

Private written proof, 16 November 2026.

The fixed-parent action gap extends from the terminal-height collar
to the entire height box whenever every removed power has absolute
value at least two. The extension uses the free incidences at the
deleted ends of cut edges. Their exact optimization also gives a
finite convex minimization criterion for arbitrary signed powers.
Surviving variables and their original unit rows remain shared.

These are classical angle-envelope statements. They do not bound
the actual endpoint-decorated quantum descendant. A positive original
kernel gives an explicit obstruction to transferring this envelope
to a pointwise quantum bound without an additional rate.

## 1. Original parent and the free saturated incidences

Use a supplied positive unit-charge parent on the original finite
circle tree, with selected vertices \(S\), complete outside angles,
and fixed signed integer powers \(n_v\). Every selected vertex has
an original incidence. Include every edge incident to \(S\), once
each, and write \(e_G\) for their number. The ambient closed angle
body has selected real angles \(s_v\), incidence angles \(g_{v,e}\),
outside \(s_b=0\), and inequalities
\[
 |s_v|\le\pi,\qquad
 |s_v|+2|g_{w,e}|\le\pi,\qquad
 |s_w|+2|g_{v,e}|\le\pi\quad(e=vw).
 \tag{1}
\]
Write \(X\) for the strict version of this body.
Let \(\mathcal E\) be the original raw square energy. Write \(z_0\)
for the supplied parent assignment, \(E_0=\mathcal E(z_0)\),
\(H_v^0=-\Im t_v^0>0\), and
\[
 M_G=e_GM_\infty-E_0/\pi,\qquad M_\infty=4G_{\rm Cat}/\pi.
 \tag{2}
\]
The fixed-parent theorem supplies the continuous Bregman remainder
\[
 D_0(z)=\mathcal E(z)-E_0-d\mathcal E(z_0)(z-z_0),\qquad
 \delta_0=\min_{\partial X}D_0>0.
 \tag{3}
\]
The boundary is that of the full ambient body, without charge rows.

Fix a nonempty removed set \(C\subseteq S\). Delete its incident
edges, counted once, and let \(r_C\) be their number. On the retained
forest keep every selected vertex in \(Y=S\setminus C\), including
isolated vertices, and its unchanged row
\[
 \sum_{\substack{e\ni w\\e\ {\rm retained}}}g_{w,e}
                         -n_ws_w/2=-\pi\quad(w\in Y).
 \tag{4}
\]
An isolated selected vertex still obeys \(n_ws_w=2\pi\) and
\(|s_w|\le\pi\). Let \(\mathcal F_{\rm del}\) be this compact
convex weak angle body with all outside real angles still zero.
In what follows assume it is nonempty. An empty body has no
angle envelope here and is not assigned a vanishing quantum source.
Its retained energy is \(\mathcal E_{\rm del}(z')\).

For signs \(\varepsilon_v=\pm1\), put \(s_v=\varepsilon_v\pi\)
on \(C\), impose (4) on the survivors, and impose no row at a
removed vertex. This defines the saturated face
\(\mathcal F_C^\varepsilon\). Its remaining degrees of freedom are
particularly simple. At every cut edge \(e=vw\), \(v\in C,w\notin C\),
\[
 g_{w,e}=0,\qquad
 -\frac{\pi-|s_w|}{2}\le g_{v,e}\le
                       \frac{\pi-|s_w|}{2}.
 \tag{5}
\]
Both incidences on an internal \(C\)-edge are zero. The intervals
in (5) are independent, even when several cut edges meet the same
surviving vertex. They do not alter that vertex's row (4).
Thus the face projects onto all of \(\mathcal F_{\rm del}\),
and its fiber is exactly the product of (5).

Both square factors on every deleted edge have their original
boundary energy. Consequently, throughout this fiber,
\[
                 \mathcal E(z)=r_C\pi M_\infty+
                                      \mathcal E_{\rm del}(z').
 \tag{6}
\]
In particular the deleted-end incidences affect the endpoint work
but not the energy in (6). This is why they must remain free.

Define, using all cut incidences including edges to original outside
vertices,
\[
 \begin{split}
 d_C(v)&=\#\{e=vw:w\notin C\},\\
 L_v(s)&=\sum_{\substack{e=vw\\w\notin C}}
                            (1-|s_w|/\pi),\\
 \lambda_v(s)&=\frac{|n_v|}{2}-1+\frac{L_v(s)}2 .
 \end{split}                                                   \tag{7}
\]
Thus \(0\le L_v\le d_C(v)\). Internal removed edges contribute
to \(r_C\), but not to these sums.

## 2. Exact incidence optimization and the whole height box

For \(h_v\ge0\), the original classical current action is
\[
 \begin{split}
 A_C^\varepsilon(h;z)
 &=e_GM_\infty-\mathcal E(z)/\pi
                  +\sum_{v\in C}h_v(c_v(z)-1),\\
 c_v(z)&=\varepsilon_v n_v/2-G_v(z)/\pi,\qquad
 G_v(z)=\sum_{e\ni v}g_{v,e}.
 \end{split}                                                   \tag{8}
\]
This includes both the outside work and the signed current
exponential, with the original normalization. At the parent heights,
the fixed-parent identity gives
\[
 A_C^\varepsilon(H_C^0;z)=M_G-D_0(z)/\pi
                            \le M_G-\delta_0/\pi .
 \tag{9}
\]
No matched positive boundary chart is asserted for an arbitrary
weak assignment in (8).

**Proposition 1.** The exact largest angle action at fixed height is
\[
 \begin{split}
 B_C(h)&:=\max_{\varepsilon}\max_{z\in\mathcal F_C^\varepsilon}
                                      A_C^\varepsilon(h;z)\\
 &=(e_G-r_C)M_\infty-\frac1\pi
       \min_{z'\in\mathcal F_{\rm del}}
       \left\{\mathcal E_{\rm del}(z')
                         -\pi\sum_{v\in C}h_v\lambda_v(s)\right\}.
 \end{split}                                                   \tag{10}
\]
All extrema are attained. The minimization in (10) is convex
for each fixed \(h\ge0\).

*Proof.* For fixed retained \(z'\), choose the dominant sign
\(\varepsilon_v n_v=|n_v|\), with either sign allowed if \(n_v=0\).
This only increases (8). Since \(h_v\ge0\), the incidence term
\(-h_vG_v/\pi\) is largest when every independent interval (5)
is at its lower endpoint:
\[
         g_{v,e}^*(s)=-(\pi-|s_w|)/2,\qquad
         G_v^*(s)=-\pi L_v(s)/2.
 \tag{11}
\]
These simultaneous choices are feasible on the same retained
assignment. Equations (6),(8) then give (10), including equality.
Compactness and continuity give attainment. Finally the objective
in (10) equals the convex retained energy plus
\(\frac12\sum_vh_v\sum_{\rm cut(v,w)}|s_w|\) and a constant.
The retained constraints (1),(4) are convex. \(\square\)

**Theorem 2 (full-height classical gap).** If
\[
                              |n_v|\ge2\quad(v\in C),
 \tag{12}
\]
then, for every sign, every admitted saturated assignment and every
height in the full box,
\[
 \boxed{\qquad
 0\le h_v\le H_v^0\ (v\in C)
 \quad\Longrightarrow\quad
 A_C^\varepsilon(h;z)\le B_C(h)
            \le M_G-\delta_0/\pi .
 \qquad}                                                       \tag{13}
\]

*Proof.* Under (12), every \(\lambda_v(s)\) in (7) is nonnegative.
The maximum in (10) is therefore coordinatewise nondecreasing in
\(h\). Consequently
\[
 B_C(h)\le B_C(H_C^0)\le M_G-\delta_0/\pi,
\]
where the last inequality is (9), applied to all the assignments
(11). This proves (13).

Equivalently, compare an arbitrary assignment directly with the
different boundary assignment having the same survivors and the
incidences (11). Its energy is unchanged. The action first increases
when the incidences and signs are replaced, and then increases when
the heights are raised to \(H_C^0\). Thus no sign is assumed for the
comparison rows of the original assignment. \(\square\)

The theorem holds for every nonempty removed set satisfying (12),
with the same parent \(\delta_0\). It requires neither a positive
critical point of the retained forest nor an extension of that
forest with unit rows at the removed vertices.

## 3. All signed powers: an exact finite corner criterion

For \(T\subseteq C\), let \(h^T_v=H_v^0\) on \(T\) and zero
on \(C\setminus T\). Define
\[
 \begin{split}
 \mathcal E_T(z')={}&\mathcal E_{\rm del}(z')
       +\frac12\sum_{v\in T}H_v^0
                      \sum_{\substack{e=vw\\w\notin C}}|s_w|\\
 &-\pi\sum_{v\in T}H_v^0
                  \left(\frac{|n_v|}{2}-1+\frac{d_C(v)}2\right),
 \qquad
 \mu_T=\min_{\mathcal F_{\rm del}}\mathcal E_T .
 \end{split}                                                   \tag{14}
\]
Each is an attained convex minimization on the same retained body.
No survivor is optimized independently of its shared neighbors.

**Theorem 3.** Without (12), the exact worst action over all signs,
weak assignments and heights is
\[
 \boxed{\quad
 \sup_{0\le h\le H_C^0}B_C(h)
       =(e_G-r_C)M_\infty-\frac1\pi\min_{T\subseteq C}\mu_T.
 \quad}                                                        \tag{15}
\]
Hence a strict uniform classical gap on the full height box exists
if and only if
\[
 \boxed{\qquad
       \min_{T\subseteq C}\mu_T>E_0-r_C\pi M_\infty .
 \qquad}                                                       \tag{16}
\]
The exact gap is the difference in (16), divided by \(\pi\).
The terminal corner \(T=C\) always satisfies
\[
                 \mu_C\ge E_0-r_C\pi M_\infty+\delta_0 .
 \tag{17}
\]

*Proof.* The function \(B_C\) is the supremum of affine functions
of \(h\). Every height in the box is a convex combination of its
corners, so its value is at most the largest corner value.
The converse follows because all corners are admitted.
Equation (10) at \(h=h^T\) is precisely (14), giving (15).
Subtract (15) from (2) to obtain (16); (9) gives (17).
\(\square\)

One equivalent formula eliminates the heights first:
\[
 \min_{T\subseteq C}\mu_T
 =\min_{z'\in\mathcal F_{\rm del}}
   \left\{\mathcal E_{\rm del}(z')
             -\pi\sum_{v\in C}H_v^0(\lambda_v(s))_+\right\}.
 \tag{18}
\]
This single displayed objective is not asserted convex. Its finite
corner representation (14) is the convex formulation.

A simpler sufficient condition follows from the terminal gap.
Put
\[
 b_C=\max_{z'\in\mathcal F_{\rm del}}
                 \sum_{v\in C}H_v^0(-\lambda_v(s))_+ .
 \tag{19}
\]
Then every action on the box is at most
\[
                         M_G-\delta_0/\pi+b_C.
 \tag{20}
\]
Indeed, at the maximizing incidences, replacing \(h\) by \(H_C^0\)
loses at most the expression in (19). If every removed power is a
nonzero integer, only \(|n_v|=1\) can contribute to (19), with
\[
             (-\lambda_v)_+=\tfrac12(1-L_v(s))_+.
 \tag{21}
\]
Thus the remaining classical obstruction is an explicit capacity
deficit, and the full corner criterion remains available when the
sufficient estimate (20) is inconclusive.

## 4. Exact source placement and the failure of a zero-cost transfer

Use the original Newton kernel \(K_N\) and the full physical algebra
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^{N-1}]\operatorname{rem}_{P_N}f .
 \tag{21a}
\]
The crossing \(R^n\) retains the values and all first spectral
normals of \(C_{N,n}\exp(inNt^2/(4\pi))\) at \(z=-2\cos t\),
and the original simple-node value at odd levels.
The original unit-charge vertical current has paired weight
\[
 \begin{split}
 \rho_{N,n,1}(h)
 ={}&\frac{i\eta N^2C_{N,n}}{\pi}
      \frac{\sinh h\,E_{N,n}(h)}{(1+e^{-Nh})^2}\\
 &\qquad\cdot
 \left[e^{N(n/2-1)h}-e^{N(-n/2-1)h}\right],\\
 \eta={}&(-1)^{N-1},\quad
 C_{N,n}=e^{\pi i n(N-1)^2/(4N)},\quad
 E_{N,n}(h)=e^{inN(\pi^2-h^2)/(4\pi)} .
 \end{split}                                                   \tag{22}
\]
In particular \(n=0\) makes this whole paired current exactly zero.
This fact applies to a term whose removed set contains that vertex.
It does not erase a zero-power surviving vertex, its row, its
incidences or its original trace in a different removed-set term.
For the classical formulas (10)--(20), zero powers may simply remain
in the displayed minimizations.

For clarity, consider the original graph with no additional coupon.
Put \(w_{h_v}=2\cosh h_v\), and keep the entire common-color product
\[
 Q_{w,N,h}(z_w)=
             \prod_{\substack{e=vw\\v\in C}}K_N(w_{h_v},z_w)
                                      \quad(w\in Y).
 \tag{23}
\]
Let
\[
 D_{C,N}(h)=
 \prod_{\substack{e=vv'\\v,v'\in C}}K_N(w_{h_v},w_{h_{v'}})
 \prod_{\substack{e=vb\\v\in C,\ b\notin S}}K_N(w_{h_v},-2).
 \tag{24}
\]
The actual descendant, including every internal removed edge and
every surviving full trace, is
\[
 \mathcal Q_{C,N}(h)=D_{C,N}(h)
 \left(\prod_{w\in Y}\phi_N^{(z_w)}\right)
 \left[\prod_{w\in Y}R^{n_w}(z_w)
       \prod_{e\ {\rm retained}}K_N
       \prod_{w\in Y}Q_{w,N,h}(z_w)\right].
 \tag{25}
\]
Outside colors are complete as above. Products at shared colors
are formed before any trace. The exact current is
\[
 I_{C,N}=\int_{\prod_{v\in C}[0,H_v^0]}
                 \prod_{v\in C}\rho_{N,n_v,1}(h_v)\,
                         \mathcal Q_{C,N}(h)\,d h .
 \tag{26}
\]
Its original inclusion--exclusion sign is retained when (26) is
placed back in the full trace expansion.

For a nonempty retained angle body, a tempting pointwise transfer is
\[
 |\mathcal Q_{C,N}(h)|
 \ \le\ e^{o(N)}
 \exp N\left\{
 B_C(h)-\sum_{v\in C}h_v\left(\frac{|n_v|}{2}-1\right)
                 \right\}.
 \tag{27}
\]
**Estimate (27) is false**, even with a supplied positive parent and
no surviving variable or trace left to estimate.

Take the original one-edge graph with both endpoints selected and
\(C=S\). Then \(e_G=r_C=1\), the retained body is a point,
\(\mathcal E_{\rm del}=0\), and \(L_v=0\). Thus
\[
 B_C(h)=\sum_{v\in C}(|n_v|/2-1)h_v,\qquad
 \mathcal Q_{C,N}(h)=K_N(2\cosh h_1,2\cosh h_2).
 \tag{28}
\]
In this case (27) would assert a subexponential bound for that
kernel at every fixed positive pair of heights.

Here is the original finite-level normalization. Put \(D=N-1\),
\(c_j=2\cos((2j+1)\pi/N)\), and
\[
 e_k(w)=S_k^{-2}\prod_{j<k}(c_j-w),\qquad
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),\qquad
 K_N(w_1,w_2)=\sum_{k=0}^D e_k(w_1)e_k(w_2).
 \tag{29}
\]
The elementary root-of-unity product gives \(S_D=N\), and
\(c_D=c_0\). Since \(P_N(w)=\prod_{j=0}^{N-1}(w-c_j)\),
\[
 e_D(w)=\frac{\eta P_N(w)}{N^2(w-c_0)}.
 \tag{30}
\]
For \(w_1,w_2>2\), the signs of the individual \(e_k(w_i)\)
are both \((-1)^k\). Every same-index product in (29) is
strictly positive. The actual kernel therefore obeys
\[
 K_N(w_1,w_2)\ge
 \frac{P_N(w_1)P_N(w_2)}
             {N^4(w_1-c_0)(w_2-c_0)}.
 \tag{31}
\]
At \(w_i=2\cosh h_i\), \(h_i>0\) fixed,
\(P_N(w_i)=2\cosh(Nh_i)+2\). Consequently
\[
 \liminf_{N\to\infty}\frac1N
 \log K_N(2\cosh h_1,2\cosh h_2)\ge h_1+h_2>0.
 \tag{32}
\]
This is a pointwise bound for the literal internal-edge factor,
not an absolute-value estimate of a sum with possible Newton
cancellation.

In fact its rate is exactly \(h_1+h_2\). To see this directly, put
\(T_k=e_k(w_1)e_k(w_2)>0\) and fix
\(\delta=\min_i(w_i-2)>0\). Uniformly in \(0\le k<D\),
\[
 w_i-c_k-4\sin^2(\pi(k+1)/N)
 =w_i-2+2\cos(2\pi(k+1)/N)-c_k
 \ge\delta-2\pi/N.
\]
For large \(N\), each individual forward magnitude ratio is at
least \(1+\delta/8\), hence \(T_{k+1}/T_k\ge(1+\delta/8)^2\).
The last backward ratio is
\[
 \frac{T_{D-1}}{T_D}
   =\prod_{i=1}^2
       \frac{4\sin^2(\pi/N)}{w_i-c_{D-1}}=O(N^{-4}).
\]
Summing the preceding geometric bound gives
\(K_N(w_1,w_2)=T_D[1+O(N^{-4})]\). These bounds are uniform
on compact positive height intervals. The lower bound (32) alone
already disproves (27).

The example admits the required positive parent. Take equal
sufficiently large positive integer powers \(m\) at both endpoints.
The original complete-edge branch satisfies
\[
 \psi_t(t,u)=-\pi^{-1}\operatorname{asinh}
                       (\tan(t/2)\cos(u/2)).
 \tag{33}
\]
It is symmetric between the two endpoints, and its original positive
chart contains a neighborhood of \((0,0)\). Set \(t_1=t_2=z/m\).
Both unit-period equations reduce to
\[
 z=2\pi+2\pi i\,\psi_t(z/m,z/m).
 \tag{34}
\]
At \(m^{-1}=0\), the derivative with respect to \(z\) of the
equation moved to one side is one. The holomorphic implicit-function
theorem gives its unique nearby solution. Since
\(\psi_t(t,t)=-t/(2\pi)+O(t^3)\),
\[
 z=2\pi-\frac{2\pi i}{m}+O(m^{-2}),\qquad
 t_v^0=\frac{2\pi}{m}-\frac{2\pi i}{m^2}+O(m^{-3}).
 \tag{35}
\]
For all sufficiently large \(m\), this is in that original positive
chart and \(H_v^0>0\). Fix such an integer before taking \(N\to\infty\),
and choose any \(0<h_v\le H_v^0\). Thus (32) contradicts (27)
within the actual parent hypotheses of Theorem 2.

Any pointwise estimate of the form (27) with an added quantum rate
\(\Delta_C(h)\) must have \(\Delta_C(h)\ge h_1+h_2\) in this example.
The strict classical gap must then be compared with that additional
rate; it cannot be assumed to absorb it. The original full-current
source gives positive-cost upper estimates for these kernels, rather
than a zero-cost replacement. Alternatively one must estimate a
joint integrated current or a sum of original currents, retaining
the cancellations that such a representation may possess.
Neither (31) nor (32) is a lower bound for the oscillatory integral
(26) or for the complete inclusion--exclusion sum.

The exact source has no known projector onto the face used in (10).
Already \(K_N(2,z)\) has a degree-\(N-1\) Chebyshev coefficient of
polynomial size, producing the literal surviving charges \(1/N\)
and \(2-1/N\). These are full-normal identities, and no angle-fiber
restriction follows. Bounds for bounded microscopic parameters
\(\alpha_v=Nh_v\) cover only a shrinking part of the present
fixed-height box. Optimizing classical survivor variables or using
their reduced Schur Hessian does not remove the positive internal
kernel rate in (32). Empty retained angle bodies also require
their own actual source argument.

## 5. Coverage and direct-source readback

The general Legendre contour and the reduced-angle inverse-period
graph already prove local convexity, Schur reduction and a positive
prism near the parent's own heights. They also record why a connector
to the real-height rim need not have smaller action. The split-current
comparison gives a deleted-energy gap using a different Ward source.
The retained-boundary leaf profile gives exact fixed-height infimal
projection while keeping cut incidences.

The additional step here is the explicit optimization of those
previously retained free deleted incidences, followed by height-box
optimization. It proves (13) for every height, and replaces the
remaining all-height classical question by the finite convex tests
(14)--(16). The explicit obstruction (28)--(35) shows why these
tests cannot simply be imposed as a zero-cost pointwise quantum
envelope. No new contour realization, integrated-current lower
bound or volume asymptotic is inferred.

The three complete direct sources were read in full at these pins,
with every used implication and all source hashes checked:

* [Fixed-parent action and saturated-edge calibration](research_fixed_parent_height_global_calibration.md),
  SHA256 268da098a6650065dc2abada9ce7c1bd8029abc33feb59783a67f03cd25a7bf0.
* [Original full-height current and coherent descendant](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595.
* [Original complete bare-edge branch and positive chart](research_uniform_terminal_family_and_star_fillings.md),
  SHA256 d9da305e1567393f5f714f11bd646cd2dca37b7d7569b9ab12d6a63014ece4f9.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Previously adopted notes and public manuscripts are unchanged.
