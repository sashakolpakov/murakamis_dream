# Horizontal completion after the full first collar

Research reduction, 5 November 2026. The completed first-collar
comparisons leave one precise real boundary force. On a horizontal
domain with the required complete conditional sources, arbitrary third
and later real motions are paid by the ordinary coherent energy. A
second-coordinate motion additionally costs the work of the original
first-pair marginal. This gives a one-variable completion criterion,
without replacing the open reference by a periodic one. The existing
source domains do not yet supply the entire plateau domain in this
criterion.

## 1. The physical block and its source-admissible horizontal domain

Fix an actual complete-color open reference \(r_j=a_j+ic_j\).
Take a first collar \(0\le x_1\le\rho\), a fixed cut at
position \(h\ge3\), and keep \(z_h=r_h\). The second
coordinate has its full physical height attenuation: if its type is
three, \(k\) lies between \(c_2\) and zero; if it is four,
either \(c_2\le k\le0\) is unselected or
\(0\le k\le H=.014\) is selected. All positions
\(3,\ldots,h\) are unselected, lie in the plateau, and have
their unchanged reference heights. The real coordinate of position
two also lies in the plateau. Thus its height change does not alter
the third height, and no additional cutoff variation is suppressed.

Put \(y=(y_2,\ldots,y_{h-1})\), \(y_j=a_j+d_j\), and
define the horizontal comparison targets
\(\widehat z_j=y_j+ic_j\), including position two. Its
physical target is instead \(z_2=y_2+ik\).

The following source condition is explicit and important. Let
\(\mathcal D\) be a compact set of such real tuples containing
the reference and the segment from the reference to every tuple in
\(\mathcal D\). Require, along every segment:

1. Each original conditional factor with edges \(3,\ldots,h\),
   at the horizontal targets \((\widehat z_{j-1},\widehat z_j)\),
   has its complete coherent source upper bound on an ambient
   neighborhood. All its retained arguments and its original
   conditional root lie in
   \(Q=[.23,.45]+i[-.12,.12]\).
2. At edge three the reference-height source admits the original
   contour used in the completed vertical transport proofs, with
   cuts \(.15,.49\), alias heights \(\pm.2\), and root height
   at least \(-.108\). Its complete real tails have gap at least
   \(1/1000\), its horizontal aliases gap at least \(1/10\),
   and its zero mode and joins have rate at most its coherent
   critical action, with the original normalization.
   The second real coordinate remains in
   \((.267,.433)\) for type three or \((.24,.363)\) for type
   four. Its reference height is the original fixed \(c_2\).

These conditions hold in a sufficiently small horizontal neighborhood
of the actual reference. A concrete sufficient larger domain is any
such segment whose edge targets stay in the certified conditional
images of the
[reduced-disk theorem](research_mixed_reduced_disk_conditional_packets.md)
(or a separately proved complete source product), with their original
root branches and image bounds. Membership in an independent product
of plateau intervals is not asserted. In particular an unspecified
ambient source germ is not silently enlarged to all of \(Q^2\).

For edge three, both vertical transport arguments apply uniformly
with its new second argument held fixed. Their height derivatives do
not involve that argument. They use the complete reference-height
contour supplied in condition 2, rather than requiring the transported
target to be an actual critical reference of another word. Therefore
the [type-three transport](research_mixed_three_first_source_transport.md)
gives the allowance \(a_{c_2}(k)\), and the
[type-four fixed-contour theorem](research_mixed_four_fixed_contour_transport.md)
gives the allowance \(13/2000\), relative to the coherent action at
\((\widehat z_2,\widehat z_3)\).

## 2. The source ceiling before horizontal completion

