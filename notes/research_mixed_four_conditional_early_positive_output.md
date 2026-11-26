# Complete conditional source at an early positive outgoing height

Private written proof, 11 November 2026. The outgoing coordinate in
this note lies on the early interval at a small positive height.
The incoming coordinate lies on the real right half period. A full
finite conditional bound reduces to a fixed negative-height main
and a real low-cut profile at the incoming half point. Both
unweighted joins, all six sampling corrections and all physical
rows are retained.

This is a conditional-source theorem. It does not calibrate an
attached complete cap, the shared Fourier polynomial, or a next
conditional factor against the original three-factor action.

## 1. Literal source and statement

Put
\[
 \zeta=e^{-2\pi i/N},\quad P_j=(\zeta;\zeta)_j,\quad
 p_j(V)=(\zeta V;\zeta)_j,
\]
and keep the original polynomial
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                   \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
                                                               \tag{1}
\]
The parameter domain is
\[
 \frac12\le a\le\frac78,\qquad
 y=q+iH,\quad\frac1{10}\le q\le\frac{11}{50},\quad
 0\le H\le\frac1{100},\qquad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy}.
                                                               \tag{2}
\]
Write \(R=|Y|\). The elementary exponential bound in the
[positive-output source](research_mixed_four_conditional_positive_output_real_arc.md),
equation (3), gives
\[
                         1\le R<43/40.                         \tag{3}
\]
Use the original primitive, its additive constant and its
continuous strip logarithm:
\[
 g'(w)=\operatorname{Log}(1-e^{-2\pi iw}),\qquad
 Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias.
                                                               \tag{4}
\]
Let \(s_*\) be its original upper critical point and
\(\Theta(a,y)=Q(s_*;a,y)\). Existence and the zero logarithmic
lift on (2) are checked below.

For real physical indices define
\[
\begin{split}
 J(t)&=\int_0^t\log(2\sin\pi v)\,dv,\qquad
 I_b(t)=\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv,\\
 E_a(t;y)&=I_a(t)+I_y(t)-3J(t),\\
 \ell&=3/40,\qquad L(y)=E_{1/2}(\ell;y),\qquad
 L_0(y)=E_{1/2}(1/8;y).
\end{split}                                                       \tag{5}
\]
The continuous extension of \(J\) is odd and one-periodic;
in particular \(J(1/2)=0\). All integrated numerator zeros
are retained.

For any fixed
\[
                         -27/250\le h_s\le0,
\]
put
\[
 M(y;h_s)=\max_{1/6\le v\le5/12}
                         \Re Q(v+ih_s;1/2,y).
                                                               \tag{6}
\]

**Theorem.** For every \(\tau>0\), uniformly on (2), on the
stated interval of \(h_s\), at both level parities and for all
sufficiently large \(N\),
\[
 \boxed{\quad
 |C_{1,N}(X,Y)|\le C_\tau N^{A_\tau}
      \exp N\{\max(M(y;h_s),L_0(y))+\tau\}.
 \quad}                                                        \tag{7}
\]
Before comparison with the fixed half-point main, the proof
gives the complete ceiling
\[
 |C_{1,N}(X,Y)|\le C_\tau N^{A_\tau}
      \exp N\{\max(\Re\Theta(a,y),L_0(y))+\tau\}.
                                                               \tag{8}
\]
For any prescribed fixed \(B>0\), both horizontal sampling
corrections can instead be bounded at rate
\(\Re\Theta(a,y)-B+\tau\), by choosing a sufficiently tall
fixed rectangle. No leading coefficient or noncancellation
statement is asserted.

## 2. The original root remains before the numerator wall

