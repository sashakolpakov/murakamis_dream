# The complete incoming right tail on the lower right shoulder

Research proof, 8 November 2026. This extends the original incoming
right tail to the output shoulder \(9/20\le\Re y\le1/2\), at its
actual negative height. The next kernel is kept with the explicit
last-row alternative of its completed shoulder estimate. That
alternative is compared only after multiplication by the first
block and both incident Fourier halves.

The old incoming corner is replaced by its exact finite Cauchy
rectangle before taking absolute values. All original physical
rows, weighted currents and unweighted joins remain in the proof.
No numerical evaluation or modification of a frozen source is used.

## 1. Original source and statement

Keep the actual ordinary-next references, phases, cap plane and
notation of [the old incoming right tail](research_mixed_next_unselected_incoming_right_tail.md).
Thus
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
 (\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),\quad \beta=0,1,
 \tag{1}
\]
and both later vertices are ordinary. Write
\[
\begin{gathered}
 A=\Re a_*,\quad \alpha=\Re y_*,\quad
 h_a=\Im a_*,\ h_s=\Im s_*,\ h_y=\Im y_*,\\
 .278\le A\le.391,\quad .24<\alpha,\Re s_*<.36,\quad
 -.072<h_a<0,\quad -.102<h_s,h_y<-.001,\\
 y=q+ih_y,\quad .45\le q\le.5,\qquad
 z=u+i\Im z_*,\quad u\in P=[.22,.45].
\end{gathered}                                                    \tag{2}
\]
The external parameter remains the actual \(s_4^*\in K_3\cup K_4\).
Put \(X=e^{-2\pi ia},Y=e^{-2\pi iy},Z=e^{-2\pi iz}\).
The exact density is
\[
 D_N(a;y,z,w)=U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{\beta,N}(Y,Z).
 \tag{3}
\]
There is no selected factor \(Y^{-N}\).

Let the original increasing/upward chain be
\[
 \Gamma_R=[.45+ih_a,.5+ih_a]\ \cup\
          [.5+ih_a,.5]\ \cup\ [.5,1].
 \tag{4}
\]

**Theorem.** Uniformly over (1)--(2), all real ordinary colors
\(w\in[-2,2]\), and both level parities,
\[
 \left|N\int_{\Gamma_R}D_N(a;y,z,w)\,da\right|
       |d_N(Z)|^{\beta/2}
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}} .
 \tag{5}
\]
Here \(\Lambda_{123}\) is the original outgoing affine action.
The same estimate holds for fixed real-color derivatives with
polynomial cost. On sufficiently small fixed local complete-color
and actual-output neighborhoods, the unweighted integral normalized
by the original next action has every fixed normalized mixed jet
bounded with gap \(10^{-12}\). Paths and integer cuts are fixed
at their base values for these outside derivatives.

Only at the actual output is the established nonzero factorial
packet used to remove an outgoing halfweight. For \(\beta=0\)
no such halfweight is inserted.

## 2. The two next-kernel alternatives and a raw-prefix lemma

Use
\[
\begin{split}
 Q(s;a,y)&=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,\\
 F(s;a,y)&=Q(s;a,y)-\tfrac12g(y),\\
 B_U(x)&=\Re T_0(a_*)-\Re p_L(x-A)-\kappa(x-A)^2,
                  \qquad\kappa=1/2500000,
\end{split}                                                       \tag{6}
\]
with exactly the original \(p_L,p,A_*\). The complete cap has the
rate \(B_U(x)\) for \(.22\le x\le.5\) at height \(h_a\).

The [complete next-block shoulder theorem](research_mixed_next_lower_right_shoulder_next_block.md),
equations (5)--(7),(22), gives
\[
\begin{split}
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)|^{1/2}|d_N(Z)|^{\beta/2}
 \le C_\tau N^{B_\tau}\bigl[
 e^{N(\mathcal B(q,u)-10^{-9}+\tau)}
                   +e^{N(\mathcal L(q,u)+\tau)}\bigr],\\
 A_*+p(q-\alpha)+\mathcal B(q,u)=\Lambda_{123}(z),\\
 \mathcal L(q,u)=-2\pi h_y+2\pi(\Im z_*)_+
                      -\tfrac12\Re g(y)-\tfrac\beta2\Re g(z).
\end{split}                                                       \tag{7}
\]
It bounds the entire next kernel. Its last term is not asserted
to obey the same standalone supporting plane on this shoulder.

