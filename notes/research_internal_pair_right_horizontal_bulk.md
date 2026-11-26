# The regular right-hand horizontal part of the pair contour

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The uniform shared-index cutoff leaves \(1/50<j/N<12/25\).
Within that range, the horizontal part with wire real coordinate
at least \(1/4\) has a strict exponential gap for both signs of
each trace angle. The estimate
extends through the closed regular factorial wall and to a fixed
small reflected width, for both wire heights. It follows from joint
concavity, the exact reciprocal-factorial upper bound, and the
logarithmic normalization of the actual complete-end kernels.
It concerns the original double-pole density. The row insertions and
observation terms in a reduced-pole cell formula remain separate.

## 1. The exact density and the fixed heights

Fix positive integer powers \(n,p\ge3\), with two complete outside
endpoints. Write the actual geometric point as
\[
 x_*=\xi_*+iY,\qquad
 t_*=\tau_*-iH_1,\qquad r_*=\rho_*-iH_2.
 \tag{1}
\]
The proved geometric bounds give
\[
 0<\xi_*<1/4,\quad Y>0,\qquad
 0<\tau_*,\rho_*<\pi/2,\quad 0<H_i<107/100.
 \tag{2}
\]
The original wire-order theorem and the mixed-phase domain
conditions give, with \(S_i=H_i/(2\pi)\),
\[
 \alpha(Y)<\xi_*<b_{i,*}<1/2,\qquad
 b_{i,*}>\alpha(S_i),\qquad
 \alpha(h)=\frac{\arccos(\operatorname{sech}(2\pi h))}{2\pi},
 \tag{3}
\]
where \(b_{1,*}=1/2-\tau_*/(2\pi)\) and
\(b_{2,*}=1/2-\rho_*/(2\pi)\).
These are the actual geometric data, not freely assigned heights.
The relevant inputs are the
[wire-order proof](research_positive_path_real_wire_order.md),
[pair angle and height bounds](research_real_pair_geometry_and_tail_gap.md),
and [mixed-phase domain extension](research_mixed_phase_height_extension_and_wire_order.md).

