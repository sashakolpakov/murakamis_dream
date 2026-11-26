# The exact prepared main sum for the adjacent three-crossing boundary

Research note, 3 November 2026.

After extracting the exact scalar from the original three-crossing
column, its prepared contribution to the complete adjacent-pair
boundary has a three-index sine-factorial formula. The inner
alternating factors cancel exactly. The formula retains the
ordinary free-boundary polynomial and every first normal.
Its local phase reduces, with the full logarithmic charge fixed,
to the geometric remaining-row phase already identified.

This note proves the finite reduction and the phase and amplitude
normalizations. It does not yet prove a global contour comparison
for the prepared boundary sum.

## 1. The full finite prepared source

Fix \(N\ge2\), \(D=N-1\), and
\[
 \begin{gathered}
 q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \kappa=e^{\pi iD^2/(2N)},\qquad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad S_0=1,\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_j(w)=S_j^{-2}\prod_{r=0}^{j-1}(c_r-w),\\
 \alpha=M^3\mathbf e_0,\qquad
 h_j=q^{j(j+2)}S_j^2 .
 \end{gathered}                                                   \tag{1}
\]
Here \(M\) is the original crossing multiplication matrix, \(J\)
is the original coefficient reversal, and the full quotient is
\(\mathbb C[w]/(2T_N(w/2)+2)\).
Let \(A_N\) be the exact scalar fixed in
[the polynomial remainder theorem](research_three_crossing_next_step_profile.md).
Thus
\[
 \alpha=\kappa^3A_Nh+\delta_N,\qquad
 \max_j|\delta_{N,j}|=O(N),\qquad
 A_N=N^{-1/2}\omega_N(1+O(N^{-1})),
 \quad
 \omega_N=e^{i\pi(1/4+1/(4N)-N/12)} .
 \tag{2}
\]
The original positive-pair boundary and its prepared contribution are
\[
 \begin{split}
 F_N(w)&=\mathbf e(w)^TJM^3J\alpha,\\
 F_N^{\,0}(w)&=\kappa^3A_N\mathbf e(w)^TJM^3Jh,\qquad
 \mathbf e(w)=(e_0(w),\ldots,e_D(w))^T .
 \end{split}                                                     \tag{3}
\]
The error in (3) is still the exact original operation on
\(\delta_N\). It is not removed merely by writing (2).

**Proposition 1.** At every level,
\[
 \boxed{\begin{split}
 F_N^{\,0}(w)=A_NN^3\kappa^2
  \sum_{\substack{i,j,k\ge0\\i+j<N,\ k\le j}}
 &\,\mathrm i^{\,i+j}(-1)^j
 q^{((i-j)^2-i+j)/2+k(j+k)}\\[-1mm]
 &\times
 \frac{S_{i+j}}{S_i^2S_jS_k^3S_{j-k}}\,e_i(w).
 \end{split}}                                                   \tag{4}
\]
The symbol \(\mathrm i\) outside the indices denotes
\(\sqrt{-1}\). Every denominator is a nonzero original factorial,
and the equality is an ordinary polynomial identity in \(w\).
The negative-pair version is obtained by conjugating all
coefficients, with \(w\) kept as the free polynomial variable.

*Proof.* The original matrix entries are
\[
 M_{j\ell}=\kappa(-1)^j q^{j(\ell+1)}
                     \frac{S_j}{S_\ell S_{j-\ell}}
              \quad(0\le\ell\le j<N).
 \tag{5}
\]
The exact reflection and scalar identities are
\[
 S_{D-\ell}S_\ell=N,\qquad
 h_{D-\ell}=(-1)^Nq^{\ell^2-1}\frac{N^2}{S_\ell^2},
 \qquad (-1)^N\kappa^2q^{-1}=1.
 \tag{6}
\]
They give the particularly simple prepared next-crossing column
\[
 \boxed{\quad
 (\kappa^3A_NMJh)_j=
 A_NN^2\kappa^2(-q)^j S_j
       \sum_{k=0}^j\frac{q^{k(j+k)}}{S_k^3S_{j-k}} .
 \quad}                                                         \tag{7}
\]
All alternating factors in the inner sum have canceled.
No estimate or semiclassical replacement has been used.

