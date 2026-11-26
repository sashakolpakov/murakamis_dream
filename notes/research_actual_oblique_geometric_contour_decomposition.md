# An exact oblique contour decomposition through the geometric point

Private written proof, 18 November 2026.

For any fixed finite braid of a hyperbolic knot, the literal root
state has an exact contour decomposition with a distinguished
translated real sheet passing through the regular geometric point.
Its local coefficient is \(+1\). The construction retains an exact
physical boundary band, every initial mixed rectangle current,
every translated side current and all other horizontal sheets.
No factorial divisor occurs in the constructed bulk prisms.

This supplies a whole-source domain and a relative-current
decomposition, not a thimble coefficient or a scalar lower bound.
The geometric centralizer remains a null direction. The retained
boundary terms and other sheets have not been bounded by smaller
actions. Their number or their geometric mass alone cannot provide
that estimate.

The complete proof directs are A, the literal factorial amplitude,
and L, the local geometric period for any braid. All new coordinate,
cell, translation and orientation calculations are given below.

## 1. Primitive cut-and-transfer coordinates and a strict interior

Let the fixed braid have \(c\) crossings, let \(m=c+1\), and put
\[
 d=N-1,\qquad h=2\pi i/N,\qquad c_0=2\pi i.
 \tag{1}
\]
Use as independent integer coordinates the cut occupation \(a\)
and every signed-crossing transfer \(n_1,\ldots,n_c\).
At a positive crossing the two oriented strand visits change
occupation by \(-n_i,+n_i\); at a negative crossing they change it
by \(+n_i,-n_i\). Traverse the single oriented knot from the cut.
Every wire occupation is thereby an integer linear form
\[
                   \ell_e(k)=a+\sum_i\epsilon_{ei}n_i,
             \qquad \epsilon_{ei}\in\{-1,0,1\}.
 \tag{2}
\]
Each transfer is encountered with both signs before returning to
the cut, so the final occupation is exactly \(a\). Conversely the
cut and transfers of a matching state recover all its wires by
this traversal. Thus these coordinates identify the whole
matching lattice with \(\mathbb Z^m\), with no index factor.

Equivalently, split each crossing into its two strand visits and
join the donor to the receiver by a transfer edge. The wire edges
form one directed knot cycle. That wire cycle with the cut edge
removed is a spanning tree; the cut and \(c\) transfer edges are its chords.
The traversal above is the direct integer reconstruction on this
expanded graph.

The actual support is exactly
\[
 S_N=\{k\in\mathbb Z^m:0\le \ell_e(k)\le d
                  \text{ for every wire},\quad n_i\ge0\}.
 \tag{3}
\]
The positive inequalities \(n_i\le a_{\rm in}\) and
\(n_i\le d-b_{\rm in}\), and the analogous negative inequalities,
are the nonnegativity and upper bounds of the output wires.
In particular \(0\le n_i\le d\) follows from (3).
All five factorial arguments of each literal crossing in A are
wire occupations or transfers. No support value is extended
cyclically or assigned an artificial negative factorial.

Let \(\mathscr L\) be the finite list consisting of every wire
form (2) and the coordinate forms \(n_i\). It has nonzero integer
rows, and the support is equivalently \(0\le\ell(k)\le d\) for
all \(\ell\in\mathscr L\). This list may contain repetitions.
Set
\[
 L_0=\max_{\ell\in\mathscr L}\sum_j|\ell_j|,
 \qquad B\in\mathbb Z,\qquad B>L_0/2+2.
 \tag{4}
\]

There is a strict real normalized interior independent of \(N\).
Take
\[
 x^0_{\rm cut}=\tfrac12,\qquad
 x^0_{n_i}=\varepsilon_0=\frac1{8(c+1)}.
 \tag{5}
\]
During the knot traversal each transfer has coefficient \(0\)
or \(\pm1\), so every wire lies strictly between \(3/8\) and
\(5/8\). Every transfer equals \(\varepsilon_0>0\).
Consequently all \(\ell(x^0)\) lie in a fixed compact subinterval
of \((0,1)\). This also tracks the upper endpoint \(d=N-1\):
for all sufficiently large \(N\), a fixed real neighborhood of
\(Nx^0\) of radius proportional to \(N\) has every form in
\([B,d-B]\). The required threshold may depend on the fixed braid.

