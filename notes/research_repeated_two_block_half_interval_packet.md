# The complete two-block cap coefficient on a macroscopic half interval

Research proof, 8 November 2026. No numerical evaluation is used.

The actual interior coefficient constructed in
[the first seed theorem](research_repeated_two_block_interior_cap_seed.md)
has a complete nonzero packet for every physical scaled row
\(0\le n/N\le1/2\). The proof includes the full original sum, rather
than continuing only its critical equation. It determines the exact
exponential norm of the initialized vector: its complementary half
has a strictly smaller rate. This determines the sharp second capped
moment as an explicit variational action and improves the lower bound
for every longer repeated block. The sharp higher moments and the
geometric volume identity remain separate problems.

## 1. Exact source and statement

Retain \(D=N-1\), \(q=e^{\pi i/N}\),
\(S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N)\),
\(\kappa=q^{D^2/2}\), and the full original matrix \(M\).
Put \(K_2=(M^2)^*M^2\) and \(\beta_N=K_2\mathbf e_0\).
The exact identity of the seed theorem is
\[
 (\beta_N)_n
 =i^nq^{-n(n+1)/2-nD}\frac{N^2}{S_n^2}T_N(n/N),
 \qquad
 T_N(n/N)=\sum_{j=0}^{D-n}q^{nj}\frac{S_{j+n}}{S_j^3}.
 \tag{1}
\]
This is an identity of the full original Newton matrices, including
their normal directions and both quantum-level parities.

Use the same original primitive and phase
\[
 J(z)=\int_0^z\operatorname{Log}(2\sin\pi w)\,dw,
 \qquad F(x,t)=J(x+t)-3J(x)+i\pi tx.
 \tag{2}
\]
The branches continue the real interval \((0,1)\). Write
\[
 c=-2J(1/6),\qquad b_2=-4J(1/4),
 \qquad \Phi(t)=F(x(t),t),
 \tag{3}
\]
where \(x(0)=1/6\) and \(F_x(x(t),t)=0\) on the branch proved
below. Set
\[
 A(t)=\sqrt{\frac\pi2}
       \sqrt{\frac{\sin\pi(x(t)+t)}{\sin^3\pi x(t)}}
       \frac1{\sqrt{-F_{xx}(x(t),t)}}.
 \tag{4}
\]
All roots continue the positive choices at zero.

**Theorem 1.** Uniformly over all physical rows
\(0\le n\le\lfloor N/2\rfloor\), through all integer levels,
\[
 \boxed{\quad
 T_N(n/N)=N^{-1/2}A(n/N)e^{N\Phi(n/N)}(1+O(N^{-1})).
 \quad}
 \tag{5}
\]
The branch, action, and nonzero symbol in (3)--(4) are holomorphic
on a fixed neighborhood of \([0,1/2]\). This assertion about their
analytic continuation does not turn the moving upper endpoint in
the finite sum (1) into a noninteger row.

## 2. The original selected root on the entire interval

Put \(p=e^{2\pi it}\) and \(u=e^{2\pi ix}\).
Exponentiating the original force gives
\[
 e^{F_x}=\frac{u(1-pu)}{(u-1)^3}.
 \tag{6}
\]
The critical cubic is therefore
\[
 u^3+(p-3)u^2+2u-1=0,
 \qquad u(0)=e^{\pi i/3}.
 \tag{7}
\]
The selected root is simple on the whole arc \(p=e^{i\theta}\),
\(0\le\theta\le\pi\). Indeed the discriminant is
\[
 \mathcal D(p)=4p^3-32p^2+48p-23.
 \tag{8}
\]
For \(0<\theta<\pi\), writing \(z=\cos\theta\),
\(\Im\mathcal D=4\sin\theta(4z^2-16z+11)\).
Its only possible interior zero of the imaginary part has
\(4z^2-16z+11=0\), at which the real part is \(9-8z>0\).
At the two endpoints the discriminants are \(-3\) and \(-107\).
Thus there is no double root.

