# Critical branches for the finite entrance attachments

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This records two quantitative continuations of the actual prepared
cap phase. The first supplies its curvature on a real interval. The
second supplies the critical point and two Gaussian sectors for its
next attachment, on the true output disk. Neither assertion replaces
a complementary-source estimate by analytic continuation of a phase.

## 1. The prepared phase on a wider real interval

Use \(x_h,k_0\) and the exact original phases from
[the phase-graph theorem](research_three_phase_graph_transform.md).
Let \(C(x,\tau)\) be the original cap phase before its angular
saddle, and \(\Phi(x,y)\) the original retained phase after its
two index saddles. The prepared action is
\[
 S_1(y)=\operatorname{crit}_{x,\tau}
             \{C(x,\tau)+\Phi(x,y)\}.
 \tag{1}
\]
All constants and logarithmic lifts are those of the proved first
attachment. Put \(q=\cot\pi x\), \(t=\tan(\tau/2)\),
and \(e=\sec(\tau/2)\). Its angular equation is
\[
 P(x,\tau)=3\tau+2i\log(t+e)
             +i\{\log(q+t)-\log(q-t)\}-2\pi=0,
 \qquad C_\tau=\frac{iP}{2\pi}.
 \tag{2}
\]
The second equation is \(C_x+\Phi_x=0\). The exact derivatives
used in the certificate are
\[
 \begin{split}
 P_\tau&=3+i\left(e+\frac{qe^2}{(q-t)(q+t)}\right),
 &P_x&=\frac{2\pi i t(1+q^2)}{(q-t)(q+t)},\\
 C_{xx}&=-\pi\{\tan(\pi x+\tau/2)+\tan(\pi x-\tau/2)+2q\},
 &C_{x\tau}&=\frac{\tan(\pi x-\tau/2)-\tan(\pi x+\tau/2)}2.
 \end{split}
 \tag{3}
\]
The retained derivatives are the exact rational functions of its
selected quadratic root, with the logarithmic lifts fixed in the
original critical chart; no asymptotic phase replaces them.

