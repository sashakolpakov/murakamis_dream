# Paired prewall currents on the real second right interval

Private written proof, 11 November 2026. This is a substantive
current estimate. It
transports the first conditional upper correction together with
three actual third-factor horizontal currents, retaining their joint
original calibration. The two private intervals shrink before the
incoming numerator wall. Their moving endpoints are included in
the maximizing argument.
On the substantial interval from one half to \(18/25\), the
remaining third currents and every physical third row are also
paid. This gives the first upper correction paired with the complete
third kernel. It does not estimate the other first conditional
currents or the complete first polynomial.

Author-frozen after full proof and direct-source readback. The
finite-upper-current input has itself been author-frozen and submitted
for independent review. This deduction is not adopted until the
required independent and root reviews, including that input, finish.
Frozen sources and public files are unchanged; no mathematical
numerical evaluation is used.

## 1. Source and statement

Use the actual word, original primitives, allocations and affine
action of the complete 443 half-face theorem. In particular
\[
 a=x+ih,\quad 11/50\le x\le1/2,\quad c_1\le h\le1/100,
 \qquad z=b+ic_3,\quad b\in[11/50,9/20],
\]
\[
 -39/500<c_1<-1/50,\quad -51/500<h_2<-1/1000,
 \qquad -13/200\le h_3,c_3\le17/250.                    \tag{1}
\]
All heights are those of the same fixed actual word. Define
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                      -g(a)-g(b)+2\pi ias,
 \qquad g'(w)=\operatorname{Log}(1-e^{-2\pi iw}),\quad g(0)=0.
                                                               \tag{2}
\]
Fix \(Q<7/8\), an old right cut \(21/100<r_0<1/2\), and
\[
 0<\varepsilon<\min\{1/40,1-Q-1/8\},\quad
 r(q)=\min\{r_0,1-q-\varepsilon\},\quad
 I_q=[1/8,r(q)],\qquad 1/2\le q\le Q.                   \tag{3}
\]
The cut \(r_0\) is chosen sufficiently close to one half as in
the original half-face source. Put
\[
 h_U=\frac{\log2}{4\pi},\qquad L=13/200,
\]
\[
 A(q)=\max_{t\in I_q}\Re Q_1(t+ih_U;a,q)-2\pi h_U,
 \qquad B_\sigma(q)=\max_{t\in I_q}\Re Q_0(t+i\sigma;q,z).
                                                               \tag{4}
\]

**Proposition 1.** For every \(-L\le\sigma\le17/250\),
\[
                    A(q)+B_\sigma(q)
                    \le A(1/2)+B_\sigma(1/2).            \tag{5}
\]
The same inequality holds for \(\sigma=1/5\). The constants
\(-2\pi|\sigma|\), when these are sampling corrections, may
be subtracted on both sides. No maximizing-index restriction is
assumed in this statement; the needed restrictions are proved below.

Write \(M_2(a)\) and \(M_3(z)\) for the original half-face
main maxima at heights \(h_2,h_3\), on respective intervals
\([1/8,r_0]\) and \([3/20,r_0]\). Then
\[
\begin{array}{ll}
 A(q)+B_{h_3}(q)&<M_2(a)+M_3(z)-1/162,\\
 A(q)+B_{-L}(q)-2\pi L
       &<M_2(a)+M_3(z)-1/162-31\pi/1000,\\
 A(q)+B_{1/5}(q)-2\pi/5
       &<M_2(a)+M_3(z)-1/162-323\pi/2000.
\end{array}                                                    \tag{6}
\]
These are original absolute actions, with no phase reset.

