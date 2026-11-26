# High Newton coefficients from the original terminal-three source

Research deduction, 7 November 2026. The full Newton coefficients of
the ordinary \(33\) source have rate below \(153/100\) for \(b\ge8N/9\).
Their exact high-index observation uses a single-three two-boundary
kernel near its positive spectral endpoint. We bound that restricted
kernel by inserting a finite polynomial into the complete
terminal-three contour proof. The global maximum of the single-three
two-boundary kernel is not used.

The result pays the combined physical \(b\ge8N/9\) band in the next
\(343/344\) transfer. It does not separately estimate the two Fourier
coefficients or identify physical rows with a contour arc.
No numerical evaluation or certificate replay is used.

## 1. The exact high-index observation

Use the original full Newton algebra and Frobenius trace:
\[
 \begin{gathered}
 D=N-1,\ q=e^{\pi i/N},\ r=q^{-2},\\
 \kappa=q^{D^2/2},\ \eta=(-1)^D,\\
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\\
 c_j=2\cos((2j+1)\pi/N),\\
 e_j(z)=S_j^{-2}\prod_{\nu<j}(c_\nu-z),\\
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f .
 \end{gathered}                                                   \tag{1}
\]
The crossing polynomial \(R\), its matrix \(M\), and reversal \(J\)
keep their original conventions. Write \(A_3=JM^3\), \(v=(e_0,\ldots,e_D)^T\),
and
\[
 \ell_b(w)=(v(w)^TA_3^2)_b,\quad
 \mathcal K_{3,N}(w,z)=v(w)^TJM^3v(z),\quad
 K_N(z,t)=\sum_{\ell=0}^{D}e_\ell(z)e_\ell(t).
                                                                  \tag{2}
\]
Transposes are bilinear. Since \(\phi_N(e_i e_j)=J_{ij}\),
\[
 \mathcal K_{3,N}(w,z)=\phi_N^{(t)}[R^3K_N(w,t)K_N(z,t)],
 \qquad
 \ell_b(w)=\phi_N^{(t)}[\mathcal K_{3,N}(w,t)e_b(t)R(t)^3].
                                                                  \tag{3}
\]
These identities retain the original double-root normal data.

For \(2b\ge N\), put \(n=D-b<\lfloor N/2\rfloor\). The existing
[high Newton radical contraction, Theorems 1--2](research_high_newton_radical_contraction.md)
gives the exact coefficients
\[
 b_{nj}=(-1)^{n+j}
 \frac{2\sin((2j+1)\pi/N)S_n^2}{S_{n-j}S_{n+j+1}},
 \qquad 0\le j\le n,\qquad |b_{nj}|\le2 .
                                                                  \tag{4}
\]
Every denominator index is below \(N\). Applying that original
identity to (3) yields
\[
 \boxed{\quad
 \ell_b(w)=\sum_{j=0}^{N-b-1}
      b_{D-b,j}R(c_j)^3\mathcal K_{3,N}(w,c_j),
                    \qquad 2b\ge N .
 \quad}                                                         \tag{5}
\]
This contraction includes the original double-root normal:
the radical insertion consumes it, leaving the spectator's value.
The odd simple node contributes zero. The actual eigenvalues are
\(R(c_j)=\kappa(-1)^j q^{j(j+1)}\), of unit modulus.
Thus (4)--(5) reduce the coefficient bound to the restricted kernel
with cost at most \(2(N-b)\). The radical identity is an existing
input; the new estimate below concerns its terminal-source insertion.

## 2. The entire insertion on all old trace contours

For \(0\le j\le N/9\), physical termination gives exactly
\[
 \mathcal B_{j,N}(t):=K_N(c_j,-2\cos t)
       =\sum_{\ell=0}^j e_\ell(c_j)e_\ell(-2\cos t).
                                                                  \tag{6}
\]
The coefficients are nonnegative and have the product
\[
 e_\ell(c_j)=\prod_{k=0}^{\ell-1}
 \frac{\sin(\pi(j-k)/N)\sin(\pi(j+k+1)/N)}
      {\sin^2(\pi(k+1)/N)}.
                                                                  \tag{7}
\]
Reorder the first numerator product. Since \(\sin u/u\) decreases
on \((0,\pi)\), comparison with the corresponding denominator factors
proves
\[
 e_\ell(c_j)\le\binom j\ell\binom{j+\ell}{\ell},\qquad
 \sum_{\ell=0}^j e_\ell(c_j)
       \le\sum_{\ell=0}^j\binom j\ell2^{j+\ell}=6^j.              \tag{8}
\]
Every factorial index is below \(N\).

