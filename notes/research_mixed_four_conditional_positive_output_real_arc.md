# The complete type-four conditional sum at a small positive outgoing height

Private written proof, 11 November 2026. The outgoing height used by
the second Fourier term is positive. Earlier real-arc estimates assumed
a nonpositive outgoing height, so those estimates cannot simply be
applied to this term. Here the outgoing height may range from zero
to \(1/100\). The complete conditional sum is bounded on the entire
incoming real interval \([1/2,7/8]\).

The proof moves a central index interval which stops before the first
numerator zero. Every later physical row is estimated on the original
real index interval. In particular no assertion about a continued
critical-height contour beyond that zero is needed.

## 1. The finite sum and its comparison rates

Put
\[
 q_N=e^{-2\pi i/N},\qquad P_j=(q_N;q_N)_j,\qquad
 p_j(Z)=(q_NZ;q_N)_j ,
\]
and retain the original polynomial
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                 \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{1}
\]
The parameter set in this note is
\[
 \frac12\le a\le\frac78,\qquad b=z+id,\qquad
 \frac{11}{50}\le z\le\frac9{20},\qquad
 0\le d\le\frac1{100},\qquad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
 \tag{2}
\]
All quantities are fixed before \(N\) tends to infinity. Write
\[
 R=|Y|=e^{2\pi d},\qquad \delta=1-a,\qquad \ell=\frac2{25}.
\]
The elementary bound \(e^t\le(1-t)^{-1}\), together with
\(\pi<22/7\), gives
\[
                    1\le R<\frac{175}{164}<\frac{43}{40}.
 \tag{3}
\]

