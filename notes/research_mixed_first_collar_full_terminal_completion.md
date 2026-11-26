# The whole first collar with a complete mixed terminal source

Research deduction, 5 November 2026. Every fixed mixed three/four
open word of length at least three has a strict upper source gap on
its whole first collar, with independent unselected plateau
coordinates afterward. Both first selections and the physical
second type-four selection are included. The terminal polynomial,
of either type, is kept whole. The length-three cases use its
height-transport theorem directly; longer words use the completed
ordinary prefix. No new root, source comparison or numerical
computation is needed.

## 1. The literal sector and actual reference coverage

Fix an open word \(3+\epsilon_1,\ldots,3+\epsilon_m\),
where \(m\ge3\) and \(\epsilon_j\in\{0,1\}\). Write
\[
 h=m-1,\qquad \alpha=\epsilon_1,\quad\beta=\epsilon_2,\qquad
 r_j=a_j+ic_j\quad(1\le j\le h),\qquad
 \kappa=1/2500000.
 \tag{1}
\]
The references are the original complete-color critical point.
Take the fixed first collar \(0\le x_1\le\rho\) from the
first-pair comparisons and set
\[
 \begin{split}
 z_1&=x_1,\qquad z_2=y_2+ik,\qquad
 z_j=y_j+ic_j\quad(3\le j\le h),\\
 y_2&\in I_{3+\beta},\qquad
 I_3=[.267,.433],\quad I_4=[.24,.363],\\
 y_j&\in P=[.22,.45]\quad(3\le j\le h),\qquad
 d_j=y_j-a_j,\qquad X_j=e^{-2\pi iz_j}.
 \end{split}
 \tag{2}
\]
If \(\beta=0\), then \(\sigma_2=0\) and \(k\) lies
between \(c_2\) and zero. If \(\beta=1\), the two choices are
\[
 \sigma_2=0:\ c_2\le k\le0,\qquad
 \sigma_2=1:\ 0\le k\le H=7/500.
 \tag{3}
\]
Let \(\sigma_1\in\{0,\alpha\}\); all later retained selections
are zero. These are independent height ranges containing the
actual open hybrid contour. Its selected base is \(H\), and all
height cutoffs belong to \([0,1]\), as recorded in
[the second-four collar proof](research_mixed_second_four_cap_collar.md),
Section 1. On (2) all later real cutoffs are one. Selecting
coordinate two changes its own height, not the neighboring real
cutoffs, so the heights at positions three onward remain \(c_j\).

The exact contracted integrand is
\[
 \mathscr J_N=
 U_{\alpha,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)\,
 V_{\epsilon_m,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}
                  X_1^{-N\sigma_1}X_2^{-N\sigma_2}.
 \tag{4}
\]
The terminal alternatives and all terminal internal indices have
already been summed into the literal \(V_{\epsilon_m,N}\).
The original external scalar is
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), where
\(k_4=\sum_{j=1}^m\epsilon_j\) and \(|\kappa_N|=1\).

Every conditional block in (4) is ordinary. At length three,
the external inputs of vertex two are \(t_1\) and the attached
right-endpoint leg \(s_3\), as in
[actual factor coverage](research_mixed_open_local_factor_coverage.md),
Section 3. Both lie in their reduced typed disks. Neither private
leg \(s_1,t_3\) is substituted for these inputs. The full ordinary
image theorem therefore gives
\[
 \begin{array}{c|cc}
 \beta& a_2&c_2\\\hline
 0&(.267,.433)&(-.065,.068)\\
 1&(.24,.36)&(-.102,-.001).
 \end{array}
 \tag{5}
\]
This also holds at every larger length. The conditional block at
\(j=m-1\) may have an attached external input; it is included
in the completed ordinary theorem. These are full input-product
image estimates, not periodic repetitions or interior-window
assumptions.

## 2. Terminal planes, including negative-height attenuation

For terminal own type \(3+\epsilon\) and incoming type
\(3+\nu\), put
\[
 \begin{split}
 \Pi_{\epsilon,\nu}(a_*)&=P_\epsilon(a_*)-\nu g(a_*)/2,\\
 B_{\epsilon,\nu}(a_*;y)
 &=\Re\Pi_{\epsilon,\nu}(a_*)
    +\Re\Pi_{\epsilon,\nu}'(a_*)(y-\Re a_*)
                         -\kappa(y-\Re a_*)^2 .
 \end{split}
 \tag{6}
\]
The [completed mixed plateau theorem](research_mixed_full_unselected_plateau.md)
supplies the entire terminal source, for both own types, at the
actual incoming height:
\[
 |V_{\epsilon,N}(w,e^{-2\pi i(y+i\Im a_*)})|\,
 |d_N(e^{-2\pi i(y+i\Im a_*)})|^{\nu/2}
 \le C_\tau N^{A_\tau}e^{N(B_{\epsilon,\nu}(a_*;y)+\tau)}
                 \qquad(y\in P).
 \tag{7}
\]
Its Corollary 3 discharges the formerly conditional type-four
source on the necessary actual-reference domain; a discarded
auxiliary input is not restored by using (7).

