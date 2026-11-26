# The complete endpoint source on the new lower private side

Research deduction, 7 November 2026. The literal endpoint sum,
including every row revived at a complex private index, pays the
entire lower side at real part \(1/8\), from height zero to
\(-11/200\). The proof retains the marked outer factorial and the
endpoint carrier before taking an upper bound. It uses no endpoint
asymptotic on an unproved rectangle.

We also supply the missing revived-row comparison for a genuine
thin-strip endpoint packet over \([1/8,.27]\). Its unspecified
strip width is distinct from the explicit full-height side bound.
Neither conclusion pays the new horizontal private path.
No numerical evaluation or saved-source replay is used.

## 1. Exact source, branches, and uniform row bounds

Let \(E=1/8\), \(H=11/200\), \(r=e^{-2\pi i/N}\), and keep
the prescribed finite continuation
\[
 \mathcal C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)}.
 \tag{1}
\]
Here \(e_l\), \(G_N\), and \(S_l\) are the original Newton
polynomial, sine factorial, and physical sine factorial. The
private cap interpolation is exactly
\[
 \begin{split}
 \mathscr A_N(e,a,w)
 &=D_N(e)^{-1}\mathcal C_N(e,w)
                        \frac{\Pi_N(a+e)}{\Pi_N(a)},\\
 D_N(e)&=\exp\{\pi i[N(e-e^2)-e]/2\},\qquad
 \Pi_N(e)=D_N(e)G_N(Ne).
 \end{split}                                                    \tag{2}
\]
At physical \(e=j/N\), (2) is the complete row
\(H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j\).
The identities in
[the complex-index theorem, equation (18)](research_complete_boundary_complex_index.md)
also give
\[
 \mathscr A_N(e,a,w)=
 H_N(w,e^{2\pi ie})
       \frac{\Pi_N(a+e)}{\Pi_N(a)\Pi_N(e)}.
 \tag{3}
\]
Thus all boundary forcing of the finite endpoint polynomial is
retained. In particular no even-level high coefficient is deleted.

We first take
\[
 e=E-i\eta,\quad 0\le\eta\le H,\qquad
                  \frac12\le a\le\frac7{10}.
 \tag{4}
\]
All marked outer arguments in (2) are in regular strips.
The reciprocal in (1) uses the original reflected lower branch
when its real part is negative; its zeros remain.

For \(u=l/N\), the zero-safe factorial bounds and
[the Newton color tube theorem, equations (4)--(7)](research_mixed_newton_color_tubes.md)
bound the \(l\)-th term of (1), at every real color, with rate
\[
 R(e,u)=V_\theta(u)-J(u)
                   -\Re J_{\rm side}(e-u)+\pi\eta u,
 \tag{5}
\]
where
\[
 V_\theta(u)\le V_0(u)=-2J(1/2-u)-2J(u)\quad(0\le u\le1/2),
 \qquad V_\theta(u)\le0\quad(1/2\le u\le1).
 \tag{6}
\]
Only the second, weaker bound is used above the half index.
These estimates include ordinary derivatives and numerator zeros,
with polynomial factors. A small fixed complex color neighborhood
adds an arbitrarily small prescribed exponential tolerance.

The outer marked factor in (2) has rate
\[
 T(a,e)=\Re\{J(a+e)-J(a)-i\pi ae\}.
 \tag{7}
\]
This keeps the \(D_N^{-1}\) carrier. Its order-one factors cost
only a bounded factor on (4). We will bound \(R+T\) before
summing any of the \(N\) terms.

## 2. The incoming angle and its marked height term

The maximum of (7) on the real incoming interval in (4) is at
\(a=1/2\). Indeed
\[
 \partial_aT
 =\log\frac{|1-\rho e^{-2\pi i(a+E)}|}
                    {|1-e^{-2\pi ia}|},\qquad
                         \rho=e^{-2\pi\eta}\le1.
 \tag{8}
\]
The squared numerator is convex in \(\rho\in[0,1]\).
At its two endpoints its values are \(1\) and
\(4\sin^2\pi(a+E)\), both at most \(4\sin^2\pi a\).
Here \(a\ge1/2\), \(a+E<1\), and \(2\sin\pi a>1\).
Thus (8) is nonpositive.

