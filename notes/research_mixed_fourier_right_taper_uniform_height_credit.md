# A uniform height decrease for the complete Fourier cap

Research deduction, 7 November 2026. The complete incoming-taper
estimate can retain more of the incoming height decrease. All physical
small and high groups, and all nonpositive retained contour profiles,
keep the stronger decrease \(\pi(H-c)/10\). The complete positive
groups and outgoing endpoint currents instead keep their already
proved strict gaps. Combining these two estimates gives a positive
uniform height credit, including at the real taper endpoint.

This is a bound for the entire finite Fourier cap. No contour group
is discarded, and no modulus of an uncontrolled physical sum replaces
one of the coherent estimates. No numerical evaluation is used.

## 1. Parameters and the improved envelope

Use precisely the references and source of
[the full incoming-taper assembly](research_mixed_fourier_right_taper_small_rows.md),
Section 5. In particular
\[
\begin{gathered}
 \eta\in\{0,1\},\quad y=x_0,\quad
 a_*=a_R+ic,\quad -.108\le c\le0,\quad
 a=x+iH,\quad b=9/20\le x\le1/2,\quad c\le H\le0,\\
 D=H-c,\qquad 0\le D\le27/250,\qquad
 \kappa=1/2500000,\quad
 \chi_0=1989/4489,\quad\chi_1=171/196 .
\end{gathered}
 \tag{1}
\]
Both original private critical heights are negative. All references
remain correlated with the original Fourier output. The actual
quadratic taper is the subcase \(H=400(1/2-x)^2c\).

