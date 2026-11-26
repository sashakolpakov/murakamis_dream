# A complete uniform left cap component on the real incoming arc

Research deduction, 8 November 2026. The existing private cut at
\(1/8\) works uniformly for every real incoming parameter
\(1/2\le a\le7/10\). A positive bound for the literal auxiliary
rows pays all lower physical cap rows and both entire weighted
left sides. The same comparison, with a smaller explicit reserve,
pays the unweighted join from that cut to the auxiliary-real
curve, on an already proved endpoint-source domain.

Thus no new endpoint packet below \(1/8\), or continuation from
a small seam disk, is needed for this contour component.
A fixed initial portion of the curve is paid as well.
The rest of the curve, its departure to the actual saddle,
and the full outer-cap assembly on the real incoming arc
remain separate. No numerical evaluation is used.

## 1. Exact finite source and the original action

Keep the literal interpolation from
[the complete upper-alias source](research_mixed_cap_tall_upper_alias.md):
\[
 \mathscr A_N(e,a,w)=
 \sum_{l=0}^{N-1}\frac{e_l(w)}{S_l}
 e^{i\pi Ne(l/N-a)}
 \frac{G_N(N(a+e))}
      {G_N(Na)G_N(N(e-l/N))}.
                                                               \tag{1}
\]
At \(e=j/N\) this is precisely
\(H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j\).
All auxiliary rows, original carriers, reflected reciprocal
zeros and both level parities are retained.

Put
\[
 E_0=\frac18,\qquad a=1-v,\qquad
       \frac3{10}\le v\le\frac12.
\]
The original endpoint and cap actions are
\[
 S(e)=F(e,u_c(e)),\qquad
 \Psi(e,a)=S(e)+J(a+e)-J(a)-i\pi ae,\qquad
 M(a)=\Re\Psi(e_*(a),a).
                                                               \tag{2}
\]
The [cap-wall action theorem](research_mixed_cap_wall_action_gap.md)
proves, on this entire incoming arc,
\[
 M(a)>h(v),\qquad h(v)=\lambda(v)+J(v),\qquad
 \lambda(v)=\Re S(v),\qquad h(v)>41/60.
                                                               \tag{3}
\]
These are the original zero-lift phases and additive constants.
The actual critical branch and its local ordinary-color
continuation are the ones in that theorem.

Let \(V_\theta(u)\) be the all-real Newton upper entropy, with
\(w=-2\cos\theta\). The
[zero-safe color theorem](research_mixed_newton_color_tubes.md)
gives
\[
 \begin{split}
 V_\theta(u)&\le V_0(u)
       =-2J(1/2-u)-2J(u)\le b_2<73/125,
                              &&0\le u\le1/2,\\
 V_\theta(u)&\le0,             &&1/2\le u\le1.
 \end{split}                                                    \tag{4}
\]
For real \(0\le E\le E_0\), the complete inner row rate in
(1) is therefore bounded by
\[
 \mathcal I_\theta(E,u)
    =V_\theta(u)-J(u)-\Re J_{\rm side}(E-u).
                                                               \tag{5}
\]
At a negative real argument the original reflected real value is
\(\Re J_{\rm side}(-d)=-J(d)\). There is no division by a sine
zero in (5). The uniform finite factorial/Newton inequalities
bound every literal row by this continuous rate, with polynomial
costs and arbitrarily small fixed tolerances. Those bounds hold
through both true ends.

## 2. A positive bound for every lower physical row

We prove the uniform bound
\[
 \boxed{\quad
 \mathcal I_\theta(E,u)<\frac{1741}{2560},
 \qquad 0\le E\le E_0,\quad 0\le u\le1,\quad 0\le\theta\le\pi .
 \quad}                                                         \tag{6}
\]
It is a bound before any auxiliary summation.