At the half face,
\[
 T(1/2,E-i\eta)
   =\Re J(5/8-i\eta)-\frac{\pi\eta}{2}
   \le J(5/8)+\frac{\pi\eta^2}{4}-\frac{\pi\eta}{2}.
 \tag{9}
\]
To prove the inequality, the absolute argument of
\(\sin\pi(5/8-is)\) is
\(\arctan((\sqrt2-1)\tanh\pi s)\le\pi s/2\).
Integrate from zero to \(\eta\).
Also \(J(5/8)=-J(3/8)<(\log2)/8<7/80\).
The negative linear term in (9) is essential.

## 3. Auxiliary indices below the real private coordinate

For \(0\le u\le E\), sine concavity gives
\(-J(s)\le s(1-\log(6s))\) for \(0\le s\le E\).
Moreover \(-2J(1/2-u)\le2u\log2\). The real-row bound is
therefore
\[
 B(E,u)\le2u\log2+3u(1-\log(6u))
                           +(E-u)(1-\log(6(E-u))).
 \tag{10}
\]
Use the concave tangent of the first two terms at \(u=E\).
With \(d=E-u\), the additional expression has maximum
\[
 \max_{d\ge0}d\{1-\log(6d)+3\log(6E)-2\log2\}=9E^3 .
 \tag{11}
\]
Consequently
\[
 B(E,u)\le2E\log2+3E(1-\log(6E))+9E^3
 <\frac7{40}+\frac{39}{80}+\frac9{512}
 <\frac{681}{1000}.
 \tag{12}
\]
We used \(\log2<7/10\) and \(\log(4/3)<3/10\);
the latter follows already from
\(1+3/10+(3/10)^2/2>4/3\).

Moving the positive argument \(E-u\) to \(E-u-i\eta\)
increases its reciprocal rate by at most \(\pi\eta/2\),
since the sine argument has absolute argument at most \(\pi/2\).
The endpoint carrier is \(\pi\eta u\le\pi\eta E\).
The former debit cancels the negative linear term in (9), leaving
\[
 R(e,u)+T(a,e)
 <\frac{681}{1000}+\frac7{80}
                      +\frac{\pi\eta}{8}+\frac{\pi\eta^2}{4}
 \le\frac{443791}{560000}<\frac45 .
 \tag{13}
\]
Here and below \(\pi\eta\le121/700\) and
\(\pi\eta^2/4\le1331/560000\).
All assertions extend to \(u=0,E\) by continuity.

## 4. Every revived row between \(E\) and \(1/2\)

For real \(u\ge E\), write
\[
 \mathcal H(E,u)=-2J(1/2-u)-3J(u)+J(u-E).
 \tag{14}
\]
With \(c=\cos(\pi E)\), \(d_0=\sin(\pi E)\), and
\(z=\cot\pi u\), its derivative obeys
\[
 \exp\{\partial_u\mathcal H(E,u)\}
       =z^2(c-d_0z)
       \le\frac{4c^3}{27d_0^2}<\frac45.
 \tag{15}
\]
The last strict inequality is exact: the half-angle values reduce
it to \(6007\sqrt2<8498\), and
\(8498^2-2\cdot6007^2=47906>0\).
Thus for \(d=u-E\ge0\),
\[
       \mathcal H(E,E+d)\le\mathcal H(E,E)-d\log(5/4).
 \tag{16}
\]

The lower-side reciprocal has the exact real-part identity
\[
 \begin{split}
 -\Re J_-(-d-i\eta)&=J(d)+\frac{\pi\eta}{2}+K_\eta(d),\\
 K_\eta(d)&=\frac12\int_0^d
        \log\left(1+\frac{\sinh^2(\pi\eta)}{\sin^2\pi s}\right)ds .
 \end{split}                                                    \tag{17}
\]
To check it, differentiate in \(d\) using the original lower
logarithmic lift, and use
\(\Re J(-i\eta)=-\pi\eta/2\) at \(d=0\).
Equivalently
\(J_-(-d-i\eta)=-J(d+i\eta)+i\pi d-\pi\eta\).
Since \(\Re J(1/2+i\eta)=0\), (17) gives
\[
               0\le K_\eta(d)\le K_\eta(1/2)
                          =\frac{\pi\eta}{2}\quad(0\le d\le1/2).
 \tag{18}
\]
No uniform \(\pi\eta/2\) estimate is applied to the reflected
reciprocal alone: its extra \(K_\eta\) remains.