**Proposition 1.** The actual branch (1) extends holomorphically to
a fixed neighborhood of
\(y=x_h+u\), \(-1/50\le u\le1/50\). On that real interval,
\[
 -\Re S_1''(y)>\frac{93}{10},\qquad |S_1''(y)|<16.
 \tag{4}
\]
At its center,
\[
 |\Re S_1'(x_h)|<\frac{113}{10000},\qquad
 \left|\frac{S_1'(x_h)}{k_0}\right|<\frac{69}{2500}.
 \tag{5}
\]
The complete real interval is covered by 399 accepted rational
parameter intervals. Each record retains both complex Newton
coordinates and both recovered retained indices.

*Proof.* On each interval solve \((P,C_x+\Phi_x)=0\) by a
fixed rational inverse-Jacobian proposal. The numerical solver supplies
only rational centers. If the parameter half-width is \(p\), the
unknown radii are \((7p/20,p)\). The parameter changes only the
second equation, by at most \(\sup|\Phi_{xy}|p\).
The outward weighted Newton derivative norm is below \(1/4\),
and its center displacement plus that norm times the radius is strictly
smaller than the radius in each coordinate. Thus every parameter in
the interval has a unique root in that polydisk. The intervals have
an exact multiplicity-one cover of \([-1/50,1/50]\).

All roots lie in
\[
 \begin{gathered}
 \Re x\in(.14,.20),\quad\Im x\in(.09,.12),\quad
 \Re\tau\in(0,1.8),\quad-\Im\tau\in(.97,1),\\
 \Re s,\Re t\in(.25,.45),\qquad
                         |\Im s|,|\Im t|<.03.
 \end{gathered}
 \tag{6}
\]
The larger index height here is explicit: the previous \(.02\)
box does not contain the entire branch. All root-product radii remain
below one. Every cap logarithm remains in its original right-half-plane
chart, and both retained quadratic roots remain on the original branch.

The arbitrary-height sign decomposition in
[joint concavity, Lemma 1](research_three_vertex_joint_concavity.md)
applies throughout the convex box (6). The cap Hessian estimate in
that note is unchanged. Consequently the full unsummed complex
symmetric Hessian has strictly negative real part. Its gradient is
injective: integrate that Hessian along a segment and pair with the
conjugate of the segment vector. Hence the interval roots agree on
overlapping parameter neighborhoods. At the center they agree with
the already certified prepared phase, fixing its constants and lifts.

The envelope derivative and Schur complement are exactly
\[
 S_1'=\Phi_y,
 \qquad
 S_1''=\Phi_{yy}-
 \frac{\Phi_{xy}^2}
      {C_{xx}-C_{x\tau}^2/C_{\tau\tau}+\Phi_{xx}}.
 \tag{7}
\]
Outward evaluation over every complete Newton box proves (4).
A separate center polydisk of radius \(10^{-10}\) proves (5).
All its Newton inequalities are retained in the same record.
\(\square\)

This proposition is an assertion about the original critical phase.
A source expansion on this larger real interval requires its own
finite-contour proof and error bound.

## 2. The next critical point on the true output disk

Let \(R=1/200\), and let
\[
 U(z,w)=S_1(z)+\Phi(z,w),\qquad
 z_c(w)=\operatorname{crit}_z U(z,w),\qquad |w-x_h|\le R.
 \tag{8}
\]
The analytic phase theorem already gives this holomorphic branch
inside \(|z-x_h|<R\). To retain its correlation with the output,
use the original three-variable system in \((x,\tau,z)\):
\[
 P(x,\tau)=0,\qquad C_x(x,\tau)+\Phi_x(x,z)=0,
 \qquad \Phi_y(x,z)+\Phi_x(z,w)=0.
 \tag{9}
\]
Its exact Jacobian is
\[
 \begin{pmatrix}
 P_x&P_\tau&0\\
 C_{xx}+\Phi_{xx}(x,z)&C_{x\tau}&\Phi_{xy}(x,z)\\
 \Phi_{xy}(x,z)&0&\Phi_{yy}(x,z)+\Phi_{xx}(z,w)
 \end{pmatrix}.
 \tag{10}
\]
The factor relating \(P\) to the cap angular derivative is retained
in (2); it is also retained in every Schur complement.

**Proposition 2.** Put \(D=5+\sqrt{21}\). On the closed output
disk in (8),
\[
 \Re\{k_0D(\epsilon R-(z_c(w)-x_h))^2\}
 -\frac35|k_0|\,|\epsilon R-(z_c(w)-x_h)|^2>10^{-6}
 \quad(\epsilon=\pm1).
 \tag{11}
\]
The certificate for this proposition accepts 179 rational angular
intervals after 294 visits. It is an exact cover of
the true output circle; it does not replace its image by an
uncorrelated disk around the central critical point.

*Proof.* Parameterize \(w=x_h+R e^{2\pi i\theta}\),
\(0\le\theta\le1\). On each exact rational interval use its
midpoint and the parameter radius \(p=\pi R\,\Delta\theta\),
which bounds the full arc distance to its midpoint. For (9), take
unknown radii \((.05p,.15p,.24p)\). Only the third equation
depends explicitly on the output, with variation at most
\(\sup|\Phi_{xy}(z,w)|p\). The certificate checks the
weighted Newton self-map on the entire arc rectangle, all original
branches, and all inequalities in (11). Any failed interval is split;
acceptance requires a strict outward inequality over the whole cell.

All certified \(z\) lie inside the true source disk. The old cap
and both retained index pairs stay in the same convex original
sign chamber used above. Thus the roots of (9) are exactly the
holomorphic critical branch (8). The derivative is evaluated through
the exact formula
\[
 z_c'(w)=-\frac{\Phi_{xy}(z_c,w)}
                        {S_1''(z_c)+\Phi_{xx}(z_c,w)},
 \tag{12}
\]
where \(S_1''\) is the first Schur complement (7).

For a fixed endpoint \(e=\epsilon R\),
the second expression in (11) is superharmonic in \(w\): its
first term is the real part of a holomorphic function, and its
Laplacian is
\[
               -\frac{12}{5}|k_0|\,|z_c'(w)|^2\le0.
 \tag{13}
\]
Its minimum is therefore on the circle, proving (11) throughout
the disk. Strict margins preserve a fixed neighborhood.
\(\square\)

**Corollary 3.** The two straight segments from
\(x_h-R\) to \(z_c(w)\), and from \(z_c(w)\) to
\(x_h+R\), stay inside the true source disk and give a valid
local saddle contour for the actual incoming source packet.
At both real endpoints its phase is below the critical phase by
more than \(1/(2\cdot10^6)\).

Indeed, throughout the disk the established phase estimates give
\[
 -U_{zz}=k_0D-k_0\{h_1'(z-x_h)+R_{xx}(z-x_h,w-x_h)\},
 \qquad |h_1'|\le\tfrac12,\quad |R_{xx}|<\tfrac1{10}.
 \tag{14}
\]
Here \(R_{xx}=\Phi_{xx}/k_0+5\) is the normalized kernel
Hessian remainder from the phase-graph theorem.
Along either segment with displacement \(d=\epsilon R-(z_c-x_h)\),
(11)--(14) give \(\Re[-U_{zz}d^2]>10^{-6}\).
Integrating twice from the critical point proves the stated endpoint
loss and strict decay along the segment. Convexity of the geometric
disk keeps this contour inside the domain of the original source
packet. The two tangent rays belong to opposite Gaussian convergence
sectors, fixed by continuation from the central parameter. A local
rounding gives the usual oriented full Gaussian coefficient. This
controls the central segment only; its real annulus and the rest of
the Fourier period still require the original complementary estimates.

## 3. Reproduction and scope

The real-interval certificate is
[certify_three_prepared_cap_real_critical.py](../experiments/certify_three_prepared_cap_real_critical.py),
with [its record](../repro/results/research-three-prepared-cap-real-critical.json).
The true-circle certificate is
[certify_three_first_entrance_critical.py](../experiments/certify_three_first_entrance_critical.py),
with [its record](../repro/results/research-three-first-entrance-critical.json).
Run each with `--precision 192`. Numerical root solving only chooses
rational Newton data; acceptance and exact interval coverage use
outward arithmetic. Neither artifact asserts a full source asymptotic
on a domain solely from phase continuation. The strict bounds and the
original parameter-dependent packets persist on a fixed neighborhood
of the complete ordinary outside color; Cauchy estimates there retain
the ordinary outside derivatives when this central contour is used.
