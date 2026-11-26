# Complete conditional currents on the lower left interval

Private research proof, 8 November 2026. Both conditional middle
sums reduce to their original main and real-cut profiles on the
lower left shared interval. Every horizontal alias, both halves of
each weighted side, and both unweighted joins are retained.
The common alias heights are \(-1/5\) and \(4\).

The resulting finite source theorem includes the closed interval
\(0\le q\le.22\). At its nonreal seam the original reciprocal
factorial is continued by its exact recurrence, while the finite
Fourier polynomial retains its distinct forced upper bound.
No numerical evaluation or modification of a frozen input is used.

## 1. Original source and the precise retained sums

Use the actual ordinary-next references and allocations of
[the joint lower-left profile theorem](research_mixed_next_lower_left_joint_main_profiles.md).
Thus
\[
\begin{gathered}
a=x+ih_a,\quad x\in P=[.22,.45],\qquad
y=q+ih_y,\quad 0\le q\le.22,\qquad
z=u+ih_z,\quad u\in P,\\
-.072<h_a<0,\quad -.102<h_s,h_y<-.001,\quad
-.108\le h_t\le.068,\quad |h_z|\le.108 .
\end{gathered}
\tag{1}
\]
When \(\beta=1\), \(h_t,h_z<0\). All original typed
reference correlations remain imposed. Let
\[
Q_\gamma(v;b,c)
=g(b+v)+g(c+v)-(2+\gamma)g(v)-g(b)-g(c)+2\pi ibv .
\tag{2}
\]
The first phase is \(Q_1(s;a,y)\), on main height \(h_s\);
the next is \(Q_\beta(t;y,z)\), on main height \(h_t\).
The shared weight gives exactly \(-g(y)\), and the outgoing
allocation is \(-\beta g(z)/2\).

Put
\[
\ell_{\rm first}=1/8,\qquad
\ell_0=3/20,\quad\ell_1=1/8,\qquad
L_N(\ell)=\lfloor N\ell\rfloor+1,\quad M_N=\lceil N/2\rceil .
\tag{3}
\]
For either factor define its literal middle sum by
\[
\mathcal M_{\gamma,N}(b,c)
=\sum_{j=L_N(\ell)}^{M_N-1}
  \frac{e^{2\pi ibj}p_j(e^{-2\pi ib})p_j(e^{-2\pi ic})}
       {P_j^{2+\gamma}},
\quad
P_j=(r;r)_j,\quad p_j(W)=(rW;r)_j,\quad
r=e^{-2\pi i/N}.
\tag{4}
\]
Here \((\gamma,b,c,\ell)=(1,a,y,1/8)\) or
\((\beta,y,z,\ell_\beta)\).
The associated real half-grid cuts are
\[
\ell_N=(L_N-\tfrac12)/N,\qquad b_N=(M_N-\tfrac12)/N .
\tag{5}
\]
They differ from their stated cuts by at most \(1/(2N)\).
The exact canonical row function is
\[
T_{\gamma,N}(v;b,c)=
 e^{2\pi iNb v}\Pi_N(b+v)\Pi_N(c+v)
                  E_N(b)E_N(c)E_N(v)^{2+\gamma}.
\tag{6}
\]
At \(v=j/N\), it is exactly the summand in (4).
These are the same \(\Pi_N,E_N\) and cotangent decomposition
as in [the lower-output middle reduction](research_mixed_conditional_lower_output_middle_reduction.md),
Sections 1 and 4. No phase or level scalar is reset.

## 2. Elementary argument bounds retained below

For \(0<r<1\) and real \(h\), write
\[
\mathcal A(r,h)=\operatorname{Arg}(1-e^{2\pi h-2\pi ir})
\tag{7}
\]
with the original continuous strip argument. It lies between
zero and \(\pi(1-2r)\). For \(h\le0\), it lies between zero
and \(\pi(1/2-r)\); for \(h\ge0\), it lies between
\(\pi(1/2-r)\) and \(\pi(1-2r)\).
These statements follow by following the ray
\(1-\rho e^{-2\pi ir}\) from \(\rho=0\) to infinity.