All trace contours in the
[complete terminal-three theorem](research_three_crossing_terminal_filling.md)
have \(|\Im t|\le h_t\), where
\[
 h_t=2\operatorname{arsinh}\sqrt{(\sqrt2-1)/4},\qquad
 \cosh h_t=(1+\sqrt2)/2<5/4=\cosh(\log2).                       \tag{9}
\]
On the larger fixed strip \(|\Im t|\le\log2\), every numerator
factor of \(e_\ell(-2\cos t)\) has modulus at most \(9/2\).
Also \(S_\ell\ge S_j\) for \(\ell\le j\le N/9\), because every
intervening sine factor is less than one. Hence
\[
 \boxed{\quad
 \sup_{|\Im t|\le\log2}|\mathcal B_{j,N}(t)|
                          \le27^j/S_j^2.
 \quad}                                                         \tag{10}
\]
The fixed strip margin gives the same bound, up to fixed constants,
for all fixed \(t\)-derivatives on the original trace contours.
This bounds the entire inserted polynomial, not a partial trace.

Put \(J_0(u)=\int_0^u\log(2\sin\pi s)\,ds\). The uniform
sine-factorial estimate, including zero, gives
\[
 |\mathcal B_{j,N}|\le CN^A e^{NE(j/N)},\qquad
 E(u)=u\log27-2J_0(u).
                                                                  \tag{11}
\]
This function increases on \([0,1/9]\). The sine chord
\(2\sin\pi s\ge6s\) through \(s=1/6\) proves
\[
 E(1/9)\le\frac19\{\log27+2+2\log(3/2)\}
 <\frac19\left\{\frac{33}{10}+2+\frac{82}{100}\right\}
 =\frac{17}{25}.                                                 \tag{12}
\]
The existing finite exponential-series witness gives
\(\log3<11/10\). For the other comparison, explicitly
\[
 e^{41/100}>
 1+\frac{41}{100}+\frac{1681}{20000}+\frac{68921}{6000000}
       =\frac{9033221}{6000000}>\frac32 .
                                                                  \tag{13}
\]
These are written elementary inequalities, not new profile evaluations.

## 3. Full terminal-source accounting

Let \(M_{\rm term}\) be the single **terminal** three action.
It differs from the global single-three two-boundary action.
The saved
[central-phase certificate](../repro/results/research-terminal-three-central-phase.json),
SHA256 ac360f2d1409f1806d8765292ed219405153bff39496f07f37b3f1ad9a74635a,
records
\[
 M_{\rm term}\in
 [\,0.848851228500887723385626533073631
                         \ \mathord{+/-}\ 4.59\,10^{-34}\,].
                                                                  \tag{14}
\]
We use only its consequence \(M_{\rm term}<17/20\).
The finite-source terminal theorem, not this phase certificate alone,
provides the contour estimates below.

For each \(\tau>0\), that full proof with insertion (6) gives
\[
 |\mathcal K_{3,N}(w,c_j)|
 \le C_\tau N^{A_\tau}
 e^{N\{M_{\rm term}+E(j/N)+\tau\}},\qquad j\le N/9,               \tag{15}
\]
uniformly for all real \(w\in[-2,2]\), and on a sufficiently small
fixed complex disk about \(-2\). The complete accounting is as follows.