For \(0\le u\le E\), use the original sine chord
\(2\sin\pi s\ge6s\) for \(s\le1/6\), together with
\(-2J(1/2-u)\le2u\log2\). The entropy tangent used in
[the lower private-cut source, equations (10)--(12)](research_mixed_next_lower_private_cut_source.md)
gives, for every \(0<E\le E_0\),
\[
 \begin{split}
 \mathcal I_\theta(E,u)
 &\le 2u\log2+3u(1-\log(6u))
                    +(E-u)(1-\log(6(E-u)))\\
 &\le B(E):=2E\log2+3E(1-\log(6E))+9E^3.
 \end{split}                                                    \tag{7}
\]
The proof of that tangent bound is unchanged when \(E\)
varies: with \(d=E-u\), maximize
\(d\{1-\log(6d)+3\log(6E)-2\log2\}\), whose maximum is \(9E^3\).
Also
\[
 B'(E)=2\log2-3\log(6E)+27E^2>0
                                      \quad(0<E\le E_0).
\]
Keeping the exact rational sum in the cited source, rather
than rounding it upward to \(681/1000\), gives
\[
 B(E)\le B(E_0)
   <\frac7{40}+\frac{39}{80}+\frac9{512}
    =\frac{1741}{2560}.
                                                               \tag{8}
\]
Here \(\log2<7/10\) and \(\log(4/3)<3/10\) are the same
written elementary witnesses used there.

