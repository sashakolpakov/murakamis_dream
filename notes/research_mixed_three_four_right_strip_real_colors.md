# Real ordinary colors on the completed three/four right strip

Research deduction, 7 November 2026. The completed fixed-height
right-strip estimate holds uniformly for both real ordinary boundary
colors. Its proof uses the original whole-coefficient color estimates
before contour deformation, together with the exact physical support.
A fixed portion of the strip gap can then be retained while paying
a strict angular loss at either endpoint.

No far-color critical point, continuation of a small color disk to
the full period, or comparison with the modulus of a canceled
complete-color value is used. No numerical evaluation is needed.

## 1. Exact source and the two color estimates

Retain the source, actual reference, height and scalar of
[the complete moving-cut theorem](research_mixed_three_four_moving_transform_cut.md):
\[
 \begin{gathered}
 a_*=A+ic,\quad a=x+ic,\quad 9/20\le x\le1/2,\\
 M=\Re\{T_0(a_*)+P_1(a_*)\},\quad p=\Re P_1'(a_*),\\
 B_U(x)=\Re T_0(a_*)-p(x-A)-\kappa_*(x-A)^2,\qquad
                    \kappa_*=\frac1{2500000},\\
 Z_{34,N}(w_L,w_R)=\kappa_N^3N^2
       \oint U_{0,N}(w_L,X)V_{1,N}(w_R,X)\frac{dX}{2\pi iX}.
 \end{gathered}
\tag{1}
\]
Only the indicated incoming strip is estimated here. Put
\(D(\theta)=1-\cos\theta\), \(w=-2\cos\theta\).

The complete first-cap theorem already gives, for some \(c_L>0\),
every tolerance \(\tau>0\), and every real \(\theta_L\),
\[
 |U_{0,N}(-2\cos\theta_L,e^{-2\pi ia})|
 \le C_\tau N^{B_\tau}
       e^{N\{B_U(x)-c_LD(\theta_L)+\tau\}} .
\tag{2}
\]
This is equation (11) of
[upper-target cap completion](research_mixed_cap_upper_target_completion.md),
with own type three. It includes all original cap currents,
physical tails, true private-index ends and fixed ordinary
derivatives. It is valid on \([.22,.5]\), so its use on (1)
does not enlarge the target domain.

For the right endpoint coefficient,
[real-color endpoint decay](research_mixed_endpoint_real_color_decay.md),
Theorem 1, proves the exact-source bounds
\[
 \begin{split}
 |C_N(e,-2\cos\theta_R)|
 &\le C N^B
       e^{N\{\Re S(e)-c_E D(\theta_R)\}},
       &&e\in E_c=[.27,.49]+i[-.055,.04],\\
 |H_N(-2\cos\theta_R,r^{-j})|
 &\le C_I N^{B_I}e^{Nh(j/N)},
       &&j/N\in I\Subset(0,1),\\
 h(e)&=J(e)+\Re S(e).
 \end{split}
\tag{3}
\]
The second bound drops a favorable angular loss. Both statements
hold for the whole original coefficients and all real colors, with
their original fixed-derivative versions. The first bound also
holds on a fixed neighborhood of \(E_c\). It includes revived
Newton rows and is not an estimate for a single saddle term.

## 2. The original all-color physical endpoint bounds suffice

The exact terminal square source is
\[
 V_{1,N}(w,X)=
 \sum_{i,j<N}\frac{X^{-i}p_i(X)}{P_i^2}
           \frac{p_j(r^i)H_N(w,r^{-j})}{P_j^2}.
\tag{4}
\]
Its physical terms with \(i+j\ge N\) vanish at every color.
The real-color Newton bounds are
\[
 V_\theta(u)\le V_0(u)\quad(0\le u\le1/2),\qquad
 V_\theta(u)\le0\quad(1/2\le u\le1),\qquad
                  \max_u V_\theta(u)<3/5 .
\tag{5}
\]
The upper-half complete-color Newton entropy is not used as a
majorant for other colors.

The following are the explicit finite-source consequences in
Section 2 of
[terminal real-color decay](research_mixed_terminal_real_color_decay.md).

