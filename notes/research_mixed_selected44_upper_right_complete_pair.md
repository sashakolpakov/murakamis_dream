# The complete selected initial four/four pair on the upper right horizontal

Private written proof, 10 November 2026. The selected first path extends
from one half to seven tenths at height \(1/100\). The proof bounds the
literal complete type-four cap and type-four conditional polynomial,
with the original first Fourier weight and selected monomial. It keeps
the neighboring target on its whole plateau at its actual negative
height. No vertical reset or subsequent arc is included.

## 1. Source, calibration and statement

Use exactly the actual coupled references of
[the selected half-face theorem](research_mixed_selected44_right_half_interval.md).
The positive three/four word has length \(m\ge3\) and begins with four
and four. Its actual cap and conditional private heights and second
retained height satisfy
\[
 -.051<h_e<-.019,\qquad -.108\le h_s\le0,\qquad
                         -.102\le d\le-.001.
\]
Only these weaker established private-height bounds are used below;
the reference itself remains the actual coupled reference.
Put
\[
 H=1/100,\quad r=e^{2\pi H},\quad
 a=x+iH,\quad 1/2\le x\le7/10,\qquad
 b=z+id,\quad z\in P=[11/50,9/20].                         \tag{1}
\]
For \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\) and
\(p_j(X)=(q_NX;q_N)_j\), retain
\[
\begin{split}
 X&=e^{-2\pi ia},\qquad Y=e^{-2\pi ib},\\
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 \mathcal K_N(w;a,b)&=U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X)X^{-N}.
\end{split}                                                   \tag{2}
\]
The outgoing allocation is the unchanged \(|d_N(Y)|^{1/2}\).
Every \(H_N\), physical row, forcing term and original scalar is kept.

Let \(\Psi,Q,\Lambda(z)\) have exactly the definitions and original
primitive constants in (4) of the half-face theorem. Thus
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias.           \tag{3}
\]
Set \(\gamma_0=1/4000\).

**Theorem 1.** For every \(\tau>0\), uniformly on (1), both level
parities and all real ordinary colors \(w\in[-2,2]\),
\[
 |\mathcal K_N(w;a,b)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
       e^{N\{\Lambda(z)-1/8000+\tau\}}.                    \tag{4}
\]
At a separately reserved arbitrary allowance, the same bound holds
on fixed small ordinary-color disks, with fixed derivatives on smaller
disks. The original horizontal integral with measure \(+N\,da\) and
its exterior scalar has the same exponential bound.

The complete Fourier upper theorem retains the two first alternatives
\[
 W_1(a)=-\Re g(a)-2\pi H,\qquad W_0(a)=0.                 \tag{5}
\]
Here \(\Re g(1/2+iH)=0\), and
\(\partial_x\Re g(a)=\log|1-re^{-2\pi ix}|>0\) on (1).
Consequently their maximum is zero throughout this note. The outgoing
halfweight has rate \(-\Re g(b)/2\), because \(d<0\) and \(z<1/2\).
These are upper bounds with both forcing alternatives retained, not
divisions by either finite weight.

## 2. The selected half-face supplies the same source plane

Write \(a_L=1/2+iH\). At that point let \(\mathcal A_L\) be the maximum
of the five bare cap profiles (7) of the half-face theorem and its
separate true-end ceiling
\[
 E_* =3/5+2\pi H+\log4/100<69/100.                         \tag{6}
\]
The five profiles include main height \(h_e\), real cuts \(.27,.49\),
and aliases at \(-.055,.04\) with penalties \(.11\pi,.08\pi\).
The original cap convexity and weighted-side comparisons bound its
two unweighted joins and four weighted verticals by these profiles.
The [complete upper-target source](research_mixed_cap_upper_target_extension.md)
bounds all omitted physical cap rows
by the same envelope, with its true ends kept separately. The number
\(\mathcal A_L\) is an upper rate; it is not the logarithm of a finite
cap value.

The profile proof of the half-face theorem gives
\[
 \mathcal A_L+\max_{1/8\le v\le1/2}
       \Re Q(v+ih_s;a_L,b)-\tfrac12\Re g(b)
 \le\Lambda(z)-\gamma_0.                                  \tag{7}
\]
To justify the closed upper endpoint in (7), its Section 3 proves
the same main inequality on every fixed right cut below one half,
with gap \(1/2000\) independent of that cut. Section 4 treats both
cap aliases and true ends with the same reserve. Pass to one half
using continuity of the integrated logarithmic primitive. No finite
contour is extended by this limiting statement.