## 2. The geometric chart and the literal holomorphic domains

Use L's complex-binomial cut with parameter \(\theta\), and its
original scalar normalization. Its actual interpolated summand
will be denoted \(I_N(z)\), now in the coordinates of Section 1.
It includes the exact binomial Gamma factor, signed crossing
monomials, Cartan line, tail pivots and framing.

The change from L's primitive chord coordinates to these coordinates
is integral and unimodular. The cut clock and every transfer clock
at its chosen geometric point are off the unit circle. Hence in
the new coordinates the same point \(x^*\) satisfies
\[
 \Im x^*_j\ne0\quad(1\le j\le m),\qquad
 \Im\ell(x^*)\ne0\quad(\ell\in\mathscr L).
 \tag{6}
\]
The wire assertions follow from the same common frame. All
logarithmic flow relations remain exact under the coordinate
change. The corrected integer character is correspondingly
an integer vector \(q\in\mathbb Z^m\). Fix it once and put
\[
                       J_N(z)=e^{-c_0q\cdot z}I_N(z).
 \tag{7}
\]
At every original integer state the new character is one.
Near \(x^*\), L gives the actual nonzero local amplitude,
additive principal stationarity, and geometric action rate.
No character is changed during the contour construction.

We use two elementary consequences of A's exact marked product.
The root factorial \(\widehat F_N(\zeta)\) is holomorphic and
nonzero for
\[
                  -1<\Re\zeta<N,
 \tag{8}
\]
and also at every nonreal \(\zeta\). For (8), every Gamma
argument in A's product has positive real part, and its normally
convergent logarithm is finite. For nonreal \(\zeta\),
\(\zeta/N\) lies in A's slit domain; its product there is
holomorphic and nonzero. These are the same marked function.

The binomial interpolant
\[
 \frac{\Gamma(N)}
 {\Gamma(z_{\rm cut}+1)\Gamma(N-z_{\rm cut})}
          \theta^{z_{\rm cut}}(1-\theta)^{d-z_{\rm cut}}
 \tag{9}
\]
is entire in \(z_{\rm cut}\), with its fixed logarithms; it
introduces zeros but no poles. All remaining exact monomials
in \(I_N\) are entire nonzero exponentials. Therefore \(J_N\)
is holomorphic on any region where every factorial form is
either in (8) or nonreal. This conclusion concerns the actual
full summand, not only its principal action.

## 3. Retain the whole boundary band

Define the bulk states and their indicator by
\[
 R_N=\{k\in\mathbb Z^m:B\le\ell(k)\le d-B
                              \text{ for every }\ell\in\mathscr L\},
 \qquad \chi_N={\bf1}_{R_N}.
 \tag{10}
\]
They are a subset of \(S_N\). Keep the complementary states
\(S_N\setminus R_N\) exactly as their original positively
oriented small product tori. Denote their sum by
\(\Gamma_N^{\rm band}\). Their radii can be chosen small and
fixed in unscaled coordinates so that every factorial form
has real part in \((-1,N)\) and no other integer pole is
enclosed. Equation (8) verifies this at every supported state.
The band is not discarded or estimated.

There are \(O(N^{m-1})\) band states. Indeed every such state has
some fixed nonzero integer form within a fixed distance of
one of its two physical supporting hyperplanes. All independent
coordinates lie in \([0,d]\). Fix the other \(m-1\) coordinates
and one nonzero coefficient of that form; only \(O(1)\) choices
of the remaining coordinate lie in the band. Sum over the
finite list of forms. This count gives no bound on their
weighted sum.

For \(k\in R_N\), the closed unit cube
\[
 C_k=\prod_j[k_j-\tfrac12,k_j+\tfrac12],\qquad
                         \Omega_N=\bigcup_{k\in R_N}C_k
 \tag{11}
\]
has every factorial form in \([2,d-2]\) on its real points,
by (4). The union is an oriented real polyhedral \(m\)-chain,
with the standard \(dx_1\wedge\cdots\wedge dx_m\) orientation.
It contains a real neighborhood of \(Nx^0\) of radius
proportional to \(N\), for all sufficiently large \(N\).
This holds even if \(Nx^0\) lies on a unit-cell boundary:
all cells meeting a sufficiently small proportional
neighborhood are bulk cells by the strict margin in (5).

## 4. Polarized residue kernels and initial rectangle currents

