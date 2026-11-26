# An invariant analytic phase class for three-crossing attachment

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The actual prepared cap phase belongs to an explicit analytic class
preserved by attachment of the retained three-crossing phase. The
critical wire and the centered outgoing gradient contract uniformly.
This is an analytic phase theorem. A uniform original-source packet
on the initial disk and bounds for the complementary wire integrals
remain separate requirements for full-source propagation.

## 1. The exact normalization

Use the original retained phase \(\Phi\), including its cardinal
factor and constant, from
[the local composition calculation](research_three_vertex_local_composition.md).
Put
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\quad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),\quad
 \rho=\frac{5-\sqrt{21}}2,\quad R=\frac1{200}.
 \tag{1}
\]
For \(x=x_h+z\), \(y=x_h+w\), define the actual derivative
remainders by
\[
 \frac{\Phi_x}{k_0}=-5z+2w+R_x(z,w),\qquad
 \frac{\Phi_y}{k_0}=2z-5w+R_y(z,w).
 \tag{2}
\]
The subscripts in \(R_x,R_y\) label these two functions. Their
first derivatives are the corresponding Hessian remainders. The
exact homogeneous identities give \(R_x(0,0)=R_y(0,0)=0\).

**Lemma 1.** On the complex bidisk \(|z|,|w|\le R\),
\[
 |\partial_zR_x|,|\partial_wR_x|,
 |\partial_zR_y|,|\partial_wR_y|<\frac1{10}.
 \tag{3}
\]
These are bounds on the exact holomorphic retained phase, not on a
quadratic approximation to it.

Here and below a holomorphic function on a closed disk means one
holomorphic on a neighborhood of that disk. Section 3 proves (3)
by a finite Taylor enclosure with its full analytic remainder.

## 2. The invariant class

