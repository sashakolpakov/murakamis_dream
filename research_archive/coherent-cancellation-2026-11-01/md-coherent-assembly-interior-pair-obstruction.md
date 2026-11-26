# The original paired reference does not control the whole cap interval

1 November 2026. Private finite-source theorem. No public files were edited.

The known cap/central contraction keeps the original internal face demand
and gains cancellation at the spectral pair \((+2,-2)\). Its extension to
small complex neighborhoods of those two values also retains that demand.
The same paired-reference comparison cannot hold on the whole real cap
interval. This note proves an explicit exponential violation at the pair
\((0,-2)\), without shifting a face target or attaching an exterior to the
internal face.

The qualification is substantial: the large values in this example lie
between spectral nodes at which both the value and the first normal
vanish. It is therefore an obstruction to the whole-interval supremum
comparison, not a lower bound for the original filling functional or a
closed knot invariant.

## 1. Existing statements and the exact pair

The inputs read before this calculation were the all-demand contraction,
its odd counterpart, the incidence/disjoint-assembly lemma, the cap-star
cut, the whole-star spectral-strip theorem, and the two-spectrum
neighborhood theorem. Their respective restrictions remain:

- disjoint pair replacement permits shared exterior variables but requires
  each extracted internal face to occur only in its own pair;
- shifting that internal demand already has an exponential counterexample;
- the whole-star theorem handles all real neighboring central spectra,
  but the cap remains near \(+2\), and the conclusion is a relative
  weighted-star improvement;
- the two-spectrum pair theorem controls neighborhoods of \((+2,-2)\),
  not the entire real square.

Here the incidence and demand are exactly those of the original pair:

\[
 E=(A,0,C,Z),\qquad F=(0,A,0,C),\qquad [A^d],\qquad d=N-1.
 \tag{1}
\]

The zeros are the two original protected faces. The ordinary face \(A\)
has no other incidence. The first coupon is restricted to its central
piece and the second to its right one-sided piece. This is the literal
pair in the existing original-demand theorem; its common raw sign has
modulus one. It occurs in the documented seven-region original source.
No new diagram or topological identity is claimed here.

For even \(N=2m\), put \(M=m-1\), \(\theta=\pi/N\), and

\[
 c_j=2\cos((2j+1)\theta),\quad
 a_j=2+c_j,\quad s_j=2\sin(j\theta),\quad
 B_j=\prod_{r=1}^{j}s_r^2,\quad B_0=1.
 \tag{2}
\]

Define the actual positive endpoint continuant by

\[
 \begin{aligned}
 K_0&=1,\qquad K_1=s_1^2(A+Z),\\
 K_r&=s_r^2(A+Z)K_{r-1}
       +s_rs_{r-1}a_{r-1}AZK_{r-2},\\
 C_{j,h}&=[A^jZ^{d-h-j}]K_{d-h}
                   \prod_{r=d-h+1}^{d}a_r.
 \end{aligned}
 \tag{3}
\]

All unused rows are included. The coefficient is zero outside its literal
nonnegative degree range. In particular

\[
 C_{0,\ell}=\frac{N^2}{B_\ell}\prod_{r=0}^{\ell-1}a_r>0,
 \qquad
 \frac{C_{0,\ell}}{C_{0,\ell-1}}=\frac{a_{\ell-1}}{s_\ell^2}.
 \tag{4}
\]

Write \(\chi_N(\sigma)=2T_N(\sigma/2)+2\). The polynomial cap factors are

\[
 b_j(\sigma)=B_j\prod_{r=j+1}^{d}(\sigma-c_r).
 \tag{5}
\]

For \(0\le\ell\le M\), both original cutoffs give precisely
\(j=0,\ldots,\ell\). The extracted coefficient, apart from the one
fixed raw sign, and its positive paired reference are

\[
 \begin{aligned}
 T_\ell(\sigma)&=\sum_{j=0}^{\ell}
                  (-1)^j b_j(\sigma)C_{j,\ell-j},\\
 D_\ell&=\sum_{j=0}^{\ell}V_j C_{j,\ell-j}>0,\qquad
 V_j=B_j\prod_{r=j+1}^{d}a_r.
 \end{aligned}
 \tag{6}
\]

These retain the remaining degrees \(C^\ell Z^{d-\ell}\). They are not
independent local maxima. Their source normalization is the one in
[the original-demand convolution](research_two_port_main_cap_original_demand_convolution.md).

