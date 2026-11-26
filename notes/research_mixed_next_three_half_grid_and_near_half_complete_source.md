# The complete half-grid side and upper near-half source

Private finite-source assembly, 8 November 2026. The complete incoming
source is paid on the half-grid vertical and the full upper near-half
interval. Every component, including the incoming-corner theorem,
has completed its source and proof reviews.

The assembly retains the complete first incoming cycle, the unchanged
old filter, both original factors of \(N\), and both short horizontal
grid corrections separately. It supplies no estimate for the coherent
middle physical insertion. No mathematical numerical evaluation,
saved-value calculation, or modification of a frozen source is used.

## 1. Actual references and the literal finite source

Take an actual complete word in the original powers three and four,
beginning \(343\), of length \(m\ge5\). Retain its original coupled
reference
\[
 (a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),
 \qquad h_a=\Im a_*,\quad c=\Im y_*,\quad h_z=\Im z_*,
 \qquad H=1/100 .
 \tag{1}
\]
Every other private height and every reference correlation is kept
as in the component sources. In particular
\[
 7/10<e^{2\pi c}<41/50,\qquad -.072<h_a<0,\qquad
 -.03<\Im t_*,h_z<.02 .
 \tag{2}
\]
Use the same ordinary color \(w\in[-2,2]\), output
\[
 z=u+ih_z,\qquad 3/10\le u\le39/100,\qquad Z=e^{-2\pi iz},
 \tag{3}
\]
affine rate \(\Lambda_{123}(z)\), and original action
\(\mathcal P_0^+(w,z)\). In particular
\[
 \Lambda_{123}(z_*)=\Re\mathcal P_0^+(-2,z_*).
 \tag{4}
\]
The real output interval in (3) is the actual inherited \(j=3\)
window. Neither (2) nor (3) replaces the coupled reference by an
independent containing box. Length-four words and terminal \(343\)
are outside this assertion.

For \(D=N-1\), \(r=e^{-2\pi i/N}\), retain
\[
 \begin{split}
 P_j&=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\\
 U_{0,N}(w,X)&=\sum_{j=0}^{D}H_N(w,r^{-j})p_j(X)/P_j,\\
 C_{\beta,N}(V,W)&=\sum_{j=0}^{D}
       \frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}},\\
 F_N(w,Y)&=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 F_N^{\rm mid}&=F_N-E_N^{\rm filt},\qquad
 Y=e^{-2\pi iy}.
 \end{split}
 \tag{5}
\]
Here \(H_N\) is the original coherent coefficient. The full forced
polynomial \(d_N\), of degree at most \(D\), has its original values
\(d_N(r^b)=P_b^{-1}\). The correction \(E_N^{\rm filt}\) is exactly
the old first-coordinate deletion and shared-node interpolation
correction in
[the right paired rectangle](research_mixed_next_right_paired_terminal_insertion.md),
equation (3). Thus the same lower cutoff
\(l_N=\lfloor\delta N\rfloor\), with the original fixed
\(0<\delta<1/40\), upper cutoff
\(B_N=\lceil11N/12\rceil\), and first-coordinate cutoff
\(A_N=\lceil23N/24\rceil\) are retained. No filter is applied to an
individual incoming path.