Here is a uniform positive-height comparison used twice.
Let \(v\in[1/8,1/2]\), \(\sigma\ge0\), and
\(R\in[1/2,1]\). Put
\[
B=\mathcal A(v,\sigma),\qquad
I_0=\operatorname{Arg}(1-Re^{2\pi\sigma-2\pi iv}).
\]
Then
\[
                         0\le B-I_0\le\pi/4.
\tag{8}
\]
Indeed set \(A=e^{2\pi\sigma}\), \(\theta=2\pi v\).
The quotient of the two arguments has nonnegative imaginary
part. Its real part minus its imaginary part has the sign of
\[
1/A+RA-(1+R)\cos\theta-(1-R)\sin\theta .
\]
The first two terms are at least \(2\sqrt R\ge\sqrt2\).
On \(\pi/4\le\theta\le\pi\), the last trigonometric
combination is at most its value \(\sqrt2\) at \(\pi/4\):
its unrestricted maximizing angle is
\(\arctan((1-R)/(1+R))<\pi/4\).
This proves (8), with endpoint values taken continuously.

If \(0\le q\le.22\), then
\[
\left|\Im\cot\pi(v+q+ih)\right|\le\sqrt2
\quad\hbox{for all real }h .
\tag{9}
\]
In fact \(\cos(2\pi(v+q))\le1/\sqrt2\). With
\(C=\cosh(2\pi h)\ge1\) and \(c\le1/\sqrt2\),
\[
2(C-c)^2-(C^2-1)\ge(C-\sqrt2)^2\ge0 .
\]
Since \(\partial_q\mathcal A=\pi\Im\cot-\pi\),
(8)--(9), including their original lifts, imply
\[
\mathcal A(v+q,\sigma+h_y)
 \ge B-\pi/4-\pi(1+\sqrt2)q,\qquad \sigma\ge0 .
\tag{10}
\]
Here \(e^{2\pi h_y}>1/2\), as follows from the original
height bound and \(.204\pi<2/3<\log2\).

All following bounds allow an index at \(1/2\), by
continuity. Its own argument is then exactly zero.

## 3. All next-kernel weighted currents

Let
\[
J_\beta(v,\sigma)=\Im Q_{\beta,t}(v+i\sigma;y,z)
=\mathcal A(q+v,h_y+\sigma)+\mathcal A(u+v,h_z+\sigma)
 -(2+\beta)\mathcal A(v,\sigma)+2\pi q .
\tag{11}
\]
We keep \(\ell_\beta\le v\le1/2\).
Since the own argument is nonnegative, and \(q\le u\),
the three possibilities for the shifted arguments give
\[
                         J_\beta<53\pi/50
                         \qquad(-\infty<\sigma<\infty).
\tag{12}
\]
When both shifted real parts are below \(1/2\), the bound
after division by \(\pi\) is \(2-4v-2u\le53/50\).
When only the incoming one is below \(1/2\), it is
\(1-2v\le3/4\); when both are above it, it is
\(2q\le11/25\). Finite radii give the displayed strictness.

For lower bounds it suffices to use the auxiliary expression
with index coefficient three, because \(J_0=J_1+\mathcal A(v,\sigma)
\ge J_1\) at the same parameters. If \(\sigma\le0\), the own
argument is at most \(\pi(1/2-v)\).
Use the full strip lower bounds for the shifted arguments.
If both shifted parts are below \(1/2\), this gives
\(-3/2+3v+2q\ge-9/8\).
If only the incoming one is below \(1/2\), it gives
\(-1/2-2u+v+2q\ge-51/40\).
If neither is below it, it gives \(1/2-2u-v\ge-9/10\).
Thus
\[
                         J_\beta>-51\pi/40\qquad(\sigma\le0).
\tag{13}
\]

For \(\sigma\ge0\), combine (10), the bound
\(\mathcal A(u+v,h_z+\sigma)\ge\pi(1/10-2v)\),
and \(B\le\pi(1-2v)\). Retaining \(2\pi q\) gives
\[
\frac{J_\beta}{\pi}
 \ge-\frac{43}{20}+2v-(\sqrt2-1)q
 >-\frac{349}{175}>-2 .
\tag{14}
\]
The last inequality uses \(v\ge1/8\), \(q\le11/50\),
and \(\sqrt2<10/7\). Thus both weighted vertical halves
decrease away from their real cut: their rates are
\(\Re Q_\beta(v+i\sigma)-2\pi|\sigma|\).

