# Complete conditional source at every nonnegative critical height

Research deduction, 8 November 2026. The half-index contour works
throughout the displaced incoming rectangle whenever the selected
conditional critical height is nonnegative. Its upper connector does
not require the critical point to lie below the incoming zero line.
The exact two-branch upper envelope decreases to that line and increases
after it, so its two already-paid endpoints control the whole connector.

Only a fixed prewall neighborhood of the actual saddle uses a nonzero
factorial symbol. The remaining main path uses uniform zero-safe upper
bounds, including when its incoming numerator lies on the positive
real cut. Every literal physical row, alias and unweighted connector
is retained. Earlier frozen notes are unchanged; no numerical evaluation
is used.

## 1. Original finite function and theorem

Use precisely
\[
\begin{gathered}
a=x-i\eta,\quad \tfrac12\le x\le\tfrac7{10},\quad
0\le\eta\le\tfrac9{125},\qquad
y=z+iH,\quad\tfrac{11}{50}\le z\le\tfrac9{20},\quad
0\le H\le\tfrac1{100},\\
X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad r=e^{-2\pi i/N},
\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
C_{1,N}(X,Y)=\sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
\end{gathered}                                                     \tag{1}
\]
Write \(\mathcal D\) for this compact parameter set. The original
phase, stationary value and selected branch are
\[
\begin{split}
Q(s;a,y)&=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,\\
Q_s(s_*;a,y)&=0,\qquad
s_*=u_*+ih_*,\qquad \Theta(a,y)=Q(s_*;a,y).
\end{split}                                                       \tag{2}
\]
All logarithmic lifts and additive constants are unchanged.
The [negative-height branch theorem](research_mixed_conditional_negative_height_branch.md)
and [height-action monotonicity](research_mixed_conditional_height_action_monotonicity.md)
prove
\[
\begin{gathered}
\tfrac1{16}<u_*<1-x,\quad
\tfrac25<|e^{2\pi is_*}|<2,\quad \Re\Theta>13/24,\\
-\Re Q_{ss}(t+i\sigma;a,y)>0
\quad\left(\tfrac3{50}\le t<1-x,\ \sigma\in\mathbb R\right).
\end{gathered}                                                     \tag{3}
\]
The branch is simple and has fixed holomorphic neighborhoods.
Its prewall distances have positive minima on \(\mathcal D\).
For \(h_*\ge0\), the
[explicit positive-height guards](research_mixed_conditional_positive_height_critical_guards.md)
also give \(u_*<3/10\) and \(1-x-u_*>3/40\).

**Theorem 1.** On a fixed open complex neighborhood of the compact set
\[
                  \mathcal D_+=\{(a,y)\in\mathcal D:h_*\ge0\},
                                                                    \tag{4}
\]
the complete original function has
\[
 C_{1,N}(X,Y)=N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                         (1+O_{\rm hol}(N^{-1})),\qquad
                         \mathcal B(a,y)\ne0.                    \tag{5}
\]
Both level parities and all fixed mixed derivatives of the normalized
error are included on smaller fixed neighborhoods. The coefficient is
the original Gaussian symbol in (20). No assumption on the sign of
\(h_*-\eta\), or on the real wall-action gap, is made.

## 2. One exact interpolation and its continuous upper envelope

Keep the original marked factorial \(\Pi_N\), its reciprocal \(E_N\),
and the literal row interpolation
\[
 T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                          E_N(a)E_N(y)E_N(s)^3.                 \tag{6}
\]
At \(s=j/N\) this is exactly the summand in (1). The
[global chart theorem](research_mixed_fourier_right_cap_joint_global_chart.md)
proves its holomorphy through the first positive numerator wall.
No shifted meromorphic chart is substituted for (6).

We need its upper rate, not a nonvanishing approximation on that wall.
Let \(g\) have its original strip branch, with its continuous boundary
values, and define for \(0<\Re q\le6/5\)
\[
 \mathfrak p(q)=
 \begin{cases}
       \Re g(q),&0<\Re q\le1,\\
       \Re g(q-1)+2\pi(\Im q)_+,&1\le\Re q\le6/5 .
 \end{cases}                                                    \tag{7}
\]
The two definitions agree on their common boundary. More explicitly,
\[
 \Re g(1+i\sigma)=\Re g(i\sigma)+2\pi\sigma_+
                         \qquad(\sigma\in\mathbb R).            \tag{8}
\]
For \(\sigma<0\), the proved lower-half-plane phase is periodic.
For \(\sigma>0\), the exact identity
\[
             \Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q)               \tag{9}
