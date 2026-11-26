# Coherent lower bounds for arbitrary zero-seam runs

Research proof, 5 November 2026. The 256-bit focused outward
certificate passes all 48 scalar corners using 40 original-log disks.
The argument is uniform in run length. It compares the complete raw
source on every seam-incident edge with the original coherent phase
after all seam coordinates are simultaneously replaced. No isolated
seam hypothesis, word-length enumeration or boundary-potential
approximation is used. Neighboring nonseam angles are still restricted
to small neighborhoods of one tenth or one half.

## 1. Original logarithmic gradients and a height lower bound

Use the original normalized primitive
\(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\)
and \(J(x)=\Re g(x)\) on the real period, with its continuous
periodic endpoint values. The original allocated phase is
\[
 \phi_{\eta\epsilon}(a,b)
 =g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias
       -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \tag{1}
\]
with the original zero-lift conditional root \(s\), and write
\(f_{\eta\epsilon}=\Re\phi_{\eta\epsilon}\) on real arguments.
For \(0<a,b\le1/2\), set
\[
 S=\cot(\pi s)=u+iv,\quad p=\cot(\pi a),\quad q=\cot(\pi b).
 \tag{2}
\]
The [closed real root theorem](research_mixed_half_endpoint_conditional_packet.md)
gives \(u>0,\ |v|<1,\ p,q\ge0\). With the logarithm on the right
half-plane, the exact original derivatives are
\[
 \begin{split}
 \phi_a&=\Log(S+p)-\Log(S-i)-\frac\eta2g'(a),\\
 \phi_b&=\Log(S+q)-\Log(S+i)-\frac\epsilon2g'(b).
 \end{split}
 \tag{3}
\]
Exponentiating follows from \(e^{-2\pi is}=(S-i)/(S+i)\).
At real \(S>0\) the original sine-log differences have imaginary
parts \(+\pi s\) and \(-\pi s\), respectively, so (3) has the
original additive lift. Both sides extend holomorphically over the
connected chamber \(u>0,|v|<1\): the displayed logarithms have
positive-real-part arguments, and \(0<\Re s,\Re(s+a),\Re(s+b)<1\)
keeps the original derivatives regular. This also includes \(p=0\)
or \(q=0\) by the same regular continuation.