For \(\Im p>0\), a real root would have
\(\Im p\,u^2=0\), which is impossible in (7). At \(p=1\)
the roots are \(1,e^{\pi i/3},e^{-\pi i/3}\); the root through
one enters the lower half-plane because \(du/d\theta=-i\)
there. Consequently (7) has exactly one upper root on the open arc.
At \(p=-1\), the negative discriminant gives one real root and a
nonreal conjugate pair; the upper root is the endpoint of this same
branch.

Here are explicit guards for this root:
\[
 \boxed{\quad
 \frac12<|u(t)|<1,\qquad
 \frac16<\Re x(t)<\frac14,\qquad
 0<\Im x(t)<\frac{\log2}{2\pi}
 \quad(0<t\le1/2).
 \quad}
 \tag{9}
\]
To prove them, solve (7) for
\[
 p=3-u-2u^{-1}+u^{-2}.
 \tag{10}
\]
On \(u=e^{i\varphi}\), \(0<\varphi<\pi\), put
\(z=\cos\varphi\). Then
\[
 \Im p=\sin\varphi(1-2z),\qquad
 |p|^2-1=4(1-z)^2(1-2z).
 \tag{11}
\]
An upper \(p\) on the unit circle cannot occur on this boundary.
The local derivative
\(x'(0)=1/2+i/(2\sqrt3)\) from the seed theorem places the
branch inside \(|u|<1\) immediately, and (11) prevents a later
exit. At the endpoint \(p=-1\), the equality case in (11) would
give \(p=1\), so the radius remains strictly less than one.

On the lower angular boundary \(u=r e^{\pi i/3}\), with
\(0<r<1\), the condition \(\Im p>0\) requires
\(r>g=(\sqrt5-1)/2\), and
\[
 |p|^2-1=\frac{(r-1)Q(r)}{r^4},\qquad
 Q(r)=r^5-2r^4+4r^3+r-1.
 \tag{12}
\]
One has \(Q'(r)=r^2(5r^2-8r+12)+1>0\) and
\(Q(g)=20g-12>0\). Hence this expression is negative wherever
an upper \(p\) could occur, excluding a unit-circle crossing.
The same argument includes the possible endpoint \(r=g\) at
\(p=-1\). On the other boundary \(u=ir\), putting \(R=r^2\),
\[
 |p|^2-1=\frac{R^3+4R^2-2R+1}{R^2}>0,
 \tag{13}
\]
since \(4R^2-2R+1>0\). The local positive real derivative of
\(x(t)\) and these two barriers prove the angular bounds.

It remains to exclude \(|u|=1/2\). Within the angular sector
already proved, write \(u=\tfrac12e^{i\varphi}\), so
\(0\le z=\cos\varphi\le1/2\). Direct substitution gives
\[
 4(|p|^2-1)=-64z^3+224z^2-188z+49\ge3.
 \tag{14}
\]
The displayed polynomial is decreasing on \([0,1/2]\): its
derivative is increasing there and has value \(-12\) at \(1/2\).
Its endpoint value is three. This excludes the inner radius and
finishes (9).

The original primitive strips are now guarded:
\(0<\Re x<1/4\) and \(0<\Re(x+t)<3/4\).
All divisors in (6) are nonzero. The continuous logarithmic lift of
(6) begins with \(F_x=0\); hence it remains zero, not an unspecified
multiple of \(2\pi i\). Simplicity and compactness provide the
asserted fixed holomorphic neighborhood.

## 3. All-height concavity and quantitative real-tail gaps

Set \(a=1/18\), and write
\[
 C(z)=\Re\cot\pi z
 =\frac{\sin(2\pi\Re z)}
        {\cosh(2\pi\Im z)-\cos(2\pi\Re z)}.
 \tag{15}
\]
For \(a\le x<1/2\), real \(0\le t\le1/2\), and any real
height \(h\),
\[
 \Re F_{xx}(x+ih,t)
       =\pi[C(x+t+ih)-3C(x+ih)]<0.
 \tag{16}
\]
If \(x+t\ge1/2\), the first term is nonpositive and the second
positive. Otherwise the denominator in (15) increases under the
shift by \(t\). For \(x\le1/4\), the sine ratio is at most
\(1/\sin(2\pi a)<3\); for \(x\ge1/4\), it is at most one.
The elementary bound \(\sin(\pi/9)>1/3\) follows from
\(\pi>25/8\), \(\pi<22/7\), and
\(\sin q\ge q-q^3/6\). This proves (16).

Let \(h_c=\Im x(t)\) and \(M(t)=\Re\Phi(t)\).
The vertical convexity supplied by (16), at the fixed real point
\(1/4\), gives the supporting-line bound
\[
 \begin{split}
 M(t)&\ge \Re F(1/4+ih_c,t)\\
     &\ge J(1/4+t)-3J(1/4)-\pi t h_c\\
     &\ge R(t):=J(1/4+t)-3J(1/4)-\tfrac t2\log2.
 \end{split}
 \tag{17}
\]
The first inequality follows from horizontal concavity and the
selected critical point. At \(t=0\) the same argument uses
\(h_c=0\). Since
\(R'(t)=\log(2\sin\pi(1/4+t))-\tfrac12\log2\ge0\),
\[
                         M(t)\ge R(t)\ge b_2/2.
 \tag{18}
\]

The low physical rows have a stronger gap. Define
\[
 D(t)=R(t)-[J(a+t)-3J(a)].
 \tag{19}
\]
Its second derivative is
\(\pi\cot\pi(1/4+t)-\pi\cot\pi(a+t)<0\), so its minimum
on \([0,1/2]\) occurs at an endpoint. The following written
bounds suffice:
\[
 -J(a)<\frac{1+\log3}{18}<\frac7{60},\qquad
 J(1/2+a)<\frac7{180},\qquad
 \log2<\frac7{10},\qquad b_2>\frac{63}{110}.
 \tag{20}
\]
The first follows from \(2\sin\pi s\ge6s\) on
\([0,1/6]\), and \(\log3<11/10\). The second follows by
integrating \(J'\le\log2\) from \(1/2\). For the last, let
\(G\) be Catalan's constant. The elementary alternating integral
series gives
\[
 G>1-\frac19+\frac1{25}-\frac1{49}
   =\frac{10016}{11025}>\frac9{10},
 \qquad b_2=\frac{2G}{\pi}>\frac{63}{110}.
 \tag{21}
\]
Thus
\[
 D(0)>\frac7{132},\qquad
 D(1/2)>\frac{63}{110}-\frac{203}{360}
       =\frac7{792},\qquad
 D(t)>\frac7{792}.
 \tag{22}
\]
For \(0<x\le a\), the physical profile
\(J(x+t)-3J(x)\) is strictly increasing in \(x\):
\(\sin\pi(x+t)\ge\sin\pi x\) on this entire parameter
range, and \(2\sin\pi x<1\). Hence (22) pays every physical
row \(j/N\le a\), including zero, with its original carrier.

For the high physical rows \(x\ge1/2\), \(x+t\le1\),
\(J(x)\ge0\) and \(J(x+t)\le c/2\), so
\[
 J(x+t)-3J(x)\le c/2<M(t).
 \tag{23}
\]
The elementary bound \(c<1/3\) is proved in
[the original next-step profile](research_three_crossing_next_step_profile.md),
Section 4. Equations (18) and (20) leave a reserve
\((b_2-c)/2>79/660\). Uniform continuity on the closed
triangle \(x,t\ge0,x+t\le1\) therefore permits a fixed
\(b<1/2\), sufficiently close to \(1/2\), such that all rows
\(x\ge b\) have a uniform strict gap below \(M(t)\).
The chosen \(b\) is independent of \(t,N\), and exceeds \(1/4\).
No continuation of a regular factorial expansion across a true end
is used here: the endpoint-uniform absolute factorial bound pays
the entire omitted physical sum with only polynomial factors.

## 4. Complete finite currents for both height signs

Retain precisely \(aN<j<bN\), with adjacent half-grid cuts
\(a_N,b_N\). These rows occur in (1) for every physical
\(0\le n/N\le1/2\) once \(N\) is sufficiently large.
Use the same exact interpolant as in the seed theorem,
\[
 f_N(x,t)=e^{i\pi Ntx}\frac{G_N(N(x+t))}{G_N(Nx)^3}
 =\frac1{2N}
   \sqrt{\frac{\sin\pi(x+t)}{\sin^3\pi x}}
       e^{NF(x,t)}(1+O(N^{-1})).
 \tag{24}
\]
The canonical factorial lemma in
[the original factorial source](../papers/conway-asymptotics/factorial.tex)
provides this holomorphic expansion, with fixed derivatives, on
each compact contour used below. In particular the scaled arguments
have real parts in \((0,1)\), because \(b+t<1\).

The already proved seed theorem gives (5) for a fixed interval
\(0\le t\le\tau_0\). It remains to cover the compact interval
\(\tau_0/2\le t\le1/2\). Here (9) makes \(h_c\) uniformly
positive. On the horizontal line at height \(h_c\), (16) and
the critical equation imply
\[
                  \Re F(x+ih_c,t)\le M(t)
                         \qquad(a_N\le x\le b_N),
 \tag{25}
\]
with a strict uniform loss away from the critical point. Exact
conjugation of the original primitives, retaining the chirp, gives
\[
       \Re F(x-ih,t)=\Re F(x+ih,t)+2\pi th.
 \tag{26}
\]
Consequently the upper and lower cotangent remainder profiles at
heights \(\pm h_c\) are bounded respectively by
\[
                  M(t)-2\pi h_c,\qquad
                  M(t)-2\pi(1-t)h_c.
 \tag{27}
\]
Both gaps are uniform and positive on the compact parameter interval.
Increase the rectangle height slightly beyond \(h_c\); by uniform
continuity the two complete horizontal remainders retain a strict
gap, while the saddle lies strictly inside. A finite cover in \(t\)
can use fixed heights on each member.

On a half-grid vertical cut, the upper or lower cotangent remainder
is bounded by a constant times \(e^{-2\pi N|h|}\), including
the real midpoint. Its exponential profile is
\(\Re F(a_N+ih,t)-2\pi|h|\), or the analogous expression at
\(b_N\). By (16), each half is convex as a function of height.
Its real endpoint is paid by (22)--(23), and its outer endpoint by
(27) and the small height enlargement. Thus all four complete
vertical remainders have a fixed strict gap. The half-grid shifts
change the real profiles by only \(O(N^{-1})\) on the retained
regular domain. If \(a_N\) lies just below \(a\), strict
negativity in (16) on each compact finite rectangle persists on
this \(O(N^{-1})\) enlargement; the same applies to the other cut.

The counterclockwise finite residue identity with
\(\pi N\cot(\pi Nx)\) is exact. Splitting its upper and lower
constant modes \(-i\) and \(+i\), including the vertical parts,
leaves precisely
\(N\int_{a_N}^{b_N} f_N(x,t)\,dx\).
The preceding paragraphs pay its two horizontal and four vertical
weighted remainders. Deform this unweighted integral to the line
at \(h_c\), retaining both vertical joins. A join's real endpoint
is paid by (22)--(23); its endpoint at \(h_c\) has a strict gap
by horizontal concavity and the fixed separation of either cut
from \(\Re x(t)\). Vertical convexity then pays the entire join.

There is now one nondegenerate horizontal Gaussian, with the
original square root. The exact \(+N\) density, the \((2N)^{-1}\)
amplitude in (24), and \(\sqrt{2\pi/N}\) from that Gaussian give
exactly \(N^{-1/2}A(t)\). The omitted physical rows were paid in
Section 3, including both true ends. The finite cover and the
overlapping small-\(t\) theorem give a uniform relative
\(O(N^{-1})\) error on all of \([0,1/2]\). The explicit branch
and symbol agree on overlaps. This proves Theorem 1 without
discarding any original row, alias, or unweighted join.

## 5. Exact rate of the whole second capped moment

Extend continuously to zero the function
\[
 \mathcal S(t)=\Re\Phi(t)-2J(t),\qquad
 \mathfrak s=\max_{0\le t\le1/2}\mathcal S(t).
 \tag{28}
\]
This is a maximum of an explicitly specified original branch, not
of freely selected roots. It is attained in the open interval.
Indeed differentiation of (2), using criticality, gives
\[
 \mathcal S'(t)
   =\log\frac{|1-pu|}{|1-p|^2}\quad(0<t\le1/2).
 \tag{29}
\]
This tends to \(+\infty\) at zero. At \(t=1/2\), the numerator
is \(|1+u|<2\), while the denominator is four, so the derivative
is strictly negative. In particular \(\mathfrak s>c\), also
following from the seed expansion near zero. No uniqueness of the
maximizer is needed.

Theorem 1, (1), and the uniform factorial estimate imply
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac1N
   \log\!\left(\sum_{n=0}^{\lfloor N/2\rfloor}
                       |(\beta_N)_n|^2\right)
      =2\mathfrak s.
 \quad}
 \tag{30}
\]
For the upper bound, every summand has rate
\(2\mathcal S(n/N)+O(\log N/N)\) uniformly, including zero.
For the lower bound, take a physical row nearest an interior
maximizer and use its nonzero coefficient in (5). This retains an
actual macroscopic part of the initialized vector.

The other half is strictly smaller. For physical \(t=n/N\ge1/2\),
the summation coordinates in (1) satisfy \(0\le x=j/N\le1-t\).
The endpoint-uniform factorial estimate bounds the absolute rate of
each term in the full coefficient by
\[
 J(x+t)-3J(x)-2J(t)\le\frac c2+\frac{3c}{2}=2c<\frac23.
 \tag{31}
\]
Here \(x+t\in[1/2,1]\), \(x\in[0,1/2]\), and
\(J(t)\ge0\). Thus every such coefficient is bounded by a
polynomial times \(e^{2Nc}\), including the final physical row.

An actual interior coefficient exceeds this entire upper rate.
At \(t=1/4\), put \(f(h)=\Re F(1/4+ih,1/4)\). On
\(0\le h\le\log2/(2\pi)\),
\[
 f(0)=\frac{3b_2}{4},\qquad f'(0)=-\frac\pi4,
 \qquad f''(h)=\frac{3\pi}{\cosh(2\pi h)}
                      \ge\frac{12\pi}{5}.
 \tag{32}
\]
Horizontal concavity at the actual critical height therefore gives
\[
 \begin{split}
 \mathcal S(1/4)
 &\ge \frac{5b_2}{4}-\frac{5\pi}{384}\\
 &>\frac{63}{88}-\frac{55}{1344}
   =\frac23+\frac{41}{4928}.
 \end{split}
 \tag{33}
\]
The quadratic debit is the minimum of
\(-\pi h/4+(6\pi/5)h^2\). This calculation uses the actual
critical height guard (9), not an arbitrarily chosen index contour.
Equations (31)--(33) give a uniform exponential gap for every
coefficient in the complementary half.

Since \(\mu_{2,N}=\|\beta_N\|_2^2\), (30)--(33) prove the
sharp full rate
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac1N\log\mu_{2,N}
 =\lim_{N\to\infty}\frac1N\log|Z_{2,2,N}|
 =2\mathfrak s>\frac43+\frac{41}{2464}.
 \quad}
 \tag{34}
\]
This is an explicit variational characterization of the full original
second moment, with the unique selected cubic branch fixed in (7).
It does not require choosing a maximizer numerically or proving its
uniqueness.