For the finite consequence restrict \(a\) to the core first paths
\[
\begin{array}{c|c}
 \nu=0 &[11/50,1/2]+ic_1\quad\hbox{or}\quad1/2+i[c_1,0],\\
 \nu=1 &[11/50,1/2]+i/100\quad\hbox{or}\quad1/2+i[0,1/100].
\end{array}                                                    \tag{7}
\]
Let \(\mathcal A_N(a,q)\) be the exact first upper correction
at height \(h_U\) over the inward half-grid version of \(I_q\).
Let \(\mathcal B_N(q,z)\) be any one of the third zero-mode
horizontal at height \(h_3\), its lower correction at height
\(-L\), or its upper correction at height \(1/5\), on the
same limiting interval. The exact definitions are in Section 5.
On the fixed original ordinary-color disk, after shrinking it if
needed, both parities and both second Fourier choices obey
\[
\begin{split}
 &|U_{1,N}(w,X)d_N(X)X^{-\nu N}\mathcal A_N(a,q)
             d_N(Y)Y^{-\mu N}\mathcal B_N(q,z)|\\
 &\hspace{20mm}\le C N^B
               e^{N\{\Lambda_{123}(z)-1/324\}},\qquad
 X=e^{-2\pi ia},\ Y=e^{-2\pi iq},\quad \mu=0,1.
\end{split}                                                     \tag{8}
\]
There is no third-coordinate halfweight for type three. Integrating
these specified currents over any core first piece retains its
original density and only changes the polynomial prefactor.

Equation (8) by itself does not replace \(\mathcal B_N\) by the
complete \(C_{0,N}\). Section 6 proves that stronger conclusion
on \([1/2,18/25]\), using additional endpoint and physical-row
comparisons. Section 7 preserves the distinction beyond that interval.

## 2. The first maximizing numerator

Set
\[
 D=|1-e^{-2\pi iq}|,\qquad
 N_2(t)=|1-\sqrt2e^{-2\pi i(q+t)}|.
\]
At any maximizer in (4),
\[
                           N_2\le D.                     \tag{9}
\]
For \(q\ge5/8\), this is pointwise on \(I_q\). Indeed the
shifted cosine increases up to the wall, so its worst value is at
\(t=1/8\). With \(\theta=2\pi(q-1/2)\),
\[
 D^2-N_2(1/8)^2=-1+2\sin\theta\ge\sqrt2-1>0.
                                                               \tag{10}
\]
For \(q\le5/8\) and \(t\ge1/5\), it suffices to take
\(t=1/5\). The difference is
\[
 -1+2\cos\theta-2\sqrt2\cos(\theta+2\pi/5),
                  \qquad 0\le\theta\le\pi/4.
\]
Its variable part has at most one critical point on this interval,
which is a maximum. Both endpoint differences are positive: at zero
use \(2\sqrt2\cos(2\pi/5)<1\), and at \(\pi/4\) use
\(\cos(13\pi/20)<0\).

It remains to exclude a maximizing point with \(t<1/5\) and
\(N_2>D\). The incoming folded square and own square satisfy
the bounds in the finite-upper-current proof,
\[
 N_a^2>18/5,\qquad D_s^2<54/25.
\]
Since \(D^2\ge2+\sqrt2>17/5\), the squared private force is
then greater than
\[
                 \frac{(18/5)(17/5)}{(54/25)^3}>1;
\]
the cleared comparison is \(191250>157464\). The real private
derivative is positive. Such a point cannot maximize at an interior
point or at the left cut. It is not the right cut either: while
\(q\le5/8\), both possible right cuts in (3) exceed \(1/5\).
This proves (9).

There is a useful sharper bound for \(1/2\le q\le21/40\):
\[
               N_2^2<31/8\quad\hbox{at every maximizer}.   \tag{11}
\]
If its real coordinate is below \(1/5\), the nonpositive
private derivative gives
\(N_2^2<(54/25)^3/(18/5)=8748/3125<14/5\).
Otherwise
\[
 N_2^2\le3+2\sqrt2\cos(2\pi/5)<31/8.
\]
The last comparison is equivalent, after positive squaring, to
\(\sqrt5>143/64\); here \(5\cdot64^2-143^2=31>0\).

## 3. The third maximizing numerator and joint transport