Both terms of (7) can be multiplied by any prefix contribution
whose pointwise raw rate is at most
\[
                         B_{\rm raw}=2383/1500.                  \tag{8}
\]
For the first term this is exactly the shoulder marginal lemma in
[the central-first shoulder proof, Section 5](research_mixed_next_lower_right_shoulder_central_prefix.md):
\[
 B_{\rm raw}-\tfrac12\Re g(y)
              \le A_*+p(q-\alpha)-1/50.                          \tag{9}
\]
Its proof uses only (8), the actual \(A_*>9/5\), the two signs of
\(p\), and the full Fourier bound. In particular it applies to a
current estimate; no polynomial interpolation of that current is
needed.

For the second term of (7), the full bound is
\[
 B_{\rm raw}-\Re g(y)-2\pi h_y+2\pi(\Im z_*)_+
                                         -\tfrac\beta2\Re g(z).
 \tag{10}
\]
At \(q_0=.45\), the original ordinary next last-row supporting
estimate and the old raw-prefix marginal give a gap greater than
\(1/50\) below \(\Lambda_{123}\). These are precisely the original
row and marginal inputs retained in the low-block theorem and
Section 5 of the next-block shoulder theorem.
As \(q\) increases, the derivative of (10) is
\[
                         -\log|1-Y|<-\log(3/2)<0.                \tag{11}
\]
Thus that same comparison persists through \(q=.5\).
Here and below \(R=|Y|>13/25>1/2\), and
\(|1-Y|>3/2\), by the elementary actual-radius witnesses in the
central-first shoulder proof.

The original whole Fourier inequality is
\[
 |d_N(Y)|^{1/2}\le C_\tau N^{B_\tau}
                         e^{N\{-\Re g(y)/2+\tau\}}.              \tag{12}
\]
It includes the forcing alternative. On the closed lower strip
\(-\Re g(y)\ge0\), with equality permitted at \(q=.5\).
No division at a possible zero is used in (9)--(12).
Consequently every raw-prefix group in (8) is paid against both
complete-next alternatives, with a fixed reserve.

## 3. A fixed lower cut on the first right horizontal segment

Consider \(a=x+ih_a\), \(.45\le x\le.5\).
Take the new fixed index cuts \(c=1/20\) and \(b=1/2\).
For every physical row \(t=j/N\le c\), the exact incoming
carrier combines with its numerator as
\[
 |X|^{-1}|1-Xr^k|=|e^{-2\pi h_a}-e^{-2\pi i(x+k/N)}|
                         <13/5<e.
\]
Together with \(|1-Yr^k|\le2\) and the sine chord bound,
the absolute row rate obeys
\[
 E(t)<t\{47/10-3\log(6t)\}\le169/400.                              \tag{13}
\]
The function on the right increases up to \(1/20\).
For its endpoint use \(\log(10/3)<5/4\); indeed
\[
 e^{5/4}>
 1+\frac54+\frac{25}{32}+\frac{125}{384}+\frac{625}{6144}
 =\frac{21249}{6144}>\frac{10}{3}.
\]
The zero row is included by its exact value one.
The whole cap disk ceiling from the seam theorem is
\(b_0+c_{\rm b}<1133/1000\). Hence the complete cap times
the full positive lower-row sum has raw rate
\[
 \frac{1133}{1000}+\frac{169}{400}
   =\frac{3111}{2000}<\frac{2383}{1500},\qquad
 \frac{2383}{1500}-\frac{3111}{2000}=\frac{199}{6000}.              \tag{14}
\]
This also pays a fixed small real collar of the lower cut,
by the canonical uniform upper bound and continuity of its rate.

For \(t\in[1/8,.5]\) at height \(h_s\), the full supporting
inequality holds on the square \(a_R,y_R\in[.22,.5]\).
The four-domain proof is given in
[closed half-output action transport, Section 3](research_mixed_four_conditional_closed_half_output.md):
the old domain is strictly concave, the separate two extensions
are already proved, and when both outer coordinates exceed .45
the two shifted cotangents are nonpositive. The extension is
negative semidefinite, including its closed half faces.
It follows that
\[
 B_U(x)+\Re F(t+ih_s;x+ih_a,y)
 \le A_*+p(q-\alpha)-\kappa(x-A)^2,
\quad
 \kappa(x-A)^2\ge\frac{3481}{2500000000000}>10^{-9}.                \tag{15}
\]
For \(c\le t\le1/8\), both shifted real coordinates are at least
\(1/2\) and below one. The two chirp-folded numerator moduli
are at least one, while the own modulus at \(h_s<0\) is
strictly less than one. Thus the original real-index force
is greater than one, and the main rate increases up to \(1/8\).
Equation (15) pays this whole additional main strip.

