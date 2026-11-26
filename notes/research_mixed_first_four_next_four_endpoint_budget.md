# A static central budget for a first four followed by a four

Research deduction, 6 November 2026.

For an actual mixed open word beginning with two type-four vertices,
this note proves a stronger positive-height ordinary-coordinate barrier,
a forced-coordinate ceiling at height \(1/100\), and an explicit
static endpoint majorant. An endpoint gain at most \(\pi/384\)
would give a common central real-phase gap \(1/500\). The remaining
uniform scalar inequality is stated precisely below and is not proved.
No source-root calculation, interval cover, or source certificate is
run or replayed in these deductions.

## 1. The original reference and fixed horizontal domain

Let \(m\ge3\), with first and second types both four. Retain the
same actual open critical reference, canonical private cap action,
logarithmic lifts and outgoing tangent as in
[the joint height-envelope proof](research_mixed_selected_boundary_height_envelope.md).
The joint holomorphic phase is
\[
 \begin{split}
 \mathcal F_4(e,s;z,b)={}&S(e)+g(e+z)+g(s+z)+g(s+b)
      -3g(s)-3g(z)-\tfrac32g(b)-g(e)\\
 &-\tfrac{i\pi}{2}(e-e^2)+2\pi izs.
 \end{split}
 \tag{1}
\]
All primitives have their original branches. Write \(f(x,k)\) for
its real part after the original real outgoing affine term is
subtracted, with \(x=(e_R,s_R,z_R,b_R)\) and \(\Im z=k\).
The other heights are fixed at the actual values \(h_e,h_s,h_b\).
The original horizontal domain is
\[
 K=[.27,.49]\times[.125,.5]\times[.22,.45]^2.
 \tag{2}
\]
The reference bounds supplied by the
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md),
[coupled attached-height bound](research_mixed_first_four_attached_height_bound.md),
and [ordinary block images](research_mixed_cyclic_critical_height_bounds.md)
give
\[
 \begin{gathered}
 .333<e_{*,R}<.363,\quad -.051<h_e<-.019,\\
 .246<z_{*,R}<.350,\quad -.078<c:=\Im z_*<-.020,\\
 .24<s_{*,R},b_{*,R}<.36,\quad -.102<h_s,h_b<-.001.
 \end{gathered}
 \tag{3}
\]
The ordinary real ranges follow from the reduced disk of radius
\(.060\) about \(.30-.052i\), for both outputs of vertex 2.
The [reduced-disk pair-sum theorem](research_mixed_reduced_disk_pair_sums.md)
also gives
\[
             \Re(s_*+z_*)>.545.
 \tag{4}
\]
It applies when the other external leg is either ordinary or attached;
the latter case includes \(m=3\).

Set
\[
 H=1/100,\qquad G(k)=\max_{x\in K}f(x,k),\qquad
 M=f(x_*,c),\qquad L_*=G(H)-f(x_*,H).
 \tag{5}
\]
Section 12 of the height-envelope proof gives \(G(c)=M\) and
\(f_k(x_*,c)=0\), using the original unexponentiated equations and
the same outgoing tangent. Its real-concavity argument applies to
both next types. The two central alternatives are
\[
          f_{\rm fac}=f(x,H)-2\pi H,\qquad
          f_{\rm force}=f(x,H)+\Re g(z_R+iH).
 \tag{6}
\]

## 2. A stronger lower barrier for the ordinary coordinate

**Lemma 1.** At every maximizer of either central alternative, for
\(0\le k\le7/500\), one has \(s_R>11/50\).

The existing whole-path bound gives \(s_R>.2\). At the proposed
cut \(s_R=.22\), put
\(r=|e^{-2\pi is}|\), \(t=|e^{-2\pi ib}|\), and
\(q=|e^{-2\pi iz}|^{-1}\). The unchanged type-four heights and
the existing exponential witnesses give
\[
             13/25<r,t<1,\qquad q>91/100.
 \tag{7}
\]
Here \(r,t>10/19>13/25\) follows from
\(e^{.204\pi}<19/10\); the upper bounds use negative ordinary
heights. The lower bound for \(q\) follows from
\(e^{.028\pi}<100/91\).