\]
and the anchored upper-half factorial asymptotic give the additional
real rate \(2\pi\sigma\). The real endpoint values in (8) are both
zero, so the identity extends continuously to \(\sigma=0\).
The branches and their constants are those in
[lower-half continuation](research_lower_half_factorial_continuation.md)
and [uniform half-plane continuation](research_factorial_uniform_halfplane_continuation.md).

Both terms of the multiplier in (9) are kept:
\[
             |1-e^{-2\pi iNq}|\le2e^{2\pi N(\Im q)_+}.
\]
The regular-strip bounds, the midpoint bound of
[uniform factorial estimates, Section 1](research_uniform_factorial_and_boundary_decay.md),
and its reciprocal bound in Section 2, equation (4), consequently give
the upper rate (7) uniformly through the real cut and every numerator
zero. From the prewall side use explicitly
\[
              G_N(Nq)=N/G_N(N(1-q)-1).
\]
The reciprocal midpoint argument is \(1-q-1/(2N)\); its estimate
includes both signs of its real part and its reciprocal zeros.
From the postwall side use (9) and the midpoint argument
\(q-1+1/(2N)\). The shifts of their continuous logarithmic primitives
cost \(O(\log N)\). These are the same zero-safe estimates established
in Section 2 of
[the half-cut theorem](research_mixed_conditional_half_cut_below_incoming_zero.md).
No division by the period factor or by a numerator zero is used.

For \(s=t+i\sigma\), \(3/50\le t\le1/2\), set
\[
 \widehat R(t,\sigma;a,y)
 =\mathfrak p(a+s)
  +\Re\{g(y+s)-3g(s)-g(a)-g(y)+2\pi ias\}.                     \tag{10}
\]
This is jointly continuous on the full bounded parameter and contour
sets, including \(x+t=1\) and \(\sigma=\eta\).
On the prewall part it is exactly \(\Re Q\). On the real path it is
the original continuous physical row rate, with its incoming chirp.
Uniformly on these sets, the original row satisfies
\[
 |T_N(s;a,y)|\le C_\tau N^{B_\tau}
                         e^{N(\widehat R(t,\sigma;a,y)+\tau)}
                                                                    \tag{11}
\]
for every fixed tolerance \(\tau>0\). The estimates also apply on
small fixed complex parameter neighborhoods, using the same continuous
rate construction. A full regular symbol is asserted only where its
actual factorial arguments are regular.

## 3. The whole main line has just the original maximum

The algebra in Sections 3--4 of the half-cut theorem is independent
of its additional condition \(h_*<\eta\).
For \(1-x\le t\le1/2\), \(\sigma\ge0\), put
\(U=e^{2\pi\sigma}\ge1\), \(T=e^{2\pi\eta}<8/5\),
\(R_y=e^{2\pi H}<8/7\). The two branches in (7) have the same real
horizontal derivative. Its exact force satisfies
\[
 \exp(2\partial_t\widehat R)
 =\frac{|T-Ue^{-2\pi i(x+t)}|^2
        |1-R_yUe^{-2\pi i(z+t)}|^2}
        {|1-Ue^{-2\pi it}|^6}
 \le
 \frac{(U^2-3U/5+64/25)(1+8U/7)^2}
        {(U^2+3U/5+1)^3}<1.                                  \tag{12}
\]
At a logarithmic zero the statement is read by integrating its
continuous primitive. The corrected polynomial witness in that
theorem gives the last strict inequality for every \(U\ge1\).
The extra rate \(2\pi(\sigma-\eta)_+\) is independent of \(t\),
so it does not change this horizontal force.

On the prewall part of the main line \(\sigma=h_*\), (3) gives a
unique nondegenerate maximum at \(s_*\). A fixed portion of the
segment strictly between \(u_*\) and \(1-x\) already has a uniform
strict loss. Equation (12) then makes the whole postwall rate
decrease further. Thus \(\widehat R(t,h_*)\) has the same unique
maximum \(\Re\Theta\) over the entire retained main interval.

Crucially, the saddle stays a fixed real distance before the wall.
A fixed small neighborhood of it uses the original regular
factorial expansion with nonzero symbol, even when \(h_*=\eta\).
Every remaining part of the main line has a uniform strict gap and
needs only (11). At \(h_*=\eta\), the incoming numerator on its
postwall part can meet all its original real zeros; those values
are retained and satisfy (11). No relative expansion is claimed
on that smaller-rate portion.

