# Retained-boundary leaf energy and the exact parent budget

Private written proof, 16 November 2026.

The scalar terminal ceiling \(\mathcal I_n\) forgets the boundary
coupling of a leaf. The original square energy gives a precise
replacement: a one-variable closed minimization with an explicit
capacity domain. On a deletion face these minimizations separate
without separating their shared neighboring variables. Their
projected action has exactly the original parent comparison,
including the endpoint work.

This is a classical profile and an exact comparison criterion.
It is not a boundary-dependent upper bound for the quantum message
\(T(R^nB)\). Empty angle fibers are not assigned zero quantum sources.

## 1. The literal leaf fiber

Use the original edge energy
\[
 \begin{split}
 E(u,s,g,G)=4\{&
 E_\square(u/4-G/2,g/2+s/4)\\
 &+E_\square(u/4+G/2,g/2-s/4)\}.
 \end{split}                                                   \tag{1}
\]
The leaf real angle is \(u\), its outgoing incidence is \(g\);
the neighboring real angle and opposite incidence are \(s,G\).
The closed positive edge body is
\[
 |u|+2|G|\le\pi,\qquad |s|+2|g|\le\pi.                         \tag{2}
\]
The energy is continuous and convex on that body, with positive
definite Hessian in its interior. On the original positive chart,
\[
 dE=k_\ell\,du+k_w\,ds+h_\ell\,dg+h_w\,dG,
 \quad t_\ell=u+i h_\ell,\quad t_w=s+i h_w.                    \tag{3}
\]
These are the original normalizations; each edge contributes the
complete constant \(M_\infty=4G_{\rm Cat}/\pi\).

Suppose all other edges at the leaf go to saturated deleted vertices.
Their incidences at the leaf are zero. Fix their opposite incidences
\(\boldsymbol\beta=(\beta_1,\ldots,\beta_b)\); the cut edges impose
\[
                         |u|+2|\beta_i|\le\pi.                \tag{4}
\]
An empty list is allowed. Fix \(|s|\le\pi\) and
\(|G|,|\beta_i|\le\pi/2\), and put
\[
 a=\pi-2\max(|G|,|\beta_1|,\ldots,|\beta_b|).
 \tag{5}
\]
The original unit row at this leaf is
\[
                              g-nu/2=-\pi.                   \tag{6}
\]
No row at the neighbor or at a deleted vertex has been replaced.

**Proposition 1.** For \(n=\sigma m\ne0\), \(m=|n|\) an integer,
put \(u=\sigma v\). The exact closed fiber of (2),(4),(6) is
\[
 \boxed{\quad
 v\in I_n(s,G;\boldsymbol\beta)
 =\left[\frac{\pi+|s|}{m},
        \min\left(a,\frac{3\pi-|s|}{m}\right)\right],
 \qquad g=mv/2-\pi .
 \quad}                                                       \tag{7}
\]
It is nonempty exactly when
\[
 |s|+2m\max(|G|,|\beta_1|,\ldots,|\beta_b|)
                                      \le(m-1)\pi.             \tag{8}
\]
Its strict version is nonempty exactly when \(|s|<\pi\) and
the inequality in (8) is strict. Here strictness concerns the
surviving edge and the nonforced inequalities (4), not the
already saturated cut faces.

For \(n=0\) the closed fiber is empty. For \(n=\pm1\) it is
nonempty only at \(s=G=\boldsymbol\beta=0\), where
\(u=\sigma\pi,\ g=-\pi/2\).

*Proof.* The second inequality of (2) and (6) say
\[
             \pi+|s|\le nu\le3\pi-|s|.
\]
Thus \(nu>0\), and the remaining inequalities are \(v\le a\).
This proves (7). The lower endpoint is at most the second
upper endpoint because \(|s|\le\pi\); comparison with \(a\)
is exactly (8). The strict statements follow from the open
intervals, with \(|s|<\pi\) retained separately.
If \(n=0\), (6) forces \(g=-\pi\), violating (2).
If \(m=1\), (8) forces all the displayed boundary variables
to vanish and (7) is the asserted singleton. \(\square\)

Define the extended-valued retained-boundary profile
\[
 \mathfrak e_n(s,G;\boldsymbol\beta)
   =\min_{v\in I_n(s,G;\boldsymbol\beta)}
                  E(\sigma v,s,mv/2-\pi,G),                  \tag{9}
\]
with value \(+\infty\) on an empty fiber.
Set \(\mathfrak e_0\equiv+\infty\).
This minimum retains the cut constraints, even though their
edge energies have become constants.

## 2. Convexity, the regular locus, and the terminal constant