The half real row is also paid. At \(q=.45\), the old right-tail
proof pays it uniformly in \(x\). Its derivative in \(q\) after
the first halfweight allocation is
\[
 \log|1+Y|-\tfrac32\log|1-Y|<-11/10<p.                            \tag{16}
\]
This transports the old \(1/2000\) deficit to the shoulder.
The original transformed-upper-row endpoint theorem applies
on the full independent square \([.22,.5]^2\) with these heights.
Every upper physical row is therefore bounded by the half or
last row. The last row with the whole cap has raw ceiling
\[
 b_0+c_{\rm b}+18\pi/125
       <11099/7000<2383/1500,                                   \tag{17}
\]
exactly as in the old right-tail proof. Thus both physical ends
are retained and paid, without physical termination off grid.

## 4. All currents on that horizontal segment

For \(c\le t\le.5\), both shifted real coordinates \(x+t,q+t\)
belong to \([.5,1]\). Before the possible boundary zeros,
\[
 \Re Q_{ss}=\pi\{C(a+s)+C(y+s)-3C(s)\}\le0,\qquad
 C(v)=\Re\cot\pi v.                                             \tag{18}
\]
It is strict for \(t<.5\). At the half boundary take the
continuous one-sided rate; its possible numerator kinks have
upward height-derivative jumps, so height convexity persists.

For \(\sigma=\Im s\le0\), both numerator arguments are
nonpositive and the own argument is nonnegative. Therefore
\(\Im Q_s\le2\pi x\le\pi\).
By (18), \(\Im Q_s\) decreases with \(\sigma\); its original
upper-height limit is
\[
                   -\pi-2\pi q+2\pi t\ge-19\pi/10.               \tag{19}
\]
These are the original logarithmic lifts, not arguments reduced
modulo \(2\pi\).

Use lower alias height \(-1/5\), upper height \(4\).
Compared at the same \(q\) with the main height \(h_s\),
their weighted rates lose at least
\[
 \pi/5,\qquad
 8\pi-\frac{19\pi}{10}\left(4+\frac{51}{500}\right)
                           =\frac{1031\pi}{5000}.               \tag{20}
\]
Every weighted upper side decreases from its real endpoint
with slope at most \(-\pi/10\); every weighted lower side
decreases as its downward height increases. Both unweighted
joins are bounded by the maximum of their real and main
endpoint rates, using (18).

The original canonical interpolation is
\[
 T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                              E_N(a)E_N(y)E_N(s)^3.
 \tag{21}
\]
Use \(L_N=\lfloor N/20\rfloor+1\), \(M_N=\lceil N/2\rceil\)
and their half-grid boundaries. The exact cotangent identity
retains the \(+N\) main integral, two horizontal aliases, four
weighted half-sides and both unweighted joins. The two numerator
arguments may equal one at the upper cut. The canonical
reflection bound in
[the repeated two-block row source, Section 3](research_repeated_two_block_canonical_row_source.md)
gives the original continuous upper rate there, including its
exact midpoint shift and both reflected terms. All denominator
arguments stay regular. The \(O(1/N)\) half-grid shifts have
only \(O(\log N)\) cost, uniformly through numerator zeros.
No relative expansion is used at such a zero.

For the regular term of (7), (14)--(20) give the claimed gap.
For its last-row term, attach \(\mathcal L(q,u)\) to every
profile before comparing it. At a fixed negative index height,
\[
 \partial_q\Re\{F(s;a,y)+\mathcal L(q,u)\}
   =\log|1-e^{-2\pi i(s+y)}|-2\log|1-Y|<\log(3/4)<-1/4.          \tag{22}
\]
This is the exact joint derivative of the next-block shoulder
theorem. At \(q=.45\), the old right profiles and next last-row
source obey the original marginal comparison. Their retained
cap loss in (15) is already greater than \(10^{-9}\).
The new main strip below \(1/8\) increases to that endpoint
before (22) is used. The half real row obeys the same joint
derivative bound; the new lower real cut and first last row
use the raw-prefix lemma instead.
Finally (20) and the join endpoint comparisons are at the
same \(q\), so the attached last-row factor is retained on
both sides. This accounts for positive-height currents without
transporting them directly by (22).

