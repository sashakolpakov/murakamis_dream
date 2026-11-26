# The complete first cap at the incoming half face

Research deduction, 7 November 2026. The original type-three cap
has a nonzero asymptotic expansion near \(X=-1\) and complete ordinary
color. The proof keeps the original private cuts \(.27,.49\).
Both real cuts and every alias lie strictly below the cap's own
critical action. The physical tails, actual endpoint rows, and
unweighted joining currents are retained.

This does not compare the cap times the conditional factor with
the reference-dependent affine action of the next selected source.
In particular the earlier obstruction to an arbitrary uniform
prefix ceiling is unchanged. No numerical evaluation or saved
certificate replay is used.

## 1. Exact source and inherited local critical point

Keep
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
                  H_N(w,r^{-j})\frac{p_j(X)}{P_j},
                  \qquad X=e^{-2\pi ia}.
 \end{gathered}                                                   \tag{1}
\]
The endpoint polynomial \(H_N\) and the ordinary color \(w\) are
the original ones. On the retained private rectangle
\[
             E_c=[27/100,49/100]+i[-11/200,1/25],                 \tag{2}
\]
the exact row interpolation is
\[
 \mathscr A_N(e,a,w)=D_N(e)^{-1}C_N(e,w)
                         \frac{\Pi_N(a+e)}{\Pi_N(a)}.
                                                                    \tag{3}
\]
The identity \(H_N(w,r^{-j})=P_jD_N(j/N)^{-1}C_N(j/N,w)\)
shows that (3) equals the summand in (1) at \(e=j/N\).
Its full endpoint coefficient is never replaced by a partial
Newton sum.

Use the original phase
\[
 \Psi(e,a,w)=S(e,w)+J(e+a)-J(a)-i\pi ea.                            \tag{4}
\]
The [half-face critical-point theorem](research_mixed_half_face_cap_critical_point.md)
proves at \(a=1/2,w=-2\) an actual zero of \(\Psi_e\), with zero
logarithmic lift and nonzero \(\Psi_{ee}\). In its notation,
\[
 \begin{gathered}
 f(\omega)=7\omega^3-3\omega^2+5\omega-1,\qquad
 f(\alpha)=0,\quad \alpha\text{ real},\\
 \omega_+=\sigma+i\tau,\quad\tau>0,\qquad
 \sigma=\frac{3/7-\alpha}{2},\quad
 |\omega_+|^2=\frac1{7\alpha},\\
 p_+=\frac{2\omega_+}{1-\omega_+},\qquad
 e_+=\frac{\Log p_+}{2\pi i},\qquad
 u_+=\frac{\Log\omega_+}{2\pi i}.
 \end{gathered}                                                   \tag{5}
\]
Both logarithms have arguments in \((0,\pi)\), and \(\omega_+\)
is the original endpoint branch at \(e_+\). Put
\[
                 h_+=\Im e_+,\qquad M_{\rm half}
                             =\Re\Psi(e_+,1/2,-2).                \tag{6}
\]
The notation \(h_+\) here denotes this fixed negative critical
height, not its positive part.

The same theorem already proves the nonzero packet for the
retained constant-mode integral on
\([.27,.49]+ih_+\). What remains here is to pay every other
piece of the literal finite cap.

## 2. Sharper algebraic enclosure, without root evaluation

The cubic is strictly increasing on the real line, and
\[
 f(4/19)=-\frac{103}{6859}<0,\qquad
 f(3/14)=\frac7{2744}>0.
                                                                    \tag{7}
\]
Thus \(4/19<\alpha<3/14\). Writing \(s=|\omega_+|^2\), (5) gives
\[
 \frac3{28}<\sigma<\frac{29}{266}<\frac18,\qquad
 \frac23<s<\frac{19}{28},\qquad
                         \frac45<\tau<\frac56.                  \tag{8}
\]
For the last two inequalities, use
\(s-\sigma^2>2/3-1/64=125/192>16/25\) and
\(s<19/28<25/36\).

The real and imaginary parts of \(p_+\) are proportional to
\(\sigma-s\) and \(\tau\), with a common positive factor.
Consequently
\[
 \frac23<\frac{89}{133}
       <\frac{s-\sigma}{\tau}<\frac57,\qquad
 \arg p_+=\frac\pi2+\arctan\frac{s-\sigma}{\tau}.                  \tag{9}
\]
The lower bound uses
\((2/3-29/266)/(5/6)=89/133\); the upper uses
\((19/28-3/28)/(4/5)=5/7\).
Moreover
\[
 \arctan(2/3)>\frac23-\frac{(2/3)^3}{3}
             =\frac{46}{81}>\frac{99}{175}>\frac{9\pi}{50}.
                                                                    \tag{10}
\]
For the other direction, \(\sqrt5<56/25\) gives
\[
 \tan^2(\pi/5)=5-2\sqrt5>\frac{13}{25}>\frac{25}{49}.
                                                                    \tag{11}
\]
Equations (9)--(11) prove
\(17/50<\Re e_+<7/20\).