The profile is convex and lower semicontinuous on its capacity
domain. Indeed its epigraph is the infimal projection of the
convex epigraph of (1) subject to the original affine row and
the convex inequalities (2),(4). For lower semicontinuity,
take a convergent sequence of parameters and a convergent
subsequence of their minimizing leaf angles in the compact
interval \([-\pi,\pi]\). The limit is feasible and (1) is
continuous. This argument also proves attainment wherever
the profile is finite.

Call a point regular if a minimizing \(v\) obeys all the strict
inequalities used in Proposition 1. At such a point the minimum
is unique, including against boundary competitors, and real
analytic locally. The positive Hessian of (1), restricted to
the affine row, proves uniqueness by the segment argument;
its positive \(v,v\) entry proves the implicit-function claim.
The cut bounds are inactive in this neighborhood. Consequently
the profile is locally independent of \(\boldsymbol\beta\), and
its Hessian in \((s,G)\) is the positive Schur complement of the
Hessian in \((v,s,G)\).

At a regular minimum, (3) gives
\[
 k_\ell+n h_\ell/2=0,\qquad g-nu/2=-\pi,\qquad
                   d\mathfrak e_n=k_w\,ds+h_w\,dG.             \tag{10}
\]
Thus it reconstructs the actual one-edge leaf period, with its
retained boundary data. Strict linear feasibility alone is not
being used to assert an interior minimum or a global positive
stationary chart.

For \(|n|=m\ge2\), let \(z_n^\circ\) be the selected terminal
solution whose neighbor is complete. The terminal action source
gives, for positive \(n\),
\[
 t_\ell^\circ=2A_m-2iB_m,\quad B_m>0,\quad
             \pi/2<mA_m<\pi,\quad A_m<\pi/2 .
 \tag{11}
\]
For negative \(n\), reflect \(t_\ell^\circ\) to
\(-\overline{t_\ell^\circ}\). In both cases
\[
 s^\circ=G^\circ=0,\quad
 u^\circ=\operatorname{sgn}(n)\,2A_m,\quad
 g^\circ=mA_m-\pi .
\]
These inequalities place the entire reference edge strictly
inside (2). Its original calibration is
\[
 E_n^\circ:=E(z_n^\circ)
                         =\pi(M_\infty-\mathcal I_n).          \tag{12}
\]
There is no volume identification in (12).

Its full ambient differential is
\[
               dE(z_n^\circ)=-H_n^\circ\,d(g-nu/2),
                      \qquad H_n^\circ=2B_m>0.                \tag{13}
\]
Both neighboring coefficients vanish: \(k_w=h_w=0\).
Let \(D_n^\circ(z)\) be the Bregman remainder of (1) at this
reference point. On every weak unit-row edge,
\[
 E(z)=E_n^\circ+D_n^\circ(z),\qquad D_n^\circ(z)\ge0,
 \tag{14}
\]
with equality only at \(z_n^\circ\). Strictness follows from
strict convexity along the segment from that interior point.
In particular, whenever (9) is finite,
\[
 \mathfrak d_n(s,G;\boldsymbol\beta)
 :=\mathfrak e_n(s,G;\boldsymbol\beta)-E_n^\circ
                          =\min_{\text{fiber}}D_n^\circ\ge0.  \tag{15}
\]
Equality holds precisely when \(s=G=0\) and the cut bounds
allow \(v=2A_m\). It does not require the cut incidences to
vanish individually.

For \(n=\pm1\), the sole feasible edge is on the boundary and
has energy \(\pi M_\infty\). Use
\(E_{\pm1}^\circ=\pi M_\infty\), consistent with
\(\mathcal I_{\pm1}=0\), and define
\(\mathfrak d_{\pm1}=\mathfrak e_{\pm1}-E_{\pm1}^\circ=0\)
on its singleton domain. No Bregman reference is asserted
in this case.

## 3. Fixed incidence is different from real external height

On a regular positive leaf chart put
\[
 S_{\rm leaf}(t_w)=
       \psi(t_\ell,t_w)+\frac{in}{4\pi}t_\ell^2-it_\ell,
 \tag{16}
\]
where the original unit primitive is stationary in \(t_\ell\).
The edge calibration and (6) give exactly
\[
 \boxed{\quad
 \mathfrak e_n
       =\pi(M_\infty-\Re S_{\rm leaf})+h_wG,
       \qquad \partial_G\mathfrak e_n=h_w .
 \quad}                                                       \tag{17}
\]
Indeed in the calibration the leaf-height coefficient is
\(g-nu/2+\pi=0\). The remaining work is the displayed
\(h_wG\), with its original sign.