The exact two-crossing kernel, in the same normalization, is
\[
 (JM^2)_{ij}
 =N\,\mathrm i^{\,i+j}
      q^{((i-j)^2-i-j)/2}
      \frac{S_{i+j}}{S_i^2S_j^2}\qquad(i+j<N),
 \tag{8}
\]
and is zero outside that triangle. This is
[the original degree-two formula](research_degree_two_power_two_formula.md).
Insert (7) in \(\mathbf e(w)^TJM^2\), and combine its
factor \(q^j\) with (8). The result is exactly (4).
Since (5), (7), and (8) are full finite matrix identities,
they preserve the original double-root normals.
Ordinary \(w\)-differentiation of (4) is also exact.
\(\square\)

In particular, at odd levels the value \(e_i(-2)\) vanishes
above the simple central root, but the corresponding
\(\partial_we_i(-2)\) generally does not. Those indices
remain present in (4).

## 2. Bulk phase and complete density

Write \(w=-2\cos u\), and let
\[
 \mathcal J(z)=\int_0^z\operatorname{Log}(2\sin\pi t)\,dt
 \tag{9}
\]
on the original factorial branch. Let \(b(y,u)\) be the
canonical Newton phase, with \(b(y,0)=\mathcal J(2y)-4\mathcal
J(y)\). On compact bulk rectangles its full interpolation
satisfies
\[
 e_{Ny}(-2\cos u)
    \sim\frac{1}{2N\sin\pi y}\,e^{Nb(y,u)}.
 \tag{10}
\]
Here (10) denotes the canonical holomorphic factorial
interpolation at noninteger \(Ny\), not a new polynomial
definition. Its relative expansion and fixed derivatives are
uniform on compact bulk sets.

Use \(x=j/N\), \(y=i/N\), \(z=k/N\), and retain
\[
                    (-1)^j=e^{-i\pi j}.
 \tag{11}
\]
The phase in (4) is
\[
 \boxed{\begin{split}
 \Xi(x,y,z;u)={}&
 \mathcal J(x+y)-\mathcal J(x)-\mathcal J(x-z)-3\mathcal J(z)
                 -2\mathcal J(y)+b(y,u)\\
 &+\frac{i\pi}{2}
            \{(x-y)^2-x+y+2xz+2z^2\}.
 \end{split}}                                                   \tag{12}
\]
At \(u=0\), its \(y\)-only part is
\(\mathcal J(2y)-6\mathcal J(y)\).
The exact summand in (4), including its outside factor
\(A_NN^3\kappa^2\), has the uniform bulk expansion
\[
       A_N\kappa^2N^{-1}
          a_3(x,y,z)e^{N\Xi(x,y,z;u)}(1+O(N^{-1})),
 \tag{13}
\]
where
\[
 a_3(x,y,z)=
 \frac{e^{i\pi(x-y)/2}\sqrt{\sin\pi(x+y)}}
 {16\sin^2(\pi y)\sqrt{\sin\pi x}\,
                  (\sin\pi z)^{3/2}\sqrt{\sin\pi(x-z)}}.
 \tag{14}
\]
All square roots continue from the positive real factorials.
The midpoint shifts of the Newton factor are included.

For the normalization in (13), the factorial ratio in (4)
has power \(N^{-3}\), and the Newton factor has power
\(N^{-1}\). Its outside factor is \(A_NN^3\kappa^2\).
The two density phases in (8), (7) combine to
\(e^{i\pi(x-y)/2}\); there is no leftover linear \(z\)
phase. These facts give (13)--(14).

## 3. Exact reduction to the selected geometric phase

Let \(\tau\) be the selected positive-source root and use
the original source clocks from
[the geometric remaining-saddle calculation](research_three_crossing_geometric_remaining_saddle.md):
\[
 \begin{gathered}
 (\tau-2)^2(\tau^2-2\tau+2)=-2i,\qquad
 \tau\ \hbox{near }0.944-1.303i,\\
 r=\tau^2-3\tau+3,\quad
 z_{\rm out}=4-5\tau+4\tau^2-\tau^3,\quad
 Y_{\rm out}=\frac r{z_{\rm out}r-1},\\
 x_*=\frac{\operatorname{Log}r}{2\pi i},\qquad
 y_*=\frac{\operatorname{Log}Y_{\rm out}}{2\pi i},\qquad
 z_*=\frac{\operatorname{Log}(1/\tau)}{2\pi i}.
 \end{gathered}                                                   \tag{15}
\]
The last coordinate is the already controlled one-variable
main saddle; it is different from the final Newton-wire clock
\(Y_{\rm out}\).
All \(x_*,y_*,z_*,x_*-z_*,x_*+y_*,2y_*\) are strictly
inside their original factorial strips.