For \(A=F,\mathrm{mid}\), let
\[
 K_N^A(y)=
 \frac{N F_N^A(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},
 \qquad F_N^F=F_N .
 \tag{6}
\]
There is no outgoing halfweight for the next own-three factor.
The factor \(N\) in (6) is distinct from the incoming constant-mode
factor in (5). This is the original conditional-message
normalization; no new outgoing ordinary-boundary scalar is inserted.

Set
\[
 M_N=\lceil N/2\rceil,\qquad
 L_N=(M_N-\tfrac12)/N,\qquad L_N\le\tfrac12 .
 \tag{7}
\]
For either density (6), define the actual currents
\[
 \begin{split}
 V_N^A&=i\int_c^H K_N^A(L_N+ih)\,dh,\\
 J_{N,-}^A&=\int_{[L_N,1/2]+ic}^{\longrightarrow}
                       K_N^A(y)\,dy,\\
 J_{N,+}^A&=\int_{[L_N,1/2]+iH}^{\longrightarrow}
                       K_N^A(y)\,dy,\qquad
 J_N^{A,\rm grid}=J_{N,-}^A-J_{N,+}^A .
 \end{split}
 \tag{8}
\]
At odd \(N\), both short horizontal currents are zero. At even
\(N\), they each have length \(1/(2N)\). Their small length is
not used as a substitute for a source estimate.

**Theorem.** Uniformly for the actual references above, all real
ordinary colors \(w\in[-2,2]\), both level parities, and all sufficiently
large \(N\), there are constants \(C,B\) such that:

1. The complete selected densities satisfy
\[
 \left|F_N^A(w,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z)\right|
   +|K_N^A(y)|
 \le C N^B e^{N\{\Lambda_{123}(z)-1/20000\}},
 \quad y=q+iH,\quad 9/20\le q\le1/2 ,
 \tag{9}
\]
for \(A=F,\mathrm{mid}\).
2. The complete half-grid densities and their actual currents satisfy
\[
 \begin{split}
 |K_N^A(L_N+ih)|
   &\le C N^B e^{N\{\Lambda_{123}(z)-10^{-13}\}},
                       &&c\le h\le H,\\
 |V_N^A|+|J_{N,-}^A|+|J_{N,+}^A|
   &\le C N^B e^{N\{\Lambda_{123}(z)-10^{-13}\}} .
 \end{split}
 \tag{10}
\]
The pointwise bound in (10) also holds on each short horizontal
path in (8). Integrating (9) over any subinterval, in either
orientation, preserves its exponential bound.

For the complete numerator, (10) also gives directly
\[
 |F_N^A(w,Y)d_N(Y)C_{0,N}(Y,Z)|
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-13}\}},
 \qquad y=L_N+ih,\quad c\le h\le0 .
 \tag{10a}
\]
Indeed this numerator equals \((1-Y^N)K_N^A/N\), and
\(|1-Y^N|=1+e^{2\pi Nh}\le2\) there. This is an exact
consequence for either \(A=F,\mathrm{mid}\), with the full
forced weight still present.

The constants have the same uniform reference scope as the
component theorems. The reference, contour heights and integer cuts
are fixed when forming each source. No outside complex-neighborhood,
mixed-jet, nonzero-coefficient, or whole-transfer conclusion is
made here.

## 2. The exact incoming cycle and the far real segment

The original increasing contour is
\[
 \begin{split}
 \Gamma_{\rm in}&=[0,1/10],\\
 \Gamma_{\rm tap}&:
     a=x+ih_a(x-1/10)/(3/25),\qquad 1/10\le x\le11/50,\\
 \Gamma_{\rm cen}&=[11/50,9/20]+ih_a,\\
 \Gamma_H&=[9/20,1/2]+ih_a,\\
 \Gamma_C&=[1/2+ih_a,1/2]\ \cup\ [1/2,7/10],\\
 \Gamma_{\rm far}&=[7/10,1].
 \end{split}
 \tag{11}
\]
In particular the vertical part of \(\Gamma_C\) points upward.
The taper has its literal measure
\(da=(1+ih_a/(3/25))\,dx\). The concatenation runs from zero
to one with no omitted side.

For each piece put
\[
 F_N^\Gamma(w,Y)=
 N\int_\Gamma U_{0,N}(w,e^{-2\pi ia})
                      C_{1,N}(e^{-2\pi ia},Y)\,da .
 \tag{12}
\]
The finite integrand is an entire periodic function of \(a\).
The exact constant-mode identity therefore gives
\[
                      F_N=\sum_{\Gamma\ {\rm in}\ (11)}F_N^\Gamma
 \tag{13}
\]
at every shared coordinate used here. This is the identity in
[the complete lower-half assembly, Section 2](research_mixed_next_three_actual_complete_lower_left.md);
it is not restricted to that note's lower shared height.

The far real segment needs no new contour comparison. The complete
disk source in
[incoming ends, equation (14)](research_mixed_next_three_selected_left_incoming_ends.md)
gives
\[
 \sup_{\substack{a\in[7/10,1]\\ |Y|\le1\\-2\le w\le2}}
 |U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)|
                \le C N^B e^{153N/100}.
 \tag{14}