Thus imposing a real external angle means stationarity in
\(G\), not fixing \(G=0\). For \(|n|\ge2\), near the complete
reference with cut incidences zero, the positive Hessian gives
a unique interior minimum in both \(v,G\) at each sufficiently
small real \(s\). It is the continuation of the original terminal
branch. Therefore
\[
 \min_G\mathfrak e_n(s,G;0)
                   =\pi(M_\infty-\Re S_n(s))                  \tag{18}
\]
on this neighborhood, with the phase and primitive of the
terminal action source. Its integral calibration equivalently
uses the partial characteristic integral at
\((\pi-|s|)/(2\pi)\).

The minimizing incidence is generally nonzero. For positive \(n\)
and \(0<s<\pi\), the continued phase's incidence is
\[
 G_n(s)=\Im\operatorname{asinh}\!
       \left(\zeta_n(\cos(s/2))\tan(s/2)\right)>0.              \tag{19}
\]
The chosen \(\zeta_n\) lies in the first quadrant; the principal
inverse hyperbolic sine has positive imaginary part there.
Reflection gives the corresponding sign for negative \(n\)
or negative \(s\). In the small positive neighborhood just
specified, this is the minimizing incidence, and strict
convexity consequently gives
\[
 \mathfrak e_n(s,0;0)>
                    \min_G\mathfrak e_n(s,G;0)\qquad(s\ne0).
 \tag{20}
\]
Neither (18) nor a positive-cell interpretation is extended
through a boundary minimum or outside that regular branch.
The terminal phase source itself allows continuation beyond
its positive-cell domain.

## 4. Exact projection of a saturated deletion face

Retain a supplied positive unit-charge parent, complete outside
angles, and all the notation of the fixed-parent calibration:
the included edge count \(e_G\), raw energy \(\mathcal E\),
parent \(z_0\), heights \(H_v^0\), action \(M_G\), and
Bregman remainder \(D_0\). Its uniform ambient boundary gap
is \(\delta_0=\min_{\partial X}D_0>0\).

Fix a nonempty deleted set \(C\), signs \(\varepsilon_v\), and
the compact weak face
\[
 \mathcal F_C=\{z\in\overline X:
    s_v=\varepsilon_v\pi\ (v\in C),\
    \rho_w=-\pi\ (w\notin C,\ w\text{ selected})\}.
 \tag{21}
\]
Only nonempty such faces are used below. Let \(r_C\) count
their incident edges, once each. Choose current surviving
leaves \(L\): each has exactly one remaining included edge,
all its other original edges go to \(C\), and the chosen
leaf edges are distinct with no two chosen leaves adjacent.
The neighbor can be another selected vertex or a complete
outside vertex. All neighboring rows and shared incidences
remain in place.

Project away only \(u_\ell\) and its sole surviving incidence
\(g_{\ell,e_\ell}\), for \(\ell\in L\). Call the retained
coordinates \(b\), and their compact convex image \(\mathcal B_C\).
In particular \(b\) retains \(s_w,G_\ell\), every cut-opposite
incidence \(\beta_{\ell,i}\), and every deleted comparison row
\[
                    c_v(b)=\varepsilon_v n_v/2
                              -\sum_{e\ni v}g_{v,e}/\pi .
 \tag{22}
\]
Every opposite surviving incidence on a cut edge is zero.
The full fiber over \(b\) is exactly the product of the
intervals (7). All other constraints involve retained
coordinates only. Thus Proposition 1 gives the explicit
additional capacity inequalities defining \(\mathcal B_C\);
no neighboring variable is optimized separately for different
leaves. In particular a chosen zero-power leaf makes this
weak face empty, not a zero quantum source.

Let \(\mathcal E_R(b)\) be the energy of edges neither incident
to \(C\) nor among the chosen leaf edges. The boundary-square
constant and the independent leaf minima give
\[
 \min_{\mathcal F_C\text{ over }b}\mathcal E
 =r_C\pi M_\infty+\mathcal E_R(b)
                              +\sum_{\ell\in L}\mathfrak e_{n_\ell}(b).
 \tag{23}
\]
Every cut edge, including internal \(C\)-edges, occurs in
the first term exactly once.

For endpoint heights \(h_v\ge0\), keep the entire classical
paired-current work
\[
 W_h(b)=\sum_{v\in C}h_v(c_v(b)-1).
\]
It is constant along each leaf fiber. The projected action is
\[
 A^{\rm red}_{C,L}(h;b)
 =(e_G-r_C)M_\infty
 -\frac{\mathcal E_R(b)+\sum_\ell\mathfrak e_{n_\ell}(b)}{\pi}
 +W_h(b).
 \tag{24}
\]
It is exactly the maximum of the original angle functional
\(A_C(h;z)\) over that fiber.