Put \(X=e^{-2\pi ix}\) and define the inner phase
\[
 K(x,z)=\mathcal J(x)-\mathcal J(x-z)-3\mathcal J(z)
                              +i\pi(xz+z^2-x).
 \tag{16}
\]
On the selected branches,
\[
 K(x,z)=\Phi_{\rm main}(z;X)+i\pi x,                             \tag{17}
\]
where \(\Phi_{\rm main}\) is equation (12) of
[the complex next-step theorem](research_three_crossing_complex_next_step.md).
Indeed
\[
 2\sin\pi(x-z)
     =-i e^{i\pi(x-z)}(1-Xe^{2\pi iz})
 \]
fixes the derivatives in \(z\), including their logarithms;
both sides of (17) agree at \(z=0\).
This is a branch identity near the selected point, continued
from the same regular path used for the one-variable action.

The proved main-saddle action calibration therefore gives
\[
        \operatorname{stat}_z K(x,z)
                  =I(x)-2\mathcal J(x)-i\pi x,
 \tag{18}
\]
where \(I(x)=\int_0^x\operatorname{Log}\lambda(t)\,dt\)
uses the endpoint-selected characteristic branch.
Eliminating \(z\) from (12) recovers exactly
\[
 \begin{split}
 \operatorname{stat}_z\Xi(x,y,z;0)
 ={}&I(x)+\mathcal J(x+y)-4\mathcal J(x)
             -6\mathcal J(y)+\mathcal J(2y)\\
   &+\frac{i\pi}{2}\{(x-y)^2-x+y\},
 \end{split}                                                     \tag{19}
\]
the original two-variable remaining-row phase.
Consequently (15) satisfies the full three logarithmic
stationary equations, not just their exponentials.

There is also a useful strict concavity region. Fix arbitrary
imaginary heights and suppose the real parts obey
\[
 \begin{gathered}
 0<\operatorname{Re}z<\operatorname{Re}x<1/2,\qquad
 0<\operatorname{Re}y<1/2,\qquad
 1/2\le\operatorname{Re}(x+y)<1 .
 \end{gathered}                                                   \tag{20}
\]
Then the horizontal real Hessian of \(\Xi(\,\cdot\,;0)\)
is strictly negative definite.
To see this, \(\operatorname{Re}\mathcal J''(x+y)\le0\),
while the real parts of \(\mathcal J''(x)\),
\(\mathcal J''(x-z)\), and \(\mathcal J''(z)\) are positive.
Their Hessian contributions are respectively the squares of
the \(x+y\), \(x\), \(x-z\), and \(z\) directions with the
signs in (12). The remaining diagonal entry is
\[
 -6\pi\cot\pi y+4\pi\cot2\pi y
                        =-4\pi\cot\pi y-2\pi\tan\pi y,
 \tag{21}
\]
whose real part is strictly negative. The quadratic imaginary
polynomial in (12) contributes zero to this real Hessian.
This proves the assertion, including at
\(\operatorname{Re}(x+y)=1/2\).

The selected point is strictly inside (20). Thus its
three-variable Hessian is nonsingular and the local Gaussian
coefficient is nonzero. If the full original summation cycle
is shown to select this saddle with coefficient one and with
all complementary terms exponentially smaller, its leading
contribution will be
\[
 \kappa^2\omega_N\,
 \frac{(2\pi)^{3/2}a_3(x(u),y(u),z(u))}
       {\sqrt{\det[-\Xi''_{x,y,z}(x(u),y(u),z(u);u)]}}
 e^{N\Xi(x(u),y(u),z(u);u)}(1+O(N^{-1})).
 \tag{22}
\]
The exponent of \(N\) is zero: the \(N^3\) lattice density
and \(N^{-3/2}\) Gaussian factor in (13) leave
\(A_NN^{1/2}=\omega_N(1+O(N^{-1}))\).
Equation (22) is only the local consequence until that
whole-cycle comparison is proved. The strict concavity on
(20) alone does not control the remainder of the original
finite simplex.

## 4. Exact finite checks

The focused
[original-matrix checker](../experiments/check_three_crossing_prepared_boundary_sum.py)
forms \(M^{\pm1}Jh\) and \(JM^{\pm3}Jh\) independently
of the displayed sums. It compares every coefficient of
(7), (4), and the corresponding ordinary boundary values
and first derivatives. The free scalar \(A_N\) is set to
one in this finite identity check; linearity then reinstates
its exact value.

