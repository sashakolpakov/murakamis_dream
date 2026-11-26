# An absolute real-output expansion for the original prepared cap

Research proof, 4 November 2026. Completed source artifacts and frozen
manuscripts are unchanged.

The original prepared source has a controlled principal term on the
larger real output interval of radius \(.02\), with an absolute
complementary error. Its main term need not dominate that error at the
ends of the interval. A separate full-period estimate controls every
output phase outside this interval. Together they give a stronger real
Gaussian envelope for the prescribed initial source.

## 1. Statement and the actual critical branch

Keep the original source and carriers
\[
 B_N(y,w)=v(w)^T(JM^3)^2h(y),\qquad
 x_h=\frac16+iY_h,\quad Y_h=\frac{\log2}{2\pi},
 \qquad M_1=\Re S_1(x_h,-2)>1.9113.
 \tag{1}
\]
The phase \(S_1\) and nonzero amplitude \(\mathcal A\) agree
with \(\Theta_{\rm eff}\) and \(\mathcal A\) in
[the quantified source theorem](research_three_prepared_cap_quantified_source.md).
Continue them by their original stationary equations.

**Theorem 1.** Uniformly for real \(|v|\le1/50\), with
\(y=x_h+v\), the full original source has the absolute expansion
\[
 \begin{split}
 B_N(y,w)={}&C_{N,3}\kappa N^{-1}\mathcal A(y,w)
                  e^{NS_1(y,w)}(1+O(N^{-1}))
                   +O(N^A e^{1.9107N}),\\
 &\hspace{35mm}\mathcal A(y,w)\ne0.
 \end{split}
 \tag{2}
\]
The phase and amplitude extend holomorphically to a neighborhood of
this real interval and of the complete ordinary color \(w=-2\).
The expansion holds at both parities, uniformly on a sufficiently
small such neighborhood, and with the corresponding fixed parameter
derivative estimates. The algebraic Gaussian error in the first term
and the absolute error in the second term are kept separately.
No relative asymptotic for the complete source is asserted where
\(\Re S_1\le1.9107\).

The critical-branch input is
[the real entrance certificate](research_three_entrance_critical_branches.md),
Section 1, and its
[399-cell record](../repro/results/research-three-prepared-cap-real-critical.json).
It proves existence and uniqueness of the original critical branch on
the entire real interval by outward complex Newton self-maps. All four
critical variables lie strictly in
\[
 \begin{array}{c|c|c}
 &\Re&\Im\\ \hline
 x&(.14,.20)&(.09,.12)\\
 \tau&(0,1.8)&(-1,-.97)\\
 s,t&(.25,.45)&(-.03,.03).
 \end{array}
 \tag{3}
\]
The actual cap angles also satisfy \(\Re\tau<1.55<\pi/2\) and
\(-\Im\tau<1<1.07\), so the original complete-edge local packet
applies near their entire compact critical curve. The unchanged cap
box and the arbitrary-height retained Hessian sign chamber give an
accretive joint Hessian. Its complex gradient is injective on the
convex chamber: pairing a gradient difference with the conjugate of
the point difference integrates a strictly positive Hermitian real
part. Thus all neighboring Newton boxes select the same original
branch. The certificate also proves
\[
             -\Re S_{1,yy}>9.3,\quad |S_{1,yy}|<16,
             \quad |\Re S_{1,y}(x_h,-2)|<.0113.
 \tag{4}
\]

## 2. Global real-index and wire-join bounds

Use the L40 retained source and the central fixed wire height
\(h_c=.10135869\), overcovered by
\([.10135867,.10135871]\). Its unweighted, phase-optimized real
index envelope is \(\mathscr E_r\) in equation (7) of
[the whole-period entrance theorem](research_three_prepared_cap_period_bound.md),
where \(r=e^{-2\pi h_c}\). The output radius is \(1/2\).
For every \(r\in[1/2,.53]\), the already proved global maximum
lies in \([.30,.37]^2\), and the envelope is strictly concave on
\(s+t>1/2\).

**Lemma 2.** Let \(B=[1/4,9/20]\). Uniformly over both entire
real wire phases and input heights \(h_c\le h\le Y_h\), every
original real-index subset outside \(B^2\) has upper rate below
\(.64\). At either input join \(\Re x=.14,.20\), the whole
retained vertex has upper rate below \(.6459\), uniformly over
the same heights and the entire real output period.

