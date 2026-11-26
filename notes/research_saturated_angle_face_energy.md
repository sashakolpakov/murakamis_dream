# Saturated angular faces: reduced energy and matched signs

Private written proof, 16 November 2026.

The endpoint-face theorem already computes the energy of an original
angular endpoint and characterizes its feasible deletion. This note
assembles that result with the reduced-angle fiber problem and finite
real-period compactness. The resulting identity is for the entire
reduced energy on a compatible face, with arbitrary positive charges.
At an actual finite-period limit, the sharp corner data give additional
sign and incidence constraints. These specify the classical rate a
genuine source reduction would have to produce. They do not identify an
angular side current with a deleted quantum source.

## 1. The original charged face and its exact fiber

Fix the original finite connected circle tree, a nonempty selected
set \(S\), and all edges incident to \(S\), counted once. Outside
angles are complete, and every selected vertex has positive original
degree. Keep the original real powers \(n_v\) and
positive real charges \(c_v\). In the integral filling convention
\(n_v=\eta_v-2p_v\), neither the carrier nor the slope is changed.
Write
\[
 t_v=s_v+i h_v,\qquad r_{v,e}=k_{v,e}+i g_{v,e},\qquad
 P_v=\sum_{e\ni v}r_{v,e}-i n_vt_v/2.
 \tag{1}
\]
The closed original angle body has \(|s_v|\leq\pi\), outside
\(s_b=0\), and
\[
 |s_v|+2|g_{w,e}|\leq\pi,\qquad
 |s_w|+2|g_{v,e}|\leq\pi,\qquad
 \sum_{e\ni v}g_{v,e}-n_vs_v/2=-\pi c_v\quad(v\in S).
 \tag{2}
\]
Assume strict feasibility. Its energy and reduced energy are
\[
 \mathcal E_G=4\sum_e(E_{P,e}+E_{Q,e}),\qquad
 e_{G,c}(s)=\min_{g\text{ satisfying }(2)}\mathcal E_G(s,g).
 \tag{3}
\]
Only nonempty fibers are assigned a value. No uniqueness of a closed
boundary fiber minimizer is asserted.