Let \(M_{12}\) be the original allocated first-pair action:
the first cap and the first conditional, with the full first Fourier
weight and one half of the second. Let \(P_2\) be its original
second marginal and put \(p=\Re P_2\).
The first-pair absolute ceilings used by the completed collar proofs
are independent of the second real angle. They depend on its height
and selection, which are retained here. Combining them with the next
edge's vertical transport gives the following unrounded rate reserves:
\[
 \delta_{33}=3/100,\qquad
 \delta_{43}=3/125,\qquad
 \delta_{34}=\delta_{44}=87/2000.
 \tag{1}
\]
The first two are the strict pair-plus-allowance inequalities in
the type-three source theorem. The last is
\(1/20-13/2000\), using the ending-four pair ceiling before
its favorable supporting tangent.

Define the coherent post-pair action
\[
 \Psi_h(y)=\sum_{j=3}^{h}
       \phi_{\epsilon_{j-1},\epsilon_j}
                        (\widehat z_{j-1},\widehat z_j).
 \tag{2}
\]
Its allocation contains the remaining second Fourier halfweight,
the full weights at positions \(3,\ldots,h-1\), and half the
fixed cut weight. Thus no physical Fourier factor is counted twice.
The complete first-collar product through this cut has upper rate
\[
 M_{12}-\delta+\Re\Psi_h(y)+\eta,
 \qquad \delta=\delta_{3+\epsilon_1,3+\epsilon_2},
 \tag{3}
\]
where \(\eta>0\) is one prescribed total source and ordinary-color
tolerance for the fixed block. This is an inequality for the original
finite factors under Section 1, not monotonicity of their finite
values. Both first selections, when allowed, and the actual second
selection are retained. The subsequent comparison is at the original
complete-color reference.

## 3. The ordinary Schur coefficient is \(\pi/8\)

For one conditional factor of own type \(3+\epsilon\) and
first type \(3+\alpha\), before eliminating its index \(s\)
the allocated action is
\[
 Q_\epsilon(s;a,b)-(1+\alpha/2)g(a)-(1+\epsilon/2)g(b).
 \tag{4}
\]
Up to a polynomial with purely imaginary Hessian, its \(J\)-part is
exactly
\[
 V(s,a)+V(s,b)-\epsilon J(s)
                     -\tfrac\alpha2J(a)-\tfrac\epsilon2J(b),
 \qquad V(u,v)=J(u+v)-J(u)-J(v).
 \tag{5}
\]
Equation (5) of the
[open Hessian theorem](research_mixed_open_word_hessian.md)
gives \(-\Re V''>(\pi/8)I_2\) throughout \(Q^2\).
Also \(\Re J''>0\) on \(Q\). Thus the three-variable
negative Hessian in (4) has real part greater than
\((\pi/8)I_3\). Its complex Schur complement after eliminating
\(s\) retains the same lower bound. Indeed, for a vector in the
two retained coordinates append the solution of the eliminated
linear equation; pairing the full accretive matrix with this vector
gives the Schur form and a norm at least that of the retained vector.
Consequently
\[
             -\Re\phi_{\alpha\epsilon}''\succ(\pi/8)I_2
 \tag{6}
\]
wherever the entire continued conditional branch stays in \(Q^3\).

Each free coordinate in (2) occurs at least once; the first has only
edge three, and later free coordinates have two incidences. Therefore
\(-D_y^2\Re\Psi_h\succeq(\pi/8)I\) on the admitted
horizontal domain. The cut coordinate is fixed, and original
stationarity gives the exact gradient
\[
                  \nabla\Re\Psi_h(a)=(-p,0,\ldots,0).
 \tag{7}
\]
The sign is important: the first entry is the next edge's first
marginal, \(\partial_1\phi_3=-P_2\). All later derivatives
cancel between their two ordinary incidences. The cut has zero
displacement, so it contributes no boundary work.

Taylor integration on the actual horizontal segment gives
\[
 \Re\{\Psi_h(y)-\Psi_h(a)\}
            \le-pd_2-\frac\pi{16}\sum_{j=2}^{h-1}d_j^2.
 \tag{8}
\]
This is a uniform-in-length real variational inequality under the
stated source/branch domain; it does not claim that those source
hypotheses hold everywhere in the plateau.

