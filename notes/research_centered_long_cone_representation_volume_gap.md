# A uniform representation-volume gap along centered long cone paths

Research note, 18 November 2026.

For a fixed complete hyperbolic core, sufficiently long primitive filling
equations remain in one complete-holonomy chart throughout the cone-angle
cube. Near-maximal representation rigidity then gives a uniform volume
gap to every other representation satisfying the same centered equations.
The comparison is along the whole path, rather than only at its endpoints.

The conclusion concerns marked representations and their volumes.
It neither compares different logarithmic lifts of the same representation
nor transports the original quantum cycle.

## 1. Complete proof sources and the comparison data

The only proof sources are:

* **N**, [A uniform volume gap away from geometric holonomy](
  research_near_maximal_representation_volume.md), complete text.
  Its Theorem 1 and Corollary 2 give a fixed positive volume deficit
  outside any conjugacy-invariant neighborhood of the oriented complete
  holonomy. Its Sections 5--6 explain why every nearby peripheral
  decoration lies in the supplied positive gluing chart.
* **F**, [A finite positive certificate supplies every sufficiently long
  filling branch](finite_geometric_certificate_uniform_filling_existence.md),
  complete text. It supplies the actual centered peripheral germ,
  the uniform contraction for all primitive slope directions, and the
  absolutely normalized local volume expansion.

Let \(M\) be one fixed oriented complete finite-volume hyperbolic
three-manifold, with \(c\) torus cusps and volume \(V>0\). Supply the
actual positive complete marked triangulation required by these sources.
In an application, \(M\) may already be a fixed hyperbolic short partial
filling. Its primitive cusp paths and every earlier filling are fixed.

On cusp \(i\), choose the positively oriented primitive basis
\((\mu_i,\lambda_i)\). In the decorated complete-holonomy chart write
\(U_i,V_i\) for the centered logarithms of the projective similarity
multipliers. Thus these are twice eigenvalue logarithms; no central
\(\mathrm{SL}_2\) sign is inserted in them. Source F proves
\[
 V_i(U)=U_i\tau_i(U),\qquad
 \Im\tau_i(0)>0.
 \tag{1}
\]
All these are the actual peripheral words of \(M\).

Choose a subset \(I\) of cusps and primitive slopes
\((a_i,b_i)\in\mathbb Z^2\), \(i\in I\). Set
\[
 \ell_i=(a_i^2+b_i^2)^{1/2},\qquad
 \ell_{\min}=\min_{i\in I}\ell_i.
\]
For the empty subset take \(\ell_{\min}=+\infty\); its branch is the
complete representation and the same proof below gives the gap in N.
Choose signs \(\epsilon_i\in\{1,-1\}\) and real charges
\(\lambda=(\lambda_i)_{i\in I}\in[0,1]^I\). The prescribed equations are
\[
 U_j=0\quad(j\notin I),\qquad
 a_iU_i+b_iV_i=2\pi i\epsilon_i\lambda_i\quad(i\in I).
 \tag{2}
\]
On the constructed branch the first condition keeps every unfilled
physical main cusp complete.
At a coordinate \(\lambda_i=0\), equation (1) will also make that
selected cusp parabolic on the constructed branch.

Here is a precise convention for competitors. Each peripheral group
has a retained common fixed flag, and is parabolic, trivial, or fixes
both endpoints of an axis individually, as in N. On the selected cusps
its multipliers lie in a fixed sufficiently small neighborhood of one;
take their single-valued centered logarithms there and impose (2).
On all other cusps impose the stated boundary-parabolic condition.
These conditions describe actual decorated representations, modulo
simultaneous conjugation. They do not allow an arbitrary deck translate
of a centered logarithm to be substituted into (2).

Only competitors near complete holonomy need these small-multiplier
conditions in the proof: all representations outside the fixed
neighborhood already satisfy the stronger volume deficit supplied by N.

## 2. The uniform centered branch and its volume

There are constants \(L_0,C>0\), depending on the fixed marked
certificate, such that, whenever \(\ell_{\min}>L_0\), equation (2)
has one solution in a fixed centered chart for every
\(\lambda\in[0,1]^I\). Denote its representation by
\(\rho_{\mathrm g}(\lambda)\).