The arguments in (3) obey
\[
 0<\Arg(S+p)-\Arg(S-i)<\pi,\qquad
 -\pi<\Arg(S+q)-\Arg(S+i)<0 .
 \tag{4}
\]
For example, the imaginary numerator of
\((S+p)/(S-i)\) is \(u+(1-v)p>0\); the right-half-plane
logarithm difference lies in \((-\pi,\pi)\), fixing its sign.
The second numerator is \(-u-(1+v)q<0\).
Put \(\theta_x=\pi(1/2-x)\), so that
\(g'(x)=\log(2\sin\pi x)+i\theta_x\). Thus
\[
 -\frac\eta2\theta_a<\Im\phi_a<\pi-\frac\eta2\theta_a,\qquad
 -\pi-\frac\epsilon2\theta_b<\Im\phi_b
                                      <-\frac\epsilon2\theta_b.
 \tag{5}
\]
These coarse bounds suffice; no sharper acute-angle theorem is needed.

Let
\[
 I_0=[.30,.39],\quad I_1=[.27,.33],\qquad
 H_0=[-.03,.02],\quad H_1=[-.057,0].
 \tag{6}
\]
The [full height-reset theorem](research_mixed_full_height_reset.md)
proves \(-\Re\phi''>0\) on the admitted unselected products with
real coordinates in \([.22,.5]\) and heights in \(H_\eta,H_\epsilon\).
Hence for \(a,b\) in that real interval, the function
\(t\mapsto\Re\phi(a+ith,b+itk)\) is convex. Its tangent at zero
gives
\[
 \Re\phi_{\eta\epsilon}(a+ih,b+ik)
       \ge f_{\eta\epsilon}(a,b)
                   -h\Im\phi_a(a,b)-k\Im\phi_b(a,b).
 \tag{7}
\]
Define the affine height costs
\[
 \begin{array}{c|cc}
 d&c^L_d(x)&c^R_d(x)\\\hline
 0&.02\pi&.03\pi\\
 1&(.057/2)\theta_x&.057(\pi+\theta_x/2).
 \end{array}
 \tag{8}
\]
Equations (5) and the signed height intervals (6) imply
\[
 \Re\phi_{\eta\epsilon}(a+ih,b+ik)
   \ge f_{\eta\epsilon}(a,b)-c^L_\eta(a)-c^R_\epsilon(b).
 \tag{9}
\]
If either height is zero, its cost is omitted. In particular the
positive contribution of a negative first height is not replaced by
an unnecessary absolute gradient bound.

## 2. Literal raw source ceilings

Fix \(0<\rho\le1/1000\), independently of \(N\), and put
\[
 \nu=-J(1/1000),\qquad
 \Delta=(1/1000)\log2-J(1/1000).
 \tag{10}
\]
These dominate the corresponding collar costs for every such \(\rho\).
The [zero-uniform collar estimates](research_mixed_real_zero_collar.md)
bound each low product factor by its value at one times
\(CN^A e^{N\Delta}\), and its actual Fourier weight by
\(CN^A e^{N\nu}\). All low targets here are real, so every selected
monomial has unit modulus.

On an edge with both targets in \([0,\rho]\), the literal row at the
zero endpoint is \(P_j^{-\epsilon}\), because \(p_j(1)=P_j\).
The original factorial estimate
\(\sum_j|P_j|^{-\epsilon}\le CN^A e^{N\epsilon/6}\), proved in the
[both-low source theorem](research_mixed_both_low_raw_support.md),
therefore gives the complete raw upper rate
\[
 U^{SS}_{\eta\epsilon}
     =\frac\epsilon6+2\Delta+\frac{\eta+\epsilon}{2}\nu .
 \tag{11}
\]
Both Fourier halves, both low numerator factors, all rows and both
parities remain. The real first-argument chirp has modulus one.

The [height-resolved source profiles](research_mixed_height_resolved_seam_sources.md)
give the exact height-zero ceilings
\[
 A_{00}=.325066,\quad A_{01}=.386681,\quad
 A_{10}=.460764,\quad A_{11}=.515591,\qquad
 B_0=.325066,\ B_1=.515591 .
 \tag{12}
\]
For a left boundary edge, with seam in the second argument and its
nonseam neighbor real, the raw rate is
\[
 U^L_{\eta\epsilon}=A_{\epsilon,\eta}
                                  +\Delta+\frac\epsilon2\nu.
 \tag{13}
\]
For a right boundary edge it is
\[
 U^R_{\eta\epsilon}=B_\epsilon+\Delta+\frac\eta2\nu.
 \tag{14}
\]
At nonzero physical neighbor height use its original profile in
place of the corresponding zero-height constant. These piecewise
affine profiles are continuous on each permitted selection band.
The rates (11)--(14) bound absolute sums of original rows, with
any separately prescribed positive Fourier tolerance.

## 3. Forty-eight scalar lower bounds

For each ordered pair \((\eta,\epsilon)\), the focused checker proves:
\[
 \begin{split}
 f_{\eta\epsilon}(a,b)-c^L_\eta(a)-c^R_\epsilon(b)
                        -U^{SS}_{\eta\epsilon}&>1/3,
       &&(a,b)\in I_\eta\times I_\epsilon,\\
 f_{\eta\epsilon}(.1,b)-U^L_{\eta\epsilon}&>1/20,
       &&b\in I_\epsilon,\\
 f_{\eta\epsilon}(.5,b)-c^R_\epsilon(b)
                        -U^L_{\eta\epsilon}&>1/20,
       &&b\in I_\epsilon,\\
 f_{\eta\epsilon}(a,.1)-U^R_{\eta\epsilon}&>1/20,
       &&a\in I_\eta,\\
 f_{\eta\epsilon}(a,.5)-c^L_\eta(a)
                        -U^R_{\eta\epsilon}&>1/20,
       &&a\in I_\eta .
 \end{split}
 \tag{15}
\]
The [real phase is jointly concave](research_mixed_real_outer_support.md);
the costs (8) are affine. Thus the first line is reduced to four
corners for each of four types, and each remaining line to two
endpoints for each type. There are exactly 16 internal and 32
boundary scalar comparisons. Concavity at a real half endpoint
follows by continuity of the original closed-half branch.

The checker accepts forty distinct roots by strict disk self-maps of
the original logarithmic equation, not by proximity to polynomial
roots. It checks the original strips and selected cotangent chamber
and evaluates the calibrated dilogarithm phase outward. Saved-center
replay reuses the exact rational disk centers. There is no parameter
cover or sampling premise in (15).
The smallest certified internal reserve exceeds .3489238265;
the left and right boundary reserves exceed .0791397414 and
.0791574502, respectively, before the stated rational thresholds
are subtracted. The source and proof bindings are checked before
and after the complete scalar run.

## 4. Simultaneous replacement of every seam run

Fix the original word and hybrid contour at collar \(\rho\).
Let \(S\) be any nonempty set of seam positions; adjacency is allowed.
Assume
\[
 \begin{split}
 &x_s\in[0,\rho]\quad(s\in S),\qquad
 x_j\in[\rho,.5]\quad(j\notin S),\\
 &x_j\in[.1,.1+\zeta]\ \cup\ [.5-\zeta,.5]
       \quad\hbox{whenever }j\notin S
       \hbox{ neighbors a position in }S .
 \end{split}
 \tag{16}
\]
All original selections are allowed. Replace every seam real
coordinate by \(\Re r_s\) and remove its selection, simultaneously.
The repaired target \(z_s^\#\) has real part in \(I_{\epsilon_s}\)
and unselected height in \(H_{\epsilon_s}\). Every interior vertex
of a seam run has target exactly \(r_s\); its own and both neighbor
cutoffs are one. Run endpoints may be partly reset by an outside
low neighbor. No conditional source is evaluated at a physical
zero argument in this replacement argument.

For an internal seam edge, both repaired coordinates satisfy (6).
Equations (9), (11) and (15), with a small finite tolerance, give
the strict finite raw-to-coherent gain \(1/4\) on that edge.
This is uniform even when both endpoint heights are partly reset.

At an exact low boundary \(x_j=.1\), the physical nonseam height
and the repaired adjacent seam height are zero. The second or fourth
line of (15) applies. At an exact half boundary \(x_j=.5\), the
nonseam height is zero and the repaired seam height may be any
admitted unselected height; (7)--(9) and the third or fifth line apply.
Thus these individual boundary comparisons include singleton runs
with mixed outside endpoints, as well as arbitrary longer runs.

Choose \(0<\zeta<.02\) small enough. At a low neighbor both its
physical and repaired heights have magnitude at most \(.7\zeta\),
and the adjacent repaired seam height has magnitude at most
\(.475\zeta\). At a half neighbor both heights have magnitude at
most \(22.8\zeta^2\). These are the exact row-cutoff bounds of the
[low/half neighborhood assembly](research_mixed_low_endpoint_connector_lower.md).
Compact continuity of the established source profiles and original
coherent phases, retaining the true selected half-corrections, turns
each boundary comparison into a finite raw-to-coherent gain \(1/40\).
There are finitely many types, selection choices and endpoint classes,
so one width suffices, independently of run length.

For precision, the coherent allocated rate is
\[
 e_j(u,v)=\Re\phi_j(u,v)
    +\frac{\sigma_{j-1}}2\chi(u)+\frac{\sigma_j}2\chi(v),
 \qquad \chi(z)=\max\{\Re g(z),-2\pi\Im z\}.
 \tag{17}
\]
All repaired seam selections are zero. The nonseam selections stay
unchanged. At the exact real boundary endpoints the corrections
vanish, and their continuity is included when choosing \(\zeta\).
For a fixed selection no source estimate is interpolated across the
opposite-sign height band.

## 5. The remaining edges and the whole region

Let \(n_{SS}\) count original edges with both endpoints in \(S\),
and \(n_{SA}\) edges with exactly one endpoint in \(S\).
The remaining edges are AA edges. Replacing the seam coordinates
changes only neighboring nonseam heights; an AA-edge real coordinate
and selection never change.

If a changed nonseam vertex has one seam neighbor, it belongs to
at most one AA edge. If it has two seam neighbors, it belongs to
none. Therefore there are at most \(n_{SA}\) changed endpoint
incidences on AA edges. Every height change is at most \(.7\zeta\):
for half endpoints use \(22.8\zeta^2\le.7\zeta\).
Shared endpoints and two changes on one edge are counted by
incidences, with that edge evaluated only once.

On every relevant compact nonlow source product let \(L_\rho\)
bound the vertical derivatives of each branch of (17). The finite
maximum of branches is Lipschitz with that same bound.
If the other endpoint is below .1, its zero cutoff prevents any
height change, so no unproved complex deep-low source is used.
All nonzero AA changes and straight height interpolations stay in
the completed early-cap, plateau and left/right interface products.
Consequently the total AA discrepancy is at most
\[
                         .7L_\rho\zeta\,n_{SA}.
 \tag{18}
\]
Decrease \(\zeta\) until this is at most \(n_{SA}/200\).

The repaired configuration lies entirely in \([\rho,.5]^m\);
the [deep-half phase theorem](research_mixed_deep_low_half_region.md)
therefore gives \(\sum_j e_j(z^\#_{j-1},z^\#_j)\le M\).
Use the complete original packets on AA edges and spend total
remaining Fourier tolerance below \(1/200\). Since
\(n_{SS}+n_{SA}\ge1\), the full rate is bounded by
\[
 \begin{split}
 M-\frac14 n_{SS}-\frac1{40}n_{SA}
                   +\frac1{200}n_{SA}+\frac1{200}
 &\le M-\frac{49}{200}n_{SS}-\frac3{200}n_{SA}\\
 &\le M-\frac{|S|}{100}.
 \end{split}
 \tag{19}
\]
The final inequality uses the exact incidence identity
\(2|S|=2n_{SS}+n_{SA}\).

**Theorem.** For every fixed word and fixed collar \(\rho\), there
is a width \(\zeta>0\) such that the original finite densities on
all regions (16) have a polynomial upper factor times
\(\exp\{N(M-|S|/100)\}\). Summing their selected integrals over
every nonempty \(S\) and all original selections gives
\[
                            C N^A e^{N(M-1/100)}.
 \tag{20}
\]
Every Fourier halfweight is allocated exactly once along the
original edges; a shared nonseam neighbor contributes its two
halves on the two incident edges. The original finite Laurent
source, scalar, carriers and bounded hybrid Jacobian are unchanged.
The comparison is not a substitution in the integral and asserts
no monotonicity of finite kernel moduli.

For \(S\) equal to the whole cycle, all edges are SS, every repaired
target is exactly its reference, and there are no AA or boundary
terms. A one-cycle uses its single diagonal SS edge and two
halfweights; a two-cycle keeps both original parallel edges.
The identity in (19) includes these cases and arbitrary runs without
enumerating their lengths.

The width is qualitative and may depend on the fixed collar.
Nonseam neighbors outside the two endpoint neighborhoods and
coordinates in the right half-period remain separate. This is not
a whole-period asymptotic or a new knot-family conclusion.

Reproduction:

    python3 experiments/check_mixed_seam_run_connector_lower.py --precision 256
    python3 experiments/check_mixed_seam_run_connector_lower.py --precision 320 --input repro/results/research-mixed-seam-run-connector-lower.json --output /tmp/research-mixed-seam-run-connector-lower-review.json