Here \(\Im Y<0\), and
\[
 \Re Y\le R\cos(\pi/5)<(43/40)(13/16)<1.
\]
Thus the full outgoing domain of the
[unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md)
applies. It supplies the unique simple upper root
\[
 v(v-X)(v-Y)=X(v-1)^3,\qquad
 s_*=\frac{\operatorname{Log}v}{2\pi i}=u_*+ih_*,
 \quad0<u_*<\delta:=1-a,\quad Q_s(s_*;a,y)=0.
                                                               \tag{9}
\]
No sign of an action multiplier is imposed here.

Set \(U=e^{2\pi h_*}\). The original argument proof in
Section 2 of the positive-output source gives
\[
                         1/2<U<4.                             \tag{10}
\]
Its domain audit is short. At \(U\le1/2\), the four incoming
and own argument contributions have modulus at most \(\pi/6\)
each; the outgoing one has modulus below \(\pi/5\), since
\(RU\le43/80<\sin(\pi/5)\). The chirp is at least \(\pi\),
leaving \(2\pi/15>0\) in the imaginary critical equation.
At \(U\ge4\), the exponential force is at most
\[
 \frac{(1+U)(1+(43/40)U)}{(U-1)^3}<1.
                                                               \tag{11}
\]
After \(U=4+t\), the denominator minus numerator is
\[
 t^3+\frac{317}{40}t^2+\frac{653}{40}t+\frac12>0.
 \]
Both cases contradict the original critical equation.

The lower real cut from Section 2 of the
[early negative-output real-source proof](research_mixed_complete44_second_early_real_first_arc.md)
also survives:
\[
                              u_*>\ell.                        \tag{12}
\]
We record why none of its outgoing-radius restrictions is
being silently enlarged. For \(u\le\ell\), \(U\ge8/5\),
the original identity
\[
 \alpha_U(V)=\pi-V+\operatorname{Arg}(1-U^{-1}e^{iV}),\qquad
 \alpha_U(V)=\operatorname{Arg}(1-Ue^{-iV}),
\]
and \(\arcsin(5/8)<\pi/4\) bound the imaginary critical
equation strictly above by \(2\pi(u-q)<0\). The outgoing
argument bound used here is its full positive-radius bound
\(\alpha_{RU}(2\pi(q+u))<\pi-2\pi(q+u)\).

For \(1/2\le U\le8/5\), set
\[
 w=(U-1)^2,\quad
 A=|1-Ue^{-2\pi i(a+u)}|^2,\quad
 B=|1-RUe^{-2\pi i(q+u)}|^2,\quad
 D=|1-Ue^{-2\pi iu}|^2.
\]
The following are exactly the force comparisons in that source:
\[
\begin{array}{c|c|c|c}
u\text{ range}&A\text{ lower bound}&B\text{ lower bound}
                                      &D\text{ upper bound}\\ \hline
(0,1/25]&D&1/3&w+U/15<1/2\\
[1/25,3/50]&D&5/9&w+3U/20\le3/5\\
[3/50,7/100]&w+11U/100&16/25&w+U/5\\
[7/100,3/40]&w+12U/125&3/4&w+9U/40
\end{array}                                                       \tag{13}
\]
Every entry in the \(B\) column follows by minimizing
\(|1-\rho e^{-2\pi i(q+u)}|^2\) over all \(\rho\ge0\).
It therefore holds for the present \(RU\), without an
upper-radius assumption. The other columns are independent
of \(R\). The source's splits of \(U\) at \(5/4,3/2\)
and its concave polynomials consequently prove \(AB>D^3\)
unchanged. More explicitly, in the third row the relevant
large-\(U\) polynomial has endpoint values
\(863/15625,62/15625\); in the fourth row the two endpoint
pairs are \(26397/512000,38257/512000\) and
\(68519/1000000,297/62500\). For \(U\le5/4\), comparison
with \((9/64)D\) has positive coefficients. The first two
rows use \(B>D^2\). These are strict contradictions to the
force equation and prove (12).

The branch is continuous and simple on the compact domain
(2). Its distances from \(\ell\), from \(\delta\), and
from the height bounds
\[
                        |h_*|<H_0:=\log4/(2\pi)                 \tag{14}
\]
therefore have positive minima.