For the height use the exact identity from (5),
\[
 |p_+|^2=\frac4{1+4\alpha+7\alpha^2}
                  <\frac{1444}{777}.
                                                                    \tag{12}
\]
Since \(\pi>25/8\), the positive exponential series gives
\[
 e^{\pi/5}>e^{5/8}>
       1+\frac58+\frac{25}{128}+\frac{125}{3072}
       =\frac{5717}{3072}>\frac{1444}{777}.
                                                                    \tag{13}
\]
The final cross-product difference is \(6141>0\).
The earlier \(|p_+|>1\) then yields the sharper enclosure
\[
 \boxed{\qquad
       \frac{17}{50}<\Re e_+<\frac7{20},\qquad
                         -\frac1{20}<h_+<0 .
       \qquad}                                                    \tag{14}
\]
These are exact algebraic and elementary inequalities for the
already selected original root.

## 3. Both original real cuts lie below the own critical action

At \(a=1/2,w=-2\), the exact curvature is
\[
 -\Psi_{ee}(e)=
 \frac{2\pi}{\sin(2\pi e)}
 +\frac{2\pi}{\sin(\pi e)\sqrt{\,2-e^{-2\pi ie}\,}}.
                                                                    \tag{15}
\]
Its square root is the original principal branch. The
[half-face theorem, Section 4](research_mixed_half_face_cap_critical_point.md)
and the [upper-target theorem, Lemma 1](research_mixed_cap_upper_target_extension.md)
give \(-\Re\Psi_{ee}>0\) on (2), including the positive heights
needed later. Below height zero, the two individual terms in
(15) have positive real part.

First consider
\[
                .27\le x\le .35,\qquad -1/20\le h\le0,
                              \quad e=x+ih.                       \tag{16}
\]
For the first term in (15), its imaginary-to-real ratio is
\[
       |\cot(2\pi x)|\,|\tanh(2\pi h)|
        <\frac34\frac{11}{35}=\frac{33}{140}<\frac8{31}.
                                                                    \tag{17}
\]
Here \(|\cot(2\pi x)|\le\tan(\pi/5)<3/4\);
the latter follows from
\(\sqrt5>20/9\) and \(5-2\sqrt5<5/9<9/16\).
We also used \(|\tanh(2\pi h)|<\pi/10<11/35\).

For the denominator of the second term,
\[
 -\frac{11}{70}<\arg\sin(\pi e)\le0,\qquad
 0<\arg\sqrt{2-e^{-2\pi ie}}<\frac14.
                                                                    \tag{18}
\]
Indeed \(\cot(\pi x)<1\) and
\(|\tanh(\pi h)|<\pi/20<11/70\) prove the first.
For the second, \(e^{-2\pi ie}\) has modulus at most one,
negative real part, and negative imaginary part.
Thus \(2-e^{-2\pi ie}\) has real part greater than two and
imaginary part at most one; its square-root argument is less
than \(\tfrac12\arctan(1/2)<1/4\).
The product in (18) has argument of modulus less than \(1/4\).
As \(\sin(1/4)<1/4\) and \(\cos(1/4)>31/32\), its
reciprocal has imaginary-to-real ratio less than \(8/31\).
These same second-term bounds hold for every
\(.27\le x\le.49\), \(-1/20\le h\le0\).

Write \(\Psi_{ee}=-A+iB\), where \(A>0\). Positivity of
both real parts in (15) and the triangle inequality show on
(16) that \(|B|<(8/31)A\). Along the straight segment
from \(e_+\) to \(c_L=27/100\), put
\[
        d_x=c_L-\Re e_+,\qquad d_y=-h_+.
\]
Equation (14) gives \(d_y/|d_x|<5/7\), so
\[
 \begin{split}
 \Re\{\Psi_{ee}(d_x+id_y)^2\}
 &\le-A d_x^2
       \left(1-\frac{16}{31}\frac57-\frac{25}{49}\right)\\
 &=-\frac{184}{1519}A d_x^2<0.
 \end{split}                                                       \tag{19}
\]
The segment lies in (16). Its first derivative at \(e_+\)
is zero, with the original logarithmic lift. Integrating
(19) twice proves
\[
                  \Re\Psi(c_L,1/2,-2)<M_{\rm half}.              \tag{20}
\]