The shared real base in (14) and (9) satisfies
\[
 \mathcal H(E,E)+J(5/8)
       =-3\{J(1/8)+J(3/8)\}<\frac{721}{1000}.
 \tag{19}
\]
Here is a purely analytic witness. The sum of the two primitives is
\(\int_0^{1/8}\log\tan(\pi s)\,ds\). From
\(\tan x\ge x+x^3/3\) and \(\log(1+x)\ge x-x^2/2\),
\[
 -3\{J(1/8)+J(3/8)\}
 \le\frac38(1+\log(8/\pi))-\frac{\pi^2}{1536}
                                      +\frac{\pi^4}{983040}.
 \tag{20}
\]
The inequalities \(\pi>157/50\) and
\[
 e^{15/16}>
 \sum_{k=0}^{5}\frac{(15/16)^k}{k!}
 =\frac{321179295}{125829120}>\frac{400}{157}
 \tag{21}
\]
give \(\log(8/\pi)<15/16\); the last cross-product difference
is \(93501315>0\). Using \(\pi>25/8\) and \(\pi<16/5\),
the right side of (20) is less than
\[
 \frac{93}{128}-\frac1{160}+\frac1{9375}
       =\frac{461}{640}+\frac1{9375}<\frac{721}{1000}.
 \tag{22}
\]

Combine (9), (16), and (17), retaining the full carrier
\(\pi\eta u=\pi\eta(E+d)\). It gives
\[
 R(e,E+d)+T(a,e)
 <\frac{721}{1000}+\pi\eta E+\frac{\pi\eta^2}{4}
                +K_\eta(d)-d\{\log(5/4)-\pi\eta\}.
 \tag{23}
\]
The last coefficient is positive, since
\(\log(5/4)>2/9>121/700\ge\pi\eta\).
By (18), every row in this block therefore has rate less than
\[
 \frac{721}{1000}+\frac{121}{5600}
             +\frac{1331}{560000}+\frac{121}{1400}
 =\frac{465591}{560000}<\frac56 .
 \tag{24}
\]
The reserve below \(5/6\) is exactly \(3227/1680000\).
In particular the carrier term \(\pi\eta d\) has not been omitted.

## 5. The upper auxiliary half and finite-level conclusion

For \(1/2\le u\le1\), use only \(V_\theta(u)\le0\).
Put \(d=u-E\in[3/8,7/8]\).
The same lower continuation gives
\[
 -\Re J_-(-d-i\eta)
       =\Re J(d+i\eta)+\pi\eta
       \le J(d)+3\pi\eta/2.
 \tag{25}
\]
The sine argument bound proves the last step, including \(d>1/2\).
On this interval
\[
                  J(u-E)-J(u)\le-J(E)<1/6.
 \tag{26}
\]
For example differentiate \(J(v)-J(v+E)\) on
\(3/8\le v\le7/8\): its only interior turning point is a
minimum, and its endpoint values are \(J(3/8)<0\) and
\(-J(E)>0\). The bound \(\max(-J)<1/6\) is the original
sine-concavity estimate. Combining (9), (25), (26), and the
carrier \(\pi\eta u\le\pi\eta\) proves
\[
 R(e,u)+T(a,e)
 \le\frac16+\frac7{80}+2\pi\eta+\frac{\pi\eta^2}{4}
 \le\frac{1011793}{1680000}<\frac23.
 \tag{27}
\]
Thus no upper row, including \(l=N-1\), uses the negative
complete-color entropy in place of the all-real bound.