Choose a nonempty set \(C\subseteq S\), signs
\(\varepsilon_v=\pm1\), and set \(s_v=\varepsilon_v\pi\) on
\(C\). Delete \(C\) and every incident edge; let \(r_C\) be the
number of deleted edges, counted once. Write \(G'\) for the retained
forest and \(c'=c|_{S\setminus C}\). Retain all surviving selected
vertices, including isolated ones, with their original powers and
rows. In particular, an isolated vertex must satisfy
\[
                         n_ws_w=2\pi c_w,\qquad |s_w|\leq\pi.
 \tag{4}
\]
It is not silently removed. The retained outside data remain complete.
Define \(e_{G',c'}(s')\) by the same closed fiber minimization, with
the sum over retained edges; this also covers a fiber with no edge
variables if its remaining rows hold.

**Proposition 1 (exact reduced face factorization).** The full fiber
over \((\varepsilon\pi,s')\) is nonempty if and only if the retained
fiber is nonempty and
\[
 \boxed{\quad
 |\varepsilon_v n_v-2c_v|
 \leq L_v(s')
 :=\sum_{\substack{e=vw\\w\notin C}}
                     (1-|s_w|/\pi)\quad(v\in C).
 \quad}
 \tag{5}
\]
For every such \(s'\),
\[
 \boxed{\quad
 e_{G,c}(\varepsilon\pi,s')
       =r_C\pi M_\infty+e_{G',c'}(s'),\qquad
 M_\infty=4G_{\rm Cat}/\pi.
 \quad}
 \tag{6}
\]
The surviving charge lifts in this identity are exactly \(c'\).
Here \(G_{\rm Cat}=\sum_{\ell\geq0}(-1)^\ell/(2\ell+1)^2\).

**Proof.** At an edge incident to \(v\in C\), (2) forces
\(g_{w,e}=0\). Both incidences on an internal \(C\)-edge therefore
vanish. Every restored incidence at a surviving vertex is zero, so
its row is precisely its retained row, including (4).

The remaining choices at a removed vertex are independent intervals
\[
 |g_{v,e}|\leq(\pi-|s_w|)/2\quad(w\notin C),\qquad
 \sum_{e=vw,\ w\notin C}g_{v,e}
                =\frac{\pi}{2}(\varepsilon_v n_v-2c_v).
 \tag{7}
\]
Their sum interval gives (5). Choices for different removed vertices
are independent, even if they have a common surviving neighbor.
Consequently the full fiber is exactly the product of the retained
fiber and the interval-section polytopes (7).

For clarity, the original square coordinates at an ordered edge are
\[
 A_P=s_v/4-g_{w,e}/2,\quad A_Q=s_v/4+g_{w,e}/2,\qquad
 y_P=g_{v,e}/2+s_w/4,\quad y_Q=g_{v,e}/2-s_w/4.
 \tag{8}
\]
The archived endpoint-face computation gives the same value at every
side and every corner:
\[
 E_\square|_{\partial[-\pi/4,\pi/4]^2}
                    =G_{\rm Cat}/2=\pi M_\infty/8.
 \tag{9}
\]
For example its normalization is
\[
 E_\square(\pi/4,0)
 =\frac14\int_0^{\pi/2}\log(\sec u+\tan u)\,du
 =\frac12\int_{\pi/4}^{\pi/2}\log\tan v\,dv
 =G_{\rm Cat}/2.
 \tag{10}
\]
The side derivative is zero in the continuous boundary limit, and
continuity joins the side values at all corners. Each deleted edge
has both square factors on their boundaries by (8), hence contributes
exactly
\[
                       4(E_{P,e}+E_{Q,e})
                             =4G_{\rm Cat}=\pi M_\infty.
 \tag{11}
\]
Every retained square is unchanged. The energy is therefore the
retained energy plus this constant on the entire product fiber.
Taking minima proves (6). \(\square\)

Proposition 1 is the charged reduced-fiber form of the existing
endpoint-face theorem. The product proof does not require a matched
complex limit or sharp corners. The same algebra remains valid for
other specified real charges, including zero, whenever the displayed
fibers are defined; it does not authorize changing a charge in the
original finite source.

## 2. The uniform classical gap on this face

Suppose additionally that the original positive solution at \(P=-\pi i c\)
is supplied. Let \(z_0\) be its angle assignment, \(E_0=\mathcal E_G(z_0)\),
and let \(m\) be the original number of edges. The reduced-angle theorem
gives
\[
 \Delta_c=\min_{\partial\mathcal P_c}\mathcal E_G-E_0>0,\qquad
 M_G=mM_\infty-E_0/\pi.
 \tag{12}
\]
The boundary is relative to the original affine charge rows. Because
the original polytope has an interior point and every removed vertex
has an incidence, every feasible face in Proposition 1 is on that
boundary. Equations (6) and (12) give the uniform bound
\[
 \boxed{\quad
 (m-r_C)M_\infty-\frac{e_{G',c'}(s')}{\pi}
                      \leq M_G-\Delta_c/\pi<M_G.
 \quad}
 \tag{13}
\]
The same bound holds for any retained assignment in that fiber,
since its energy is at least its fiber minimum. This is a definite
positive gap depending only on the supplied original charged problem.
It requires no condition \(|n_v|\geq2\). In place of that condition
it requires the exact compatibility (5).

If a retained assignment is a matched positive inverse-period point,
its expression in (13) is its calibrated real charged action.
Otherwise (13) is only its angle-energy value. Deleting the saturated
vertices from a matched boundary point \(P=u-\pi i c\), as in
Section 3 below, does not in general preserve the real periods:
at a surviving vertex it removes the real returns \(k_{w,e}\).
If the retained edges remain positive, the new period is
\[
 P'_w=\left(u_w-\sum_{\substack{e=wv\\v\in C}}k_{w,e}\right)
                                      -\pi i c_w.
 \tag{14}
\]
It need not have real part zero. For degenerate retained assignments
no positive metric or stationary interpretation is assigned by (13).

## 3. Sharp finite-period saturation

Now assume \(S\) is proper in the connected original tree, and take
a bounded real-period sequence \(P(t^{(j)})=u^{(j)}-\pi i c\)
of positive points tending to a finite image boundary. Pass to the
joint finite limits supplied by the compactness theorem. Let
\[
 C=\{v\in S:|s_v|=\pi\},\qquad s_v=\varepsilon_v\pi,
 \tag{15}
\]
and suppose \(C\ne\varnothing\). This \(C\) includes all saturated
vertices. Write \(d_0(v)\) for its number of edges from \(v\) to
vertices outside \(C\), and \(d_{\rm in}(v)\) for its number of
neighbors in \(C\).

**Proposition 2 (matched corner signs).** Every cut neighbor
\(w\notin C\) of \(C\) has \(s_w=0\). At a cut edge \(e=vw\),
\[
 g_{w,e}=0,\qquad g_{v,e}=\tau_v\pi/2,\qquad
 \operatorname{sgn}k_{v,e}=\varepsilon_v,\qquad
                   \tau_v=\operatorname{sgn}h_v\in\{-1,1\}.
 \tag{16}
\]
Both incidences on internal \(C\)-edges are zero. Consequently
\[
 \boxed{\quad \varepsilon_v n_v-2c_v=\tau_v d_0(v).\quad}
 \tag{17}
\]
In particular the capacity inequality (5) is saturated.

**Proof.** The opposite incidence is zero by (2), so both
\(A\)-coordinates in (8) equal \(\varepsilon_v\pi/4\).
There are no open-side squares at a finite-period limit. Thus both
\(y\)-coordinates are corners. Solving their two possible signs gives
exactly
\[
 (s_w,g_{v,e})\in
 \{(0,\pi/2),(0,-\pi/2),(\pi,0),(-\pi,0)\}.
 \tag{18}
\]
The last two alternatives put \(w\) in \(C\).

At a sharp square corner the finite covectors satisfy
\[
 \operatorname{sgn}x=\operatorname{sgn}A,\qquad
 \operatorname{sgn}B=\operatorname{sgn}y,\qquad
            \sinh(2|x|)\sinh(2|B|)=1.
 \tag{19}
\]
For a cut edge \(y_P=y_Q=g_{v,e}/2\). The original matching
identities
\[
 k_{v,e}=x_P+x_Q,\qquad h_v=2(B_P+B_Q)
 \tag{20}
\]
therefore give both signs in (16), strictly. The proper-selection
observation bound also excludes \(h_v=0\) at every saturated vertex,
including one with no cut edge: otherwise \(t_v=\pm\pi\) would
make \(\cos(t_v/2)=0\). Thus \(\tau_v\) is defined throughout \(C\).
All cut incidences at a given vertex have the same sign.
Summing the unchanged primitive row gives (17). \(\square\)

At a cut neighbor \(s_w=0\) means \(t_w=i h_w\), not necessarily
\(t_w=0\). Such a surviving selected vertex must not be relabeled
as a complete outside vertex. If it becomes isolated after deletion,
its unchanged row (4) and \(s_w=0\) force \(c_w=0\). Hence this
cannot occur under the positive charges of the present theorem.
For a separate zero-charge sector it is an actual remaining row
obligation, not a license to discard the vertex or its finite trace.

The limiting assignment minimizes its fixed-\(s\) fiber: it minimizes
\(\mathcal E-u_*\cdot s\), whose second term is constant on that
fiber. Proposition 1 therefore identifies its exact reduced energy
with the deleted reduced energy. If (12) is available, (13) applies
to this boundary value with the same charge lifts and gap.

## 4. The component sign and an arithmetic resonance restriction

Retain the original edge root \(q_e\), rather than resetting its sign.
The finite observation identities are
\[
 a_v=\tan(t_v/2),\quad q_e^2=1+a_v^2+a_w^2,\qquad
                    \cosh r_{v,e}=\cos(t_w/2)q_e.
 \tag{21}
\]
At a cut edge, write
\(a_v=i\coth(h_v/2)\) and \(a_w=i\tanh(h_w/2)\).
Thus \(q_e=iQ_e\), \(Q_e\ne0\). Equations (16), (21), and
\(\cos(t_w/2)=\cosh(h_w/2)>0\) give
\[
                 \operatorname{sgn}Q_e=\varepsilon_v\tau_v.
 \tag{22}
\]
At an internal \(C\)-edge both tangent imaginary moduli exceed one,
so \(|Q_e|>1\). Since \(g_{v,e}=g_{w,e}=0\), its two instances
of (21), with
\(\cos(t_v/2)=-i\varepsilon_v\sinh(h_v/2)\), give
\[
       \operatorname{sgn}Q_e
              =\varepsilon_v\tau_v=\varepsilon_w\tau_w.
 \tag{23}
\]
Hence \(\sigma_C:=\varepsilon_v\tau_v\) is constant on each
connected component of \(C\). Internal edges never have \(q_e=\pm i\).

Here is a consequence usable by a separate exact deck calculation.
Fix \(v\in C\) and a nonempty set \(J_v\) of incident edges with
\(q_e=\sigma_e i\), \(\sigma_e=\pm1\); put \(r_v=|J_v|\).
They are cut edges, \(r_v\leq d_0(v)\), and every
\(\sigma_e=\varepsilon_v\tau_v\). Therefore
\[
 n_v+\sum_{e\in J_v}\sigma_e
   =\varepsilon_v\{2c_v+\tau_v(d_0(v)+r_v)\}.
 \tag{24}
\]
If a source calculation requires the left side to vanish, positivity
of \(c_v\) forces precisely the necessary arithmetic conditions
\[
 \tau_v=-1,\qquad 2c_v=d_0(v)+r_v,\qquad n_v=\varepsilon_v r_v.
 \tag{25}
\]
Moreover original strict feasibility implies
\[
 2\pi c_v
   \leq |n_v||s_v^{\rm int}|+2\sum_{e\ni v}|g_{v,e}^{\rm int}|
   <\pi(|n_v|+d_v)
 \tag{26}
\]
at any supplied strictly feasible assignment. Substituting (25) and
\(d_v=d_0(v)+d_{\rm in}(v)\) gives
\[
                              d_{\rm in}(v)>0.
 \tag{27}
\]
Thus an isolated saturated vertex cannot satisfy this resonance,
even when only some of its incident wires have \(q=\pm i\).
In particular all incidences cannot be escaping wires. At unit charge
a remaining candidate has \(d_0(v)=r_v=1\), \(n_v=\varepsilon_v\),
and at least one saturated neighbor. These are necessary conditions;
no realization or global exclusion of the remaining candidates is
claimed. Equation (24) is an arithmetic consequence of the original
period rows, not by itself a finite-source deck identity.

## 5. What still requires the actual source

The constant in (11), the exact reduced factorization (6), and the
gap (13) are classical statements about the original angle problem.
The archived one-step Ward current has its own exact physical-node
support and retained coupons. A general angular side at
\(t_v=\pm\pi+i h_v\), a wire-end residue, or a deck defect is not
identified with that current by a shared limiting real angle.
Their full Hermite normals, angular aliases, wire seams, and exterior
contractions must still be retained.

In particular, an energy comparison on a compatible deleted fiber
does not bound the entire deleted quantum source or show that a
given side current lands in that fiber. An unconstrained deleted
forest may have other assignments failing (5). Nor does the sign
restriction (25) imply that a nonresonant bulk term has a smaller
whole-current rate. The result supplies an exact boundary rate and
matching constraints for such a future reduction, without claiming
an arbitrary-short-filling asymptotic or a nonzero cycle coefficient.

## Direct sources and author readback

* [Endpoint-current angle face](research_endpoint_current_angle_face.md),
  SHA256 f84acb848b889a1553b467ba2d040884f7792a5ab0439eaada14a79216f363cc:
  original interval-section proof, exact square-boundary normalization,
  pointwise deleted-energy identity, and the distinction from actual
  finite current deployment. Complete source read in this sequence.
* [Reduced-angle inverse-period graph](research_reduced_angle_inverse_period_graph.md),
  SHA256 9575d0231700e49e46ddea42c989921ce23adaafaa6e81b4f4b83c16f227f0af:
  closed fiber problem with arbitrary positive charges, strict
  feasibility, original calibrated action, and the fixed positive
  boundary gap. Complete source reread.
* [Finite real-period compactness](research_real_period_image_compactness.md),
  SHA256 8ecdecc2c71e8a47a83fe60986ed618abaa926937920f376abebed779fb0c37e:
  finite matched sharp covectors, absence of open sides, retained
  matching identities and edge observations, and proper-selection
  observation units. Complete source reread.

Only written mathematics, text reads and metadata hashes were used.
No mathematical program, numerical calculation, test or compilation
was run. Adopted notes, manuscripts and public documents were unchanged.
