# Global calibration at the original parent's fixed heights

Private written proof, 16 November 2026.

The original unit-charge phase has its unique global maximum on its
entire positive slice at the parent's imaginary angles. No convexity
or connectedness of that slice is required. Its loss is exactly the
ambient angle-energy Bregman remainder. The same identity gives a
uniform boundary gap and an exact correction for saturated endpoint
currents at other heights, retaining their outside work.

These are classical identities and gaps. They do not bound the
original quantum kernel or its joined horizontal, outer-row and
vertical currents.

## 1. Original phase and unconstrained angle body

Fix an original finite circle tree, a nonempty selected set \(S\),
and every edge incident to \(S\), counted once. Let \(e_G\) be the
number of included edges and \(d_v\) the original degrees. Every
selected vertex has an incidence. Outside angles are complete,
\(t_b=0\). Keep arbitrary fixed real powers \(n_v\); when they are
integers, their original peripheral marking and crossing carrier
are unchanged.

On every canonical original positive edge write
\[
 t_v=s_v+i h_v,\qquad r_{v,e}=k_{v,e}+i g_{v,e}.
 \tag{1}
\]
Assume a supplied positive unit-charge solution \(t^0\):
\[
 P_v(t^0):=\sum_{e\ni v}r_{v,e}(t^0)
                    -\frac{i n_vt_v^0}{2}=-\pi i .
 \tag{2}
\]
Put \(H_v^0=-\Im t_v^0>0\), and denote its real angle assignment
by \(z_0\). The strict positivity of these heights follows from
the pinned ambient reflection proof.

The ambient angle body \(X\) has selected coordinates \(s_v\),
all endpoint incidence coordinates \(g_{v,e}\), fixed outside
\(s_b=0\), and inequalities
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad
 |s_w|+2|g_{v,e}|<\pi\qquad(e=vw).
 \tag{3}
\]
No charge rows are imposed on \(X\). Its closure \(\overline X\)
is compact. For an ordered edge set
\[
 A_P=s_v/4-g_{w,e}/2,\quad A_Q=s_v/4+g_{w,e}/2,\qquad
 y_P=g_{v,e}/2+s_w/4,\quad y_Q=g_{v,e}/2-s_w/4.
 \tag{4}
\]
The original square energy satisfies
\[
 dE_\square=x\,dA+B\,dy,\quad E_\square(0,0)=0,\qquad
 x=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),\quad
 B=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{5}
\]
Write \(E_{P,e}=E_\square(A_P,y_P)\) and
\(E_{Q,e}=E_\square(A_Q,y_Q)\).
Define the raw full energy and the comparison row values by
\[
 \mathcal E(z)=4\sum_e(E_{P,e}+E_{Q,e}),\qquad
 \rho_v(z)=\sum_{e\ni v}g_{v,e}-n_vs_v/2,\qquad
 c_v(z)=-\rho_v(z)/\pi.
 \tag{6}
\]
The outside work is zero here because the original outside angles
are complete. The square Hessians and the injectivity of (4) give
a positive definite Hessian for \(\mathcal E\) on \(X\). It has
a continuous convex extension to \(\overline X\).

Retain the original phase and its complete normalization:
\[
 \Phi_1(t)=\sum_{e=vw}\psi(t_v,t_w)
       +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
       -i\sum_{v\in S}t_v,\qquad
 M_\infty=\psi(0,0)=4G_{\rm Cat}/\pi .
 \tag{7}
\]
Here \(G_{\rm Cat}=\sum_{\ell\ge0}(-1)^\ell/(2\ell+1)^2\).
Thus \((\Phi_1)_{t_v}=-(P_v+\pi i)/\pi\). There is no added
phase constant or reset of a logarithmic lift. The pinned global
edge calibration is
\[
 \pi\Re\psi(t_v,t_w)+4(E_{P,e}+E_{Q,e})
                  -g_{v,e}h_v-g_{w,e}h_w=\pi M_\infty .
 \tag{8}
\]
It holds throughout the original positive edge domain, independently
of any period equation.

