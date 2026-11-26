# Complete endpoint continuation to private real part 9/40

Research deduction, 8 November 2026. The complete endpoint theorem
extends to the below-curve strip with private real part at least
\(9/40\) and depth at most \(3/50\). The new ingredient is a
directional cotangent inequality along the actual segment from
the auxiliary critical point to its right real cut. It retains
the correlation between the reciprocal argument and that segment.

The theorem concerns the whole original endpoint coefficient.
It does not compare an outer-cap path with its own action.
No numerical evaluation or frozen-source change is used.

## 1. Original source and added domain

Keep exactly the source, original primitive, critical root and
ordinary-color continuation of
[the western endpoint theorem](research_mixed_endpoint_west_below_curve.md):
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi el}e_l(w)}{S_lG_N(Ne-l)},\qquad
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\qquad
 S(e)=F(e,u_c(e)).
 \tag{1}
\]
Let \(\eta_0(E)\) be the depth of the original auxiliary-real
curve \(p=1-2t^2+2it\), with
\(E-i\eta_0(E)=\Log p/(2\pi i)\). Define the added closed set
\[
 \mathcal W_{9/40}=
 \{E-i\eta:9/40\le E\le23/100,\quad
                         \eta_0(E)\le\eta\le3/50\}.
 \tag{2}
\]

**Theorem.** On a fixed complex neighborhood of
\(\mathcal W_{9/40}\times\{-2\}\), the complete original function
has
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                 (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.
 \tag{3}
\]
All phases, coefficients, branches and ordinary normalizations
are unchanged. Both level parities, all revived rows and every
fixed normalized mixed ordinary-color/index derivative are included.
Together with the western and earlier rectangle theorems, and
the above-curve source, this supplies the complete endpoint
asymptotic on a fixed neighborhood of
\([9/40,49/100]+i[-3/50,0]\), near complete ordinary color.
It makes no outer-action claim.

## 2. Exact root bounds on the new strip

Put
\[
 p=Re^{2\pi iE},\quad c=\Re p,\quad
 \sqrt{1-2p}=A-iB,\quad
 \tan\pi u_c=A/2-i(B-1)/2 .
 \tag{4}
\]
The original branches continue from the auxiliary-real curve.
The square-root monotonicity in the western theorem gives
\(B\ge1\) below it. On (2),
\[
 R<35/24,\qquad R\ge R_0(E)>5/4,\qquad
                         31/200<c<11/48 .
 \tag{5}
\]
The upper radius is exactly the logarithmic witness already
proved in the western theorem, since the height bound is unchanged.
For the upper real part,
\(\cos2\pi E\le\sin(\pi/20)<11/70\).
For the curve radius use
\[
 (1-c_0^2)R_0^2+2c_0R_0-2=0,\qquad c_0=\cos2\pi E<11/70.
\]
At \(R=5/4\), the left side is at most
\(-261/3136<0\), using its increase in \(c_0\) there.
This proves \(R_0>5/4\).
For the lower real part, \(E\le23/100\) and
\[
 \sin(\pi/25)>\sin(1/8)\ge383/3072>31/250
\]
give \(c>31/200\). In particular
\[
                       \pi\eta>1/9.
 \tag{6}
\]

The exact radical formulas
\[
 A^2=\frac{\sqrt{1-4c+4R^2}+1-2c}{2},\qquad
 B^2=\frac{\sqrt{1-4c+4R^2}-1+2c}{2}
 \tag{7}
\]
imply
\[
 A<34/25,\qquad 1\le B<219/200.
 \tag{8}
\]
For \(A\), its square decreases in \(c\) and increases in \(R\)
at the fixed lower \(c\). The radical at those bounds is
\(\sqrt{31993/3600}<3\), so
\(A^2<369/200<(34/25)^2\).
For \(B\), its square increases in both variables. At the
upper bounds the radical is \(\sqrt{1237}/12<47/16\), so
\[
 B^2<115/96<(219/200)^2.
\]
Here \(\sqrt{1237}<141/4\) is a direct squared rational inequality.

