# A common slit chart for the actual factorial crossing source

Private written proof, 18 November 2026.

Every finite collection of literal crossing factorial clocks can be
put off the unit circle by an arbitrarily small complex change of a
regular selected-flag frame. No factor clock in the required list is
constant on the full framing orbit. This follows from an irreducible
prefix-minor calculation, and does not require faithfulness of the
representation. Integral wire-logarithm repair then puts all the
normalized factorial lengths in one common slit domain.

For complete geometric holonomy, the change can be made arbitrarily
close to the regular midpoint frame. An exact complex-binomial cut
selects its cut position in the principal stationary scheme, while
retaining the original unmarked scalar. Its exponential total-variation
cost can be made arbitrarily small, and is recorded rather than omitted.
This is a chart and source-presentation theorem. It does not deform
the finite state cycle to this point or estimate a full coherent kernel.

## 1. Actual clocks and the statement

Keep a fixed finite braid whose closure is one knot, its actual signed
crossings, pivotal closures, framing and factorial basis. Use the
classical correspondence of M and the weighted principal source of S.
At a positive crossing, with input clocks \(A,B\) and transfer \(C\),
the output clocks are \(BC,A/C\). At a negative crossing they are
\(B/C,AC\). The complete color is \(M=1\), with classical \(x=-1\).

The five leading factorial lengths at a positive crossing are
\[
 (b+n,\ a;\ b,\ n,\ a-n)/N,
 \tag{1}
\]
and at a negative crossing they are
\[
 (a+n,\ b;\ a,\ n,\ b-n)/N.
 \tag{2}
\]
The semicolon separates numerator from denominator factors. Their
exponentials are respectively
\[
 (BC,A;\ B,C,A/C),\qquad (AC,B;\ A,C,B/C).
 \tag{3}
\]
Thus each is a wire occupation clock or a transfer clock. These are
the actual five-factor lists, not independent octahedral coordinates.
For example M's positive finite product is
\[
 \frac{F_{b+n}}{F_bF_n}(Qx^2/A;Q)_n.
\]
At the physical color \(Qx^2=1\), reversing its last product gives
\[
 (Q^{-a};Q)_n
 =(-1)^nQ^{-an+n(n-1)/2}\frac{F_a}{F_{a-n}},
 \tag{4}
\]
which proves (1) without deleting its monomial factor. The negative
formula is the same reversal with \(a,b\) interchanged. All Cartan,
sign and pivotal factors remain. At nearby color, write
\(\alpha=-2\log M/h\), \(h=\log Q\); the reversed endpoints are
\(a+\alpha,a-n+\alpha\), or \(b+\alpha,b-n+\alpha\).
Their leading clocks are \(A/M^2,A/(CM^2)\), or
\(B/M^2,B/(CM^2)\). Fixed Weyl offsets remain in the finite factors.

Let
\[
 \mathcal D=\mathbb C\setminus
                   \bigl((-\infty,0]\cup[1,\infty)\bigr).
 \tag{5}
\]
Fix any selected-flag representation with noncentral strand meridians,
and any nonempty regular chart of its finite actual braid correspondence.
The theorem is that, in every complex neighborhood in that chart,
there is a frame and a compatible set of wire logarithms for which
every length in (1)--(2) lies in \(\mathcal D\). Each length in fact
has nonzero imaginary part. The lengths lie in compact subsets of
\(\mathcal D\) on a sufficiently small common neighborhood.

For a complete hyperbolic knot, G supplies the required regular
midpoint chart. In that case the cut logarithm can be retained near
\(\pi i\), and the source cost in Section 5 can be made smaller than
\(\exp(\varepsilon N)\) for every prescribed \(\varepsilon>0\).
The chart theorem for noncentral representations below uses no
faithfulness or cusp-lattice assumption; G is used only to start
arbitrarily close to that particular geometric midpoint.

## 2. Every nonscalar prefix has an irreducible minor

Normalize the selected flag to the vector \(w=(1,0)^t\). Write
\[
 \alpha_t=(1,t),\qquad v_{t,s}=(1-ts,s)^t,\qquad
 F(t,s)=(v_{t,s},w-v_{t,s}),\qquad s\ne0.
 \tag{6}
\]
Then \(\alpha_t(v_{t,s})=1\), and \(\alpha_t\) is the first row
of \(F^{-1}\). These are the original framing coordinates
\(F(r,s)\) with \(r=1-ts\). In particular this is the full
two-dimensional selected-flag frame chart, not a fixed-\(s\) slice.