At \(z_0\), the ambient differential is
\[
 d\mathcal E(z_0)=-\sum_{v\in S}H_v^0\,d\rho_v,\qquad
 \rho_v(z_0)=-\pi .
 \tag{9}
\]
Indeed the \(ds_v\) coefficient is \(\sum k_{v,e}=n_vH_v^0/2\);
the selected incidence coefficient is \(-H_v^0\); and the
outside incidence coefficient is zero. Set
\[
 D_0(z)=\mathcal E(z)-\mathcal E(z_0)
                      -d\mathcal E(z_0)(z-z_0),\qquad
 M_G=e_GM_\infty-\mathcal E(z_0)/\pi .
 \tag{10}
\]
Strict convexity on the segment from \(z_0\) to any distinct
point of \(\overline X\) gives \(D_0(z)>0\) there. In particular
\[
 \delta_0:=\min_{\partial X}D_0>0,\qquad
 \mathcal E(z)-\mathcal E(z_0)
       =D_0(z)+\pi\sum_{v\in S}H_v^0(c_v(z)-1).
 \tag{11}
\]
All boundaries in (11) are those of the ambient body, not of
a fixed-charge fiber.

## 2. The entire positive horizontal slice

Let
\[
 U_{H^0}=\{s\in(-\pi,\pi)^S:
     t_v=s_v-iH_v^0,\ t_b=0
     \text{ belongs to the original positive edge domain}\}.
 \tag{12}
\]
The domain uses the original canonical edge branches. It contains
\(s^0=\Re t^0\) and is open and bounded; its convexity and
connectedness are not assumed. Let \(z(s)\in X\) be the resulting
angle assignment. Its rows \(c_v(z(s))\) need not equal one or
even be positive.

**Theorem 1.** Throughout all of \(U_{H^0}\),
\[
 \boxed{\qquad
       \Re\Phi_1(s-iH^0)=M_G-\frac{D_0(z(s))}{\pi}.
 \qquad}                                                     \tag{13}
\]
The unique global maximum is \(M_G\), attained at \(s^0\).
For every \(a>0\), the portion with \(|s-s^0|\ge a\), if
nonempty, has a uniform strict gap. Moreover
\[
 \limsup_{\substack{s\in U_{H^0}\\
                    \operatorname{dist}(s,\partial U_{H^0})\to0}}
            \Re\Phi_1(s-iH^0)\le M_G-\delta_0/\pi .
 \tag{14}
\]
Consequently some full neighborhood of \(\partial U_{H^0}\)
inside this slice has gap at least \(\delta_0/(2\pi)\).

*Proof.* At an arbitrary positive point with \(h_v=-H_v\),
sum (8) and retain both terms after the edge sum in (7). One gets
\[
 \Re\Phi_1(t)
 =e_GM_\infty-\frac{\mathcal E(z)}{\pi}
                              +\sum_{v\in S}H_v(c_v(z)-1).
 \tag{15}
\]
The sign follows explicitly from
\(\Re(i n_vt_v^2/(4\pi))=-n_vs_vh_v/(2\pi)\) and
\(\Re(-it_v)=h_v\). At \(H=H^0\), (11) cancels the last
sum and proves (13). This uses the same edge constant on every
component of (12).

Equality forces \(z(s)=z_0\), hence \(s=s^0\). For the away
gap, minimize \(D_0\) on the compact set
\(\{z\in\overline X:|s(z)-s^0|\ge a\}\). When this set is
nonempty its minimum is positive.