To see the uniformity directly, take the polydisk from F on which
\[
 \Im\tau_i\ge m>0,\qquad |\tau_i|\le T,\qquad
 \sum_j|\partial_j\tau_i|\le L.
\]
With \(c_0=m/\sqrt{1+T^2}\), the real two-column estimate in F gives
\[
 |a_i+b_i\tau_i(U)|\ge c_0\ell_i.
 \tag{3}
\]
Keep unfilled coordinates zero and use the fixed-point map
\[
 \mathcal T_{\lambda,i}(U)=
 \frac{2\pi i\epsilon_i\lambda_i}{a_i+b_i\tau_i(U)}.
 \tag{4}
\]
Since \(0\le\lambda_i\le1\), exactly the estimates of F give
\[
 \|\mathcal T_\lambda(U)\|_\infty
       \le\frac{2\pi}{c_0\ell_{\min}},\qquad
 \|D\mathcal T_\lambda(U)\|
       \le\frac{2\pi L}{c_0^2\ell_{\min}}.
 \tag{5}
\]
One fixed long-slope threshold makes the image lie in the interior
half-polydisk and the second bound smaller than \(1/2\).
This proves existence and uniqueness throughout the closed charge cube.
It also gives invertibility of the normalized filling Jacobian
\(I-D\mathcal T_\lambda\), with inverse norm at most two.
The branch is holomorphic in a neighborhood of each charge value;
uniqueness patches these neighborhoods along the whole cube.

Coordinatewise,
\[
 |U_i|\le\frac{2\pi\lambda_i}{c_0\ell_i},\qquad
 U_i=
 \frac{2\pi i\epsilon_i\lambda_i}{a_i+b_i\tau_i(0)}
       +O\!\left(\frac{\lambda_i}{\ell_i\ell_{\min}}\right).
 \tag{6}
\]
The constants do not depend on signs, directions, relative slope
lengths, or charges. If \(\lambda_i=0\), (4) gives \(U_i=V_i=0\)
exactly. Such a cusp remains nontrivial parabolic in the fixed chart.

The absolutely normalized volume expansion proved in F is
\[
 \operatorname{Vol}(\rho_U)
 =V-\frac14\sum_i\Im\tau_i(0)|U_i|^2
       +O\!\left(\|U\|_\infty\sum_i|U_i|^2\right).
 \tag{7}
\]
Substitution of (6) gives, uniformly on the entire charge cube,
\[
 \operatorname{Vol}(\rho_{\mathrm g}(\lambda))
 =V-\pi^2\sum_{i\in I}
       \frac{\Im\tau_i(0)\lambda_i^2}
            {|a_i+b_i\tau_i(0)|^2}
   +O\!\left(\ell_{\min}^{-1}
                    \sum_{i\in I}\frac{\lambda_i^2}{\ell_i^2}\right).
 \tag{8}
\]
In particular its volume loss is at most \(C\sum_i\ell_i^{-2}\).
At unit charges, F identifies this branch with the actual smooth
hyperbolic filling. At intermediate charges the argument here constructs
the actual representation path. If an actual cone deformation with these
centered periods is supplied in the chart, uniqueness identifies its
holonomy with this path. No separate metric-existence assertion at every
intermediate angle is needed for the volume comparison.

## 3. Uniform dominance over centered competitors

**Theorem.** There are \(L_*\) and \(g>0\), depending only on the fixed
marked core and certificate, such that for every subset \(I\), every
independently signed primitive slope tuple with
\(\ell_{\min}>L_*\), and every \(\lambda\in[0,1]^I\), each competitor
specified in Section 1 obeys
\[
 \rho\not\sim\rho_{\mathrm g}(\lambda)
 \quad\Longrightarrow\quad
 \operatorname{Vol}(\rho)
       \le\operatorname{Vol}(\rho_{\mathrm g}(\lambda))-g .
 \tag{9}
\]
The relation \(\sim\) is conjugacy of the underlying projective
representation. The assertion is signed, with the chosen orientation.
It does not separate central lifts or source decorations of one
underlying representation.

**Proof.** First choose a sufficiently small representation neighborhood
of the oriented complete holonomy, before choosing the slopes.
At each cusp retain a primitive element with nonidentity parabolic
complete image. Its nearby images remain nonidentity. Every fixed flag
of these nearby matrices lies near the unique complete flag: otherwise
a convergent subsequence of flags in \(\mathbb{CP}^1\) would produce a
second fixed flag of the nonidentity parabolic.

As explained in N, Sections 5--6, developing the supplied triangulation
from any such peripheral flags therefore gives positive shapes in its
fixed gluing chart. The normalized decorated representation and gluing
constructions are inverse there. Shrink this representation neighborhood
so every centered peripheral vector lies in the contraction polydisk of
Section 2. Its conjugacy saturation \(\mathcal U\) is open.

Consequently any competitor in \(\mathcal U\), with any retained flags,
satisfying the centered equations (2), is the unique fixed point (4).
It is conjugate to \(\rho_{\mathrm g}(\lambda)\). This uses centered
similarity logs of all the actual selected primitive words, rather than
traces or exponential filling equations alone.