**Removed wire rows.** The old cuts are
\(\alpha=3/32,\beta=13/32\). A removed row is
\[
       e_k(w)\phi_N[R^3e_k K_N(c_j,\cdot)] .                    \tag{16}
\]
We do not multiply an estimate of the signed coefficient
\(\phi_N(R^3e_k)\). Instead apply the exact derivative-sampling
formula for \(\phi_N(R^3f)\). Its real crossing chirp has modulus
one and derivative of polynomial size. Markov on the polynomial
\(e_k K_N(c_j,\cdot)\), whose degree is at most \(D+j=O(N)\),
bounds its derivative by its real-interval supremum with polynomial
cost. The original full real Newton estimates are
\[
 \sup_t|e_k(-2\cos t)|\le CN^A e^{Ng(k/N)}\ (2k<N),\qquad
 \sup_t|e_k(-2\cos t)|\le CN^A\ (2k\ge N),
 \quad g(u)=J_0(2u)-4J_0(u).
                                                                  \tag{17}
\]
Thus (10) bounds the removed low rows by
\(2g(\alpha)+E(j/N)+o(1)\), and the removed high rows by
\(E(j/N)+o(1)\). The old strict inequality
\(2g(\alpha)<M_{\rm term}-19/1000\) pays the whole group.
The old Bernstein enlargement permits a small complex \(w\)-disk
at an arbitrary extra tolerance. Both the odd simple node and every
double-root derivative are retained.

**Removed angular nodes.** For the retained old wire kernel,
\(|t|\ge T_N=2\pi/3+O(N^{-1})\) has the absolute rate
\(\psi(2\pi/3,0)<4/5<M_{\rm term}\). Multiplication by (6)
adds (11). Markov on the same spectral interval controls the
derivative sampling at degree at most \(D+j\). Hence the entire
removed angular sum retains its old rate plus \(E(j/N)+\tau\).
No complete signed-trace bound is assigned to a partial trace.

**Retained contours.** In the exact trace rectangle, equation (13)
of the terminal theorem, the insertion multiplies the old kernel.
It is even in \(t\), so the oddness combining the two angular
connectors is unchanged. In the subsequent one-sided wire formula,
equation (16) there, it is independent of the wire variable.
It is therefore an exact amplitude on the upper main rectangle,
both horizontal wire aliases, both full wire-cut currents, both
angular connectors and all their nested wire-endpoint surfaces.
Every trace point has \(|\Im t|\le h_t\), so (10)--(11) apply.
The original rational trace kernel and its full higher-charge
remainder also retain their old bounds times this amplitude.

**Initial angular connector.** At height \(O(N^{-1})\), keep the
old whole truncated wire polynomial, as in Section 5 of that theorem.
Its rate \(\psi(2\pi/3,0)+O(N^{-1/2})\) acquires only (11).
The strict old gap absorbs the subexponential factor.
No rational wire currents are separated at height zero.

The upper main rectangle has phase at most \(M_{\rm term}\);
all other retained contours have smaller bounds. The insertion need
not be slowly varying or nonzero, since only an upper bound is
claimed. The original real-parent phase inequality supplies uniform
all-real-color bounds on the retained surfaces. Together with the
removed groups, this proves (15). It is not an inference from the
terminal value at complete color alone.

Equations (12), (14), and (15) give
\[
 M_{\rm term}+E(j/N)<\frac{17}{20}+\frac{17}{25}
          =\frac{153}{100}.
                                                                  \tag{18}
\]
The strict inequalities leave a fixed positive reserve. Choose the
total finite and color allowance inside it.

**Theorem 1.** At every sufficiently large level of either parity,
\[
 |\ell_b(w)|\le CN^A e^{153N/100},
 \qquad \lceil8N/9\rceil\le b<N,\quad w\in[-2,2].
                                                                  \tag{19}
\]
The same bound holds on a small fixed complex disk about \(-2\),
with every fixed ordinary derivative and polynomial cost.
Indeed (5) has \(j<N-b\le N/9\), and (4), (18) prove (19).
Markov on the complete polynomial proves the real derivative bound;
Cauchy on a slightly larger fixed disk proves the local one.
All original ordinary normal coordinates remain.
The saved pendant action exceeds \(153/100\), by
[action calibration, Section 6](research_three_crossing_action_volume_calibration.md),
so (19) lies strictly below it. No separate preparation-error bound
or nonzero inserted coefficient is asserted.

The same conclusion is uniform in a second signed crossing power.
For every integer \(m\), possibly depending on \(N\), set
\[
 A_m=JM^m,\qquad
 \ell_b^{(m)}(w)=(v(w)^TA_3A_m)_b.
\]
The Frobenius identity and the same radical contraction give exactly
\[
 \ell_b^{(m)}(w)
 =\phi_N[\mathcal K_{3,N}(w,\cdot)e_bR^m]
 =\sum_{j=0}^{N-b-1}
          b_{D-b,j}R(c_j)^m\mathcal K_{3,N}(w,c_j).
                                                                  \tag{19a}
\]
Consequently (19), including its ordinary derivatives and fixed
complex-color disk, holds with constants independent of \(m\).
The specialization \(m=3\) is the coefficient used below. This is
uniformity of the exact observed source, not a claim about a complete
filled-word asymptotic.

