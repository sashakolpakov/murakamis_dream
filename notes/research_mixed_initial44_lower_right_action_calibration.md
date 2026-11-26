# The original four/four action on the lower right interval

Private written deduction, 10 November 2026. The moving critical
action of the first conditional factor is bounded by the original
geometric supporting plane when the incoming real coordinate runs
from one half to seven tenths. Multiplication by the complete first
cap and its Fourier weight preserves a strict deficit.

The conditional factor itself is not replaced by its critical action
in this theorem. Its other finite contour contributions still need
their own estimates.

## 1. The same reference and the action to be bounded

Use an actual positive three/four word of length at least three
beginning with four and four. Keep the notation and bounds of the
[complete pair theorem through one half](research_mixed_initial44_right_half_interval.md):
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\quad
 s_*=v_0+ih_s,\qquad
 .246<a_0<.350,\quad -.078<c<-.020,
\]
\[
 -.102\le d\le-.001,\qquad -.108\le h_s<0,\qquad
 a_0,b_0,v_0\in P=[11/50,9/20].
\tag{1}
\]
These are coordinates of the same original coupled reference.
The independent targets in this note are
\[
 a=x+ic,\quad 1/2\le x\le7/10,\qquad
 b=z+id,\quad z\in P,\qquad a_L=1/2+ic.
\tag{2}
\]
Write \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\). The original
primitive and conditional phase are
\[
 g(q)=J(q)+\frac{i\pi}{2}(q-q^2),\qquad
 J'(q)=\operatorname{Log}(2\sin\pi q),\quad J(0)=0,
\]
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias.
\tag{3}
\]
All logarithms continue from the original positive real sine chamber.
The allocated phase used by the pair theorem is
\[
 F(s;a,b)=Q(s;a,b)-\tfrac12g(a)-\tfrac12g(b).
\tag{4}
\]