The [120-digit record](../repro/results/research-three-crossing-prepared-boundary-sum.json)
covers \(N=2,\ldots,12\), both signs, the complete boundary,
two original physical colors, and a free complex boundary.
The physical endpoint derivative is retained even where the
value vanishes. Script and dependency hashes are recorded.
These are checks of the exact source reduction, not numerical
evidence for the missing global asymptotic comparison.

## 5. Certified real scalar rates for the outer colors

The following inequalities are useful before deforming any of the
retained sums. Use the original endpoint-selected functions
\[
 A(x)=\Re I(x)-2\mathcal J(x),\qquad
 B(x)=\Re I(x)-\mathcal J(x),\qquad
 g(y)=\mathcal J(2y)-4\mathcal J(y),\qquad b_2=2G/\pi .
 \tag{23}
\]
Here \(G\) is Catalan's constant. The global coefficient theorem in
[the next-crossing profile](research_three_crossing_next_crossing_fourier.md)
proves that \(A\) has a unique maximum at \(x_{\max}\), that \(B\)
increases up to \(1/2\), and that
\[
 t_{\max}=2\cos(2\pi x_{\max}),\qquad
 t_{\max}^3-2t_{\max}^2-t_{\max}+3=0,\quad -2<t_{\max}<-1 .
 \tag{24}
\]

**Lemma 2.** The following are strict inequalities:
\[
\begin{gathered}
 A(1/10)<1/3,\qquad g(1/10)<9/20,\qquad
 A(x_{\max})<23/50,\qquad B(1/2)<43/100,\\
 \max_{0\le y\le1/2}\{\mathcal J(2y)-6\mathcal J(y)\}<9/10,
 \qquad b_2<73/125 .
\end{gathered}                                                    \tag{25}
\]

*Proof and finite certificate.* The exact real clocks used for the
first and third comparisons are
\[
\begin{split}
 X_{1/10}&=\frac{1+\sqrt5}{4}
               -\frac{i\sqrt{10-2\sqrt5}}4,\\
 X_{\max}&=t_{\max}/2-i\sqrt{1-t_{\max}^2/4}.
\end{split}                                                      \tag{26}
\]
For each lower unit-circle clock \(X=e^{-2\pi ix}\), set
\[
 \tau=\frac{3-\sqrt{4/X-3}}2,\qquad Y=\tau^{-1},\qquad
 z=\frac{\operatorname{Log}Y}{2\pi i}.
 \tag{27}
\]
The square root continues from \(+1\) at \(x=0\) and has positive
imaginary part for \(0<x\le1/2\). The branch in (27) has
\(|\tau|>1\), hence \(|Y|,|XY|<1\), on that open arc. Indeed on
\(|\tau|=1\) the exact identity
\(|\tau^2-3\tau+3|^2=1+12(1-\Re\tau)^2\)
prevents a return to that circle except at \(\tau=1\).
The near-zero expansion selects its outside side.
The action calibration from Section 7 of
[the complex next-step theorem](research_three_crossing_complex_next_step.md)
therefore continues along the real arc, with no change of logarithmic
lift. In particular
\[
\begin{split}
 A(x)=\Re\biggl[&(1-z)\operatorname{Log}X
 +\frac{\operatorname{Li}_2(X)-\operatorname{Li}_2(XY)
          -\pi^2/2+3\operatorname{Li}_2(Y)}{2\pi i}\\
 &\hspace{30mm}+2\pi i(z^2-z)\biggr].
\end{split}                                                      \tag{28}
\]
At \(x=1/2\) the continuous lower-arc logarithm is
\(\operatorname{Log}X=-i\pi\); here
\(\tau=(3-i\sqrt7)/2\), \(Y=(3+i\sqrt7)/8\), and
\(A(1/2)=B(1/2)\).

For the remaining real sine integrals one uses
\[
 \mathcal J(y)=-\frac{\Im\operatorname{Li}_2(e^{2\pi iy})}{2\pi}.
 \tag{29}
\]
The derivative of \(\mathcal J(2y)-6\mathcal J(y)\) is
\(2\log[\cos(\pi y)/(2\sin^2(\pi y))]\).
It changes sign exactly once on \((0,1/2)\), so the maximum
in (25) occurs at
\(\cos(\pi y)=(\sqrt{17}-1)/4\).
Thus every input of (28)--(29) is specified by algebraic numbers.

