# Compatible endpoint logarithms and a common regular factorial chart

Private written proof, 18 November 2026.

At every usable finite endpoint branch, a single generic complex
soft-cut parameter gives a buffered slit chart for all regular
factorial arguments. The endpoint arguments can simultaneously
have their prescribed lower or upper principal lifts, with zero
transfer lifts and the cut logarithm unchanged.

Two exact calculations supply this statement. Integral flow gives
the complete compatibility criterion for prescribed unit-edge
logarithms, including dependent endpoint clusters. On each endpoint
branch the prefix minors are affine polynomials in the cut parameter.
Their adjacency forces every constant wire or transfer clock to be
one. The remaining clocks can consequently be put off the unit circle
simultaneously on these one-dimensional branches.

These are principal source charts. Choosing logarithms does not
translate a finite head, identify its two endpoints, or discard
long-transfer aliases and their currents.

## 1. The expanded graph and the exact relative lifting criterion

Use R's expanded directed graph \(\Gamma\): split each crossing
into its donor and receiver visits and insert the directed transfer
edge between them. Every visit has one incoming and one outgoing
wire edge. The wire edges form the single directed knot cycle.
The cut edge and all transfer edges are R's primitive chord
coordinates. Let \(\partial\) be incoming-minus-outgoing incidence.
The wire and transfer clocks obey
\[
                 \prod_e Z_e^{\partial_{ve}}=1
                 \quad\text{at every vertex }v.
 \tag{1}
\]
This is the original signed crossing conservation law, not an
additional cyclic extension of the finite source.

Consider holomorphic nonzero clocks near a base point. Let \(I\)
be all edges whose base clock is one. Prescribe integers \(b_e\)
for \(e\in I\), and a logarithm \(\ell_*\) of the cut clock.
Assume the cut clock differs from one, as it does near the
chosen midpoint cut. Thus the cut does not belong to \(I\).
We seek logarithms satisfying
\[
 \partial\zeta=0,\qquad
 \zeta_e=c_0b_e\ (e\in I)\text{ at the base point},\qquad
 \zeta_{\rm cut}=\ell_*,\qquad c_0=2\pi i.
 \tag{2}
\]
The cut logarithm is prescribed as a holomorphic branch nearby.
The values on \(I\) in (2) are base values; they need not remain
constant away from the base point.

Delete \(I\) and contract each component of \(\Gamma\setminus I\)
to a vertex. Keep the edges of \(I\), allowing loops, to obtain
the graph \(\Gamma_I\). The exact compatibility condition is
\[
                             \partial_{\Gamma_I}b=0.
 \tag{3}
\]
It imposes no independence assumption on the edge forms in \(I\).

Necessity follows by summing \(\partial\zeta=0\) over each
complementary component: its internal edges cancel and its
boundary values are exactly \(c_0b\).
For sufficiency, choose arbitrary logarithms elsewhere, with the
specified cut branch and the specified values on \(I\).
Equation (1) gives
\[
                         \partial\zeta=c_0k,\qquad
                              k\in\mathbb Z^{V(\Gamma)}.
 \tag{4}
\]
By (3), the sum of \(k\) on every complementary component is zero.
On a spanning tree of each component, remove leaves successively:
assign the incident tree edge an integer correction cancelling
the leaf defect, then transfer that defect to the next vertex.
The last defect is zero. This constructs an integer correction
on the complementary edges and leaves \(I\) untouched.

The correction can also leave the cut untouched. If the cut
were a bridge of its complementary component, one side of that
bridge would have, in the full graph, only the cut and edges
of \(I\) in its boundary. Multiplying (1) over that side at the
base point would give \(Z_{\rm cut}^{\pm1}=1\), a contradiction.
Choose the spanning tree in that component without the cut.
Loops cause no difficulty. The integer corrections just constructed
therefore prove all of (2).

The construction extends holomorphically. Choose the initial local
logarithm branches with their stated base values. In a connected
small neighborhood, (4) has the same integer \(k\) because it is
continuous and integer-valued. The same constant integer correction
then gives exact holomorphic conservation. In particular the
component boundary-log sums remain zero, not merely zero at the
base point.

The same tree argument proves the integral image identity
\[
 \operatorname{im}\bigl(\ker(\partial:\mathbb Z^E\to\mathbb Z^V)
                         \longrightarrow\mathbb Z^I\bigr)
                         =\ker\partial_{\Gamma_I}.
 \tag{5}
\]
Thus (3) is an exact integral criterion, not just its complex-linear
relaxation.

## 2. The lower and upper endpoint assignments are compatible

Let \(\gamma\) be the actual knot circulation:
\[
              \gamma_e=1\text{ on wire edges},\qquad
              \gamma_e=0\text{ on transfer edges}.
 \tag{6}
\]
Each split visit has one incoming and one outgoing wire, so
\(\partial\gamma=0\).