For \(E\le u\le1/2\), the complete-color upper profile is
\[
 \mathcal H(E,u)
   =-2J(1/2-u)-3J(u)+J(u-E).
                                                               \tag{9}
\]
Fix \(u\). As \(E\) ranges over \([0,\min(E_0,u)]\),
\(\partial_E\mathcal H=-J'(u-E)\).
Its only possible interior turning point is a minimum,
at \(u-E=1/6\). Hence the maximum is at an endpoint
of that \(E\)-interval.

At \(E=0\), (9) is \(V_0(u)\le b_2<73/125\).
If the other endpoint is \(E=u\), it is covered by (7)--(8).
Otherwise it is \(E=E_0\). Equations (15)--(22) of the
lower private-cut source prove
\[
 \partial_u\mathcal H(E_0,u)<\log(4/5)<0,\qquad
 \mathcal H(E_0,E_0)+J(5/8)<721/1000.
                                                               \tag{10}
\]
Moreover
\[
 J(5/8)=-J(3/8)
   =\int_{3/8}^{1/2}\log(2\sin\pi s)\,ds
   >\frac1{16}.
                                                               \tag{11}
\]
Indeed \(2\sin(3\pi/8)>\sqrt3\) and \(\log3>1\);
the latter follows, for example, from the already proved
\(\log3>13/12\).
Thus this endpoint of (9) is less than
\(721/1000-1/16<1741/2560\).

For \(1/2\le u\le1\), use only the second line of (4):
\[
 \mathcal I_\theta(E,u)
      \le -J(u)+J(u-E)\le-J(E)<1/6.
                                                               \tag{12}
\]
To check the middle inequality for all \(E\le E_0\),
differentiate in \(u\). Its only interior turning point,
\(u=(1+E)/2\), is a minimum. Its endpoint values are
\(J(1/2-E)\le0\) and \(-J(E)\ge0\).
The continuous cases \(E=0\), \(u=0,1\), and \(u=E\)
are included. Equations (7)--(12) prove (6).

The real outer factor in (1) is
\[
                         J(a+E)-J(a).
\]
It increases with \(E\in[0,E_0]\), since
\(1/2\le a+E\le33/40<5/6\) and \(2\sin\pi(a+E)>1\).
Consequently every literal auxiliary summand of every
physical cap row with \(0\le j/N\le E_0\) has rate less than
\[
 \frac{1741}{2560}+J(a+E_0)-J(a)
   =\frac{1741}{2560}-J(v-E_0)+J(v).
                                                               \tag{13}
\]
This includes the terminating rows at physical indices
without discarding the extra rows of the off-grid interpolation.
No compact-index endpoint asymptotic below \(1/8\) is an input.

## 3. A correlated lower bound for the wall profile

The correlation needed to compare (13) with (3) is
\[
 L(v):=\lambda(v)+J(v-E_0)>\frac{41}{60},
                 \qquad 3/10\le v\le1/2.
                                                               \tag{14}
\]
We prove it from the original curvature formula and the
already printed scalar consequences, without evaluating
any new action.

The exact real derivative identity is
\[
 -\lambda''(v)
 =\pi\cot\pi v+
  \frac{2\pi}{\sin\pi v}
      \Re\frac1{\sqrt{\,2-e^{-2\pi iv}\,}}.
                                                               \tag{15}
\]
The square root is the original branch. On this interval,
\(z=2-e^{-2\pi iv}\) has \(\Re z>2\), nonnegative imaginary
part, \(|z|\le3\), and \(\arg z<\pi/4\). Therefore
\[
                \Re z^{-1/2}>\frac12.
\]
Also \(v-E_0\ge7/40>1/6\), so
\[
 \frac{\sin\pi E_0}{\sin\pi(v-E_0)}<\frac45.
\]
Here \(\sin(\pi/8)<2/5\) and
\(\sin\pi(v-E_0)>1/2\). The cotangent subtraction formula
now gives
\[
 \begin{split}
 L''(v)
 =\frac{\pi}{\sin\pi v}
 \left\{
   \frac{\sin\pi E_0}{\sin\pi(v-E_0)}
      -2\Re z^{-1/2}
 \right\}<0.
 \end{split}                                                    \tag{16}
\]
Thus \(L\) is strictly concave and its minimum is at one
of its two endpoints.

At the left endpoint,
[wrapped-row transport, equation (15)](research_mixed_cap_wrapped_row_transport.md)
proves \(\lambda(3/10)>17/20\). Hence
\(L(3/10)>17/20-1/6=41/60\).

For the other endpoint, the saved scalar consequences in
[the bridge phase floor, equation (17)](research_mixed_endpoint_bridge_phase_floor.md)
are
\[
 \lambda(7/20)>108/125,\qquad
                      |\lambda'(7/20)|<1/200.
                                                               \tag{17}
\]
They are imported as written; no saved primitive is replayed.
For \(7/20\le v\le1/2\), we have
\[
 \cot\pi v<3/5,\qquad \sin\pi v>5/6,\qquad
             |\sqrt{2-e^{-2\pi iv}}|>8/5.
\]
Indeed \(v>1/3\), and
\(|2-e^{-2\pi iv}|^2\ge7>(8/5)^4\).
Equation (15) consequently gives
\[
                 0<-\lambda''(v)<(21/10)\pi<33/5.
\]
Twice integrating from \(7/20\) to \(1/2\) yields
\[
 \lambda(1/2)>
 \frac{108}{125}-\frac1{200}\frac3{20}
                    -\frac{33}{10}\left(\frac3{20}\right)^2
 =\frac{789}{1000}.
                                                               \tag{18}
\]
Finally \(-J(3/8)<(\log2)/8<7/80\), so
\[
 L(1/2)>\frac{789}{1000}-\frac7{80}
            =\frac{1403}{2000}>\frac{41}{60}.
\]
This proves (14). Combining (3), (13), and (14) gives the
uniform positive-row reserve
\[
 M(a)-\left\{
       \frac{1741}{2560}+J(a+E_0)-J(a)
       \right\}
  >\frac{41}{60}-\frac{1741}{2560}
   =\frac5{1536}.
                                                               \tag{19}
\]

## 4. Both complete weighted left sides

At the real private cut \(E_0\), (19) bounds every literal
auxiliary row, uniformly at all real ordinary colors.
Use the exact weighted row rates of
[the later-point left-current proof, equations (4), (11)--(14)](research_mixed_cap_later_point_left_currents.md).
Those identities do not require \(a=a_0\).
For \(H>0\), put
\[
 \rho=e^{-2\pi H},\quad
 A=\Arg(1-\rho e^{2\pi i(E_0-u)}),\quad
 B=\Arg(1-\rho e^{2\pi i(a+E_0)}).
\]
The disk arguments are in \((-\pi/2,\pi/2)\), and \(B>0\).
After retaining the exact cotangent penalty \(2\pi H\),
the upper and lower derivatives are
\[
 \partial_H W_\theta^+
       =-2\pi(1-a)+A-B<-\pi/10,\qquad
 \partial_H W_\theta^-
       =-2\pi(1-u)+A-B<0.
                                                               \tag{20}
\]
For the second inequality, \(A\le0\) when \(u\le E_0\)
or \(u\ge E_0+1/2\). In the intervening interval
\(u<5/8\), it is less than \(-\pi/4\).
The limiting value at \(u=1\) is also strictly negative
because \(B>0\). Every reflected lower carrier is retained.

Both weighted rates therefore decrease from the positive
real-cut majorant in (19), for all \(0\le H\le1\).
This pays the two entire vertical currents, rather than
only their short portions. It assumes no endpoint packet
at the larger heights.

Use the exact half-grid convention
\[
 L_N=\lfloor N/8\rfloor+1,\qquad
                  \ell_N=(L_N-1/2)/N.
                                                               \tag{21}
\]
The two cotangent remainders on the respective halves have
modulus at most \(2e^{-2\pi N H}\), including \(H=0\).
Their original orientations and density \(+N\) are unchanged.
Uniform zero-safe factorial bounds and continuity of the
integrated row rates preserve (19) at
\(\ell_N=E_0+O(N^{-1})\); their error is
\(O(\log N/N)\), including a reciprocal zero.
There is no pointwise derivative assertion at such a zero.

It follows from (13), (19), and (20), after polynomial row
counts and fixed tolerance losses, that the complete lower
physical sector and each complete weighted left side obey
\[
 \begin{split}
 \sum_{j=0}^{\lfloor N/8\rfloor}
 \left|H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j\right|
     &\le C N^B e^{N(M(a)-1/1000)},\\
 |\text{upper weighted left current}|+
 |\text{lower weighted left current}|
     &\le C N^B e^{N(M(a)-1/1000)}.
 \end{split}                                                    \tag{22}
\]
The physical estimate even bounds the positive double sum
of its literal auxiliary summands. Both assertions hold for
all \(a\in[1/2,7/10]\), all \(-2\le w\le2\), both parities,
and all sufficiently large levels. Fixed ordinary derivatives
cost only polynomial factors, by the original color-tube
bounds before summation.

## 5. The full unweighted join to the proved source curve

Let
\[
 t_L=\frac{\sqrt3-1}{2},\qquad
 e_L=E_0-i\eta_L=
       \frac{\Log(1-2t_L^2+2it_L)}{2\pi i}.
\]
The existing curve proof gives
\[
                         0<\eta_L<\frac1{49\pi}.
                                                               \tag{23}
\]
The [region above the auxiliary-real curve](research_mixed_endpoint_region_above_real_curve.md)
supplies the complete endpoint packet on the entire
vertical segment \(E_0-i[0,\eta_L]\), and on a fixed
complex neighborhood. In particular its original
auxiliary critical branch satisfies
\[
 0<\Re u_c<E_0,\qquad \Im u_c\ge0,\qquad
 S'(e)=-J'(e-u_c)+i\pi u_c.
\]
The argument \(e-u_c\) has positive real part less than
\(E_0\) and nonpositive height. Thus
\[
                  \Im S'(e)<\pi/2+\pi E_0.
\]
The incoming sine argument is nonnegative and obeys
\[
 \begin{split}
 0\le\Arg\sin\pi(a+E_0-i\eta)
 &=\arctan\{-\cot\pi(a+E_0)\tanh(\pi\eta)\}\\
 &<2\pi\eta.
 \end{split}
\]
Indeed \(a+E_0\le33/40\) and
\(-\cot\pi(a+E_0)\le\cot(7\pi/40)<\sqrt3<2\).
The original carrier in (2) gives the resulting bound
\[
 \partial_\eta\Re\Psi(E_0-i\eta,a)
 =\Im S'(e)+\Arg\sin\pi(a+e)-\pi a
                    <\frac{\pi}{8}+2\pi\eta.
                                                               \tag{24}
\]
All arguments here are the original zero lifts.

The total rise from the real cut to any point of this
join is therefore less than
\[
 \frac{\pi\eta_L}{8}+\pi\eta_L^2
   <\frac1{392}+\frac1{7203}<\frac1{360}.
                                                               \tag{25}
\]
The middle inequality uses \(\pi>3\); the final comparison
follows from \(7203>4410\) and
\(1/360-1/392=1/4410\).
At the real cut, its complete critical action cannot
exceed the positive finite-row ceiling in (13).
This follows either from its nonzero whole endpoint packet
and the positive bound, or directly by the same source
comparison. Hence (19), (24)--(25) imply
\[
 \boxed{\quad
 \Re\Psi(E_0-i\eta,a)
       <M(a)-\frac{11}{23040}
       <M(a)-\frac1{2500},
 \quad 0\le\eta\le\eta_L,\quad 1/2\le a\le7/10.
 \quad}                                                         \tag{26}
\]
The subtraction is \(5/1536-1/360=11/23040\).
This proves the entire unweighted join, without needing
a global outer-cap asymptotic or a departure-point comparison.

The complete endpoint packet on that join, multiplied by
the unchanged outer factorial ratio, now bounds its
original \(+N\)-weighted integral with, for example,
finite gap \(1/5000\). The short real segment from
\(\ell_N\) to \(E_0\) retains the stronger real-cut gap.
Every endpoint of this deformation remains in the
constant-mode integral.

## 6. A compatible initial curve segment and local derivatives

The auxiliary-real curve theorem supplies a fixed open
endpoint-source neighborhood of its entire curve.
The original phase is continuous jointly in that curve
parameter and in \(a\in[1/2,7/10]\).
Equation (26) has a common positive reserve at \(e_L\).
Consequently there is a fixed \(\epsilon>0\), independent
of \(a,N\), such that the initial segment
\[
 e(t),\qquad t_L\le t\le t_L+\epsilon,
\]
lies below \(M(a)\) by \(1/5000\), for every incoming
parameter in the real arc. Shrink \(\epsilon\) inside
the already proved curve if needed. Its entire original
\(+N\)-weighted integral has, for example, finite gap
\(1/10000\). This is an actual paid contour component
with a proved source neighborhood; it is not a hypothesis
about the rest of the curve.

For each base \(a\), fix (21), the vertical join and the
chosen initial curve before varying the parameters.
The positive finite-row bounds preserve the reserves
on sufficiently small ordinary-color/incoming complex
neighborhoods. The main joins use their already proved
holomorphic endpoint packet. A finite cover of the real
incoming arc gives uniform constants after common
shrinks. Normalizing by the local original
\(e^{N\mathcal T(a,w)}\), with
\(\mathcal T(a,w)=\Psi(e_*(a,w),a,w)\), and applying
Cauchy's formula on smaller neighborhoods gives all
fixed mixed derivatives with a smaller common gap,
for example \(1/20000\).

The all-real assertions in (22) use the complete-color
reference \(M(a)\); they do not assert a nonzero
far-color action. The unweighted join and its initial
curve integral use only complete color and its fixed
small complex neighborhood. No moving integer row
set or reference-dependent contour is differentiated.

We have paid, uniformly on the full real incoming arc,
the lower physical sector, both entire weighted left
sides, the full unweighted left join, and a compatible
initial source segment. Continuing that segment to
a descending path through the actual outer saddle
is the remaining main-path problem. This note makes
no selected affine-action or filling-family claim.