## 3. An all-height cotangent and argument comparison

For \(\ell\le u<\delta\), suppose first \(q+u<1/2\), and put
\[
 \theta=2\pi u,\quad\phi=2\pi q,\quad
 c=\cos\theta,\quad C=\cos(\theta+\phi).
\]
Then \(u<2/5\), so \(\sin\theta>9/20\). Moreover
\[
 c-C=2\sin(\phi/2)\sin(\theta+\phi/2)>9/50.
                                                               \tag{15}
\]
Indeed \(\phi/2\in[\pi/10,11\pi/50]\), while
\(\theta+\phi/2\in[\pi/4,9\pi/10)\), and
\(\sin(\pi/10)>3/10\). Thus
\[
                      c-RC>9/50-3/40=21/200>0.
                                                               \tag{16}
\]
For every \(V>0\), it follows that
\[
 1+R^2V^2-2RVC\ \ge\ 1+V^2-2Vc.                                \tag{17}
\]
Consequently
\[
 \frac{\Re\cot\pi(y+u+i\sigma)}
      {\Re\cot\pi(u+i\sigma)}
 =R\,\frac{\sin(\theta+\phi)}{\sin\theta}
       \frac{1+V^2-2Vc}{1+R^2V^2-2RVC}
 <\frac{43}{18}<3,\qquad V=e^{2\pi\sigma}.
                                                               \tag{18}
\]
The denominator cotangent is positive. If \(q+u\ge1/2\),
the outgoing cotangent is instead nonpositive. The incoming
one is negative because \(1/2<a+u<1\). Therefore, at
**every finite conditional height**,
\[
 -\Re Q_{ss}
 =\pi\{3\Re\cot\pi s-\Re\cot\pi(a+s)-\Re\cot\pi(y+s)\}>0.
                                                               \tag{19}
\]
This supplies strict horizontal concavity and vertical
convexity on every compact strip before the incoming wall.

The same comparison controls the original arguments.
For \(q+u<1/2\), (17) gives
\[
 \frac{d}{dV}\alpha_{RV}(\theta+\phi)
 <\frac{43}{18}\frac{d}{dV}\alpha_V(\theta).
\]
Both arguments vanish at \(V=0\). Integration gives
\[
           0<\alpha_{RV}(\theta+\phi)
                     <(43/18)\alpha_V(\theta).                 \tag{20}
\]
This is a comparison on the original continuous strip lift,
not an independent principal-log reset.

## 4. All omitted physical rows

The sine-entropy identities used in the two real-source proofs
are independent of \(y\):
\[
 I_a(t)\le I_{1/2}(t)\quad(0\le t\le1/2),\qquad
 I_a(t)=J(\delta)+J(t-\delta)\le J(t)\quad(\delta\le t\le1).
                                                               \tag{21}
\]
For the first, the derivative in \(a\) changes sign only
from negative to positive, so the larger endpoint is \(a=1/2\).
For the second, \(J(t)-J(\delta)-J(t-\delta)\) increases and
then decreases between its zero endpoint values.

On \(0<t\le1/8\), the half-incoming physical force is
\[
 \frac{2\cos(\pi t)|1-Ye^{-2\pi it}|}{(2\sin\pi t)^3}>1.
                                                               \tag{22}
\]
The second modulus exceeds \(1/2\) by radial minimization,
\(2\cos(\pi t)>9/5\), and \(2\sin(\pi t)<4/5\).
Hence every physical row \(t\le\ell\) is bounded by \(L(y)\),
and \(L(y)\le L_0(y)\).

The old written bounds give \(J(\ell)<-13/100\).
We sharpen its accompanying half-incoming bound:
\[
 I_{1/2}(\ell)>\frac9{200}.                                     \tag{23}
\]
Indeed \(\cos(3\pi/40)>19/20\), from
\(\cos t>1-t^2/2\) and \(3\pi/40<33/140\);
also \(\log(19/10)>18/29>3/5\).