Let \(g\) be the original primitive, with
\(g'(w)=\operatorname{Log}(1-e^{-2\pi iw})\) on \(0<\Re w<1\),
and put
\[
 Q(s;a,b)=g(a+s)+g(b+s)-3g(s)-g(a)-g(b)+2\pi ias.
 \tag{4}
\]
The original simple upper-root branch defines
\[
 Q_s(s_*;a,b)=0,\qquad
 \Theta(a,b)=Q(s_*;a,b).
 \tag{5}
\]
Its existence on (2), its original logarithmic lift, and the
quantitative bounds needed below are proved in Section 2.

Write \(J(t)=\Re g(t)\) on the real interval, and extend this real
function continuously and periodically. Thus
\[
 J'(t)=\log|2\sin\pi t|,\qquad
 J(0)=J(1/2)=J(1)=0,\qquad J(1-t)=-J(t).
\]
Define the continuous physical-row rates
\[
 \begin{split}
 I_a(t)&=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv,\\
 I_b(t)&=\int_0^t\log|1-Ye^{-2\pi iv}|\,dv,\\
 E_a(t;b)&=I_a(t)+I_b(t)-3J(t),\qquad 0\le t\le1,\\
 L(b)&=E_{1/2}(\ell;b).
 \end{split}
 \tag{6}
\]
These rates include their integrated logarithmic zeros. The incoming
carrier in (1) has modulus one because \(a\) is real.

**Theorem 1.** For every \(\tau>0\), constants \(C_\tau,A_\tau\)
independent of the parameters in (2) and of \(N\) give
\[
 |C_{1,N}(X,Y)|
 \le C_\tau N^{A_\tau}
       \exp N\{\max(\Re\Theta(a,b),L(b))+\tau\}.
 \tag{7}
\]
The estimate includes both level parities and every index in (1).
For any prescribed \(B>0\), the two horizontal sampling corrections
in the proof may be bounded at rate
\(\Re\Theta(a,b)-B+\tau\), by a sufficiently tall fixed rectangle.

This is an upper bound for the complete conditional polynomial.
It neither supplies a nonzero leading coefficient for that polynomial
nor incorporates an adjoining cap, a Fourier weight, or a following
conditional factor.

## 2. The original critical point stays in a fixed regular region

For (2), \(\Im Y<0\) and \(\Re Y<1\). Indeed
\(\cos(2\pi z)<1/5\) on the specified interval, so
\(\Re Y<43/200\). The incoming coordinate is on the upper unit
semicircle, including \(X=-1\) and excluding \(X=1\).
The [unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md)
therefore applies with no extension of its parameter domain.
It gives the unique simple upper root
\[
 v(v-X)(v-Y)=X(v-1)^3,\qquad
 s_*=\frac{\operatorname{Log}v}{2\pi i}=u_*+ih_*,
 \qquad 0<u_*<\delta,
 \tag{8}
\]
with \(Q_s(s_*;a,b)=0\) on the original, unsquared logarithmic lift.

Set \(U=e^{2\pi h_*}=|v|^{-1}\). We claim
\[
       \frac12<U<4,\qquad
       \ell<u_*<\delta,\qquad
       |h_*|<H_0:=\frac{\log4}{2\pi}.
 \tag{9}
\]
For \(V\in(0,2\pi)\), write
\(\alpha_r(V)=\operatorname{Arg}(1-re^{-iV})\), using the
original continuous strip argument. The imaginary critical equation is
\[
 \alpha_U(2\pi(a+u_*))
 +\alpha_{RU}(2\pi(z+u_*))
 -3\alpha_U(2\pi u_*)+2\pi a=0.
 \tag{10}
\]
If \(U\le1/2\), each incoming or own argument has modulus at
most \(\pi/6\). The outgoing argument has modulus at most
\(\arcsin(43/80)<\pi/5\). For the last strict bound,
\(\sin(\pi/5)>7/12>43/80\); its first inequality follows by
squaring \(\sin^2(\pi/5)=(5-\sqrt5)/8\).
Consequently the left side of (10) is at least
\(\pi-4\pi/6-\pi/5=2\pi/15>0\), a contradiction.

If \(U\ge4\), the modulus of the exponential critical equation
instead satisfies
\[
 |e^{Q_s}|
 \le\frac{(1+U)(1+(43/40)U)}{(U-1)^3}<1.
 \tag{11}
\]
To check the strict inequality, put \(U=4+t\), \(t\ge0\).
The denominator minus the numerator in (11) is
\[
 t^3+\frac{317}{40}t^2+\frac{653}{40}t+\frac12>0.
 \tag{12}
\]
This contradicts \(Q_s=0\). These arguments prove the radius and
height assertions in (9).

Here is the lower real-part bound, with its dependence on the
outgoing radius made explicit. Suppose \(0<u_*\le2/25\).
For \(U\ge8/5\), put \(\beta=\arcsin(U^{-1})<\pi/4\).
The exact argument identity
\[
 \alpha_U(V)=\pi-V+\operatorname{Arg}(1-U^{-1}e^{iV}),
 \qquad
 |\operatorname{Arg}(1-U^{-1}e^{iV})|\le\beta
 \tag{13}
\]
applies to the incoming and own factors. For every positive
outgoing radius,
\(\alpha_{RU}(2\pi(z+u_*))\le14\pi/25\).
Substitution in (10) bounds its left side above by
\[
 -2\pi+4\pi u_*+\frac{14\pi}{25}+4\beta
 <-\frac{3\pi}{25}.
 \tag{14}
\]
This is impossible.

For \(1/2<U<8/5\), put \(w_0=(U-1)^2\) and
\[
 A=|1-Ue^{-2\pi i(a+u_*)}|^2,\quad
 B=|1-RUe^{-2\pi i(z+u_*)}|^2,\quad
 D=|1-Ue^{-2\pi iu_*}|^2.
\]
The estimates in Section 4 of the
[fixed lower-cut proof](research_mixed_four_unit_arc_fixed_lower_cut.md)
give
\[
 A>w_0+\frac U{16},\qquad D<w_0+\frac U4,\qquad
 B>1+\frac{U^2}{4}-\frac U5,\qquad B>\frac{24}{25}.
 \tag{15}
\]
For precision, the first two use only \(a\le7/8\) and
\(u_*\le2/25\). For the last two,
\(\cos(2\pi(z+u_*))<1/5\), so
\[
 B>1+(RU)^2-\frac25RU.
\]
This quadratic is increasing for \(RU>1/5\), and here
\(RU\ge U>U/2>1/4\). Thus the same estimates hold when \(R>1\);
no upper-radius hypothesis was used in these two comparisons.

To finish the contradiction without a critical-root evaluation,
if \(1/2\le U\le5/4\), (15) gives
\[
 D<\frac38,\qquad A>\frac{63}{1024},\qquad
 AB>\frac{189}{3200}>\frac{27}{512}>D^3.
 \tag{16}
\]
If \(5/4\le U\le8/5\), then \(0\le w_0<2/5\) and
\[
 A>w_0+\frac5{64},\qquad D<w_0+\frac25,\qquad B>\frac98.
 \tag{17}
\]
The concave polynomial
\((9/8)(w+5/64)-(w+2/5)^3\) is positive at both endpoints
of \([0,2/5]\): its endpoint values are
\(45/512-8/125\) and \(1377/2560-64/125\).
It is therefore positive throughout that interval.
Again \(AB>D^3\), contrary to \(|e^{Q_s}|^2=1\).
This proves (9).

The parameter set (2) is compact, and the simple original root
is continuous there. Its strict distances from \(\ell\), from
\(\delta\), and from the height boundaries in (9) consequently
have positive minima.

## 3. Concavity before the incoming numerator zero

For \(s=u+i\sigma\), define
\[
 \mathcal C(s)=\Re\cot(\pi s)
   =\frac{\sin(2\pi u)}
          {\cosh(2\pi\sigma)-\cos(2\pi u)}.
 \tag{18}
\]
On
\[
                \ell\le u<\delta,\qquad |\sigma|\le H_0,
 \tag{19}
\]
one has
\[
 -\Re Q_{ss}
 =\pi\{3\mathcal C(s)-\mathcal C(a+s)-\mathcal C(b+s)\}>0.
 \tag{20}
\]
The incoming term has \(\mathcal C(a+s)<0\), since
\(1/2<a+u<1\), and \(\mathcal C(s)>0\), since \(0<u<1/2\).
Thus only the case \(\mathcal C(b+s)>0\) needs a quantitative
comparison. It implies \(z+u<1/2\), hence \(u<7/25\), and
\[
            \mathcal C(b+s)\le\cot(3\pi/10)<\frac34.
 \tag{21}
\]
The last inequality follows from
\(\tan^2(\pi/5)=5-2\sqrt5<9/16\).

Also \(\cosh(2\pi\sigma)\le\cosh(\log4)=17/8\).
On \([2/25,1/8]\),
\(\sin(2\pi u)>12/25\) and
\(\cos(2\pi u)>7/10\). Therefore
\[
                    \mathcal C(s)>\frac{32}{95}.
 \tag{22}
\]
On \([1/8,7/25]\),
\(\sin(2\pi u)>7/10\) and
\(\cos(2\pi u)>-1/5\), giving
\[
                    \mathcal C(s)>\frac{28}{93}.
 \tag{23}
\]
The elementary sine bound at \(2/25\) is written in Section 2
of the [earlier intermediate-arc proof](research_mixed_four_conditional_intermediate_real_source.md);
the other endpoints follow from \(\sqrt2/2>7/10\) and
\(\sin(3\pi/50)<1/5\).
Both \(3(32/95)\) and \(3(28/93)\) exceed \(3/4\).
This proves (20). On every compact subrectangle strictly before
the incoming zero the positive lower bound is uniform.

Consequently the real restriction at the critical height is
strictly concave and has its unique maximum at \(u_*\).
At a fixed real index, the real phase is strictly convex in
the height. These are the two facts used in moving the central
integral; neither follows merely from uniqueness of an algebraic root.

## 4. The physical rows outside the central interval

We first record sharper elementary constants which allow a
positive outgoing height. The sine upper bound and \(\pi<22/7\)
give
\[
 J(\ell)\le\ell\{\log(2\pi\ell)-1\}<-\frac2{15}.
 \tag{24}
\]
Indeed \(2\pi\ell<88/175\), and
\[
 \log(175/88)>
 \frac{174}{263}+\frac23\left(\frac{87}{263}\right)^3
 >\frac23 .
 \tag{25}
\]
The first inequality is the positive \(\operatorname{artanh}\)
series. For the second, the deficit of \(174/263\) from \(2/3\)
is \(4/789\), smaller than the displayed cubic term because
\(87^3>2\cdot263^2\).
Furthermore,
\[
 I_{1/2}(\ell)=\int_0^\ell\log(2\cos\pi v)\,dv>\frac4{125}.
 \tag{26}
\]
Here \(\cos(\pi v)>3/4\) and
\(\log(3/2)>2/5\), as in the original real-row proof.

For \(0\le t\le\ell\), one has
\(|1-Ye^{-2\pi it}|>1\): the angle \(z+t\) lies in
\([11/50,53/100]\), its cosine is less than \(1/5\),
and \(R\ge1\). In particular \(I_b(\ell)>0\), so
\[
                              L(b)>\frac{54}{125}.
 \tag{27}
\]
The derivative of \(E_{1/2}(t;b)\) is positive on \((0,\ell]\).
For example its exponential is
\[
 \frac{2\cos(\pi t)|1-Ye^{-2\pi it}|}{(2\sin\pi t)^3}>1,
 \tag{28}
\]
using \(2\cos(\pi t)>3/2\) and \(2\sin(\pi t)<3/5\).

For every real \(1/2\le a\le1\) and \(0\le t\le1/2\),
\[
                         I_a(t)\le I_{1/2}(t).
 \tag{29}
\]
At fixed \(t>0\), differentiation in \(a\) gives
\(\log|\sin\pi(a+t)/\sin\pi a|\). Its sign changes only
from negative to positive at \(a=1-t/2\), with its integrable
numerator zero included by integration. The maximum is therefore
at an endpoint. Those endpoint values are
\(I_{1/2}(t)=-J(1/2-t)\ge0\) and \(I_1(t)=J(t)\le0\).
Equations (28)--(29) bound every low row \(0\le t\le\ell\)
by \(L(b)\).

For the other rows use the entropy identity
\[
 I_a(t)=J(\delta)+J(t-\delta)\le J(t),
                       \qquad \delta\le t\le1.
 \tag{30}
\]
For completeness, \(J(t)-J(\delta)-J(t-\delta)\) vanishes
at \(t=\delta,1\). Its derivative is positive up to
\((1+\delta)/2\) and negative afterwards, proving (30)
on the whole stated interval.

For \(\ell\le t\le1/2\), (3) gives
\[
 \begin{split}
 E_1(t;b)-L(b)
 &\le (t-\ell)\log(1+R)-2J(t)
                  +3J(\ell)-I_{1/2}(\ell)\\
 &< (t-\ell)\log2-2J(t)
       +\frac{63}{4000}+3J(\ell)-I_{1/2}(\ell).
 \end{split}
 \tag{31}
\]
Indeed \(\log((1+R)/2)<\log(83/80)<3/80\) and
\(t-\ell\le21/50\).
The maximum of \(t\log2-2J(t)\) on this interval is at
\(t=1/4\). Use the original analytic bound
\[
 b_2:=-4J(1/4)<\frac7{12},\qquad \log2<\frac7{10},
\]
recorded in the [complete-column theorem](research_mixed_symmetric_closing_complete_column_norm.md),
Sections 1 and 5. Together with (24)--(26), (31) gives
\[
 E_1(t;b)-L(b)
 <\frac{119}{1000}+\frac7{24}+\frac{63}{4000}
                         -\frac25-\frac4{125}
 =-\frac{67}{12000}<-\frac1{200}.
 \tag{32}
\]
Thus (30) pays every physical middle row
\(\delta\le t\le1/2\), including the moving incoming zero
at \(t=\delta\).

The high physical rows admit a separate simpler estimate.
Let \(G_d(r)=\Re g(r-id)\). The
[original radial reflection identity](research_mixed_right_tail_reflection.md)
gives
\[
 I_b(t)=2\pi dt+G_d(z+t)-G_d(z).
 \tag{33}
\]
The same primitive is odd and periodic, with
\(J(r)\le G_d(r)\le0\) for \(0\le r\le1/2\).
Also \(|J(r)|<1/6\): its negative minimum is at \(1/6\),
and \(2\sin\pi r\ge6r\) on \([0,1/6]\) gives
\(-J(1/6)<1/6\). Hence \(|G_d(r)|<1/6\) for every real \(r\).
For \(1/2\le t\le1\), use (30), \(J(t)\ge0\), and (33):
\[
 E_a(t;b)\le I_b(t)-2J(t)
 \le\frac{\pi}{50}+\frac13
 <\frac{208}{525}<\frac{54}{125}-\frac1{50}<L(b)-\frac1{50}.
 \tag{34}
\]
The reciprocal-radius term \(2\pi dt\) has been retained.
This is why an old zero-drift high-row estimate is unnecessary here.

Choose a fixed \(\eta>0\), small enough that
\[
 \ell<u_*<r(a):=\delta-\eta<\delta,\qquad
 E_a(t;b)<L(b)-\frac1{400}
                    \quad(\delta-\eta\le t\le\delta).
 \tag{35}
\]
The first choice is possible by the compact strict root bounds
in Section 2. The second follows from (32) at \(t=\delta\)
and uniform continuity of the integrated physical rates.
Both choices precede \(N\) and the final allowance \(\tau\).
All physical rows outside \([\ell,r(a)]\) are now bounded
by \(L(b)\), with a strict reserve at the right cut.

## 5. All weighted contour terms at the new outgoing height

Put \(F(u,\sigma)=\Re Q(u+i\sigma;a,b)\).
On the whole fixed-width strip \(\ell\le u\le r(a)\),
at arbitrary finite heights,
\[
 F_\sigma
 =-\alpha_{e^{2\pi\sigma}}(2\pi(a+u))
  -\alpha_{Re^{2\pi\sigma}}(2\pi(z+u))
  +3\alpha_{e^{2\pi\sigma}}(2\pi u)-2\pi a.
 \tag{36}
\]
For \(\sigma\ge0\), the original argument bounds give
\[
 F_\sigma
 \le2\pi-4\pi u+\max(2\pi(z+u)-\pi,0)
 \le\frac{87\pi}{50}.
 \tag{37}
\]
The first numerator has real argument in \((1/2,1)\),
and its radius is at least one. The outgoing estimate uses
the full positive-radius argument interval, so no sign of \(d\)
is assumed in (37).

For \(\sigma\le0\), the incoming argument is nonpositive
and the own argument nonnegative. If \(z+u\ge1/2\),
the outgoing argument is nonpositive as well. Otherwise put
\(V=2\pi(z+u)\in[3\pi/5,\pi)\). Its radius is at most
\(43/40\). At radius one,
\(\alpha_1(V)=\pi/2-V/2\le\pi/5\).
For \(1\le r\le43/40\),
\[
 \frac{\partial\alpha_r(V)}{\partial r}
 =\frac{\sin V}{1+r^2-2r\cos V}\le\frac12.
 \tag{38}
\]
Radii at most one give a smaller argument. Thus throughout
the lower half-strip the outgoing argument is at most
\[
             \frac{\pi}{5}+\frac3{80}<\frac{9\pi}{40}.
 \tag{39}
\]
Keeping this correction, rather than reusing the old unit-radius
bound, proves
\[
 F_\sigma\ge-\frac{9\pi}{40}-2\pi a
                     \ge-\frac{79\pi}{40}\qquad(\sigma\le0).
 \tag{40}
\]
Consequently
\[
 \begin{split}
 \partial_\sigma(F-2\pi\sigma)&\le-\frac{13\pi}{50}
                                      &&(\sigma\ge0),\\
 \partial_\sigma(F+2\pi\sigma)&\ge\frac{\pi}{40}
                                      &&(\sigma\le0).
 \end{split}
 \tag{41}
\]
Every weighted vertical half-side is therefore bounded by its
real-cut rate.

Let \(M\) be an upper bound for \(F(u,0)\) on the compact
parameter/core family, and \(m\) a lower bound for \(\Re\Theta\).
For a prescribed \(B>0\), choose a fixed \(T\) with
\[
 T>H_0+1,\qquad \frac{\pi T}{40}>M-m+B+1.
 \tag{42}
\]
Integrating (41) makes both horizontal weighted rates at
heights \(\pm T\) less than \(\Re\Theta-B-1\).
Only a sufficiently large fixed compact rectangle is used.

## 6. Exact finite assembly

Use the original negative-root factorial
\[
 \Pi_N(w)=G_N(Nw)
       \exp\!\left\{\frac{\pi i}{2}[N(w-w^2)-w]\right\},
 \qquad E_N(w)=\Pi_N(w)^{-1}\quad(0<\Re w<1).
 \tag{43}
\]
Here \(G_N\) is the canonical sine-factorial interpolation.
The [joint factorial chart](research_mixed_fourier_right_cap_joint_global_chart.md),
equations (2), (4), and (6), gives its exact recurrence and
\(\Pi_N(j/N)=P_j\). The literal central interpolant is
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(b+s)
                      E_N(a)E_N(b)E_N(s)^3.
 \tag{44}
\]
At \(s=j/N\), this equals the summand of (1).
All factorial arguments on the rectangle below have real parts
in fixed compact subsets of \((0,1)\); the incoming upper bound
is \(a+r(a)=1-\eta\). The
[canonical complex factorial expansion](exact_factorial_interpolation_and_complex_contours.md),
Section 4, therefore bounds (44) by
\(C_\tau N^{A_\tau}e^{N(F+\tau)}\), uniformly for
\(|\Im s|\le T\). Its normalization gives exactly the phase (4).