For \(-L\le\sigma\le17/250\), put
\[
 \rho=e^{2\pi\sigma},\quad T=\rho^{-1},\quad R=e^{2\pi c_3}.
\]
The original written radius bounds imply
\[
 13/20<\rho,R<31/20,\qquad 13/20<T<151/100.                \tag{12}
\]
At a third main maximum the incoming derivative is
\(\log(N_3/D)\), where
\[
                       N_3=|T-e^{-2\pi i(q+t)}|.
\]
The actual private force is greater than one on
\[
 1/8\le t\le\min\{21/100,(1-q)/2\}.                    \tag{13}
\]
Indeed \(q+2t\le1\) makes the folded incoming square at least
the own square. Also \(\cos2\pi t>6/25\), and
\(b+t\in[69/200,33/50]\subset(1/3,2/3)\), so the outgoing
square minus the own square exceeds
\[
 \rho\{(R^2-1)\rho+R+12/25\}>0.
\]
If \(R<1\), the braces exceed
\[
 ((13/20)^2-1)(31/20)+13/20+12/25=1879/8000;
\]
if \(R\ge1\), positivity is immediate. The elementary cosine
witness uses
\(\cos(21\pi/50)=\sin(2\pi/25)>6/25\), from
\(\sin u\ge u-u^3/6\) and the original bounds on \(\pi\).
Every right cut relevant to (13) is strictly larger than its upper
endpoint. Thus a maximum occurs beyond (13).

When \(1/2\le q\le21/40\), (13) gives \(t\ge21/100\).
Consequently
\[
 N_3^2\le1+(151/100)^2+(151/50)(44/175)<81/20,
 \qquad D^2>159/40.                                      \tag{14}
\]
Here \(\sin(2\pi/25)<44/175\), and
\(\cos(\pi/20)>1-\pi^2/800>79/80\).
Combining (11) and (14),
\[
 N_2^2N_3^2<(31/8)(81/20)<(159/40)^2<D^4,
                                                               \tag{15}
\]
where the middle cleared comparison is \(25110<25281\).

For the remainder of the interval, every third maximizing numerator
also satisfies \(N_3<D\). Three elementary ranges prove this.

* On \([21/40,29/50]\), the barrier is still \(21/100\).
  It gives \(N_3^2<18/5\), using
  \(\sin(3\pi/100)<33/350\), whereas
  \(D^2>37/10\), using \(\cos(4\pi/25)>17/20\).
* On \([29/50,7/10]\), the barrier is \((1-q)/2\).
  Put \(s=\sin\pi(q-1/2)\in[0,3/5]\). Then
  \(N_3^2\le1+T^2-2Ts\) and \(D^2=4(1-s^2)\).
  The difference has the required sign because
  \(4s^2-2Ts+T^2-3<0\) on the rectangle in (12).
  Convexity in each variable reduces this to its four endpoints;
  at \(s=0\) use \(T^2<5/2\), and at \(s=3/5\) the two
  endpoint values of \(T^2-6T/5-39/25\) are
  \(-767/400\) and \(-10919/10000\).
* On \([7/10,7/8]\), the pointwise prewall bound at \(t=1/8\)
  suffices. With \(\theta=2\pi(q-1/2)\),
  \[
  D^2-N_3^2\ge1-T^2+(2-\sqrt2T)\cos\theta
                                      +\sqrt2T\sin\theta.
  \]
  Every interior critical point of the sinusoidal part is a maximum on
  \([2\pi/5,3\pi/4]\), so its minimum is at an endpoint.
  At the left endpoint the expression is greater than
  \(8/5-T^2+4T/5>0\); its two endpoint values are
  \(679/400\) and \(5279/10000\). Use
  \(\cos(2\pi/5)>3/10\), \(\sin(3\pi/20)>2/5\).
  At the right endpoint it is
  \(2-\sqrt2-(T-1)^2>1/2-(51/100)^2>0\).

The trigonometric witnesses here use only the sine and cosine
Taylor inequalities and \(25/8<\pi<22/7\); no trigonometric
value has been evaluated numerically.