Its physical-profile proof also pays every high row \(1/2\le t\le1\),
the real cut \(t=1/8\), and all lower rows through that cut, with the
same actual affine rate. At the selected half face the upper cap
alias has an additional reserve greater than \(1/50\), by its
pointwise same-index comparison (20). The true-end ceiling has
an additional reserve greater than \(53/500\) for these physical
profiles: at the old face \(x=.45\) this is (9), and its physical-row
derivative is nonpositive up to one half. For low rows use their
increasing ratio to the cut at the current half face. These stronger
reserves are retained below; a bound on a signed sum would not supply
them.

## 3. Complete cap transport, including the positive-height tails

The original global numerator factorial gives the continuous rate
\[
 \mathfrak p(q)=
 \begin{cases}
 \Re g(q),&0<\Re q\le1,\\
 \Re g(q-1)+2\pi(\Im q)_+,&1\le\Re q\le6/5.
 \end{cases}                                                \tag{8}
\]
It retains both terms of
\(\Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q)\). Its two boundary
values agree. In the exact notation of
[the lower-right cap source](research_mixed_first_four_cap_lower_right_horizontal.md),
the retained interpolant is
\[
 \mathscr A_{1,N}(e,a,w)
 =D_N(e)^{-1}\mathcal C_N(e,w)
                     \Pi_N(a+e)E_N(a)E_N(e).
 \tag{8a}
\]
Its full coefficient continuation \(\mathcal C_N\), normalization
\(D_N\), and physical values are unchanged. The original residue
identity keeps its \(+N\,de\) zero mode, both unweighted joins,
and six weighted currents with coefficient \(N/(2i)\), as well as
every physical row outside its two half-grid cuts. The coefficient's
all-real-color estimate holds on the whole original private rectangle.
Only its numerator factorial crosses the new wall.

For this original cap interpolant on
\(e=u+i\eta\in[.27,.49]+i[-.055,.04]\), replace only the
numerator primitive in \(\Psi\) by (8); denote the resulting real
upper rate by \(\widehat\Psi(e,a)\). All remaining factorial and
complete-coefficient factors have their original regular domains.

Put \(q=e^{2\pi\eta}\), \(D=|1-X|\), and
\(N_e=|1-Xe^{-2\pi ie}|\). The original elementary bounds give
\[
 1<r<43/40,\qquad 7/10<q<13/10,
 \qquad \cos2\pi(x+u)>1/8,\quad \cos2\pi x<-4/13.
\]
The exact squared difference therefore satisfies
\[
 D^2-N_e^2>
 r\left\{8/13+7/40-(69/100)r\right\}
 >r\,2529/52000>0.                                         \tag{9}
\]
On either branch of (8),
\(\partial_x\widehat\Psi=\log(N_e/D)<0\).
The added period term is constant in \(x\). Thus every point of the
entire original cap contour decreases from its half-face rate,
including all its aliases, weighted sides and unweighted joins.
Integrate the continuous upper rate across its numerator wall.

For real compact cap index \(e\in(0,1)\), its complete-color rate is
\[
 R_1(e,x)=\lambda(e)+I_{x,r}(e)-J(e),\qquad
 I_{x,r}(e)=\int_0^e\log|1-re^{-2\pi i(x+t)}|\,dt.           \tag{10}
\]
This uses the original coherent coefficient \(H_N\), not its separate
Newton summands. For \(e\le.27\),
\(\partial_x I_{x,r}(e)\le0\), since
\(\sin(\pi e)\sin\pi(2x+e)\le0\). Its old lower-cut comparison
therefore persists. For \(e\ge.49\),
\[
 \partial_e R_1=\lambda'(e)-J'(e)
                    +\log|1-re^{-2\pi i(x+e)}|<0.           \tag{11}
\]
Indeed the first difference is less than \(-6/5\) on
\([.49,.5]\) and at most \(-\log4\) above one half. The last
term is at most \(\log(1+r)<3/4\); the witness
\(e^{3/4}>269/128>83/40>1+r\) proves the latter inequality.
Thus the compact upper tail reduces to the current right real cut.