For (14), take any sequence approaching the boundary of (12).
Pass to convergent subsequences of \(s\) and \(z(s)\).
If its limiting angle assignment were inside \(X\), the smooth
inverse square formulas (5) would reconstruct positive edges
at the limiting \(s-iH^0\). Imaginary-angle matching and the
complete outside data persist by continuity. That point would
belong to the open set (12), a contradiction. Every angle
limit therefore lies in \(\partial X\). Apply (11), continuity
of \(D_0\), and (13). A sequence contradicting the final
neighborhood assertion would contradict the same argument.
\(\square\)

This proof does not integrate a Hessian along a segment in the
positive slice. Such a segment need not be available. It also
does not require the slice to satisfy the unit imaginary-period
rows away from its center.

## 3. Saturated endpoint work and the exact height correction

Fix a nonempty \(C\subseteq S\) and signs \(\varepsilon_v=\pm1\).
Consider any \(z\in\overline X\) such that
\[
 s_v=\varepsilon_v\pi\quad(v\in C),\qquad
 c_w(z)=1\quad(w\in S\setminus C).
 \tag{16}
\]
The rows at \(C\) are unrestricted:
\[
 G_v(z)=\sum_{e\ni v}g_{v,e},\qquad
                 c_v(z)=\varepsilon_v n_v/2-G_v(z)/\pi .
 \tag{17}
\]
This removes the usual capacity requirement for imposing \(c_v=1\)
at a saturated vertex. It does not assert that (16) is nonempty
for every deleted forest; isolated survivor rows remain in force.