At length three the incoming coordinate is coordinate two and its
height changes. For incoming type three, the
[common terminal height theorem](research_mixed_terminal_height_transport.md)
gives (7), without a Fourier weight, with the allowance
\[
 A_c(k)=
 \begin{cases}
 0,&c\le0,\ c\le k\le0,\\
 \pi(c-k),&c\ge0,\ 0\le k\le c.
 \end{cases}
 \tag{8}
\]
Its type-four-terminal hypothesis is now supplied by the same
completed source. The exact common incoming factor
\(X^{-i}p_i(X)\), its Poisson derivative, and its complex
current marginal are unchanged.

For incoming type four, write \(a_*=A+ic\), with
\(-.108<c\le-.001\), and \(a_k=y+ik\). The
[selected \(V_0\) theorem](research_mixed_terminal_three_selected_height_completion.md)
and [selected \(V_1\) theorem](research_mixed_terminal_four_selected_height_completion.md),
together with Corollary 2 of the latter, give
\[
 |V_{\epsilon,N}(w,e^{-2\pi ia_k})|\,
 |d_N(e^{-2\pi ia_k})e^{2\pi iNa_k\sigma}|^{1/2}
 \le C_\tau N^{A_\tau}e^{N(B_{\epsilon,1}(a_*;y)+\tau)}
 \tag{9}
\]
on \(c\le k\le0,\sigma=0\), and on \(0\le k\le H,\sigma=1\).
The selected halfweight rate is exactly
\[
 q_1(k)=\max\{-\Re g(y+ik)/2-\pi k,0\};
 \qquad q_0(k)=-\Re g(y+ik)/2\quad(k\le0).
 \tag{10}
\]
Thus (9) retains both original Fourier alternatives.

For clarity, the negative-height conclusion in (9) is a proof
on its own interval, not an inference from the selected interval.
Here are its finite-source ingredients, also recording the argument
needed when the terminal is type three.

* The original negative-path argument gives
  \[
   q_0(k)-q_0(c)
   \le\tfrac12\pi(k-c)(1/2-y)
   \le .01512\pi<.048.
   \tag{11}
  \]
  The actual-reference bare plane exceeds \(.99\). The coherent
  end-index majorant has rate \(.868\); for terminal type three,
  the positive low-, high- and near-half-Newton bounds have rate
  less than \(.879\). Their strict reserves survive (11).
  Remove whole coherent end-index sectors before restricting any
  inner index.
* At every physical transform index \(t\ge.15\),
  \[
   \partial_k\{R(t;k)+q_0(k)\}
    \le\pi(1/4-y/2-t)\le-\pi/100.
   \tag{12}
  \]
  The zero-safe finite product estimate transports the complete
  incoming-dependent factor. The fixed reference is away from
  height zero; any new zero at \(k=0\) improves the upper bound.
  An inner coherent coefficient is kept whole.
* At complex transform real part \(v\ge.18\), the allocated
  negative-path derivative is strictly negative. On the zero-mode
  strip \(.15\le v\le.18\), its transform derivative stays
  positive: the radial quantity is now
  \(e^{-2\pi k}\ge1>10/11\), strengthening the lower numerator
  estimates in the selected proofs. Push to \(v=.18\), then
  use negative-path transport. The actual index displacement
  supplies a strict reserve. For terminal three it exceeds
  \(\pi(.278-.18)^2/200>1/10000\); for terminal four it
  exceeds \(\pi(.246-.18)^2/200>1/20000\).
* Every penalized alias endpoint has its completed bare gap
  \(1/10\). Its possible increase is at most
  \[
   \pi(k-c)[3/4-3y/2-2v]_+
              \le .01296\pi<.041.
   \tag{13}
  \]
  Successive separate-height convexity controls the vertical
  sides and ordinary joins, retaining the linear alias penalties.
  No diagonal-height convexity is needed.