## 2. Source contiguity and the sign at the interior spectrum

The polynomial contiguity identity in
[the two-spectrum theorem](research_cap_cross_two_spectrum_neighborhood_stability.md),
equations (3)–(4), is

\[
 (\sigma-c_\ell)T_\ell(\sigma)+s_\ell^2T_{\ell-1}(\sigma)
           =\chi_N(\sigma)C_{0,\ell},\qquad T_{-1}=0.
 \tag{7}
\]

For clarity, this is obtained before dividing by any spectral factor.
The exact coefficient identity

\[
 s_{j+1}^2C_{j+1,h-1}
   =(c_j-c_{j+h})C_{j,h}+s_{j+h}^2C_{j,h-1}
 \tag{8}
\]

combines with
\((\sigma-c_{j+1})b_{j+1}=s_{j+1}^2b_j\).
Multiplication and summation over \(0\le j\le\ell\) telescope. The upper
term has negative middle degree and is zero; the lower term is exactly
\(\chi_N(\sigma)C_{0,\ell}\). Thus (7) has neither a missing current nor
an auxiliary enlarged summation range in the range used here.

Suppose \(N\) is divisible by four and \(0\le\ell<N/4-1/2\).
Then \(c_0,\ldots,c_\ell>0\) and \(\chi_N(0)=4\).
The first term is \(b_0(0)=-4/c_0<0\), and

\[
 b_{j+1}(0)=-\frac{s_{j+1}^2}{c_{j+1}}b_j(0).
 \tag{9}
\]

Hence all \((-1)^jb_j(0)\) in (6) are negative. There is no alternating
cancellation left at this spectrum. Set \(X_\ell=-T_\ell(0)>0\).
At \(\sigma=-2\), every \((-1)^jb_j(-2)=(-1)^dV_j=-V_j\);
thus \(T_\ell(-2)=-D_\ell\). Evaluating (7) at these two spectra gives

\[
 \begin{aligned}
 c_\ell X_\ell-s_\ell^2X_{\ell-1}&=4C_{0,\ell},\\
 a_\ell D_\ell-s_\ell^2D_{\ell-1}&=4C_{0,\ell}.
 \end{aligned}
 \tag{10}
\]

Only the fixed positive numbers \(c_\ell,a_\ell\) in this strict low
range will be divided out.

## 3. Explicit exponential failure of the whole-interval comparison

Normalize by the same original coefficient:

\[
 R_\ell=\frac{c_\ell X_\ell}{4C_{0,\ell}},\qquad
 S_\ell=\frac{a_\ell D_\ell}{4C_{0,\ell}}.
 \tag{11}
\]

Equation (4) turns (10) into the exact positive recurrences

\[
 \begin{aligned}
 R_0=S_0&=1,\\
 R_\ell&=1+t_\ell R_{\ell-1},
 &t_\ell&=\frac{s_\ell^4}{a_{\ell-1}c_{\ell-1}},\\
 S_\ell&=1+r_\ell S_{\ell-1},
 &r_\ell&=\frac{s_\ell^4}{a_{\ell-1}^2}.
 \end{aligned}
 \tag{12}
\]

Take \(N=32k\), \(k\ge1\), and \(L=7N/32=7k\). This is strictly
inside the range of (10). Put

\[
 \rho=\tan^4(7\pi/32)<1,\qquad \tau=5\sqrt5-10>1.
 \tag{13}
\]

For \(1\le\ell\le L\),

\[
 r_\ell
  =\frac{\sin^4(\pi\ell/N)}
          {\cos^4(\pi(\ell-\tfrac12)/N)}
       \le\rho,\qquad
               1\le S_\ell\le\frac1{1-\rho}.
 \tag{14}
\]

For the other recurrence define

\[
 t(x)=\frac{2\sin^4(\pi x)}
            {\cos^2(\pi x)\cos(2\pi x)},\qquad 0<x<1/4.
 \tag{15}
\]

Its positive numerator increases and its positive denominator decreases,
so it is strictly increasing. If \((\ell-\tfrac12)/N\ge1/5\), then

\[
 t_\ell=
 \frac{2\sin^4(\pi\ell/N)}
 {\cos^2(\pi(\ell-\tfrac12)/N)\cos(2\pi(\ell-\tfrac12)/N)}
 \ge t(1/5)=5\sqrt5-10=\tau.
 \tag{16}
\]