The true cap ends require their literal finite bounds. The lower end
is bounded exactly as in Section 4 of
[the lower-right cap theorem](research_mixed_first_four_cap_lower_right_horizontal.md),
replacing \(2^i\) by \((1+r)^i\). Its entropy tends uniformly to zero
as \(i/N\to0\), so a fixed sufficiently small end width gives a rate
less than \(1/4\). At \(i=N-1-k\), the exact unit-disk estimate there is
\(|p_i(X)|/|P_i|\le2^k\) for \(|X|\le1\). The polynomial has degree
\(i\), hence the reciprocal maximum principle gives on \(|X|=r\)
\[
 |p_i(X)|/|P_i|\le r^i2^k.
\]
The unchanged complete coefficient estimate then bounds the type-four
row by \(r^i4^kN^{-1}\sum_l|e_l(w)|\). Choose a fixed end width with
\(b_2+\delta\log4<3/5\), using the original \(b_2<73/125\).
The upper-end rate is less than \(3/5+\log r<E_*\).
Both arguments are uniform in all real colors and both parities.

We have proved the complete cap estimate
\[
 |U_{1,N}(w,X)|\le C_\tau N^{A_\tau}
                        e^{N(\mathcal A_L+\tau)}.          \tag{12}
\]
This is a sourcewise upper bound, not a relative cap asymptotic.

## 4. Joint physical rows keep the calibrated rate

Keep the exact ordinary physical-row rate
\[
 E(t;a,b)=I_{x,r}(t)+I_{z,e^{2\pi d}}(t)-3J(t)-2\pi Ht,
                    \qquad0\le t\le1.                     \tag{13}
\]
In particular the last row includes its incoming chirp. Set
\(N_t=|1-re^{-2\pi i(x+t)}|\le1+r\). For a fixed cap point,
the joint derivative for the larger Fourier branch \(W_0\) is
\(\log(N_eN_t/D^2)\).

First let \(\eta\le0\), so \(0<q\le1\). If
\(1/2\le x\le13/20\), the angle bounds already proved in
[the physical-row theorem](research_mixed_initial44_lower_right_physical_rows.md)
give
\[
 D^2>1+r^2+7r/6,\qquad N_e^2<1+r^2-r/4.
\]
The numerator bound follows by convexity in \(q\in[0,1]\), and its
endpoint at one exceeds its endpoint at zero. The squared difference,
divided by \(r\), is exactly
\[
 7/12+(67/36)r+(7/12)r^2>0.                                \tag{14}
\]
If \(13/20\le x\le7/10\), use instead
\[
 D^2>1+r^2+8r/13,\qquad N_e^2<1+r^2-18r/25.
\]
The corresponding difference divided by \(r\) is
\[
 -(16/325)(1+r^2)+(64/169+36/25)r>0.                       \tag{15}
\]
For a simple witness, \(1+r^2<11/5\), \(r\ge1\), and the positive
coefficient exceeds one, whereas \(176/1625<1\).
Equations (14)--(15) prove \(N_e(1+r)<D^2\). Thus every cap main
point, real cut, lower alias, lower weighted side and unweighted join
contracts jointly with every fixed physical ordinary row.

The upper horizontal cap alias is treated separately. Its bare rate
decreases by (9). Any physical ordinary row can increase by at most
\[
\begin{split}
 \int_{1/2}^{x}\log\frac{1+r}{D(v)}\,dv
 &\le\int_0^{1/5}\log\sec(\pi v)\,dv
 <\frac{3}{175}<\frac1{50}.
\end{split}
\tag{16}
\]
Here \(D(v)^2=(1+r)^2-4r\sin^2\pi(v-1/2)\), and
\(4r/(1+r)^2\le1\). For \(0\le y\le\pi/5<2/3\),
\(\tan y\le y/(1-y^2/2)\le9y/7\). Integrating this inequality
twice gives the upper bound \(3\pi^2/1750<3/175\).
The old upper-alias reserve \(1/50\) in Section 2 therefore pays
the entire cost, with a remaining reserve greater than \(1/350\).