First, the whole coherent cap seam ceilings \(101/125,433/500\)
remain valid for every real color. On compact physical private
indices this follows from (3); at both private ends the original
reflected-factorial estimates use only (5). The same zero-safe
small outgoing collar product estimate therefore retains its old
cost \(\Delta_\delta\).

Consequently the terminal true transform ends retain the upper
rate \(217/250\), with an arbitrarily small common tolerance.
For the lower transform end, each removed \(i\)-row includes its
whole cap, private sum and Newton sum. For the upper end the
actual support forces \(j/N<1-i/N\) and every Newton index
\(l/N\le j/N\) below one half. Its original absolute entropy tends
uniformly to zero there. The incoming coefficient has the same
continuous rate \(\chi_1(t,a)\), with
\[
              \chi_1(0,a)=0,\qquad
              \chi_1(1,a)=2\pi(-c)_+ .
\tag{6}
\]
These endpoint statements extend to (1) for exactly the reason
given in Lemma 1 of
[the right-strip physical-complement theorem](research_mixed_three_four_right_strip_physical_complement.md):
their dependence on the incoming parameter is only a uniform
zero-safe product bound on a fixed compact annulus, with (6).
No angle restriction \(x\le.45\) is used in that step.
The coupled endpoint calibration and its fixed positive gap
are thus unchanged for all real right colors.

Second, for every fixed \(\delta,\epsilon>0\), the same original
source gives
\[
 |H_N(-2\cos\theta_R,r^{-j})|
 \le C_{\delta,\epsilon}N^{B_{\delta,\epsilon}}
       e^{N\{h(j/N)+\epsilon\}},
                    \qquad 0\le j/N\le1-\delta .
\tag{7}
\]
This is equation (8) of the terminal real-color theorem.
Near physical \(j=0\), its proof uses the whole finite Newton
entropy on \(0\le l\le j\), which tends uniformly to zero,
and \(h(0)=0\); on the closed remaining interval it uses (3).
There is no all-color claim for an off-grid endpoint collar
near \(j/N=1\).

That missing collar is unnecessary. Choose a fixed
\(0<\delta<.01\) for the true transform ends, and remove the
complete \(i\le\lfloor N\delta\rfloor\) rows first.
Set \(i_{\min}=\lfloor N\delta\rfloor+1\).
For every remaining physical \(i\), the entire columns
\[
                         j\ge N-i_{\min}
\tag{8}
\]
vanish. Delete these columns before moving any contour.
Every retained physical private index has \(j/N<1-\delta\),
so (7) covers it. Within each retained column keep
\(p_j(e^{-2\pi it})\) literal when \(t\) becomes complex.
Its row-dependent physical zeros may revive off grid;
they are neither deleted nor set to zero there.
The central private rectangle is unaffected by (8) for large \(N\).

This is the original all-color column deletion, and it commutes
with the moving transform cutoff: \(i_{\min}\) is fixed before
the incoming-dependent central partition is made.

## 3. The complete moving-cut partition keeps its calibrated upper rates

**Proposition 1.** There is \(\gamma_0>0\) such that the unchanged
whole terminal source satisfies
\[
 |V_{1,N}(-2\cos\theta_R,e^{-2\pi ia})|
 \le C N^B e^{N\{M-B_U(x)-\gamma_0\}}
\tag{9}
\]
uniformly on (1), for every real \(\theta_R\), both parities
and every fixed ordinary-color derivative, with the corresponding
polynomial prefactor.

*Proof.* This conclusion is obtained from the terminal source
pieces, not by dividing the product estimate by \(U_{0,N}\).
Each calibrated rate inequality in the moving-cut proof has the
form \(B_U(x)+\rho(x)\le M-\delta_\rho\), where \(\rho\) is
an upper rate for an explicitly retained terminal piece.
All \(\delta_\rho\) are strictly positive and uniform.

For the central private contour the exact interpolant remains
\[
 e^{2\pi iNat}\Pi_N(a+t)\Pi_N(e+t)
 E_N(a)E_N(t)^3E_N(e)\Delta_N(e)^{-1}C_N(e,w_R).
\tag{10}
\]
Insert the first bound of (3) before estimating any current,
and, if desired, drop its favorable angular loss. Every other
factor is color independent. Thus the same complete-color
phase upper is valid on the old rectangle and on the added strip
\(.1\le\Re t\le.15\). It applies to the shifted main,
both kinds of joins, every single and double alias, and their
half-grid sides. The moving real cut \(t=.6-x\), its original
calibrated start, the positive transform force and both height
convexities are inequalities for this same upper phase.
No far-color stationary equation is used.