N, Corollary 2, now gives a fixed \(\delta>0\) such that every admitted
representation outside \(\mathcal U\) satisfies
\[
                  \operatorname{Vol}(\rho)\le V-\delta.
 \tag{10}
\]
This estimate requires no bound on shape coordinates, chosen
conjugations, or peripheral translation lengths.
Increase the slope threshold until (8) gives
\[
       \operatorname{Vol}(\rho_{\mathrm g}(\lambda))>V-\delta/2
 \tag{11}
\]
for all charges, subsets and directions under consideration.
There are only finitely many cusps and subsets, so the same threshold
works for all of them. Every nonconjugate competitor lies outside
\(\mathcal U\); (10)--(11) prove (9) with \(g=\delta/2\).
\(\square\)

In particular (9) holds along every path in the charge cube, including
the straight cone path \(\lambda_i=t\), \(0\le t\le1\).
For a fixed hyperbolic short partial filling, the constants depend on
that entire short-filled core. There is no uniformity assertion over
varying short cores.

## 4. Exact volume ordering on the larger centered charge box

There is also an exact comparison of different nearby real charges.
It does not require that their magnitudes be at most one.
Choose a sufficiently small fixed \(\rho_*>0\). The same fixed-point
map, with numerator \(2\pi iq_i\), is a contraction for every
\[
 q\in\mathbb R^I,\qquad |q_i|\le\rho_*\ell_i.
 \tag{12}
\]
Indeed its image norm is at most \(2\pi\rho_*/c_0\), and its derivative
norm is at most \(2\pi L\rho_*/c_0^2\). Choose \(\rho_*\) so these
are within the fixed chart and below the contraction threshold.
Write \(\mathcal V(q)\) for the volume of the resulting representation.

Choose an integral complementary primitive curve on each selected cusp:
\[
 a_i d_i-b_i c_i=1,\qquad
 s_i=a_iU_i+b_iV_i=2\pi iq_i,\qquad
 W_i=c_iU_i+d_iV_i.
 \tag{13}
\]
The exact volume differential F(10) is invariant under this determinant-one
change of peripheral basis. Along the real charge box it therefore gives
\[
 d\mathcal V
 =\frac12\sum_i
       [\Re W_i\,d\Im s_i-\Re s_i\,d\Im W_i]
 =\pi\sum_i\Re W_i\,dq_i.
 \tag{14}
\]
Unfilled terms vanish since their \(U_i,V_i\) are identically zero.
By (1), (3) and (13),
\[
 W_i=2\pi iq_i
        \frac{c_i+d_i\tau_i(U)}{a_i+b_i\tau_i(U)},\qquad
 \Re W_i=
   -\frac{2\pi q_i\Im\tau_i(U)}
                {|a_i+b_i\tau_i(U)|^2}.
 \tag{15}
\]
Here the last identity uses
\(\Im[(c+d\tau)/(a+b\tau)]=\Im\tau/|a+b\tau|^2\);
the determinant in (13) fixes its sign. Consequently
\[
 \frac{\partial\mathcal V}{\partial q_i}
 =-\frac{2\pi^2q_i\Im\tau_i(U(q))}
               {|a_i+b_i\tau_i(U(q))|^2}.
 \tag{16}
\]
This is exact, including all coupling between cusps.
There is no uncontrolled derivative of the remainder in (8).

The volume is unchanged by independently reversing the sign of any
\(q_i\). For \(q_i\ne0\), change only that cusp's retained common
eigenflag to the other fixed flag of the same representation. This
negates \(U_i,V_i\) and keeps all other cusp logs unchanged. The
nearby-flags argument in Section 3 puts this decoration in the same
positive chart. Its centered charge is the sign-reversed tuple, so
uniqueness identifies it with that tuple's constructed representation.
The underlying representation has not changed. At \(q_i=0\) the
assertion follows directly, or by continuity.

Thus \(\mathcal V(q)\) is a function of the coordinatewise absolute
charges and is strictly decreasing in each \(q_i^2\) on (12).
More quantitatively, if \(q,\widetilde q\) lie in that box and
\(|q_i|\ge|\widetilde q_i|\) for every \(i\), integration of (16)
one coordinate at a time gives
\[
 \mathcal V(\widetilde q)-\mathcal V(q)
 \ge c_1\sum_i\frac{q_i^2-\widetilde q_i^2}{\ell_i^2},
 \qquad c_1=\frac{\pi^2m}{1+T^2}>0.
 \tag{17}
\]
We used \(|a_i+b_i\tau_i|^2\le(1+T^2)\ell_i^2\).
Equality of all absolute charges gives the same underlying
representation by the flag argument.

