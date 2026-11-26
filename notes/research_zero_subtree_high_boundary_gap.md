# High boundary indices in a zero-power subtree

Research proof, 2 November 2026. The existing positive comparison for
Conway sources applies to the boundary coefficient arrays of a
zero-power subtree. It supplies a strict bound for every term having
a high boundary index, uniformly over all real boundary angles and
at both level parities. Internal indices remain unrestricted in this
comparison.

Together with the internal-index estimate and the regular all-low
asymptotic, this gives the whole-boundary source theorem for every
zero-power subtree whose minimizing heights have interior edge
maxima. In particular it covers all such selected subtrees with
original vertex degrees at least four. This is an asymptotic of
the stated finite source; identification of its action with the
volume of a partially filled knot complement is a separate question.

## 1. The arrays and the positive reference

Let \(S\) be a nonempty connected proper set of vertices in a
fixed finite tree. All crossing powers on \(S\) are zero.
Every selected vertex has original degree \(d_v\ge3\), including
edges to vertices outside \(S\). Write \(b\) for the number
of these boundary edges. Then
\[
 b=\sum_{v\in S}d_v-2(|S|-1)\ge |S|+2\ge3.
 \tag{1}
\]
Use the original Newton polynomials \(e_r\), complete kernel,
and full closing functional:
\[
 K_N(t,u)=\sum_{r=0}^{N-1}e_r(-2\cos t)e_r(-2\cos u),
 \qquad
 \phi_N(f)=(-1)^{N-1}N^2[z^{N-1}]
                         \operatorname{rem}_{P_N}f.
 \tag{2}
\]
The quotient retains its double roots and their first derivatives.
The complete definitions are in
[the subtree Fourier note](research_zero_power_subtree_fourier_bound.md).

Put \(D=N-1\) and \(m_N=\lfloor D/2\rfloor\).
A boundary angle \(u\) supplies the polynomial
\[
 B_N^u(z)=\sum_{r=0}^{D}b_{N,r}(u)e_r(z),
 \qquad b_{N,r}(u)=e_r(-2\cos u).
 \tag{3}
\]
Its low part has \(0\le r\le m_N\); its high part has
\(m_N<r\le D\).
Define the positive weights
\[
 w_{N,r}=
 \begin{cases}
 e_r(-2),&0\le r\le m_N,\\
 1,&m_N<r\le D,
 \end{cases}
 \qquad W_N=\sum_{r=0}^{D}w_{N,r}e_r.
 \tag{4}
\]
For real \(u\), the low Laurent coefficients are positive and
give \(|b_{N,r}(u)|\le e_r(-2)\).
For high \(r\), the complete value-and-derivative interpolation
bound gives a polynomial interval norm. Hence absolute constants
\(C,A\) satisfy
\[
 |b_{N,r}(u)|\le CN^A w_{N,r}
       \qquad(0\le r<N,\ u\in\mathbb R).
 \tag{5}
\]
The high bound in (5) concerns the whole polynomial on \([-2,2]\);
it is not deduced from its vanishing spectral values alone.
The first derivatives at double roots are bounded before Hermite
interpolation, as proved in
[the complete-node conditioning argument](../papers/conway-source-bounds/norms.tex).

Contraction of an internal kernel is exactly the Newton reversal:
\[
 \phi_N^{(t)}
  \left(K_N(t,u)\sum_j f_j e_j(-2\cos t)\right)
       =\sum_{r=0}^{D}f_{D-r}e_r(-2\cos u).
 \tag{6}
\]
Thus the selected source compiles into product junctions at the
original selected vertices, coefficient reversal on each internal
edge, and the \(b\) boundary arrays (3). There is no reversal
on a boundary leaf. In the terminology of the Newton syntax,
all these boundary leaves are unflagged.

Replace each boundary array by the pure positive complete leaf
\[
 h_N=\sum_{r=0}^{m_N}\frac{N^2S_{2r}}{S_r^4}e_r.
 \tag{7}
\]
The resulting positive reference has a strict state by the
reduced-junction criterion: all its junction degrees are at least
three and none has a flagged leaf.
Let \(F_0\) be its complete action maximum. Explicitly, this is
the maximum on its original shared-label polytope of one
\[
 g(a)=J(2a)-4J(a),\qquad
 J(a)=\int_0^a\log(2\sin\pi s)\,ds
\]
for each boundary leaf, and one original multiplication phase
\[
 m(x,y,z)=J(x+y)+J(z)-J(x)-J(y)
            -J(z-x)-J(z-y)-J(x+y-z)
 \tag{8}
\]
for each retained product. Turns and the deleted closing product
retain their exact complementary constraints.
This reference is used for comparison; (7) is not asserted to equal
the actual array (3).

## 2. The comparison theorem being used