## 4. The one real force, and an exact completion criterion

Combining (3) and (8), with
\(M_h=M_{12}+\Re\Psi_h(a)\), proves
\[
 \boxed{\quad
 \text{original block upper rate}-M_h
 \le-\delta-pd_2-\frac\pi{16}\sum_{j=2}^{h-1}d_j^2+\eta.
 \quad}
 \tag{9}
\]
Thus all admitted third-and-later real motions, with the second real
coordinate fixed, preserve the endpoint gap and add a quadratic loss.
The same is true for any admitted second motion in the favorable
direction \(pd_2\ge0\). It is unnecessary to charge each later
motion separately against the endpoint reserve.

If both second directions are allowed, completing the square gives
the sufficient upper bound
\[
 \text{upper rate}-M_h
                  \le-\delta+\frac{4p^2}{\pi}+\eta.
 \tag{10}
\]
No uniform bound \(4p^2/\pi<\delta\) is asserted. The missing
linear term cannot be paid simply by declaring all later coherent
residuals nonpositive.

There is an exact, potentially sharper one-variable criterion. Put
\[
 \begin{split}
 E_h(d)&=-\Re\{\Psi_h(a+d)-\Psi_h(a)+P_2d_2\},\\
 V_h(t)&=\min\{E_h(d):d_2=t,\ a+d\in\mathcal D\}.
 \end{split}
 \tag{11}
\]
Only nonempty fibers are included, and all their original edge
constants remain. Compactness gives the minimum. By (8),
\(V_h(t)\ge\pi t^2/16\). The unrelaxed sufficient boundary
condition is
\[
                   \sup_t\{-pt-V_h(t)\}<\delta.
 \tag{12}
\]
This retains the entire horizontal completion, including the response
of every later coordinate. Formula (10) is its explicit coarse bound.
A sharper angle-dependent first-pair estimate whose increment is at
most \(pd_2\) would instead cancel the force in (9) directly.
Neither route requires enumerating word lengths.

## 5. The precise remaining domain obstruction

The [finite-window reduction](research_mixed_open_finite_boundary_windows.md)
already pays the pinning fees and retains arbitrary safe mixed
interiors. The new full-collar buffered extension supplies a strict
left endpoint loss when the second and third real targets stay in
small coherent neighborhoods. Equations (9)--(12) identify what is
needed to remove that smallness condition:

* Complete horizontal source control and the original root branch on
  the proposed larger domain must first be supplied.
* The only uncancelled real load is \(p\) at position two; it must
  be paid by the true first-pair angle dependence or by (12).

The first item is a genuine noninclusion in current theorems. The
reduced-disk source covers coupled images of input disks of radii
\(.083,.060\), not the independent plateau square. For example
a type-four first target with real coordinate \(.45\) is outside
the radius-\(.060\) disk centered at \(.30-.052i\), whatever
its height. The cyclic plateau source bands also do not cover all
allowed open boundary heights down to \(-.102\). Even the common
Hessian rectangle starts at real coordinate \(.23\), whereas
the plateau begins at \(.22\). These facts do not exhibit a finite
kernel counterexample; they identify why a Hessian-only argument
cannot fill the source gap.

After these horizontal collar sectors, the finite boundary functions
still include left outgoing targets outside the collar and its
coherent reference germ, right targets outside the proved right half
and its reference germ, and selected or nonplateau symbols in the
finite physical buffers. Existing safe-interior repair flows do not
automatically reach those buffers: their refined reference windows
and their two endpoint tangents must still be retained. Short words
without the two good blocks remain complete finite boundary-source
problems, not checks of finitely many numerical levels.

Nothing here changes the remaining whole-contour, ordinary-boundary
strip, or arbitrary-short-filling obligations. In particular the
three/four family is not asserted to exhaust short fillings.
