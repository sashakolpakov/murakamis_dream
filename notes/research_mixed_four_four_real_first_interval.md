# Moving the real first coordinate toward the one-tenth face

Private written proof, 10 November 2026. For a first pair of type
four/four, the complete finite sum on a real first-coordinate interval
can be bounded by the same collection of contour profiles at its right
endpoint. The second coordinate remains at its original geometric
height. The argument includes the small and large physical indices,
the cap endpoints, and every correction in the finite contour formula.
It concerns a real interval; a vertical connection is a separate step.

## 1. Source and the endpoint envelope

Fix an actual positive three/four word of length at least three,
beginning with four and four.
Keep its original private heights and second retained coordinate:
\[
 h_e\in[-.051,-.019],\qquad h_s,d\in[-.102,-.001],\qquad
 b=z+id,\quad z\in P=[11/50,9/20].
\tag{1}
\]
Let \(0<\rho<1/10\) be fixed before the quantum level \(N\), and put
\[
 \rho\le x\le1/10,
 \qquad X=e^{-2\pi ix},\quad Y=e^{-2\pi ib},\quad
 q_N=e^{-2\pi i/N},\quad P_j=(q_N;q_N)_j.
\tag{2}
\]
The original kernels and their two possible first Fourier terms are
\[
\begin{split}
 U_N(w,X)&=\sum_{i=0}^{N-1}
       \frac{H_N(w,q_N^{-i})(q_NX;q_N)_i}{P_i^2},\\
 C_N(X,Y)&=\sum_{j=0}^{N-1}R_{j,N},\qquad
 R_{j,N}=X^{-j}\frac{(q_NX;q_N)_j(q_NY;q_N)_j}{P_j^3},\\
 K_{\sigma,N}(w;X,Y)&=U_N(w,X)C_N(X,Y)d_N(X)X^{-N\sigma},
                    \qquad \sigma\in\{0,1\}.
\end{split}
\tag{3}
\]
The outgoing allocation is \(|d_N(Y)|^{1/2}\). The phase conventions
are those of the [complete selected four/four source](research_mixed_selected_four_four_early_complete_source.md):
\[
\begin{split}
 \Psi(e,x)&=S(e)+g(e+x)-g(x)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;x,b)&=g(s+x)+g(s+b)-3g(s)-g(x)-g(b)+2\pi ixs,\\
 J(x)&=\Re g(x)=\int_0^x\log(2\sin\pi t)\,dt.