For the row/\(e\)-zero endpoint type of E, prescribe
\[
                              b_e=0\quad(e\in I).
 \tag{7}
\]
For the column/\(f\)-zero type, prescribe instead
\[
 b_e=1\text{ on unit wire edges},\qquad
 b_e=0\text{ on unit transfer edges}.
 \tag{8}
\]
Condition (3) holds for (7) trivially and for (8) because
\(b=\gamma|_I\). This includes all simultaneous dependent
wire and transfer walls.

There is also an explicit cut-preserving conversion from (7)
to (8). Since the cut is not a bridge in \(\Gamma\setminus I\),
an undirected return path supplies an integer circulation \(c\)
supported in that complementary graph with \(c_{\rm cut}=1\).
Its coefficients use the signs of the fixed edge orientations.
Starting with the zero-lift solution, add
\[
                                  c_0(\gamma-c).
 \tag{9}
\]
It has the required values on \(I\), zero cut coefficient, and
zero incidence. No positivity of this correcting circulation is
claimed or needed. For arbitrary mixed prescriptions, (3) remains
the criterion; they are not asserted automatically compatible.

## 3. Prefix polynomials on an individual endpoint branch

Use E's fixed complete representation, finite list of stage
meridians \(H_j\), prefixes \(P_j=H_j\cdots H_1\), and framing
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad
 \alpha_r=(1,(1-r)/s),\quad v_r=(r,s)^t.
 \tag{10}
\]
Every \(H_j\) has characteristic polynomial \((t+1)^2\) and is
noncentral. E identifies the finite row and column branches as
\[
               r=1+s\xi,\qquad r=s\eta,
 \tag{11}
\]
for finite lists of constants \(\xi,\eta\).
Flags at infinity give no finite branch and are excluded here.
For a fixed branch define the prefix polynomial
\[
                              p_P(s)=\alpha_rPv_r.
 \tag{12}
\]
Every such polynomial is affine in \(s\).
For a row branch,
\[
 \alpha_r=(1,-\xi),\qquad
                 v_r=(1,0)^t+s(\xi,1)^t.
 \tag{13}
\]
For a column branch, with \(u=(\eta,1)^t\),
\[
 v_r=su,\qquad
 p_P(s)=s(1,-\eta)Pu+(0,1)Pu.
 \tag{14}
\]
A branch is called usable if none of the retained prefix
polynomials is identically zero. An unusable branch has no
point at which all those prefix minors are units, and hence
does not conceal an omitted regular point.