For the original higher capped moments
\(\mu_{m,N}=\mathbf e_0^*K_2^m\mathbf e_0\), positivity gives
\(\mu_{2,N}=\|\beta_N\|_2^2\) and
\(\mu_{m,N}\ge\mu_{2,N}^{m-1}/\mu_{1,N}^{m-2}\).
The exact first-moment rate is \(c\), as in the seed theorem.
Thus the literal original capped word satisfies
\[
 \boxed{\quad
 \liminf_N\frac1N\log|Z_{2,m,N}|
       \ge 2(m-1)\mathfrak s-(m-2)c>mc,
                  \qquad m\ge2.
 \quad}
 \tag{35}
\]
All scalars \(Z_{2,m,N}=\kappa^{2m-1}\mu_{m,N}\) and both
parities are unchanged. For \(m=2\), equality is proved in (34).
For \(m\ge3\), (35) is a lower bound only. No identification of
\(2\mathfrak s\) with a knot-complement volume is asserted. The
different cyclic trace rate is not substituted for a capped moment.

## 6. Author refinement: unique maximum and the full moment Gaussian

The variational maximum in (28) is in fact unique and nondegenerate.
This refinement uses the complex Schur complement of the actual
phase, rather than inferring its sign from horizontal concavity alone.

For \(0<t\le1/2\), evaluate at the selected \(x=x(t)\) and put
\[
 U=\cot\pi x,\qquad V=\cot\pi(x+t),\qquad
 C=\cot\pi t\ge0,\qquad a=\Re U>0,\quad b=\Re V.
 \tag{36}
\]
One has both \(b<a\) and \(b<C\). For the first inequality,
at the fixed height \(h_c\), the real cotangent is strictly
decreasing on the full interval from \(\Re x\) to \(\Re x+t\):
its derivative has the sign of
\(\cos(2\pi s)\cosh(2\pi h_c)-1\), and (9) bounds the
product by \(5/8<1\) throughout
\([\Re x,\Re x+t]\subset[1/6,3/4]\).
For the second, if \(\Re x+t<1/2\), then
\[
 \Re\cot\pi(x+t)\le\cot\pi(\Re x+t)<\cot\pi t.
 \tag{37}
\]
If \(\Re x+t\ge1/2\), its real cotangent is nonpositive.
This is still strictly below \(C\); at \(t=1/2\) it is
strictly negative.