For a sharper upper-horizontal comparison take \(\sigma\ge1/5\).
Both shifted inverse radii are less than \(3/5\), since
\[
\sigma+h_y>.098,\quad \sigma+h_z\ge.092,\quad
.184\pi>23/40>8/15>\log(5/3).
\]
The last logarithmic inequality follows by integrating
\(1/t\le(1+t^{-2})/2\) from one to \(5/3\).
The exact large-radius formula is
\[
\mathcal A(r,h)=\pi(1-2r)
        +\operatorname{Arg}(1-e^{-2\pi h+2\pi ir}),\qquad h>0.
\tag{15}
\]
If \(r<1/2\), the last argument lies between
\(-\arcsin(3/5)\) and zero; if \(r\ge1/2\), it is
nonnegative. Also \(\arcsin(3/5)<2\pi/9\):
\(2\pi/9>25/36\) and
\(25/36-(25/36)^3/6>3/5\).

The limiting expression for coefficient three in (11) is
\(\pi(-1-2u+2v)\), and the own correction in (15) is
nonnegative after multiplication by minus three.
If \(u+v<1/2\), both shifted corrections may be negative,
but \(u<1/2-v\) gives the limiting bound \(-3\pi/2\).
Subtracting \(4\pi/9\) gives \(-35\pi/18\).
If only \(q+v<1/2\), the limiting bound is \(-33\pi/20\)
and only \(2\pi/9\) is subtracted, giving
\(-337\pi/180>-35\pi/18\). If both shifted real parts
are at least \(1/2\), no negative correction is needed.
Consequently
\[
                         J_\beta>-35\pi/18\qquad(\sigma\ge1/5).
\tag{16}
\]

Integrating (12)--(16), with the original sampling penalties,
now proves both full horizontal bounds:
\[
\begin{split}
\Re Q_\beta(v-i/5)-2\pi/5
 &<\Re Q_\beta(v+ih_t)-1449\pi/12500,\\
\Re Q_\beta(v+4i)-8\pi
 &<\Re Q_\beta(v+ih_t)-46969\pi/630000 .
\end{split}
\tag{17}
\]
For the first line use \(h_t+1/5\le67/250\).
For the second, a common upper cost from \(h_t\) to \(4\) is
\[
\frac{51}{40}\frac{27}{250}
+\frac{349}{175}\frac15
+\frac{35}{18}\frac{19}{5}.
\]
Its difference from \(8\) is \(46969/630000>7/100\).
The first loss exceeds \(\pi/10\).
Allocation terms independent of the index do not alter these bounds.

## 4. All first-kernel weighted currents

Put
\[
J_{\rm first}(v,\sigma)=
 \mathcal A(x+v,h_a+\sigma)+\mathcal A(q+v,h_y+\sigma)
                    -3\mathcal A(v,\sigma)+2\pi x,
\quad 1/8\le v\le1/2 .
\tag{18}
\]
Both outer heights are negative and \(q\le x\).
The same three real-part cases give, at all heights,
\[
                         J_{\rm first}<33\pi/20.
\tag{19}
\]
When both shifted parts are below \(1/2\), the upper bound
is \(2-4v-2q\le3/2\); when only \(q+v\) is below it,
it is \(1-2v-2q+2x\le33/20\); otherwise it is \(2x\le9/10\).

If \(\sigma\le0\), both shifted radii are at most one.
Use their lower bounds \(\pi\min(1/2-r,0)\) and the own
upper bound \(\pi(1/2-v)\).
The three cases give respectively
\(-3/2+3v+2x\ge-137/200\),
\(-1+x+2v\ge-53/100\), and
\(-1/2+x-q+v\ge-3/8\).
Hence
\[
                         J_{\rm first}>-137\pi/200
                         \qquad(\sigma\le0).
\tag{20}
\]

For \(\sigma\ge0\), use (10) for the shared outgoing
argument. If \(x+v\ge1/2\), its other argument is at least
\(\pi(1-2x-2v)\), giving
\[
J_{\rm first}/\pi
 \ge-5/4+2v-(1+\sqrt2)q>-537/350 .
\]
If \(x+v<1/2\), its other argument is only bounded below
by zero. This distinct case gives
\[
J_{\rm first}/\pi
 \ge-9/4+4v+2x-(1+\sqrt2)q>-1291/700 .
\]
Here \(\sqrt2<10/7\), \(v\ge1/8\), \(x\ge11/50\)
and \(q\le11/50\) suffice. Thus the common valid bound is
\[
                         J_{\rm first}>-1291\pi/700>-2\pi
                         \qquad(\sigma\ge0).
\tag{21}
\]
In particular no positive asymptotic argument was used as a
lower bound when \(x+v<1/2\).