Keep the original \(M_\eta=\Re\Pi_\eta(a_*)\) and
\(p_\eta=\Re\Pi_\eta'(a_*)\), and write
\[
\begin{split}
 B_b&=M_\eta+p_\eta(b-a_R)-\kappa(b-a_R)^2,\\
 B_{\rm ext}(x)&=
      M_\eta+p_\eta(x-a_R)-\kappa\chi_\eta(x-a_R)^2,\\
 B_0(x)&=\max\{B_b,B_{\rm ext}(x)\},\\
 \gamma_\eta(x,H)&=\pi(1-\eta/2)(1/2-x)D,\\
 \delta_+&=1/280000,\qquad
 \widehat\gamma_\eta(x,H)=
              \min\{\pi D/10,\ \gamma_\eta(x,H)+\delta_+\}.
\end{split}
 \tag{2}
\]
The old envelope was \(B_0-\gamma_\eta\).
There is no redefinition of either reference plane in (2).

**Theorem 1.** For every fixed \(\tau>0\), uniformly on (1), at
both level parities and all sufficiently large \(N\),
\[
\boxed{\quad
 |d_N(e^{-2\pi ia})|^{\eta/2}
       |V_N^{\rm F}(x_0,e^{-2\pi ia})|
 \le C_\tau N^{A_\tau}
             e^{N\{B_0(x)-\widehat\gamma_\eta(x,H)+\tau\}} .
 \quad}
 \tag{3}
\]
More precisely the proof gives the two-rate estimate
\[
\begin{split}
 |d_N(e^{-2\pi ia})|^{\eta/2}|V_N^{\rm F}|
 \le C_\tau N^{A_\tau}\big[
 &e^{N\{B_0(x)-\pi D/10+\tau\}}\\
 &+e^{N\{B_0(x)-\gamma_\eta(x,H)-\delta_++\tau\}}\big].
\end{split}
 \tag{4}
\]
The harmless factor two is absorbed into \(C_\tau\) in (3).
The incoming halfweight is always an absolute allocation; it is
never divided out.

## 2. Retaining the stronger decrease before taking contour moduli

The entire incoming dependence of each original joint profile is
\[
 \mathcal J_\eta(s,a)
             =g(s+a)-(1+\eta/2)g(a)+2\pi ias .
 \tag{5}
\]
For \(s=u+iv\), \(1/8\le u\le1/2\), \(v\le0\), the exact
inequality (22) of
[incoming height transport](research_mixed_fourier_incoming_height_transport.md)
gives
\[
 \Re\mathcal J_\eta(s,x+iH)
       \le\Re\mathcal J_\eta(s,x+ic)-\pi D/10 .
 \tag{6}
\]
Every outgoing phase term and retained alias debit is independent
of the incoming height. Thus (6) applies to the main sheet,
the lower retained alias, its negative sides, and the unpenalized
joins between the original private critical height and zero.
It applies for all outgoing points on the already chosen bent
horizontal path.

At height \(c\), the extended main sheet is bounded by
\(B_{\rm ext}(x)\). The real cuts are bounded by
\(B_b-1/35000\), using their real-direction transport at retained
height zero. The negative joins are bounded by the maximum of
these endpoint comparisons, by the existing vertical convexity.
These are exactly the height-\(c\) arguments of Sections 2--3 of
[the central-source theorem](research_mixed_fourier_right_taper_central_source.md).
Apply (6) to each such profile after that comparison. Their rates
are therefore at most
\[
                           B_0(x)-\pi D/10 .
 \tag{7}
\]
All their additional private-index and outgoing-coordinate losses
may be retained; none is needed for the upper rate (7).

The outgoing left-taper differences and the two right-arc
comparisons are independent of \(a\). Consequently they do not
spend the credit in (6). In particular (7) holds on the complete
left taper, outgoing plateau and right horizontal arc for all
these nonpositive retained groups. The lower-alias comparison
uses the enlarged incoming strip \(\Im F_{\eta,s}<3\pi/2\)
from the central-source theorem; its \(\pi/10\) alias reserve
is separate from the incoming decrease in (6).

The exact half-grid cuts differ from their limiting endpoints
by \(O(1/N)\). The same uniform continuous rate bounds and
undivided numerator estimate used by that theorem give the
finite profiles with an arbitrarily small common rate tolerance.
At \(s+a=1\) the numerator zero is kept; no bounded logarithmic
derivative at that zero is required. The cardinal normalization
and the two original zero-mode coefficients remain unchanged.

## 3. Positive retained groups keep their finite reserve

The positive retained heights cannot be assigned (6). Instead
use their already proved original current estimates.

On the outgoing plateau, the upper retained alias has raw reserve
\(7/50\), and the positive sides have raw reserve \(1/35000\),
at incoming \(b+ic\). On the left outgoing taper the corresponding
raw reserves are \(661\pi/12500\) and \(1/35000\), by
equations (9)--(12) and the exact four-current formula (17) of
[the left-taper completion](research_mixed_fourier_left_taper_source_completion.md).
The latter side bound includes the complete positive side interval;
it is not a bound only at its top endpoint.

For each of these profiles, the
[all-height transport](research_mixed_fourier_incoming_taper_all_height.md)
first moves the incoming real part from \(b\) to \(x\), without
increasing a positive-height profile, and then raises its incoming
height with credit \(\gamma_\eta\). Their original finite kernels,
both side orientations, and the outgoing integrals on the bounded
arcs are retained. A fixed source tolerance and the same zero-safe
factorial bounds therefore give a finite rate at most
\[
                     B_0(x)-\gamma_\eta(x,H)-1/140000
 \tag{8}
\]
for the sum of these positive groups. The reserve used here is
smaller than half the smallest raw side gap; it pays the uniform
polynomial factors and the original outgoing coefficient \(N\).

On the remaining right arc it is essential to use the complete
coupled current. Equation (25) of
[the incoming-taper shear theorem](research_mixed_fourier_right_taper_shear_connector.md)
already gives
\[
 |d_N(e^{-2\pi ia})|^{\eta/2}
       |\mathcal I_N^{+}|
       \le e^{N\{B_0(x)-\gamma_\eta(x,H)-1/280000\}} .
 \tag{9}
\]
Its proof retains the exact right-period replacement, the negative
replacement path with its outgoing lower kernel, both retained
side faces, the complete left face and the uniform infinite ends.
No pointwise modulus estimate on the old small upper arch is
substituted for (9). In particular the negative replacement path
is allowed to stay in this paid group; it need not be reassigned
to the profiles in Section 2.

Equations (8)--(9) put every positive retained correction in the
second rate of (4). The fixed gap \(\delta_+\) is kept after the
original current identity, before the final finite triangle
inequality.

## 4. The remaining exact source groups

The original physical split is
\[
 [0,L_N-1]\ \sqcup\ [L_N,M_N]\ \sqcup\ [M_N+1,N-1],
 \quad L_N=\lceil N/8\rceil,\quad M_N=\lceil N/2\rceil-1.
 \tag{10}
\]
Each group retains its whole outgoing sum. The complete small group
has rate
\[
                   B_b-\pi D/10-1/140000
 \tag{11}
\]
by the full small-row theorem, including its absolute vertical
tails and unweighted return. The complete coherent high group
has rate
\[
                   B_b-9\pi D/25-1/70000 .
 \tag{12}
\]
This is the actual initialized Wall contraction from incoming
height transport. It is not a bound on the absolute outgoing
rows. Both (11) and (12) belong to the first rate of (4).

For the central group, Section 2 treats its nonpositive retained
currents on the left taper, plateau and right arc; Section 3
treats all its positive retained corrections. The still separate
outgoing pieces have the following complete finite gaps below
\(B_0-\gamma_\eta\), as proved in Sections 3--4 of the
central-source theorem:

| Original outgoing group | Finite gap |
|---|---:|
| Shrinking real segment from \(\alpha_N=-1/(2N)\) to zero | \(1/1000\) |
| Entire outgoing vertical current, including both infinite ends | \(1/2000\) |
| Unweighted right return | \(1/200\) |

Each exceeds \(\delta_+\), so these three groups belong directly
to the second rate of (4). This use of their complete bounds
does not move a cardinal zero, reuse the vertical kernel on the
unweighted return, or compare different off-grid cardinals.
The noncompact bounds retain the exact upper damping \(N-2j\)
and lower damping \(2\pi N(1-\Re y)\); they need no new height
cutoff for the present deduction.

The exact outgoing identity and each retained four-current
identity now account for every original term. There are finitely
many integral groups, their polynomial factors are uniform, and
their source tolerances can be chosen to sum to \(\tau\).
Applying the finite triangle inequality only at this stage
proves (4), hence Theorem 1.

## 5. A positive uniform credit, and its compensation limit

The new credit improves the old one pointwise:
\[
 \widehat\gamma_\eta\ge\gamma_\eta,\qquad
 \widehat\gamma_\eta>\gamma_\eta\quad(D>0).
 \tag{13}
\]
Indeed \(\gamma_\eta\le\pi D/20\), whereas the two entries
in its new minimum are \(\pi D/10\) and
\(\gamma_\eta+\delta_+\).
There is also an explicit uniform linear credit. With
\(\alpha=1/100000\), one has
\[
 \alpha D\le\frac{27}{25000000}
                   <\frac1{560000}=\frac{\delta_+}{2},
 \qquad \alpha<\pi/10.
 \tag{14}
\]
Thus
\[
 \widehat\gamma_\eta\ge
                 \max\{\gamma_\eta,\alpha(H-c)\}.
 \tag{15}
\]
In particular (3) remains valid with the positive uniform
height credit \(\alpha(H-c)\), even at \(x=1/2\).
The sharper two-rate form (4) keeps the distinction between
the strongly decreasing profiles and the paid corrections.

This does not yet pay the adjacent ordinary compensation.
In equation (12) of
[the exact compensation note](research_mixed_fourier_right_taper_adjacent_compensation.md),
the replacement is precisely
\[
 \gamma_\eta\longmapsto\widehat\gamma_\eta .
 \tag{16}
\]
The original complex marginal and both maximum branches remain.
For example, at an actual ordinary type-four reference,
\(c\le-1/1000\). At \(x=1/2,H=0\) the new credit is
\(\widehat\gamma_1=\delta_+\), since \(\pi(-c)/10>\delta_+\).
The envelope residual proved in that note is consequently
still greater than
\[
             \frac1{7000}-\frac1{280000}
                        =\frac{39}{280000}>\frac1{8000}.
 \tag{17}
\]
This statement concerns the displayed upper envelope, not the
actual finite source. The stronger complete-cap estimate is
proved without a new evaluation; a sharper coupled action or
source comparison is still required for the boundary sign.