Let \(\mathcal F(x,t)=F(x,t)-2J(t)\). Its exact complex Hessian
at the critical point is
\[
 \operatorname{Hess}\mathcal F
       =\pi\begin{pmatrix}V-3U&V+i\\ V+i&V-2C\end{pmatrix}.
 \tag{38}
\]
The negative of its real part is positive definite. Apart from
the positive factor \(\pi\), its determinant is
\[
                     6aC-b(3a+2C)>0.
 \tag{39}
\]
If \(b<0\), this is immediate, including \(C=0\). If
\(b\ge0\), use \(b<\min(a,C)\): when \(a\le C\) the
determinant is bounded below by \(a(4C-3a)>0\), and when
\(C\le a\) by \(C(3a-2C)>0\). The two diagonal entries
are positive as well.

Set \(Q=-\operatorname{Hess}\mathcal F\) and
\(v=(-Q_{xt}/Q_{xx},1)^T\). The first coordinate of \(Qv\)
is zero, so
\[
 v^*Qv=Q_{tt}-\frac{Q_{xt}^2}{Q_{xx}}
       =-[\Phi''(t)-2J''(t)].
 \tag{40}
\]
Since \(Q\) is complex symmetric, its Hermitian real part is
the entrywise real matrix just proved positive definite. Taking
real parts in (40) therefore proves
\[
                         \mathcal S''(t)<0
                              \qquad(0<t\le1/2).
 \tag{41}
\]
Together with (29), this gives a unique
\(t_*\in(0,1/4)\) with \(\mathcal S'(t_*)=0\), and
\(\mathfrak s=\mathcal S(t_*)\).
Indeed \(|1-pu|<2\), whereas \(|1-p|^2\ge2\) for
\(1/4\le t\le1/2\), so (29) is strictly negative on that
entire interval. In particular \(\Re x(t_*)+t_*<1/2\).

On a fixed compact interval about \(t_*\), the exact coefficient
(1) and the regular factorial expansion give
\[
 |(\beta_N)_n|^2
   =N\left|\frac{A(t)}{2\sin\pi t}\right|^2
          e^{2N\mathcal S(t)}(1+O(N^{-1})),\qquad t=n/N.
 \tag{42}
\]
All other rows have a strict exponential loss: on the lower half
this follows from uniqueness of the maximum and the uniform packet,
and on the upper half from (31)--(33). The ordinary discrete Laplace
expansion in (42) now yields the complete original moment
\[
 \boxed{\quad
 \mu_{2,N}
  =N^{3/2}\mathcal D_*e^{2N\mathfrak s}(1+O(N^{-1})),
 \qquad
 \mathcal D_*=
 \left|\frac{A(t_*)}{2\sin\pi t_*}\right|^2
           \sqrt{\frac\pi{-\mathcal S''(t_*)}}>0.
 \quad}
 \tag{43}
\]
The extra \(N\) is the density of physical coefficient rows;
the Gaussian for the exponent \(2N\mathcal S\) contributes
\(\sqrt{\pi/(-N\mathcal S'')}\). The uniform relative error
in (42) remains \(O(N^{-1})\) after summing positive terms.
For the smooth main term, Taylor expansion at \(t_*\) gives the
same error by the discrete Gaussian formula; the odd Taylor terms
have exponentially small lattice sums and the first even corrections
have relative size \(N^{-1}\).

In particular the normalized squared coefficients have a genuine
Gaussian concentration: for every fixed bounded interval \(I\),
\[
 \frac{1}{\mu_{2,N}}
 \sum_{(n-Nt_*)/\sqrt N\in I}|(\beta_N)_n|^2
 \longrightarrow
 \sqrt{\frac{-\mathcal S''(t_*)}{\pi}}
       \int_I e^{\mathcal S''(t_*)s^2}\,ds.
 \tag{44}
\]
This concerns the actual initialized vector, with its full original
closing functional. Finally
\(Z_{2,2,N}=\kappa^3\mu_{2,N}\) retains exactly the original
phase in (43). For higher fixed \(m\), (43), the first-moment
asymptotic from the seed theorem, and positive moment ratios also give
\[
 \mu_{m,N}\ge C_m N^{3/2}
       e^{N[2(m-1)\mathfrak s-(m-2)c]},\qquad C_m>0,
 \tag{45}
\]
for sufficiently large levels. No equality of those higher rates or
geometric volume identification is used or asserted.

There is also an exact regulator expression for the rate, with its
constant fixed by the original primitive. Define the Bloch--Wigner
function by
\[
 \mathcal D(z)=\Im\operatorname{Li}_2(z)
                   +\log|z|\operatorname{Arg}(1-z).
 \tag{46}
\]
On the original strip and the branch in (9),
\[
 J(z)=\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iz})
             +\frac{i\pi}{2}(z-z^2)-\frac{i\pi}{12}.
 \tag{47}
\]
This follows by differentiating and taking the limit at zero;
the logarithms are the continuations used in (2). At the selected
critical point \(x=\xi+ih_c\), the exact zero lift of \(F_x\)
gives
\[
 \operatorname{Arg}(1-pu)-3\operatorname{Arg}(1-u)
                          =\pi(1-2\xi).
 \tag{48}
\]
Substitution in (47) yields
\[
 \begin{split}
 2\pi\mathcal S(t)
 &=3\Im\operatorname{Li}_2(u)
       +2\Im\operatorname{Li}_2(p)-\Im\operatorname{Li}_2(pu)
       +2\pi^2h_c(1-2\xi)\\
 &=3\mathcal D(u)+2\mathcal D(p)-\mathcal D(pu).
 \end{split}
 \tag{49}
\]
Here \(|p|=1\) and \(\log|u|=\log|pu|=-2\pi h_c\),
so (48) supplies precisely the displayed correction. No additive
real constant is omitted. At the unique maximum, \(u,p,pu\)
are all in the upper half-plane. Formula (49) identifies the value
of the original action; by itself it does not identify a marked
ideal triangulation, its complete gluing equations, or its volume.