## 4. The half-cut connector has its maximum at its endpoints

This is the new comparison. At \(t=1/2\), write \(r_0=x-1/2\).
Then \(0\le r_0\le1/5\), and the own logarithmic argument is zero.
For \(0\le\sigma<\eta\), the original incoming argument is
nonnegative and the outgoing one is at least \(-2\pi z\).
Therefore
\[
             \partial_\sigma\widehat R(1/2,\sigma)
                       \le-2\pi(x-z)\le-\pi/10.                \tag{13}
\]
For \(\sigma>\eta\), the second branch of (7) instead gives
\[
 \begin{split}
 \partial_\sigma\widehat R(1/2,\sigma)
  ={}&-A(r_0+i(\sigma-\eta))
      -A(y+1/2+i\sigma)-2\pi x+2\pi\\
  &\ge-(\pi-2\pi r_0)-2\pi x+2\pi=0,
 \end{split}                                                     \tag{14}
\]
where \(A(q)=\Arg(1-e^{-2\pi iq})\) on the original strip.
Indeed \(A(r_0+i(\sigma-\eta))\le\pi-2\pi r_0\), while the
outgoing argument is nonpositive since \(1/2<z+1/2<1\).
When \(r_0=0\), use the one-sided limits of that argument.
At the separating line the exact rate (10) is continuous.
Its derivative can jump; no curvature or smoothness is asserted there.

Equations (13)--(14) prove that the half-cut rate decreases up to
\(\sigma=\eta\), then increases. If the connecting interval does
not reach \(\eta\), only its decreasing part is used. In every case,
\[
 \widehat R(1/2,\sigma)
 \le\max\{\widehat R(1/2,0),\widehat R(1/2,h_*)\}
                        \quad(0\le\sigma\le h_*).               \tag{15}
\]
This holds also for \(\eta=0\) and for \(h_*=\eta\).
There is no upper-branch term missing from (14): its \(+2\pi\)
is exactly the contribution of the full cyclotomic factor (9).

The real endpoint in (15) is paid by the
[full physical upper-half theorem](research_mixed_conditional_negative_height_upper_half.md).
The main endpoint is paid by Section 3. Both gaps are uniform
on the compact set \(\mathcal D_+\). Consequently (15) pays the
whole unweighted half-cut connector.

For the actual half-grid cut \(b_N\) below, use uniform continuity
of (10), not a pointwise derivative sign at a shifted kink:
\(\widehat R(b_N,\sigma)-\widehat R(1/2,\sigma)\to0\) uniformly
on the relevant compact sets. This preserves a fixed part of both
endpoint gaps for all large \(N\), including the even cut approaching
the wall and the odd cut lying exactly at one half.

## 5. All finite rows, aliases, and the local Gaussian

Use exactly
\[
 L_N=\lfloor N/16\rfloor+1,\qquad M_N=\lceil N/2\rceil,\qquad
 \ell_N=(L_N-1/2)/N,\qquad b_N=(M_N-1/2)/N.                     \tag{16}
\]
The retained indices are \(L_N\le j<M_N\).
The [lower-current theorem](research_mixed_conditional_negative_height_lower_currents.md)
pays every row \(j<L_N\), including zero, and the real lower cut.
The upper-half theorem pays every row \(j\ge M_N\), including
both parities and every revived numerator value. The real upper
cut is paid by the same continuous upper rate.
All physical wall rows between these cuts remain in (6).

Apply the original split cotangent identity to the holomorphic
interpolant (6):
\[
 \begin{split}
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
 &=N\int_{\ell_N}^{b_N}T_N(t)\,dt+\mathcal R_N,\\
 \mathcal R_N&=\frac{N}{2i}\left\{
  \int_{\partial R^+}T_N(s)[\cot(\pi Ns)+i]\,ds+
  \int_{\partial R^-}T_N(s)[\cot(\pi Ns)-i]\,ds\right\}.
 \end{split}                                                     \tag{17}
\]
The outer heights are \(\pm2\). Each sign-half boundary in (17)
omits the real segment and keeps its original induced orientation.
The density is \(+N\), and there are no new interpolation poles.