Let \(S\) be a holomorphic phase on \(|z|\le R\), written in
the exact normalization
\[
 \frac{S'(x_h+z)}{k_0}=-\sqrt{21}\,z+h(z),\qquad
 |h(0)|\le\frac3{100},\quad \sup_{|z|\le R}|h'(z)|\le\frac12.
 \tag{4}
\]
There is no restriction or renormalization of its additive constant.

**Theorem 2.** For every \(|w|\le R\), the original critical
equation \(S'(x_h+z)+\Phi_x(x_h+z,x_h+w)=0\) has exactly
one solution in the closed disk. It lies strictly inside that disk
and depends holomorphically on \(w\). Set
\[
 S_+(x_h+w)=S(x_h+z(w))+\Phi(x_h+z(w),x_h+w).
 \tag{5}
\]
Then \(S_+\) belongs to the same class (4). More precisely,
\[
 \sup|z'|<\frac{47}{200},\qquad
 |h_+(0)|<\frac{47}{200}|h(0)|,\qquad
 \sup|h_+'|<\frac9{50},
 \tag{6}
\]
where the middle strict inequality is replaced by equality zero
when \(h(0)=0\). The critical wire Hessian has
\(-\Re(S''+\Phi_{xx})>18\), and every phase in (4) has
\(-\Re S''>8\).

*Proof.* Put \(a=\rho/2\), \(B=1/2\), \(e=1/10\),
\(H=3/100\). The exact equation is
\[
 z=\rho w+\frac\rho2\{h(z)+R_x(z,w)\}.
 \tag{7}
\]
The factor \(1/2\) follows from
\(5+\sqrt{21}=2/\rho\); it is essential to the self-map.
The right side has derivative bounded by
\(q=a(B+e)<63/1000\). On the closed disk its modulus is at most
\[
 \rho R+a\{H+(B+2e)R\}<R.
 \tag{8}
\]
The complex Banach theorem proves existence and uniqueness. Its
uniform strict margin and the nonzero derivative of the critical
equation give holomorphic dependence on a neighborhood of the
closed output disk.

The envelope derivative and (7) give the exact identity
\[
 h_+(w)=\rho h(z(w))+\rho R_x(z(w),w)+R_y(z(w),w).
 \tag{9}
\]
Define
\[
 Z=\frac{\rho(1+e/2)}{1-a(B+e)}<\frac{47}{200}.
 \tag{10}
\]
Differentiating (7) proves \(|z'|\le Z\). At \(w=0\),
\(|z(0)|\le a|h(0)|/(1-q)\). Since (9) also reads
\(h_+(0)=2z(0)+R_y(z(0),0)\), it gives
\(|h_+(0)|\le Z|h(0)|\). Finally differentiation of (9) yields
\[
 |h_+'|\le\{\rho(B+e)+e\}Z+\rho e+e<\frac9{50}.
 \tag{11}
\]
This proves preservation of (4), including its centered bound.
The Hessian assertions follow from
\[
 \sqrt{21}\Re k_0-|k_0|B>8,\qquad
 (5+\sqrt{21})\Re k_0-|k_0|(B+e)>18.
 \tag{12}
\]
All inequalities in (8), (10)--(12) are recorded as strict outward
scalar comparisons. \(\square\)

Iteration is consequently defined for any number of attachments at
the phase level, with \(|h_j(0)|\le(47/200)^j|h_0(0)|\).
The original constants in (5) are kept at every step. A nonzero
local source amplitude, when supplied on these domains, would be
multiplied by the actual retained amplitude and
\(\sqrt{2\pi}/\sqrt{-(S''+\Phi_{xx})}\); the branch is the
continuous Gaussian branch in the accretive right half-plane.
This observation is local and supplies no estimate of a complementary
source contour.

## 3. A rigorous retained-Hessian bound

The following details make the Taylor calculation self-contained.
Let \(X=X_he^{2\pi iz}\), \(Y=X_he^{2\pi iw}\), where
\(X_h=(1+i\sqrt3)/4\), and use the exact algebraic critical
branch
\[
 \alpha=X^{-1}-1,\quad\beta=Y^{-1}-1,\quad
 D=\sqrt{1-2(\alpha+\beta)+(\alpha-\beta)^2},\quad
 U=(1+\alpha-\beta-D)/2,\quad V=(1-\alpha+\beta-D)/2.
 \tag{13}
\]
At the origin \(D=2+i\sqrt3\), \(U=V=e^{-2\pi i/3}\).
On the larger bidisk \(|z|,|w|\le1/50\),
\(e^{2\pi/50}<23/20\) gives
\(|\alpha-\alpha_0|,|\beta-\beta_0|<3/10\). Thus
\[
 |D^2-D_0^2|<39/25,\quad |D|>23/10,
 \quad |U-U_0|,|V-V_0|<23/50.
 \tag{14}
\]
For the last bound, expand the square root about \(D_0^2\),
whose modulus is seven. The absolute binomial series bounds its
increment by
\((39/25)/(\sqrt7+\sqrt{7-39/25})<78/245\).
The discriminant stays in the upper half-plane, so this is the
same root as (13).

In particular
\[
 |U|,|V|>27/50,\quad |X|,|Y|<23/40,\quad
 |1-XU|,|1-YV|>321/2000,
 \quad |1-X|,|1-Y|>17/40.
 \tag{15}
\]
The continued indices and their logarithms are regular there.
Their exact derivatives satisfy
\[
 U_x=\frac{\alpha_x(1-U)}D,\quad
 U_y=\frac{\beta_yU}D,\quad
 V_y=\frac{\beta_y(1-V)}D,
 \quad \alpha_x=-2\pi i/X,\quad\beta_y=-2\pi i/Y.
 \tag{16}
\]
Equivalently differentiating (13) bounds each derivative in (16)
by \((253/35)(1+16/23)=429/35\). In the exact expressions
\[
 \Phi_{xx}=-\frac{U_x}U-
       \frac{2\pi iXU+XU_x}{1-XU}+\frac{2\pi iX}{1-X},
 \qquad \Phi_{xy}=-\frac{U_y}{U(1-XU)},
 \tag{17}
\]
these bounds and \(|k_0|>12/5\) give a common upper bound 64
for all three normalized Hessian remainders in (3) on the larger
bidisk. The checker verifies these rational majorants explicitly.

Compute their bivariate Taylor coefficients through total degree
eight by the finite power-series operations in (13), (16)--(17).
Every coefficient is enclosed outward. Cauchy's coefficient estimate
on radius \(1/50\) bounds the omitted total degrees by
\[
 64\sum_{j=9}^{\infty}(j+1)(1/4)^j
 =64(1/4)^9\frac{10-9/4}{(1-1/4)^2}.
 \tag{18}
\]
The polynomial plus this tail gives respective bounds below
\(.097,.051,.097\), proving (3). The calculation retains the
entire analytic remainder; no sampled derivative estimate is used.

## 4. The actual prepared phase is in this class

Let \(S_1(y)=\Theta_{\rm eff}(y,0)\) be the phase produced by
the [actual first complete-cap attachment](research_three_cap_central_source.md).
This specifies an actual phase germ and its constant, rather than a
chosen quadratic seed.

**Proposition 3.** This germ continues holomorphically to the
coordinate square
\(|\Re(y-x_h)|,|\Im(y-x_h)|\le1/200\), and its restriction
to the disk belongs to (4). More precisely,
\[
 |h_1(0)|<7/250,\qquad
 \sup|S_1''/k_0+\sqrt{21}|<1/2.
 \tag{19}
\]
On the true complex disk it also satisfies
\[
 |S_1''|<14,\qquad \Re S_1(y)>19107/10000.
 \tag{20}
\]

*Proof.* Use the exact original cap period and retained gradient,
\[
 3\tau+2i\log\{\tan(\tau/2)+\sec(\tau/2)\}
 +i\{\log(q+\tan(\tau/2))-\log(q-\tan(\tau/2))\}-2\pi=0,
 \quad b_x(x,\tau)+\Phi_x(x,y)=0,
 \tag{21}
\]
where \(q=\cot\pi x\). The checker partitions the output
square into exactly \(64^2\) rational cells. For each cell it
encloses an analytic Newton polydisk in the two variables
\((x,\tau)\), uniformly for every complex output in that cell.
Rational root proposals are not assumed to be zeros: outward
residuals, the parameter derivative \(\Phi_{xy}\), and the full
Jacobian prove contraction below \(1/10\) and a strict self-map.
All logarithms stay on their original branches.

Every enclosed root, including both index coordinates recovered from
(13), lies in the convex complex domain of the
[joint accretivity theorem](research_three_vertex_joint_concavity.md).
For fixed \(y\), its negative Hessian has positive Hermitian real
part throughout that domain. Integrating the gradient difference
along a complex segment and pairing with its conjugate shows that
the joint gradient is injective there. Hence the local roots agree
on overlapping output neighborhoods. The implicit function theorem
glues them to one holomorphic continuation of the established seed.

At each cell the exact two-stage Schur complement is
\[
 S_1''=\Phi_{yy}-\frac{\Phi_{xy}^2}
 {b_{xx}-b_{x\tau}^2/\mathcal F_{3,\tau\tau}+\Phi_{xx}}.
 \tag{22}
\]
Its outward enclosure proves (19). The center bound uses the
original first-attachment root enclosure, not an approximate root.
Equation (19) gives \(|S_1''|<4\pi+2\pi/\sqrt{21}<14\).
The established bounds \(\Re S_1(x_h)>1.9113\) and
\(|S_1'(x_h)|<.08\), integrated along the complex segment,
give
\[
 \Re S_1(y)>1.9113-.08(.005)-7(.005)^2
                         =1.910725>1.9107.
 \tag{23}
\]
This proves (20). \(\square\)

The proposition extends the actual phase, not automatically its
full-source asymptotic, to this quantified square. The established
first-attachment source theorem initially supplies some fixed output
neighborhood. To iterate original-source packets using (4), that
neighborhood must contain the disk used here, and the complementary
wire contours must be controlled. A retained-vertex packet on the
same disk is now supplied by the
[genuine bidisk theorem](research_three_vertex_bidisk_packet.md),
for the exact corner cutoff \(L=\lfloor N/40\rfloor\), with the
same phase and amplitude. The phase theorem does not replace the
remaining seed-source and complementary-contour conditions.

## 5. Reproduction

Run

    python3 experiments/certify_three_phase_graph_transform.py

The [checker](../experiments/certify_three_phase_graph_transform.py)
and [record](../repro/results/research-three-phase-graph-transform.json)
retain the Taylor coefficients and full Cauchy tail, the 4,096 exact
output cells, their rational Newton centers and radii, all four
critical-coordinate enclosures and branch margins, and the analytic
class inequalities. Numerical solving only chooses the rational
centers. The finite arithmetic verifies an analytic phase statement;
it does not certify a complementary quantum integration cycle.