This box includes every sufficiently near-complete representation whose
centered primitive slope logs are purely imaginary. In fact
\[
 \frac{|q_i|}{\ell_i}
 \le\frac{\sqrt{1+T^2}}{2\pi}|U_i|.
 \tag{18}
\]
Shrink the representation neighborhood in Section 3 so the right side
is below \(\rho_*\). This shrink is independent of the slopes.
Representations outside it still have the fixed gap from N.

At unit charge, (17) compares every nonzero centered integer-charge
tuple \(q\in(\mathbb Z\setminus\{0\})^I\) in the neighborhood with
the tuple of unit absolute charges. If some \(|q_i|\ge2\), its volume
deficit is at least \(3c_1/\ell_{\max}^2\), where
\(\ell_{\max}=\max_{i\in I}\ell_i\). All tuples with \(|q_i|=1\)
give the same underlying representation. Outside the neighborhood,
combine N with (11). Thus the geometric comparison over all such
nonzero integer charges has a positive gap for each fixed long slope
tuple:
\[
 g_\sigma=\min\{\delta/2,\,3c_1/\ell_{\max}^2\}.
 \tag{19}
\]
This statement assumes that the centered primitive charges are those
integers; it does not infer this from an exponentiated filling equation.

More generally, if \(q_i=\lambda_i n_i\) with nonzero integers \(n_i\)
and \(\lambda_i\in[\lambda_0,1]\), \(\lambda_0>0\), the same argument
gives a gap
\(\min\{\delta/2,3c_1\lambda_0^2/\ell_{\max}^2\}\) to every different
underlying representation. This is a geometric statement for that
specified charge family, not an assertion that a deformation of the
original quantum kernel has been constructed.

For other charge families, the comparison across different classes need
not give a fixed positive gap up to every endpoint. For example,
\((\lambda-2)^2-\lambda^2=4(1-\lambda)\) tends to zero as
\(\lambda\uparrow1\); the two minimal signs then represent the same
underlying representation. Their source coefficients still need to be
combined with their actual signs and peripheral factors.

## 5. Why exponentiated projective data alone are insufficient

The same actual gluing germ shows why exponentiated slope equations
would be insufficient. Fill just one cusp, and fix
\(1/2<\lambda<1\). Formula (4) also defines the nearby actual
representation for the bounded signed charge \(\lambda-1\).
The two branches have the same exponentiated projective slope multiplier:
\[
       e^{2\pi i\lambda}=e^{2\pi i(\lambda-1)}.
 \tag{20}
\]
Nevertheless their volumes, by the same uniform expansion (8), satisfy
\[
 \operatorname{Vol}(\rho_{\lambda-1})
       -\operatorname{Vol}(\rho_\lambda)
 =\frac{\pi^2\Im\tau(0)(2\lambda-1)}
            {|a+b\tau(0)|^2}+O(\ell^{-3})>0
 \tag{21}
\]
for all sufficiently long slopes. The last inequality follows from
\(|a+b\tau(0)|\le C\ell\) and \(\Im\tau(0)>0\).
These are actual representations of the same fixed core, constructed
by its supplied positive germ. Equation (21) makes no assertion that
the second branch occurs in the original quantum cycle.

The two charges in (20) differ by an odd integer: the unsquared
\(\mathrm{SL}_2\) slope multiplier changes sign. Thus this comparison
does not apply to a source that separately fixes that sign. In the latter
case the possible charge shifts are even, and the geometric comparison
in Section 4 is the relevant one. Determining the actual congruence class,
including integer-spin channels and Weyl factors, is a literal source
calculation, not a consequence of projective volume rigidity.

Thus near-maximal rigidity does not select a logarithmic sheet. Even
within the complete neighborhood, the full source equations must be
matched to the centered primitive equations before (9) applies.
Representations outside that neighborhood already satisfy (10).

## 6. The remaining source question

This assembly replaces an arbitrary-cone maximality premise by a proved
geometric comparison for sufficiently long centered fillings of a fixed
core. It supplies a gap throughout the deformation and local isolation
of the marked representation branch. It does not identify every original
critical action with that volume, eliminate equal-action decorations,
or prove a quantum Hessian nondegenerate from the representation Jacobian.

In particular, an initially nonzero thimble coefficient is not transported
by this note. Applying (9) to that question still requires the actual
centered source marking and action normalization, the original relative
cycle with both endpoint currents, and control or exact cancellation of
source divisors and ends. Compactness of near-maximal representations
does not imply compactness of their highest-cut source coordinates.

## Frozen proof-source pins

* N: `research_near_maximal_representation_volume.md`,
  SHA256 `9ff00d61704e2fc7a13e8abb5cbd37d61d3413220bcc4e6f763609a48177f997`.
* F: `finite_geometric_certificate_uniform_filling_existence.md`,
  SHA256 `f3f78212e1f42f501593412a71c21590f24f8838f4add8abeb2f12534ad2b39b`.