## 4. The actual next transfer

Keep \(P_j=(r;r)_j\) and the full conditional kernel
\[
 C_{\beta,N}(Y,Z)=\sum_{k=0}^{D}
       \frac{Y^{-k}p_k(Y)p_k(Z)}{P_k^{2+\beta}},\qquad \beta=0,1.
                                                                  \tag{20}
\]
The exact lowered-word identity is
\[
 \mathcal F_{\beta,N}(w,Z)=
 \frac1{\kappa^2N}\sum_{b=0}^{D}
              (-q)^b\ell_b(w)C_{\beta,N}(r^b,Z).
                                                                  \tag{21}
\]
It includes both Fourier sectors; \(P_b\) cancels only by this identity.
For \(b\ge\lceil8N/9\rceil\), put \(n=D-b<N/9\).
The support in (20) is exactly \(k\le n\), and reflection gives
\[
 |p_k(r^b)|/S_k=S_{b+k}/(S_bS_k)\le\binom nk .
                                                                  \tag{22}
\]
On \(|Z|\le3\), use \(|p_k(Z)|\le4^k\). Uniform factorial bounds
and the decrease of \(J_0\) on \([0,1/9]\) imply
\[
 |C_{\beta,N}(r^b,Z)|
 \le\sum_{k=0}^{n}\binom nk\frac{4^k}{S_k^{1+\beta}}
 \le CN^A e^{-N(1+\beta)J_0(1/9)}5^n .
                                                                  \tag{23}
\]
All zeros and endpoint rows remain. The same written inequalities give
\[
 -J_0(1/9)<47/300,\qquad \log5<5/3 .
                                                                  \tag{24}
\]
The latter is the existing finite positive-series witness in the
binomial end theorem. Thus the worst rate in (21), using (19), is
\[
 \frac{153}{100}+\frac{47}{150}+\frac5{27}
       =\frac{5477}{2700}
       =\frac{203}{100}-\frac1{675}.
                                                                  \tag{25}
\]

**Theorem 2.** For both parities and both next types,
\[
 \sum_{b=\lceil8N/9\rceil}^{D}
 \left|\frac{(-q)^b}{\kappa^2N}
                 \ell_b(w)C_{\beta,N}(r^b,Z)\right|
                       \le CN^A e^{203N/100},\qquad |Z|\le3 .
                                                                  \tag{26}
\]
It is uniform for all real ordinary colors and small fixed
complete-color disks, and for any subset of the displayed band.
The exact scalar and all finite sums cost only polynomial powers.
Markov or Cauchy before the positive sum gives fixed ordinary
derivatives; Cauchy on smaller output disks gives output derivatives.

On every actual ordinary and terminal next-reference family,
[the kernel-margin theorem, equation (23)](research_mixed_next_low_index_kernel_margin.md)
gives \(\Re\mathcal P_\beta^+>51/25\), and the output modulus is
strictly below three. On fixed smaller matching neighborhoods the
same floor holds. Thus the complete high-band contribution and its
fixed mixed derivatives, normalized by \(e^{-N\mathcal P_\beta^+}\),
are \(O(e^{-N/200})\).

This extends the paid combined physical band from \(b\ge11N/12\)
to \(b\ge8N/9\). Neither individual Fourier-sector cardinal correction
is estimated. An arbitrary first-coordinate truncation inside a
coefficient is also not bounded here: overlap with another deletion
requires its own positive bound. The coherent middle range and its
prescribed complete closing observation remain separate.

## 5. A distinct local filter with the larger high-index deletion

The physical-node identity in (21) also preserves the already proved
local prefix when this larger band is deleted. This uses a new
cardinal filter; it does not enlarge the previous selected-plateau
correction theorem with its \(77/50\) ceiling.