The [exact rational checker](../experiments/verify_three_crossing_real_tail_rates.py)
encloses these numbers by rational square-root bounds and 150
steps of bisection for (24). It imports the fixed logarithm and
dilogarithm series from the existing phase certificate. All arithmetic
rounds outwards to denominator \(10^{50}\).
The logarithm uses its 250-term atanh series in the right half-plane.
The dilogarithm uses 250 terms with remainder
\(r^{251}/[251^2(1-r)]\).
Unit-circle arguments are brought strictly inside that disk by
one of the principal identities
\[
\begin{split}
 \operatorname{Li}_2(Z)
   &=\pi^2/6-\operatorname{Log}Z\operatorname{Log}(1-Z)
                         -\operatorname{Li}_2(1-Z),\\
 \operatorname{Li}_2(Z)
   &=-\operatorname{Li}_2\!\left(\frac{Z}{Z-1}\right)
                         -\tfrac12\operatorname{Log}^2(1-Z).
\end{split}                                                      \tag{30}
\]
These identities follow by differentiating along the ray to \(Z\)
and matching the value at zero; the arguments used here avoid their
cuts. The first is used near \(Z=1\), the second elsewhere.
Also \(\operatorname{Li}_2(-1)=-\pi^2/12\).
The same helper encloses \(\pi\) by Machin's formula with 90 terms.
Finally the first 65 terms of Catalan's alternating series are an
upper bound for \(G\). The saved
[rational result](../repro/results/research-three-crossing-real-tail-rates.json)
asserts every inequality in (25), with script and dependency hashes.
No numerical quadrature or floating-point comparison is used.
\(\square\)

For example the three sums of upper rates
\[
\begin{split}
 1/3+2(73/125)+1/1000&=4507/3000,\\
 9/20+73/125+23/50+1/1000&=299/200,\\
 43/100+1/6+9/10+1/1000&=4493/3000
\end{split}                                                      \tag{31}
\]
are all strictly below \(153/100\). The last \(1/1000\)
allows the full ordinary-boundary perturbation on
\(|w+2|\le10^{-6}\). Equation (31) records scalar comparisons;
their application to a specified original color sector must still
retain that sector's exact source decomposition.

## 6. A globally removable prepared input tail

There is one input truncation that can be made before any contour
argument. Put
\[
        \alpha_0=1/1024,\qquad \beta_0=511/1024,
\]
and let \(h^{\mathrm{tail}}\) retain exactly those components
\(h_{D-k}\) for which \(k/N\le\alpha_0\) or \(k/N\ge\beta_0\).
Then, uniformly on \(|w+2|\le10^{-6}\),
\[
 \left|\kappa^3A_N\mathbf e(w)^TJM^3J h^{\mathrm{tail}}\right|
       \le \operatorname{poly}(N)\exp\!\left(\frac{775}{512}N\right),
       \qquad \frac{775}{512}<\frac{153}{100}.
 \tag{32}
\]
The same rate bound holds for every fixed ordinary boundary
derivative on the half-sized disk, at both parities and both
crossing signs.

To prove this, the exact reflection formula (6) gives
\(|h_{D-k}|=N^2/S_k^2\).
The uniform factorial estimate bounds this by a polynomial times
\(\exp[-2N\mathcal J(k/N)]\), including all endpoint indices.
For \(0\le t\le\alpha_0\), the sine chord bound implies
\[
 -2\mathcal J(t)
 \le 2t(1-\log(4t))
 \le \frac{2}{1024}(1+\log256)<\frac7{512}.
 \tag{33}
\]
For \(\beta_0\le t\le1/2\), use
\(\mathcal J(1/2)=0\) and \(\mathcal J'\le\log2\);
the resulting bound is less than \(2/1024\).
For \(1/2\le t\le1\), \(\mathcal J(t)\ge0\).
Consequently \(\|h^{\mathrm{tail}}\|_2\) has rate at most \(7/512\).
The exact original operator estimate in
[the whole preparation-error theorem](research_three_crossing_global_preparation_error.md)
has rate strictly below \(3/2\) on this disk for every input,
not just for \(\delta_N\). Its proof is the product bound
\(\|\mathbf e(w)\|_2\|M^2\|_2\|M\|_2\|h^{\mathrm{tail}}\|_2\).
Since \(A_N\) is polynomial in size, the sum of these rates gives
(32). Cauchy's formula and coefficient conjugation give the remaining
assertions. This is a statement about the full image of an actual
input truncation; it does not discard individual future contour
currents.