The two summed real parts are in \([.44,.67]\). Thus their
cosines are less than \(-12/25\), while
\(\cos(2\pi s_R)>9/50\). The cubic sine bounds at
\(314/625<.16\pi\) and \(471/2500<.06\pi\) prove these
two rational inequalities. The exact original derivative, including
the chirp, therefore satisfies
\[
 e^{2\partial_{s_R}f}>
 \frac{\{(91/100)^2+r^2+(24/25)(91/100)r\}
       \{1+(13/25)^2r^2+(24/25)(13/25)r\}}
      {(1+r^2-(9/25)r)^3}>1.
 \tag{8}
\]
For completeness, numerator minus denominator is
\[
 P(r)=-r^6+\frac{27}{25}r^5-\frac{1949}{625}r^4
 +\frac{1149249}{390625}r^3-\frac{10804879}{6250000}r^2
 +\frac{1849209}{781250}r-\frac{1719}{10000}.
 \tag{9}
\]
For \(r=13/25+(12/25)v\), its degree-six Bernstein coefficients,
with common denominator \(244140625000\), are
\[
 (194930869745,221659107435,241725065149,250490096231,
       239542984425,194584871875,90328203125).
 \tag{10}
\]
All are positive, proving (8) on the whole closed radius interval.
The established real concavity makes this marginal decrease with
\(s_R\) on \([.2,.22]\). Its positive value at the cut excludes
that entire interval by an admissible increase of \(s_R\).
The extra forced term depends only on \(z\), so the same proof
applies to both alternatives.

The stronger private barrier \(e_R>153/500\) from Section 2 of
[the sharper forced-budget proof](research_mixed_forced_optimizer_sharper_budget.md)
also applies here at positive height. Although that note states its
application for next type three, the barrier proof uses only
\(h_e\in(-.051,-.019)\), \(z_R\in[.22,.45]\),
\(0\le k\le7/500\), the common private derivative, and the
canonical cap branch. None changes when the next type is four.
The earlier barrier \(e_R>.3\) for either next type is Proposition 7
of the height-envelope proof; its proof supplies the same starting
point for this strengthened argument.

## 3. A forced ceiling at the chosen final height

**Lemma 2.** At \(H=1/100\), every forced maximizer satisfies
\(z_R<21/50\).

Suppose \(.42\le x=z_R\le.45\). The private barriers and
Lemma 1 give \(.306<e_R<.4\) and \(.22<s_R<.44\).
Consequently
\[
 \begin{gathered}
 \cos(2\pi(e_R+x))>-151/1000,\qquad
 \cos(2\pi(s_R+x))>-319/500,\\
                    \cos(2\pi x)<-219/250.
 \end{gathered}
 \tag{11}
\]
For the first bound use \(e_R+x>.726\) and
\(\sin(.048\pi)<.048(22/7)<151/1000\). The second uses
\(s_R+x>.64\) and \(\cos(.28\pi)<319/500\); its witness
is the degree-eight cosine upper polynomial at
\((7/25)(157/50)\). The last uses
\(\cos(.16\pi)>219/250\), proved by the degree-six cosine
lower polynomial at \((4/25)(22/7)\).

Put \(R=e^{2\pi H}\). The actual heights give
\(|E|<8/9\), \(|S|^{-1}<19/10\), and
\(R>133/125\). For the last inequality,
\(1+157/2500+(157/2500)^2/2>133/125\).
The squared original forced derivative ratio is bounded above by
\[
 \frac{(1+(302/1125)R+(64/81)R^2)
       (R^2+(6061/2500)R+361/100)}
      {(R^2+(219/125)R+1)^2}<1.
 \tag{12}
\]
The denominator minus numerator is
\[
 P_F(R)=\frac{17}{81}R^4+\frac{66824}{50625}R^3
 +\frac{7167761}{12656250}R^2+\frac{12433}{112500}R
 -\frac{261}{100}.
 \tag{13}
\]
It increases for \(R>0\), and
\(P_F(133/125)=60991067/7910156250>0\).
Thus the real forced derivative is negative at every proposed
maximizer with \(x\ge.42\). Decreasing \(x\) is an admissible
improvement on the original domain, proving the ceiling.

## 4. A fixed-reference budget sufficient for both alternatives