For \(\ell\le t\le1/2\), the numerator bound \(1+R\) gives
\[
\begin{split}
 E_1(t;y)-L(y)
 &\le(t-\ell)\log(1+R)-2J(t)+3J(\ell)-I_{1/2}(\ell)\\
 &<\frac{49}{400}+\frac7{24}+\frac{51}{3200}
                          -\frac{39}{100}-\frac9{200}
   =-\frac{47}{9600}<-\frac1{250}.                              \tag{24}
\end{split}
\]
Here \(\log((1+R)/2)<3/80\), \(t-\ell\le17/40\), and
the maximum of \(t\log2-2J(t)\) is at \(t=1/4\).
The written bounds \(\log2<7/10\) and
\(b_2=-4J(1/4)<7/12\) are precisely those used in the
positive-output source. By (21), (24) pays every postwall
middle row.

For \(t\ge1/2\), (21) bounds the row rate by
\[
                         I_y(t)-2J(t).
\]
This is the continuous own-four rate at first incoming
angle and height zero. The
[small-positive-output high-row theorem](research_mixed_all_angle_high_rows_with_small_positive_output.md),
including its closed angular endpoints, bounds its maximum by
\[
               \max\{H_{\rm half}(y),2\pi H\},\qquad
                       H_{\rm half}(y)=I_y(1/2).               \tag{25}
\]
The hypothesis is \(H\le1/100<11/125\). No continuous last
rate has been discarded.

Both alternatives in (25) are below \(L_0(y)\).
For the first,
\[
\begin{split}
 L_0(y)-H_{\rm half}(y)
 &\ge I_{1/2}(1/8)-3J(1/8)-\frac38\log(1+R)\\
 &>\frac{93}{200}-\frac9{32}=\frac{147}{800}>0.                 \tag{26}
\end{split}
\]
We used \(-J(1/8)>31/200\), as proved in Section 7 of the
early real-source proof, and
\(\log(1+R)<7/10+3/80<3/4\).
For the second, the same source's radial-minimum witnesses
apply at every positive radius: the outgoing modulus is
above \(7/12\) on \([0,1/16]\) and above \(4/5\) on
\([1/16,1/8]\). Thus
\[
 I_y(1/8)>-1/20,\quad I_{1/2}(1/8)>1/14,\quad
                   L_0(y)>681/1400>2\pi H.                     \tag{27}
\]
For clarity, their logarithm witness is
\(e^{4/5}>827/375>15/7\), giving
\(I_y(1/8)>-\log(15/7)/16>-1/20\).
These arguments do not require \(R\le1\).

Choose a fixed sufficiently small \(\eta>0\), before \(N\),
so that
\[
 \ell<u_*<r(a):=\delta-\eta,\qquad
 E_a(t;y)<L(y)-1/500\quad(\delta-\eta\le t\le\delta).
                                                               \tag{28}
\]
The root margins and uniform continuity of the integrated
rates justify both choices. Every physical index outside
\([\ell,r(a)]\) is now bounded by \(L_0(y)\); the incoming
zero and both true endpoint groups are included.

## 5. Both unweighted joins and all six sampling currents