* In the low physical transform strip, use its exact one-inner-index
  residue and push to real \(t=.15\) before applying (12).
  Its inequality is independent of that inner coordinate and
  its alias penalty. The private or Newton exterior derivatives
  are incoming-independent. The right physical positive
  majorants use (12) termwise. Whole endpoint polynomials,
  support-wall zeros, even half-rows, and inward-cut slivers remain
  exactly in their original partitions.

These steps transport each current or previously justified physical
majorant separately. They never infer a bound for a changed
cancelling total sum from its value at one height. The exact
interpolants remain valid, and one total tolerance gives (9).
Both (7)--(9) hold on fixed small ordinary-color disks for both
level parities; Cauchy's formula supplies fixed ordinary derivatives.

All these planes are horizontal at the original reference height.
Relative to the complex affine plane, (9) would retain
\(\Im\Pi_{\epsilon,1}'(a_*)(k-c)\). No sign for that term is
asserted. The first-pair estimates used below are horizontal too,
so no imaginary tangent is discarded or charged anew.

## 3. The first-pair bounds and their exact allocation

Let \(\phi_{0\beta}\) be the original conditional phase with
one second Fourier halfweight and no first halfweight. Set
\[
 \begin{split}
 \Phi_{12}
 &=\mathcal T_\alpha(r_1,-2)
             +\phi_{0\beta}(r_1,r_2)-\alpha g(r_1),\\
 M_{12}&=\Re\Phi_{12},\qquad
 P_2=\partial_2\phi_{0\beta}(r_1,r_2),\qquad p=\Re P_2 .
 \end{split}
 \tag{14}
\]
This counts the full first Fourier weight and exactly one half
of the second weight. The literal pair modulus is
\[
 \mathcal B_N=
 |U_{\alpha,N}(w_L,X_1)C_{\beta,N}(X_1,X_2)
              d_N(X_1)^\alpha X_1^{-N\sigma_1}|\,
 |d_N(X_2)^\beta X_2^{-N\sigma_2}|^{1/2}.
 \tag{15}
\]
Its full-row upper rate \(U_{\alpha\beta}(k)\), before one
arbitrarily small final tolerance, satisfies
\[
 \begin{split}
 U_{\alpha0}(k)+A_{c_2}(k)
   &<M_{12}+p\,d_2-\delta_{\alpha0},
       &\delta_{00}&=3/100,\quad\delta_{10}=3/125,\\
 U_{\alpha1}(k)
   &<M_{12}+p\,d_2-1/20 .
 \end{split}
 \tag{16}
\]
These are the pair-only conclusions of
[horizontal tangent cancellation](research_mixed_first_collar_horizontal_tangent.md),
equations (12)--(13). For the second line subtract its allowance
\(13/2000\), obtaining \(87/2000+13/2000=1/20\).
It is also stated in
[enlarged type-four transport](research_mixed_four_enlarged_contour_transport.md),
equation (26).

The phase branch, its concavity and its uniform floor use the
actual attached first reference and the ordinary second height
in (5). Thus they apply at length three as well: the attached
third external input is covered by Section 1. The later ordinary
cut in the prefix theorems is not required for their pair-only
argument. Every first-cap private row and every first conditional
row is retained. The first selected monomial has modulus one on
the real collar, and the middle selected halfweight in (15) is
exactly (10).

## 4. Longer words: attach the complete terminal to the ordinary prefix

Suppose \(m\ge4\), so \(h=m-1\ge3\). Take the prefix
\(\mathcal L_{h,N}\) with its one remaining cut halfweight in
[the completed three-row assembly](research_mixed_three_row_source_assembly.md),
Section 3. Its equation (11) gives
\[
 \begin{split}
 \frac1N\log\mathcal L_{h,N}
 \le{}&M_h+\Re P_{h,b}d_h-\delta_{\alpha\beta}+\tau\\
 &-\kappa\left(d_2^2+
             2\sum_{j=3}^{h-1}d_j^2+d_h^2\right)
                  +O_m(\log N/N),\\
 \delta_{00}&=3/100,\quad\delta_{10}=3/125,\quad
 \delta_{01}=\delta_{11}=4/125 .
 \end{split}
 \tag{17}
\]
All ordinary real-row excesses in that result are zero by the
completed half- and last-row comparisons. For \(\beta=1\),
the fixed \(9/500\) transport allowance is paid once on edge
three from the \(1/20\) pair reserve. No fixed loss is paid
again at later edges.

Since coordinate \(h\) is unselected and at height \(c_h\),
apply (7) with \(a_*=r_h\), \(\nu=\epsilon_h\) and
\(\epsilon=\epsilon_m\). Original stationarity and action
calibration give
\[
 M_h+\Re\Pi_{\epsilon_m,\epsilon_h}(r_h)=M_{\rm open},
 \qquad P_{h,b}+\Pi_{\epsilon_m,\epsilon_h}'(r_h)=0.
 \tag{18}
\]
The two cut halfweights multiply to its original full weight.
Combining (17) and (7) therefore bounds (4) by the rate
\[
 M_{\rm open}-\delta_{\alpha\beta}
 -\kappa\left(d_2^2+2\sum_{j=3}^{h}d_j^2\right)+\tau,
 \tag{19}
\]
with its polynomial prefactor. This uses the entire terminal
polynomial, not only its end-index contribution.

## 5. Length three: the moved second coordinate is the terminal input

For \(m=3\), the prefix before the terminal consists only of
the pair (15). Put \(\epsilon=\epsilon_3\).
The two exact allocated identities are now
\[
 P_2+\Pi_{\epsilon,\beta}'(r_2)=0,\qquad
 M_{12}+\Re\Pi_{\epsilon,\beta}(r_2)=M_{\rm open}.
 \tag{20}
\]
If \(\beta=0\), multiply the first line of (16) by the
terminal bound (7) with allowance (8). This allowance occurs
once, already paid by that pair inequality. If \(\beta=1\),
multiply the second line of (16) by (9), for either physical
selection. Again two middle halfweights give the literal factor
\(d_N(X_2)X_2^{-N\sigma_2}\).

The real tangents cancel by (20). The resulting rate is
\[
 M_{\rm open}-\Delta_{\alpha\beta}^{(3)}
               -\kappa d_2^2+\tau,\qquad
 \Delta_{00}^{(3)}=3/100,\quad
 \Delta_{10}^{(3)}=3/125,\quad
 \Delta_{01}^{(3)}=\Delta_{11}^{(3)}=1/20.
 \tag{21}
\]
No imaginary fee is inferred to vanish; both source bounds being
combined were horizontal from the start. This proves the whole
first-collar comparison for all eight length-three words, with
both middle selections when its type is four. In particular the
four words \((3+\alpha,4,3+\epsilon)\) retain loss \(1/25\)
after one total tolerance less than \(1/100\).
Their original scalar is
\(\kappa_N^{\alpha+\epsilon+4}N^{\alpha+\epsilon+3}\);
at \(\epsilon=0\) it is
\(\kappa_N^{\alpha+4}N^{\alpha+3}\).

## 6. Uniform sector statement and its limits

**Theorem.** For every fixed mixed word of length \(m\ge3\),
on the first-collar sector (2)--(3), the entire contracted
integrand (4) satisfies, for every \(\tau>0\),
\[
 |\mathscr J_N|\le C_\tau N^{A_\tau}
 \exp N\left\{M_{\rm open}-\Delta_{\alpha\beta}^{(m)}
       -\kappa\left(d_2^2+2\sum_{j=3}^{m-1}d_j^2\right)
       +\tau\right\}.
 \tag{22}
\]
For \(m=3\), use the constants in (21); for \(m\ge4\),
use \(\Delta_{\alpha\beta}^{(m)}=\delta_{\alpha\beta}\)
from (17). All constants are at least \(3/125\), so one
total tolerance less than \(1/250\) leaves the common strict
finite loss \(1/50\). Both first selections, both physical
second-four selections, both terminal types, and every sufficiently
large integer level of either parity are included.

The estimate holds on fixed sufficiently small ordinary-color disks
at both ends. Every fixed ordinary-color derivative satisfies the
same rate on smaller disks. For the fixed word, choose individual
factor tolerances with sum less than \(\tau\), including all
color perturbations, and apply Cauchy's formula. There is no
per-edge fixed rate charge.

On the actual hybrid graph, (3) contains its realized second
height pointwise, and the later heights are unchanged. Its fixed
graph measure is bounded almost everywhere. Integration over this
sector and multiplication by the original scalar following (4)
therefore change only the polynomial prefactor. Thus its full
contribution is exponentially below the central reference action,
with the same stated gap.

This theorem requires the second real coordinate in its interval
\(I_3\) or \(I_4\), and the entire later retained suffix to be
unselected in \(P\). It does not cover later selections or
nonplateau suffix coordinates. At length two the first collar is
also the terminal incoming coordinate and lies near zero, outside
the terminal input plateau; that case requires a separate argument.
Only the specified left collar is used here. No reflection identity,
whole open-word asymptotic, ordinary-knot conclusion, or stability
under arbitrary short partial fillings is inferred from this sector.
