# Physical facets, momentum seams, and the geometric framing boundary

Private written proof, 18 November 2026.

The explicit braid contour decomposition has several different kinds of
boundary. On a holomorphic affine stratum, constrained stationarity is
the original crossing correspondence with specified diagonal momentum
seams. It is not automatically the original knot representation scheme.
For limits that do retain the full geometric correspondence, the physical
facets meet a fixed complex-binomial framing line at an explicit finite
algebraic set. These points can be exceptional decorations of the same
geometric holonomy. No representation-volume gap separates them from it.

The statements below retain the original polynomial wall equations and
their multiplicities. They make no estimate for the boundary integrals,
and do not replace a singular endpoint layer by a regular critical point.
The complete directs are M (marked holonomy), F (common slit frame),
C (oblique currents), and H (the incidence/gradient adapter).

## 1. The source facets and the different boundary currents

Use C's primitive lattice coordinates: the cut occupation and the \(c\)
crossing transfers. Every wire occupation is an integer linear form
\(\ell_e\) in these \(m=c+1\) coordinates. The original support is
\[
 0\leq \ell_e(k)\leq N-1,\qquad 0\leq n_j(k)\leq N-1.
 \tag{1}
\]
Some inequalities can be redundant. In normalized positions \(k/N\),
the possible physical supporting hyperplanes tend to
\(\ell=0\) and \(\ell=1\), for a wire or transfer form \(\ell\).
Their principal multiplicative clock is consequently one.
This is a limiting statement: the exact upper clock at \(N-1\) is
\(Q^{-1}\), not one.

C retains the full fixed-width band of actual states, all initial mixed
rectangle currents, every translated staircase side prism, and all top
sheets. These remain exactly the currents in its equation (24).
In particular its translated side prisms have nonreal factorial forms.
They are not themselves clock-one physical facets. The microscopic
staircase cells also retain their actual coordinate orientations; they
are not silently replaced by a smooth limiting polytope face.

We first give an algebraic test on any holomorphic affine stratum of
the actual phase. Applying that test to a limiting physical face requires
its own holomorphic chart. The singular clock-one endpoint layer is
not covered by such an assumption merely because the finite array exists.

## 2. Exact constrained stationarity produces momentum seams

Let \(L\) be the incoming-minus-outgoing incidence matrix on the \(2c\)
wire arcs, and let \(W=\ker L\). Its chord coordinates have dimension
\(c+1\). Keep the actual signed crossing primitives, pivots, framing,
complex-binomial cut action \(g_\theta\), and the selected integer
Fourier correction. Denote this corrected phase by \(\Phi_\theta\).
Work only on a holomorphic logarithmic chart of the original canonical
graphs, with every momentum and required denominator a unit.

Let an affine stratum be given in \(W\) by independent equations
\[
 a_\nu(\zeta)=b_\nu,\qquad 1\leq \nu\leq d.
 \tag{2}
\]
Choose fixed linear extensions of the covectors \(a_\nu\) to the wire
space. No independence in that larger space is required. Elementary
linear duality gives the exact constrained critical equations
\[
 d(\Phi_\theta|_{\text{stratum}})=0
 \quad\Longleftrightarrow\quad
 d\Phi_\theta=\sum_{\nu=1}^d t_\nu a_\nu\quad\hbox{in }W^*.
 \tag{3}
\]
The multipliers \(t_\nu\) are unique. Fixed linear splittings prove this
also over local Artin algebras.

Here is its actual source meaning. Choose local half-edge log momenta
\(\pi=\log p\) from M's signed generating relations. Absorb the retained
integer pivotal turns and the complete Fourier covector as in H.
For an arc \(e\), set
\[
 R_e=\pi_{\mathrm{out},e}-\pi_{\mathrm{in},e}
                     +g_\theta'(u)\,1_{e=\mathrm{cut}}.
 \tag{4}
\]
Changing the common momentum at crossing \(v\) by a log constant
\(\lambda_v\) changes \(R\) by \(-L^t\lambda\).
The exact sequence
\[
 0\longrightarrow\mathbb C\longrightarrow\mathbb C^c
 \xrightarrow{L^t}\mathbb C^{2c}\longrightarrow W^*
 \longrightarrow0
 \tag{5}
\]
therefore turns (3), after vertex rescalings, into the individual rows
\[
 R_e=\sum_\nu t_\nu a_{\nu,e}.
 \tag{6}
\]
This is an equivalence of local schemes on the stated unit chart.
Only the one global common momentum remains free. No positive gluing
certificate is needed for this linear adapter.