\end{split}
\tag{4}
\]
Here \(S\) is the original coherent endpoint action, and
\(g'(t)=\operatorname{Log}(1-e^{-2\pi it})\) on its original strip.

For the cap, let \(\mathcal E\) be the following compact collection
of a private point and its Fourier penalty:
\[
\begin{array}{c|c}
 e&\text{penalty }p_e\\ \hline
 u+ih_e,\quad .27\le u\le.49&0\\
 .27,\ .49&0\\
 u-.055i,\quad .27\le u\le.49&.11\pi\\
 u+.04i,\quad .27\le u\le.49&.08\pi .
\end{array}
\tag{5}
\]
Add the separate cap-end rate
\[
 E_*=\frac35+\frac{\log4}{100}.
\tag{6}
\]
For the ordinary factor retain the complete collection \(\mathcal S\):
\[
\begin{array}{c|c}
 s&\text{penalty }p_s\\ \hline
 v+ih_s,\quad 1/8\le v\le1/2&0\\
 c+it,\quad c\in\{1/8,1/2\},\ h_s\le t\le0&0\\
 v-i/5,\quad 1/8\le v\le1/2&2\pi/5\\
 v+2i,\quad 1/8\le v\le1/2&4\pi\\
 c+it,\quad c\in\{1/8,1/2\},\ -1/5\le t\le2&2\pi|t|.
\end{array}
\tag{7}
\]
In particular the real cuts belong to this collection. Define
\[
\begin{split}
 A(x)&=\max\left\{E_*,\max_{(e,p_e)\in\mathcal E}
                              (\Re\Psi(e,x)-p_e)\right\},\\
 B(x,b)&=\max_{(s,p_s)\in\mathcal S}
                       (\Re Q(s;x,b)-p_s)-\tfrac12\Re g(b),\\
 \mathcal M(x,b)&=A(x)+B(x,b)-J(x).
\end{split}
\tag{8}
\]
Every maximum is over a fixed compact set. These are upper profiles
of the specified finite functions, not new critical values.

**Theorem 1.** For every \(\tau>0\), both level parities and both
\(\sigma\), uniformly on (1)--(2),
\[
 |K_{\sigma,N}(w;X,Y)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
   \exp N\left\{\mathcal M(1/10,b)
                 -\frac{1/10-x}{3}+\tau\right\}.
\tag{9}
\]
This holds on the entire real ordinary-color interval \([-2,2]\),
and on a sufficiently small fixed complex neighborhood of \(-2\).
Each fixed ordinary-color derivative has the same rate on a smaller
neighborhood. The constants may depend on \(\rho\) and the fixed word.

## 2. The complete cap for a smaller real first coordinate

The exact row representation is
\[
 U_N(w,X)=\sum_{i=0}^{N-1}
     \Delta_N(i/N)^{-1}\mathcal C_N(i/N,w)
             \frac{(q_NX;q_N)_i}{P_i}.
\tag{10}
\]
On real physical indices \(|\Delta_N|=1\). The
[complete endpoint coefficient estimate](research_mixed_endpoint_real_color_decay.md),
Theorem 1, bounds \(\mathcal C_N\) at rate
\(\lambda(t)=\Re S(t)\) on compact subintervals of \((0,1)\),
uniformly for real ordinary colors. The associated physical row rate is
\[
 R(t,x)=\lambda(t)+J(t+x)-J(x)-J(t),
\tag{11}
\]
with the numerator integral continued across its integrable zeros.

For \(0<t\le.27\), the [original endpoint bound](research_mixed_outer_cap_real_tails.md),
equation (12a), gives
\(\lambda'(t)>27/50\). Since \(t+x\le.37<1/2\),
\[
 R_t(t,x)=\lambda'(t)
          +\log\frac{\sin\pi(t+x)}{\sin\pi t}>27/50.
\tag{12}
\]
Thus the compact lower tail increases to the cut \(.27\).
On \([.49,.5]\), the unchanged bounds
\(\lambda'<-3/5\), \(J'>3/5\), and
\(\log(2|\sin\pi(t+x)|)\le\log2<7/10\)
give \(R_t<-1/2\). For \(.5\le t<1\), the exact identity
\(\lambda'(t)-J'(t)\le-\log4\) gives \(R_t\le-\log2\).
These statements remain valid after integration across numerator zeros.
The compact upper tail therefore decreases from the cut \(.49\).

The true endpoints require finite coefficient estimates. The small-index
Newton estimate in Section 3 of that same real-tail proof gives rate less than \(1/4\) when
\(i/N\le.01\); its proof only uses an upper bound on the numerator
radius and so applies at the present unit radius.
For \(t=i/N=1-\delta\ge.99\), the all-real coefficient bound has
rate at most \(3/5+\delta\log2\). The other factors admit a uniform
bound even when the missing numerator arc contains a zero. The integral
of \(\log(2|\sin\pi v|)\) over the whole period is zero, and its
minimum over an arc of length \(\delta\) is \(2J(\delta/2)\).
Consequently
\[
 \int_0^{1-\delta}\log(2|\sin\pi(x+v)|)\,dv-J(1-\delta)
 \le J(\delta)-2J(\delta/2)
 =\int_0^\delta\log(2\cos(\pi v/2))\,dv
 \le\delta\log2.
\tag{13}
\]
The minimum-arc statement follows by centering the arc at a zero:
the integrand increases with distance from the nearest integer.
The [uniform finite-product upper argument](research_mixed_conditional_contour_allowance.md),
Section 2, with an arbitrarily small rate tolerance, applies through all
zeros and all physical indices. Equivalently, its proof clips each
numerator logarithm before taking a uniform Riemann sum, and then lets
the clipping error tend to zero; the denominator has uniform
\(O(\log N)\) error up to its final nonzero index.
Equation (13) therefore gives precisely (6) for the true upper end.
No denominator from an omitted arc is divided out.

For the central cap indices use the original interpolation on
\([.27,.49]+i[-.055,.04]\). It remains regular for
\(\rho\le x\le.1\): its shifted real argument lies in
\([.27+\rho,.59]\). The private vertical convexity needed to
reduce its joins to their endpoints also holds on this smaller domain.
Indeed, writing \(C(e)=\Re\cot\pi e\), the original endpoint
curvature and cotangent bound in Section 2 of the
[complex cap proof](research_mixed_cap_early_taper_complex_profiles.md) give
\[
 -\Re\Psi_{ee}>2\pi C(e)-\pi C(e+x),\qquad
 C(e)>\frac{15}{16}\cot(\pi\Re e).
\tag{14}
\]
If \(\Re(e+x)<1/2\), then
\(C(e+x)\le\cot(\pi\Re(e+x))\le\cot(\pi\Re e)\),
leaving a positive lower bound in (14). Above one half,
\(C(e+x)\le0\). Thus every private zero-mode join and weighted
vertical alias is bounded by the five profiles in (5).
The exact contour formula retains its \(+N\) density, horizontal
aliases and all vertical halves. Together with (12)--(13), this proves
the complete cap envelope with rate \(A(x)\). The endpoint coefficient
bounds give it uniformly for every real ordinary color.

## 3. Every ordinary row and contour term

Partition the original sum at \(\lfloor N/8\rfloor\) and
\(\lceil N/2\rceil\). For the lower block the exact ratio is
\[
 \frac{|R_{j+1,N}|}{|R_{j,N}|}
 =\frac{\sin\pi(x+u)}{\sin\pi u}
   \frac{|\sin\pi(b+u)|}{\sin\pi u}
   \frac{e^{\pi d}}{2\sin\pi u},\qquad u=(j+1)/N\le1/8.
\tag{15}
\]
All factors are nonzero here. The first ratio is at least one.
Since \(z+u\in[.22,.575]\), its sine is greater than \(1/2\).
Also \(\sin^2(\pi/8)=(2-\sqrt2)/4<4/25\), using
\(\sqrt2>34/25\). Hence the right side exceeds
\((25/16)e^{-51\pi/500}>e^{1/10}\). To verify the final strict
inequality by rational bounds, use
\[
 \log(25/16)>18/41,
 \qquad
 \frac{18}{41}-\frac{51}{500}\frac{22}{7}-\frac1{10}
       =\frac{1324}{71750}>0.
\tag{16}
\]
Thus the whole lower absolute sum is less than eleven times its last
row. That row has, up to a rate tolerance, the real-cut value
\(\Re Q(1/8;x,b)\) already included in (7).

For every row above one half, the [all-angle high-row theorem](research_mixed_all_angle_high_row_sign_class.md) applies
with first height zero and second height negative. It bounds the
entire upper absolute sum by the continuous rate at \(s=1/2\),
again included in (7). It includes wrapped rows, zeros, both level
parities and the literal last index; no comparison with a possibly
zero finite half-row is used.

On the central block the [original exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
Section 4, is
regular on the rectangle with real cuts \(1/8,1/2\) and imaginary
heights \(-1/5,2\). Its shifted real arguments lie in
\([1/8+\rho,.6]\) and \([.345,.95]\). The
[residue formula](research_mixed_horizontal_asymmetric_contour.md), Section 4, has
the same \(+N\) zero mode and the same Fourier penalties as (7).
Move the zero mode to the fixed original height \(h_s\), retaining
both joins. All these terms are left explicitly in (7); no private
curvature or alias comparison at the smaller value of \(x\) is
being assumed. The fixed rectangle, exact interpolation and finite
number of rows give the complete ordinary envelope with rate
\(B(x,b)\) after its outgoing allocation is restored.

## 4. Monotonicity of the joint profiles

On the real first interval, the [complete Fourier upper rate](research_mixed_fourier_weight_continuation.md),
Section 5, is
\(\max\{-J(x),0\}=-J(x)\). The selected monomial has modulus
one. The second weight has rate \(-\Re g(b)/2\), since its
height is negative. These statements are bounds for the whole
polynomials, including their interpolation remainders.

For any fixed private points from (5) and (7), set
\[
 D=2\sin\pi x,\qquad
 N_e=|1-e^{-2\pi i(e+x)}|,\qquad
 N_s=|e^{-2\pi\Im s}-e^{-2\pi i(\Re s+x)}|.
\tag{17}
\]
Exact differentiation of the joint allocated rate gives
\[
 \partial_x\{\Re\Psi(e,x)+\Re Q(s;x,b)-J(x)\}
      =\log\frac{N_eN_s}{D^3}.
\tag{18}
\]
The ordinary chirp is included in \(N_s\). All penalties and the
outgoing halfweight are constant in this differentiation.

Here \(.27<\Re e+x\le.59\), so its twice-angle cosine is
negative and \(N_e>1\). Also
\(1/8<\Re s+x\le.6\). Minimizing the distance in \(N_s\)
over its positive radius shows that \(N_s\ge1/\sqrt2>7/10\):
up to angle \(1/4\) the minimum is the sine, and above it the
nonpositive cosine makes the distance at least one. Finally
\[
 D\le2\sin(\pi/10)=\frac{\sqrt5-1}{2}<5/8.
\tag{19}
\]
Consequently (18) is greater than \(\log2>1/3\).
For a true cap-end profile the derivative instead is
\[
 \partial_x\{E_*+\Re Q(s;x,b)-J(x)\}
       =\log\frac{N_s}{D^2}>\log(3/2)>1/3.
\tag{20}
\]
For example \((7/10)/(5/8)^2=224/125>3/2\), and the positive
atanh series gives \(\log(3/2)>2/5\).
Integrate (18) or (20) for each fixed pair of private points and
penalties, and then take their maxima. This yields
\[
 \mathcal M(x,b)\le\mathcal M(1/10,b)-\frac{1/10-x}{3}.
\tag{21}
\]
Sections 2--3 and the whole Fourier upper bounds now prove (9) on
the real ordinary-color interval. All factorial errors, shifted
finite cuts and polynomial factors fit in one prescribed \(\tau\).
The exact expression (3) has degree less than \(N\) in \(w\).
[Polynomial continuation](research_mixed_horizontal_complex_extension.md) from \([-2,2]\), followed by Cauchy's formula
on a smaller fixed neighborhood of \(-2\), gives the stated complex
color and derivative assertions with any additional prescribed rate
allowance. No modulus halfweight is differentiated or divided out.

## 5. Comparison with the original geometric rate

Let \(\Lambda(z)\) be the original geometric affine rate of the first
pair, with its unchanged outgoing derivative. Proposition 2 of the
[zero-height face theorem](research_mixed_selected_four_four_zero_height_face.md)
proves, for every individual cap alternative and every ordinary
current in (5)--(7),
\[
                 \mathcal M(1/10,z+id)<\Lambda(z)-1/1000.
\tag{22}
\]
Its cap-end constant is exactly (6), and its ordinary collection
contains all of (7). Thus it is an estimate of the required envelope,
not just of the modulus of a signed sum.

**Corollary 2.** Under (1)--(3), for both first selections,
\[
 |K_{\sigma,N}(w;X,Y)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
 \exp N\left\{\Lambda(z)-\frac1{1000}
                         -\frac{1/10-x}{3}+\tau\right\},
             \qquad \rho\le x\le1/10.
\tag{23}
\]
The parities, color neighborhoods and derivative assertions of
Theorem 1 persist. Substitute (22) into (9) to prove the claim.

The choice of \(\rho\) can be made small enough to overlap the
existing real first-collar estimate. This removes the intervening
real interval as an additional obligation for initial four/four,
with the second coordinate fixed at its geometric height. A vertical
connection and the other portions of the original integration cycle
are separate. No whole-word or knot conclusion follows from (23).

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_endpoint_real_color_decay.md | 44921926dbdccef49c84e02566e86cf175979c8f189e62c7ba2e9b92c0d577eb |
| research_mixed_outer_cap_real_tails.md | 17148159a21dc7d6e74dd92e4dcd8f5e62d91be1b01bd559c2566cdf66fb8b94 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_cap_early_taper_complex_profiles.md | 6a7b8cd841d89690a9733c1005a2449ce808ba20a875c2d1f8d8ca0b0a769138 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_selected_four_four_zero_height_face.md | fe99fcefe1618991471f083febcf4c6043418a4387d76be1ae2015542734810f |

The proof uses written inequalities and the indicated source implications.
No new mathematical numerical evaluation, test, compilation or change
to a frozen source was used.