Write \(u_c=\xi+ih_c\) and \(\tan\pi u_c=x-iy\).
Then \(0\le y<19/400\), and
\[
                  x^2>37/96+y+y^2.
 \tag{9}
\]
The same original arctangent formula as in the western proof gives
\[
 \tan(2\pi\xi)
   <\frac{43520}{17131}<\frac{51}{20}
                              <\cot(29\pi/250).
 \tag{10}
\]
For the last comparison use
\(\cot q>1/q-q/2\) at \(q<319/875\).
Thus \(\xi<24/125\); also (9) gives \(\xi>1/6\).
On the vertical arctangent segment from \(x\) to \(x-iy\),
\(\Re(1/(1+z^2))<1/(133/96+y)\). Integration proves
\[
 \boxed{\quad
  \frac16<\xi<\frac{24}{125},\qquad
  0\le-h_c<\frac{114}{3439\pi}<\frac4{375}.
 \quad}
 \tag{11}
\]
The last comparison uses \(\pi>25/8\).
Consequently \(0<\xi<E\) and
\[
 \pi(\eta+h_c)>
       \frac19-\frac{114}{3439}>\frac1{13}.
 \tag{12}
\]
All original primitive arguments remain in their regular chambers,
with \(\Im(e-u_c)<0\), and the critical point is simple.
There is no logarithmic lift change from the real-auxiliary curve.

The common estimates used below are
\[
 \sinh(2\pi|h_c|)<1/15,\qquad
 \Re A_0>4,\qquad
 A_0=2\tan\pi u+3\cot\pi u .
 \tag{13}
\]
Indeed \(2\pi|h_c|<228/3439<199/3000\), and
\(\sinh t\le t/(1-t^2/6)\), together with
\(15t+t^2/6<199/200+1/1350<1\), proves the first.
The real tangent/cotangent product bounds are the same elementary
identities as in the earlier corridor. On the right cut segment
they give the sharper estimates
\[
                  \Re A_0>5,\qquad
           |\Im A_0|<(2/25)\Re A_0.
 \tag{14}
\]
Its real parts lie between \(1/6\) and \(23/100\), a subset of
the interval used for these bounds in the western theorem.

## 3. A correlated cotangent inequality

**Lemma.** Suppose
\[
 0\le\delta\le d\le1/8,\qquad 0\le m\le1/3,\qquad
 y=\eta-m(d-\delta)>0,\qquad \eta>0.
\]
Then
\[
 (1-m^2)\Re\cot\pi(d-iy)
       -2m\Im\cot\pi(d-iy)\ge-2m\coth(\pi\eta).
 \tag{15}
\]