All six weighted sides are paid by the half-cut theorem, Section 4.
For precision, its source estimates on the prewall part are the
original bounds. On the postwall part the exact rate derivatives are
\[
 \partial_\sigma\widehat R\le9\pi/5\quad(\sigma\ge0),\qquad
 \partial_\sigma\widehat R\ge-19\pi/10\quad(\sigma\le0),
\]
with the improved lower bound \(-47\pi/30\) when \(\sigma\le-1/8\).
The cotangent kernels supply \(2\pi|\sigma|\).
Every vertical side is thus bounded by its paid real cut with a
positive extra loss. The real rate on the whole interval is below
\(11/8\); at height \(+2\) the loss is at least \(2\pi/5\), and
at height \(-2\) it is at least \(7\pi/10\). Both horizontal
remainders therefore have rate at most \(11/8-2\pi/5<7/40<M\).
Those calculations use only (1), (7) and the original carrier;
they do not assume \(h_*<\eta\). They remain valid at \(\eta=0\),
since no factor \(1-e^{-2\pi iNa}\) has been divided out.

Move the real integral in (17) to height \(h_*\).
The lower unweighted connector is paid by the lower-current
theorem's prewall convexity argument. Section 4 pays the upper
one without a convexity assumption across the incoming zero.
Section 3 pays the part of the main line outside a fixed regular
saddle neighborhood. This is the full retained-current inventory.

Near the original critical point the regular row symbol is
\[
 T_N(s)=N^{-3/2}b(s;a,y)e^{NQ(s;a,y)}
                             (1+O_{\rm hol}(N^{-1})),           \tag{18}
\]
where
\[
 a_0(q)=\sqrt{2\sin\pi q}\,e^{-i\pi q/2},\qquad
 b(s;a,y)=\frac{a_0(a+s)a_0(y+s)}
                    {a_0(s)^3a_0(a)a_0(y)}.                   \tag{19}
\]
All its arguments lie in the original regular strips.
The Gaussian coefficient is consequently
\[
 \mathcal B(a,y)=
     \frac{\sqrt{2\pi}\,b(s_*;a,y)}
                    {\sqrt{-Q_{ss}(s_*;a,y)}}\ne0,              \tag{20}
\]
with the original accretive square root. The powers are exactly
\(N^{-3/2}\cdot N\cdot N^{-1/2}=N^{-1}\).
All other source groups have a common fixed positive rate loss,
after the arbitrary finite-product tolerances in (11) are chosen
inside the established reserves. The local Gaussian expansion,
with its odd correction vanishing, proves (5).

For parameter continuation, fix the integer cuts, alias paths,
main height and connectors at each base point before varying \(a,y\).
The local saddle chart is uniformly separated from every divisor.
Its short local contour adjustment stays in that chart.
Outside it, the strict source gaps persist by the joint continuity
of (10) and the uniform zero-safe estimates, including on paths
through the incoming real cut. The original interpolation remains
holomorphic there even when its zeros move. No asymptotic symbol
at those zeros is used. A finite cover of \(\mathcal D_+\) gives
fixed uniform neighborhoods and error constants. Cauchy's formula
on smaller neighborhoods gives every fixed normalized mixed derivative.
No moving floor or ceiling is differentiated.

## 6. Consequence for the entire displaced conditional rectangle

The [wall-gap completion theorem](research_mixed_conditional_wall_gap_completion.md)
already proves the same packet with the same coefficient (20) on
a fixed neighborhood of
\(\mathcal D_-=\{(a,y)\in\mathcal D:h_*\le0\}\).
The two sets \(\mathcal D_\pm\) are compact and cover \(\mathcal D\).
Their original critical branch, symbol and literal finite polynomial
agree on overlaps, including \(h_*=0\).

**Corollary.** Formula (5), with coefficient (20), holds on a fixed
complex neighborhood of the entire parameter rectangle (1).
It is uniform along all integer levels, for both parities, and with
all fixed normalized mixed derivatives. In particular, for all
sufficiently large \(N\),
\[
 |C_{1,N}(X,Y)|\ge
             \frac{|\mathcal B(a,y)|}{2N}e^{N\Re\Theta(a,y)}
                           \qquad((a,y)\in\mathcal D).           \tag{21}
\]
Compact covering and the uniform relative error give this directly.

No positive sign for the old wall gap \(M-\mathcal R(1-x)\) is
deduced or needed on the nonnegative-height portion. Its possibly
large individual wall rows belong to the coherent retained cycle.
This completes the original conditional factor on the displaced
rectangle. A full cap packet, the original outside allocations,
incoming contour comparison, and full next-transfer asymptotic
remain separate; no knot-family enlargement is asserted here.