Along the vertical line through the actual reference,
\[
 \frac{f_{kk}(x_*,k)}\pi
 \le3\cot(\pi x)+\tan\pi(x-.137)+\tan\pi(x-.14)
 <19/5,\qquad x=z_{*,R}.
 \tag{14}
\]
The private and ordinary summed real parts lie above one half by
(3)--(4), and the reference upper bounds are \(e_{*,R}<.363\)
and \(s_{*,R}<.36\). Imaginary displacement decreases the
magnitude of a negative real cotangent. The displayed function is
convex on \([.246,.35]\). At the lower endpoint the bounds
\(\cot(.246\pi)<103/100\), \(\tan(.109\pi)<9/25\), and
\(\tan(.106\pi)<7/20\) give a total less than \(19/5\).
At the upper endpoint,
\(\tan(.15\pi)<13/25\), \(\tan(.213\pi)<4/5\), and
\(\tan(.21\pi)<39/50\) give a total less than \(157/50\).
The two new tangent bounds follow from the degree-five sine upper
and degree-six cosine lower polynomials at the corresponding rational
multiples of \(22/7\); all denominators are positive.

Since \(H-c<11/125\) and the initial vertical derivative is zero,
\[
 f(x_*,H)-M<\frac{19\pi}{10}(11/125)^2.
 \tag{15}
\]
It follows that the single endpoint inequality
\[
                             L_*\le\pi/384
 \tag{16}
\]
is sufficient for a common central gap \(1/500\). Indeed (15)--(16)
give \(G(H)-M<519533\pi/30000000\), whence
\[
 \max f_{\rm fac}-M<-\frac{80467\pi}{30000000}<-1/500.
 \tag{17}
\]
For the forced alternative, \(\Re g(x+iH)\) increases with
\(x\) on the original plateau. Lemma 2 and the original argument
bound give
\[
 \Re g(x+iH)\le\Re g(.42+iH)
 \le J(.42)-\pi/1250<-27/500-\pi/1250.
 \tag{18}
\]
To verify the last constant, \(J'(.42)>33/50\) and
\(J'(1/2)>69/100\). The first follows from
\(e^{33/50}<2-(44/175)^2<2\cos(.08\pi)\), using the
positive exponential series with its tail bounded geometrically
after degree three. The second is the usual positive
\(2\operatorname{atanh}(1/3)\) series for \(\log2\).
Concavity of \(J'\) on \([.42,.5]\) then gives
\(J(.42)<-(.08)(.66+.69)/2=-27/500\).
Combining with \(\pi<22/7\),
\[
 \max f_{\rm force}-M
 <\frac{495533\pi}{30000000}-\frac{27}{500}
 <-\frac{219137}{105000000}<-1/500.
 \tag{19}
\]
Here the forced maximizing point need not maximize the unselected
phase: its unselected value is bounded by the same full-domain
\(G(H)\). No factorial-only real-coordinate restriction is imposed
on that forced point.

## 5. A scalar majorant that permits summed angles below one half

The existing factorial upper-coordinate bound and the preceding
barriers put every final factorial maximum in
\[
 e_R\in[.3,.4],\quad s_R\in[.22,.44],\quad
 z_R\in[.22,.35],\quad b_R\in[.22,.45].
 \tag{20}
\]
The bound \(z_R<.35\) is Proposition 1 of
[the positive-height factorial estimate](research_mixed_positive_height_factorial_bounds.md).
Only the original lower \(z\) face and the two outgoing faces need
be allowed; no assertion of interior stationarity there is used.
In particular (20) does not imply \(s_R+z_R>1/2\) or
\(s_R+b_R>1/2\). The type-three edge decomposition cannot be
imported with those extra constraints.

Let \(A,B,C,\ell\) be the same exact logarithmic increments as
in the static endpoint note, now at \(H=1/100\), and put
\[
 d=\ell-B,
 \quad \ell=2\pi(H-c),
 \quad q=\Re(s_*+z_*)-1/2\in(.045,.21).
 \tag{21}
\]
The endpoint gradient is still
\((A,-d,A+B-3C,0)\): changing the coefficient of the fixed-height
single-node terms introduces no new gradient increment.
Moreover \(A>0\) and \(0<B<\ell\), so \(d>0\).
Indeed both reference products \(EZ,SZ\) have negative real part,
and the same elementary modulus identities used in the type-three
endpoint proof apply.

For a potential \(W\), let \(D_W\) denote its Bregman remainder
about the actual reference at the final fixed heights. Decompose
the negative phase, modulo affine terms, into
\[
 \begin{gathered}
 P_e=-\Re S(e)+\Re g(e),\quad P_s=2\Re g(s),\quad
 P_z=3\Re g(z),\quad P_b=\tfrac12\Re g(b),\\
 Q_e=-\Re g(e+z),\qquad Q_s=-\Re g(s+z),\\
 W_{sb}=\Re g(s)+\Re g(b)-\Re g(s+b).
 \end{gathered}
 \tag{22}
\]
The outgoing pair \(W_{sb}\) is convex on the entire connecting
rectangle, by the pair-Hessian argument in Section 12 of the
height-envelope proof. Thus \(D_{W_{sb}}\ge0\), without a
summed-angle assumption. Also \(D_{P_b}\ge0\).

The node conjugate bounds needed below are
\[
 \pi\phi_e^*(a)\le\frac{45}{163}a^2,
 \qquad \pi\phi_z^*(a)\le\frac13a^2,
 \qquad \pi\phi_s^*(-a)\le\frac58a^2\quad(a\ge0).
 \tag{23}
\]
The first is the canonical cap bound. For the second the full
connecting interval is \([.22,.35]\), where
\(P_z''>3\pi/2\), just as in the centered type-three estimate.
For the last, only targets at most \(s_{*,R}<.36\) can give
positive conjugate objective. On \([.22,.36]\),
\(\Re\cot\pi(t+ih_s)>2/5\), so \(P_s''>4\pi/5\).
The cotangent decreases there; at the upper endpoint use
\[
 \sin(.28\pi)>3/4,\quad \cos(.28\pi)<13/20,
                  \quad \cosh(.204\pi)<49/40.
\]
The first two follow from the cubic sine lower and quartic cosine
upper polynomials at \(7/8<.28\pi\). The hyperbolic bound follows
from its positive series at \(321/500>.204\pi\).

For the private edge, the same centered cubic argument gives
\[
                   \pi\chi_e^*(u)\le k_0u^2,
                    \qquad k_0=3075/(356\pi).
 \tag{24}
\]
Its target real sum is now \([.52,.75]\), and its actual center
minus one half is in \((.079,.213)\). The height obeys
\(|2\pi(h_e+H)|<.082\pi<.26\), whose hyperbolic cosine is less
than \(21/20\). Hence \(Q_e''(t)\ge(40\pi^2/41)(t-.5)\)
on the complete connecting interval. Explicitly, for
\(0\le u\le\pi/2\), the derivative of
\((41/20)\sin u-u(21/20+\cos u)\) is
\(2\sin(u/2)\{u\cos(u/2)-(21/20)\sin(u/2)\}\ge0\).
Here \(u\cot(u/2)\) decreases to \(\pi/2>21/20\).
The function vanishes at zero, proving the claimed curvature bound
all the way to the target sum \(.75\). Its centered remainder is at
least \((89\pi^2/3075)v^2\), giving (24).

The remaining ordinary edge is treated on both sides of its flat
point. Put
\[
       \rho=3/50,\qquad \kappa=10\pi^2/11,
                          \qquad \eta=11\pi^2/10.
 \tag{25}
\]
Its target \(y=s_R+z_R-.5\) ranges in \([-\rho,.29]\),
and its reference center is \(q\) in (21). On the whole interval,
\[
 Q_s''(.5+y)\ge
 \begin{cases}\eta y,&y\le0,\\ \kappa y,&y\ge0.\end{cases}
 \tag{26}
\]
For \(y\ge0\), the fixed height obeys
\(|2\pi(h_s+H)|<.184\pi<3/5\), whose hyperbolic cosine is
less than \(6/5\). With \(u=2\pi y<2\), the function
\((11/5)\sin u-u(6/5+\cos u)\) increases from zero:
its derivative is
\(2\sin(u/2)\{u\cos(u/2)-(6/5)\sin(u/2)\}\ge0\),
using \(u\cot(u/2)>5/4\). Indeed \(t\cot t\) decreases for
\(0<t<1\), and the alternating Taylor bounds give
\(\tan1\le(101/120)/(389/720)=606/389<8/5\).
Thus \(u\cot(u/2)=2t\cot t>2\cot1>5/4\).
This proves the positive branch.
For \(y\le0\), \(|u|\le.12\pi\) and
\(\cos u>9/10\). Thus
\(Q_s''(.5+y)/y<20\pi^2/19<\eta\); multiplying by the
negative \(y\) proves the other branch.

Define \(W(y)=\kappa y^3/6\) for \(y\ge0\), and
\(W(y)=\eta y^3/6\) for \(y\le0\). The function
\(Q_s(.5+y)-W(y)\) is convex by (26). Its Bregman remainder
is nonnegative, even though \(Q_s\) itself need not be convex
on the full target interval. Therefore its restricted conjugate at
a nonpositive force is bounded by the following explicit function:
\[
 \begin{split}
 T_q(a)=\max\biggl\{&
 aq-\frac\kappa3q^3
       +\frac\kappa3(q^2-2a/\kappa)_+^{3/2},\\
 &a(q+\rho)-\frac\kappa3q^3-\frac{\kappa\rho}{2}q^2
                           +\frac\eta6\rho^3\biggr\},
       \qquad \chi_s^*(-a)\le T_q(a),\quad a\ge0.
 \end{split}
 \tag{27}
\]
To check (27), maximize the model conjugate objective on the two
parts of the target interval. On \([0,.29]\), its maximum is
at \(\sqrt{(q^2-2a/\kappa)_+}\le q<.21\), giving the first
entry. On \([-\rho,0]\), its objective is convex, so its maximum
is at an endpoint. Zero is already included in the first entry;
\(-\rho\) gives the second. This retains every target below one
half and introduces no new source stationary point.

## 6. A finite explicit family of sufficient tests

For any \(0\le\theta\le1\), use the ordinary-edge flow
\(-\theta d\), no outgoing-pair flow, and a free private-edge
flow \(u\). Put
\[
 h_\theta=3C-B-\theta d,\qquad
                    m_\theta=A-\frac{163}{298}h_\theta.
 \tag{28}
\]
The node forces are
\((A-u,-(1-\theta)d,A-h_\theta-u,0)\). Their sum with
the two edge flows is exactly the original endpoint gradient.
Fenchel's elementary supremum inequality, which needs no convexity
assumption for the bounded \(Q_s\) cost, and (23)--(27) give
\[
 \boxed{\displaystyle
 \pi L_*\le\mathcal N_\theta:=
 \frac58(1-\theta)^2d^2
   +\frac{45}{298}h_\theta^2+\frac12m_\theta^2
   +\pi T_q(\theta d).}
 \tag{29}
\]
The coefficient \(1/2\) follows by minimizing
\((45/163)(A-u)^2+(A-h_\theta-u)^2/3+k_0u^2\)
exactly as in the centered type-three proof: with \(D=298/489\),
its value is
\(45h_\theta^2/298+Dk_0m_\theta^2/(D+k_0)\), and
\(Dk_0/(D+k_0)<1/2\).

One fully specified remaining scalar inequality is
\[
 \min_{\theta\in\{0,1/4,1/2,3/4,1\}}
                \mathcal N_\theta\le\frac{\pi^2}{384}
                 \quad\hbox{at every actual reference.}
 \tag{30}
\]
If proved, it implies (16), hence both central gaps (17),(19).
The actual data are rationally parametrized by the original endpoint
coordinate \(U=e^{2\pi i u_*}\):
\(E=E(U), Z=Z_1(U), S=S_1(U)\), with outgoing and next external
exponentials now given by \(R_3(Z_1(U),S_1(U))\), not \(R_2\).
The canonical endpoint sheet, original logarithmic lifts, ordinary
type-four output ranges and remaining-word compatibility must remain.
Independent optimization of \(A,B,C,q\) is not licensed by (29).

Equation (30) has not been proved. The present results are the new
coordinate barriers, the common budget at one specified height, and
the explicit endpoint majorants, including the summed-angle region
below one half. They establish no complete selected-source comparison,
no length-two statement, and no knot or filling volume conclusion.