**Theorem 2.** The sharp uniform classical gap for (24) is
\[
 \begin{split}
 \Gamma_{C,L}(h)
 &:=\min_{b\in\mathcal B_C}
                        \{M_G-A^{\rm red}_{C,L}(h;b)\}\\
 &=\min_{z\in\mathcal F_C}
       \left\{\frac{D_0(z)}{\pi}
        +\sum_{v\in C}(H_v^0-h_v)(c_v(z)-1)\right\}.
 \end{split}                                                   \tag{25}
\]
Both minima are attained. A strict uniform gap is equivalent
to \(\Gamma_{C,L}(h)>0\). At the parent terminal heights,
\[
                         \Gamma_{C,L}(H_C^0)\ge\delta_0/\pi.  \tag{26}
\]
The same terminal-height collar and constants as in the
fixed-parent theorem retain its \(\delta_0/(2\pi)\) gap.

*Proof.* The exact calibration on (21) is
\[
 M_G-A_C(h;z)=D_0(z)/\pi+
                  \sum_{v\in C}(H_v^0-h_v)(c_v(z)-1).
 \tag{27}
\]
The work is fixed along the fiber, and (23) minimizes its
energy, proving (25). The original face is compact and all
terms on its right are continuous, so the extrema are
attained. Equivalently the reduced energy is lower
semicontinuous on its compact base. Every point of the
nonempty saturated face is on \(\partial X\); (26) and
the same height-collar estimate follow from (27).
No interior leaf minimizer is needed in this proof. \(\square\)

For comparison, replacing each profile by its complete-neighbor
constant raises (24) to
\[
 \widehat A_{C,L}(h;b)
 =(e_G-r_C-|L|)M_\infty-\mathcal E_R(b)/\pi
                         +\sum_{\ell\in L}\mathcal I_{n_\ell}+W_h(b).
 \tag{28}
\]
Its exact loss of parent budget is
\[
 M_G-\widehat A_{C,L}
 =M_G-A^{\rm red}_{C,L}
                         -\frac1\pi\sum_{\ell\in L}\mathfrak d_{n_\ell}(b).
 \tag{29}
\]
Hence the necessary and sufficient uniform criterion for
this scalar-ceiling angle envelope is positivity of the
minimum of (29) over the SAME projected capacity base.
It is an explicit convex minimization: after cancellation
the objective contains \(\mathcal E_R/\pi\), an affine work
term, and constants. The parent boundary gap alone does not
bound the nonnegative coupling costs in (29).

## 5. Source scope and prior coverage

Convex infimal projection, the regular-locus Schur complement,
and their general limitations were already established in the
reduced-angle graph theorem. They are not new abstract results
here. The new specialization is the literal leaf interval with
all cut and shared incidences, its terminal constant and outside
work, and its exact placement in the saturated parent budget.

The actual leaf theorem bounds \(T(R^nB)\) on the real output
interval by the scalar rate \(\mathcal I_n\), retaining all
physical first normals and bounded microscopic parameters.
It does not supply an upper bound with the smaller retained
profile (24), on complex parent boundaries or otherwise.
Nor does a feasible profile impose angle support on the
actual quantum message. Consequently (25)--(29) are classical
comparison statements and precise targets for such a source
estimate, not a general boundary-current bound or a
noncancellation theorem. Empty fibers, active constraints,
and the actual outer currents remain.

The following complete direct sources were freshly read in
this author sequence, with their used implications and pins checked:

* [Original reduced-angle graph](research_reduced_angle_inverse_period_graph.md),
  SHA256 9575d0231700e49e46ddea42c989921ce23adaafaa6e81b4f4b83c16f227f0af:
  the raw square energy, full edge differential, convex extension
  and the existing regular-fiber argument.
* [Fixed-parent global calibration](research_fixed_parent_height_global_calibration.md),
  SHA256 268da098a6650065dc2abada9ce7c1bd8029abc33feb59783a67f03cd25a7bf0:
  ambient parent differential, every saturated-edge constant,
  paired endpoint work and the uniform terminal collar.
* [Terminal characteristic action](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd:
  the original signed terminal primitive, its interior
  complete-neighbor reference, phase constant and partial integral.
* [Literal filled-leaf source](research_filled_leaf_endpoint_product_upper_bound.md),
  SHA256 5a5f9be510823289b97c1c4df6104d95156b43a881fe148adf592ed5b5adc844:
  the exact \(T(R^nB)\) placement and the scope of its proved
  real-output upper rate.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Adopted notes and public manuscripts are unchanged.