**Theorem 1.** For every \(\tau>0\), the complete source satisfies
\[
 |\partial_w^k\mathscr A_N(E-i\eta,a,w)|
 \le C_{\tau,k}N^{B_{\tau,k}}e^{N(5/6+\tau)}
 \tag{28}
\]
uniformly on (4), at every real ordinary color, both level parities,
and every fixed ordinary derivative order. The same assertion holds
on a sufficiently small fixed complex-color neighborhood, with
arbitrarily small additional tolerance and smaller neighborhoods
for derivatives.

Indeed (13), (24), and (27) bound every literal summand of (1)
after multiplication by its marked factor. The zero-safe uniform
factorial and Newton bounds include all true endpoints and reciprocal
zeros. Summing at most \(N\) rows costs only a polynomial. The Newton
color-tube bounds give the stated ordinary-color scope directly.

The real upper rate in (5) is uniformly continuous on the full
compact row set, including \(e-u=0\) and its lower cut. The strict
reserve in (24) therefore also supplies a fixed real neighborhood
of \(E\), and small neighborhoods of the outer endpoints, before
finite half-grid cuts are used. In particular an \(O(N^{-1})\)
change of \(E\) is absorbed inside that reserve, not into an
unproved endpoint packet. Formula (28), together with the explicit
regular factor (7), is also an actual global bound for
\(\mathcal C_N(e,w)\) on this lower-side neighborhood.

## 6. The selected source and cancellation of the artificial side

Keep the original conditional indices
\[
 L_N=\lfloor N/16\rfloor+1,\qquad
 K_N(a)=\lceil N(1-a-\varepsilon)\rceil
 \tag{29}
\]
and their literal middle polynomial \(C_{1,N}^{\rm mid}\).
Its positive disk bound is \(A(1-a)+7/15\le91/120\), and
its degree in \(Y\) is strictly less than \(N/2\).
Thus (28) times this polynomial has selected-radius rate
\[
             \frac56+\frac{91}{120}+\frac{\pi}{100}.
 \tag{30}
\]
The proof of
[the allocated-action theorem, Theorem 2](research_mixed_next_allocated_action_floor.md)
uses its prefix only through the selected-radius ceiling
\(25/16+\pi/50\). That theorem has its original raw gap \(1/200\),
retaining both \(d_N(Y)Y^{-N}\) alternatives, the whole third
conditional factor and its outgoing halfweight. The improvement
of (30) over that ceiling is
\[
        \frac{\pi}{100}-\frac7{240}>\frac1{480},
 \qquad \frac1{200}+\frac1{480}=\frac{17}{2400}>\frac1{150}.
 \tag{31}
\]
Consequently the complete lower-side product on the ordinary-next
canonical family has raw gap \(1/150\) against the same affine
target \(\Lambda_{123}\). A finite gap \(1/300\) is available
after the half-grid changes, common tolerances and polynomial costs.
All-real colors and local complex colors have the scope of (28).
At the actual outgoing reference, the existing nonzero factorial
weight and fixed-contour Cauchy argument give every fixed normalized
mixed derivative with, for example, gap \(1/600\). On the full
independent outgoing plateau the statement remains weighted;
no zero of \(d_N\) is divided out.

Here is the exact cut surgery. Decrease the permitted fixed wall
collar so \(0<\delta_*<1/100\), and put
\[
 \begin{split}
 J_-&=\lfloor N/8\rfloor+1,\quad
 J_c=\lceil27N/100\rceil,\quad
 J_+=\lceil N(1-a-\delta_*)\rceil,\\
 \ell&=(J_--1/2)/N,\quad c=(J_c-1/2)/N,\quad
 b=(J_+-1/2)/N .
 \end{split}                                                    \tag{32}
\]
For large \(N\), \(\ell<c<b\), and \(a+b<1-3\delta_*/4\).
The source (3) is holomorphic on these fixed real strips at
all finite heights. On two rectangles with identical upper and
lower heights and respective real intervals \([\ell,c]\),
\([c,b]\), their exact integrals
\[
       \frac1{2\pi i}\oint
             \mathscr A_N(e,a,w)\,\pi N\cot(\pi Ne)\,de
 \tag{33}
\]
add to the integral on \([\ell,b]\). The entire shared side at
\(c\) cancels pointwise with opposite orientations. The residue
sum is exactly the original rows \(J_-\le j<J_+\); no constant
mode or alias was dropped. Multiplication by the conditional and
selected factors, which are independent of \(e\), preserves this
identity. The newly exposed negative lower side
\(\ell-i[0,11/200]\) is paid by (28)--(31), also after splitting
the cotangent kernel into its constant and decaying parts.