*Proof.* Put \(C_0=\coth(\pi\eta)\). Multiplying the desired
inequality by its positive denominator
\(\cosh(2\pi y)-\cos(2\pi d)\) reduces it to \(Q(d)\ge0\), where
\[
 Q(d)=(1-m^2)\sin2\pi d
       +2mC_0(\cosh2\pi y-\cos2\pi d)-2m\sinh2\pi y .
\]
At the left endpoint,
\[
 Q(\delta)=(1-m^2)\sin2\pi\delta
                       +2mC_0(1-\cos2\pi\delta)\ge0.
\]
Differentiating with \(\eta,\delta,m\) fixed gives
\[
 \frac{Q'(d)}{2\pi}
 =(1-m^2)\cos2\pi d+2mC_0\sin2\pi d
          +2m^2(\cosh2\pi y-C_0\sinh2\pi y).
\]
Since \(0<y\le\eta\),
\[
 \cosh2\pi y-C_0\sinh2\pi y
       =\frac{\sinh(\pi\eta-2\pi y)}{\sinh\pi\eta}\ge-1.
\]
Therefore
\[
 \frac{Q'(d)}{2\pi}
 \ge\frac{1-m^2}{\sqrt2}-2m^2
 \ge\frac{4\sqrt2-2}{9}>0.
\]
This proves (15), including \(m=0\). \(\square\)

This lemma bounds the directional quadratic form, rather than
discarding the favorable real part of the reciprocal cotangent.

## 4. Both actual real cut gaps

Keep the cuts
\[
                      a_L=1/20,\qquad b(E)=E-1/1000 .
 \tag{16}
\]
On the left segment from \(u_c\) to \(a_L\),
(12) gives
\[
 0<\Im\cot\pi(e-u)<\coth(\pi(\eta+h_c))
                              <13+1/5<14.
\]
Also \(\Re A_0>4\) and
\(|\Im A_0|<(\Re A_0)/4\), since the real part is at least
\(1/20\) and (13) holds. Writing \(F_{uu}=-A_*+iB_*\),
\[
 |B_*|<(15/4)A_*,\qquad
 \frac{|\Delta\Im u|}{|\Delta\Re u|}
     <\frac{4/375}{1/6-1/20}<1/10.
\]
The left quadratic cone bracket is greater than
\(1-1/100-3/4=6/25>0\).
Taylor's exact second-order integral from the critical point
therefore pays the left real cut.

On the right segment put \(\delta=1/1000\) and
\[
        m=\frac{-h_c}{b(E)-\xi}<\frac13 .
\]
Here \(b(E)-\xi>4/125\) by (11).
For a point of that segment write \(d=E-\Re u\); then
\[
 \delta\le d\le E-\xi<1/8,\qquad
 \eta+\Im u=\eta-m(d-\delta)>0.
\]
Thus (15) applies to the actual reciprocal argument on the
entire segment. The directional Hessian is exactly
\[
 -\Re\{F_{uu}(1+im)^2\}
       =\pi\Re\{(A_0+\cot\pi(e-u))(1+im)^2\}.
 \tag{17}
\]
We bound this form in two fixed depth ranges.

If \(\eta\ge13/250\), then
\[
 \pi\eta>13/80,\qquad
 \coth(\pi\eta)<80/13+1/15=1213/195.
\]
The latter follows from
\(\coth q<1/q+q/3\) and \(q<1/5\).
Equations (14)--(15) give
\[
 \Re\{(A_0+\cot\pi(e-u))(1+im)^2\}
 >5\left(1-\frac19-\frac4{75}\right)
       -\frac23\frac{1213}{195}
 =\frac2{65}>0 .
 \tag{18}
\]

If \(\eta\le13/250\), then \(R<7/5\), since
\(\log(7/5)>1/3>26\pi/250\).
Thus \(c<11/50\), and (7) yields
\[
 B^2<453/400<(16/15)^2.
\]
Indeed the radical is at most
\(\sqrt{199/25}<113/40\).
Consequently \(y<1/30\); using (9) in the arctangent integral
now gives
\[
 -h_c<\frac{16}{681\pi},\qquad
 m<\frac{160}{681}<\frac6{25}.
\]
Moreover the exact radius identity, not the weaker (6), gives
\[
                 \coth(\pi\eta)=\frac{R+1}{R-1}<9
\]
by \(R>5/4\). Therefore (14)--(15) give
\[
 \Re\{(A_0+\cot\pi(e-u))(1+im)^2\}
 >5\left(1-\frac{36}{625}-\frac{24}{625}\right)
       -2\frac6{25}\,9
 =\frac15>0.
 \tag{19}
\]
Equations (17)--(19) pay the right real cut by the same exact
Taylor integral. Hence
\[
       \Re F(e,a_L)<\Re S(e),\qquad
       \Re F(e,b(E))<\Re S(e)
 \tag{20}
\]
with uniform strictly positive gaps on the compact set (2).

## 5. Every omitted physical and revived row

The real-tail and action-floor estimates must be extended to
the new real interval; no older domain statement is used beyond
its range. For the lower rows \(x\le1/20\),
\(E-x\ge7/40>1/6\), so the original lower force remains greater
than \(27\).

For \(x\ge b(E)\ge28/125\), \(\pi x>7/10\).
The elementary positive tangent polynomial gives
\[
 \tan(\pi x)>
 \frac7{10}+\frac{(7/10)^3}{3}+\frac{2(7/10)^5}{15}
       =\frac{627557}{750000}>\frac56 .
\]
The polynomial is a lower bound for tangent: its derivative
is at most one plus its square, and both start at zero.
Also the sine and cosine polynomials at \(7/10\) give
\[
 \sin\pi E>16/25,\qquad \cos\pi E<4/5.
\]
The remaining height bounds are unchanged:
\(\sinh(\pi\eta)<1/5\) and \(e^{\pi\eta}<5/4\).

In the exact force formula (9) of
[the bridge real-tail theorem](research_mixed_endpoint_bridge_real_tails.md),
the postwall real-angle maximum is consequently at most
\[
 \frac{4\cos^3\pi E}{27\sin^2\pi E}
       <\frac{4(4/5)^3}{27(16/25)^2}=\frac5{27}<\frac15 .
\]
Before the wall, \(0\le E-x\le1/1000\) and
\(\sin\pi x>3/5\), so the same real-angle term is less than
\(1/5\). The height term remains less than \(288/625\).
Thus every row from the actual upper cut to one half has
\[
                  e^{R_x}<\frac54
                    \left(\frac15+\frac{288}{625}\right)
                          =\frac{413}{500}<1.
 \tag{21}
\]
This includes all revived rows past \(x=E\).
Both lower-half tails reduce to the real cuts in (20).

The complete reflected upper-half estimate uses only \(E>1/6\)
and still has ceiling \(67/105\).
For its own-action comparison, on the real interval
\([9/40,7/20]\) the original curvature formula gives
\[
 0<-\lambda''(E)
 <\pi\left\{\frac65+
        \frac{2}{(16/25)(7/5)}\right\}
 =\frac{961\pi}{280}<11 .
 \tag{22}
\]
Here the square-root bound \( |\sqrt{2-e^{-2\pi iE}}|>7/5\)
follows from \(\cos2\pi E<1/4\).
The exact printed source consequences
\(\lambda(7/20)>108/125\) and
\(|\lambda'(7/20)|<1/200\), with their saved source identified
in [the bridge phase floor](research_mixed_endpoint_bridge_phase_floor.md),
therefore give the same
\[
                         \lambda(E)>1511/2000 .
 \tag{23}
\]
This uses the old displacement bound \(7/50\), which is still
larger than all displacements here. No saved value is recomputed.

The above-curve theorem supplies the original chamber from
the real edge to the curve; (11)--(12) retain it below the
curve. In particular
\[
 \partial_\eta\Re S
       =-\Arg\sin\pi(e-u_c)+\pi\Re u_c>0.
\]
Hence \(\Re S(e)>1511/2000\) on (2), paying the entire
upper half with a gap greater than \(1/10\).
These are the literal all-row Newton/reciprocal-factorial
bounds, including zeros and both parities.

## 6. Complete finite contour and continuation

Choose the half-grid cuts
\[
 a_N=(\lceil Na_L\rceil-1/2)/N,\qquad
 b_N=(\lceil Nb(E)\rceil-1/2)/N .
\]
The retained regular strip satisfies \(0<\Re u<E\) and
\(E-\Re u\ge1/1000+O(N^{-1})\).
Its exact row has the original nonzero \(N^{-2}\) symbol.
Every omitted row is paid by (20)--(23), with its full original
carrier; physical termination is never imposed off grid.

The critical auxiliary height is nonpositive. At height
\(h_c=-H<0\), the symmetric signed-height reflection retains
the opposite upper-alias loss \(\pi(1+2E)H\), while the
main-side alias loses \(2\pi H\).
The original horizontal concavity, vertical convexity, and
the two paid real cuts control both horizontal aliases,
all four weighted vertical half-sides, and both unweighted
joins. At \(H=0\), use a fixed sufficiently small finite
symmetric rectangle: the original imaginary derivative
satisfies \(|\Im F_u|<\pi\), so both aliases remain strictly
paid. As in the western proof, enlarge the rectangle slightly
where needed to keep the saddle interior, and use a finite
compact cover.

This is the full original cotangent inventory with density
\(+N\), not a local critical contribution alone.
The nonzero interior Gaussian yields
\(N^{-2}N N^{-1/2}=N^{-3/2}\), with precisely the original
coefficient in (3). The uniform zero-safe row bounds preserve
the discarded-source gaps on a fixed small ordinary-color disk.
Fix the integer cuts and paths at each base point before
continuing parameters; all strict gaps persist.
A finite cover and Cauchy's formula prove the holomorphic
relative error and every stated fixed normalized mixed derivative.

Finally combine (2) with the western below-curve strip, the
above-curve region, and the earlier lower rectangle. Their
same-source actions and coefficients agree on overlaps.
This proves the rectangle consequence stated after (3).
No comparison of an outer phase along that rectangle is inferred.