For a determinant-one matrix
\(P=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), put
\[
 w_P(t,s)=\alpha_tPv_{t,s}
 =a+ct+s\bigl[b+(d-a)t-ct^2\bigr].
 \tag{7}
\]
The map \(P\mapsto w_P\) is linear and injective: its coefficients
recover \(a,c,b,d-a\).

If \(P\) is nonscalar, \(w_P\) is an irreducible nonconstant
polynomial in \(\mathbb C[t,s]\). Indeed set
\(A(t)=a+ct\), \(B(t)=b+(d-a)t-ct^2\). If \(c\ne0\),
\[
                         B(-a/c)=-1/c,
 \tag{8}
\]
by \(ad-bc=1\). Thus \(A,B\) are relatively prime. If \(c=0\),
then \(a\ne0\), so \(A\) is a unit, and \(B\) can vanish
identically only when \(P\) is scalar. In both cases the primitive
polynomial \(A+sB\) has degree one in \(s\) over \(\mathbb C(t)\)
and is irreducible there; clearing polynomial contents proves
irreducibility over \(\mathbb C[t,s]\).
For scalar \(P=\pm I\), instead \(w_P=\pm1\).
Finally,
\[
                 w_P=\lambda w_Q
       \quad\Longrightarrow\quad P=\lambda Q,\quad\lambda=\pm1
 \tag{9}
\]
for determinant-one matrices. Hence distinct projective nonscalar
matrices give nonassociate irreducible prefix polynomials.

These polynomial statements are made before restricting to \(s\ne0\)
or to the regular braid chart. An identity on any of those nonempty
complex opens would be the same rational-function identity, so
localizing the chart does not invalidate the argument.

## 3. No required occupation or transfer clock is constant

At any braid stage let \(H_1,\ldots,H_b\) be M's unframed strand
matrices, and \(P_j=H_j\cdots H_1\), \(P_0=I\).
They are determinant-one matrices; \(H_j\) is minus the corresponding
actual meridian and is noncentral. M's exact Gauss inverse gives
\[
 K_j=\frac{w_{P_j}}{w_{P_{j-1}}},\qquad
 A_j=x\,\frac{w_{P_{j-1}}}{w_{P_j}}.
 \tag{10}
\]
If \(A_j\) were constant, injectivity in (9) would give
\(P_j=\pm P_{j-1}\), and therefore \(H_j=\pm I\), a contradiction.
This includes input and output wire clocks at every stage.