Use the canonical factorial representative \(B_N\), the full
original kernel \(K_N\), and \(\eta=(-1)^{N-1}\). Apart from its
original scalar, whose modulus is bounded by a fixed power of
\(N\), the upper-wire, lower-trace density is exactly
\[
 \begin{split}
 \mathcal I_N(x,t,r)
 ={}&\frac{B_N(x,t)B_N(x,r)K_N(t,0)K_N(r,0)
                         \sin t\sin r}{1-e^{2\pi iNx}}\\
 &{}\times
 \frac{\exp\{iN(nt^2+pr^2)/(4\pi)-iN(t+r)\}}
 {(1-\eta e^{-iNt})^2(1-\eta e^{-iNr})^2}.
 \end{split}
 \tag{4}
\]
This is the principal density of the
[exact combined contour reduction](research_internal_pair_combined_contour_reduction.md#3-a-compact-contour-with-the-original-trace-kernels).
The double poles represent the original first normals. Both their
denominators and all higher Fourier charges remain in (4).
The crossing carriers have modulus one.

For \(\varepsilon>0\), let \(\mathcal R_\varepsilon\) consist of
\[
 \begin{gathered}
 x=\xi+iY,\quad t=\tau-iH_1,\quad r=\rho-iH_2,\\
 1/4\le\xi\le12/25,\qquad
 0\le\tau,\rho\le\pi-2\pi\xi-\varepsilon.
 \end{gathered}
 \tag{5}
\]
Empty sections of this set are omitted. The fixed positive
\(\varepsilon\) keeps both shifted factorial real parts away
from zero. In particular this proposition does not include
the \(O(N^{-1})\) walls of the exact support-cell decomposition.

## 2. The actual finite factors have the mixed-phase upper rate

Put
\[
 \begin{split}
 \Phi(x,t,r)={}&b(x,t)+b(x,r)+\Psi(t)+\Psi(r)\\
              &+\frac{i(nt^2+pr^2)}{4\pi}-it-ir,
 \qquad \Psi(t)=\psi(t,0),\\
 M_{n,p}={}&\Re\Phi(x_*,t_*,r_*).
 \end{split}
 \tag{6}
\]
The normalization of \(\Psi\) is the original one,
\(\Psi(0)=M_\infty\).

On (5), all Newton factorial real arguments lie in a fixed
compact subinterval of \((0,1)\). Their actual uniform expansion is
\[
 B_N(x,t)=\frac{e^{Nb(x,t)}}{2N\sin(\pi x)}
                              (1+O(N^{-1})),
 \tag{7}
\]
and similarly for \(r\), with all fixed derivatives on smaller
complex neighborhoods. The sine denominator is bounded away
from zero since \(Y>0\) and \(\xi\) stays in the stated interval.

Both trace real parts in (5) belong to \([0,\pi/2]\).
The [complete-edge logarithmic theorem](research_internal_pair_complete_edge_gap.md#3-the-full-complete-end-kernel-at-both-parities)
therefore applies uniformly to the full original factors:
\[
 K_N(t,0)=\exp\{N\Psi(t)+e_N(t)\},\qquad
                  |\partial_t^\ell e_N(t)|\le C_\ell\log N.
 \tag{8}
\]
It holds on a fixed complex neighborhood of the entire rectangle
\(0\le\Re t\le\pi/2\), \(0\le-\Im t\le107/100\).
In particular (8) includes \(\tau=0\) and \(\rho=0\).
It does not require the additional condition
\(|\cos(t/2)|<1\) used in the local free-outside Gaussian theorem.

All denominators in (4) are uniformly harmless at these fixed
positive heights:
\[
 |1-e^{2\pi iNx}|\ge1-e^{-2\pi NY},\qquad
 |1-\eta e^{-iNt}|\ge1-e^{-NH_1},
 \tag{9}
\]
with the analogous bound at \(r\). The sine factors and coordinate
Jacobians are bounded. Consequently
\[
 |\mathcal I_N(x,t,r)|
                \le CN^A e^{N\Re\Phi(x,t,r)}
                     \qquad ((x,t,r)\in\mathcal R_\varepsilon).
 \tag{10}
\]
This includes both level parities and their literal finite trace
weights, rather than a leading Fourier mode of those weights.

The same bound, with an enlarged polynomial power, holds after any
fixed number of derivatives in \(x,t,r\). It also holds for fixed
ordinary selected-color normals. Indeed
\[
 |\sin(\tau-iH_i)|^2=\sin^2\tau+\sinh^2H_i
                         \ge\sinh^2H_i>0,
 \tag{11}
\]
so \((2\sin t)^{-1}\partial_t\), including at \(\tau=0\),
costs a fixed constant before differentiation. Equations
(7)–(9) and their holomorphic bounds then cost only powers of
\(N\). The outside colors here stay exactly complete.
No derivative in a free outside color is inferred from (8).

## 3. A strict gap on the whole regular right bulk

**Proposition 1.** For every nonempty set (5), there is
\(\delta_{n,p,\varepsilon}>0\) such that
\[
 \sup_{\mathcal R_\varepsilon}|\mathcal I_N|
       \le CN^A e^{N(M_{n,p}-\delta_{n,p,\varepsilon})}.
 \tag{12}
\]
The same statement holds for the derivatives specified after (10),
and for their integrals over subsets of (5) with bounded volume.

*Proof.* Use the real coordinates
\[
 z=(\xi,b_1,b_2),\qquad
 b_1=1/2-\tau/(2\pi),\quad b_2=1/2-\rho/(2\pi).
 \tag{13}
\]
Let \(Q\) be the convex hull of the image of (5) and the actual
critical point \(z_*\). On \(Q\),
\[
 \alpha(Y)<\xi,\qquad
 \xi<b_i\le1/2,\qquad b_i>\alpha(S_i).
 \tag{14}
\]
All strict inequalities have a positive margin: they hold at
the saddle by (3), and on (5) because
\(\xi\ge1/4>\alpha(Y),\alpha(S_i)\) and
\(b_i-\xi\ge\varepsilon/(2\pi)\).

The [joint mixed-phase concavity theorem](research_mixed_wire_phase_concavity.md#4-two-selected-vertices-and-their-shared-wire),
with its proved removal of height ordering, gives a strictly
negative real Hessian on this convex set. The faces \(b_i=1/2\)
cause no loss of strictness. In the Hessian proof, there
\[
 u=\Re\cot\pi(s_i+x)<0,\qquad
 v=\Re\cot\pi(s_i-x)>0,\quad
 w=\Re\cot\pi x>0,\quad
 d=\Re\csc\pi s_i>0.
 \tag{15}
\]
Thus the positive rank-one decomposition continues to those faces.
All functions are regular there and the other domain inequalities
retain their strict margins. Compactness therefore gives
\[
 \lambda_Q=\inf_Q
     \lambda_{\min}(-D_z^2\Re\Phi)>0.
 \tag{16}
\]
The real gradient vanishes at \(z_*\). Integration twice along
the segment from \(z_*\) to \(z\) gives
\[
 \Re\Phi(z)\le M_{n,p}-\frac{\lambda_Q}{2}|z-z_*|^2
 \le M_{n,p}
           -\frac{\lambda_Q}{2}(1/4-\xi_*)^2.
 \tag{17}
\]
The last quantity has a strict gap because \(\xi_*<1/4\).
Combine (17) with (10). This proves (12) with
\(\delta_{n,p,\varepsilon}
 =\lambda_Q(1/4-\xi_*)^2/2\).
Fixed derivatives and bounded-volume integration preserve the
exponential gap. \(\square\)

This proposition concerns the original double-pole density on a
specified horizontal part. The
[exact support-cell construction](research_pair_regular_support_cells.md)
also has vertical factorial-wall currents and shared-face row
insertions. Its reduced-pole representation includes additional
observation terms. None of those pieces is included in (12).
In particular the proposition does not justify taking separate
absolute values of the three shared-face insertion terms or
discarding a wall because the adjoining horizontal part has a gap.

## 4. The closed wall and a fixed reflected width

We now replace the strict regularity margin in (5) by zero and
allow both signs of each trace angle. Let \(\mathcal R_0^+\)
have the fixed heights \(Y,H_1,H_2\) and
\[
 1/4\le\xi\le12/25,\qquad
              |\tau|,|\rho|\le\pi-2\pi\xi.
 \tag{18}
\]
Let \(\mathcal R_0^-\) have the same trace variables and wire
height \(-Y\). The finite factorial bound, not a relative Stirling
expansion at a zero, will be used on their walls.

**Lemma 2.** There is \(\delta_0>0\), depending on the fixed pair,
such that the original real upper exponents on both sets obey
\[
                  \mathcal E\le M_{n,p}-\delta_0.
 \tag{19}
\]
Here, for \(x=\xi+iy,\ t=\tau-ih_1,\ r=\rho-ih_2\),
\[
 \begin{split}
 \mathcal E(x,t,r)={}&
  \mathfrak b(x,t)+\mathfrak b(x,r)+\Re\Psi(t)+\Re\Psi(r)\\
 &+\frac{n\tau h_1+p\rho h_2}{2\pi}
       -h_1-h_2-2\pi(-y)_+,
 \end{split}
 \tag{20}
\]
and \(\mathfrak b\) is the continuous real upper exponent of the
[uniform reciprocal-factorial theorem](research_uniform_factorial_and_boundary_decay.md#3-the-exact-newton-interpolation).

*Proof for the upper wire.* In coordinates (13), the right-hand
set (18) has \(\xi\le b_i\le1-\xi\). Its convex hull \(Q_0\)
with \(z_*\) therefore satisfies
\[
 \alpha(Y)<\xi<1/2,\qquad b_i>\alpha(S_i),\qquad
 0\le b_i-\xi\le1/2,\quad b_i+\xi\le1,\quad 0<b_i<1.
\]
The bounds away from \(\alpha(Y),\alpha(S_i),0,1\) have positive
margins. At the saddle the remaining inequalities are strict.
A point with \(b_i=\xi\) must belong to the endpoint set (18):
the saddle has \(b_{i,*}-\xi_*>0\), so a convex combination with
positive saddle weight cannot have equality. Thus any added wall
has \(\xi\ge1/4\), and \(b_i+\xi\ge1/2\).

Use \(u_i,v_i,w,d_i\) as in the Hessian proof, and put
\[
 \mu=\min_{i=1,2}\inf_{Q_0}
               \min\{w-(u_i)_+,\,d_i-(u_i)_+\}>0.
 \tag{21}
\]
The Hessian identity used in Section 3 remains valid here:
its factorial arguments have real parts in \((0,1)\) in the
interior, although \(b_i\) may exceed \(1/2\). If \(u_i>0\),
then \(b_i+\xi<1/2\), hence \(b_i<1/2\), and the original
mixed-concavity comparison still gives \(u_i<w,d_i\).
If \(b_i+\xi\ge1/2\), then \(u_i\le0\); also \(w,d_i>0\)
because \(0<\xi<1/2\) and \(0<b_i<1\).
These signs include \(b_i>1/2\), corresponding to a negative
real trace angle.

The expressions in (21) are continuous on \(Q_0\).
On the new walls \(b_i=\xi\), \(b_i-\xi=1/2\), or
\(b_i+\xi=1\), one still has \(u_i\le0\) and \(w,d_i>0\).
No singularity of \(u_i,w,d_i\) occurs on this compact set;
in particular \(\Im(s_i+x)=S_i+Y>0\).
This proves the strict infimum in (21).

The quantity \(v_i=\Re\cot\pi(s_i-x)\) is nonnegative in the
regular interior. It can diverge as a wall is approached, but
only in a positive semidefinite rank-one part of the negative
Hessian. Discarding that part gives the uniform lower bound
from (21). Integrate this bound along the segment from \(z_*\)
to a point of (18), stopping short of its endpoint if necessary:
\[
 \Re\Phi(z)\le M_{n,p}
 -\pi\mu\{2(\xi-\xi_*)^2+(b_1-b_{1,*})^2+(b_2-b_{2,*})^2\}.
 \tag{22}
\]
The primitive \(J\) is continuous at zero, so passage to the
closed endpoint is legitimate even when \(s_i-x=0\).
On the closed regular chart \(\mathfrak b=\Re b\) by this same
continuous limit. Consequently (19) holds on \(\mathcal R_0^+\)
with
\[
                    \delta_0=2\pi\mu(1/4-\xi_*)^2>0.
 \tag{23}
\]

*Proof for the lower wire.* On a strict regular point of (18),
both trace real parts have absolute value less than \(\pi/2\). The
[regular-chamber reflection bound](research_internal_pair_wire_alias_reflection.md)
gives, for each trace factor,
\[
 \Re b(\xi-iY,t)-\Re b(\xi+iY,t)\le\pi Y,
 \tag{24}
\]
and the analogous inequality at \(r\). This is the integrated
bound \(D_t'(s)<\pi\); a non-strict inequality suffices here.
Continuity extends (24) to the closed regular walls, including
\(\xi=1/4,\ \tau=\pm\pi/2\), and to a vanishing factorial argument.
The two losses in (24) sum to at most \(2\pi Y\). They are
cancelled by the exact lower-wire Fourier penalty, the last term
of (20). All other terms of (20) are identical at the two wire
heights. Thus
\(\mathcal E(\xi-iY,t,r)\le\mathcal E(\xi+iY,t,r)\), proving
(19) on \(\mathcal R_0^-\). No strict alias gap is needed.
\(\square\)

**Theorem 3.** There are fixed numbers \(\epsilon_0,\delta>0\)
such that the original density (4), through both parities, satisfies
\[
                  |\mathcal I_N(x,t,r)|
                       \le CN^A e^{N(M_{n,p}-\delta)}
 \tag{25}
\]
on both of the following tubes, indexed by \(\sigma=\pm1\):
\[
 \begin{gathered}
 1/4-\epsilon_0\le\xi\le12/25+\epsilon_0,\qquad
                 |y-\sigma Y|\le\epsilon_0,\\
 |h_i-H_i|\le\epsilon_0\quad(i=1,2),\\
 |\tau|,|\rho|\le\pi-2\pi\xi+\epsilon_0.
 \end{gathered}
 \tag{26}
\]
Here \(x=\xi+iy,\ t=\tau-ih_1,\ r=\rho-ih_2\).
On tubes of half this width, all fixed \(x,t,r\) derivatives and
ordinary selected-color normals obey the same exponential bound.

*Proof.* On a compact neighborhood of the two sets in Lemma 2,
the real upper exponent (20) is continuous. This assertion
includes a factorial crossing zero or the negative real axis:
the exact reciprocal identity retains both cosine terms, and its
upper exponent is \(-\Re J_{\rm side}\), with the equal real
boundary values on the cut. Near zero \(z\log z\) tends to zero.
The [uniform factorial bound](research_uniform_factorial_and_boundary_decay.md)
therefore applies without removing a moving zero or choosing a
new principal branch.

For sufficiently small \(\epsilon_0\), (26) stays in that compact
neighborhood. The distance to the corresponding set (18) tends
uniformly to zero with \(\epsilon_0\): clamp \(\xi\) to
\([1/4,12/25]\), then clamp each trace real part to its regular
interval. The required changes are at most a fixed multiple of
\(\epsilon_0\). Uniform continuity and (19) imply
\[
                     \sup_{\text{both tubes}}\mathcal E
                                  \le M_{n,p}-\delta_0/2.
 \tag{27}
\]
Choose \(\epsilon_0<\min(Y,H_1,H_2)/2\). The trace denominators
then stay uniformly away from zero, and the wire factor has the
actual bound
\[
 \left|\frac1{1-e^{2\pi iNx}}\right|
                 \le C e^{-2\pi N(-y)_+}.
 \tag{28}
\]
The full complete kernels satisfy (8) on these slightly enlarged
sets. For the negative real angles this follows from
\[
 K_N(-\overline t,0)=\overline{K_N(t,0)},\qquad
             \Psi(-\overline t)=\overline{\Psi(t)},
\]
using evenness and the real coefficients of the original kernel.
Thus the logarithmic upper bound and its derivative bounds hold
on a fixed complex neighborhood of the reflected rectangle as
well. The larger neighborhood statement supplies the small
additional widths in (26).
The exact reciprocal-factorial theorem supplies
\(|B_N|\le CN^{-1}e^{N\mathfrak b}\) throughout both tubes,
including the fixed small reflected width. The remaining factors
in (4) are bounded precisely by the other terms in (20), up to
powers of \(N\). Equations (27)–(28) prove (25), for example with
\(\delta=\delta_0/2\).

The original density is holomorphic on a neighborhood of the
inner tubes: reciprocal factorial zeros are zeros, and the
rational trace and wire denominators cannot vanish at the
specified heights. A polydisk of fixed radius, depending only
on \(\epsilon_0\), around each inner point lies in the outer
tube. Cauchy's formula proves the derivative statements using
(25). Conversion to ordinary selected colors remains bounded
by (11), with \(H_i\) replaced by \(H_i/2\).
\(\square\)

This is a fixed-width estimate, not a statement whose margin
shrinks with the level. In particular, split \([1/4,12/25]\)
into finitely many intervals of length less than
\(\epsilon_0/(8\pi)\). On a block \([a,b]\), a single angular
pair of cuts \(\pm T\), \(T=\pi-2\pi a\), with their physical
midpoint adjustments \(T_N=T+O(N^{-1})\), lies within (26) throughout the block,
for all sufficiently large levels. Both horizontal wire sides
and all four trace-angle quadrants, with small height
perturbations, then have the same gap. The
literal \(O(N^{-1})\) regular-support wall is included.

The theorem does not estimate a vertical wire side running from
\(-Y\) to \(Y\), or a trace connector running from height zero to
\(H_i\). It also does not identify the double-pole density with
the separate observation or row-insertion terms of a reduced-pole
cell representation. Those pieces must still be grouped or
bounded within their own exact contour identities.
