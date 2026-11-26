# The initial incoming path and taper on the complete half-grid side

Private finite-source proof, 8 November 2026. The original initial
incoming path and its taper are controlled on the entire half-period
vertical side, with the full forced Fourier weight and the actual
half-grid denominator. Both grid-correction horizontals are retained.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Original source and the precise contribution

Use the actual complete words in powers three and four beginning
\(343\), of length \(m\ge5\), and their reference
\[
(a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3).
\]
All reference data and heights remain fixed. Write
\[
\begin{gathered}
h_a=\Im a_*,\quad h_s=\Im s_*,\quad c=\Im y_*,
\quad h_t=\Im t_*,\quad h_z=\Im z_*,\quad H=1/100,\\
-.072<h_a<0,\quad -.102<h_s,c<-.001,\quad
-.03<h_t,h_z<.02,\quad 7/10<e^{2\pi c}<41/50,\\
z=u+ih_z,\qquad 3/10\le u\le39/100 .
\end{gathered}                                                    \tag{1}
\]
These are the original actual correlations, not independent
replacement reference parameters. Keep the affine rate
\(\Lambda_{123}(z)\) of
[the central half-grid source](research_mixed_next_three_central_half_grid_vertical.md).
There is no next outgoing halfweight.

Put \(D=N-1,\ r=e^{-2\pi i/N}\), and retain
\[
\begin{split}
P_j&=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\\
U_{0,N}(w,X)&=\sum_{j=0}^{D}H_N(w,r^{-j})p_j(X)/P_j,\\
C_{\beta,N}(V,W)&=\sum_{j=0}^{D}
             \frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}} .
\end{split}                                                       \tag{2}
\]
Every \(H_N\) is the complete original coherent coefficient.
The original polynomial \(d_N\), of degree at most \(D\), satisfies
\(d_N(r^b)=P_b^{-1}\); all its forcing remains.
Throughout, \(X=e^{-2\pi ia}\).

The two incoming paths have their original increasing orientations:
\[
\Gamma_{\rm in}=[0,1/10],\qquad
\Gamma_{\rm tap}=\{a(x)=x-i\lambda(x-1/10):1/10\le x\le11/50\},
\quad \lambda=-h_a/(3/25)\in(0,3/5).
\tag{3}
\]
For either path \(\Gamma\), define
\[
\begin{split}
F_N^\Gamma(w,Y)&=N\int_\Gamma
 U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da,\\
K_N^\Gamma(y)&=\frac{N F_N^\Gamma(w,Y)d_N(Y)C_{0,N}(Y,Z)}
                         {1-Y^N},\qquad
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\\
M_N&=\lceil N/2\rceil,\qquad L_N=(M_N-1/2)/N,\\
V_N^\Gamma&=i\int_c^H K_N^\Gamma(L_N+ih)\,dh,\\
J_N^{\Gamma,\mathrm{grid}}&=
 \int_{L_N}^{1/2}K_N^\Gamma(q+ic)\,dq
 -\int_{L_N}^{1/2}K_N^\Gamma(q+iH)\,dq .
\end{split}                                                       \tag{4}
\]
Thus both original factors \(N\) occur, with different origins.
The last term is zero at odd levels; at even levels its two
horizontal intervals have length \(1/(2N)\).