The applicable result is the theorem entitled **Positive comparison
with shared indices** in
[the Conway source comparison](../papers/conway-source-bounds/probe.tex),
with its weights defined in (4).
It concerns a fixed connected region of unflagged product junctions,
with coefficient reversal on its internal edges and at least two
incoming boundary arrays. Its hypothesis is the coefficient envelope
\[
 |[e_r]F_{j,N}|\le e^{N(c_j+\varepsilon_N)}w_{N,r},
 \qquad \varepsilon_N\longrightarrow0.
 \tag{9}
\]
The arrays may be complex and may occupy both Newton ranges.
The designation of an input as low type refers to the positive
reference used for the comparison, not to a support restriction on
the actual coefficient array.

Expose one outgoing edge and write the other part of the expression
as \(A(F_1,\ldots,F_n)\), before its outgoing reversal.
The theorem estimates the positive scalar
\[
 \phi_N(W_N A_N^{\rm abs}),
 \tag{10}
\]
where each input coefficient has first been replaced by its
absolute value and the same products and reversals are performed.
Its upper rate is \(\sum_j c_j+\Phi_A\), where \(\Phi_A\)
is the action of the pure reference closure
\(\phi_N(h_N A(h_N,\ldots,h_N))\).
More precisely, every sector in which at least one input index
or the comparison index from \(W_N\) is high has a strict
exponential loss below that rate. The internal indices are unrestricted.

The proof of this statement is relevant to its present use.
The low coefficient profile in (9) is \(g\), and the high
profile is zero. It compares them on the full product supports
using the concave upper functions
\[
 \widetilde g(x)=g(\max(x,1/4)),\quad 0\le x\le1/2,
 \qquad k(x)=-2J(x/2),\quad0\le x\le1.
 \tag{11}
\]
Here \(g\le\widetilde g\) and \(0\le k\).
Two supporting-plane inequalities supply a loss at a two-input
seed or a single-input attachment. They are proved, with their
exact parameter ranges, in
[the two-input and attachment calculation](../papers/conway-source-bounds/composition.tex).
At all-low inputs the same supporting planes apply without a loss.
At a product, the child slopes cancel against the derivatives of
the original multiplication phase. A reversal changes the output
slope's sign. At the closing product the two output slopes cancel
under its complementary relation. Consequently a high external
index leaves a fixed positive loss while all intermediate labels
remain shared.

For at least four boundary leaves, the unflagged tree can be
rooted between two completed expressions. An internal edge has at
least two leaves on either side; for a single junction split its
leaves into two groups of size at least two. This makes exactly
the parameter inequalities required by the two supporting-plane
estimates available. The three-leaf case is handled separately
at their recorded endpoint parameter \(X=1/2\); two high
indices there vanish by the exact product law.
Thus the comparison does not assume a completed-root grammar for
an arbitrary original boundary rooting.

The two scalar comparisons use finite rational certificates.
Their outward enclosure rules and coverage arguments are written
in [the arithmetic proof](../papers/conway-source-bounds/arithmetic.tex).
Both certificates were replayed for this application:

| Comparison | Covered domain | Certified loss |
|---|---|---|
| Two-input seed | 16 full slope intervals and their product polytopes | \(1/100\) |
| Single-input attachment, bounded slope part | 55 rectangles covering the slope square | \(1/1000\) |

The remaining attachment range uses the written elementary rational
bound \(57269/136687500>1/2500\).
The saved runs are
[the two-input record](../repro/results/research-zero-subtree-two-leaf-certificate.json)
and [the attachment record](../repro/results/research-zero-subtree-attachment-certificate.json).
The existing reproduction runner executes these certificates and
the finite trace checks with one command:

    python3 papers/conway-source-bounds/check.py --output /tmp/conway-source-check

The certificates prove the scalar inequalities together with their
written concavity and enclosure arguments. The tree propagation,
the polynomial envelope (5), and the identification of the present
reference are the written parts of the application.

## 3. A uniform gap for every high boundary sector

Let \(Z_{S,N}(\mathbf u)\) be the original source and let
\(Y_{S,N}(\mathbf u)\) retain only low boundary indices,
while keeping every internal index. Then there are constants
\(C,A,\delta>0\), depending on the fixed selected tree, such that
\[
 \sup_{\mathbf u\in\mathbb R^{\partial S}}
 |Z_{S,N}(\mathbf u)-Y_{S,N}(\mathbf u)|
       \le CN^A e^{N(F_0-\delta)}.
 \tag{12}
\]
All sufficiently large integer levels are included.

To prove this, expose any one boundary edge as the closing input.
The other \(n=b-1\ge2\) boundary arrays feed the unflagged
expression \(A\), and the exact source is
\[
 Z_{S,N}(\mathbf u)
   =\phi_N\bigl(B_N^{u_0}
          A(B_N^{u_1},\ldots,B_N^{u_n})\bigr).
 \tag{13}
\]
This is the exact identity (6) followed by the original product
and closure; it is not a geometric move.