The upper weighted vertical cap pieces reduce to their real cuts
at the current \(x\); this avoids assuming the sign of (14) for
positive private height. The exact canonical identity of the
[cap-alias theorem](research_mixed_selected_cap_alias_transport.md) is
\(\Im\Psi_e=A(e+a)+T(e)\), with
\(T>\pi(2u-1)\), \(T<14\pi/25\). After the numerator wall,
the corresponding negative height derivative of the upper rate is
\[
 A(u+x-1,\eta+H)-2\pi\mathbf1_{\{\eta+H>0\}}+T(e).       \tag{17}
\]
For \(\eta\ge0\), its prewall lower bound is \(-2\pi x\).
After the wall, \(A\ge\pi/2-\pi(u+x-1)\), so its lower bound
is \(\pi(u-x-3/2)\ge-193\pi/100>-2\pi\).
Thus \(\partial_\eta(\widehat\Psi-2\pi\eta)<0\), paying each
whole upper weighted side by its real cut. At kinks integrate the
continuous one-sided bounds. The lower weighted pieces already
belong to the nonpositive-private-height comparison above. No cap
vertical term has been omitted.

The omitted compact physical cap rows also require joint transport,
rather than (12) alone. For \(.08\le e\le.27\), the proof of
(8b) in the physical-row theorem gives \(N_e(1+r)<D^2\): its only
radial premise is \(k=4r/(1+r)^2\ge15/16\), which holds here since
\(((r-1)/(r+1))^2<9/6400<1/16\). All its real-angle intervals and
written concave-polynomial witnesses are unchanged. Below \(.08\),
the same source gives \(\lambda'-J'>13/100\), and \(N_e>1\) because
\(x+e\in[.5,.78]\), \(\cos2\pi(x+e)<1/5\), \(r>1\).
Thus these cap rows increase to the current \(.08\) row. Upper cap
rows reduce by (11) to the right cut. This covers the entire compact
cap physical tail against each ordinary row.

For the true cap ends, the constant ceiling (6) is unchanged. Their
joint derivative is \(\log(N_t/D)\); its total increase is bounded
by (16). This is smaller than the old \(53/500\) reserve in Section 2.
One may retain, for example, a reserve \(1/20\) after this comparison
and arbitrarily small collar tolerances.

Consequently all low rows \(0\le j\le\lfloor2N/25\rfloor\), high
rows \(\lceil N/2\rceil\le j<N\), and the real cuts tending to
\(.08,.5\), multiplied by the whole cap and the exact weights, have
rate at most \(\Lambda(z)-\gamma_0+\tau\). The compact half collar
is chosen once by uniform continuity of the integrated zero-safe
rates. Its small debit can be included in \(\tau\). There is no
finite-row replacement by a stationary index.

## 5. The original conditional critical point and its calibration