Consider an adjacent crossing at positions \(j,j+1\), and abbreviate
the four prefix matrices by \(P_0,P_1,P_2,P'_1\). Here \(P_0\)
means the prefix immediately before these positions, not necessarily
the identity. The prefix \(P_2\) is preserved by M's actual
Hurwitz correspondence. The positive transfer formula is
\[
 C=\frac{w_{P_0}w_{P_2}}{w_{P_1}w_{P'_1}},
 \tag{11}
\]
and for the inverse crossing it is the reciprocal of (11).
For example \(K'_j=K_{j+1}/C\) in the positive map and
\(K'_j=K_{j+1}C\) in the inverse map, which proves both formulas
directly from (10).

Suppose (11) were a nonzero constant. If \(P_1\) is nonscalar,
its irreducible polynomial \(w_{P_1}\) must divide
\(w_{P_0}w_{P_2}\). Equations (7)--(9) then force
\(P_1=\pm P_0\) or \(P_1=\pm P_2\). Both are impossible:
the intervening strand matrix is a noncentral meridian.
If \(P_1\) is scalar, both \(P_0\) and \(P_2\) are nonscalar
for the same reason. The left side of the cleared identity
has two irreducible factors, counted with multiplicity, whereas
the right side has at most one. This is again impossible.
Thus every transfer clock is nonconstant.

It follows that every function in (3) is nonconstant on the
full selected-flag frame orbit. Multiplying a function by a fixed
nonzero color constant or taking its inverse preserves this conclusion.
Consequently there are no identically unit-modulus functions in
the required factor-clock list. This assertion is about these
actual clocks; it does not assert multiplicative independence
of them or of arbitrary monomials in wire clocks.

On a sufficiently small connected complex neighborhood in the regular
chart all these finitely many clocks are holomorphic and nonzero.
For a nonconstant such function the set \(|C|=1\) has empty interior:
otherwise restriction to complex lines and the one-variable maximum
principle would make it constant on an open set, hence everywhere.
It is closed in the neighborhood. The complement of the finite
union of these sets is therefore open and dense. Choose a frame
there. This proves simultaneous off-unit modulus, arbitrarily close
to any initially supplied regular frame.

## 4. Exact wire-logarithm compatibility

There is no assumption that independently chosen logarithms already
obey additive state conservation. Here is an integral repair.
View the oriented knot diagram as the directed crossing graph:
edges are wire arcs and each crossing has two incoming and two
outgoing arcs. Let \(L\) be its integer incidence matrix, with
incoming coefficient \(+1\) and outgoing coefficient \(-1\).
Its multiplicative conservation law is the actual one
\(A_aA_b=A_cA_d\).

Choose any logarithms \(\zeta_e\) of the wire clocks. Then
\[
                    L\zeta=2\pi i\,k,\qquad k\in\mathbb Z^V,
                    \qquad \sum_v k_v=0.
 \tag{12}
\]
The graph is connected because the closure is one knot. Its incidence
matrix has integer image exactly the vectors of total sum zero.
For a direct proof, choose a spanning tree and remove its leaves
successively. At a leaf prescribe the unique incident tree-edge
integer to cancel the current integer at that leaf, then transfer
the remaining integer to its neighbor. The last vertex has integer
zero by the total-sum condition. This constructs \(m\in\mathbb Z^E\)
with \(Lm=-k\). Hence
\[
                \widetilde\zeta=\zeta+2\pi i\,m,\qquad
                L\widetilde\zeta=0
 \tag{13}
\]
without changing any multiplicative clock.

The repair can preserve the chosen cut logarithm. The oriented
one-component knot traverses the crossing graph as an Euler circuit,
so the cut edge is not an undirected bridge. Choose the spanning
tree without that edge. The same leaf elimination then has
\(m_{\rm cut}=0\). Loops of the graph cause no difficulty: their
incidence columns are zero, and they are not used in the tree.

Define a positive transfer logarithm by
\(\nu=\widetilde\zeta_c-\widetilde\zeta_b\), so conservation gives
also \(\nu=\widetilde\zeta_a-\widetilde\zeta_d\).
For a negative crossing use
\(\nu=\widetilde\zeta_b-\widetilde\zeta_c
     =\widetilde\zeta_d-\widetilde\zeta_a\).
These are exactly the additive relations behind (1)--(2), and
their exponentials are the prescribed transfers. Every normalized
factor length is now its appropriate logarithm divided by \(2\pi i\).
For every such clock \(Z\),
\[
 \Im\left(\frac{\log Z}{2\pi i}\right)
                         =-\frac{\log|Z|}{2\pi}\ne0.
 \tag{14}
\]
This is independent of the integer logarithm lift. All required
lengths therefore belong to \(\mathcal D\) simultaneously, with
the exact additive conservation and transfer relations retained.
Finite integer shifts of the lifts need not be individually small.

At the chosen point there are finitely many lengths. Shrinking
the common neighborhood keeps each in a compact subset of
\(\mathcal D\). All fixed \(O(N^{-1})\) Weyl offsets remain in
slightly larger compact subsets for sufficiently large \(N\).
Nearby color endpoints from Section 1 are included by continuity.
This is local uniformity for a fixed source/frame, not a denominator
bound uniform over a degenerating family of diagrams.

## 5. Exact complex-binomial selection and its recorded cost

Put \(d=N-1\), \(c_0=2\pi i\), and set
\(\theta=\widetilde\zeta_{\rm cut}/c_0\).
Since the cut clock is off-unit, \(\Im\theta\ne0\), in particular
\(\theta\ne0,1\). Use the literal diagonal probe
\[
 P_{N,\theta}=\sum_{a=0}^{d}
       \binom da\theta^a(1-\theta)^{d-a}T_a.
 \tag{15}
\]
The binomial theorem gives \(\operatorname{Tr}P_{N,\theta}=1\)
for every complex \(\theta\). The actual scalar endomorphism
identity in S therefore gives
\[
                  \operatorname{Tr}(P_{N,\theta}C_N)=F_N
 \tag{16}
\]
with every original crossing, pivot, framing and support wall.
For a marked cut endomorphism \(C\), retain instead the exact
current
\[
 \operatorname{Tr}((P_{N,\theta}-T_0)C)
       =\operatorname{Tr}(B_{N,\theta}[C,\mathcal E]),\qquad
 B_{N,\theta}=-\sum_{r<d}
   \frac{\sum_{a>r}\binom da\theta^a(1-\theta)^{d-a}}
        {M Q^{-r-1}-M^{-1}}E_{r+1,r}.
 \tag{17}
\]
Direct multiplication telescopes the commutator to
\(P_{N,\theta}-T_0\). Thus no marked-source equality is inferred
from (16).

For \(u=ha\) the exact consecutive weight ratio is
\[
 \frac{\theta}{1-\theta}\frac{c_0-h-u}{u+h}.
 \tag{18}
\]
With the logarithms continued consistently near the selected
\(\theta\), the principal normalized boundary action is
\[
 g_\theta(u)=c_0\left[
  -z\log z-(1-z)\log(1-z)
       +z\log\theta+(1-z)\log(1-\theta)\right],
 \qquad z=u/c_0.
 \tag{19}
\]
It is the action in S plus the exact linear logarithm of the
change of binomial weights. On these matching sheets
\[
 g_\theta(c_0\theta)=g_\theta'(c_0\theta)=0,\qquad
 g_\theta''(c_0\theta)=-\frac1{c_0\theta(1-\theta)}.
 \tag{20}
\]
Other sheets retain their additive Fourier characters.
The exponentiated cut row is
\[
 \frac{p_{\rm out}}{p_{\rm in}}
                =\frac{1-\theta}{\theta}\frac{u}{c_0-u}.
 \tag{21}
\]
The ordered-coproduct ideal calculation in S uses only the internal
rows and the unit cut factors. It still forces
\(p_{\rm out}=p_{\rm in}\). Hence (21) is equivalent, in that
localized graph ring, to \(u=c_0\theta\). Conversely a full braid
fixed point at that logarithmic cut value satisfies the weighted
principal rows. Our chosen framed representation is therefore a
regular principal stationary point of this exact source presentation.
This remains an exponentiated-row statement with its log lifts.

The price of the complex probe is exact:
\[
 \sum_a\left|\binom da\theta^a(1-\theta)^{d-a}\right|
             =R_\theta^d,\qquad
 R_\theta=|\theta|+|1-\theta|.
 \tag{22}
\]
At \(M=1\) the denominators have moduli
\(2|\sin(\pi(r+1)/N)|\ge4/N\). For \(|M-1|\le1/(4N)\),
their changes are less than \(3|M-1|\le3/(4N)\), so their
moduli remain at least \(3/N\). On that disk (17) has operator norm at most
\((N/3)R_\theta^d\) in the stated factorial basis. All fixed
meridian derivatives have the corresponding polynomial factor
on a smaller disk by the Cauchy formula; the exponential factor is retained.

For complete geometric holonomy start at G's regular midpoint
\(A_{\rm cut}=-1\). The off-unit frames of Section 3 are dense
arbitrarily close to it. Preserve the branch of the cut logarithm
near \(\pi i\) in Section 4. Then \(\theta\) is arbitrarily close
to \(1/2\). Given \(\varepsilon>0\), continuity and
\(R_{1/2}=1\) permit the choice
\[
                       \log R_\theta<\varepsilon.
 \tag{23}
\]
Thus this source cost is at most \(e^{\varepsilon d}\), with an
actual fixed choice of frame and \(\theta\); it is not declared
polynomial or zero. Internal transfer and head walls remain.
No uniform slit-chart margin as \(\varepsilon\downarrow0\) is asserted.
No contributing deformation of the original finite cycle has
been constructed by changing its exact trace-one probe.

## 6. Scope and complete sources

The theorem supplies a common scalar factorial slit chart and an
exact source presentation having its geometric point as a regular
principal critical point. It does not prove the scalar factorial
amplitude theorem itself, a uniform full coherent-kernel phase,
an integration contour reaching this point, an \(r\)-centralizer
period, or a nonzero geometric coefficient. The construction also
does not replace actual support inequalities by analytic clocks.

* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* S: notes/research_soft_binomial_cut_stationary_source.md, SHA256
  667cb1eb70b770552de05e6f95f518016852b2c0aecdc874c3dff167fccb3d8b.
* G: notes/research_midpoint_geometric_braid_frame.md, SHA256
  9b9756929ac16b9413744ab376ac74718ecbaac645ab0440e3e3a835349b8e30.

The three complete sources were freshly read nontruncated in this
author sequence. Their used implications are checked separately
from the polynomial irreducibility, transfer-factor, integer-lift
and complex-probe calculations proved here. Only written mathematics
and text/hash operations are used. Frozen and public files are unchanged.