Put
\[
 \epsilon_j=\operatorname{sgn}(\Im x^*_j),\qquad
 K_{\epsilon_j}(z_j)=\pi\cot(\pi z_j)-i\pi\epsilon_j,
\]
\[
 \omega_N=\frac1{(2\pi i)^m}J_N(z)
                       \prod_jK_{\epsilon_j}(z_j)\,dz_1\cdots dz_m.
 \tag{12}
\]
Every kernel has residue one at every integer. Thus the
original small-torus residue identity is still exactly
\[
                         \int_{\Gamma_N}\omega_N=K_N.
 \tag{13}
\]
The subtraction in (12) is recorded off the lattice, not
treated as equality of meromorphic integrands. Replacing
one cotangent by its subtracted constant removes that
coordinate's lattice-pole family and integrates to zero
on each original supported torus.

Choose a positive vector \(a=(a_1,\ldots,a_m)\) sufficiently
close to \((|\Im x^*_1|,\ldots,|\Im x^*_m|)\) that
\[
 \operatorname{sgn}\ell(\epsilon a)
                      =\operatorname{sgn}\Im\ell(x^*)
                          \quad(\ell\in\mathscr L).
 \tag{14}
\]
Here signs act coordinatewise, and the quantities are real.
Require in addition
\[
                 \ell(\sigma a)\ne0
       \quad(\ell\in\mathscr L,\ \sigma\in\{\pm1\}^m).
 \tag{15}
\]
This is possible: (14) is an open condition at the original
positive vector, while (15) excludes only finitely many proper
real hyperplanes. Every row of \(\mathscr L\) is nonzero.
Fix a small positive number \(\eta\).

For each coordinate and integer \(l\), let \(H_{j,\sigma}^{\,l}\)
be the interval
\([l-\tfrac12,l+\tfrac12]+i\eta\sigma a_j\), oriented in
increasing real direction. Let \(V_j^{\,l}\) be the interval
\(l+\tfrac12+i[-\eta a_j,\eta a_j]\), oriented upward.
The positively oriented rectangle boundary about \(l\) is
\[
 B_j^{\,l}=\sum_{\sigma=\pm1}(-\sigma)H_{j,\sigma}^{\,l}
                                  +V_j^{\,l}-V_j^{\,l-1}.
 \tag{16}
\]
Every product rectangle over a bulk cell is a valid residue
cycle: on its whole product box every factorial real part
stays in \([2,d-2]\), and each coordinate rectangle encloses
only its original integer. Its period is the corresponding
literal summand.

Expand \(\sum_k\chi_N(k)\prod_jB_j^{\,k_j}\) in the coordinate
order \(1,\ldots,m\). For \(J\subseteq\{1,\ldots,m\}\), define
\[
 \Delta_J\chi_N(l)=
       \sum_{\delta\in\{0,1\}^{J}}(-1)^{|\delta|}
                                                 \chi_N(l+\delta).
 \tag{17}
\]
Finite index shifts in (16), with no integration by parts
in the source, give the exact chain identity
\[
 \sum_k\chi_N(k)\prod_j B_j^{\,k_j}
 =\sum_{\sigma\in\{\pm1\}^m}c_\sigma
                       (\Omega_N+i\eta\sigma a)
                      +\mathcal M_N,\qquad
 c_\sigma=\prod_j(-\sigma_j),
 \tag{18}
\]
where the complete mixed current is
\[
 \mathcal M_N=
 \sum_{\varnothing\ne J\subseteq[m]}\ \sum_l
 \Delta_J\chi_N(l)
 \sum_{\sigma\in\{\pm1\}^{J^c}}
       \left(\prod_{j\notin J}(-\sigma_j)\right)
       \prod_{j=1}^m
       \begin{cases}
           V_j^{\,l_j},&j\in J,\\
           H_{j,\sigma_j}^{\,l_j},&j\notin J .
       \end{cases}
 \tag{19}
\]
Products in (19) always have the stated coordinate orientation.
These are explicit integer coefficients, including all
intersections and cancellations; no mixed face is suppressed.

Whenever \(\Delta_J\chi_N(l)\ne0\), at least one adjacent
cube is a bulk cube, and the displayed face lies in its
boundary. Its factorial real parts therefore remain in
the physical strip. Each vertical coordinate is half-integral
in real part; each horizontal coordinate has nonzero
imaginary part. Thus every cotangent factor is regular on
the whole mixed current.