Set \(B_N=\lceil8N/9\rceil\). At its high physical nodes,
\[
 F_{34,N}(w,r^b)=\frac{(-q)^bP_b}{\kappa^2N}\ell_b(w),
 \qquad b\ge B_N .
                                                                  \tag{27}
\]
The uniform sine-factorial estimate and \(J_0(u)\le1/6\) give
\[
 |F_{34,N}(w,r^b)|
       \le C_\tau N^{A_\tau}
                e^{N(509/300+\tau)},\qquad
       \frac{509}{300}=\frac{153}{100}+\frac16 .
                                                                  \tag{28}
\]
This holds at all real ordinary colors and on a sufficiently small
fixed complete-color disk, with the same fixed derivatives.
Let \(\delta>0\) be the fixed low-index choice in the
[low physical interval theorem](research_mixed_next_low_physical_interval.md),
shrinking it if necessary. That theorem bounds the low prefix nodes
\(b\le\lfloor\delta N\rfloor\) at rate less than \(8/5\), including
the required complex-color allowance.

For \(I_N=\{b\le\lfloor\delta N\rfloor\}\cup\{b\ge B_N\}\), use the
exact cardinal projection
\[
 \Pi_NF(Y)=\sum_{b\in I_N}F(r^b)\mathfrak l_b(Y),\qquad
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu,
 \qquad |\mathfrak l_b(Y)|\le1\quad(|Y|\le1).
                                                                  \tag{29}
\]
Write \(R_N^a\) for the complete first-coordinate polynomial with
\(a\ge A_N=\lceil23N/24\rceil\). The
[sectorwise first-end theorem](research_mixed_three_four_next_sectorwise_first_end.md)
gives its whole unit-disk rate \(371/720+\tau\), and its positive
physical-rectangle bound controls every overlap with \(I_N\).
Define
\[
       F_N^{\rm mid,new}=(I-\Pi_N)(F_{34,N}-R_N^a).
                                                                  \tag{30}
\]
The exact difference
\[
 F_{34,N}-F_N^{\rm mid,new}
       =R_N^a+\Pi_NF_{34,N}-\Pi_NR_N^a
                                                                  \tag{31}
\]
and (28)--(29) imply
\[
 \sup_{|Y|\le1}|F_{34,N}(w,Y)-F_N^{\rm mid,new}(w,Y)|
       \le C_\tau N^{A_\tau}e^{N(509/300+\tau)} .
                                                                  \tag{32}
\]
All projections cost only polynomial factors. In particular the
overlap in (31) is retained, rather than subtracted from an absolute
estimate for a signed inner sum.

At the actual matching inputs \(y=q_{34}(s_3)\), the
[whole following-prefix theorem](research_mixed_three_four_following_complete_prefix.md)
has \(|e^{-2\pi iy}|<1\) and
\(\Re\mathcal P_{34}(-2,y)>7/4\). The exact reserve is
\[
                  \frac74-\frac{509}{300}=\frac4{75}>\frac1{25}.
                                                                  \tag{33}
\]
Choose the finite allowance and fixed complex neighborhoods small
enough to spend less than \(1/75\) in total. On smaller matching
neighborhoods, (32) and Cauchy then give, for every fixed mixed jet,
\[
 \partial_w^j\partial_y^k
 \left[e^{-N\mathcal P_{34}(w,y)}
     \{F_{34,N}(w,e^{-2\pi iy})
                    -F_N^{\rm mid,new}(w,e^{-2\pi iy})\}\right]
                       =O(e^{-N/25}).
                                                                  \tag{34}
\]
Thus (30) retains the same \(N^{-3/2}\) prefix action and nonzero
coefficient, and the same \(N^{-2-\beta/2}\) contribution to the
actual local next integral with its full \(d_NC_{\beta,N}\) factors.

At physical nodes (30) represents exactly the narrower rectangle
\[
       0\le a<\lceil23N/24\rceil,\qquad
       \lfloor\delta N\rfloor<b<\lceil8N/9\rceil .
                                                                  \tag{35}
\]
The low-band theorem, Theorem 2 above, and the positive first-end
rectangle bound pay its full difference from the original physical
next transfer, including every overlap. This is a combined physical
deletion and local-packet preservation. It gives neither an
individual bound on the two Fourier coefficients of the correction
in (31) nor a selected-plateau \(77/50\) bound for this new filter.