Retain its original cap action \(L_1\), ordinary action \(\phi\),
and constants
\[
 \kappa=\frac1{2500000},\qquad \kappa_R=\frac{8\kappa}{9},
\]
\[
 \Lambda(z)=\Re\{L_1(a_*)+\phi(a_*,b_*)\}
              +\Re\phi_b(a_*,b_*)(z-b_0).
\tag{5}
\]
The stationary equation is \(L_1'(a_*)+\phi_a(a_*,b_*)=0\).
Define the two fixed supporting planes at the half endpoint by
\[
 B_*=\Re L_1(a_*)+\Re L_1'(a_*)(1/2-a_0)
                              -\kappa(1/2-a_0)^2,
\]
\[
 B_R(z)=\Re\phi(a_*,b_*)+
   \Re\phi_a(a_*,b_*)(1/2-a_0)+
   \Re\phi_b(a_*,b_*)(z-b_0)
   -\kappa_R\{(1/2-a_0)^2+(z-b_0)^2\}.
\tag{6}
\]
Their sum is exactly
\[
 B_*+B_R(z)=\Lambda(z)
     -(\kappa+\kappa_R)(1/2-a_0)^2-\kappa_R(z-b_0)^2.
\tag{7}
\]

## 2. The critical branch on the required parameter set

Put \(r=|X|=e^{2\pi c}\). Then \(3/5<r<1\).
Indeed \(2\pi|c|<39\pi/250<1/2\), and the positive exponential
series gives
\[
 e^{1/2}
 <1+\frac12+\frac{1/8}{1-1/6}
 =\frac{33}{20}<\frac53.
\]
For (2), \(\Re X<0\), \(\Im X\ge0\), and
\[
 |X|^2(3-2\Re X)>3(3/5)^2=\frac{27}{25}>1.
\tag{8}
\]
Also \(\Im Y<0\), \(|Y|\le1\), and \(\Re Y<1\).
Thus the [algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md)
applies. The exact cubic
\[
 (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0
\tag{9}
\]
has a unique simple upper-half-plane root. With
\[
 t(a,b)=\frac{\operatorname{Log}v}{2\pi i},\qquad
 \Theta(a,b)=Q(t(a,b);a,b),\qquad
 \omega=\frac{v-X}{1-X},
\]
its conclusions are
\[
 Q_s(t;a,b)=0,\quad 0<\Re t<1-x,\qquad
 \Theta_a=\operatorname{Log}\omega,\quad
 \Im\omega>0,\quad 0<|\omega|<1.
\tag{10}
\]
The logarithmic lift in (10) is zero in the original phase.

The critical-strip bounds in Section 5 of the
[lower-output reduction](research_mixed_conditional_lower_output_middle_reduction.md)
extend to this slightly deeper incoming height:
\[
 \frac15<|v|<2,\qquad \frac2{25}<\Re t<1-x,\qquad
 |\Im t|<H_*:=\frac{\log5}{2\pi}.
\tag{11}
\]
Here is the check of that extension. The monic cubic bound still
uses coefficient moduli at most \(3,4,1\). Its reciprocal polynomial is
\[
 w^3+(Y-3)w^2+(2-Y/X)w+(1/X-1).
\]
The latter coefficients now have bounds \(4,11/3,8/3\);
their maximum is still four. The same strict Cauchy estimate
therefore gives \(1/5<|v|<5\).
If \(|v|\ge2\), the three logarithms in \(Q_s\) each have
argument of modulus at most \(\pi/6\), and their multiplicities
give \(\Im Q_s\ge2\pi x-5\pi/6>0\). This contradicts (10).

For the real-part lower bound, the proof in the cited reduction
uses \(T=1/r\) only through \(T\ge1\). When
\(U=e^{2\pi\Im t}\ge8/5\), its argument comparison gives
\(\Im Q_s<-\pi/50\) if \(\Re t\le2/25\).
When \(1/2<U<8/5\), its exact squared-force comparison is
\[
 |e^{Q_s}|^2=
 \frac{|T-Ue^{-2\pi i(x+\Re t)}|^2
       |1-|Y|Ue^{-2\pi i(z+\Re t)}|^2}
      {|1-Ue^{-2\pi i\Re t}|^6}
 >\frac{24/25}{(5/6)^3}>1.
\]
The first numerator lower bound is increasing in \(T\ge1\);
no upper bound \(T\le8/5\) is needed. This proves (11).

The same source proves
\[
 \Re Q_{ss}(u+i\sigma;a,b)<0,\qquad
 2/25\le u<1-x,\quad |\sigma|\le H_* .
\tag{12}
\]
Its proof is independent of the incoming negative height: the
incoming shifted cotangent is nonpositive, the own cotangent is
positive, and the only positive outgoing case uses
\(\Re\cot\pi(b+s)<4/5\). The bounds on \(z\) and
\(\cosh(2\pi\sigma)\le13/5\) are unchanged. Thus its explicit
bound in that case, \(-43\pi/2440\), remains valid.

## 3. Calibrating the moving point at the half endpoint

The pair theorem, equations (10)--(11), gives
\[
 \Re F(u+ih_s;a_L,b)\le B_R(z),\qquad
                         1/8\le u\le1/2.
\tag{13}
\]
At this fixed negative private height, the value at \(u=1/2\)
is regular. Extend (13) to \(2/25\le u\le1/8\) as follows.
Put \(U=e^{2\pi h_s}\), \(R=|Y|\), and \(T=1/r\).
The original bound \(.216\pi<\log2\) gives \(1/2<U<1\).
The exact force, including the incoming chirp, is
\[
 |e^{Q_s}|^2=
 \frac{|T-Ue^{-2\pi i(1/2+u)}|^2
       |1-RUe^{-2\pi i(z+u)}|^2}
      {|1-Ue^{-2\pi iu}|^6}>1.
\tag{14}
\]
Both shifted cosines are negative, since
\(1/2+u\in[.58,.625]\) and \(z+u\in[.30,.575]\).
Each numerator square is therefore greater than one.
For the denominator, \(\cos(2\pi u)\ge\sqrt2/2>7/10\), so
\[
 |1-Ue^{-2\pi iu}|^2
 <1+U^2-\tfrac75U
 \le\max\{11/20,3/5\}=3/5.
\]
This proves (14). Consequently \(\Re Q\), and hence \(\Re F\),
increases to the already bounded cut \(u=1/8\).

To pass from this fixed height to the moving critical height, define
\[
 m(\sigma)=\max_{2/25\le u\le1/2}
                        \Re Q(u+i\sigma;a_L,b),
                         \qquad |\sigma|\le H_*.
\tag{15}
\]
The continuous boundary value from \(u<1/2\) is understood at
\(u=1/2\). Equation (12) makes every profile in (15) vertically
convex. Its boundary value is convex as well: it is a finite
pointwise limit of those convex profiles. The logarithmic
singularity, when \(a_L+s=1\), has a finite continuous primitive
value. Thus \(m\), a maximum of convex functions, is convex.
This is the same minimax argument as Section 3 of the
[closed-half-output theorem](research_mixed_four_conditional_closed_half_output.md),
now using the four/four fixed-height comparison (13).

At \(\sigma=\Im t(a_L,b)\), (10)--(12) give a unique interior
maximizer \(u=\Re t(a_L,b)\). Its height derivative is
\(-\Im Q_s=0\). The derivative of the maximum is therefore zero
there. Convexity proves that this height minimizes \(m\).
The original height \(h_s\) belongs to the same interval, so
\[
 \Re\Theta(a_L,b)\le m(h_s).
\tag{16}
\]
Since \(\Re g(a_L)=0\), equations (4), (13)--(16) imply
\[
 \boxed{\quad
 \Re\Theta(a_L,b)-\tfrac12\Re g(b)\le B_R(z).
 \quad}
\tag{17}
\]
This compares the original critical action with a fixed contour
bound. It neither infers a lower bound from a signed finite upper
bound nor asserts concavity of the eliminated action.

## 4. Transport and the complete cap multiplier

Equation (10) gives \(\partial_x\Re\Theta=\log|\omega|<0\).
Hence, for all (2),
\[
             \Re\Theta(a,b)\le\Re\Theta(a_L,b).
\tag{18}
\]
The [complete cap transport theorem](research_mixed_first_four_cap_lower_right_horizontal.md)
proves, for every \(\tau>0\),
\[
 |U_{1,N}(w,X)d_N(X)|\le C_\tau N^{A_\tau}e^{N(B_*+\tau)}
\tag{19}
\]
for both parities and all real ordinary colors \(w\in[-2,2]\).
It includes every private row and every original contour term.
The exact Fourier estimate retains
\[
 |d_N(Y)|^{1/2}
       \le C_\tau N^{A_\tau}e^{N(-\Re g(b)/2+\tau)}
\tag{20}
\]
on \(b\in P+id\); the forcing alternative has rate zero and
\(\Re g(b)<0\). Neither finite weight is divided out.

**Theorem 1.** For every prescribed positive allowance \(\tau\),
the complete cap times the conditional critical exponential obeys
\[
 \begin{split}
 &|U_{1,N}(w,X)d_N(X)|\,|d_N(Y)|^{1/2}
                                       e^{N\Re\Theta(a,b)}\\
 &\quad\le C_\tau N^{A_\tau}
 \exp N\left\{\Lambda(z)-\kappa_R(z-b_0)^2
        -(\kappa+\kappa_R)(1/2-a_0)^2+\tau\right\}.
 \end{split}
\tag{21}
\]
All references and targets are as in (1)--(2), both level parities
are included, and the ordinary color ranges over its whole real
interval. The fixed ordinary-color neighborhoods and derivatives
supplied by the cap theorem are also included.

*Proof.* Multiply (19)--(20), apply (17)--(18), and use the exact
plane identity (7). Divide the one requested allowance among the
finitely many bounds. This proves (21). The ordinary-color
extension changes only the cap factor. \(\square\)

The positive deficit in (21) is uniform because \(a_0<.350\).
It also pays the actual local conditional Gaussian: its symbol
is holomorphic and bounded on the compact regular critical charts,
and its normalization is \(N^{-1}\) times \(e^{N\Theta}\).
This is only the local contribution, not the whole conditional
polynomial. Physical rows outside its chart, weighted residue
corrections, and the two unweighted connecting sides remain
separate finite-source obligations. Nor does (21) estimate an
incoming vertical segment at \(x=7/10\) or the rest of the period.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_initial44_right_half_interval.md | 309d6869f7438a9ed0a407c43666198ce1a039db7545c404a5e97f4ba2538c9c |
| research_mixed_four_conditional_algebraic_transport_domain.md | 4788b140b0ab435bb5951db75aadad03376ddaf3bfb6378b8f17242253b7ace0 |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| research_mixed_four_conditional_closed_half_output.md | 33f0bea8bc6e2c35bca2e1f2c5b4eefdebb04805613469e7af376dcaea5b8c11 |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

This deduction uses written inequalities and the stated source
implications. No mathematical numerical evaluation, saved-value
arithmetic, test, import, compilation, or frozen-source edit was used.
