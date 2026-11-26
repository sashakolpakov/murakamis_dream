# The complete first-four cap with the last row of its three neighbor

Private written proof, 10 November 2026. The complete first-four cap
and the last-row rate of its own-three neighbor lie below their
original joint supporting plane at every actual fixed early height.
The next outgoing height may have either sign. The new step localizes
the maximum of the cap's negative-height main profile before applying
the exact joint derivative. Both real cuts, both aliases, and the true
cap index ends are retained separately.

The finite conclusion pays the entire late physical block through
the literal final index. It does not assert a bound for the remaining
wrapped ordinary sum or for a whole word. No mathematical numerical
evaluation is used.

## 1. Original source, reference and endpoint rate

Fix an actual positive three/four open word of length at least three
beginning with types four and three. Use the same coupled reference
and original phases as in the
[first-four/three central theorem](research_mixed_early_four_three_positive_private_central.md):
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad e_*=u_*+ih_*.
\tag{1}
\]
Its endpoint and attached-height bounds are
\[
\begin{gathered}
 .246<a_0<.350,\quad -.070<c<-.020,\quad
 .333<u_*<.363,\quad -.051<h_*<-.019,\\
 -.065\le d\le.068.
\end{gathered}
\tag{2}
\]
The assumption on the ordinary private critical height in that
central theorem is not imposed here: neither the last rate nor the
proof below uses that height. All variables in (1) remain those of
the same actual reference, rather than independent box points.
Keep their displayed heights fixed and take
\[
 a=x+ic,\quad b=z+id,\qquad
 \frac1{10}\le x\le\frac{11}{50},\quad
 \frac{11}{50}\le z\le\frac9{20}.
\tag{3}
\]
With the original primitives and logarithmic lifts, put
\[
\begin{split}
 \Xi_1(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea-g(e)-\tfrac12g(a),\\
 F_{10}(s;a,b)&=g(s+a)+g(s+b)-2g(s)+2\pi ias
                                      -\tfrac32g(a)-g(b),
\end{split}
\tag{4}
\]
where \(J'(v)=\Log(2\sin\pi v)\),
\(g(v)=J(v)+\pi i(v-v^2)/2\), and \(S\) is the complete
endpoint coefficient action. Write
\(L_1=\operatorname{stat}_e\Xi_1\) and
\(\phi_{10}=\operatorname{stat}_sF_{10}\) on the original
critical branches. Their first-coordinate marginals cancel:
\[
                  L_1'(a_*)+\partial_a\phi_{10}(a_*,b_*)=0.
\tag{5}
\]
For \(\kappa=1/2500000\), retain the original plane
\[
\begin{split}
 \Gamma(z)&=\Re L_1(a_*)+\Re\phi_{10}(a_*,b_*)
       +\Re\partial_b\phi_{10}(a_*,b_*)(z-b_0)
                                      -\kappa(z-b_0)^2,\\
 \gamma&=\kappa(a_0-11/50)^2>\kappa(13/500)^2>0.
\end{split}
\tag{6}
\]

For \(r_N=e^{-2\pi i/N}\), set
\[
 \begin{gathered}
 P_j=(r_N;r_N)_j,\quad p_j(X)=(r_NX;r_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\\
 R_{j,N}(a,b)=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^2}.
 \end{gathered}
\tag{7}
\]
The full first cap is \(U_{1,N}(w,X)\), and the first Fourier
weight is the complete unselected factor \(d_N(X)\). There is
no outgoing own-three halfweight at \(Y\), and no selected monomial
or \(1+X^{-N}\) factor is introduced. The allocated ordinary
row rate is
\[
\begin{split}
 \mathcal R(s;a,b)={}&\int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt
   +\int_0^s\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &-2J(s)-2\pi cs-\tfrac12\Re g(a).
\end{split}
\tag{8}
\]
In particular its exact continuous endpoint is
\[
 \mathcal R(1;a,b)=\lambda-\tfrac12\Re g(a),\qquad
                \lambda=2\pi(-c+d_+).
\tag{9}
\]
Here \(c<0\), but \(d\) has either sign. Formula (9) uses
the full-period logarithmic means, not a choice of a single revived
carrier. It is a rate statement, not an identification with a
possibly vanishing finite last-row value.

Let \(\mathcal A(a)\) denote the maximum of the allocated
profiles in the [complete fixed-height cap theorem](research_mixed_cap_early_fixed_height_full_source.md):
\[
\begin{array}{c|c|c}
 \text{profile}&e&\text{penalty }\mathfrak p_e\\ \hline
 \text{main}&u+ih_*,\quad .27\le u\le.49&0\\
 \text{real cuts}&.27,\ .49&0\\
 \text{lower alias}&u-.055i,\quad .27\le u\le.49&.11\pi\\
 \text{upper alias}&u+.04i,\quad .27\le u\le.49&.08\pi .
\end{array}
\tag{10}
\]
Each regular profile is \(\Re\Xi_1(e,a)-\mathfrak p_e\).
Include also the separate true-end profile
\[
 E_{\rm end}-\tfrac12\Re g(a),\qquad
 E_{\rm end}=\frac35+\frac{\log4}{100}<\frac{123}{200}.
\tag{11}
\]
For first type four there is no extra physical upper-row allowance.
These profiles include the two unweighted private joins, every
horizontal and vertical alias, all physical tails and both parity
stops of the complete cap.

**Theorem 1.** Uniformly on (1)--(3),
\[
                  \mathcal A(a)+\mathcal R(1;a,b)
                            \le\Gamma(z)-\gamma.
\tag{12}
\]
Thus, for every \(\tau>0\), the literal late block satisfies
\[
 |U_{1,N}(w,X)|\,|d_N(X)|
       \sum_{j=\lceil N(1-x)\rceil}^{N-1}|R_{j,N}(a,b)|
 \le C_\tau N^{A_\tau}
                  e^{N\{\Gamma(z)-\gamma+\tau\}}.
\tag{13}
\]
It holds for both parities and all real ordinary colors
\(w\in[-2,2]\). It also holds on a sufficiently small fixed
ordinary-color disk about \(-2\), with any prescribed additional
positive rate tolerance; every fixed ordinary-color derivative has
the same rate with polynomial cost on a smaller disk.

## 2. The main cap maximum lies before forty-three hundredths

Put \(r=e^{2\pi c}\). The actual first-four bound gives
\(0<r<9/10\). Indeed
\(e^{\pi/25}>1+3/25>10/9\).
The main private radius obeys
\[
                     e^{2\pi h_*}>18/25.
\tag{14}
\]
For example \(2\pi|h_*|<13/40\), and
\(e^v\le1+v+v^2/[2(1-v/3)]\) gives
\(e^{13/40}\le11849/8560<25/18\).

**Lemma 2.** For every target (3),
\[
        \Re\partial_e\Xi_1(43/100+ih_*,a)<-1/25.
\tag{15}
\]
Consequently the maximum of the main profile in (10) is attained
in \(27/100\le u\le43/100\).

*Proof.* Use the original radical identity, including its fixed branch,
from the [real-row proof](research_mixed_cap_early_taper_real_rows.md)
and its [complex continuation](research_mixed_cap_early_taper_complex_profiles.md):
\[
 S''(e)=-\pi\cot\pi e
        -\frac{2\pi}{\sin\pi e\sqrt{2-e^{-2\pi ie}}}.
\tag{16}
\]
The square root has positive real part. On the real interval
\([.43,.49]\),
\[
 \cot\pi e<1/4,\quad \sin\pi e>39/40,\quad
 \Re(2-e^{-2\pi ie})>29/10>25/9.
\]
The first two bounds follow from \(.07\pi<11/50\), using
\(\tan t\le t/(1-t^2/2)\) and \(\cos t\ge1-t^2/2\).
The third uses \(\cos(.14\pi)>9/10\).
Thus, with \(\ell(u)=\Re S(u)\),
\[
 -\ell''(u)<\pi(1/4+16/13)=77\pi/52.
\]
The source bound \(\ell'(.49)<-\log2+19/500\) implies
\[
           \ell'(.43)<-\log2+19/500+231\pi/2600.
\tag{17}
\]
At the real private point \(e=.43\), exact differentiation gives
\[
 \Re\Xi_{1,e}(e,a)=\ell'(e)
    +\log|\sin\pi(e+a)|-\log(\sin\pi e)+\pi c.
\tag{18}
\]
The function \(c\mapsto\log\cosh(\pi c)+\pi c\) is
increasing. Since \(c<-1/50\),
\[
 \log|\sin\pi(e+a)|+\pi c
 \le\log\cosh(\pi c)+\pi c
 <1/500-3/50=-29/500.
\]
Here \(\log\cosh t\le t^2/2\), \(\pi^2<10\), and
\(\pi>3\) suffice. Equations (17)--(18) yield
\[
 \Re\Xi_{1,e}(.43,a)
 <-\log(39/20)-1/50+231\pi/2600.
\tag{19}
\]

We next transport this derivative down the actual private height.
Set \(e=.43+i\xi\), \(-.051\le\xi\le0\),
\(R=e^{2\pi\xi}\), and \(w_0=2-Re^{-.86\pi i}\).
Then \(18/25<R\le1\), and the same elementary angle bounds give
\[
 \Re w_0>2+(9/10)R>331/125>64/25,\quad
 0<\Im w_0<(11/25)R,\quad
 0<\arg\sqrt{w_0}<11/145.
\tag{20}
\]
For the last inequality, bound the argument by one half of the
imaginary-to-real ratio and maximize
\(R/[2+(9/10)R]\) at \(R=1\).
Also \(|\sin\pi e|>39/40\), and
\(-\pi/2<\arg\sin\pi e\le0\). Hence
\(Z=\sin\pi e\sqrt{w_0}\) has modulus greater than
\(39/25\), argument greater than \(-\pi/2\), and argument
less than \(11/145\). If its argument is nonpositive,
\(\Im(-2\pi/Z)\le0\); otherwise \(\sin t\le t\) gives
\[
                  \Im(-2\pi/Z)<110\pi/1131<\pi/10.
\tag{21}
\]
Since \(\Im\cot\pi e\ge0\), (16) implies
\(\Im S''(e)<\pi/10\).
Now
\[
 \Xi_{1,ee}=S''(e)+\pi\cot\pi(e+a)-\pi\cot\pi e+i\pi.
\tag{22}
\]
The real part of \(e+a\) is in \([.53,.65]\), while its
height is negative. Its cotangent has imaginary part between
zero and one: in the exact formula the numerator is
\(\sinh(2\pi|\Im(e+a)|)\), and the denominator is
\(\cosh(2\pi\Im(e+a))-\cos(2\pi\Re(e+a))\), with a
negative cosine. It follows that
\[
                         \Im\Xi_{1,ee}<21\pi/10.
\tag{23}
\]
Because \(\partial_\xi\Re\Xi_{1,e}=-\Im\Xi_{1,ee}\),
the increase in (19) during downward transport is less than
\[
                   (51/1000)(21\pi/10)<17/50.
\]
Finally
\(\log(39/20)>38/59>16/25\) by the positive atanh series,
and \(231\pi/2600<7/25\). Substitution into (19) gives
\[
 -16/25-1/50+7/25+17/50=-1/25,
\]
proving (15).

The [joint early curvature theorem](research_mixed_cap_joint_early_horizontal_concavity.md)
gives strict private horizontal concavity on the entire original
product used here. Thus the real derivative remains negative for
every \(u\ge.43\); replacing such a point by \(u=.43\)
increases the profile. This proves the maximum assertion without
choosing or differentiating a moving private critical point.
\(\square\)

## 3. Exact transport of the main, the real cuts and the upper alias

For a regular cap point \(e=u+i\xi\), put
\[
 N_e=|1-r e^{2\pi\xi}e^{-2\pi i(u+x)}|,\qquad
 D=|1-r e^{-2\pi ix}|.
\]
The unchanged allocations (4), (9) give
\[
 \partial_x\{\Re\Xi_1(e,a)+\mathcal R(1;a,b)-\mathfrak p_e\}
                            =\log(N_e/D^2).
\tag{24}
\]
In particular \(d_+\) contributes no derivative. Both halves of
the first Fourier weight are needed for the denominator exponent.

For the main maximum, Lemma 2 permits restriction to
\(.27\le u\le.43\). Thus \(.37\le u+x\le.65\) and
\(\cos2\pi(u+x)<-7/12\). One elementary witness is
\(\sin^2(\pi/5)=(5-\sqrt5)/8>11/32>49/144\), using
\(\sqrt5<9/4\). Together with (14),
\[
              N_e^2>1+324r^2/625+21r/25.
\tag{25}
\]
For \(x\le4/25\), \(D^2<1+r^2-r<1\) whereas
\(N_e>1\), so (24) is positive. For \(x\ge4/25\),
the source's elementary bound \(\cos(2\pi x)>14/75\)
gives \(D^2<1+r^2-28r/75\). Subtracting its square from
(25) gives
\[
\begin{split}
 N_e^2-D^4&>rQ(r),\\
 Q(r)&=119/75-(9118/5625)r+(56/75)r^2-r^3>0.
\end{split}
\tag{26}
\]
Indeed \(Q'\) has negative leading coefficient and discriminant
\(-96872/5625<0\), so \(Q\) decreases; its endpoint is
\(Q(9/10)=269/75000>0\). Each permitted main point therefore
transports favorably to \(x=.22\).

For both real cuts and the upper alias, the private radius is at
least one. On the full private real interval,
\(\cos2\pi(u+x)<-6/25\) and \(\cos2\pi x>9/50\),
as established in the
[original first-four last-row proof](research_mixed_first_four_four_true_last_row_calibration.md).
Consequently
\[
 N_e^2>1+r^2+12r/25,\qquad D^2<1+r^2-9r/25,
\]
and
\[
 N_e^2-D^4>r\{6/5-(706/625)r+(18/25)r^2-r^3\}>0.
\tag{27}
\]
The cubic decreases because the derivative discriminant is
\((1296-8472)/625<0\); at \(r=9/10\) its value is
\(939/25000>0\). The upper alias penalty remains \(.08\pi\).

At \(x=.22\), the complete cap plane and the completed typed
ordinary last-row plane apply at the same actual reference. The
latter includes all four revived carriers, hence also (9), for
either sign of \(d\). Their first marginals cancel by (5), and
each retains its first-coordinate quadratic loss. Thus every
transported profile in this section is bounded by
\[
                         \Gamma(z)-2\gamma.
\tag{28}
\]
Taking the maximum over the fixed private intervals preserves
this inequality. No ordinary endpoint-selection assertion is used.

## 4. The lower alias and true cap index ends

The source-specific lower-alias comparison, equation (31) of the
first-four/three central theorem, holds independently of the ordinary
private height:
\[
 \Re\Xi_1(u-.055i,a)-.11\pi
 <\Re\Xi_1(u+ih_*,a)-211\pi/3125.
\tag{29}
\]
It follows by integrating the original derivative bound
\(\Im\Xi_{1,e}<59\pi/50\) through a height interval shorter
than \(9/250\), retaining the entire Fourier penalty.
Adding (9) to both sides and applying the main comparison (28)
pays this complete alias. Its private real coordinate need not
belong to the shorter interval from Lemma 2: that lemma bounds
the entire main maximum first.

For the true-end profile (11), the combined derivative is instead
\[
 \partial_x\{E_{\rm end}-\tfrac12\Re g(a)
                              +\mathcal R(1;a,b)\}=-\log D.
\tag{30}
\]
Throughout the early interval, the bounds used in (27) imply
\(D^2<3/2\): the convex quadratic
\(1+r^2-9r/25\) has endpoint values \(1\) and
\(743/500<3/2\) on \([0,9/10]\).
Thus \(-\log D>-1/4\), since \(\log(3/2)<1/2\).
Transport over the entire length \(3/25\) costs less than
\(3/100\).

At \(x=.22\), the original bare cap plane is greater than
\(79/100\), whereas (11) is less than \(123/200\); its
reserve is greater than \(7/40\). Allocating the outgoing cap
halfweight preserves this comparison by convexity of \(\Re g\),
exactly as in the joint low-row and first-four last-row proofs.
Add the completed ordinary last-row plane there, with the original
marginals and halfweight. After (30), the reserve remains greater
than
\[
                          7/40-3/100=29/200.
\tag{31}
\]
This is larger than \(\gamma<\kappa\). Equations (28)--(31)
prove (12) for all five regular profiles and both true cap ends.

## 5. Literal finite late rows, parities and colors

The exact reflected product-integral identity in the
[right-tail theorem](research_mixed_right_tail_reflection.md)
retains drift \(\lambda=2\pi((-c)_++d_+)\). Its proof for
\(0\le v\le\min(x,z)\) uses only \(0<x,z<1/2\), not
that both coordinates lie on the old plateau. Here \(x\le z\),
and for own three it gives
\[
 \mathcal R(1-v;a,b)-\mathcal R(1;a,b)\le-\lambda v\le0,
                              \qquad 0\le v\le x.
\tag{32}
\]
The full zero-safe factorial estimate applies uniformly to every
physical index from \(\lceil N(1-x)\rceil\) to \(N-1\).
It estimates the literal products (7), including zeros and revived
rows, by (8) plus any fixed positive tolerance and a polynomial
factor. No numerator or endpoint value is divided out.

The complete fixed-height cap theorem bounds its entire coherent
private sum by the profiles (10)--(11), uniformly for all real
incoming ordinary colors. Multiply by the full first Fourier
weight: its two allocated halves are exactly those in (4) and (8),
using the original continuation at the negative height \(c\).
Equations (12), (32) bound each remaining absolute ordinary row.
There are at most \(N\) of them. Aggregating the source tolerances
proves (13), with every original scalar unchanged.

Both cap parities, the exact final physical stop \(N-1\), and
all original Fourier corrections inside the cap are part of the
invoked source theorem. Nothing here uses an even-only physical
identity or drops an odd revived row.

Finally the ordinary-color dependence is polynomial of degree
less than \(N\). Its uniform all-real bound extends to a fixed
small Bernstein ellipse with arbitrarily small exponential cost;
that ellipse contains a fixed ordinary disk about \(-2\).
Cauchy estimates on a smaller disk give every fixed ordinary-color
derivative with the same chosen tolerance. Equivalently the real
derivatives follow from the source derivative theorem and polynomial
degree bounds. No continuation is inferred from a bound solely at
the complete color.

The result closes the last-row calibration and the complete late
physical block for first \(4,3\), including positive \(d\).
The wrapped ordinary block still requires its own signed finite-source
argument. Combining the present estimate with a merely conjectured
wrapped cancellation, or identifying it with a whole-word lower
bound, would be a separate unsupported step.

## Source bindings

All files are unchanged and were read directly. The proof uses their
original source identities and already proved inequalities; it does
not evaluate saved enclosures or rerun any certificate.

| File | SHA-256 |
|---|---|
| research_mixed_early_four_three_positive_private_central.md | b8ffb45bbb9eae0d144b0c2e219207509aa7a119543560b058dfca1734e7c289 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_cap_early_taper_real_rows.md | d82b0506e7e156463360773bc8ab0e798334ee3a733ce9e6275215027c9c7ebc |
| research_mixed_cap_early_taper_complex_profiles.md | 6a7b8cd841d89690a9733c1005a2449ce808ba20a875c2d1f8d8ca0b0a769138 |
| research_mixed_cap_joint_early_horizontal_concavity.md | 1b623741d70402af77287b287aa1e2636b0b8d1abcb7275d5347f14ac75dbb20 |
| research_mixed_first_four_four_true_last_row_calibration.md | 52c149d8500e88c6e4e3fdf1c9e699baf376dfaac8b96d3461dc81f9d1725e0d |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_typed_last_row_support_completion.md | 70e842fee569d7429cec8fe38441012dd5775c5fb248bba6656a2ea7cc1b24aa |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

No numerical evaluation, import, test or compilation was performed.
The earlier notes and frozen manuscripts are unchanged.