Write \(d_e=\exp(\sum_\nu t_\nu a_{\nu,e})\). On each noncut arc,
(6) says \(p_{\mathrm{out}}=d_e p_{\mathrm{in}}\).
At the cut it says instead
\[
 \frac{p_{\mathrm{out}}}{p_{\mathrm{in}}}
                       =d_e\,e^{-g_\theta'(u)}.
 \tag{7}
\]
The actual physical coordinates in M are
\[
 K=x/A,\qquad e=(1-x^2/A)p/x,\qquad f=(1-A)/p.
 \tag{8}
\]
Thus the noncut seam preserves \(K\) and sends
\((e,f)\) to \((d_e e,d_e^{-1}f)\). On its physical matrix
\[
 G=\begin{pmatrix}K&e\\Kf&K^{-1}+ef\end{pmatrix}
 \tag{9}
\]
this is exactly conjugation by \(\operatorname{diag}(d_e,1)\).
These are explicit classical seam coupons in the same canonical
network, not new finite quantum identities or discarded source currents.

For a wire constraint \(a_\nu=\zeta_e\), only that wire has its direct
seam. For a positive transfer use
\(a_\nu=\zeta_{\mathrm{out,left}}-\zeta_{\mathrm{in,right}}\);
the two seam factors are opposite. For a negative transfer reverse
that difference. Changing the chosen extension by an incidence row
merely changes the vertex gauges in (5).

Only when these seam factors are removed, or their compatibility with
the original closure is independently proved, may one apply the
original knot representation comparison. Even the soft-cut deduction
using the conserved total \(K,E,F\) requires the ordinary noncut
matching rows; it cannot be applied after ignoring (6).
Locally near \(t_\nu=0\), all seam factors equal to one modulo vertex
gauge force all \(t_\nu=0\), by (5) and independence in (2).
Away from that neighborhood the prescribed integer log sheets remain.
There is no claim that every constrained face critical point represents
either a geometric or a nongeometric representation of the knot.

## 3. A finite boundary set on the fixed geometric framing line

Fix the complete geometric representation and the selected flag.
Normalize its selected meridian to \(J_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}\)
by a fixed classical frame, as in H; this is not a quantum change of
the source. Use F's regular complex-binomial frame, with its parameter \(\theta\)
near \(1/2\). Set
\[
 s=e^{-2\pi i\theta}-1\ne0,\qquad
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix}.
 \tag{10}
\]
The cut clock is fixed to \(e^{2\pi i\theta}\), and \(r\) varies.
Let \(r_0\) be the chosen regular common-slit frame. In particular
all prefix minors there are units, and every required wire and
transfer clock differs from one.

For every stage prefix matrix \(P=\begin{pmatrix}a&b\\c&d\end{pmatrix}\)
in the original signed braid, define the polynomial
\[
 Q_P(r)=s(F(r,s)^{-1}PF(r,s))_{11}
       =c r(1-r)+(a-d)rs+ds+bs^2 .
 \tag{11}
\]
Its degree is at most two. For \(P=\pm I\), it is the nonzero
constant \(\pm s\). The formula follows by multiplying the first
row \((1,(1-r)/s)\) of \(F^{-1}\) by \(P(r,s)^t\).
No change of the actual matrix products or central lifts is made.