Put \(F(u,\sigma)=\Re Q(u+i\sigma;a,y)\).
On the entire prewall strip, at arbitrary finite heights,
\[
 F_\sigma=-\alpha_V(2\pi(a+u))
           -\alpha_{RV}(2\pi(q+u))
           +3\alpha_V(2\pi u)-2\pi a .
                                                               \tag{29}
\]
For \(\sigma\ge0\), original strip argument intervals give
\[
 F_\sigma\le2\pi-4\pi u+
                       \max(2\pi(q+u)-\pi,0)\le17\pi/10.
                                                               \tag{30}
\]
For \(\sigma\le0\), the incoming argument is nonpositive.
If the outgoing angle is below one half, use (20); otherwise
its argument is nonpositive as well. Thus
\[
 F_\sigma\ge-2\pi a\ge-7\pi/4.
\]
In particular,
\[
 \partial_\sigma(F-2\pi\sigma)\le-3\pi/10\quad(\sigma\ge0),
 \qquad
 \partial_\sigma(F+2\pi\sigma)\ge\pi/4\quad(\sigma\le0).
                                                               \tag{31}
\]
Every weighted vertical half reduces to its real cut.
A sufficiently tall fixed rectangle consequently gives
any prescribed loss \(B\) on both horizontal corrections:
take its height larger than \(H_0+1\) and then large enough
using (31), the compact upper bound on \(F(u,0)\), and
the compact lower bound on \(\Re\Theta\).

At the original critical height, (19) bounds the whole
horizontal by \(\Re\Theta\). For either real cut, (19)
also gives vertical convexity. Its unweighted join is
therefore bounded by the larger of its real-cut rate
and its critical-height endpoint rate. Equations (28)
and (22) bound the former by \(L_0\), and horizontal
concavity bounds the latter by \(\Re\Theta\).
This treats both unweighted joins without replacing a
central physical row by an unproved absolute estimate.

Use the exact original functions from the
[joint factorial chart](research_mixed_fourier_right_cap_joint_global_chart.md),
\[
 \Pi_N(w)=G_N(Nw)
       \exp\!\left\{\frac{\pi i}{2}[N(w-w^2)-w]\right\},
 \qquad E_N(w)=1/\Pi_N(w)\quad(0<\Re w<1).
\]
They obey the exact unit recurrence and
\(\Pi_N(j/N)=P_j\). The literal interpolant is
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                             E_N(a)E_N(y)E_N(s)^3.             \tag{32}
\]
It equals the row of (1) at \(s=j/N\). On the fixed
rectangle every factorial argument has real part in
a compact subset of \((0,1)\), since \(a+r(a)=1-\eta\).
The [canonical complex factorial expansion](exact_factorial_interpolation_and_complex_contours.md),
Section 4, therefore bounds it by
\(C_\tau N^{A_\tau}e^{N(F+\tau)}\), with the original
phase and no branch or scalar reset.

Set
\[
 L_N=\lfloor N\ell\rfloor+1,\quad M_N=\lceil Nr(a)\rceil,\quad
 \ell_N=(L_N-\tfrac12)/N,\quad r_N=(M_N-\tfrac12)/N .
\]
The [original split-cotangent identity](research_mixed_conditional_lower_output_middle_reduction.md),
Section 4, is exactly
\[
\begin{split}
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
 ={}&N\int_{\ell_N}^{r_N}T_N(s)\,ds\\
 &+\frac{N}{2i}\left\{
 \int_{\partial R^+_{\rm off}}T_N(s)(\cot\pi Ns+i)\,ds+
 \int_{\partial R^-_{\rm off}}T_N(s)(\cot\pi Ns-i)\,ds\right\}.
\end{split}                                                       \tag{33}
\]
Keep the induced orientations and both horizontal/four
vertical corrections. On each half-grid vertical the
matching weight has modulus at most
\(2e^{-2\pi N|\Im s|}\); on fixed horizontal sides the
constant four suffices for all large \(N\). Equations
(30)--(31) pay every correction. Moving only the zero-mode
integral gives the two joins just estimated and the
unchanged coefficient \(+N\).

Finally, the omitted sums retain every \(0\le j<L_N\)
and \(M_N\le j<N\). Apply the
[zero-safe physical-row argument](research_mixed_conditional_contour_allowance.md),
Section 2: regularize each numerator logarithm before
taking upper Riemann sums, and retain the uniform
\(NJ(j/N)+O(\log N)\) denominator estimate through all
\(j<N\). The integrated excess tends uniformly to zero
on the present compact parameters. This includes all
numerator zeros and both parity endpoints. The physical
rates are exactly (5), and Section 4 pays all of them.
Assign a single total tolerance to symbols, rounded cuts,
row sums and contour lengths. This proves (8), with the
claimed arbitrary fixed horizontal-alias loss.

