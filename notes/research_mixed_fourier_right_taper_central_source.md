# The complete central retained source on the incoming right taper

Research deduction, 7 November 2026. The extended incoming sheet and
the completed coupled connector control the entire outgoing period
of the central retained rows. The outgoing vertical current is
included, with its original finite cardinal at both endpoints.
All estimates use the explicit maximum baseline from the connector
theorem. No sign for its difference from the compensated boundary
tangent is assumed.

This note concerns the retained range between the original half-grid
cuts. It does not estimate the physical rows below the lower cut
by subtraction from a bound on a canceled sum.

## 1. Exact restricted source and notation

Use exactly the actual reference, incoming targets and allocation in
[the incoming-taper connector theorem](research_mixed_fourier_right_taper_shear_connector.md):
\[
 \eta\in\{0,1\},\quad a=x+ih,\quad
 9/20\le x\le1/2,\quad
 c=\Im a_*\le h\le0,\quad -.108\le c,
 \qquad -.102\le h_s,h_q\le-.001 .
 \tag{1}
\]
The output remains \(y=x_0\), \(Y=e^{2\pi iy}\). Let
\(\mathfrak B_\eta(x,h)\), \(\gamma_\eta\) and
\(\chi_\eta\) be precisely (3) of that theorem, and put
\[
 \kappa_\eta=\kappa\chi_\eta,\qquad
 \delta_{s,\eta}=\kappa_\eta(23/200)^2,\qquad
 \delta_{c,\eta}=\kappa_\eta/2500,\qquad
                         \kappa=1/2500000 .
 \tag{2}
\]
The original marginal in this baseline is unchanged.

Retain \(L_N=\lceil N/8\rceil\), \(M_N=\lceil N/2\rceil-1\),
\(\sigma_-=(L_N-\tfrac12)/N\), \(\sigma_+=(M_N+\tfrac12)/N\),
and \(\alpha_N=-1/(2N)\), \(\beta_N=1+\alpha_N\). Define
\[
\begin{split}
 C_N^{\rm cen}(X,Z)
   &=\sum_{j=L_N}^{M_N}\frac{X^{-j}p_j(X)p_j(Z)}{P_j^3},
       \qquad X=e^{-2\pi ia},\\
 S_N^{\rm cen}(q)
   &=C_N^{\rm cen}(X,e^{-2\pi iq})\widehat f_N(q;y),\\
 V_N^{\rm cen}(a)
   &=\sum_{l=0}^{N-1}C_N^{\rm cen}(X,r^l)f_l(y)
     =\sum_{j=L_N}^{M_N}\frac{X^{-j}p_j(X)}{P_j^3}H_{j,N}(y).
\end{split}
 \tag{3}
\]
Here \(H_{j,N}=\sum_{l=0}^{N-j-1}P_{j+l}f_l/P_l\) is the
whole original outgoing contraction. Every \(l\) in (3) remains
in that coherent sum. The second equality uses physical support
only on the physical lattice. The exact row \(T_N\), phase
\(F_\eta\), and factorial cardinal \(\widehat f_N\) are those
in equations (4)--(5) of the connector theorem.

**Theorem.** For every fixed \(\tau>0\), uniformly on (1),
there are \(C_\tau,A_\tau,N_\tau\) such that, for both parities,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}|V_N^{\rm cen}(a)|
       \le C_\tau N^{A_\tau}
                     e^{N\{\mathfrak B_\eta(x,h)+\tau\}},
                  \qquad N\ge N_\tau .
 \quad}
 \tag{4}
\]
The proof also gives strict gaps for every complementary contour
group described below. It proves an upper bound for the entire
finite source (3), not an asymptotic or a lower bound at a new target.

## 2. Central outgoing plateau and nonpositive retained corrections