For the right cut \(c_R=49/100\), put
\[
 d_x=c_R-\Re e_+>\frac7{50},\qquad
                 \varrho=\frac{-h_+}{d_x}<\frac5{14}.
                                                                    \tag{21}
\]
At any nonreal point \(e=x+ih\) on this segment,
\(|h|=\varrho(c_R-x)<\varrho(1/2-x)\). Hence the first
term of (15) has imaginary-to-real ratio
\[
 \cot(2\pi(1/2-x))\,\tanh(2\pi|h|)
                <\frac{|h|}{1/2-x}<\varrho<\frac5{14}.
                                                                    \tag{22}
\]
The limiting value at the real endpoint is zero. The second
term has ratio less than \(8/31<5/14\), by (18).
Thus the same quadratic calculation gives
\[
 \Re\{\Psi_{ee}(d_x-i h_+)^2\}
       <-A d_x^2\left(1-3\frac{25}{196}\right)
        =-\frac{121}{196}A d_x^2<0.
                                                                    \tag{23}
\]
This segment stays in (2). Therefore
\[
                  \Re\Psi(c_R,1/2,-2)<M_{\rm half}.              \tag{24}
\]
All functions are regular on these two fixed compact segments.
Both strict inequalities consequently have fixed positive gaps;
no evaluated minimum is required.

There is also a useful absolute floor. The inherited
[fixed-cut proof, equations (7)--(14)](research_mixed_next_half_face_fixed_cut_obstruction.md)
proves \(\Re\Psi(c_L,1/2,-2)>47/50\) from the saved original
endpoint scalar and elementary \(J\)-bounds. With (20),
\[
                             M_{\rm half}>\frac{47}{50}.        \tag{25}
\]
This uses the written strict bound, without replaying its saved
scalar calculation.

## 4. Both whole horizontal aliases are below the same action

The original endpoint rectangle supplies throughout (2)
\[
 .17<\Re u_c(e)<.28,\qquad \Im u_c(e)>0,\qquad
                         0<\Re(e-u_c(e))<1/2.                   \tag{26}
\]
Use the exact envelope derivative
\[
 \Psi_e(e,1/2,-2)
       =-J'(e-u_c(e))+i\pi u_c(e)+J'(e+1/2)-i\pi/2.
                                                                    \tag{27}
\]
For \(\Im e\le0\), the sine at \(e-u_c(e)\) has negative
argument, while the sine at \(e+1/2\) has nonnegative argument.
These are the original strip logarithms. Equation (26) implies
\[
                 \Im\Psi_e(e,1/2,-2)>-\frac{33\pi}{100}
                           \qquad(\Im e\le0,\ e\in E_c).         \tag{28}
\]
Horizontal strict concavity through the critical point gives
\(\Re\Psi(x+ih_+,1/2,-2)\le M_{\rm half}\).
Integrating (28) from \(h_+\) to zero and using (14) yields
\[
           \Re\Psi(x,1/2,-2)
                  <M_{\rm half}+\frac{33\pi}{2000}
                         \qquad(.27\le x\le.49).                \tag{29}
\]

On the whole rectangle, each original sine logarithm has
imaginary part between \(-\pi/2\) and \(\pi/2\).
Equations (26)--(27) therefore give
\[
       -\frac{133\pi}{100}<\Im\Psi_e(e,1/2,-2)
                                    <\frac{78\pi}{100}.          \tag{30}
\]
Consequently, with the exact residue penalties,
\[
 \begin{split}
 \Re\Psi(x+i/25,1/2,-2)-2\pi/25
       &<\Re\Psi(x,1/2,-2)-\frac{67\pi}{2500}\\
       &<M_{\rm half}-\frac{103\pi}{10000},\\
 \Re\Psi(x-11i/200,1/2,-2)-11\pi/100
       &<\Re\Psi(x,1/2,-2)-\frac{671\pi}{10000}\\
       &<M_{\rm half}-\frac{253\pi}{5000}.
 \end{split}                                                       \tag{31}
\]
These bounds apply to the entire horizontal private intervals,
not just their endpoints. They use the actual alias penalties;
no fixed-height remainder is treated as undamped.

## 5. Completion of the original finite cap

The exact source decomposition and physical-row estimates in
[the upper-target extension, Theorem 2](research_mixed_cap_upper_target_extension.md)
apply at \(a=1/2\). They use precisely (3), the real cuts
\(.27,.49\), the heights \(-.055,.04\), and any intermediate
private main height, hence \(h_+\). In particular:

* Every compact physical tail reduces to the same two real cut
  rates, retaining whole coherent endpoint coefficients and
  zero-safe incoming products. This includes all rows revived
  off the incoming physical grid.
* The true private ends have their separate rate at most \(3/4\).
  They do not use a compact endpoint packet at zero or one.