Furthermore such a coefficient occurs only within a bounded
unscaled distance of a facet of (10). If all defining
indicators were constant on the cube \(l+\{0,1\}^{J}\),
the alternating sum would vanish. A changing indicator
has its defining form within \(\sum_{j\in J}|\ell_j|\)
of its threshold. These currents are consequently in
fixed-width physical facet bands, with all their exact
multiplicities retained. They have \(O(N^{m-1})\) cells;
several difference directions may lie on a single slanted
facet, so higher codimension is not asserted.

## 5. Simultaneous oblique translation of each horizontal sheet

Let \(v_\sigma=\sigma a\) and \(\delta=x^*-x^0\).
For the preferred sign vector \(\epsilon\), choose the path
\[
 b_\epsilon(t)=(1-t)i\eta v_\epsilon+tN\delta,
                               \qquad 0\le t\le1.
 \tag{20}
\]
For every other sign vector choose
\[
 b_\sigma(t)=i\bigl((1-t)\eta+tN\bigr)v_\sigma.
 \tag{21}
\]
All coordinates of \(x+b_\sigma(t)\), with \(x\in\Omega_N\),
have fixed nonzero imaginary signs \(\sigma_j\). In (20)
this uses \(\operatorname{sgn}\Im\delta_j=\epsilon_j\).
Hence no coordinate lattice pole occurs in any prism.

Every factorial form on these prisms has a fixed nonzero
imaginary sign as well. For (21) this is (15). For (20),
\[
 \Im\ell(x+b_\epsilon(t))
    =(1-t)\eta\ell(v_\epsilon)
                            +tN\Im\ell(x^*),
 \tag{22}
\]
whose two terms have the same nonzero sign by (14).
For all sufficiently large \(N\) its absolute value is
bounded below by a positive constant independent of \(N\).
The same holds for (21). Section 2 proves that the entire
literal summand is holomorphic on a neighborhood of every
closed prism. Thus no additional factorial/source-divisor
current is hidden in these translations.

Give \([0,1]\times\Omega_N\) the orientation \(dt\wedge dx\),
and map it by \((t,x)\mapsto x+b_\sigma(t)\). Define
\(\mathcal S_{\sigma,N}\) as the image of
\([0,1]\times\partial\Omega_N\), with the \(dt\)-then-boundary
orientation. Since
\[
 \partial([0,1]\times\Omega_N)
       =\{1\}\times\Omega_N-\{0\}\times\Omega_N
                                   -[0,1]\times\partial\Omega_N,
\]
holomorphic Stokes gives exactly
\[
 \int_{\Omega_N+i\eta v_\sigma}\omega_N
       =\int_{\Omega_N+b_\sigma(1)}\omega_N
                                      -\int_{\mathcal S_{\sigma,N}}\omega_N.
 \tag{23}
\]
This is a finite sum of ordinary polyhedral Stokes identities;
internal cell sides cancel with opposite orientations.
There is no appeal to a contour at infinity.

Combining (13), (18), and (23) gives the full original scalar:
\[
 \boxed{\displaystyle
 K_N=
 c_\epsilon\int_{\Omega_N+N\delta}\omega_N
 +\sum_{\sigma\ne\epsilon}
                  c_\sigma\int_{\Omega_N+iNv_\sigma}\omega_N
 +\int_{\Gamma_N^{\rm band}}\omega_N
 +\int_{\mathcal M_N}\omega_N
 -\sum_\sigma c_\sigma\int_{\mathcal S_{\sigma,N}}\omega_N .}
 \tag{24}
\]
Every term and every sign in (24) has been specified.
The band tori use the same polarized form (12); their
residues remain the original boundary-state summands.
No complementary real band has been set to zero.

All constructed bulk currents have polynomial geometric mass
in \(N\) for the fixed braid and chosen frame. The top sheets
have \(O(N^m)\) volume; their boundary prisms have
\(O(N^{m-1})\) unit facets and translation length \(O(N)\).
The initial mixed currents have \(O(N^{m-1})\) fixed-size
cells and bounded integer multiplicities. Every kernel
factor on the latter and on the translated prisms is bounded
independently of \(N\). These are geometric and kernel bounds,
not bounds for \(J_N\) or the full weighted periods.

## 6. The distinguished sheet and what its coefficient means