\]
For each \(a,w\), this product is a polynomial in \(Y\) of degree
at most \(D\). Its reciprocal-polynomial maximum principle gives
throughout \(|Y|\le e^{\pi/50}\)
\[
 |U_{0,N}C_{1,N}|
 \le C N^B e^{N\{153/100+\log_+|Y|\}}
 \le C N^B e^{N(B_f-1/100)},\qquad
 B_f=77/50+\pi/50 .
 \tag{15}
\]
The radius bound contains the entire vertical and both grid paths,
as well as the fixed top interval.

Apply
[half-grid bounded prefix, Theorem 1](research_mixed_next_three_half_grid_bounded_prefix.md)
to the whole preceding factor in (15). It attaches the complete
next kernel and full forced weight, with gap \(1/1000\), on
each required domain. Integrating in \(a\), with the original
factor \(+N\), proves the same exponential gap for the far
contribution. This argument retains all first physical rows and
all true endpoint terms before attachment; it does not recover
them from a coherent partial-sum bound.

## 3. Assembling the complete half-grid current

The component estimates for (12), with the following factor and
paired denominator attached, are:

| Incoming contribution | Complete finite gap on the vertical and both grid horizontals | Source |
| --- | --- | --- |
| Initial segment and taper, separately | \(10^{-12}\) | [Initial/taper half-grid theorem](research_mixed_next_three_half_grid_incoming_initial_taper.md) |
| Central horizontal | \(10^{-12}\) | [Central half-grid theorem](research_mixed_next_three_central_half_grid_vertical.md) |
| Right incoming horizontal | \(10^{-12}\) | [Right-horizontal half-grid theorem](research_mixed_next_three_half_grid_incoming_right_horizontal.md) |
| Combined oriented corner | \(10^{-12}\) | [Incoming-corner theorem](research_mixed_next_three_half_grid_incoming_corner.md) |
| Far real segment | \(1/1000\) | Equations (14)--(15) and bounded-prefix attachment |

In the corner row the original integral is first replaced, by
Cauchy's theorem for the entire finite integrand, with the paid
horizontal-and-vertical path. Only their oriented integral is
identified with \(F_N^{\Gamma_C}\). No absolute estimate for either
of the two old corner sides separately is being used.

Each component keeps the complete first and next physical
partitions, both horizontal aliases, all weighted sides, both
unweighted joins, and all period or numerator-wall terms required
by its canonical identity. Those statements are established before
the component sums are bounded. The source factors external to the
incoming variable are independent of \(a\). Hence (13) is also the
exact identity after multiplication by
\(N d_N C_{0,N}/(1-Y^N)\).

The finite sum of the component bounds proves (10) for \(A=F\).
The complete central, initial/taper, right-horizontal and corner sources
have a reserve \(10^{-12}\); the displayed final reserve
\(10^{-13}\) is conservative. The old corner contour is used only
in its exact union, without separately bounding its two old pieces.

For clarity, the source-level denominator control is the original
one, not a holomorphic weight substitution. On the actual half-grid,
\[
 Y^N=-e^{2\pi Nh},\qquad |1-Y^N|=1+e^{2\pi Nh}.
 \tag{16}
\]
The full forced estimate has rate
\(\max\{-\Re g(y),\,2\pi(\Im y)_+\}\).
Since \(\Re g(L_N+ih)=O(N^{-1})\), (16) cancels this rate
with only an arbitrarily small finite tolerance. The denominator
equals two at \(h=0\), so no pole is crossed or deleted there.
At the lower and upper grid horizontals its modulus is respectively
at least \(1-R_*^N\) and \(e^{\pi N/50}-1\).
The inherited zero-safe estimates cover the actual
\(O(N^{-1})\) displacement \(L_N-1/2\), including the numerator
wall, at a cost \(O(\log N)\) in the exponent before division
by \(N\). The two horizontal sources are thus bounded separately;
their opposite signs in (8) remain unchanged.

## 4. The complete upper near-half interval

Use the following complete selected component estimates, each
with \(d_N(Y)Y^{-N}C_{0,N}(Y,Z)\) attached:

| Incoming contribution | Finite gap for every \(9/20\le q\le1/2\) | Source |
| --- | --- | --- |
| Initial segment, taper, and right horizontal, separately | \(1/10000\) | [Near-half incoming paths](research_mixed_next_three_selected_near_half_incoming_paths.md) |
| Central horizontal | \(1/2000\) | [Near-half central source](research_mixed_next_three_selected_near_half_central.md) |
| Combined oriented corner | \(1/4000\) | [Incoming-corner theorem](research_mixed_next_three_half_grid_incoming_corner.md) |
| Far real segment | \(1/1000\) | Equations (14)--(15) and bounded-prefix attachment |