Let \(P_j=H_j\cdots H_1\) at a braid stage, with \(H_j\) minus
the actual meridian. M's Gauss inverse gives at complete color
\[
 A_j=-\frac{Q_{P_{j-1}}}{Q_{P_j}}.
 \tag{12}
\]
For an adjacent crossing, write its four preserved/replaced prefixes
as \(P_0,P_1,P_2,P'_1\), as in F. Its transfer is
\[
 C=\frac{Q_{P_0}Q_{P_2}}{Q_{P_1}Q_{P'_1}}
 \quad\hbox{or its reciprocal, for the two signs.}
 \tag{13}
\]
Consequently the following list contains every possible principal
physical-facet limit on this framing line, including chart escapes:
\[
 \begin{aligned}
 &Q_P(r)=0 &&\text{for every retained stage prefix},\\
 &Q_{P_j}(r)+Q_{P_{j-1}}(r)=0 &&\text{for every wire},\\
 &Q_{P_0}(r)Q_{P_2}(r)-Q_{P_1}(r)Q_{P'_1}(r)=0
                                      &&\text{for every crossing},\\
 &r=\infty.&
 \end{aligned}
 \tag{14}
\]
All displayed polynomials are nonzero polynomials: evaluating at
\(r_0\) proves this directly from regularity and the off-unit clocks.
Their degrees are at most \(2,2,4\), respectively.
If \(p,e,c\) count the listed prefix, wire and crossing occurrences,
the number of candidate points on \(\mathbb P^1_r\) is therefore at
most \(2p+2e+4c+1\). Repetitions and extraneous candidates are allowed.
This bound depends only on the finite list, not on the root level.

On the chart where all retained prefix minors are units, the actual
wire wall ideal \((A_j-1)\) is exactly the second polynomial ideal
in (14), up to a unit. The transfer ideal \((C-1)\) is exactly the
third one, up to a unit, for either sign. No common factors are
cancelled to reduce their orders. At a prefix zero, (14) is only
a boundary candidate; the rational Gauss inverse is not asserted
to remain a regular coordinate chart there.

The classification is necessary, not sufficient for a physical face.
A clock equal to one can have different retained logarithm lifts.
Only a lift tending to \(0\) or \(2\pi i\) is the corresponding
normalized physical endpoint. If no candidate in (14) is approached,
the framing line stays in an ordinary regular source chart and cannot
approach a principal physical wire or transfer face.

## 4. The geometric wire walls are exceptional decorations

At complete color \(x=-1\), the exact classical Casimir identity is
\[
                     ef=\frac{(A-1)^2}{A}.
 \tag{15}
\]
On a Gauss-regular full representation limit with \(A=1\), the
noncentral meridian therefore has exactly one of \(e,f\) equal to
zero. Both cannot vanish, since then \(G=-I\) and the actual
meridian \(-G\) is central. The holonomy itself need not degenerate.

The prefix numerator gives a more explicit factorization. Write
\(\alpha_r=(1,(1-r)/s)\) and \(v_r=(r,s)^t\), so
\(\alpha_r v_r=1\). The complete noncentral matrix \(H_j\) has
trace \(-2\), and \(H_j+I\) is nonzero rank one with square zero.
Choose constant nonzero vectors \(a_j,b_j\) such that
\(H_j+I=a_jb_j^t\), \(b_j^ta_j=0\). Then
\[
 Q_{P_j}+Q_{P_{j-1}}
       =s(\alpha_r a_j)(b_j^tP_{j-1}v_r).
 \tag{16}
\]
These are the two flag-alignment factors. They cannot both vanish
where \(Q_{P_{j-1}}\ne0\): the second would imply
\(P_{j-1}v_r\in\ker b_j^t=\mathbb C a_j\), and the first
would then force \(\alpha_rP_{j-1}v_r=0\).
Thus this factorization introduces no claim that a noncentral
meridian has become central.

In contrast, if the factorial momentum in (8) has a finite nonzero
limit while \(A\to1\), both \(e\) and \(f\) tend to zero.
A noncentral geometric wire limit must therefore leave that
momentum chart: \(p\) tends to zero or infinity with the appropriate
nonzero remaining physical entry. The full Artin comparison on unit
log charts is not continued through this singularity by assertion.

For the two signed full crossing maps, M gives
\[
 C_+=(1-e_1f_2)^{-1},\qquad
 C_-=1-(K_1/K_2)e_2f_1.
 \tag{17}
\]
On their regular Gauss charts, \(C=1\) forces one of the displayed
entries to vanish. By (15), at least one adjacent input wire then
has \(A=1\). Hence a full geometric transfer-facet limit is not an
independent regular interior wall: it also reaches a wire wall.
On every unit chart in Section 2 the local crossing equations,
including (17), still hold; it is the global matching that carries
seams. A constrained singular transfer-face saddle is a different
matter: it need not admit a finite Gauss-regular lift at all.
Neither a restriction of the endpoint action nor tangential
stationarity proves such a lift through its nonunit log divisor.

Multiplicities matter. Where \(f\) is a unit, (15) makes \(e\)
vanish to twice the order of \(A-1\), and conversely where \(e\)
is a unit. Replacing the physical wall by its set-theoretic
description \(e=0\) or \(f=0\) loses this contact information.
Before complete-color specialization the same classical identity is
\[
                    ef=\frac{(A-1)(A-M^2)}{MA},
                    \qquad x=-M.
 \tag{18}
\]
Thus the double contact is a collision of two marked divisors.
Equations (15)--(18) are classical statements; finite Weyl shifts,
the upper clock \(Q^{-1}\), and all actual quantum/meridian normals
remain in the original source and current formulas.

## 5. What this reduces, and what remains

For fixed geometric holonomy and the chosen soft cut, the possible
physical decoration boundary is the finite algebraic set (14), with
the original polynomial multiplicities and log lifts. It can be
used as a list of boundary locations for a future relative
\(r\)-period comparison. It is not a finite-exception theorem for
knots or filling assignments.

These geometric limits are changes of decoration of the same
representation. They cannot be called lower-volume representations
merely because an occupation reaches its endpoint. Other constrained
critical points on the unit charts carry the explicitly retained seams
(6); until those seams are resolved, they are not automatically eligible
for a knot representation-volume theorem at all. Only an honest
nongeometric knot representation, with the actual peripheral data,
can be placed in the scope of such a separate theorem.
Singular endpoint critical layers without such a chart still require
their own source-compatible lift.

None of this estimates a mixed rectangle, staircase prism, physical
band or singular factorial layer. C's complete finite identity is
unchanged. No endpoint is deleted, no quantum normal is replaced by
a classical reduced divisor, and no critical-value assertion is
turned into an integral bound or scalar lower bound.

## Complete proof-source pins

* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* F: notes/research_literal_factorial_common_slit_frame.md, SHA256
  9764a2b77469c7fad402b9b8e609b304a79083bde18fb139031c06fd93650ca8.
* C: notes/research_actual_oblique_geometric_contour_decomposition.md,
  SHA256 9180de472bafb38c479d3e1aafac6c75c388d668371892f54219de658728034c.
* H: notes/research_positive_certificate_braid_morse_bott.md, SHA256
  6ef5423e542170ffe3b5464753613ae042341d9c2ee20a2fa94fd0d828738410.

All four complete directs were read nontruncated in the current
author sequence, their used implications checked, and unchanged
whole reads retained where applicable. Only written mathematics
and source/text operations were used. Frozen and public files
are unchanged.