Equations (9), (15) and these three ranges show that the sum of the
two outgoing/incoming derivatives at any pair of maximizing points
is at most zero. At a moving right-cut maximum the one-sided
private derivative is nonnegative, and \(r'(q)\le0\), so the
additional endpoint-motion term is nonpositive. The intervals are
compact and remain in fixed regular strips. Their maxima are
locally Lipschitz; differentiating at almost every parameter value,
or using the upper one-sided envelope derivative, proves (5).
The kink where the fixed and moving cuts meet is covered by the
same one-sided argument. No maximizer is assumed to stay interior.
The same argument applied to (9) alone also shows that \(A(q)\)
is nonincreasing.

For \(\sigma=1/5\), one instead has \(1/4<T<1\):
\(\log4>112/81>44/35>2\pi/5\).
The bound \(N_3\le D\) is pointwise: on \([1/2,5/8]\)
use \(N_3^2\le1+T^2+\sqrt2T\le2+\sqrt2\le D^2\);
on \([5/8,7/10]\) use \(N_3^2\le1+T^2\le2<D^2\).
On the final range use the same endpoint calculation, now with
\(1/4\le T\le1\); its right endpoint is at least
\(2-\sqrt2-9/16>0\), since \(\sqrt2<23/16\).
This proves the remaining assertion of Proposition 1.

## 4. Original half-face calibration

The finite-upper-current theorem gives
\[
                       A(1/2)<M_2(a)-1/162.              \tag{16}
\]
The extension of the third main interval from \(3/20\) down to
\(1/8\) does not change its maximum at the half face: (13)
proves strict increase throughout that added interval.

At this face put \(I(\eta)=\Im Q_{0,s}(t+i\eta;1/2,z)\).
The original curvature also extends to the added interval down to
\(1/8\). To check this directly, put \(A=\cosh2\pi\eta\).
The incoming half-shifted cotangent is negative. Whenever the
outgoing shifted cotangent is positive, \(t<7/25\), and
\[
 2\Re\cot\pi(t+i\eta)>\frac{7/5}{A+1/5},\qquad
 \Re\cot\pi(t+z+i\eta)
              <\frac{7/8}{(13/20)A+1/2}.
\]
Here \(b+t>1/3\), so its shifted cosine is below \(-1/2\)
and its positive shifted sine is below
\(\sin(31\pi/100)<\sqrt3/2<7/8\). The own sine is above
\(7/10\) and its cosine above \(-1/5\). Cross multiplication
gives positive coefficients \(91/100-7/8\) and
\(7/10-7/40\). Thus \(\Re Q_{0,ss}<0\) on the full added
domain at every height. Its exact limiting imaginary derivatives
are \(\pi\) below and \(-2\pi b\) above. Consequently
\[
 I(\eta)<\pi\quad(\eta\le0),\qquad
 I(\eta)>-9\pi/10\quad(\eta\in\mathbb R).               \tag{17}
\]
For the lower-line maximum, (13) restricts \(t\ge21/100\).
At height zero its exact argument is bounded by
\[
 I(0)\le\pi\max\{t,1-2b-t\}\le\pi/2.
\]
The original all-height curvature at the half face on this
restricted interval is negative, hence \(I(\eta)\le I(0)\)
for \(\eta\ge0\). Since \(\partial_\eta\Re Q_0=-I\),
\[
 \Re Q_0(t-iL;1/2,z)-2\pi L
 <\Re Q_0(t+ih_3;1/2,z)-31\pi/1000.                     \tag{18}
\]
For \(h_3\ge0\), the possible cost from \(-L\) to \(h_3\)
is at most \(\pi L+\pi h_3/2\); subtracting \(2\pi L\)
leaves \(\pi(L-17/500)=31\pi/1000\).
For \(h_3<0\), (17) gives the larger reserve \(\pi L\).
The actual lower height \(h_3\) is never below \(-L\).

Likewise (17), including the added interval, gives
\[
 \Re Q_0(t+i/5;1/2,z)-2\pi/5
 <\Re Q_0(t+ih_3;1/2,z)-323\pi/2000,                    \tag{19}
\]
because the largest cost is
\((9\pi/10)(1/5+13/200)=477\pi/2000\).
Taking the relevant maxima and using Proposition 1 proves (6).

## 5. Literal finite currents and Fourier choices

Use the original negative-root factorial interpolation
\[
 \Pi_N(w)=G_N(Nw)\exp\{(\pi i/2)[N(w-w^2)-w]\},
 \qquad E_N(w)=1/\Pi_N(w),
\]
and the literal row
\[
 T_{\epsilon,N}(s;a,b)=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+b)
                                 E_N(a)E_N(b)E_N(s)^{2+\epsilon}.
                                                               \tag{20}
\]
Choose inward half-grid cuts \(\ell_N\in[1/8,1/8+1/N]\),
\(r_N\in[r(q)-1/N,r(q)]\). Then
\[
 \mathcal A_N(a,q)=\frac N{2i}
 \int_{r_N+ih_U}^{\ell_N+ih_U}
 T_{1,N}(s;a,q)\{\cot(\pi Ns)+i\}\,ds.                 \tag{21}
\]
The three choices for \(\mathcal B_N\) are
\[
\begin{split}
 &N\int_{\ell_N+ih_3}^{r_N+ih_3}T_{0,N}(s;q,z)\,ds,\\
 &\frac N{2i}\int_{\ell_N-iL}^{r_N-iL}
                    T_{0,N}(s;q,z)\{\cot(\pi Ns)-i\}\,ds,\\
 &\frac N{2i}\int_{r_N+i/5}^{\ell_N+i/5}
                    T_{0,N}(s;q,z)\{\cot(\pi Ns)+i\}\,ds.
\end{split}                                                     \tag{22}
\]
These are the original orientations, zero-mode density and residue
scalars. All shifted arguments remain before real part one by
(3), and all heights remain in fixed compact sets. The original
uniform factorial upper expansion and the exact cotangent estimates
give their respective rates in (6), with polynomial prefactors and
one arbitrarily small prescribed total allowance. Inward rounding
does not enlarge either maximizing interval. No numerator factor is
divided out at a zero.