Equations (19)--(21) pay both weighted sides at both cuts.
They also give the full horizontal comparisons
\[
\begin{split}
\Re Q_1(v-i/5;a,y)-2\pi/5
 &<\Re Q_1(v+ih_s;a,y)-7\pi/100,\\
\Re Q_1(v+4i;a,y)-8\pi
 &<\Re Q_1(v+ih_s;a,y)-387091\pi/700000 .
\end{split}
\tag{22}
\]
For the upper alias the loss is
\(4(2-1291/700)-(51/500)(137/200)>1/2\).
For the lower alias use \(h_s\le0\).
The original incoming chirp is present in every case.

## 5. Both unweighted joins for each factor

Write
\[
C(v,\sigma)=\Re\cot\pi(v+i\sigma)
=\frac{\sin(2\pi v)}{\cosh(2\pi\sigma)-\cos(2\pi v)}.
\tag{23}
\]
For the compact heights needed here,
\[
\cosh(.216\pi)<5/4,\qquad
\cosh(17\pi/125)<11/10 .
\tag{24}
\]
The first follows from
\(.216\pi<594/875<56/81<\log2\), where the last
inequality retains the first two terms of
\(2\operatorname{arctanh}(1/3)\).
For the second, \(17\pi/125<3/7\), and
\[
\cosh(3/7)-1
 \le\frac{9/98}{1-3/196}
 =18/193<1/10 .
\]

If \(\sigma\le0\) and the added outer height is nonpositive,
increasing its absolute height reduces a positive cotangent.
Also \(C(v,\sigma)\) decreases as \(v\) increases through
\([1/8,1/2]\): the derivative has the sign of
\(\cosh(2\pi\sigma)\cos(2\pi v)-1<0\).
Thus each shifted positive cotangent is at most the own one.
For the first factor both outer heights are nonpositive,
so on \(h_s\le\sigma\le0\),
\[
3C(v,\sigma)-C(x+v,h_a+\sigma)-C(q+v,h_y+\sigma)>0 .
\tag{25}
\]
When a shifted real part exceeds \(1/2\), its cotangent
is nonpositive and the same conclusion holds.
At \(v=1/2\), the incoming shifted cotangent is strictly
negative, giving strictness there also.

For the next factor on a negative join, its incoming shifted
cotangent is at most the own one. If \(v+u<1/2\), then
\(v<.28\) and
\[
C(v,\sigma)>\frac{98}{145}>\frac23,\qquad
C(v+u,h_z+\sigma)<\cot(\pi/3)<\frac35 .
\tag{26}
\]
For the first bound, minimize in \(\sigma\) using (24)
and then in \(v\); at \(v=.28\),
\(\sin(14\pi/25)>49/50\) and
\(\cos(14\pi/25)>-1/5\).
For the second, \(v+u\ge.345>1/3\).
When \(v+u\ge1/2\), its cotangent is nonpositive.
It follows that
\[
(2+\beta)C(v,\sigma)-C(q+v,h_y+\sigma)
                         -C(u+v,h_z+\sigma)>0
\tag{27}
\]
on the whole negative join, for either type.
At the half cut the outgoing shifted term is strictly negative.

A positive next join occurs only for \(\beta=0\).
Here \(v\ge3/20\) and \(0\le\sigma\le h_t\le17/250\).
Put \(w=\cot\pi v>0\), initially \(v<1/2\).
Since \(\cos(2\pi v)<3/5\), (24) gives
\[
C(v,\sigma)>\frac45w,\qquad C(q+v,h_y+\sigma)\le w.
\tag{28}
\]
If the outgoing shifted cotangent is positive, let
\(c=\cot\pi u<5/4\). Then
\[
C(u+v,h_z+\sigma)
 \le\frac{wc-1}{w+c}<\frac w2,
\tag{29}
\]
because \(w^2-cw+2\ge2-c^2/4>0\).
If it is nonpositive, no upper cost is needed.
Thus (28)--(29) give the positive version of (27), with
strictness at \(v=1/2\) again supplied by the outgoing term.

Since the real index Hessian is \(-\pi\) times
(25) or (27), the real phase is convex in the vertical
index direction between its main height and zero.
Each unweighted join is therefore bounded by the larger
of its original real-cut and main-height endpoint profiles.
The other conditional factor and the full outside cap can
be held fixed throughout this comparison.

## 6. Literal current inventory and finite consequences