The original numerator \(a+t=1\) is treated with the same
zero-safe quarter-level shift. Its factors are color independent,
so the all-color endpoint estimate in (3) passes through that
corner without modification.

For physical private columns outside \(E_c\), use (7) on
the retained columns after (8). Their upper rate is precisely
the complete-endpoint rate used in the physical-complement theorem.
The private-tail and small-transform monotonicities therefore
transport it to the same calibrated real anchors. In the hybrid
partition, the private-exterior rows below \(t=.15\) stay real;
the private-exterior central rows keep their old transform contour.
Only the central-private sector uses the new moving cut.
No new private-tail continuation or raw Newton maximum is introduced.

For the upper physical transform triangle, its exact support has
\(0\le l/N\le j/N<1-i/N\le1/2\).
The first inequality in (5) preserves each original positive
triple-row majorant. Its entropy reduction and coupled \(Q\)-transport
therefore retain their strict gap throughout (1), including the
even half-row. The true transform ends were handled above.

These are all pieces of the exact moving-cut partition. Choose
the common tolerances in (7), the product bounds and the endpoint
ceilings below a fixed portion of the minimum of their calibrated
reserves. The residue powers, physical row counts and contour
lengths cost polynomial factors. This proves (9).

The whole terminal polynomial has degree at most \(N-1\) in \(w_R\).
Since (9) is now proved on the full real interval \([-2,2]\),
the polynomial Markov inequality gives the same uniform upper
exponent for each fixed ordinary derivative, with cost
\(C_kN^{2k}\). For complex coefficients, rotate each derivative
value and apply the real-polynomial inequality to its real part.
This derivative step uses a whole real-color bound, not a local
complex-color disk. \(\square\)

Equation (9) is a calibrated upper ceiling for the unchanged
finite source. It does not identify \(M-B_U(x)\) with a new
terminal critical action or assert monotonicity in its actual color.

## 4. A surviving strip gap and losses at both ordinary endpoints

**Theorem 2.** There are \(c_L,c_R,\gamma>0\) such that for all
real \(\theta_L,\theta_R\), both parities, and (1),
\[
 \begin{split}
 &|U_{0,N}(-2\cos\theta_L,e^{-2\pi ia})
      V_{1,N}(-2\cos\theta_R,e^{-2\pi ia})|\\
 &\qquad\le C N^B
 e^{N\{M-\gamma-c_LD(\theta_L)-c_RD(\theta_R)\}} .
 \end{split}
\tag{11}
\]
Every fixed mixed ordinary-color derivative obeys the same rate,
with a possibly different polynomial prefactor.

*Proof.* Keep \(c_L\) from (2), and take its tolerance
\(\tau=\gamma_0/4\), where \(\gamma_0\) is from (9).
Multiplication gives the stronger color-independent-in-\(\theta_R\)
ceiling
\[
          C N^B e^{N\{M-3\gamma_0/4-c_LD(\theta_L)\}} .
\]
Because \(0\le D(\theta_R)\le2\), choose
\(\gamma=c_R=\gamma_0/4\). This proves (11).
The fixed derivatives follow from the derivative versions of
(2) and (9); each color occurs in only its original factor.
No finite value is divided out. \(\square\)

The right-end angular loss in this deduction is paid by part of
an already strict source-region gap. It does not assert that a
true private-end row separately has an angular loss, nor that
the right source is largest at complete color. The left loss is
the existing full-cap angular estimate. Thus the reusable principle
is to lift every retained upper profile to all real colors first,
retain the independent endpoint ceilings, and only then spend
a fixed regional reserve.

The original scalar \(\kappa_N^3N^2\), both ordinary boundaries,
all normals and exact support walls are unchanged. Equation (11)
covers only the added fixed-height strip. The remaining incoming
circle, height-changing connectors, attachment estimates and
noncancellation of the whole ordinary two-boundary kernel remain
separate obligations.