For real \(q\ge1/2\), the complete second Fourier upper rate is
zero: \(\Re g(q)\ge0\), so
\(\max\{-\Re g(q),0\}=0\). Both second monomials have unit
modulus. This is the full polynomial upper bound, not replacement
of \(d_N\) by its factorial alternative. The cap alternatives,
first weight and first monomial are independent of \(q\).
The original raw half-face calibration in the finite-upper-current
theorem compares every such cap choice times \(M_2+M_3\) to
the same \(\Lambda_{123}(z)\). Apply (6) and allocate less
than \(1/324\) to all source and ordinary-color continuation
allowances. This proves (8), with fixed derivatives on smaller
ordinary disks and both parities.

## 6. The complete third factor through eighteen twenty-fifths

**Theorem 2.** In (3) take \(Q=18/25\). Choose the limiting right
cut sufficiently close to one half, and then \(\varepsilon\)
sufficiently small, both before
\(N\). For \(1/2\le q\le18/25\), replace
\(\mathcal B_N(q,z)\) in (8) by the complete original
\(C_{0,N}(Y,Z)\). The resulting bound holds with the same
gap \(1/324\), after allocating the fixed source tolerances.
It holds for every real \(q\) in this interval, not only at
physical roots of unity. It includes the full first weight on (7),
both second Fourier sectors and all finite third rows.

Here is a complete source proof. Put \(\delta=1-q\), so
\(7/25\le\delta\le1/2\), and retain the third real rate
\[
 E(t;q,z)=I_q(t)+I_z(t)-2J(t),\qquad
 I_z(t)=\int_0^t\log|1-e^{-2\pi i(z+v)}|\,dv,
 \quad J(t)=\int_0^t\log(2\sin\pi v)\,dv.              \tag{24}
\]
Extend \(J\) periodically from \([0,1]\). For real \(q\),
\(I_q(t)=J(q+t)-J(q)\), with this continuous real primitive
and its integrable zeros.

### Real cuts and the zero-mode joins