For \(q=z+ih_q\), \(z\in P=[.22,.45]\), the extended sheet
and its incoming height credit imply
\[
 \Re F_\eta(u+ih_s,a,z+ih_q)
 \le\mathfrak B_\eta(x,h)
       -\kappa_\eta\{(u-\Re s_*)^2+(z-\Re q_*)^2\}.
 \tag{5}
\]
Indeed its stronger height decrease \(\pi(h-c)/10\) is
at least \(\gamma_\eta\). At a real retained cut the
nonnegative-height real transport gives
\[
 \Re F_\eta(u,a,z+ih_q)
   <B_\eta(.45)-\gamma_\eta-1/35000
   \le\mathfrak B_\eta-1/35000,\qquad u=1/8,1/2.
 \tag{6}
\]
For \(h_s\le v\le0\), the side joins retain vertical convexity
on \(z\in P\): the new incoming pair is positive semidefinite,
and the remaining \((s,q)\) form and the original left-cut
Schur bound are exactly those proved in Section 2 of the
connector theorem. Since \(.24\le\Re s_*\le.36\),
(5)--(6) bound each unpenalized side join by
\[
       \Re F_\eta(u+iv,a,z+ih_q)
                     \le\mathfrak B_\eta-\delta_{s,\eta}.
 \tag{7}
\]