*Proof.* For \(p=s+t\le1/3\), the L40 cutoff gives
\[
 \mathscr E_r\le\log2+\mathcal J(p)+g(r)
                  <.694-.07+.012=.636<.64,
 \quad
 g(r)=-\tfrac12\log(2r)+\tfrac13\log\frac r{1-r}.
 \tag{5}
\]
Here \(g(1/2)=0\), \(g'<2/5\), and the two endpoints of
\(p\in[1/40,1/3]\) give \(\mathcal J(p)<-.07\), as in the
previous envelope proofs. For \(1/3\le p\le1/2\), increasing
a smaller index increases the envelope until \(p=1/2\).

For \(p>1/2\), the global maximizer lies inside \(B^2\).
On any ray from it, concavity makes the envelope nonincreasing.
Thus the maximum outside \(B^2\) is bounded by the four index
faces \(s=1/4,9/20\) or \(t=1/4,9/20\), with the other index
running from \(1/2\) minus the fixed index to one minus that
index. One-dimensional concave supporting planes prove the bound
\(.64\) on these four faces at each of the two endpoint heights
\(h_c,Y_h\). These are eight of the exact domains in the record.
They also cover the continuous \(p=1/2\) boundary reached above.
The envelope is convex in the input height for each fixed pair of
indices, so the endpoint bounds cover the full joining interval.

For a join with fixed real input phase \(\xi=.14\) or \(.20\),
minimize only the outgoing denominator interval, retaining the
literal input denominator. On \(B^2\), the resulting envelope
is strictly concave in the two indices: its negative Hessian is
\(a(ds+dt)^2+d_xds^2+\ell_{1/2}''(t)dt^2\), with all coefficients
positive. Indeed \(s-\xi\in[.05,.31]\) and \(s+t\ge1/2\).
Four supporting planes, one for each join phase and endpoint height,
give the bound \(.6459\) on the entire square. Outside the square
use the preceding \(.64\) bound. Finally the join envelope has
positive input-height second derivative \(d_x+c_x\) on \(B^2\),
by the exact harmonic Hessian; the center of the optimized outgoing
interval is \(t/2\) and does not depend on that height. Convexity
again supplies every intermediate height. All estimates are for the
absolute original summands, so summation and fixed derivatives cost
only polynomial factors. \(\square\)

Combining Lemma 2 with the actual cap bounds gives the following
strict original-source rates:
\[
 \begin{array}{c|c}
 \text{original remainder}&\text{upper rate}\\ \hline
 \text{real indices outside }B^2&1.26465+.64=1.90465\\
 \text{remaining cap angular pieces}&1.26+.64699=1.90699\\
 \text{two wire joins}&1.2638+.6459=1.9097\\
 \text{exterior wire intervals at }Y_h&1.264+2c<1.910132.
 \end{array}
 \tag{6}
\]
These bounds hold for every real output phase. The cap rates and their
ordinary-normal scope are the actual full-cap estimates already used
in the whole-period entrance proof, not a local Gaussian substitution.

## 3. All index and translation currents on the wider real interval

The exact joint principal phase, including both cardinal factors, is
\[
 \mathcal G(x,\tau,s,t;y)
   =b(x,\tau)+\Psi(\tau)+\frac{3i\tau^2}{4\pi}-i\tau
                         +F(s,t;x,y)-\pi i(x+y).
 \tag{7}
\]
The real box is
\[
 \mathcal B=[.14,.20]\times[0,1.8]\times B^2,
 \qquad \Re y\in[11/75,14/75],\quad\Im y=Y_h.
 \tag{8}
\]
Retain the exact initial cotangent rectangles, with index heights
\(\Im s=\pm.008\), \(\Im t=-.017,.012\). Extract their constant
product, with its original coefficient \(+N^2\), and move it first
to the baseline heights
\[
       (.10135869,-.97895510,.00300831,-.00629803)
             \quad\text{in the order }(x,\tau,s,t).
 \tag{9}
\]
All original index factorial and root-product interpolants are regular
on these rectangles. The full low complete kernel has its uniform
upper exponent \(\Re\Psi\) throughout the cap rectangle; its
nonzero local packet is needed only near the actual critical points.

The exact joint Hessian is negative definite on (8), with the input
and cap heights in (3) and arbitrary index heights of modulus at most
\(.03\). For the retained part this is the sign decomposition in
Lemma 1 of
[the joint Hessian theorem](research_three_vertex_joint_concavity.md),
which imposes no imaginary-height ordering. Its signs follow from
\(s+t\in[.5,.9]\), \(s-\Re x,t-\Re y\in(0,.5)\), and
\(0<\Re x,\Re y<.5\). The cap uses its unchanged Lemma 3 box.
The denominator radii stay below one even at index depths \(.03\).

Concave supporting planes on the full five-real-variable box give
\[
 \begin{array}{c|c|c}
 \text{domains}&\text{number}&\text{upper rate}\\ \hline
 \text{index sides, including every vertical product}&16&1.9107\\
 \text{four horizontal index products}&4&1.95\\
 \text{baseline translation boundary faces}&8&1.9107.
 \end{array}
 \tag{10}
\]
The four horizontal alias terms each pay at least \(2\pi(.008)\),
so \(1.95-2\pi(.008)<1.9107\). The index-side endpoints cover
their whole connecting height segments by joint imaginary convexity.
This retains every vertical--vertical product and all half-grid
cotangent factors, as in the previous quantified proof.

Next translate the four principal heights simultaneously from (9)
to the actual critical heights for each output parameter. A critical
index may have depth below \(-.02\); the old \(\pm.02\) constant
is not used here. The exact sign chamber remains valid through
\(\pm.03\), as just proved. The source interpolants remain regular
because \(|X|e^{2\pi(.03)}<1\), \(|Y|e^{2\pi(.03)}<1\), and
\(1/2\le\Re(s+t)\le9/10\).

For each of the 399 exact output cells, eight further supporting
planes bound every boundary face of (8) at the actual critical
heights by \(1.9107\). The full outward height enclosures from the
critical certificate are retained. To avoid cancellation in a broad
interval primitive, the value is enclosed at an interior height
midpoint plus the exact imaginary-gradient mean-value bound over
the full height box. The real gradients in the supporting plane
are also enclosed on that entire box. Thus the check covers all
critical heights and every output point of the cell, not just its
center.

The total certificate has
\[
              16+4+8+8+4+4+8(399)=3236
 \tag{11}
\]
supporting planes: the first three groups are (10), the next groups
are the real-index, join and far-output comparisons, and the last
group contains all final critical-height faces. The independent
replayer verifies the exact domain list, the complete output interval
cover, all height boxes and every inequality with independent
negative-frequency primitives.

At fixed real coordinates the real phase is convex along any joint
imaginary translation, since its imaginary Hessian is minus its real
horizontal Hessian. Hence every intervening Stokes face is bounded by
the maximum of its initial and final values, both below \(1.9107\).
The exact four-dimensional homotopy keeps all induced boundary
currents. No independent rectangular height combinations or vanished
wall terms are assumed.

## 4. Gaussian extraction and original-source restoration

Use the original finite-source decomposition in the following order:
first the real-index complement; then the cap angular remainder on
the retained real-index square; then the two exact cotangent formulas
and their connecting faces; finally the joint principal translation.
The bounds (6), (10)--(11) retain every resulting current and give
their absolute upper rate \(1.9107\). Their strict compact margins
also retain all finite midpoint shifts and the floor in the L40 cut.

On the final critical-height horizontal plane, the joint Hessian
gives strict concavity and the selected point is the unique maximum.
The actual complete-edge local packet, the exact factorial and
root-product symbols, and ordinary parameter stationary phase give
the principal term in (2). All critical variables stay away from
their real boundaries, all local factors are nonzero, and the
Gaussian determinant is accretive. The resulting nonzero amplitude
is the analytic continuation of the already normalized amplitude
at \(y=x_h\). This is a joint local computation from the actual
four-variable density; it does not assume an independently proved
sequential cap or retained packet on the larger parameter range.

The literal coefficient \(+N^2\), the original trace and wire
normalizations, and the two-dimensional index and two remaining
Gaussian integrations give the same prefactor
\(C_{N,3}\kappa N^{-1}\) as in the quantified source theorem.
Uniform parameter stationary phase supplies the indicated algebraic
relative error for this principal contribution. Every complementary
source current retains the separate absolute error in (2). The
small-complex-parameter and fixed-derivative statements follow from
the same strict compact margins and local holomorphic contour
deformations; the outside angular dependence is even and descends
to ordinary color near \(-2\).

Finally the full-period original Fourier corner-transfer error is
below \(1.715\), uniformly over every real outgoing phase. Adding
it restores \(A^2\) from \(A(A-E_{40})\) without changing the
coefficient or the absolute error in (2). This proves Theorem 1.

## 5. The far outgoing period and a sharper entrance envelope

**Proposition 3.** On the complementary outgoing arc
\(d_{\mathbb T}(\eta,1/6)\ge1/50\),
\[
             |B_N(\eta+iY_h,-2)|\le CN^A e^{1.91115N}.
 \tag{12}
\]
This includes fixed Fourier and ordinary outside derivatives, with
polynomial cost.

*Proof.* At the central input height, maximize the input denominator
over its phase and retain the outgoing interval integral. If
\(t\notin[22/75,28/75]\), strict concavity of the unweighted
envelope and its maximizer in \([.30,.37]^2\) reduce its maximum
to the two corresponding index faces. Supporting planes bound both
by \(.6465\); low-sum regions were already bounded in (5).
Indices outside \(B^2\) have the stronger \(.64\) bound.

For the remaining indices, the outgoing interval has center
\(t/2\in[11/75,14/75]\). Its integral increases strictly with
circular distance from that center. Thus on the complementary
outgoing arc its minimum occurs at one of these two endpoints.
Hold the outgoing phase at either endpoint and maximize over
\((s,t)\in B\times[22/75,28/75]\). This is a strictly concave
index function; two more supporting planes prove the bound
\(.6465\). This proves a termwise global retained bound for the
entire far outgoing arc. Multiplication by the actual central cap
bound \(1.26465\) gives \(1.91115\). The exterior wire intervals,
joins and original corner error in (6) are all smaller. \(\square\)

Put \(v(t)=\min\{d_{\mathbb T}(t,0),1/100\}\).

**Corollary 4.** The actual initial prepared source obeys
\[
 |B_N(x_h+t,-2)|\le CN^A
      \exp N\{M_1+.0113\,v(t)-(29/20)v(t)^2\}
                       \qquad(t\in\mathbb R).
 \tag{13}
\]
The linear coefficient here bounds the real directional slope. It
does not replace the complex phase-class parameter
\(|S_1'(x_h)/k_0|\).

*Proof.* On \(|t|\le.02\), (4) gives
\[
 \Re S_1(x_h+t,-2)\le M_1+.0113|t|-4.65t^2.
 \tag{14}
\]
For \(|t|\le.01\), this dominates the principal term in (2)
by (13). On \([.01,.02]\) the expression in (14) is decreasing
and is already smaller at \(.01\) than the capped right side of
(13). The absolute plateau \(1.9107\) is smaller throughout,
since \(M_1>1.9113\) and the minimum capped correction is
\(-.000032\). For \(|t|\ge.02\), (12) is below
\(M_1-.00015<M_1-.000032\). Periodicity of the modulus covers
the full torus. Fixed derivatives retain the same exponential
comparisons with polynomial factors. \(\square\)

No later quantum attachment or closing coefficient is inferred from
this entrance theorem alone.

## 6. Reproduction

```sh
python3 experiments/certify_three_prepared_cap_real_critical.py --precision 192
python3 experiments/certify_three_prepared_real_output_currents.py --precision 160
python3 experiments/replay_three_prepared_real_output_currents.py --precision 192
```

The [current author](../experiments/certify_three_prepared_real_output_currents.py)
and [record](../repro/results/research-three-prepared-real-output-currents.json)
retain every rational domain and supporting point. The
[independent replayer](../experiments/replay_three_prepared_real_output_currents.py)
and [record](../repro/results/research-three-prepared-real-output-currents-replay.json)
verify all 3,236 planes, the 399 critical-coordinate cells and exact
coverage. Optimization proposes only rational supporting points;
acceptance is entirely outward arithmetic plus the written global
concavity and monotonicity reductions.