For adjacent prefixes \(P'=HP\), a constant ratio
\(p_{P'}/p_P=\lambda\) necessarily equals \(-1\).
On a row branch, (13)'s two vector coefficients span
\(\mathbb C^2\); equality of the affine polynomials therefore gives
\(\alpha_rHP=\lambda\alpha_rP\), hence
\(\alpha_rH=\lambda\alpha_r\).
On a column branch, the two covectors in (14) span the dual
space, giving \(HPu=\lambda Pu\).
In either case \(\lambda\) is an eigenvalue of \(H\), and so is
\(-1\). The vectors and covectors used here are nonzero.
Consequently every actual wire clock
\[
                               A=-p_P/p_{P'}
 \tag{15}
\]
is either identically one or nonconstant on the branch.
This conclusion remains valid when one or both prefix
polynomials have degree zero.

## 4. Constant transfers are also exactly one

At a signed crossing use F's four actual prefixes
\(P_0,P_1,P_2,P'_1\). The outer prefix \(P_2\) is preserved.
All four adjacent ratios
\[
 \frac{p_1}{p_0},\quad \frac{p_2}{p_1},\quad
 \frac{p'_1}{p_0},\quad \frac{p_2}{p'_1}
 \tag{16}
\]
come from intervening complete parabolic meridians.
Whenever any is constant, Section 3 makes it \(-1\).
The positive transfer is
\[
                            C=\frac{p_0p_2}{p_1p'_1};
 \tag{17}
\]
the negative transfer is its reciprocal.
The four polynomials are nonzero and affine on a usable branch.

Suppose (17) is a nonzero constant. If \(p_1\) has degree one,
it divides \(p_0p_2\), and hence is proportional to \(p_0\) or
\(p_2\). Thus \(p_1=-p_0\) or \(p_2=-p_1\), by (16).
If \(p_1\) has degree zero, degree comparison gives
\[
                  \deg p_0+\deg p_2=\deg p'_1\le1.
 \tag{18}
\]
At least one of \(p_0,p_2\) is constant; the same alternatives
\(p_1=-p_0\) or \(p_2=-p_1\) follow. This includes the case
where all four polynomials are constant.

In the first alternative (17) is \(-p_2/p'_1\); its constancy
and (16) give \(p_2=-p'_1\), hence \(C=1\).
In the second it is \(-p_0/p'_1\); then \(p'_1=-p_0\) and again
\(C=1\). The reciprocal has the same conclusion.
Every required transfer clock is therefore identically one
or nonconstant. No multiplicative-independence assertion is used.

## 5. One complex cut choice works for all usable finite branches

There are finitely many branches (11), prefixes, wires and crossings.
In a small complex disk about \(s=-2\), exclude \(s=0,-1\),
all zeros of nonzero prefix polynomials on usable branches,
and E's finite mixed row/column collision set.
The prefix exclusions are finite because their degrees are at most
one. They cannot exhaust the disk.

Each remaining nonconstant wire or transfer clock is a holomorphic
nonzero rational function on the resulting domain. Its modulus-one
locus has empty interior: constancy of its modulus on an open set
would force constancy of the holomorphic function. The complement
of that locus is open and dense. Intersecting these finitely many
open dense sets gives a choice \(s_*\), arbitrarily close to \(-2\),
such that on every usable branch at \(s_*\),
\[
                    Z_e\equiv1\text{ on that branch},
                    \quad\hbox{or}\quad |Z_e(s_*)|\ne1.
 \tag{19}
\]
Here the identity in the first alternative is a branch identity.
In particular there are no accidental additional unit-clock edges
at the chosen point.
Include the cut function \((1+s)^{-1}\) in this finite off-circle
list even if there are no usable endpoint branches.

Choose the inverse of \(s=e^{-c_0\theta}-1\) near \(\theta=1/2\).
The fixed parameter \(\theta_*\) can be arbitrarily close to
\(1/2\). It is a complex choice: the cut clock itself is among
the nonconstant wire clocks and (19) puts it off the unit circle.
No analogous density assertion on a prescribed real-\(\theta\)
slice is made.

At each resulting finite puncture, E's separation gives a single
endpoint type. Use (7) or (8) and the exact lifting theorem with
cut logarithm \(c_0\theta_*\). For any remaining edge,
\[
       \Im\frac{\zeta_e}{c_0}
                    =-\frac{\log|Z_e|}{2\pi}\ne0.
 \tag{20}
\]
Integer corrections do not change this imaginary part.
F's literal positive and negative five-factor lists are all wire
or transfer lengths. Thus every regular normalized factorial
argument lies in
\[
             \mathcal D=\mathbb C\setminus
                     \bigl((-\infty,0]\cup[1,\infty)\bigr).
 \tag{21}
\]
Shrink a holomorphic neighborhood of each puncture so that these
regular lengths stay in compact subsets of \(\mathcal D\).
The endpoint lengths instead remain near their prescribed values
zero or one, with exact additive flow and the unchanged cut branch.
Since the lists are finite, common positive buffer constants can
be chosen after fixing this source and parameter. Nearby bounded
color offsets and fixed Weyl shifts, of size \(O(N^{-1})\) in
the regular normalized arguments, fit slightly larger compact
subsets for sufficiently large \(N\). Endpoint normal estimates require
their separate retained endpoint formulas.

## 6. Exact source scope

The fixed \(\theta_*\) uses F's literal trace-one binomial cut,
so the original unmarked root scalar is unchanged. Its exact
total variation is
\[
                       (|\theta_*|+|1-\theta_*|)^{N-1},
 \tag{22}
\]
which can be made at most \(e^{\varepsilon(N-1)}\) for any
prescribed \(\varepsilon>0\). It is retained, not called one.
All marked cut changes and their normal derivatives keep F's
commutator current. No off-root closed-source or ordinary-Jones
normal reset is inferred.

Equations (2), (7)--(9) choose compatible principal logarithm
lifts. They are not changes of summation variables in the finite
state. The actual upper wire index is \(N-1\), with clock
\(Q^{-1}\), rather than the index \(N\) or the lower endpoint.
An original transfer near its upper wall is not identified with
a short transfer by assigning a principal clock-one lift zero.
Every finite projector, long-transfer alias, physical band,
mixed face and inserted-current state in R remains in the source.

The theorem supplies the common regular-factor chart for local
endpoint analysis on usable finite framing branches. It does not
construct a joint endpoint Gaussian kernel or its neighboring
packet, control prefix-zero or infinite framing strata, transport
the original relative cycle, or prove noncancellation.

## Complete proof-source pins

* E: notes/research_soft_cut_separates_regular_endpoint_types.md,
  SHA256 935f6d97b9ca3a068412b33075610d17e0a571f68f2bc2925eac70c0480a2555.
* R: notes/research_actual_oblique_geometric_contour_decomposition.md,
  SHA256 9180de472bafb38c479d3e1aafac6c75c388d668371892f54219de658728034c.
* F: notes/research_literal_factorial_common_slit_frame.md,
  SHA256 9764a2b77469c7fad402b9b8e609b304a79083bde18fb139031c06fd93650ca8.

All three complete direct texts were read nontruncated in this
active author sequence, and every used implication checked.
Only written mathematics and text/hash operations were used.
Frozen and public files are unchanged.
