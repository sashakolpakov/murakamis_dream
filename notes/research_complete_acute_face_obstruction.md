# The complete source has no acute complex critical point

Private written deduction, 15 November 2026. This is a consequence of
the literal crossing phases, the original Morse bends and the two
faces fixed by the marked cut. No triangulation of the complement is
assumed, and no numerical calculation is used.

The acute domain constructed in the preceding note is nonempty for
alternating diagrams. Nevertheless its full action has no critical
point on any integral Fourier lift. The obstruction is already visible
in the imaginary equations with the clocks held fixed. It also makes
the proposed strict zonotope condition for imaginary coercivity
impossible for this complete source. Thus the earlier accretive Hessian and uniqueness statements
remain valid, but do not provide a domain containing the geometric
critical point.

## 1. The original variables and the face directions

Use the original fixed-cut Morse source of
[the acute-domain theorem](research_original_incidence_acute_tube.md).
There are \(c>0\) crossings, with local physical signs \(\sigma_j\).
The normalized incidences and the complete leading action are
\[
 n_j=(1-U_j-V_j,\ U_j-H_j+V_j,\ H_j-V_j,\ V_j),
 \tag{1}
\]
\[
 \mathscr S=-\sum_{j,a}\mathcal J(n_{ja})+i\pi\mathcal Q,
 \qquad
 \mathcal Q=\sum_j
   \{H_j+\sigma_jH_j(U_j+2J_j)-\sigma_jJ_j\}+B_{\rm bends}.
 \tag{2}
\]
Here \(\mathcal J'=\Log(2\sin\pi z)\) on
\(0<\Re z<1\). Every bend monomial and the original marked cut
are retained in \(B_{\rm bends}\). A different recorded left/right
root lift changes it by an even integral affine expression, whose
Fourier character will remain in the equations below.

The acute domain means
\[
                       0<\Re n_{ja}<1/2.              \tag{3}
\]
Its feasibility theorem implies that the chosen diagram alternates.
We may therefore assume alternation when considering a point of (3).

Ignore degree-two bends when counting the projection graph. It is
connected and four-valent, with \(c\) vertices, \(2c\) edges and
\(c+2\) faces. Expose the selected cut as a top cap, with adjacent
faces \(a,b\), and take \(a\) as the exterior face. The two faces
are distinct. Indeed a connected graph with all vertex degrees even
has no bridge: the sum of degrees in either component after cutting
a bridge would be odd. An edge of a connected plane graph has the
same face on both sides precisely when it is a bridge.

There are consequently exactly \(c\) other faces. Denote this set
by \(\mathcal F\). Give a real variation \(t_f\) to every face,
with \(t_a=t_b=0\). On a vertical physical strand put
\[
                    \delta A=t_{\rm left}-t_{\rm right}.
 \tag{4}
\]
These are actual homogeneous fixed-cut flow directions. They satisfy
the crossing conservation equations and the complementary bend
equations. Along a bent edge, the two geometric faces exchange their
left/right positions at the same time as the physical degree changes
to its complement. The directions in (4) therefore agree through
the whole Morse drawing. The marked degree is fixed because both
adjacent face variations vanish.

For integral \(t_f\), every physical degree variation and every
transfer variation is integral. Holding all clocks fixed gives an
integral tangent vector of the original source. Thus the restriction
of any original integral Fourier character to these directions has
the form \(2\pi i\sum_{f\in\mathcal F}k_f t_f\), with integral
\(k_f\). No assertion that arbitrary independent \(k_f\) occur is
needed for the obstruction. The face directions themselves are
independent: if all head variations vanish, adjacent face values
agree; connectedness of the dual graph and \(t_a=0\) make them all
zero. Even-level half-index offsets affect the affine physical
indices, not these integral homogeneous variations.

## 2. The crossing calculation in the actual frames

At one crossing call the four face variations
\(w,e,n,s\): left outer, right outer, input middle and output
middle, respectively. Repeated face labels are counted with their
multiplicity. In the local downward physical reading the variations
are
\[
\begin{array}{c|ccc}
 \sigma&\delta U&\delta V&\delta J\\ \hline
 +1&w+e-n-s&s-e&n-e\\
 -1&n+s-w-e&w-s&w-n.
\end{array}                                             \tag{5}
\]
For example, at a positive crossing the over-input degree has
variation \(w-n\), the under-input variation is \(n-e\), the
over-output variation is \(s-e\), and the under-output variation
is \(w-s\). These give the first row directly. At a negative
crossing the right input is over and the left output is over, giving
the second row. The signs are those of the physical matrices, not
an independently assigned orientation convention.

Keep \(\delta H=0\). From (2), the crossing phase differential is
\(\sigma H\delta U+\sigma(2H-1)\delta J\). Substitution in (5)
gives
\[
\begin{array}{c|l}
 +1&H w+(1-H)e-(1-H)n-Hs\\
 -1&(1-H)w+He-(1-H)n-Hs.
\end{array}                                             \tag{6}
\]
The incidence variation at fixed clock is
\(( -\delta I,\delta I,-\delta V,\delta V)\), where
\(I=U+V\). Put \(h=\Re H\). At an acute point \(0<h<1\).
The sum of the two upper-incidence weights
\(1/2-\Re n_0,1/2-\Re n_1\) is \(h\), and the sum of the
two lower weights is \(1-h\). Hence their weighted absolute
variation is
\[
\begin{array}{c|l}
 +1&h|w-n|+(1-h)|s-e|,\\
 -1&h|n-e|+(1-h)|w-s|.
\end{array}                                             \tag{7}
\]
The two terms are attached to the two over-arcs incident to this
crossing, one before and one after it. The weight of the over-input
arc is \(h\); that of the over-output arc is \(1-h\).

## 3. The bend contribution and its integer constant

The literal root cups and caps in left-to-right order are
\[
 p_{ij}=Nq^{-d^2+di}\mathbf1_{i+j=d},\qquad
 \ell_{ij}=N^{-1}q^{di}\mathbf1_{i+j=d},\qquad d=N-1.
 \tag{8}
\]
For the first head of a bend, (4) is
\(\delta A=t_o-t_z\), where \(o,z\) are its outside and inside
faces. Its variable-dependent leading phase therefore contributes
\(t_o-t_z\) in the units of \(\mathcal Q\). Let \(T_f\) count
outside bend occurrences minus inside bend occurrences. At this
stage include the ordinary cap at the selected mark.

Let \(M_f\) count the input and output middle-face occurrences at
crossing disks. The actual Morse winding identity is
\[
                         T_f=M_f-2\qquad(f\ne a).      \tag{9}
\]
Here is the sign check. Traverse a bounded face with the face on its
left, rounding repeated passages if necessary. In a crossing disk,
the input and output middle passages each reverse the vertical
tangent and contribute \(+\pi\); an outer passage continues the
vertical tangent and contributes zero. An inside bend contributes
\(+\pi\) and an outside bend \(-\pi\). Thus the total boundary
turn is \(\pi(M_f-T_f)\). Its winding is \(2\pi\), proving
(9). This is also the literal winding computation in Section 6 of
the original general Morse compiler. It concerns the given diagram
and its ordered crossing frames.

The marked cap does not change (9) for the free directions. Its
supported coefficient is \(q^{dj}/N^2\), whereas the ordinary cap
has \(q^{di}/N\). Their ratio contributes only the two adjacent
face directions \(a,b\), both fixed in (4). Equivalently the exact
fixed-cut formula has a coefficient depending on the fixed degree
alone. The left/right root comparisons in the actual bends append
only even integral face covectors. These can be combined with the
original integral Fourier character; they are not discarded as
unrecorded changes of lift.

Equation (9) says that, on the free faces, the bend differential
adds one copy of \(n+s\) per crossing to (6), then subtracts
\(2\sum_f t_f\). The resulting per-crossing coefficients are
\[
\begin{array}{c|l}
 +1&H(w+n)+(1-H)(e+s),\\
 -1&(1-H)(w+s)+H(e+n).
\end{array}                                             \tag{10}
\]
Their real parts are precisely the endpoint degrees of the weighted
edges in (7).

## 4. A strict angle budget that no integer lift satisfies

Form a graph \(\mathcal G\) whose vertices are the faces of the
projection. At each crossing insert the two dual edges in (7), with
weights \(h_j\) and \(1-h_j\). Since the diagram alternates,
every projection arc has one over endpoint and one under endpoint.
Thus each projection arc appears exactly once in this list.
The graph is the whole planar dual, with its edge multiplicities
retained. All weights are positive, and
\[
                       \sum_{e\in E(\mathcal G)}w_e=c. \tag{11}
\]
Write \(D_f\) for its weighted degree at face \(f\). Combining
(6)--(10), the imaginary derivative of the complete quadratic phase
and any Fourier lift, divided by \(\pi\), has coefficient
\[
                       D_f-2\ell_f,
                      \qquad \ell_f\in\mathbb Z       \tag{12}
\]
on each free face. The integer is \(1+k_f\), up to the retained
even integral bend character. This is an identity for the original
phase, not a choice of phase made to fit an angle structure.

Suppose first that \(z\) were an acute complex critical point.
For \(0<a<1/2\),
\[
 \arg(2\sin\pi(a+ib))
       =\arctan\bigl(\cot(\pi a)\tanh(\pi b)\bigr),
 \qquad
 |\arg(2\sin\pi(a+ib))|<\pi(1/2-a).                  \tag{13}
\]
The imaginary part of its stationary equation in the face direction
\(t\), using (7) and (12), consequently gives
\[
 \left|\sum_{f\in\mathcal F}(D_f-2\ell_f)t_f\right|
    <\sum_{e=fg}w_e|t_f-t_g|
                       \qquad(t\ne0, t_a=t_b=0).      \tag{14}
\]
The inequality is strict because (13) is strict and the connected
dual graph detects every nonzero face direction.

For precision, the zonotope condition considered here is as follows.
Let \(L\) be the real incidence matrix in independent fixed-cut
coordinates, let \(x\) be the real part of a point of (3), and put
\[
 \mathcal Z_x=L^{\mathsf T}
       \prod_e[-(1/2-\Re n_e),\,1/2-\Re n_e].
\]
The proposed criterion requires the real phase force
\(\Re\nabla\mathcal Q-2k\) to lie in the strict interior of
\(\mathcal Z_x\). Its support function on the fixed-clock face
direction is exactly (7). Strict interior membership therefore
requires (14). This second conclusion is an elementary assertion
about the displayed zonotope; it does not assume a critical point
or an analytic coercivity theorem.

Apply (14) to a singleton free face. If \(w(E_f)\) denotes the
weight of any loop edges at that face, its right side is
\(D_f-2w(E_f)\). The upper half of the strict inequality forces
\[
                         \ell_f>w(E_f)\ge0,
                     \quad\text{hence}\quad \ell_f\ge1. 
 \tag{15}
\]
Loop edges are unnecessary in the present dual graph, but allowing
them makes the argument independent of that simplification. Since
there are \(c\) free faces,
\[
                            \sum_{f\in\mathcal F}\ell_f\ge c.
 \tag{16}
\]

Now take \(t_f=1\) on every free face and zero on \(a,b\). Let
\(E_{\mathcal F}\) be the edges internal to the free faces and
\(\partial\mathcal F\) those joining them to \(a\) or \(b\).
The sum of their weighted degrees is
\(2w(E_{\mathcal F})+w(\partial\mathcal F)\).
The other half of (14) yields
\[
 \sum_{f\in\mathcal F}\ell_f
     <w(E_{\mathcal F})+w(\partial\mathcal F)
     \le \sum_{e\in E(\mathcal G)}w_e=c.               \tag{17}
\]
This contradicts (16). In fact the last inequality omits the
positive-weight edge containing the marked cut, whose two faces
are \(a,b\).

We have proved the following statement.

**Theorem.** For every nonempty knot diagram in the original Morse
source, every compatible fixed cut, and every integral Fourier lift,
the complete action has no complex critical point with all crossing
incidences in \(0<\Re n_e<1/2\). At every real part in that domain,
the imaginary-coercivity zonotope fails strict interior membership
for every such lift.

For a nonalternating diagram the acute domain is already empty.
For an alternating diagram the contradiction is (16)--(17).
The argument also allows a fixed complex cut: the face variations
still vanish on its adjacent faces, and (6)--(12) involve only the
real clock values \(h_j=\Re H_j\).

This excludes the proposed complete-source acute optimization route
before any question about the original cycle's intersection number.
It does not exclude complex saddles in other incidence chambers,
boundary critical points, or critical points of an exactly reduced
source after justified finite eliminations. It does not disprove any
volume conjecture. The proof never identifies the weighted dual graph
with an ideal triangulation of the knot complement.

## 5. Direct sources and scope of the new deduction

The written source implications and versions used here are:

* `research_original_incidence_acute_tube.md`,
  `17892b7654e7f7668be2fde7743d5adab0bf8e9dc813c29f8114023e740e78f6`:
  Sections 1--4 give the original fixed-cut Morse action, independent
  transfer/clock coordinates, alternating feasibility, and the
  specified strip logarithm. The present theorem strengthens its
  conditional critical-point conclusions; its Hessian proof is not
  used to infer existence.
* `research_joint_clock_phase_equations.md`,
  `71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867`:
  Sections 2--5 give the physical over/under crossing convention,
  exact clock expansion and full quadratic crossing action in (2).
* `research_arbitrary_main_edge_mark_transport.md`,
  `7a7c9efdca1e9f7907dc5baf5dfe8ba12e2345ee5f2df2ed94240e95ee69112a`:
  Sections 5--7 give the literal ordered bends, the marked-cap
  correction, the winding identity and the primitive face directions,
  including both parity offsets.
* `research_matched_sphere_morse_source.md`,
  `8fdfde4a0d83220f3709048f00cd9373cfbc9d14b05943e9f16f58ab50777f4f`:
  Sections 4--5 explain why these are the original frames and
  winding calculation on a newly drawn Morse network. No geometric
  certificate from that note is assumed.

The new content is the local table (5)--(10) and the resulting
integer face-budget contradiction for the complete original action.