The preferred sheet contains \(Nx^*\), since
\[
                         Nx^*=Nx^0+N\delta,
 \tag{25}
\]
and \(\Omega_N\) contains a proportional neighborhood of \(Nx^0\).
After scaling by \(N\), it therefore contains a fixed real
neighborhood of the geometric point. All chord and factorial
imaginary parts there are nonzero. L's actual local expansion
and corrected geometric action apply to this same form.

For \(z=Nx\) on this neighborhood, the polarized kernel satisfies
\[
 K_{\epsilon_j}(Nx_j)
          =-2\pi i\,\epsilon_j+O(e^{-\gamma N}).
 \tag{26}
\]
Consequently its coefficient, including the rectangle orientation
and residue normalization, is
\[
 c_\epsilon(2\pi i)^{-m}
                 \prod_j(-2\pi i\epsilon_j)=1.
 \tag{27}
\]
Thus the preferred top has the literal nonzero local amplitude
of \(J_N(Nx)N^m\,dx\), multiplied by \(1+O(e^{-\gamma N})\).
Its coefficient in this explicit current decomposition is
exactly the recorded \(+1\), not an unknown local contour weight.

For a nonpreferred top the kernel bound is instead
\[
 \left|\prod_j K_{\epsilon_j}(x_j+iNv_{\sigma,j})\right|
 \le C\exp\!\left\{-2\pi N
                \sum_{\sigma_j\ne\epsilon_j}a_j\right\},
                  \qquad x\in\Omega_N.
 \tag{28}
\]
This follows from the elementary exponential formula for
cotangent. The character in (7) and the entire factorial
action remain outside this kernel estimate. Their growth
can outweigh (28). No source gap or alias suppression is
deduced from this penalty alone.

The principal critical family on the preferred top retains
the geometric \(r\)-centralizer null direction. A real sheet
through one of its points is not thereby a specified transverse
Gaussian cycle or a centralizer period. Other critical points,
equal-holonomy aliases, all facets and the band may compensate
its contribution. Formula (24) gives no noncancellation estimate
and no lower bound for \(K_N\).

## 7. Exact character differences and the remaining reduction

For the unpolarized cotangent form of L, an integer-character
step has the exact identity
\[
 (e^{-2\pi iz_j}-1)\pi\cot(\pi z_j)
                          =-i\pi(1+e^{-2\pi iz_j}).
 \tag{29}
\]
Iterating independent character differences cancels precisely
the selected coordinate lattice-pole families. This does
not cancel factorial divisors or source endpoints. Each
difference has zero period on each original supported torus,
not merely on their sum. It therefore supplies no finite
Fourier lower bound for the original scalar: all those
integer-character periods are the same \(K_N\).

The polarized replacements used in (12) are the corresponding
one-coordinate pole-free changes with fixed constants.
The substantive additional control in (24) is its verified
whole-source domain and its complete finite relative boundary:
the original boundary band, initial mixed facet currents,
translated staircase side prisms and the other top sheets.
There is no unidentified interpolation-divisor crossing
in their bulk construction, and no discarded infinity end.
What remains is to estimate these actual terms and resolve
the residual critical family; their existence and coefficients
are no longer hypothetical.

The older factorial-core contour compiler already has exact
cell telescoping and finite-facet rules on retained holomorphic
tubes. Those calculations are coverage, not a proof premise
here. The new ingredient is that the common nonreal framing
gives the required oblique holomorphic prisms for the full
literal braid bulk in arbitrary fixed diagrams, while the
entire complementary physical band remains in (24).
This does not evade the individual-evaluation homology
obstruction by claiming a low norm for the undecomposed
source. Its potentially large boundary terms are explicit.

## Complete proof-source pins

* A: notes/research_literal_crossing_slit_chart_amplitude.md,
  SHA256 c3682b0f84000aad4c2f53235b9c93bbd86283905a75d6f07ac03b1a3c00bc4a.
* L: notes/research_local_geometric_period_for_any_braid.md,
  SHA256 3ebc94ac5c71dfb38d627704c8a3e3227ff07a6293d39eb79d662b272124578e.

Both complete texts were freshly read nontruncated in this
author sequence. Their used implications are checked separately
from the explicit graph, source-domain, current and orientation
calculations above. Only written mathematics and text/hash
operations are used. Frozen and public files are unchanged.