These estimates concern the full fixed interval; none is inferred
from a shrinking even-level grid segment. The endpoint comparisons
in their proofs retain both original selected weight alternatives
\[
              -\Re g(y)-2\pi H,\qquad 0 .
 \tag{17}
\]
The complete forced polynomial is summed only after both alternatives
have been bounded. Equation (13), with the outside factor attached,
proves the selected-density part of (9) for \(F_N\).

At the top height the exact identity is
\[
 K_N^A(y)=-
 \frac{N F_N^A(w,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z)}
      {1-Y^{-N}},
 \qquad |1-Y^{-N}|\ge1-e^{-\pi N/50}.
 \tag{18}
\]
The denominator is at least \(1/2\) for sufficiently large \(N\).
The remaining \(N\) is the original shared observation factor;
it changes only the polynomial prefactor. This proves the
meromorphic-density conclusion and its integral consequence.

## 5. The original filter and the exact signed right contour

The old correction has degree at most \(D\) in \(Y\) and the
complete unit-disk bound
\[
 \sup_{|Y|\le1}|E_N^{\rm filt}(w,Y)|
       \le C N^B e^{77N/50},\qquad -2\le w\le2 .
 \tag{19}
\]
Section 5 of
[the bounded-prefix half-grid theorem](research_mixed_next_three_half_grid_bounded_prefix.md)
continues (19) to the preceding-factor allowance \(B_f\) throughout
\(|Y|\le e^{\pi/50}\), and pays its complete attached density on
the top interval, the full vertical, and both grid horizontals,
with gap \(1/1000\).

Writing the literal correction density as \(K_N^{\rm filt}\),
the exact identities are
\[
 \begin{split}
 K_N^{\rm mid}&=K_N^F-K_N^{\rm filt},\\
 V_N^{\rm mid}&=V_N^F-V_N^{\rm filt},\\
 J_{N,\pm}^{\rm mid}&=J_{N,\pm}^{F}-J_{N,\pm}^{\rm filt}.
 \end{split}
 \tag{20}
\]
Combining this bound with Sections 3--4 proves (9)--(10) for the
unchanged filtered source. In particular it pays
\(V_N^{\rm mid}-J_N^{\mathrm{mid},\rm grid}\) with the same
conservative half-grid gap. Both Fourier sectors and their signs
are retained throughout.

To record exactly what this removes, let
\[
 \begin{split}
 \mathscr H_N(1/2)&=
   \int_{[1/2,1]+ic}^{\longrightarrow}K_N^{\rm mid}(y)\,dy
   -\int_{[1/2,1]+iH}^{\longrightarrow}K_N^{\rm mid}(y)\,dy,\\
 V_N(1)&=i\int_c^H K_N^{\rm mid}(1+ih)\,dh,\\
 \mathscr R_N^{\rm cl}&=
      \int_{\partial([L_N,1]+i[c,H])}^{\rm CCW}
                                      K_N^{\rm mid}(y)\,dy .
 \end{split}
 \tag{21}
\]
The original old-filter seam is removable. The exact orientation
identity is
\[
 \mathscr H_N(1/2)
 =\mathscr R_N^{\rm cl}-V_N(1)
               +V_N^{\rm mid}-J_N^{\mathrm{mid},\rm grid}.
 \tag{22}
\]
There is no extra \(N\) outside the closed integral: it is already
in \(K_N^{\rm mid}\). Its residue expression remains
\[
 \mathscr R_N^{\rm cl}
   =\sum_{b=M_N}^{B_N-1}
       \frac{F_N^{\rm mid}(w,r^b)}{P_b}\,
                         C_{0,N}(r^b,Z).
 \tag{23}
\]
Thus (10) removes the half-period side and the grid adjustment
from this signed reduction, with their original signs. Equation
(9) separately pays the fixed top interval
\([9/20,1/2]+iH\). Neither operation removes the coherent physical
sum (23), identifies an open horizontal integral with it without
the other terms of (22), or supplies a lower bound for the full
transfer. The previously established periodic-seam estimate and
paid physical subranges may be combined only on their stated
common domains. No new conclusion about the remaining middle
insertion or full volume identity is asserted.