Thus the literal complete source on \([.45,.5]+ih_a\), with
both next alternatives and original measure \(N\,da\), has a
finite gap at least \(10^{-10}\).

## 5. The finite middle reduction on the enlarged corner

For \(a=x-i\eta\), \(x\in[.5,.7]\), \(0\le\eta\le9/125\),
retain the exact low, middle and upper physical groups of
[the lower-output reduction](research_mixed_conditional_lower_output_middle_reduction.md):
\[
 L_N=\lfloor2N/25\rfloor+1,\quad M_N=\lceil N/2\rceil,\quad
 \ell_N=(L_N-\tfrac12)/N,\quad b_N=(M_N-\tfrac12)/N .
\]
The low and upper physical bounds are whole-output-disk
estimates. They remain valid at the shoulder, with complete-cap
raw ceilings respectively
\[
                       2383/1500,\qquad 32563/21000<2383/1500.
 \tag{23}
\]
Their real collars retain a strict raw reserve wherever the
original argument uses one. Both next alternatives are paid
by Section 2.

The exact two-branch numerator rate is the one in the cited
reduction, retaining the incoming period-shift term. At the
additional outgoing boundary \(q+t=1\), use the same zero-safe
canonical reflection bound as in Section 4.
The old vertical slope proof extends to \(q\le.5\), with
upper slope \(19\pi/10\) instead of \(9\pi/5\). Explicitly,
before the incoming wall it is bounded above by
\[
 2\pi-4\pi t+\max\{2\pi(q+t)-\pi,0\}\le19\pi/10
 \quad(t\ge3/40).
\]
After the wall, the two upper ranges give respectively
\(\pi(2+2q-4t-2x)\) and
\(\pi(5/2-x-3t+2q)\), both at most \(19\pi/10\).
The lower slope bounds \(-33\pi/20\) before the wall,
and \(-19\pi/10,-47\pi/30\) in the two old postwall
ranges, are unchanged: the outgoing argument is nonpositive
throughout this shoulder.

Keep lower height \(-2\), but enlarge the upper height to \(4\).
All four weighted vertical half-sides decrease away from their
paid real cuts. The complete horizontal remainders retain
the crude real rate \(27/20\); the upper loss is now
\(4(2\pi-19\pi/10)=2\pi/5\).
The lower loss is at least the old \(7\pi/10\).
Thus with the complete cap \(1549/1500\), both horizontal
raw rates are below
\[
             1549/1500+27/20-2\pi/5<1699/1500.                  \tag{24}
\]
The enlarged rectangle has exactly the same enclosed physical
rows and no new pole. The original factorial theorem allows
every fixed bounded height, so height four is within its scope.

Consequently the exact reduction
\[
 C_{1,N}(X,Y)=N\int_{\ell_N}^{b_N}T_N(t;a,y)\,dt+\mathcal E_N
 \tag{25}
\]
has its entire physical/current error paid against both
next alternatives, by the raw-prefix lemma. All six currents
and the two original Fourier forcing alternatives are retained.

## 6. Unweighted deformation and the two corner comparisons

The [closed half-output theorem](research_mixed_four_conditional_closed_half_output.md)
proves the original selected root, its zero logarithmic lift,
\[
 2/25<\Re s_*<1-x,\qquad
 1/5<|e^{2\pi is_*}|<2,\qquad
 |\Im s_*|<\log5/(2\pi),
 \tag{26}
\]
and strict prewall horizontal concavity on the full enlarged
compact rectangle. In this shoulder the outgoing shifted
cotangent is nonpositive, so that curvature has no additional
positive outgoing term.

The postwall horizontal inequalities of
[the Gaussian deformation, Section 2](research_mixed_conditional_lower_output_gaussian_deformation.md)
use only \(|Y|\le1\) at negative private heights, and
\(|Y|<8/7\) at nonnegative private heights. They are independent
of the old upper angular endpoint. They therefore keep the
entire critical-height main line below its unique maximum
\(\Re\Theta(a,y)\), with a strict compact loss off its local
critical chart.