Let \(r_C\) count the edges incident to \(C\). The weak inequalities
force the incidence opposite each saturated vertex to vanish;
both incidences on internal \(C\)-edges vanish. The square-boundary
normalization is
\[
 E_\square|_{\partial[-\pi/4,\pi/4]^2}
                         =\pi M_\infty/8.
 \tag{18}
\]
Thus, with every surviving edge and angle retained,
\[
 \mathcal E(z)=\mathcal E_{\rm del}(z')+r_C\pi M_\infty.
 \tag{19}
\]
For nonnegative endpoint heights \(h_v\), define the angle action
including their outside work by
\[
 A_C^{\rm ext}(h;z)
 =e_GM_\infty-\frac{\mathcal E(z)+\sum_{v\in C}h_vG_v(z)}{\pi}.
 \tag{20}
\]
The sign of the work is fixed by the outside imaginary angle
\(-h_v\): the energy subtracts that angle times \(G_v\).
Internal \(C\)-edges have zero work, but their constants in (19)
remain. If a matching complex boundary limit with these heights
exists, (8) identifies (20) with the real surviving unit-charge
phase, including its endpoint edges. Otherwise (20) is only the
displayed weak-angle functional; no such boundary chart is assumed.

The original paired unit-charge vertical current has the following
exact scalar weight, with \(\eta=(-1)^{N-1}\):
\[
 \begin{split}
 \rho_{N,n,1}(h)
 ={}&\frac{i\eta N^2C_{N,n}}{\pi}
       \frac{\sinh h\,E_{N,n}(h)}{(1+e^{-Nh})^2}\\
 &\quad\cdot
  \left[e^{N(n/2-1)h}-e^{N(-n/2-1)h}\right],\\
 C_{N,n}&=e^{\pi i n(N-1)^2/(4N)},\qquad
 E_{N,n}(h)=e^{inN(\pi^2-h^2)/(4\pi)} .
 \end{split}                                                 \tag{21}
\]
This is (12) of the full-current source at \(J=N\), rewriting
the entire \(\cosh^2\) denominator, not dropping its aliases.
It retains both signed exponentials and both parities. At \(n=0\)
they cancel exactly. For real powers and heights the two displayed
carriers have modulus one.

The signed exponential corresponding to
\(t_v=\varepsilon_v\pi-i h_v\) contributes
\((\varepsilon_v n_v/2-1)h_v\). Add that term to (20):
\[
 A_C(h;z)=A_C^{\rm ext}(h;z)
                  +\sum_{v\in C}(\varepsilon_v n_v/2-1)h_v
 =e_GM_\infty-\mathcal E(z)/\pi
                  +\sum_{v\in C}h_v(c_v(z)-1).
 \tag{22}
\]
This definition matches the classical exponential and outside-work
bookkeeping of the actual current. It is not an upper estimate for
its kernel coupons or its surviving traces.

**Theorem 2.** For every assignment (16) and every such height vector,
\[
 \boxed{\quad
 M_G-A_C(h;z)=\frac{D_0(z)}{\pi}
             +\sum_{v\in C}(H_v^0-h_v)(c_v(z)-1).
 \quad}                                                       \tag{23}
\]
In particular at \(h=H_C^0\), uniformly over all nonempty \(C\),
all signs and all admitted assignments,
\[
                        A_C(H_C^0;z)\le M_G-\delta_0/\pi .
 \tag{24}
\]
There is no restriction on the removed powers.

For an explicit common terminal-height collar put
\[
 K_v=1+|n_v|/2+d_v/2,\qquad K_*=\sum_{v\in S}K_v,\qquad
 \epsilon_*=\min\left\{\tfrac12\min_{v\in S}H_v^0,
                                      \frac{\delta_0}{2\pi K_*}\right\}.
 \tag{25}
\]
Whenever \(\max_{v\in C}|h_v-H_v^0|\le\epsilon_*\),
\[
                        A_C(h;z)\le M_G-\delta_0/(2\pi).
 \tag{26}
\]

*Proof.* Insert (11) in (22) and use the survivor rows from (16).
This gives (23). A saturated selected vertex has an incidence,
so every assignment (16) lies on \(\partial X\), proving (24).
Finally \(|G_v|\le\pi d_v/2\) gives \(|c_v-1|\le K_v\).
The absolute correction in (23) is at most
\(\epsilon_*K_*\le\delta_0/(2\pi)\), proving (26).
\(\square\)

## 4. Coverage and source scope

The ambient supporting identity (11) and boundary square energy were
already proved in the split-current gap note. The inverse-period
note already calibrates the full unit-row slice. The
[reduced-angle graph note, Section 4](research_reduced_angle_inverse_period_graph.md),
gives a local comparison with the constant parent height, while the
[general Legendre contour note, Section 5](general_legendre_rivin_contour.md),
gives the positive-chart prism mechanism. These coverage sections
were read; they are not additional proof dependencies.
The extra conclusion here is the exact global horizontal-slice
identity (13), without assumptions on its topology, and the
capacity-free correction (23) matching the full paired current.

The exact original rectangle remains \(L=H^{\rm op}+V^{\rm op}\),
with the vertical height integrated from zero to its chosen final
height. Equations (24)--(26) do not control that entire interval:
the correction in (23) can lose its favorable bound away from
the terminal-height collar. Nor do these identities place an
arbitrary endpoint kernel or physical color assignment in (16).
An empty weak fiber is not assigned a zero quantum source.

No full-period kernel bound, joined-current estimate, contour
reachability, nonzero cycle coefficient, or scalar asymptotic
is claimed. Every source use must still retain its actual full
Hermite normals, shared coupons, outer physical rows, and vertical
or interface terms.

The following complete direct sources were read at these versions,
their used implications checked, and their hashes verified:

* [Ambient split-current comparison](research_split_current_convex_action_gap.md),
  SHA256 8e42b3e549cebd45fa301ae3c41858ab2def475fa072985a49f5bc639ee204dc:
  ambient energy, parent differential, positive heights, global
  Bregman remainder and exact saturated-edge energy.
* [Original action calibration](research_positive_period_inverse_descent.md),
  SHA256 b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565:
  canonical phase, globally fixed edge constant, inverse square
  reconstruction and full outside-work normalization.
* [Full-period current and charge convolution](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595:
  exact original rectangle, signed paired weight and carrier,
  full-normal surviving sources and retained endpoint products.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Previously adopted notes and public manuscripts were unchanged.