At the incoming wall the continuous real rate is
\[
                 W(q,z)=E(\delta;q,z)
                         =I_z(\delta)-J(\delta).         \tag{25}
\]
It is no larger than the actual-height main value at that wall:
\[
               W(q,z)\le\Re Q_0(\delta+ih_3;q,z).       \tag{26}
\]
For negative private height, the incoming shifted argument on this
wall is zero. The own argument is at most
\(\pi(1/2-\delta)\); the outgoing argument is at least
\(\pi(1-2b-2\delta)\), because \(b+\delta\ge1/2\).
Thus \(\Im Q_{0,s}\ge2\pi(q-b)>0\).
For positive private height the incoming argument, in the prewall
limit, is \(-\pi\), the own argument is at least
\(\pi(1/2-\delta)\), and the outgoing argument is at most zero.
Hence \(\Im Q_{0,s}\le0\). Integration of
\(\partial_\eta\Re Q_0=-\Im Q_{0,s}\) proves (26) on
both sides, including \(h_3=0\).

All these action functions are uniformly continuous at their
integrable wall limits on the stated compact family. Consequently
the real rate at \(r(q)\), and the physical rates between
\(r(q)\) and \(\delta\), differ from (25) by an arbitrarily
small prescribed allowance when \(1/2-r_0\) and
\(\varepsilon\) are sufficiently small. Likewise the main value
at the wall is at most \(B_{h_3}(q)\) plus that allowance.
This is a comparison of continuous rates before \(N\) is chosen.

At the real left cut, \(E(1/8;q,z)\) is nonincreasing in
\(q\): its derivative is
\(\log|1-e^{-2\pi i(q+1/8)}|-\log|1-e^{-2\pi iq}|\le0\).
At the half face it is at most the original real left rate
\(E(3/20;1/2,z)\), by (13) at height zero.
Since \(A(q)\) is separately nonincreasing by (9), the original
calibration pays the first upper correction paired with this cut.

The curvature proof in Section 4 holds without change throughout
the prewall rectangle for \(q\ge1/2\): its incoming shifted
cotangent is still negative. Thus both unweighted zero-mode joins
are bounded by their actual-height and real-cut endpoints. The
imaginary derivative is strictly decreasing in private height,
with exact limits \(2\pi q\) below and \(-2\pi b\) above.
In particular
\[
                 -9\pi/10<\Im Q_{0,s}<36\pi/25.         \tag{27}
\]
Each weighted vertical half therefore decreases away from its
real cut. All four are paid by the same two real-cut bounds.
The three horizontal currents are already paid by (6).

### Every low and postwall-middle physical row

For \(0\le t\le1/8\), the same incoming derivative shows
\(E(t;q,z)\le E(t;1/2,z)\). The original half-face low-row
bound pays this entire group by its real left profile.

For \(\delta\le t\le1/2\), the real rate strictly decreases
from its wall value. Here is an elementary uniform row-ratio proof.
Put \(v=\cot\pi t\in[0,1]\) and \(R=e^{2\pi c_3}\).
The incoming modulus divided by its own modulus equals
\[
 \frac{\sin\pi(t-\delta)}{\sin\pi t}
           =\cos\pi\delta-v\sin\pi\delta
           <2/3-3v/4.                                   \tag{28}
\]
We used \(\sin(7\pi/25)>3/4\) and
\(\cos(7\pi/25)<2/3\). For example
\(\sin(7/8)\ge7/8-(7/8)^3/6>3/4\), and the cosine
bound follows by squaring. The expression in (28) is nonnegative
on this domain.

Because \(b+t\in[1/2,19/20]\), the outgoing squared
modulus is largest at \(b=11/50,R=31/20\). The radius
comparison uses \(31/20+13/20>2\). For this worst case,
\[
 \frac{|1-Re^{-2\pi i(b+t)}|^2}{4\sin^2\pi t}
 =\frac{(R-1)^2}{4}(1+v^2)
                         +R(\sin\pi b\,v+\cos\pi b)^2.
\]
Here \(\sin(11\pi/50)<7/10\) and
\(\cos(11\pi/50)<4/5\). The latter follows from
\(11\pi/50>2/3\) and
\(\cos(2/3)\le1-2/9+2/243=191/243<4/5\).
Therefore
\[
 (2/3-3v/4)(7v/10+4/5)\le8/15,
 \qquad (2/3-3v/4)^2(1+v^2)\le8/9.
\]
The squared original row ratio is consequently less than
\[
               \frac{121}{1600}\frac89
                  +\frac{31}{20}\left(\frac8{15}\right)^2
                     =\frac{4573}{9000}<1.              \tag{29}
\]
Integrating its logarithm from the wall proves
\(E(t;q,z)\le W(q,z)\). The logarithmic zero at the wall is
integrable and is not divided out. This pays the whole postwall
middle block, including rows which are nonzero off the physical grid.