**Theorem.** Uniformly on (1), for all real ordinary colors
\(w\in[-2,2]\), both parities and all sufficiently large levels,
the pointwise density before the first integration satisfies
\[
\left|
\frac{N U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z)}
     {1-Y^N}\right|
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-12}\}},
\quad a\in\Gamma_{\rm in}\cup\Gamma_{\rm tap},\
y=L_N+ih,\ c\le h\le H.                                      \tag{5}
\]
The same rate holds at the two grid-correction horizontals in (4).
Consequently
\[
|V_N^\Gamma|+|J_N^{\Gamma,\mathrm{grid}}|
 \le CN^{B'}e^{N\{\Lambda_{123}(z)-10^{-12}\}} .                 \tag{6}
\]
No outside-parameter jet or bound for the remaining incoming
paths or coherent middle insertion is asserted.

## 2. The already calibrated endpoint at \(a_0=11/50+ih_a\)

Use the original primitive \(g\), with
\(g'(\xi)=\operatorname{Log}(1-e^{-2\pi i\xi})\), and
\[
Q_\beta(v;b,d)=g(b+v)+g(d+v)-(2+\beta)g(v)-g(b)-g(d)+2\pi ibv .
\tag{7}
\]
For now set \(y=1/2+ih,\ c\le h\le H\).
Then \(\Re g(y)=0\). The first controlling profiles are
the main height \(h_s\), over \(1/8\le s_R\le1/2\), the
real cuts \(1/8,1/2\), and the periodic last rate
\[
L_1(a,h)=-2\pi\Im a+2\pi h_+ .
\tag{8}
\]
The next profiles are its main height \(h_t\), over
\(3/20\le t_R\le1/2\), the real cuts \(3/20,1/2\), and
\[
L_0(h)=2\pi(-h)_++2\pi(h_z)_+ .
\tag{9}
\]
Sections 2--3 of the central half-grid theorem prove, before
finite summation, that every pair \(\phi_1,\phi_0\) from these
families satisfies
\[
B_U(11/50)+\phi_1(a_0,h)+\phi_0(h)
 <\Lambda_{123}(z)-10^{-10} .                                  \tag{10}
\]
The proof retains the original lower-face calibration and
the selected upper forcing branch, and interpolates fixed
profiles by convexity in the shared height. We use exactly
this profilewise conclusion, not an inference from a modulus
bound for a signed kernel.

The complete cap on the taper has the original regular
envelope \(\Psi_0(e,a)\), with
\[
e=u_e+ik,\quad .27\le u_e\le.49,\quad -.019\le k\le.037,
\tag{11}
\]
and its separate true-end envelope, constant at nonpositive
incoming heights. Its own physical tails, aliases and joins
are included. At \(a_0\) all these cap profiles are bounded
by \(B_U(11/50)\). These are the original inputs in
[selected initial/taper, Section 2](research_mixed_next_three_selected_left_incoming_initial_taper.md)
and its cited all-real-color cap source.

We also use
[the half-grid bounded-factor theorem](research_mixed_next_three_half_grid_bounded_prefix.md):
an index-independent preceding factor of rate at most
\[
B_f=77/50+\pi/50                                             \tag{12}
\]
can be attached to the complete \(d_N C_{0,N}/(1-Y^N)\)
on this vertical, and to its two endpoint horizontals,
with finite gap \(1/1000\). This theorem retains both
forced-weight alternatives and every next current.

## 3. Incoming transport of the first low, main and half profiles

On the taper keep
\[
\ell(x)=7/100+x/4,\qquad .095\le\ell(x)\le1/8 .
\tag{13}
\]
For a fixed real first index \(v\), the incoming derivative of
a regular cap profile plus the first phase is
\[
\frac d{dx}\Re\{\Psi_0(e,a(x))+Q_1(v;a(x),y)\}
 =\Re D_a+\lambda\Im D_a,\quad
D_a=g'(e+a)+g'(a+v)-2g'(a)+2\pi iv .                          \tag{14}
\]
It is independent of \(y\), including its shared height.
The original fixed-index lower bounds \(-118/875,-139/800\)
on the two taper ranges therefore still apply.

At a real index the folded force is
\[
e^{\Re Q_{1,s}}=
\frac{|T-e^{-2\pi i(x+v)}|\,|1-Re^{-2\pi i(1/2+v)}|}
     {(2\sin\pi v)^3},\quad
T=e^{-2\pi\Im a}\ge1,\quad R=e^{2\pi h}>0 .                    \tag{15}
\]
The outgoing modulus is at least one. It is therefore at
least the former lower bound \(2\sin(\pi v)\cos(\pi v)\)
on \(v\le1/8\). The unchanged moving-cut forces \(9/5\)
and \(135/64\), combined with \(\ell'=1/4\), prove
the same incoming derivative \(>1/200\) along the cut.
The true-cap-end alternative has the same positive transport.
Every real low row increases to this cut: the incoming
modulus is at least \(2\sin\pi v\), and (15) exceeds
\((2\sin\pi v)^{-2}>1\). The zero row is kept.

On the added main strip \(\ell(x)\le v\le3/20\), put
\(\rho=e^{2\pi h_s}\in(1/2,1)\) and
\(D_0=|1-\rho e^{-2\pi iv}|^2<5/6\). The unchanged incoming
modulus exceeds \(15/16\). Since the outgoing shifted real
coordinate is in \([.595,.65]\), its modulus is at least one
for every positive radius \(R\rho\). Thus its force exceeds
\[
(15/16)/D_0^{3/2}>(15/16)/(5/6)=9/8>1 .                      \tag{16}
\]
Every added main point clips upward to \(3/20+ih_s\) at
the current incoming point. The original incoming transport
on the remaining main strip \(3/20\le v\le1/2\), and on
the real half cut, is independent of \(y\) by (14).
It reaches \(a_0\), where (10) applies. The full next
profile and its reference are held fixed in every comparison.

## 4. The complete first-current estimates at the half-period

Write
\[
C(v,\sigma)=\frac{\sin(2\pi v)}
                 {\cosh(2\pi\sigma)-\cos(2\pi v)} .
\]
We prove on the taper, for \(\ell(x)\le v<1/2\) and
\(\sigma\ge h_s\),
\[
3C(v,\sigma)-\Re\cot\pi(a+v+i\sigma)
                    -\Re\cot\pi(y+v+i\sigma)>0 .             \tag{17}
\]
The outgoing cotangent is nonpositive at every shared
height, since its real coordinate is \(1/2+v\).

For \(h_s\le\sigma\le.102\), the old written bound
\(\cosh(2\pi\sigma)<5/4\) applies. On \([.095,1/8]\)
the own cotangent is \(>1\), while the incoming one is
\(<3/2\). On \([1/8,1/4]\), the own cotangent is
\(>(7/10)/(5/4)=14/25\), and the incoming one is again
\(<3/2\), since \(x+v\ge9/40\) and
\(\cot(9\pi/40)<3/2\). On \([1/4,1/2)\), any positive
incoming cotangent is at most \(\cot\pi v\), and
\[
\frac{\cot\pi v}{C(v,\sigma)}
 =\frac{\cosh(2\pi\sigma)-\cos2\pi v}{1-\cos2\pi v}
 \le5/4 .
\]
These bounds prove (17) at these heights.

For \(\sigma\ge.102\), put \(A=\cosh(2\pi\sigma)\).
The taper's height \(\eta_a=-\Im a\in[0,.072]\) gives
\[
\cosh2\pi(\sigma-\eta_a)\ge kA,\qquad
k=e^{-2\pi\eta_a}>5/8 .                                      \tag{18}
\]
The following elementary comparisons suffice.

* For \(.095\le v\le1/8\), use own sine \(>11/20\),
  own cosine \(>7/10\), and incoming cosine \(<7/20\).
  Thus compare \((33/20)/(A-7/10)\) with
  \(1/\{(5/8)A-7/20\}\). Their cleared difference is
  \(A/32+49/400>0\).
* For \(1/8\le v\le3/20\), use own sine \(>7/10\),
  own cosine \(>1/2\), and incoming cosine \(<1/5\).
  The sufficient comparison
  \((21/10)/(A-1/2)>1/\{(5/8)A-1/5\}\)
  has cleared difference \(5A/16+2/25>0\).
* For \(3/20\le v\le1/4\), the incoming cosine is
  nonpositive, while own sine \(>4/5\) and own cosine
  is nonnegative. Therefore \(3C(v,\sigma)>12/(5A)\),
  whereas the incoming cotangent is at most \(8/(5A)\).
* For \(1/4\le v<1/2\), if the incoming cotangent is
  positive, increasing the angle from \(v\) to \(x+v<1/2\)
  decreases its sine and makes its cosine more negative.
  Equation (18) then bounds it by \(C(v,\sigma)/k\).
  If it is nonpositive no bound is needed.

All denominators used above are positive. The trigonometric
witnesses are those of the original small-cut proof:
\(\sin(19\pi/100)>11/20\),
\(\cos(39\pi/100)<7/20\),
\(\cos(9\pi/20)<1/5\), and
\(\sin(3\pi/10)>4/5\).
They also follow directly from the original sine/cosine
polynomials and \(\pi>25/8\). This proves (17).
At \(v=1/2\), the incoming cotangent is strictly negative.
The outgoing numerator wall is treated as the one-sided
continuous convex limit; no nonzero symbol is asserted there.

Let \(J_1(v,\sigma)=\Im Q_{1,s}(v+i\sigma;a,y)\).
At every height the outgoing argument is nonpositive
and the own argument is nonnegative. Hence
\[
J_1(v,\sigma)\le
\pi\max\{1-2v,2x\}\le81\pi/100 .                             \tag{19}
\]
By (17), \(J_1\) decreases above \(h_s\).
On the original logarithmic branches its upper-height limit is
\[
\lim_{\sigma\to+\infty}J_1(v,\sigma)
 =\pi(1-2x-2v)-2\pi v-3\pi(1-2v)+2\pi x
 =-2\pi+2\pi v\ge-181\pi/100 .                              \tag{20}
\]
Thus \(J_1>-181\pi/100\) at finite heights above \(h_s\).
Keep the aliases at \(-1/5,+4\). Relative to the same-index
main profile, their losses exceed respectively
\[
2\pi/5-(81\pi/100)/5=119\pi/500>\pi/5,
\quad
8\pi-(181\pi/100)(4+51/500)
 =28769\pi/50000>\pi/2 .                                    \tag{21}
\]
Both upper weighted sides decrease away from zero, with
derivative at most \(-19\pi/100\); both lower sides
decrease in the downward direction by (19).
The unweighted joins are vertically convex by (17), so
their real and main endpoints suffice. All these endpoints
were transported in Section 3. This proves every first
current comparison before integration.

## 5. Every first upper physical row and its last alternative

Let \(J(v)=\int_0^v\log(2\sin\pi s)\,ds\).
The exact reflected first-row rate is
\[
\begin{split}
\Phi(v)&=E_1(1-v;a,y)-\delta_a-\log_+R\\
 &=3J(v)-\int_0^v\log|T-e^{-2\pi i(x-b)}|\,db
          -\int_0^v\log|1-Re^{-2\pi i(1/2-b)}|\,db ,
\quad \delta_a=-2\pi\Im a .
\end{split}                                                       \tag{22}
\]
This retains both full-period means and the chirp. It holds
for \(R\) on either side of one.

For \(0<v\le9/50\), the outgoing integration interval
lies in \([.32,.5]\), so its integrand is nonnegative
for every \(R>0\). The incoming folded arc has the
centered lower bound \(2J(v/2)\). Therefore
\[
\Phi(v)\le3J(v)-2J(v/2)
 \le v\{\log(8\pi^2v^2)-2\}<0 .                              \tag{23}
\]
For the middle inequality use the exact duplication identity
\[
J(v)-2J(v/2)=2\int_0^{v/2}\log(2\cos\pi s)\,ds\le v\log2
\]
and \(J(v)\le v\{\log(2\pi v)-1\}\).
The last sign holds even for \(v\le1/4\), since
\(\pi^2<10\) and \(e^2>5\).

For \(9/50\le v\le1/2\), the radius-position comparison
in the adopted selected initial/taper proof bounds the
incoming modulus by \(21/10\), on both paths in (3).
The outgoing one is at most \(1+e^{\pi/50}<31/15\).
The same proof gives
\[
\Phi(v)-\Phi(1/2)\le(37/25)(1/2-v)+3J(v)\le0 .                \tag{24}
\]
Its convex envelope vanishes at \(1/2\) and is less than
\(-19/10000\) at \(9/50\), using the written
Catalan/chord bound \(-J(9/50)>317/2000\).
Thus every upper row reduces positively to its real-half
or full last rate, at every intermediate shared height.
This is an absolute physical-row estimate, not a claim
of convexity for individual upper rows in that height.

The cap plus the half rate transports by (14).
The cap plus the last rate also increases along the entire
taper. In the notation (11), set
\(D_{\rm cap}=g'(e+a)-g'(a)\).
Equation (35) of the selected initial/taper proof actually
proves \(\Re D_{\rm cap}>0\) on the larger interval
\(.1\le x\le.22\). Explicitly, with
\(r_a=e^{2\pi\Im a}\le1,\ r_e=e^{2\pi k}>7/8\),
subtracting its squared denominator from numerator gives
more than
\[
r_a\{-15r_a/64+2(9/50+7/40)\}
\ge(761/1600)r_a>0 .
\]
The shifted argument is at least \(-21\pi/50\) and
the incoming argument at most \(2\pi/5\). Hence
\[
\frac d{dx}\{\Re\Psi_0(e,a(x))+\delta_a+\log_+R\}
 =\Re D_{\rm cap}+\lambda(\Im D_{\rm cap}+2\pi)>0 .            \tag{25}
\]
The true-cap-end envelope is constant at these nonpositive
incoming heights; its additional carrier \(\delta_a\)
is increasing. This also transports to (10).
The shared term \(\log_+R\) is fixed during the transport.

## 6. Initial real path and complete finite assembly

On \([0,1/32]\), the complete prefix has unit-disk rate
at most \(77/50\), by
[incoming ends, Section 2](research_mixed_next_three_selected_left_incoming_ends.md).
Its outgoing degree is at most \(D\), so the exact
reciprocal-polynomial maximum principle gives rate at most
\(B_f\) for every \(|Y|\le e^{\pi/50}\). The attachment
in (12) pays this entire prefix on the half-grid and both
grid horizontals, without opening its finite sums.

For \(1/32\le x\le1/10\), keep the original full regular
cap envelope, its extra real profiles \(.49\le e\le.5\),
and first cuts \(19/200,1/2\). At every first-current
point \(s=v+i\sigma\) its exact incoming derivative is
\[
\frac d{dx}\Re\{\Psi_0(e,x)+Q_1(v+i\sigma;x,y)\}
 =
\log\frac{|1-e^{-2\pi i(e+x)}|
              |e^{-2\pi\sigma}-e^{-2\pi i(x+v)}|}
             {(2\sin\pi x)^2}>\log(11/8) .                    \tag{26}
\]
This is the original all-height initial transport. It is
independent of \(y\), so it reaches \(x=.1\), already
covered above. The extra real cap profiles clip to
\(e=.49\) there, exactly as in their original proof.
Low physical rows increase to their real cut by (15).
All upper rows use (22)--(24); for their last alternative
the regular cap itself increases along this real interval,
because \(|1-e^{-2\pi i(e+x)}|>1\) and \(2\sin\pi x<1\).

The separate true cap ends times the complete first kernel
have unit-disk rate \(389/300\), from the original initial
source. Their degree in \(Y\) is at most \(D\), so their
rate on the present disk is at most \(389/300+\pi/50<B_f\).
The bounded-factor attachment pays this complete group.
No cap packet is extended to a true private endpoint.

For the other groups use
\[
A_N(x)=\lfloor N\ell(x)\rfloor+1,\quad M_N=\lceil N/2\rceil ,
\]
with \(\ell=19/200\) on the initial real path, and keep
all indices \(j<A_N,\ A_N\le j<M_N,\ M_N\le j<N\).
The original canonical interpolation is
\[
e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                         E_N(a)E_N(y)E_N(s)^3 .
\tag{27}
\]
The exact middle identity retains \(+N\,ds\), both
horizontal aliases, four weighted sides and both
unweighted joins. Section 4 pays every current on the
taper; (26) pays every corresponding initial current.
The next kernel retains exactly the complete current and
physical reduction of the central half-grid theorem:
cuts \(3/20,1/2\), main height \(h_t\), aliases \(-1/5,+8\),
four weighted sides and two unweighted joins, including
its positive upper half and both last carriers.

The first endpoint bounds (10) hold with each next
controlling profile attached. For the regular-cap groups
and the taper's transported end alternative, the preceding
arguments therefore bound the product before \(d_N\)
is attached, at \(q=1/2\), by rate
\(\Lambda_{123}-10^{-10}\), with an arbitrarily small
finite tolerance. The separately bounded initial raw
groups use (12) directly, with its larger attachment gap
\(1/1000\); no weight is divided out of that estimate.
Every numerator zero and actual integer end row remains.

## 7. The original denominator and both grid horizontals

Replace \(q=1/2\) by \(L_N\); the difference is at most
\(1/(2N)\). Uniform zero-safe product bounds and the
original midpoint period/reflection estimate at \(y+s=1\)
change all continuous rates by \(O((\log N)/N)\).
Other denominator arguments remain regular. The same
observations apply on the two short horizontal intervals
between \(L_N\) and \(1/2\). This is a rate comparison,
not an assertion of a nonzero numerator symbol at the wall.

The complete forced-weight estimate gives
\[
|d_N(Y)|\le C_\tau N^B
\exp N\{\max(-\Re g(y),\,2\pi(\Im y)_+)+\tau\}.
\]
On the half-grid \(\Re g(L_N+ih)=O(N^{-1})\), whereas
exactly
\[
Y^N=-e^{2\pi Nh},\qquad |1-Y^N|=1+e^{2\pi Nh}.
\]
Consequently \(d_N(Y)/(1-Y^N)\) has arbitrarily small
exponential upper rate on the entire vertical, including
height zero. At the lower grid horizontal the denominator
is bounded below by \(1-e^{2\pi Nc}\); at the upper one
write the quotient as
\[
\frac{d_N(Y)}{1-Y^N}
 =-\frac{d_N(Y)Y^{-N}}{1-Y^{-N}} .
\]
The fixed upper denominator is bounded away from zero,
and the selected forced-weight numerator again has
arbitrarily small rate on this \(O(1/N)\) interval.
No residue, interpolation remainder or forcing is removed.

Choose the common tolerances inside the reserve in (10),
then weaken the rate to \(10^{-12}\). Finite sums, bounded
path lengths and every original factor \(N\) cost only
a polynomial. This proves (5). The incoming measures
are \(+N\,dx\) and \(+N(1-i\lambda)\,dx\); the vertical
measure and both horizontal signs are exactly (4).
Their integration proves (6).

These are contributions of the original unfiltered prefix.
With the unchanged old filter, their subtraction is linear;
no separate filter is imposed on an incoming-path contribution.
The filter correction has its own already proved half-grid
estimate. Other incoming paths, the middle coherent physical
insertion, and the full signed Fourier comparison remain
separate obligations.