The [positive-incoming action theorem](research_mixed_four_conditional_positive_incoming_action.md)
applies on (1). It gives the same unique simple upper root of
\[
 (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0,
 \qquad s_*=(\Log v)/(2\pi i),\quad Q_s(s_*)=0,
\]
with \(0<\Re s_*<1-x\), the original zero lift, and
\[
 \Theta(a,b)=Q(s_*;a,b),\qquad \partial_x\Re\Theta<0.       \tag{18}
\]
The following explicit bounds license the finite contour used below:
\[
 1/5<|v|<2,\qquad 2/25<\Re s_*<1-x,
               |\Im s_*|<H_*:=\log5/(2\pi).               \tag{19}
\]

For the first lower bound, divide the cubic and its reciprocal by
their leading coefficients. Since \(|1-X|>|X|>1\), the original
coefficient bounds \(3,4,1\), and reciprocal bounds at most four,
still give \(1/5<|v|<5\). If \(|v|\ge2\), the incoming logarithm
has argument of modulus less than \(\pi/5\):
\(|X/v|<43/80<7/12<\sin(\pi/5)\). The outgoing logarithm and the
own logarithm have argument moduli at most \(\pi/6\), with total
multiplicity four. Hence \(\Im Q_s\ge\pi-\pi/5-4\pi/6=2\pi/15>0\),
contrary to the zero lift. This proves \(|v|<2\).

For \(u=\Re s_*\le2/25\), put \(U=e^{2\pi\Im s_*}>1/2\),
\(T=1/r\in(9/10,1)\). If \(U\ge8/5\), the argument comparison
in Section 5 of
[the lower-output reduction](research_mixed_conditional_lower_output_middle_reduction.md)
still gives \(\Im Q_s<-\pi/50\): it uses the incoming angle's
nonpositive argument, not the sign of its height. For
\(1/2<U<8/5\), its exact squared-force formula instead gives
\[
 |e^{Q_s}|^2>
 \frac{(22/25)(24/25)}{(5/6)^3}>1.                         \tag{20}
\]
The first numerator is greater than
\(T^2+U^2-2TU/5>22/25\); both derivatives of this quadratic are
positive on the indicated box. The second numerator and own
denominator are exactly the original \(24/25\) and \(5/6\) bounds.
This contradicts \(Q_s=0\), proving (19).

The same prewall proof gives
\[
 \Re Q_{ss}<0\quad(2/25\le\Re s<1-x,\ |\Im s|\le H_*).  \tag{21}
\]
Its incoming cotangent is nonpositive independently of the incoming
height. The outgoing-positive case uses only \(z\ge.22\) and
\(\cosh(2\pi\Im s)\le13/5\); all the original estimates remain.
The compact actual family gives uniform strict critical separations.

At \(a=a_L\), (7) extends down to \(v=2/25\). Indeed on
\([2/25,1/8]\) at height \(h_s\), the two shifted cosines are
negative, \(U=e^{2\pi h_s}>1/2\), and \(T>9/10\). The first
squared force numerator exceeds \(T^2+U^2>1\), the second exceeds
one, while the own squared modulus is less than \(3/5\). Therefore
the real profile increases to the already paid left cut.

For \(|\sigma|\le H_*\), let
\(m(\sigma)=\max_{2/25\le u\le1/2}\Re Q(u+i\sigma;a_L,b)\),
using its continuous prewall limit at the upper endpoint.
Each such height profile is convex by (21); the boundary limit and
their maximum are convex as well. At height \(\Im s_*(a_L,b)\),
the unique interior maximum is stationary in both real directions,
so \(m'\) vanishes. Thus this height minimizes \(m\). Comparing
with the actual old private height \(h_s\) and using (7) yields
\[
 \mathcal A_L+\Re\Theta(a_L,b)-\tfrac12\Re g(b)
                         \le\Lambda(z)-\gamma_0.          \tag{22}
\]
The monotonicity (18), together with the full cap bound (12), pays
the conditional critical exponential on every target (1). This is
not yet a replacement of the finite conditional sum by that exponent.

## 6. The whole critical-height line and both unweighted joins

On the postwall interval \(1-x\le t\le1/2\), set
\(U=e^{2\pi\Im s_*}>1/2\), \(R=|Y|\le1\). The exact horizontal
force of the two-branch rate is
\[
 e^{2\partial_t\widehat R}=
 \frac{|T-Ue^{-2\pi i(x+t)}|^2|1-RUe^{-2\pi i(z+t)}|^2}
 {|1-Ue^{-2\pi it}|^6}
 \le\frac{(U^2+1)(1+U)^2}{(U^2+3U/5+1)^3}<1.             \tag{23}
\]
Here \(T<1\), \(\cos2\pi(x+t)>3/10\), and
\(\cos2\pi t<-3/10\). The denominator minus numerator is
\[
 U^6+\frac95U^5+\frac{77}{25}U^4+
       \frac{227}{125}U^3+\frac{52}{25}U^2-\frac15U>0,
\]
since its last two terms are positive for \(U\ge1/2\).
The extra period rate is independent of \(t\). With (21), this
proves that the whole critical-height horizontal has its unique
maximum at \(s_*\), including the continuous numerator-wall values.

Keep the exact half-grid cuts
\[
 L_N=\lfloor2N/25\rfloor+1,\quad M_N=\lceil N/2\rceil,
 \quad\ell_N=(L_N-1/2)/N,\quad b_N=(M_N-1/2)/N.             \tag{24}
\]
Small cut displacements cost an arbitrary uniform rate allowance.
The left unweighted connector from zero to height \(\Im s_*\) is
bounded by its endpoints, by (21) and vertical convexity. At the
limiting right cut \(t=1/2\), put \(\eta=-H<0\). The original
[two-branch argument comparison](research_mixed_conditional_lower_output_gaussian_deformation.md),
Section 3, gives
\[
 \partial_\sigma\widehat R(1/2,\sigma)
 \le-2\pi(x-z)<0\quad(\sigma<\eta),\qquad
 \partial_\sigma\widehat R(1/2,\sigma)\ge0
                                      \quad(\sigma>\eta).  \tag{25}
\]
Below \(\eta\) the shifted incoming argument is nonnegative, the
own argument is zero, and the outgoing argument is at least
\(-2\pi z\). Above \(\eta\), the incoming argument is at most
\(\pi-2\pi(x-1/2)\), the outgoing argument is nonpositive, and
the period branch contributes \(+2\pi\). These statements do not
require \(\eta\ge0\). The rate therefore has no interior maximum
on the segment between zero and the critical height. Uniform
continuity transfers this to the actual even and odd half cuts.

Both real endpoints are paid by Section 4; both critical-height
endpoints are paid by (22)--(23) and (12). The exact identity is
\[
 \int_{\ell_N}^{b_N}T_N(s)\,ds
 =\int_{\ell_N}^{\ell_N+i\Im s_*}T_N(s)\,ds
 +\int_{\ell_N+i\Im s_*}^{b_N+i\Im s_*}T_N(s)\,ds
 +\int_{b_N+i\Im s_*}^{b_N}T_N(s)\,ds.                    \tag{26}
\]
All three terms keep the original positive multiplier \(N\).

## 7. Exact finite interpolation and all six weighted currents

Use the exact normalization of the
[joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md):
\[
 \Pi_N(q)=G_N(Nq)
  \exp\!\left\{\frac{\pi i}{2}[N(q-q^2)-q]\right\},
 \qquad E_N(q)=\Pi_N(q)^{-1}\quad(0<\Re q<1).
\]
Here \(G_N\) is the original sine-factorial interpolation, with
its marked recurrence and reflection identity; \(E_N\) elsewhere
denotes its proved reciprocal continuation. The interpolant is
the original holomorphic function
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(b+s)
                         E_N(a)E_N(b)E_N(s)^3.              \tag{27}
\]
The numerator chart is holomorphic on \(\Re q>-1/N\), and the
reciprocal chart on \(\Re q<1\). Thus (27) is holomorphic on the
rectangle with cuts (24) and any fixed finite heights. The only
numerator wall is \(a+s=1\). The exact period multiplier, reflection
identity and the
[reciprocal-midpoint bound](research_uniform_factorial_and_boundary_decay.md)
give the zero-safe estimate
\[
 |T_N(t+i\sigma)|\le C_{\tau,Y_0}N^{A_{\tau,Y_0}}
                         e^{N(\widehat R(t,\sigma)+\tau)}    \tag{28}
\]
on every fixed height rectangle \(|\sigma|\le Y_0\), where
\[
 \widehat R=\mathfrak p(a+t+i\sigma)+
 \Re\{g(b+t+i\sigma)-3g(t+i\sigma)-g(a)-g(b)
                                      +2\pi ia(t+i\sigma)\}.
\]
This is the same arbitrary-fixed-height proof in Section 2 of
[the lower-right complete source](research_mixed_initial44_lower_right_complete_pair.md).
It does not assert a nonzero symbol at a numerator zero.

The upper rate has the global slope bounds
\[
 \partial_\sigma\widehat R\le9\pi/5\quad(\sigma\ge0),
 \qquad
 \partial_\sigma\widehat R\ge-19\pi/10\quad(\sigma\le0).
                                                               \tag{29}
\]
Before the wall, the original argument proof uses no incoming-height
sign: its incoming real argument exceeds one half, so that argument
is nonpositive at all heights. The upper estimate uses the global
strip bound and the own argument at \(\sigma\ge0\). After the wall,
every \(\sigma\ge0\) is above \(\eta=-H\), so the old upper-branch
calculation applies. For \(\sigma\le\eta\), its lower calculation
applies unchanged. In the additional range \(\eta<\sigma\le0\),
the incoming argument is at most \(\pi\), the negative outgoing and
own contributions are nonnegative, and the period supplies \(2\pi\).
Thus its lower derivative is at least
\(-\pi-2\pi x+2\pi\ge-2\pi/5\), stronger than (29).
Integrate the one-sided inequalities at the continuous kink.

The exact cotangent split is
\[
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
 =N\int_{\ell_N}^{b_N}T_N(t)\,dt+
 \frac N{2i}\left\{
 \int_{\partial R^+}T_N(\cot\pi Ns+i)\,ds+
 \int_{\partial R^-}T_N(\cot\pi Ns-i)\,ds\right\}.         \tag{30}
\]
The two half-boundaries omit their real segments and retain the
original induced orientations. There are four weighted vertical
half-sides and two horizontal aliases. Their kernels have bounds
\(2e^{-2\pi N|\sigma|}\) on the half-grid verticals, and the same
bound with constant four on fixed outer horizontals. Equation (29)
pays every vertical by its real cut with extra loss at least
\(\pi|\sigma|/10\). Section 4 pays those cuts with the whole cap.

For the two horizontal aliases choose one sufficiently tall fixed
height \(Y_0>2\). More explicitly, compactness makes
\[
 C_*:=\sup\{\mathcal A_L+\widehat R(t,0)-\tfrac12\Re g(b)
                      -\Lambda(z)+2\gamma_0}<\infty,
                       \qquad3/40\le t\le1/2.
\]
Choose \(\pi Y_0/10>C_*+1\), before \(N\). This is an existence
choice, not an evaluation of a supremum. Equations (28)--(29) and
the complete cap bound (12) then put both horizontal aliases below
\(\Lambda(z)-2\gamma_0-1\). Arbitrarily large but fixed finite
heights are licensed by the exact charts and the midpoint bounds.

Add all original physical rows from Section 4, the six weighted
currents (30), and the three unweighted pieces (26). Each group
has the calibrated rate \(\Lambda(z)-\gamma_0\), up to its prescribed
total allowance and polynomial factors. Sharing the strict reserves,
cut tolerances and symbol errors proves (4). This is a complete upper
bound for the finite product (2), not a relative conditional packet.

The complete-color estimates were used before taking any cap modulus.
The literal product has degree less than \(N\) in the ordinary color.
Polynomial continuation from its full real interval adds an arbitrarily
small rate allowance on a fixed ellipse and hence on small disks;
Cauchy estimates give fixed derivatives on smaller disks. The outgoing
halfweight is a constant multiplier in this argument, including at
its zeros. It is never differentiated transversely or divided out.
All \(N\) factors, original outside scalars and both parity-dependent
half-grid cuts remain unchanged.

The theorem ends at \(7/10+i/100\). Its downward connection, the
subsequent right arc, the full first period and arbitrary later
departures remain separate statements.

## 8. A reusable complete conditional-source bound across both heights

The conditional part of the proof admits the following independent
finite-source statement. It imposes no cap calibration at an
intermediate incoming height.

**Proposition 2.** On the compact parameter family
\[
 a=x+ih,\quad \frac12\le x\le\frac7{10},\quad
 -\frac{39}{500}\le h\le\frac1{100},\qquad
 b=z+id,\quad \frac{11}{50}\le z\le\frac9{20},\quad
 -\frac{51}{500}\le d\le-\frac1{1000},
 \tag{31}
\]
use the same original critical action \(\Theta(a,b)\), and the
literal physical-row rate
\[
 E_h(t)=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv
       +\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv
       -3J(t)-2\pi ht .
 \tag{32}
\]
Define the continuous finite number
\[
 \mathcal M(a,b)=
 \max\left\{\Re\Theta(a,b),\
       \max_{t\in[0,\,2/25]\cup[1/2,\,1]}E_h(t)\right\}.
 \tag{33}
\]
For each \(\tau>0\), the entire conditional polynomial satisfies
\[
 |C_{1,N}(e^{-2\pi ia},e^{-2\pi ib})|
 \le C_\tau N^{A_\tau}e^{N\{\mathcal M(a,b)+\tau\}},
 \tag{34}
\]
uniformly on (31), at both parities. The original decomposition
keeps the low and high finite blocks, the critical horizontal,
both unweighted connectors and all six weighted currents.
For any prescribed constant \(B>0\), the two outer horizontal
aliases can additionally be given rate at most
\(\mathcal M(a,b)-B+\tau\) by one sufficiently tall fixed
rectangle. No coefficient or period factor is divided out.

*Proof.* The adopted enlarged algebraic domain contains (31).
Here \(3/5<|X|<43/40\), so the monic and reciprocal cubic
coefficient bounds in Section 5 still give \(1/5<|v|<5\).
The argument excluding \(|v|\ge2\) is unchanged. Put
\(T=e^{-2\pi h}\); then \(9/10<T<5/3\). In the small-real-root
test with \(1/2<U<8/5\), both partial derivatives of
\(T^2+U^2-2TU/5\) remain positive on this larger box:
\[
 2T-\tfrac25U>\tfrac95-\tfrac{16}{25}>0,\qquad
 2U-\tfrac25T>1-\tfrac23>0.
 \tag{35}
\]
Thus the same lower bound \(22/25\) applies. For \(U\ge8/5\)
the original argument exclusion never used the incoming height
sign. This proves the strict critical strip (19) on all of (31).
The prewall concavity (21) uses only the incoming real argument
and the unchanged outgoing bounds, so it also persists.

For the postwall horizontal, if \(T\le1\), use (23).
If \(1\le T<5/3\), use the three written polynomial inequalities
(19)--(21) in Section 4 of the
[complete lower-right source](research_mixed_initial44_lower_right_complete_pair.md):
they cover \(U\ge1\), and the two intervals
\(t\in[3/10,7/20]\), \(t\in[7/20,1/2]\) when \(1/2\le U\le1\).
Their proof depends on \(T\), the same real-angle bounds and
\(|Y|\le1\), not on any cap reference or affine action comparison.
Hence the whole critical-height horizontal is bounded by
\(\Re\Theta\). Formula (25) applies with \(\eta=-h\) of either
sign. It pays the right unweighted side by its real and critical
endpoints; the left side uses the same prewall vertical convexity.

The global alias bounds (29) likewise hold on (31). If
\(\eta\ge0\), their postwall proof is exactly (13)--(14) of that
lower-right source. If \(\eta<0\), the only new range
\(\eta<\sigma\le0\) was checked explicitly in Section 7.
All regular prewall estimates depend only on the real argument
sign and the nonpositive outgoing height.
The four weighted verticals are therefore paid by their own
real-cut rates. The rates at the actual half-grid cuts tend
uniformly to \(E_h(2/25)\) and \(E_h(1/2)\).

All physical rows outside the cuts, including \(j=0,N-1\),
have the zero-safe bound with rate (32) and uniform
\(O(\log N)\) product error. This follows directly from the
uniform sine-factorial denominator bounds and the smoothed-log
upper bound for numerator products, as in the physical proof of
the selected half-face theorem. It remains valid at \(h=0\)
and at every numerator zero. Thus (33) pays both full end
blocks and both limiting real cuts.

The continuous integrated rates on (31) and
\(3/40\le t\le1/2\) are bounded. Choose a fixed \(Y_0>2\)
such that
\[
 \frac{\pi Y_0}{10}>
 B+1+\sup\{\widehat R(t,0)-\mathcal M(a,b)\}.
 \tag{36}
\]
The supremum is finite by compactness; it is neither evaluated
nor assigned a favorable sign. The zero-safe global factorial
charts hold at this fixed height. Consequently the two aliases
have the claimed extra loss \(B\). Adding the exact decomposition
(26), (30), and the two physical blocks proves (34), with the
original \(+N\) and \(N/(2i)\) multipliers. \(\square\)

Proposition 2 is an explicit complete-source ceiling. It does not
assert that \(\mathcal M\), multiplied by a moving cap or a Fourier
weight, lies below an original geometric affine rate at every
height in (31). Theorem 1 supplies that additional comparison
only on the selected horizontal (1).

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected44_right_half_interval.md | 50d7d9daaf5e33f45749b7c5ca9e2dba4fd0dca2298986d337cb58e35979ebc1 |
| research_mixed_four_conditional_positive_incoming_action.md | e8608019efbd73b2c05e6ede084b4781182259dc0e32be12b4610c66f352d371 |
| research_mixed_initial44_lower_right_complete_pair.md | 631492d2c8c6bec47e95ae6c84641429ba64256201fc7dd459aa403872a93f7b |
| research_mixed_initial44_lower_right_physical_rows.md | 6665075b979801c0d5b9296738508be527bddd8827e3aea004b9ff1e7a60f702 |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_selected_cap_alias_transport.md | f69fae6109da41fb6505daaa92d75ecaae6942bc088fe825aadbef94c158f4db |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| research_mixed_conditional_lower_output_gaussian_deformation.md | 41c5d0030a8c057c1858e3e89e66136359aa3a448f881aeea93d23cf70a48fe8 |
| research_mixed_cap_upper_target_extension.md | c705f72cbfaac8dc920ce48a4f6ea0402f15449f3ba4af202a04c5015cf2d46e |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_uniform_factorial_and_boundary_decay.md | 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The entire written proof and the directly used source implications
were read, and all fourteen source hashes were checked. No mathematical
numerical evaluation, saved-value arithmetic, test, import, compilation
or frozen-source edit was performed.