Fix \(\epsilon>0\), and first take \(\epsilon\le q\le.22\).
All factorial arguments in (6) lie in fixed regular compact
strips on
\[
 \ell_N\le\Re v\le b_N,\qquad -1/5\le\Im v\le4 .
\]
In particular the shifted real parts stay between zero and
one, and the two external denominator arguments stay strictly
inside their original real strip. The ordinary uniform
factorial estimates therefore bound (6) by its phase (2),
with polynomial amplitude and any prescribed small rate
tolerance.

At \(q=0\), the single outer argument \(y\) leaves that
real strip, but stays a fixed distance below the real axis.
[The original factorial seam theorem](research_factorial_symbol_across_inward_seam.md),
Sections 2--3, gives its unchanged symbol by the exact
recurrence for \(E_N(y)\). It retains the original action,
square root, \(N\) power and fixed holomorphic derivatives.
Every individual index and every shifted numerator argument
in (6) has real part uniformly between zero and one, even
on the full height rectangle above. Thus the seam theorem
and the regular-strip formulas cover all of \(0\le q\le.22\).
No Fourier-polynomial approximation is used for this step.

The exact finite cotangent identity gives \(+N\) times the
real middle integral plus two horizontal Fourier remainders
and four weighted vertical pieces. Moving that real main
to its original height adds its two oriented unweighted
joins. No extra physical residue lies between the two
half-grid cuts; (4) is exactly its retained integer range.
The nonconstant cotangent kernels have modulus at most
\(C e^{-2\pi N|\Im v|}\) on the half-grid sides and the
fixed-height horizontals, with polynomial outside factors.
Their constant modes are exactly the stated \(+N\) source.

Equations (12)--(22) pay every weighted piece against
its original same-index main profile or real-cut profile.
Equations (25)--(29) pay both unweighted joins. Their
strict uniform margins persist for the \(O(1/N)\) shifts
in (5), so no integer-cut derivative is needed.

**Current theorem.** On the full closed interval
\(0\le q\le.22\), every term of the complete
nine-piece decomposition of either middle sum (4) is
bounded, with polynomial cost and an arbitrarily small
rate tolerance, by its corresponding original main,
real-low or real-half profiles. Both horizontal remainders
have an additional fixed positive loss; one may take
\(\pi/20\) after the half-grid and finite-amplitude tolerances.
The result is valid at both parities and keeps the original
\(+N\) main measure and every nonzero Fourier frequency.

The two current comparisons can be applied successively
before taking their product. Section 6 of
[the joint profile theorem](research_mixed_next_lower_left_joint_main_profiles.md)
pays every pair of the resulting profiles with the complete
cap plane attached. Its deficit is \(10^{-10}\).
Section 3 of
[the low-block theorem](research_mixed_next_lower_left_low_physical_blocks.md)
gives the original Fourier weight its full absolute envelope
\(|d_N(Y)|\le C_\tau N^{B_\tau}e^{N(-\Re g(y)+\tau)}\),
including forcing and the closed seam. The outgoing allocation
is unchanged.
Consequently
\[
\begin{split}
&|U_{0,N}(w,X)\mathcal M_{1,N}(a,y)d_N(Y)
                      \mathcal M_{\beta,N}(y,z)|
                          |d_N(Z)|^{\beta/2}\\
&\hspace{15mm}\le C N^B
                    e^{N(\Lambda_{123}(z)-10^{-11})}.
\end{split}
\tag{30}
\]
The same holds when either middle sum is replaced by its
positive low physical block from
[the low-block theorem](research_mixed_next_lower_left_low_physical_blocks.md).
Adding the four low/middle combinations therefore pays
the literal product of the two sums over
\(0\le j<\lceil N/2\rceil\), on the full closed interval.
No upper physical row or last-row alternative is included
by this conclusion.

All-real-color bounds use the complete cap source.
Fixed real-color derivatives have polynomial cost.
For local normalized mixed jets, hold the paths and
integer cuts fixed at their base, use the original
integer-weight holomorphic square, and shrink the
outside neighborhoods. The resulting gap may be taken
as \(10^{-12}\). Only near the actual nonzero outgoing
packet is its halfweight removed. The extra original
first integration \(+N\int_{P+ih_a}da\) changes only
the polynomial prefactor.

The closed-seam conclusion uses both distinct inputs:
the exact reciprocal-factorial continuation for the canonical
rows, and the forced upper bound for \(d_N\). Neither is
substituted for the other.
The original upper physical rows, last-row alternatives
and noncentral first-incoming paths remain distinct
obligations.