## 6. Comparison with the fixed half-point main

The [unit-circle multiplier theorem](research_mixed_four_conditional_unit_multiplier.md)
has precisely the outgoing restrictions already checked
in Section 2. Hence
\[
                         \Re\Theta(a,y)\le\Re\Theta(1/2,y).
                                                               \tag{34}
\]
At \(a=1/2\), choose \(r_0<1/2\) beyond the compact critical
family. Vertical convexity (19) and \(Q_s(s_*;1/2,y)=0\)
give, for every stated \(h_s\),
\[
 \Re\Theta(1/2,y)
 \le\max_{\ell\le v\le r_0}\Re Q(v+ih_s;1/2,y).
                                                               \tag{35}
\]
There is no height extension hidden in this inequality:
(19) holds at all finite heights. Also
\(\rho=e^{2\pi h_s}>1/2\), because
\(\log2>56/81>27\pi/125\).

We can clip the maximum in (35). Its folded real force is
\[
 \frac{|1+\rho e^{-2\pi iv}|\,
       |1-R\rho e^{-2\pi i(q+v)}|}
      {|1-\rho e^{-2\pi iv}|^3}.
                                                               \tag{36}
\]
For \(\ell\le v\le1/8\), the first numerator is at least
one, the second exceeds \(4/5\), and the own square is
less than \(3/5\). The force exceeds one.

For \(1/8\le v\le1/6\), the first numerator square is at
least \(1+\rho^2+\rho\); the second is at least \(1/2\).
The latter follows by radial minimization before
\(q+v=1/4\), and by the bound one afterwards.
If \(\rho\le3/4\), the own square is at most \(13/16\)
and the squared numerator at least \(7/8>(13/16)^3\).
If \(\rho\ge3/4\), the own square is at most one and
the squared numerator at least \(37/32>1\).
Thus the maximum can be increased to \(v\ge1/6\).

For \(5/12\le v\le1/2\), put
\[
 D_\rho=1+\rho^2+12\rho/7,\qquad
 D_\rho-\frac75(1+\rho)
       =\rho^2+\frac{11}{35}\rho-\frac25\ge1/140.
\]
The own square is larger than \(D_\rho\). The numerator
moduli are at most \(1+\rho\) and \(R(1+\rho)\).
The squared force is consequently less than
\[
 R^2(1+\rho)(5/7)^3
 \le(43/40)^2\,250/343<1.                                      \tag{37}
\]
It increases the profile to move left to \(5/12\).
Equations (35)--(37) bound the maximum by (6), proving (7).

The comparison uses individual original phase profiles.
It is not a lower bound for a finite conditional sum.
An attached cap and next kernel still require a
profilewise comparison, with both shared Fourier upper
alternatives and their original weights. In particular
(7) alone does not complete a selected second-left path.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_second_early_real_first_arc.md | ef9c322a418436d52015c90aea221a9ef602fda54cbe7aa1f96d3321c25cce11 |
| research_mixed_four_conditional_positive_output_real_arc.md | f3c971ea0c2c24f82c2250db5c8c1196a9700b6d3bb57849cf4130f4353cc0c2 |
| research_mixed_all_angle_high_rows_with_small_positive_output.md | d74aecddc265f534d1a5af266df8565536e331f92ae36eef595cb3ab0dab2e0c |
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_four_conditional_unit_multiplier.md | 4d73d90557948056413ef0445cb7754569cbbc03e7ff3f35ecab0f3e9fe8f66f |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

The author has read the complete proof and all nine directly
used source implications and checked their bindings. Independent
full proof/direct-source review is required before adoption.
No mathematical numerical evaluation, test, import, compilation,
or frozen-source edit was used.