Choose the half-grid cuts
\[
 L_N=\lfloor N\ell\rfloor+1,\qquad
 M_N=\lceil Nr(a)\rceil,\qquad
 \ell_N=(L_N-\tfrac12)/N,\qquad
 r_N=(M_N-\tfrac12)/N .
 \tag{45}
\]
For all sufficiently large \(N\), they enclose \(u_*\),
remain before the incoming zero, and keep all strict strip
margins. The central sum has the exact split-cotangent identity
\[
 \begin{split}
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
 ={}&N\int_{\ell_N}^{r_N}T_N(s)\,ds\\
 &+\frac{N}{2i}
 \left\{\int_{\partial R^+_{\rm off}}T_N(s)(\cot\pi Ns+i)\,ds
       +\int_{\partial R^-_{\rm off}}T_N(s)(\cot\pi Ns-i)\,ds\right\}.
 \end{split}
 \tag{46}
\]
The upper and lower off-real boundaries retain their induced
orientations. This is the original residue identity used in
the [middle-source reduction](research_mixed_conditional_lower_output_middle_reduction.md),
Section 4. It has two horizontal corrections and four vertical
half-sides; its zero-mode coefficient is \(+N\).

Move the unweighted integral to height \(h_*\), retaining
its two endpoint joins. Section 3 bounds the horizontal rate
by \(\Re\Theta\). On each join, convexity in the height bounds
the rate by the larger of its real and critical-height endpoint
values. The real left rate is at most \(L(b)\); the right one
has the strict reserve in (35). These statements persist with
an arbitrarily small allowance at the displaced half-grid cuts.