### Every high physical row

Let \(d=c_3\), \(H=|d|\), and retain the original disk
primitive \(G_H(u)=\Re g(u-iH)\). It is odd and periodic.
For \(t=1-v\), \(0\le v\le1/2\), exact reflection of the
absolute row rate gives
\[
\begin{split}
 E(1-v;q,z)={}&J(\delta)-J(\delta+v)
       +G_H(b-v)-G_H(b)+2J(v)+2\pi d_+(1-v).
\end{split}                                                     \tag{30}
\]
The literal last carrier is \(E(1;q,z)=2\pi d_+\).
For \(0<v\le1/10\), the first difference in (30) is at
most \(-v\log(3/2)\): on its interval
\(2\sin\pi(\delta+u)>3/2\).
The next difference is at most \(v\log(3/2)\), because
\[
 |1-e^{-2\pi H-2\pi i(b-u)}|>2/3,
              \qquad 0\le u\le v\le1/10.
\]
Indeed \(b-u\in[3/25,9/20]\); below one quarter its radial
minimum is the sine, with
\(\sin(6\pi/25)>\sin(3/4)\ge87/128>2/3\), and above
one quarter its modulus is at least one. It follows that
\(E(1-v;q,z)<2\pi d_+\) on this first range.

For \(1/10\le v\le1/2\), use the all-angle leg inequality
\[
                 G_H(b-v)+J(v)+G_H(1/2-b)\le0.
\]
Writing \(H_0(z)=E(1/2;1/2,z)\) and
\(F_\delta(v)=J(\delta)+J(v)-J(\delta+v)\), (30) implies
\[
 E(1-v;q,z)\le H_0(z)+F_\delta(v)+\pi d_+(1-2v).        \tag{31}
\]
The function \(F_\delta\) is convex in \(v\), since
\(\pi\cot\pi v-\pi\cot\pi(\delta+v)>0\), and
\(F_\delta(1/2)=J(\delta)+J(1/2-\delta)\le0\).
Furthermore
\[
 F_\delta(1/10)
 \le\frac1{10}\{\log(2\pi/15)-1\}<-9/50.             \tag{32}
\]
For this, use \(2\sin\pi u\le2\pi u\) in \(J(1/10)\)
and \(2\sin\pi(\delta+u)>3/2\) in the increment.
Then \(2\pi/15<3/7\), and
\(\log(7/3)=2\operatorname{artanh}(2/5)>4/5\).
The convex chord between \(1/10\) and \(1/2\) now gives
\[
 F_\delta(v)\le-\frac9{40}(1-2v),\qquad
                  \frac9{40}>\frac{17\pi}{250}.         \tag{33}
\]
The last comparison follows from \(\pi<22/7<225/68\).
Equations (31)--(33) prove
\[
       E(t;q,z)\le\max\{H_0(z),2\pi d_+\}
                         \quad(1/2\le t\le1).           \tag{34}
\]
Both entries are exactly the already calibrated half-face third
half and last profiles. Their paired first rate is paid by
\(A(q)\le A(1/2)\), preserving (16).
The same raw half-face calibration also pays its left profile.
These comparisons retain the cap and first Fourier alternatives
profilewise; none is inferred from the modulus of a cancelling
finite conditional sum.

### Finite completion and normalization

