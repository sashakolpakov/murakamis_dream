# The complete initial interval and left taper on the lower right shoulder

Private research proof, 8 November 2026. The moving real cut is
calibrated by transporting the outgoing coordinate at each fixed
incoming point. This avoids identifying the old real face with the
smaller face needed on the shoulder. The complete first cap and both
branches of the following conditional bound remain attached.
No numerical evaluation or alteration of a frozen source is used.

## 1. Original source and statement

Use the actual ordinary-next references and full allocation of
[the next shoulder block](research_mixed_next_lower_right_shoulder_next_block.md),
Section 1. In particular
\[
(a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_y=\Im y_*,
\]
\[
.278\le\Re a_*\le.391,\quad -.072<h_a<0,\quad
-.102<h_s,h_y<-.001,\quad .24<\alpha:=\Re y_*<.36 .
\tag{1}
\]
Both vertices after the ordinary first cap are ordinary. Their
flags are \((0,1,\beta)\), \(\beta=0,1\). Put \(P=[.22,.45]\)
and retain independent targets
\[
y=q+ih_y,\quad .45\le q\le.5,\qquad
z=u+i\Im z_*,\quad u\in P .
\tag{2}
\]
The two incoming paths, in positive order, are
\[
\Gamma_{\mathrm I}=[0,.1],\qquad
a(x)=x+ih_a(x-.1)/.12,\quad .1\le x\le.22 .
\tag{3}
\]
Write \(X=e^{-2\pi ia},Y=e^{-2\pi iy},Z=e^{-2\pi iz}\).
The literal source is
\[
\begin{split}
U_{0,N}(w,X)&=\sum_{k<N}H_N(w,r^{-k})\,p_k(X)/P_k,\\
C_{1,N}(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
C_{\beta,N}(Y,Z)&=\sum_{j<N}Y^{-j}p_j(Y)p_j(Z)/P_j^{2+\beta},
\end{split}
\qquad
r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j .
\tag{4}
\]
The Fourier polynomial is the original \(d_N(r^b)=P_b^{-1}\).
There is no selected factor \(Y^{-N}\).

Keep the original phases and their original logarithmic lifts:
\[
Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,\qquad
F=Q-\tfrac12g(y).
\tag{5}
\]
Let \(A_*,p,\mathcal B(q,u),\mathcal L(q,u),\Lambda_{123}(z)\)
be exactly those of the next-block theorem. Thus
\[
A_*+p(q-\alpha)+\mathcal B(q,u)=\Lambda_{123}(z),\qquad
p>-21/20,
\tag{6}
\]
\[
\mathcal L(q,u)=-2\pi h_y+2\pi(\Im z_*)_+
                 -\tfrac12\Re g(y)-\tfrac\beta2\Re g(z).
\tag{7}
\]
The complete next source has the two-rate bound
\[
|C_{\beta,N}(Y,Z)|\,|d_N(Y)|^{1/2}|d_N(Z)|^{\beta/2}
\le C_\tau N^{B_\tau}
\left(e^{N(\mathcal B-10^{-9}+\tau)}
      +e^{N(\mathcal L+\tau)}\right).
\tag{8}
\]
This is its equation (22), with both terms retained.

**Theorem.** For all sufficiently large levels of both parities,
uniformly on (1)--(3) and for every real ordinary color
\(w\in[-2,2]\),
\[
|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{\beta,N}(Y,Z)|
             |d_N(Z)|^{\beta/2}
\le C N^B e^{N(\Lambda_{123}(z)-10^{-11})}.
\tag{9}
\]
The same rate, with polynomial cost, bounds each integral on
(3) with its original measure \(+N\,da\). Fixed real-color
derivatives are included. On sufficiently small fixed neighborhoods
of complete color and the actual output \(z_*\), the unweighted
integrals normalized by the original next action have every fixed
normalized mixed derivative bounded with gap \(10^{-12}\).
The outgoing halfweight is removed only there by its original
nonzero packet.

This theorem concerns the two incoming pieces (3). It neither
estimates the selected upper arcs nor asserts a standalone plane
for the next kernel's last row.

## 2. The actual shifted lower face

On the taper put
\[
\sigma(x)=39/400+x/8,\qquad
\ell(x,q)=\sigma(x)+.45-q .
\tag{10}
\]
Then \(3/50\le\ell\le1/8\) and
\[
x+\ell\ge4/25,\qquad .56\le q+\ell\le.575.
\tag{11}
\]
At the initial endpoint \(x=.1\), the cut is
\(\ell_{\mathrm I}(q)=.56-q\in[.06,.11]\).

At \(q_0=.45\), \(\ell(x,q_0)=\sigma(x)\). The full-plateau
[left-taper theorem](research_mixed_next_unselected_incoming_left_taper.md),
equation (13), pays this real face **at each fixed \(x\)**:
\[
\mathcal E_U(x)+\Re F(\sigma(x);a(x),q_0+ih_y)
\le A_*+p(q_0-\alpha)-1/2000.
\tag{12}
\]
Here \(\mathcal E_U\) is the complete cap envelope used in that
proof: all compact physical tails, retained private main and cut
profiles, inactive private aliases and explicit true-end alternative
are included. Its all-real-color source is retained unchanged.
No bound for an individual profile is inferred from a signed sum.

For fixed \(x\), differentiate (5) along \(s=\ell(x,q)\).
The chirp combines with the first numerator to give exactly
\[
\frac d{dq}\Re F(\ell(x,q);a(x),y)
=3\log(2\sin\pi\ell)
-\log|e^{-2\pi\Im a(x)}-e^{-2\pi i(x+\ell)}|
-\tfrac32\log|1-Y|.
\tag{13}
\]
The original radius and angle witnesses in the
[central-prefix shoulder theorem](research_mixed_next_lower_right_shoulder_central_prefix.md),
equations (14)--(15), give
\[
|1-Y|>3/2,\qquad |1+Y|<3/5.
\tag{14}
\]
Since \(e^{-2\pi\Im a(x)}\ge1\), the middle modulus in (13)
is at least \(2\sin\pi(x+\ell)>23/24\).
Indeed \(x+\ell\in[.16,.345]\), \(4\pi/25>1/2\), and
\(2\sin(1/2)>2(1/2-1/48)=23/24\).
Also \(2\sin(\pi/8)<4/5\), \(\log(5/4)>1/5\),
\(\log(3/2)>2/5\), and \(\log(24/23)<1/23\).
Consequently
\[
\frac d{dq}\Re F(\ell;a,y)
<-\frac65+\frac1{23}=-\frac{133}{115}<-\frac{21}{20}<p .
\tag{15}
\]
Integrating at this fixed \(x\) proves (12) with \(q_0,\sigma\)
replaced by \(q,\ell\). This is the needed real-face calibration;
no new derivative along the taper is required.

The half-row face is likewise transported from its old \(q_0\)
calibration, since
\[
\partial_q\Re F(1/2;a,y)
=\log|1+Y|-\tfrac32\log|1-Y|<-11/10<p .
\tag{16}
\]
Its \(1/2000\) deficit is preserved.

All physical rows below \(\ell\) reduce to that face. At real
\(0<t\le\ell\), put \(B=e^{-2\pi\Im a(x)}\ge1\) and
\(R=e^{2\pi h_y}>1/2\). The incoming modulus exceeds
\(2\sin\pi t\), because \(t<x+t<1/2\), and the outgoing
modulus exceeds one because \(q+t\in[.45,.625]\). Hence
\[
e^{\partial_t\Re Q}
=\frac{|B-e^{-2\pi i(x+t)}|\,|1-Re^{-2\pi i(q+t)}|}
{(2\sin\pi t)^3}>(2\sin\pi t)^{-2}>1 .
\tag{17}
\]
The rate increases from its continuous value zero; the exact
zero row and all possible numerator zeros remain in the finite
upper estimate.

## 3. Main profiles and the complete upper physical rows

For \(\ell\le v\le.15\) at the fixed negative height \(h_s\),
put \(r_s=e^{2\pi h_s}\le1\). The exact force is
\[
e^{\Re Q_s}
=\frac{|B-r_se^{-2\pi i(x+v)}|\,
       |1-Rr_se^{-2\pi i(q+v)}|}
{|1-r_se^{-2\pi iv}|^3}>1 .
\tag{18}
\]
The incoming modulus is at least the own modulus: its square
increases with \(B\ge1\), and
\(\cos2\pi(x+v)<\cos2\pi v\) here.
The second numerator exceeds one since \(.56\le q+v\le.65\).
The own squared modulus is less than one since
\(\cos2\pi v\ge\cos(3\pi/10)>1/2\).
Thus all added main profiles are bounded by the profile at
\(.15+ih_s\), at the same \(x,q\).

For \(.15\le v\le.5\), the original profilewise incoming
transport from
[the completed following taper](research_mixed_three_four_following_left_taper_source.md),
Section 3, is independent of \(y\). It transports each cap/main
profile to \(x=.22\), before a maximum is taken. The true-end
alternative has its same nonnegative transport derivative.
At \(x=.22\) the central-prefix shoulder theorem, equation (10),
gives
\[
\mathcal E_U(x)+\Re F(v+ih_s;a(x),y)
\le A_*+p(q-\alpha)-3\cdot10^{-9},
\qquad .15\le v\le.5 .
\tag{19}
\]
Equation (18) covers the added smaller indices. All original
private cap currents remain covered by this envelope.

For clarity, the full upper physical comparison requires an
extension of the old taper's outgoing-angle bound. Write
\[
f_R(t)=\log|1-Re^{-2\pi it}|,\quad
J(v)=\int_0^v\log(2\sin\pi t)\,dt,\quad
R_a=e^{2\pi\Im a(x)},\quad \delta=-\log R_a .
\]
The literal real rate satisfies \(E(1)=\delta\), and reflection
gives exactly
\[
\mathscr F(v):=E(1-v)-E(1)
=-\int_{x-v}^{x}f_{R_a}(t)\,dt
 -\int_{q-v}^{q}f_R(t)\,dt+3J(v)-\delta v .
\tag{20}
\]
Here \(5/8<R_a\le1\), so \(T=R_a^{-1}<8/5\).

If \(0<v\le9/40\), the outgoing integral in (20) is positive:
its interval lies in \([9/40,1/2]\), where \(R>1/2\) and
\(|1-Re^{-2\pi it}|>1\). The centered-arc inequality from the
original physical-row theorem gives
\(\int_{x-v}^x f_{R_a}\ge2J(v/2)\). Therefore
\[
\mathscr F(v)\le3J(v)-2J(v/2)-\delta v
\le v\{\log(8\pi^2v^2)-2\}<0 .
\tag{21}
\]
The last written witness uses \(v<1/4,\pi^2<10,e^2>5\);
it is the same inequality as
[the initial shoulder rows](research_mixed_next_initial_right_shoulder_rows.md),
equation (6).

For \(9/40\le v\le1/2\), let \(S(v)=2\sin\pi v\). Away
from integrable numerator zeros,
\[
e^{\mathscr F'(v)}
=\frac{S(v)^3}
{|T-e^{-2\pi i(x-v)}|\,|1-Re^{-2\pi i(q-v)}|}>1 .
\tag{22}
\]
Here are full interval witnesses:

* On \([9/40,1/4]\), the two squared moduli are at most
  \(303/175\) and \(81/35\). Use
  \(|x-v|\le3/20,\ \cos(3\pi/10)>4/7\), and
  \(|q-v|\le11/40\), so the second square is at most
  \(2+2\sin(\pi/20)<2+\pi/10<81/35\).
  In contrast \(S(v)^2>59/35\), and
  \(59^3=205379>171801=7\cdot303\cdot81\).
* On \([1/4,7/20]\), the squared moduli are at most
  \(89/25\) and \(2\), whereas \(S(v)^6\ge8>178/25\).
* On \([7/20,1/2]\), the moduli are at most \(13/5\) and
  \(2\), whereas \(S(v)^3>(7/4)^3>26/5\).

The first and last trigonometric guards are those already
written in the old taper, equation (18). Equations (21)--(22)
give the full endpoint reduction
\[
\max_{1/2\le t\le1}E(t)=\max\{E(1/2),E(1)\}.
\tag{23}
\]
Uniform zero-safe sine-product estimates yield the corresponding
positive sum bound with polynomial cost and arbitrarily small
rate tolerance. This includes the even half row, the first odd
row, and every revived or zero row.
The half branch was paid in (16). The last branch, with the
complete cap disk bound, has raw prefix ceiling
\[
b_0+c_{\rm b}+\delta
<101/125+13/40+18\pi/125<2383/1500 .
\tag{24}
\]
Its full remaining allocation will be paid in Section 5.

## 4. Every central conditional current on the taper

Use real half-grid cuts corresponding to \(\ell(x,q)\) and
\(1/2\), the original main height \(h_s\), and alias heights
\(-1/5,8\). On the part with real index at most \(3/20\),
[the shoulder taper current theorem](research_mixed_next_right_shoulder_taper_upper_currents.md)
proves, on the exact canonical interpolant,
\[
\Re Q_{ss}<0\quad(\Im s\ge h_s),\qquad
\Im Q_s<9\pi/10\quad(\Im s\le0),\qquad
\Im Q_s>-47\pi/25\quad(\Im s\ge h_s).
\tag{25}
\]
It pays both horizontal aliases relative to the same current
main profile, both weighted lower-cut sides by their real-cut
value, and the unweighted lower join by its two endpoints.
Its lower and upper horizontal losses are \(11\pi/50\) and
\(9603\pi/12500\), respectively.

For completeness the remaining real-index range
\(.15\le v\le.5\) retains the original argument proof.
On \(|\Im s|\le.12\), \(\cosh(2\pi\Im s)<4/3\).
Since \(q+v\ge.6\), its outgoing real cotangent is nonpositive.
The own and incoming terms then give strict
\(3\Re\cot\pi s-\Re\cot\pi(a+s)-\Re\cot\pi(y+s)>0\).
Explicit intervals verify uniformity. On \([.15,.175]\),
the own sine exceeds \(4/5\) and its cosine exceeds \(9/20\),
whereas the incoming cotangent is at most one.
On \([.175,.25]\) use the old bounds \(3C_s>9/5,C_{a+s}<1\).
On \([.25,.35]\) use \(3C_s>36/35,C_{a+s}<7/12\).
On \([.35,.4]\) use \(3C_s>9/14,C_{a+s}<1/6\).
On \([.4,.45]\), both shifted cotangents are nonpositive and
the own sine exceeds \(3/10\). On \([.45,.5]\), the incoming
shift has real part in \([.55,.72]\), sine less than \(-3/10\),
and height of modulus at most \(.192\). Its cosh is less than
two, so \(C_{a+s}<-1/10\). This also gives strict curvature
at \(v=q=.5\), using continuous one-sided values.

For heights below \(-.12\), the old radius/argument proof gives
\(\Im Q_s<257\pi/300<9\pi/10\), and this curvature transports
it through zero. At heights above \(.12\), the four-case
original argument bounds reduce, since \(q+v>.5\), to
\[
\Im Q_s/\pi>
\begin{cases}
-3/2+3v+x-2q,&x+v<.5,\\
-1+2v-2q,&x+v\ge.5 .
\end{cases}
\tag{26}
\]
Both exceed \(-39/20\) for \(v\ge.15,x\ge.1,q\le.5\).
Curvature transports this lower bound down through \(h_s\).
Consequently
\[
\begin{split}
\Re Q(v-i/5)-2\pi/5
 &<\Re Q(v+ih_s)-11\pi/50,\\
\Re Q(v+8i)-16\pi
 &<\Re Q(v+ih_s)-2011\pi/10000 .
\end{split}
\tag{27}
\]
The upper arithmetic is
\((39/20)(8+51/500)-16=-2011/10000\).
The weighted vertical profiles decrease away from their real
cuts. The unweighted joins are convex between \(h_s\) and zero,
and hence reduce to the real and main-height endpoints.

At the upper cut and \(q=.5\), the numerator \(y+s\) can equal
one. Use the exact reciprocal-factorial upper bound in
[the initial shoulder rows, Section 4](research_mixed_next_initial_right_shoulder_rows.md),
including both reflected terms and the \(O(\log N)\) half-grid
shift cost. No nonzero asymptotic symbol is used at that
divisor. The original continuous rates in (26)--(27) are
the limits from \(q<.5\); the argument jump at the zero is
downward in \(\Im Q_s\), consistent with the convex-height
upper envelope. No side or row is omitted there.

Equations (12)--(19), (23)--(27) now pay the complete first
prefix with its halfweight against
\(A_*+p(q-\alpha)\), with a common finite gap \(10^{-10}\),
except for the explicit raw-ceiling alternatives (24).
The bounds are made for individual current profiles before
their coherent sum. They can therefore retain (7) as well.

## 5. The next last-row branch and the raw-ceiling alternatives

For every fixed first-index profile with nonpositive height,
the \(q\)-dependent part after adding (7) to (5) is
\[
g(s+y)-2g(y).
\]
The exact comparison from the next-block theorem, equation (24),
therefore gives
\[
\partial_q\Re\{F(s;a,y)+\mathcal L(q,u)\}
<\log(3/4)<-1/4 .
\tag{28}
\]
The cap is independent of \(q\).
For main indices at least \(.15\), transport from \(q_0=.45\);
at that coordinate the original taper source and the original
next last-row certificate apply separately, with the unchanged
two incident halfweights and affine allocation. The first
profile already has its cap-displacement gap greater than
\(10^{-9}\); the other old supporting losses are nonnegative.
This proves a uniform gap below \(\Lambda_{123}\).
For smaller main indices use (18) at the same \(q\), keeping
the factor (7) attached.

On the moving real cut the additional halfweight changes (13)
to
\[
3\log(2\sin\pi\ell)
-\log|e^{-2\pi\Im a}-e^{-2\pi i(x+\ell)}|
-2\log|1-Y|<-\frac75+\frac1{23}<0 .
\tag{29}
\]
It is thus transported from the old paid face at each fixed
\(x\). The half row is covered by (28).
Positive first-index currents are **not** transported by (28).
They are reduced at the same \(q\) to the just-paid main and
real-cut profiles by (25)--(27), keeping (7) on both sides.
All four weighted pieces and both unweighted joins are included.

We also record how every raw prefix ceiling \(B\le2383/1500\)
is paid for both terms in (8). The central-prefix shoulder
theorem proves, using \(A_*>9/5\), that
\[
B-\tfrac12\Re g(y)
<A_*+p(q-\alpha)-1/50
\tag{30}
\]
on (2). Its proof retains the full unselected Fourier forcing
alternative; on this lower half-strip \(\Re g(y)\le0\).
Equation (30) pays the regular term in (8).
For its last-row term the complete rate is
\[
B-\Re g(y)-2\pi h_y+2\pi(\Im z_*)_+
-\tfrac\beta2\Re g(z).
\tag{31}
\]
At \(q_0=.45\) this is paid with the old generic-prefix
marginal reserve greater than \(1/50\), followed by the old
next last-row plane. Its derivative in \(q\) is
\(-\log|1-Y|<-\log(3/2)\), so that same reserve persists.
This covers (24) without making any plane assertion for the
unmultiplied next last row.

## 6. The complete initial interval

For \(0\le x\le.1\), use the fixed conditional cut
\(\ell_{\mathrm I}(q)=.56-q\), the half cut, main \(h_s\),
and alias heights \(-1/5,8\).
There is a fixed sufficiently small \(\rho>0\) on which the
complete source has raw prefix ceiling \(B<2383/1500\).
Indeed [the initial shoulder rows](research_mixed_next_initial_right_shoulder_rows.md),
equations (11)--(13), gives
\[
\sup_{|Y|\le1}|U_{0,N}(w,X)C_{1,N}(X,Y)|
\le C_\tau N^{B_\tau}
e^{N\{101/125+7/15+2\Omega(\delta)-\log(1-\delta)+\tau\}},
\tag{32}
\]
where \(|X-1|\le\delta\) and \(\Omega(\delta)\to0\).
Both branches are paid by (30)--(31); no narrower old
outgoing collar is imported.

On \([\rho,.1]\), retain the complete cap atlas of
[the original initial-interval theorem](research_mixed_next_unselected_incoming_initial_interval.md),
Section 3: its five central private profiles, all physical
tails, and the extra real profile
\(\max_{.49\le e\le.5}\{\lambda(e)+I_x(e)\}\).
At \(x=.1\) that extra profile clips to the original \(.49\)
real cut. No complex private packet beyond \(.49\) is assumed.
The separated true cap ends have rate \(3/5\). Multiplying
by the full initial-disk conditional bound gives their raw
prefix ceiling \(389/300<2383/1500\), again paid by (30)--(31).

For every remaining fixed cap state and every conditional
point \(s=v+i\eta\) on the full rectangle,
\[
\frac d{dx}\Re\{\Psi_0(e,x)+Q(v+i\eta;x,y)\}
=\log\frac{|1-e^{-2\pi i(e+x)}|\,
|e^{-2\pi\eta}-e^{-2\pi i(x+v)}|}
{(2\sin\pi x)^2}>\log(3/2).
\tag{33}
\]
This is the original incoming derivative, independent of \(y\).
Here is the needed extension down to \(v=.06\).
The first modulus exceeds one, since \(\Re(e+x)\in[.27,.6]\).
For \(x\le3/40\), the second modulus, minimized over its
nonnegative radius, exceeds \(\sin(3\pi/25)>9/25\).
The latter follows from
\(\sin(3/8)>3/8-(3/8)^3/6>9/25\).
Meanwhile
\[
(2\sin\pi x)^2<(3\pi/20)^2<(33/70)^2<9/40.
\]
The quotient is therefore greater than \(8/5\).
For \(x\ge3/40\), \(x+v\ge27/200\); whenever its cosine
is positive, its sine exceeds \(\sin(27\pi/100)>7/10\);
otherwise the modulus is at least one.
The denominator is less than \(2/5\), giving quotient
greater than \(7/4\). These arguments cover
\(.06\le v\le.5\), all intermediate heights on the sides,
and the extra real cap profile. Sampling penalties do not
depend on \(x\).

Thus each actual current profile transports to \(x=.1\),
where Sections 2--5 pay it, including the next last-row
factor. In particular every positive alias and joining side
is transported as its own profile; no signed endpoint sum
is used to bound it.

The low physical rows increase up to \(\ell_{\mathrm I}\):
for \(0<t\le.11\), \(t\le x+t<.5\) and
\(q+t\in[.45,.61]\), so the exact force exceeds
\((2\sin\pi t)^{-2}>1\).
The complete upper physical rows reduce to half and last
by the initial shoulder row theorem, equations (4)--(8).
Their last rate is exactly zero, so the complete cap disk
bound gives raw prefix ceiling \(519/500<2383/1500\).
This too is paid by (30)--(31). All initial rows are retained.

## 7. Exact finite assembly, measures and derivatives

On each taper point put
\[
L_N=\lceil N\ell(x,q)\rceil,\qquad M_N=\lceil N/2\rceil .
\]
On the initial interval use \(\ell_{\mathrm I}(q)\) instead.
The groups \(j<L_N\), \(L_N\le j<M_N\), and
\(M_N\le j<N\) partition the literal sum (4).
The outer groups were paid positively. On the middle group
the canonical interpolant is exactly
\[
e^{2\pi iNas}
\frac{\Pi_N(a+s)\Pi_N(y+s)}
{\Pi_N(a)\Pi_N(y)\Pi_N(s)^3}.
\tag{34}
\]
Its half-grid cuts differ from the stated real cuts by
\(O(1/N)\). The exact finite cotangent decomposition retains
the original \(+N\) main density, two horizontal Fourier
remainders, four weighted vertical pieces, and two unweighted
main joins. Sections 4 and 6 pay all of them.
The full cap has its own original finite decomposition and
all true-end and compact physical rows. It is never replaced
by a truncated color coefficient.

All factorial arguments stay in regular compact strips except
the explicitly treated numerator \(y+s=1\). At that divisor
the original zero-safe reciprocal estimate and its half-grid
shift bound apply. Thus the same strict profile bounds give
uniform finite bounds after arbitrarily small common source
tolerances and polynomial factors, at both parities.
No moving row partition is differentiated. At a cut jump
either adjacent exact partition has the same bound.

Combine the regular next branch (8) with (19), the transported
real cuts, and (30). Combine its last branch with (28)--(29)
and (31). The original shared Fourier halves, both forcing
alternatives and all next physical/current terms remain.
All smallest raw reserves exceed \(10^{-9}\); choosing the
finite tolerances within these reserves proves (9).
The original integrations are \(+N\,dx\) and
\(+N a'(x)\,dx\), with bounded path length and Jacobian.

The complete all-real-color cap estimates and Markov's
inequality give fixed real-color derivatives. For local
mixed derivatives hold every path and integer cut fixed
at its base reference and apply the zero-safe finite bounds
to the integer-weight holomorphic square
\[
(U_{0,N}C_{1,N}C_{\beta,N})^2d_N(Y)^2d_N(Z)^\beta .
\]
The strict gaps persist on smaller fixed complex neighborhoods.
Only near the actual \(z_*\) is its nonzero Fourier packet
used to remove the outgoing halfweight. Cauchy's formula
then gives the stated normalized \(10^{-12}\) gap with
polynomial derivative cost.

The two left incoming pieces are now covered on the full
right shoulder. The central and right incoming pieces have
their separate complete-source theorems; the other lower
complement and the selected upper arcs retain their distinct
remaining obligations.