* The exact cotangent-residue formula has constant-mode density
  \(+N\). It retains both horizontal aliases, both whole vertical
  alias sides, and both unweighted connectors to the main height.

The proof of that theorem is a sum of estimates for these actual
source groups. We use those estimates before summing, rather than
subtracting a term from a bound on the signed whole cap.
Equations (20), (24), and (25) pay the physical tails and real
cuts. Equation (31) pays both horizontal aliases.
Private vertical convexity on (2) bounds each sign-half vertical
alias by its real and horizontal endpoints, after retaining its
linear penalty. The same convexity bounds each unweighted main
connector by its real cut value and its endpoint on the shifted
horizontal line. The latter has a strict horizontal gap from
the critical point. Thus every one of these currents is paid.

Use the original half-grid cuts tending to \(.27,.49\).
Their \(O(N^{-1})\) shifts preserve all strict inequalities.
Choose the single finite-source tolerance only after the
positive gaps are fixed. There are constants \(\delta>0,C,B\)
such that the sum of all noncentral source groups has modulus
at most \(CN^B e^{N(M_{\rm half}-\delta)}\), along both parities.
Even-level zeros of \(p_j(-1)\) are retained; the proof does
not delete the nonzero upper rows at odd levels.

Let \(e(a,w)\) be the local holomorphic continuation of \(e_+\)
solving \(\Psi_e=0\), and define
\[
 \begin{split}
 \mathcal T_{\rm half}(a,w)&=\Psi(e(a,w),a,w),\\
 \mathcal B_{\rm half}(a,w)
  &=\frac{\sqrt{2\pi}}{\sqrt{-\Psi_{ee}(e(a,w),a,w)}}
       \mathcal A(e(a,w),w)
              \sqrt{\frac{\sin\pi(e(a,w)+a)}{\sin\pi a}} .
 \end{split}                                                       \tag{32}
\]
Here \(\mathcal A\) is the original nonzero endpoint symbol.
Every square root retains its original continuation; the
Gaussian root has positive real part at the base point.

**Theorem.** On a fixed complex neighborhood of
\((a,w)=(1/2,-2)\), the entire original cap satisfies
\[
 U_{0,N}(w,e^{-2\pi ia})
   =N^{-1}\mathcal B_{\rm half}(a,w)
        e^{N\mathcal T_{\rm half}(a,w)}
                   (1+O_{\rm hol}(N^{-1})),\qquad
                         \mathcal B_{\rm half}\ne0.              \tag{33}
\]
The normalized relative error and all its fixed joint
derivatives are \(O(N^{-1})\) on smaller neighborhoods.
For the original signed ordinary derivative of order \(k\)
at the complete color, the leading factor in (33) is multiplied
by
\[
                    N^k\left(\frac{\tan\pi u_+}{4\pi}\right)^k
                                                                    \tag{34}
\]
at the base point; this factor is nonzero.

The retained row has power \(N^{-3/2}\). The exact density
\(+N\) and the private Gaussian width \(N^{-1/2}\) give \(N^{-1}\),
with precisely (32). The retained-integral theorem already
supplies its \(O(N^{-1})\) relative error. The just-proved
exponential errors complete the sum. For local continuation,
keep the base cuts and outer contours fixed. All bounded
current gaps persist by continuity; the physical-row gaps
persist by their zero-safe rate bounds and the original small
ordinary-color estimates, including the numerator rows revived
by a complex perturbation away from \(X=-1\).
Move only a small central portion through the continued critical
point and retain its short connectors in the paid outer portion.
Cauchy's formula gives the normalized derivative statement.
Formula (34) is the original endpoint color derivative after
critical stationarity.

There is a distinct, legitimate all-real-color upper conclusion
at \(a=1/2\). The angular estimate in the upper-target theorem
and the now proved profile comparisons imply, for some \(c>0\)
and every \(\tau>0\),
\[
 |U_{0,N}(-2\cos\theta,-1)|
       \le C_\tau N^{B_\tau}
          e^{N\{M_{\rm half}-c(1-\cos\theta)+\tau\}} .
                                                                    \tag{35}
\]
The separate \(3/4\) endpoint ceiling is absorbed using (25)
and \(1-\cos\theta\le2\). Fixed ordinary derivatives have the
same exponential upper bound with polynomial costs.
Equation (35) is an upper estimate, not an assertion of a
nonzero saddle expansion at remote real colors.

The whole conditional half-face packet can now be multiplied
by (33) in their common local source domain. Their combined
critical action still needs comparison with the actual selected
ordinary-next affine action, and continuation along the
remaining incoming real arc and its prescribed vertical join
requires its own source estimates. Neither conclusion follows
from the nonzero half-face packets alone.

