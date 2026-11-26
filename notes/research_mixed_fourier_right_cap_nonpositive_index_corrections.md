# Paid nonpositive index corrections on the right outgoing arc

Research deduction, 7 November 2026. Over the already controlled
right outgoing arc, the lower retained-index alias and every
nonpositive-height retained-index boundary piece have a strict
gap below the original plane. The outgoing variable stays on its
original negative critical height. The exact joint interpolation,
half-grid cuts and full alias denominators are retained.

The upper retained-index corrections, the left outgoing arc and
the separate outgoing vertical current are not bounded here.
No numerical evaluation is used.

## 1. Source, phases and unchanged reference plane

Keep the exact \(T_N\) of
[the joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md),
equation (10), and the actual reference of
[the complete bare inner-source theorem](research_mixed_fourier_right_cap_bare_inner_completion.md).
Write
\[
 \begin{gathered}
 \eta\in\{0,1\},\quad
 a=x+i h_a,\quad x\in P=[11/50,9/20],\\
 s=u+i v,\quad 1/8\le u\le1/2,\quad -1/5\le v\le0,\\
 q=z+i h_q,\quad 9/20\le z\le1,\quad
 h_s=\Im s_*,\quad h_q=\Im q_*,
 \qquad -.102\le h_s,h_q\le-.001 .
 \end{gathered}
 \tag{1}
\]
The incoming height and allocation are original; if \(\eta=1\)
the height is negative and unselected.
The allocated phase is
\[
 \mathscr F_\eta=
 g(s+a)+g_-(s+q)-3g(s)
 -(1+\eta/2)g(a)-g_-(q)+2\pi ias+\ell_q(y).
 \tag{2}
\]
Here \(g_-\) is the original lower-half-plane disk branch from
[the right-main comparison](research_mixed_fourier_right_cap_upper_main_arc.md).
For \(s\) itself, its original regular-strip primitive extends
continuously to \(v=0\). All other arguments in (2) have the
same regularity as in that comparison; in particular
\(\Im(s+q)<0\) throughout (1).

Use
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                              -\kappa(x-\Re a_*)^2,
 \qquad \kappa=1/2500000.
 \tag{3}
\]
There is no new action constant or marginal.

## 2. A lower-alias comparison on the whole outgoing half-plane

The following derivative estimate is not restricted to the right
arc. It also applies to every outgoing real coordinate whenever
\(\Im q\le0\), with boundary values interpreted continuously
where a \(q\)-only term has an integrable logarithmic endpoint.
Only the \(s\) derivative is used.

**Lemma 1.** If \(1/8\le u\le1/2\), \(-1/5\le v<0\),
\(a_R\in P\), and \(\Im q\le0\), then
\[
                    \Im\mathscr F_{\eta,s}<7\pi/5.
 \tag{4}
\]