The lower alias has a uniform comparison on the whole outgoing
lower half-plane, independently of \(z\). For \(v<0\),
\[
 \Im F_{\eta,s}
 =\Im\{g'(s+a)+g_-'(s+q)-3g'(s)+2\pi ia\}
                                                    <3\pi/2 .
 \tag{8}
\]
In fact \(\Re(s+a)\in[.575,1]\) and \(\Im(s+a)<0\)
give \(\Im g'(s+a)\le0\); the lower-half-plane disk
logarithm at \(s+q\) has argument less than \(\pi/2\);
\(\Im g'(s)\ge0\); and \(2\pi x\le\pi\).
The integral endpoint at \(v=0\) is interpreted continuously
if its incoming numerator vanishes. Hence
\[
\begin{split}
 \Re F_\eta(u-i/5,a,q)-2\pi/5
    &<\Re F_\eta(u+ih_s,a,q)-\pi/10,\\
 \Re F_\eta(u+iv,a,q)+2\pi v
    &\le\Re F_\eta(u,a,q)+(\pi/2)v
                      \le\Re F_\eta(u,a,q)\quad(v\le0).
\end{split}
 \tag{9}
\]
For the first line, the exact intermediate remainder is
\((3\pi/2)h_s-\pi/10\), which is smaller than the displayed
one. The second line applies at both retained cuts.
Thus (7) pays the unpenalized joins, and (6), (9) pay the
lower vertical aliases. The original lower horizontal height,
kernel and denominator are unchanged.

All positive retained profiles on \(z\in P\) transport
pointwise from incoming \(.45+ic\), minus \(\gamma_\eta\).
The old complete upper alias has reserve \(7/50\);
its positive sides have reserve \(1/35000\).
Their finite symbols extend across the sole new numerator wall
by the undivided product bound (20) of the connector theorem.
This accounts for the original four retained groups on \(P\).

## 3. Both outer outgoing arcs and the shrinking real endpoint

The two right-arc comparisons from
[the nonpositive-current proof](research_mixed_fourier_right_cap_nonpositive_index_corrections.md),
equation (9), depend on \(s,q,Y\), not on \(a\):
\[
\begin{split}
 \Re F_{\eta,q}&<-1/10
                  &&(.45\le z\le.75,\ \Im s\le0),\\
 \Re F_\eta(s,a,z+ih_q)
  &<\Re F_\eta(s,a,z-.5+ih_q)-1/200
                  &&(.75\le z\le1,\ \Im s\le0).
\end{split}
 \tag{10}
\]
They therefore transport (5)--(7) to the full right arc.
The critical-index sheet there has a positive loss
\(\kappa_\eta(.09)^2\); the real cuts retain \(1/35000\);
the negative joins retain \(\delta_{s,\eta}\).
Equation (9) pays its lower aliases. The whole positive
retained group on this arc, including both side orientations,
has already been assembled with finite gap \(1/280000\)
in the connector theorem. No separate upper-height pointwise
bound on the original small arch is substituted for that result.

For the left outgoing taper put
\[
 q(t)=t+i h_qt/(11/50),\qquad0\le t\le11/50 .
 \tag{11}
\]
The proved derivative comparison is likewise independent of
the incoming parameter. On \(h_s\le\Im s\le0\), it carries
each phase to its value at \(q=.22+ih_q\), and at \(q=0\)
it retains the stronger loss \(3/400\). The main sheet in (5)
therefore has loss \(\delta_{c,\eta}\) all along (11);
the real cuts and negative joins are bounded by (6)--(7).
The lower alias follows from (9) on each such outgoing point.
The positive retained profiles on (11) are transported directly
from their old incoming endpoint \(.45+ic\); their old complete
left-taper proof retains all positive joins and upper debits.
After a fixed common tolerance, the whole central retained
source along (11), including its \(+N\) retained coefficient,
has a finite gap at least \(\delta_{c,\eta}/4\) below
\(\mathfrak B_\eta\). The outgoing integration coefficient
is another \(N\), absorbed by the remaining reserve.

At the real seam \(q=0\), all central retained profiles instead
have the common raw reserve \(3/400\): the negative path is
paid by the independent taper comparison and (5)--(7); the
positive path is transported from its old paid seam; and the
lower alias is paid by (9) relative to the same seam sheet.
The exact source is
\[
 f_0(y)\sum_{j=L_N}^{M_N}
                         \frac{X^{-j}p_j(X)}{P_j^2}.
 \tag{12}
\]
The exact zero-safe reciprocal bound \(|E_N(q)|\le C\) on
\(\alpha_N\le q\le0\), and the regular shared-factor and
cardinal ratios, preserve all these central contour estimates
on that shrinking real segment. These are precisely the
endpoint comparisons established in Section 2 of the connector
theorem; their finite proof keeps the new incoming numerator
zero multiplicatively. Thus the real-segment contribution has
finite gap \(1/1000\), with its original outgoing \(+N\).

## 4. The entire outgoing vertical current

The exact real-endpoint identity applies to (3) because the
outgoing alias elimination was proved for each physical
\(j\le M_N\). It is linear in the retained coefficients.
Writing
\[
 w_{N,0}(v)=\frac1{1+e^{2\pi Nv}}
                              -\boldsymbol1_{\{v<0\}},
 \tag{13}
\]
its vertical term is
\[
 iN\int_{\mathbb R}w_{N,0}(v)
       \{S_N^{\rm cen}(\beta_N+iv)
                       -S_N^{\rm cen}(\alpha_N+iv)\}\,dv .
 \tag{14}
\]
Both cardinal values and their original phases remain in (14).

On a fixed compact vertical interval, repeat the exact
two-endpoint interpolation of
[the vertical-current completion](research_mixed_fourier_right_cap_vertical_current_completion.md),
equations (8)--(9). The polynomial is first made periodic
at the physical retained indices, then the same left-\(q\)
interpolation is used at both ends with their respective
cardinals. No off-grid factorial periodicity is assumed.
The incoming factor \(\Pi_N(s+a)E_N(a)e^{2\pi iNas}\)
is identical in the seam and vertical profiles.
Thus their entire change, including the original outer debit
and the right-cardinal decrement, is independent of \(a\).
Every one of the old comparisons in Section 3 of that proof
therefore applies to each of the newly paid seam contours
from Section 3 here. In particular the raw \(3/400\) reserve
is preserved on every fixed compact interval in \(v\).

The finite estimates remain uniform through the possible
cardinal zeros at \(v=\upsilon\). They are the same zero-safe
piecewise cardinal upper rates, not a division by a leading
symbol. The exact midpoint factor is still
\[
 |E_N(\alpha_N+iv)|
             =\sqrt{(1+e^{2\pi Nv})/N}.
 \tag{15}
\]
The shared factorial has its old regular real part, while the
new incoming numerator has the uniform bound (20) of the
connector theorem. Uniform continuity of the rate functions,
rather than a logarithmic derivative at a zero, handles the
half-grid shifts.

The noncompact ends also have the same uniform payment.
To verify the only changed calibration, use the individual
coherent half-index rate from
[incoming height transport](research_mixed_fourier_incoming_height_transport.md):
\[
 \mathcal E_\eta(1/2;x+ih)
 <B_\eta(.45)-1/35000-(9\pi/25)(h-c)
 \le\mathfrak B_\eta(x,h)-1/35000.
 \tag{16}
\]
The last inequality uses
\(\gamma_\eta\le(\pi/20)(h-c)<(9\pi/25)(h-c)\).
The upper limiting row rate from
[the uniform outgoing-tail proof](research_mixed_fourier_vertical_tail_payment.md),
equations (19)--(20), is smaller than this by \(647/14400\).
The incoming coefficient rate remains jointly continuous on
the new compact targets, including its integrable zeros.
Thus the same compactness argument first fixes a collar
near \(j/N=1/2\), then one height \(H\) which pays all
remaining \(0\le j/N\le1/2\).

Its exact residual upper damping is unchanged:
\[
 e^{-\pi(N-2j)(v-H)},\qquad
 N-2M_N=\begin{cases}2,&N\ {\rm even},\\1,&N\ {\rm odd}.
                  \end{cases}
 \tag{17}
\]
The lower tail retains \(e^{-2\pi N(1-\xi)(|v|-H)}\).
The factorial remainder errors tend uniformly to zero as
the fixed \(H\) increases, and the incoming halfweight uses
its true absolute upper rate \(-\eta\Re g(a)/2\).
No division by that weight or by an incoming product occurs.
These bounds are absolute bounds for the physical rows;
restricting them to \(L_N\le j\le M_N\) is legitimate.
They give the same finite tail gap \(1/100\) below
\(\mathfrak B_\eta\).

Choose that fixed \(H\) first, apply the compact comparison
on \([-H,H]\), and then absorb the polynomial factors and
both tail contributions. With the original normalization,
\[
 |d_N(X)|^{\eta/2}N\int_{\mathbb R}|w_{N,0}(v)|
 \bigl\{|S_N^{\rm cen}(\beta_N+iv)|
                +|S_N^{\rm cen}(\alpha_N+iv)|\bigr\}\,dv
              \le e^{N(\mathfrak B_\eta-1/2000)}
 \tag{18}
\]
for all sufficiently large \(N\), uniformly on (1).

The unweighted right return is separate. On \(h_q\le v\le0\),
the same incoming-independent comparison adds
\((\pi+\phi)|v|-2\pi\upsilon<-1/50\) to each seam profile.
It preserves the raw reserve \(3/400+1/50\); the compact
finite argument just given therefore proves
\[
 |d_N(X)|^{\eta/2}
 \left|N\int_{\beta_N+ih_q}^{\beta_N}
                             S_N^{\rm cen}(q)\,dq\right|
                   \le e^{N(\mathfrak B_\eta-1/200)} .
 \tag{19}
\]
Equation (19) does not borrow the outer weight of (14).

## 5. Assembly and precise remaining scope

Use the same bent outgoing path as in the original main reduction:
the real segment \(\alpha_N\to0\), taper (11), horizontal
segment from \(.22+ih_q\) to \(\beta_N+ih_q\), and the
right return. The global factorial chart is holomorphic on
the intervening domain. Restricting to (3) leaves its exact
identity unchanged; its complete vertical correction is (14).

On the horizontal segment, decompose only the central retained
source by its original four-current identity. Sections 2--3
pay all complementary groups, including the complete coupled
positive group on the right arc. The remaining joint plateau
main integral has the phase bound (5), so its modulus is at
most \(C_\tau N^{A_\tau}e^{N(\mathfrak B_\eta+\tau)}\).
It retains the two zero-mode coefficients \(+N^2\) and the
cardinal \(1/N\) in \(T_N\). Equations (18)--(19) and the
two left pieces give strictly smaller rates. The finite
triangle inequality proves (4).

Every compact estimate uses the same true incoming halfweight
upper rate, with one common arbitrary tolerance. All physical
support walls are used only before continuation or retained
as exact numerator zeros. The proof does not require any
new source, root, or analytic evaluation.

The omitted physical ranges are explicitly \(j<L_N\) and
\(j>M_N\). The latter already has its complete coherent bound
from incoming height transport; it has not been subtracted
to estimate (3). Combining (4) with a direct bound for the
former is the remaining step for the whole-source upper
envelope on (1). Even after that step, equation (26) of the
connector theorem retains the exact difference from the
complex tangent. No compensated boundary sign, selected
incoming estimate, new nonzero packet, or closing theorem
is inferred here.