On an exact half-grid vertical,
\[
             |\cot(\pi Ns)\pm i|
                \le2e^{-2\pi N|\Im s|}
 \tag{47}
\]
with the matching sign. Thus (41) bounds all four weighted
vertical halves by their real cuts. On the fixed horizontal
sides the same estimate holds with constant four for large \(N\);
(42) gives their prescribed loss.

The omitted low and later physical sums retain every index
\(0\le j<L_N\) and \(M_N\le j<N\), including \(0,N-1\).
The [zero-safe finite-product estimate](research_mixed_conditional_contour_allowance.md),
Section 2, applies directly to their original products.
For clarity, regularize each numerator logarithm by
\(\log(|1-e^{-2\pi i(a+t)}|+\varepsilon)\), and similarly
for \(b\), before taking its uniform upper Riemann sum.
The integral error tends uniformly to zero as
\(\varepsilon\downarrow0\); the only possible real zeros
are simple. The denominator estimate
\(\log|P_j|=NJ(j/N)+O(\log N)\) is uniform for every \(j<N\).
This yields the rates (6) for all literal rows, at both parities,
without dividing by a zero. Section 4 bounds their sums by
a polynomial times \(e^{N(L(b)+\tau)}\).

All contour lengths are fixed, their number is fixed, and there
are at most \(N\) physical rows. Assign one total tolerance
among the product estimates, the cut displacements, and the
factorial symbols. Equations (35), (41), and (46)--(47) prove
(7) and the additional horizontal-alias assertion.