Both original unweighted connectors remain. The lower one is
height-convex by the prewall curvature. At the limiting half
cut, the exact two-branch rate has derivatives
\[
 \partial_\sigma\widehat R(1/2,\sigma)
    \le-2\pi(x-q)\le0\quad(\sigma<\eta),\qquad
 \partial_\sigma\widehat R(1/2,\sigma)\ge0\quad(\sigma>\eta).
 \tag{27}
\]
At \(x=q=.5\), strict decrease is unnecessary: its maximum
still occurs at one of its two endpoints. The outgoing zero
at \(q+t=1\) has the same continuous one-sided rate.
Uniform continuity transfers this endpoint maximum to the
actual half-grid cut with an arbitrarily small debit.
The real connector endpoints use (23); their main endpoints
have the strict off-saddle loss.

Thus the complete two-rate Gaussian decomposition of the cited
deformation extends to the present shoulder: its local source
is \(N^{-1}\mathcal B_1(a,y)e^{N\Theta}(1+O_{\rm hol}(N^{-1}))\),
with the same original nonzero symbol, and its errors are a
term below the conditional action and a term paid by (23)--(25).
The powers remain \(N\cdot N^{-3/2}\cdot N^{-1/2}=N^{-1}\).
No relative asymptotic for the entire polynomial is inferred.

Write \(a_L=.5+ih_a\). On the replacement bottom and right sides
\[
 a_L\longrightarrow .7+ih_a\longrightarrow .7,
 \tag{28}
\]
the closed half-output theorem gives
\[
 |U_{0,N}(w,X)|\,|d_N(Y)|^{1/2}e^{N\Re\Theta(a,y)}
 \le C_\tau N^{B_\tau}
      e^{N\{A_*+p(q-\alpha)-4\cdot10^{-9}+\tau\}}.                \tag{29}
\]
This pays the regular term of (7).

For the next last-row term, first work at \(a_L\) and the fixed
negative private height \(h_s\). At \(q=.45\), the original
supporting inequality and next last-row plane give
\[
 B_*+\Re F(t+ih_s;a_L,y)+\mathcal L(q,u)
            \le\Lambda_{123}(z)-4\cdot10^{-9},
                   \qquad1/8\le t\le1/2.                       \tag{30}
\]
For all these fixed profiles, (22) decreases the left side as
\(q\) goes to .5. On \(2/25\le t\le1/8\), the index force
increases the profile to \(1/8\), at the same \(q\).
The private-height convex maximum argument in the closed
half-output theorem now replaces \(\Re Q(t+ih_s)\) by
\(\Re\Theta(a_L,y)\), with no loss: the attached
\(\mathcal L\) is independent of the private index.
The complete cap on the bottom has rate \(B_*\), and on
the right vertical has the smaller rate \(3907/4500<B_*\).
Finally \(\Re\Theta\) decreases rightward and upward on (28).
This proves the counterpart of (29) with the last-row term
attached and the same fixed gap below \(\Lambda_{123}\).

Restoring both Gaussian errors, including the real-end errors
of its connectors, therefore pays the whole literal density
on (28). The errors from (25) already have the larger
raw-prefix reserve against both next branches. A common finite
gap \(10^{-10}\) is available.

## 7. Exact corner identity, final real arc and scope

For fixed \(Y,Z,w\), the entire incoming factor
\(U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\)
is a finite Laurent polynomial. Cauchy's theorem with its
original \(N\,da\) measure gives exactly
\[
 \int_{a_L}^{.5}D_N\,N\,da+\int_{.5}^{.7}D_N\,N\,da
 =\int_{a_L}^{.7+ih_a}D_N\,N\,da
                         +\int_{.7+ih_a}^{.7}D_N\,N\,da .
 \tag{31}
\]
Only the right side is estimated absolutely; no separate
estimate at the artificial old corner is asserted.

For the remaining real arc \(a\in[.7,1]\), the full coherent
far-arc source has output-disk rate \(153/100<2383/1500\),
as in equation (24) of the old right-tail theorem.
Section 2 pays this whole finite source against both next
alternatives at the shoulder, with its original \(+N\) measure.

Combining that arc, (31), and the first horizontal segment
proves (5). There are only finitely many source groups; their
uniform strict reserves allow the stated finite tolerances and
the smaller local normalized-jet gap. All paths and cuts are
held fixed before taking outside derivatives, and the original
integer-weight holomorphic products give those jets by Cauchy
estimates. Both parities and all real-color bounds persist.

The theorem removes precisely the right incoming chain (4)
for \(q\in[.45,.5]\). The first incoming initial interval and
left taper require their own shoulder estimates. It does not
bound the lower period beyond this shoulder, the remaining
upper selected complement, a terminal reference family, or
an arbitrary short filling.