The last equality follows by substituting
\(\sin^2(\pi/5)=(5-\sqrt5)/8\).
Put \(k_0=\lceil N/5+1/2\rceil\). Dropping only positive terms from
the first recurrence in (12) gives

\[
 R_L\ge\prod_{\ell=k_0}^{L}t_\ell
       \ge\tau^{L-k_0+1}
       \ge\tau^{3N/160-1}.
 \tag{17}
\]

The interval is nonempty already at \(N=32\). Since \(a_L/c_L>1\),
(11), (14), and (17) prove the finite inequality

\[
 \boxed{\displaystyle
 \frac{|T_L(0)|}{D_L}
       \ge(1-\tan^4(7\pi/32))
                (5\sqrt5-10)^{3N/160-1},
 \quad N\in32\mathbb N,\quad L=7N/32.}
 \tag{18}
\]

In particular the limiting lower exponential rate is at least
\((3/160)\log(5\sqrt5-10)>0\). This uses no asymptotic coefficient
entropy theorem, no numerical optimization, and no unrecorded scalar.
It disproves an \(e^{o(N)}\) coefficientwise comparison with the original
paired reference on the whole real cap interval, even when the central
neighbor remains exactly at \(-2\) and the internal demand is unchanged.

## 4. The active-node qualification

There is an exact reason not to turn (18) into a claim about the filling
functional. At either parity, retain the low range
\(\ell\le M=\lfloor N/2\rfloor-1\), and allow any fixed value of the
neighbor's spectral parameter. The same finite sum has the common factor

\[
 T_\ell(\sigma,\tau)=
 \left(\prod_{r=\ell+1}^{d}(\sigma-c_r)\right)P_\ell(\sigma,\tau),
 \qquad \deg_\sigma P_\ell\le\ell.
 \tag{19}
\]

This follows term by term from (5), so it needs no inverse or divided
recurrence. For every distinct double node indexed by \(a>\ell\),
both rows \(a,d-a\) occur in the product. Therefore

\[
 T_\ell(c_a,\tau)=
       \partial_\sigma T_\ell(c_a,\tau)=0\quad(a>\ell).
 \tag{20}
\]

At an odd level the simple node \(-2\) is also a zero. At the remaining
double nodes \(a\le\ell\), the reflected row \(d-a\) remains, so the value
is still zero but the first normal may survive. Consequently the original
full-Hermite insertion of any fixed integral power \(p\) reduces exactly
to

\[
 \mathcal L_N^pT_\ell(\,\cdot\,,\tau)
  =\frac1{N^2}\sum_{a=0}^{\ell}
      (4-c_a^2)f_p(c_a)
           \partial_\sigma T_\ell(c_a,\tau).
 \tag{21}
\]

The original Gaussian lift in \(f_p\), all normal factors, and all
remaining face targets are unchanged. No simple-node value or derivative
of \(f_p\) survives because the numerator values are zero.

For the example (18), the active nodes have \(c_a\ge c_L>0\). The large
value at \(\sigma=0\) lies outside this active-node band. The nearby
spectral nodes are double zeros of the extracted coefficient. Thus the
whole-interval supremum comparison fails more strongly than is necessary
for evaluating this particular finite functional.

## 5. Consequence for the next argument, and stopping scope

The existing pair replacement cannot be extended to every cap spectrum
with the same coefficientwise endpoint comparator. This failure persists
after the correct internal face has been extracted, so it is different
from the earlier shifted-demand counterexample.

For the actual filling problem, (21) identifies a narrower unresolved
question: control the coherent active normal sum, or its signed assembly
with the rest of the original source. Neither (18) nor (21) supplies that
estimate. In particular, no lower bound for a filled period, no new knot
class, and no contradiction to a volume conjecture is asserted.

The accompanying check reconstructs the relevant central coefficients
from the original triangular face operator and polynomial resolvent,
separately from (3), at selected finite levels. It checks the exact
contiguity, sign-normalization algebra, and inactive-node vanishing.
A short high-precision calculation checks (18) numerically at selected
multiples of 32. These computations diagnose finite transcription errors;
the all-level inequality is proved by (12)–(18).

Research is frozen at this result. The earlier exploratory ratio samples
are preserved separately and are not used as proof.