Apply the original split-cotangent identity on the central private
interval \([\ell_N,r_N]\), with lower height \(-L\), upper
height \(1/5\), and actual zero-mode height \(h_3\). Retain
its \(+N\) zero mode, the two unweighted joins, both horizontal
corrections, and all four weighted vertical halves. The preceding
bounds pay every one. Equality \(h_3=-L\) is harmless: the
zero-mode and lower-correction horizontals remain separate terms
with their literal coefficients.
All remaining physical indices are in the low block, the small
prewall right collar, the postwall middle block, or the high block
just proved. The standard zero-safe product upper argument applies
to all of them: add a fixed positive regularizer inside numerator
logarithms, use its uniform Riemann-sum bound, and then let that
regularizer decrease before choosing \(N\). Its integral error
is uniformly small at each simple real zero. The denominator has
the original uniform \(O(\log N)\) error through the last indices.
This includes both parities, every revived row and the true ends.

Assign the right-collar, source and color allowances to a total less
than \(1/324\). Each paid half-face profile retains (16)'s
\(1/162\) first-upper saving, so the claimed complete paired
bound follows. The original first and second Fourier factors and
the two finite densities are exactly those of (8), (21)--(22).
No bound for the entire first conditional kernel has been substituted
for this specified upper correction.

## 7. Exact termination and the remaining interval

For a physical second value \(Y=\zeta^b\),
\(\zeta=e^{-2\pi i/N}\), the exact factor
\(p_j(Y)=(\zeta Y;\zeta)_j\) vanishes for
\(j\ge N-b\). Thus both conditional physical sums terminate
before their incoming wall. This exact fact does not extend to an
off-grid real \(Y\), where revived rows remain in the source.
It also does not delete the prewall right vertical currents.

At the continuous wall \(t=1-q=\delta\), the third real rate is
\(W(q,z)=I_z(\delta)-J(\delta)\), as in (25).
This follows directly from \(J(1)=0\) and
\(J(q)=-J(1-q)\). The rate (25) need not decrease as \(q\)
increases. When \(h_3\le0\), the original incoming argument
at this wall is zero below the real axis, and
\[
 \Im Q_{0,s}(\delta+i\eta;q,z)>0\quad(\eta<0).
\]
Indeed the elementary lower bound is either \(\pi\) or
\(2\pi(q-b)\), according to the side of the outgoing half
angle. It follows that
\(W(q,z)\le\Re Q_0(\delta+ih_3;q,z)\), in the continuous
wall limit. For \(h_3>0\), this particular comparison is not
licensed: if \(b+\delta<1/2\), the corresponding upper-half
argument bound can have the opposite sign.

Beyond \(18/25\), this note claims only the three finite horizontal
currents in (22). The complete attached source there still requires
its real-cut and unweighted-join comparisons and every physical
group outside (3), or an exact signed-current argument retaining them.
Neither physical termination nor (5) supplies those remaining bounds.
No complete first message, second period, or knot consequence is
inferred from this current theorem.

## Direct source versions

The directly used implications are: the actual bounds, original
raw half-face calibration, third all-height curvature and complete
Fourier upper bound in the half-face theorem; Proposition 1 and
the raw calibration in the finite-upper-current theorem; and the
original finite residue identity and uniform factorial interpolation.
The joint global chart fixes the exact negative-root convention in
(20).
The all-angle high-row source supplies only its leg inequality and
disk normalization here, not a theorem outside its stated sign class.
The original contour-allowance proof supplies its zero-safe finite
row argument; that argument is explicitly reapplied above to the new
compact parameter domain.

| Source | SHA-256 |
|---|---|
| research_mixed_443_half_face_finite_upper_current.md | 9a40ef23ac4887e32be05522ea10f9b3a1b481e74111dca97928e360cd0e4eca |
| research_mixed_443_complete_second_half_face.md | 11243b9bbf31c2ab1ec662fcb6b47f56f8017a8307f424b5bdf5efcf5d83079b |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

Author full proof readback, all seven directly used source-implication
reads, and all seven metadata hash checks are complete. Independent
full proof/direct-source review and root review remain required.
No mathematical numerical evaluation, test, import, compilation or
frozen-source edit was used.