*Proof.* The exact derivative is
\[
 \mathscr F_{\eta,s}
        =g'(s+a)+g_-'(s+q)-3g'(s)+2\pi ia .
 \tag{5}
\]
Because \(\Im(s+q)<0\), its disk logarithm satisfies
\(\Im g_-'(s+q)<\pi/2\), independently of its real part.
Also \(v<0\) and \(u\le1/2\) give
\(\Im g'(s)\ge0\).

The original regular argument \(s+a\) has real part in
\([.345,.95]\). At every finite height the original argument
bound gives
\[
 \Im\{g'(s+a)+2\pi ia\}
 \le
 \begin{cases}
 \pi(1-2u),&u+x\le1/2,\\
 2\pi x,&u+x\ge1/2 .
 \end{cases}
 \tag{6}
\]
The first bound is at most \(3\pi/4\), and the second at
most \(9\pi/10\). Combining the three terms in (5) proves
(4). The limits at \(v=0\) needed below follow by continuity.
\(\square\)

Fix all real coordinates and define
\(W(v)=\Re\mathscr F_\eta(u+iv,a,q)+2\pi v\).
Equation (4) gives \(W'(v)>3\pi/5\). Consequently
\[
 \begin{split}
 \Re\mathscr F_\eta(u-i/5,a,q)-2\pi/5
 &<\Re\mathscr F_\eta(u+i h_s,a,q)
                 +\frac{7\pi}{5}h_s-\frac{3\pi}{25}\\
 &<\Re\mathscr F_\eta(u+i h_s,a,q)-\frac{3\pi}{25}.
 \end{split}
 \tag{7}
\]
This pays the lower alias relative to the same outgoing point
of the critical-index sheet. It does not assert that that
sheet is already bounded on the left outgoing arc.

The same integration to height zero gives the useful real-cut
comparison
\[
 \Re\mathscr F_\eta(c+iv,a,q)+2\pi v
       \le\Re\mathscr F_\eta(c,a,q)+\frac{3\pi}{5}v
       \le\Re\mathscr F_\eta(c,a,q),
 \quad -1/5\le v\le0,
 \tag{8}
\]
for \(c=1/8\) or \(1/2\). The Fourier penalty is present
in (8); it is not assigned to an unpenalized joining segment.

## 3. Transporting the actual cut and join estimates to the right

Both outgoing comparisons in the right-main note hold at
every fixed nonpositive index height, not just at \(h_s\).
Their proofs use only \(0\le\Re s\le1/2\) and
\(|e^{-2\pi is}|\le1\). Hence, on (1),
\[
 \begin{split}
 \Re\mathscr F_{\eta,q}&<-1/10
                               &&(9/20\le z\le3/4),\\
 \Re\mathscr F_\eta(s,a,q)
 &<\Re\mathscr F_\eta(s,a,q-1/2)-1/200
                               &&(3/4\le z\le1).
 \end{split}
 \tag{9}
\]
The first assertion follows from
\(\rho|1-SQ|/(|1-Q||1-YQ|)<9/10\).
For the second, the two incident factorials stay together in
the \(G(s+q)-G(q)\) comparison, with the same two heights.
Its proof explicitly allows \(\Im s=0\).
Any Fourier debit depending on \(v\) is unchanged under (9).

The completed bare-source theorem gives, on \(q_R\in P\),
the two original real-cut inequalities
\[
 \Re\mathscr F_\eta(c,a,z+i h_q)
       <B_\eta(x)-1/35000,\qquad c=1/8,\ 1/2 .
 \tag{10}
\]
These are its individual row comparisons, not an inference
from the modulus of a canceled sum.
Using (9), first from \(z=9/20\) and then by a half-period
shift, extends (10) to every \(9/20\le z\le1\).
For the shifted targets in \([1/4,9/20]\) use (10)
directly; those in \([9/20,1/2]\) use its first extension.

On the original \(P\) targets, the negative-index joining
segment \(h_s\le v\le0\) has vertical convexity from
the bare inner-contour Hessian. It is bounded by the
maximum of its critical-height value and its real-cut value.
At a critical-height cut the old full sheet estimate gives
\[
 \Re\mathscr F_\eta(c+i h_s,a,z+i h_q)
       \le B_\eta(x)-\kappa(c-\Re s_*)^2 .
 \tag{11}
\]
The actual \(O_4\) image satisfies \(.24\le\Re s_*\le.36\),
so both cuts have distance at least \(23/200\) from it.
Put
\[
                  \delta_s=\kappa(23/200)^2<1/35000.
 \tag{12}
\]
Equations (10)--(11) and vertical convexity yield
\[
 \Re\mathscr F_\eta(c+iv,a,z+i h_q)
     \le B_\eta(x)-\delta_s
              \quad(h_s\le v\le0,\ z\in P).
 \tag{13}
\]
Transporting each unchanged profile by (9) extends (13)
to all \(9/20\le z\le1\). This argument does not assert
joint convexity on the enlarged outgoing interval.

Thus, over that whole right outgoing arc, the real cuts
are paid by (10), the unpenalized negative-height joins
by (13), and the lower vertical aliases by (8) and (10).
The lower horizontal alias is paid by (7) and the completed
right critical-sheet estimate, with reserve \(3\pi/25\).

## 4. The literal correction currents

Let \(\sigma_\pm\) and \(\beta_N\) be the original half-grid
cuts from the joint global chart. In the exact retained-index
decomposition over the outgoing zero-mode path
\(q=z+i h_q\), \(9/20\le z\le\beta_N\), retain the complete
lower horizontal correction
\[
 \mathcal L_N^{\rm right}
 =N^2\int_{9/20}^{\beta_N}\int_{\sigma_-}^{\sigma_+}
 T_N(u-i/5,z+i h_q;a,y)
 \frac{e^{-2\pi iN(u-i/5)}}{1-e^{-2\pi iN(u-i/5)}}\,du\,dz .
 \tag{14}
\]
Also retain the nonpositive part of its signed vertical group,
\[
 \begin{split}
 \mathcal B_{N,-}^{\rm right}
 =iN^2\int_{9/20}^{\beta_N}\int_{-1/5}^{0}
 w_{N,h_s}(v)
 \{T_N(\sigma_++iv,z+i h_q;a,y)
                  -T_N(\sigma_-+iv,z+i h_q;a,y)\}\,dv\,dz,\\
 w_{N,h_s}(v)=\frac1{1+e^{2\pi Nv}}
                         -\boldsymbol1_{\{v<h_s\}} .
 \end{split}
 \tag{15}
\]
The value at the single indicator jump is irrelevant.
For \(v<h_s\), \(|w_{N,h_s}(v)|\le e^{2\pi Nv}\);
for \(h_s<v\le0\), its modulus is at most one.
These are exactly the two debits used above.

The lower-half-plane symbol across the numerator support
wall, together with the old regular-strip symbol near the
real \(s\) cuts, is uniform on all compact contours
(14)--(15). In particular it retains the row power
\(N^{-5/2}\), the original cardinal coefficient and the
two zero-mode coefficients \(N^2\). The incoming finite
halfweight remains outside the integrals and uses its
unchanged original bound. The \(O(1/N)\) half-grid shifts
cost only a uniform finite prefactor; all relevant
derivatives are bounded on a nearby compact set.

For every prescribed \(\tau>0\), it follows that
\[
 \begin{split}
 |d_N(e^{-2\pi ia})|^{\eta/2}|\mathcal L_N^{\rm right}|
     &\le C_\tau N^{A_\tau}
             e^{N(B_\eta(x)-3\pi/25+\tau)},\\
 |d_N(e^{-2\pi ia})|^{\eta/2}|\mathcal B_{N,-}^{\rm right}|
     &\le C_\tau N^{A_\tau}
             e^{N(B_\eta(x)-\delta_s+\tau)} .
 \end{split}
 \tag{16}
\]
Both parity cuts and every displayed denominator are retained.
The proof bounds the two vertical orientations absolutely
only after preserving their exact source expressions.

No positive-height retained-index alias or joining piece
is included in (16). Nor does the argument deform the
separate outgoing vertical source into these expressions.
Those terms retain their original boundaries and zeros.
The general relative comparison (7) can be used on a
nonpositive outgoing contour once that contour's main
phase has its own bound; it supplies no such bound by itself.