If the two main heights differ, their connecting segment at \(c\)
must remain. Identical-height surgery is what eliminates it.
Every jump of the integer cuts is retained pointwise in \(a\);
outside-variable derivatives keep the base cuts fixed.

## 7. A genuine thin-strip endpoint packet down to \(1/8\)

The following additionally repairs the source range needed for
local continuation; it supplies no specified height as large as \(H\).
Let \(I=[1/8,27/100]\). For real \(x\in I\) and revived
indices \(x\le u\le1/2\), the derivative of the real upper rate
is negative if
\[
 z^3-\cos(\pi x)z+\sin(\pi x)>0,\qquad z=\tan\pi u .
 \tag{34}
\]
Put \(c_x=\cos\pi x,d_x=\sin\pi x\).
For all \(x\ge1/8\) below one half,
\(d_x>3/8\) and \(c_x<15/16\), by the elementary half-angle
values at \(\pi/8\). The global minimum for \(z\ge0\) in
(34) is positive because
\[
 27d_x^2>\frac{243}{64}>
                   \frac{13500}{4096}>4c_x^3 .
 \tag{35}
\]
Thus every revived row up to the half index is bounded by the
real endpoint at \(u=x\), which the original real-index endpoint
proof places strictly below \(\lambda(x)\).

Above the half index the all-real bound is at most \(1/6\).
Meanwhile that original endpoint comparison gives
\(\lambda(x)>-2J(1/2-x)-3J(x)>18/65\).
For the last inequality, \(J\) is convex on \([1/8,3/10]\).
The bound \(2\sin(\pi s)\le2\pi s\), together with
\(\pi/4<1\), gives \(J(1/8)<-1/8\). Also
\[
 -J(3/10)=\int_{3/10}^{1/2}\log(2\sin\pi s)\,ds
       >\frac15\log\frac85>\frac6{65},
\]
since \(\sin(3\pi/10)=(1+\sqrt5)/4>4/5\) and
\(\log(8/5)>2[(8/5)-1]/[(8/5)+1]=6/13\).
Thus \(J(x)<-6/65\) on \(I\).
The upper revived gap is therefore at least \(43/390\).

The original physical endpoint proof supplies regular interior cuts,
positive gaps at both real ends and all vertical currents, and
positive upper/lower alias gaps, uniformly on this compact \(I\).
Combine those gaps with (34)--(35) and \(43/390\), retaining their
positive compact minimum \(\gamma\).
The reflected reciprocal exponent changes by at most
\(C\eta(1+|\log\eta|)\), as proved in
[the complex-index theorem, Section 4](research_complete_boundary_complex_index.md).
The other regular phases and their continued critical points are
uniformly continuous. Choose one fixed \(\eta_0>0\) so that
these changes, including the continued action, spend less than
\(\gamma/4\). All original finite rows and all currents then
retain strict gaps. The unchanged exact contour and Gaussian proof
gives
\[
 \mathcal C_N(e,w)=N^{-3/2}\mathcal A(e,w)e^{NS(e,w)}
                      (1+O_{\rm hol}(N^{-1})),\qquad\mathcal A\ne0,
 \tag{36}
\]
on a fixed neighborhood of \(I\times\{-2\}\), in particular
for \(x\in I,-\eta_0\le\Im e\le0\).
Every fixed joint derivative follows on smaller neighborhoods.
This is an estimate of the specified whole finite sum, including its
revived rows and both parities, rather than just its holomorphy.

The value of \(\eta_0\) is not asserted to reach \(11/200\).
The full-height conclusion (28) applies to the lower side near
\(\Re e=1/8\); (36) applies to the thin strip. Neither bounds
the complete lowered horizontal segment from that side to \(E_c\).
That bridge, the remaining upper sides and aliases, and the initial
incoming \(a\)-vertical join remain separate source obligations.