Split each boundary array into its low and high parts.
Fix one of the resulting sectors, with at least one high part.
Replace its coefficients by their absolute values. Positivity
of all Newton multiplication coefficients, exact reversal, and
the positive complementary pairing imply that its absolute
value is bounded by the same positive contraction.
Equation (5) puts each incoming array under (9), with
\(c_j=0\) and a common \(\varepsilon_N=O(\log N/N)\),
uniformly over every real boundary angle.
At the exposed root it gives a polynomial multiple of \(W_N\)
restricted to the sector's original low or high comparison band.

If the root part is high, (10) has a high comparison index.
If some other boundary part is high, it has a high input index.
In either case the comparison theorem in Section 2 applies and
gives a strict loss below \(\Phi_A\).
The pure closure defining \(\Phi_A\) is exactly (7) on the
compiled selected tree, so \(\Phi_A=F_0\).
There are only \(2^b-1\) such sectors, independent of \(N\).
Reducing the positive loss absorbs their number and the polynomial
envelopes, proving (12).

No sign of a real boundary coefficient was suppressed without a
bound: its absolute value was taken before the positive coefficient
comparison. Nor was any internal high index omitted. The imported
comparison leaves all internal product labels in their full supports.

## 4. The two level parities and the endpoint duality

For completeness, the exact complete-boundary behavior can also
be checked directly. If \(i\) is high, put \(r=D-i\).
Factorial reflection \(S_iS_r=N\) and root reflection give
\[
 e_i(z)e_r(z)=
        \frac{(-1)^N P_N(z)}{N^2(c_r-z)},
 \qquad c_r=2\cos((2r+1)\pi/N).
 \tag{14}
\]
The quotient on the right is a polynomial.
At an odd level, \(P_N(-2)=0\), while \(c_r+2>0\)
and \(e_r(-2)>0\); hence \(e_i(-2)=0\).
At an even level \(P_N(-2)=4\), so
\[
 e_i(-2)e_{D-i}(-2)=\frac4{N^2(c_{D-i}+2)}.
 \tag{15}
\]
The factor on the right has only polynomial size above and below
throughout the high-index range. Consequently the even-level
complete-boundary high coefficient has profile
\(-g((D-i)/D)\), with a uniform logarithmic error.

That improved profile concerns \(u=0\). Equation (12) uses the
polynomial interval bound for arbitrary real \(u\).
The uniform boundary conclusion therefore
does not depend on vanishing at odd levels or on extending (15)
to other angles.

## 5. Consequence for a regular zero-power subtree

Assume now that the unique minimizing heights of the convex
edge potential are regular:
\[
 \sinh(h_v/2)\sinh(h_w/2)<1
                       \qquad(vw\subset S).
 \tag{16}
\]
The [internal high-index proof](research_zero_subtree_internal_high_gap.md)
identifies the positive reference maximum with the stationary
all-low action \(M\):
\[
 F_0=M.
 \tag{17}
\]
Its argument uses the exact reversal compilation, the common
leaf profile \(g\), and the old concave Newton action. The
all-low asymptotic and strict Fourier tails identify the restricted
maximum. Its physical internal indices are strictly below \(1/2\),
so the restrictions are inactive there. Concavity then makes
this a global maximum of the original positive reference.
Uniqueness yields a strict gap for all internal high indices when
boundary indices remain low.

Combining that estimate with (12) gives
\[
 \sup_{\mathbf u\text{ real}}
 |Z_{S,N}(\mathbf u)-Z^{\rm low}_{S,N}(\mathbf u)|
       \le CN^A e^{N(M-\delta)}
 \tag{18}
\]
for a possibly smaller \(\delta>0\).
The difference has degree at most \(N-1\) in each boundary
spectral variable. Its strict gap therefore persists on a
sufficiently small fixed complex polydisk.
It follows that the whole original source has the same holomorphic
asymptotic as the low part:
\[
 Z_{S,N}(\mathbf u)
   =N^{-3(b-1)/2}A(\mathbf u)e^{NW(\mathbf u)}
                                  (1+O(N^{-1})).
 \tag{19}
\]
Here \(A(0)>0\), and \(W,A\) are exactly those constructed in
[the regular low-source theorem](research_regular_zero_subtree_low_source.md).
There is no additional unit factor or change of trace normalization.
The diagonal boundary Hessian and the global boundary-strip bound
from that theorem transfer as well: on the real torus absorb
(18) by decreasing the angular-loss constant; near the complete
boundary use (19), and away from it preserve the fixed real
gap by polynomial continuation.

Condition (16) holds if all selected original degrees are at
least four. More generally the edgewise criterion
\(\tan(\pi/d_v)\tan(\pi/d_w)\le1\) suffices.
Thus (19) treats arbitrarily many adjacent zero-power vertices
in those classes. The selected finite tree remains fixed as
\(N\to\infty\).

This result is a whole-boundary source theorem. A volume theorem
after further fillings still needs the original geometric periods,
the absolute volume normalization, and the hypotheses of the
further-filling argument. Neither the coefficient comparison nor
the presence of a unique source saddle supplies those identifications
by itself.