## 7. What is available for the remaining first-coordinate connection

The [unit-circle multiplier theorem](research_mixed_four_conditional_unit_multiplier.md)
already applies to (2). It gives
\[
                       \Re\Theta(a,b)\le\Re\Theta(1/2,b).
 \tag{48}
\]
There is also a useful comparison with a fixed private contour
at \(a=1/2\). Suppose \(h_s\in[-.102,0]\), and choose
\(r_0<1/2\) sufficiently close to \(1/2\) that
\(\ell<u_*(1/2,b)<r_0\) throughout the compact family.
Then
\[
 \Re\Theta(1/2,b)
 \le \Re Q(u_*(1/2,b)+ih_s;1/2,b)
 \le\max_{\ell\le u\le r_0}\Re Q(u+ih_s;1/2,b).
 \tag{49}
\]
Indeed \(|h_s|<H_0\), because \(\log4>1\) and
\(2\pi(.102)<1\). At fixed \(u_*\), (20) makes the
height restriction convex. Its derivative vanishes at \(h_*\)
by the original critical equation, proving the first inequality.
The second is immediate. Compactness permits the common \(r_0\).

Thus both comparison rates in (7) can be referred back to the
real incoming half point. Applying this fact to the original
three-factor source still requires profile bounds there with
the complete adjoining cap and following factor, both second
Fourier weight alternatives, and the unchanged geometric
action. Those comparisons are not conclusions of (7).
This note alone completes neither the second period nor a knot
volume identity.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_four_unit_arc_fixed_lower_cut.md | a2e6a56f0ff12705e6c2b7a738122ed5bd98d095cfef6bb7a593a864b2c06293 |
| research_mixed_four_conditional_intermediate_real_source.md | e5eff44816440f4675f6a216d09f614330ebe4f72a2bdcc2ddf20939b711710d |
| research_mixed_symmetric_closing_complete_column_norm.md | 4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_four_conditional_unit_multiplier.md | 4d73d90557948056413ef0445cb7754569cbbc03e7ff3f35ecab0f3e9fe8f66f |

The author read the entire proof and all ten directly used source
implications and checked the source versions. Separate full proof
and direct-source review is required before adoption.
The new positive-height arguments above are written out; no theorem
whose statement requires \(d\le0\) is invoked on \(d>0\).
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation, or frozen-source edit was used.
