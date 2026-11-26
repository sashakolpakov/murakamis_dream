# A complete cap packet before the exact later incoming point

Research deduction, 8 November 2026. The fixed departure of the
complete real-arc cap contour lies strictly below the original
critical action for every incoming parameter from the half face
through the exact later point. Consequently that same complete
finite contour gives a nonzero cap asymptotic on this entire
interval, including \([1/2,33/50]\).

The proof uses an intermediate fixed private point and a correlated
Hessian cone. It does not assert that the derivative of the
departure-minus-critical action has a sign. No numerical evaluation,
new root enclosure by computation, or change to a frozen source is
used. Complex continuation is on the fixed neighborhood proved below;
no prescribed macroscopic negative incoming depth is inferred.

## 1. Original source, critical branch, and statement

Keep the literal cap, absolute phase, endpoint source, and all
normalizations of [the complete departure envelope](research_mixed_cap_uniform_departure_envelope.md):
\[
\begin{split}
 U_{0,N}(w,e^{-2\pi ia})
   &=\sum_{j=0}^{N-1}H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j,\\
 \Psi(e,a,w)&=S(e,w)+J(a+e)-J(a)-i\pi ae,\\
 \mathcal T(a,w)&=\Psi(e_*(a,w),a,w),\qquad
 M(a)=\Re\mathcal T(a,-2).
\end{split}
\tag{1}
\]
The critical branch is the original one from
[general incoming transport](research_mixed_half_face_general_incoming_transport.md).
Define
\[
\begin{gathered}
 X_0=-\frac13+\frac{2\sqrt2}{3}i,\qquad
 a_0=1-\frac{\Arg X_0}{2\pi},\\
 p_0=i\sqrt2,\qquad
 e_0=\frac14-\frac{i\log2}{4\pi}.
\end{gathered}
\tag{2}
\]
The exact later-point theorem proves \(e_*(a_0,-2)=e_0\),
with the original zero lift. Also \(2/3<a_0<7/10\):
the upper-unit-circle argument of \(X_0\) is less than \(2\pi/3\)
and greater than \(3\pi/5\).

Keep precisely the earlier fixed departure
\[
 p_d=C+iD=\frac{23}{144}+\frac{11\sqrt2}{12}i,\qquad
 K=|p_d|^2=\frac{35377}{20736},\qquad
 e_d=\frac{\Log p_d}{2\pi i}.
\tag{3}
\]
Put \(R_d(a)=\Re\Psi(e_d,a,-2)\).

**Theorem.** On the entire closed interval
\[
                         1/2\le a\le a_0
\tag{4}
\]
one has \(R_d(a)<M(a)\), with a uniform strict gap.
There is a fixed complex neighborhood \(\mathcal U\) of
\([1/2,a_0]\times\{-2\}\) such that, along both integer parities,
\[
 U_{0,N}(w,e^{-2\pi ia})
 =N^{-1}\mathcal B(a,w)e^{N\mathcal T(a,w)}
                       \bigl(1+O_{\rm hol}(N^{-1})\bigr),
 \qquad \mathcal B(a,w)\ne0.
\tag{5}
\]
The original coefficient is
\[
 \mathcal B(a,w)=
 \frac{\sqrt{2\pi}\,A(e_*(a,w),w)}
      {\sqrt{-\Psi_{ee}(e_*(a,w),a,w)}}
 \sqrt{\frac{\sin\pi(a+e_*(a,w))}{\sin\pi a}},
\tag{6}
\]
where \(A\) and all square roots are the original endpoint,
Gaussian, and factorial symbols. Every fixed mixed ordinary-color
and incoming derivative of the normalized relative error is
\(O(N^{-1})\) on smaller fixed neighborhoods.

This is an ordinary-color packet near complete color. It does not
give a nonzero packet at arbitrary real colors, at a prescribed
negative incoming depth, or for a whole following contraction.

## 2. A cone containing the entire earlier critical path

Use the exact original variables
\[
 k=r-i\tau,\quad \tau>0,\quad U=|k|^2,\quad
 D_k=1-2r+U,\quad p=1-2k+2k^2,\quad P=|p|^2.
\tag{7}
\]
Here \(r\) is a real parameter of the critical branch, not the
level root of unity in (1). The source
[actual cap-path bridge, Sections 1--2](research_mixed_endpoint_actual_cap_path_bridge.md)
gives
\[
\begin{gathered}
 -1/100<r<1/5,\quad U>2/5,\quad 1<P<21/10,\\
 4U^3-(8r+2)U^2+12r^2U-8r^3+4r^2-r=0,\\
 X=4k^2+3-\frac2{1-k},\qquad
 \Re p=1-2r+4r^2-2U,\quad
 \Im p=2\tau(1-2r).
\end{gathered}
\tag{8}
\]
For \(r>0\) it also proves \(P>2U\). Its calculation (24),
whose hypotheses are just \(0<r<1/5\) and \(P<21/10\), gives
\[
                     \Re p<-6r(1-2r).
\tag{9}
\]
This calculation is not restricted to the later subpath
\(\Re e\le27/100\): it follows from
\(w_0^2=(P-(1-2r)^2)/4<87/200\) in that calculation.

At the half face \(r>0\). If \(r=0\), (8) and \(U>2/5\)
force \(U=1/2\), \(k=-i/\sqrt2\), and \(X=X_0\).
Thus \(r>0\) for \(1/2\le a<a_0\), and \(r=0\) at \(a_0\).
No other branch is substituted in this argument.

Write \(U=1/2+v\) when \(r>0\). Its equation becomes
\[
 f_r(v)=4v^3+(4-8r)v^2+(1-8r+12r^2)v
                      -3r+10r^2-8r^3=0.
\tag{10}
\]
The uniqueness of the root \(U>2/5\), proved in the same source,
permits comparisons with test values. Direct substitution gives
\[
                     r<v<3r,\qquad
                     v<\frac{3r}{1+4r}.
\tag{11}
\]
For the first bounds, the values are
\(-2r+6r^2<0\) and \(22r^2+64r^3>0\).
For the last bound, multiplication by \((1+4r)^3/r\)
gives
\[
 10r+40r^2-192r^3+832r^4-512r^5>0
 \quad(0<r<1/5).
\]
For example \(10+40r-192r^2>0\), and the last two terms
have positive sum.

We next record two sharper modulus inequalities:
\[
             2(1-2r+2r^2)<P<2+4r,\qquad
                         |\log(P/2)|<2r.
\tag{12}
\]
Indeed
\[
 P=2-8r+8r^2+4(1-2r)v+4v^2,
\]
so \(v>r\) proves the lower bound. For the upper bound put
\(g(v)=v^2+(1-2r)v-3r+2r^2\). At its positive root \(v_g\),
\[
 v_g=\frac{-1+2r+\sqrt{1+8r-4r^2}}2\ge3r-5r^2,
\]
since \((1+4r-10r^2)^2\le1+8r-4r^2\).
Moreover
\[
 f_r(v)=4vg(v)+(1+2r)^2v-r(1-2r)(3-4r).
\]
Hence
\[
 f_r(v_g)\ge17r^2-16r^3-20r^4>0.
\]
The selected root lies below \(v_g\), proving \(P<2+4r\).
The logarithmic upper inequality follows from
\(\log(1+2r)<2r\); the lower follows because
\[
 \frac{d}{dr}\{-\log(1-2r+2r^2)\}
        =\frac{2-4r}{1-2r+2r^2}\le2.
\]

Equations (9), \(U<P/2<21/20\), and \(\tau<41/40\) give
\[
 \Arg p-\frac{\pi}{2}
  >\arctan\frac{120r}{41}>\frac{5r}{2}.
\tag{13}
\]
The last inequality follows from
\(\arctan z\ge z-z^3/3\), \(r<1/5\), and
\[
 \frac{120}{41}-\frac{120^3}{75\cdot41^3}>\frac52;
\]
the difference after subtracting \(5/2\) is exactly
\(12755/137842>0\).

We also have \(\Arg p<3\pi/4\). In fact, by (11),
\[
 \frac{-\Re p}{\Im p}
 =\frac{r-2r^2+v}{\tau(1-2r)}
 <\frac{34/75}{12/25}=\frac{17}{18}<1.
\tag{14}
\]
Here \(v<1/3\), \(r-2r^2<3/25\), and
\[
 \tau^2(1-2r)^2>
 (1/2+r-r^2)(1-2r)^2\ge\frac{297}{1250}>
                                      \left(\frac{12}{25}\right)^2.
\]
The middle function decreases on \(0\le r\le1/5\), as direct
differentiation shows.

Let \(e_*(a,-2)=E_*-i\eta_*\), and
\(\eta_0=\log2/(4\pi)\). From (12)--(14),
\[
 \frac14<E_*<\frac38,\qquad
 0<\eta_*<\frac3{50},\qquad
 \left|\frac{\eta_*-\eta_0}{E_*-1/4}\right|<\frac25
                     \quad(a<a_0).
\tag{15}
\]
The height bound is the original cap-path enclosure. The slope
is \(|\log(P/2)|/[2(\Arg p-\pi/2)]\). At \(a=a_0\) the two
points coincide.

One further correlated angular guard will be useful. The critical
relations give
\[
 \Re(X/p)=\frac{P+1-4U^3/D_k}{2P}\le\frac23.
\tag{16}
\]
For this, (12) and \(U>1/2+r\) imply
\[
 P D_k+12U^3-3D_k>4r+28r^2+8r^3\ge0.
\]
The polynomial with \(P\) replaced by its lower bound is increasing
in \(U\ge1/2+r\). Formula (16) is equality only at \(r=0\).
Since \(|X/p|^2=1/P\), \(P<21/10\), and
\(0<\Arg X-\Arg p\le\pi/2\), it follows that
\[
 \sin(\Arg X-\Arg p)>\frac1{\sqrt{15}}>\frac14,\qquad
 \cos(\Arg X-\Arg p)<\frac{29}{30}.
\tag{17}
\]
Thus these latter two bounds hold for every \(e\) on the segment
from \(e_0\) to \(e_*(a,-2)\), with angle \(2\pi(1-a-\Re e)\).

## 3. A strict Hessian cone along these actual segments

The original endpoint derivative, with its original square-root
branch, gives exactly
\[
 \frac{-\Psi_{ee}(e,a,-2)}{\pi}
 =\cot\pi e-\cot\pi(a+e)
       +\frac{2}{\sin\pi e\sqrt{2-e^{-2\pi ie}}}.
\tag{18}
\]
This is the same identity used in the half-face cap and original
cap-path sources; all arguments on the segment are regular.
We prove there that
\[
 H:=-\Psi_{ee},\qquad \Re H>0,\qquad |\Im H|<\Re H.
\tag{19}
\]

Write \(e=E-i\eta\), \(s=\sinh(2\pi\eta)\), and denote the
three terms on the right of (18) by \(C_e,C_b,B\).
We have \(1/4\le E<3/8\), \(0\le\eta<3/50\), and (17).
The elementary hyperbolic bounds give
\[
 s<2/5,\quad \cosh(2\pi\eta)<11/10,\quad
 \Re C_e>\frac{49}{127},\quad
 0\le\Im C_e<\frac47\Re C_e.
\tag{20}
\]
For instance \(2\pi\eta<19/50\) and
\(\sinh x\le x/(1-x^2/6)\),
\(\cosh x\le(1-x^2/2)^{-1}\).
Also \(\sin2\pi E\ge\sqrt2/2>7/10\), and its denominator is
less than \(11/10+5/7=127/70\).

For \(B\), the argument of \(\sin\pi e\) is in
\((-19/100,0]\); that of the square root is in \([0,1/4)\).
Furthermore
\[
 |\sin\pi e|^2<
 \frac67+\frac1{25}<1,\qquad
 |\sqrt{2-e^{-2\pi ie}}|<\frac74.
\]
Thus
\[
                   \Re B>\frac{31}{28},\qquad
                   |\Im B|<\frac13\Re B.
\tag{21}
\]
Use \(\cos(1/4)>31/32\). The square-root argument bound follows
from \(\Re(2-e^{-2\pi ie})\ge2\) and its imaginary part at most
one; every root remains on the original branch.

The only possibly large negative imaginary contribution is \(C_b\).
If \(\theta=2\pi(1-a-E)\), (17) gives
\[
 \Re C_b+\Im C_b
 =\frac{\sin\theta-s}{\sqrt{1+s^2}-\cos\theta}.
\tag{22}
\]
For \(0\le\eta\le1/25\), \(s<4/15\), so (22) is greater than
\(-1/2\): when its numerator is negative, its magnitude is
less than \((1/60)/(1/30)\).
Then (20)--(21) show
\[
 \Re(C_e+C_b+B)+\Im(C_e+C_b+B)
 >\frac{49}{127}-\frac12+\frac{31}{42}>0.
\tag{23}
\]

For \(1/25\le\eta<3/50\), the sharper bounds are
\[
 \Re C_e+\Im C_e>\frac{133}{254},\qquad
                        |\Im B|<\frac29\Re B.
\tag{24}
\]
Indeed \(s>1/4\), proving the first inequality by the same
denominator in (20). Also
\[
 |\Arg\sin\pi e|>
 \arctan\{(2/5)\tanh(\pi/25)\}>
 \arctan(6/125)>1/25.
\]
Consequently the argument of \(B\) is between \(-21/100\) and
\(19/100\), while
\(\arctan(2/9)>478/2187>21/100\).
Here \(\tanh(\pi/25)>\tanh(1/8)>3/25\).
These prove the second inequality of (24).

The negative part of (22) is at most \(225/164\).
In fact, for \(1/4\le s\le2/5\),
\[
 \frac{s-1/4}{\sqrt{1+s^2}-29/30}
 \le\frac{3/20}{\sqrt{29}/5-29/30}<\frac{225}{164}.
\tag{25}
\]
The function increases: its derivative has numerator
\((1+s/4)/\sqrt{1+s^2}-29/30>0\).
For the last bound use \(\sqrt{29}>269/50\).
Equations (21), (24), and (25) now give
\[
 \Re(C_e+C_b+B)+\Im(C_e+C_b+B)
 >\frac{133}{254}+\frac{217}{252}-\frac{225}{164}>0.
\tag{26}
\]
The last positive cross-product difference is \(67088\).

Finally \(\Im C_b\le0\); (20)--(21) directly imply
\(\Im(C_e+C_b+B)<\Re(C_e+C_b+B)\).
Together with (23) or (26), this proves (19).

Let \(m=(\Im e_*-\Im e_0)/(E_*-1/4)\), so \(|m|<2/5\).
By (19),
\[
 \Re\{H(1+im)^2\}>
             \{1-4/25-4/5\}\Re H=\frac1{25}\Re H>0.
\tag{27}
\]
Taylor's formula from the original critical point, whose derivative
is zero on the original lift, therefore proves
\[
               \Re\Psi(e_0,a,-2)<M(a)
                     \qquad(1/2\le a<a_0).
\tag{28}
\]
At \(a=a_0\) equality holds. No comparison between unrelated
critical sheets enters this proof.

## 4. The fixed departure is lower still

Define \(R_0(a)=\Re\Psi(e_0,a,-2)\).
The original incoming derivatives retain their exact chirps:
\[
 e^{\Psi_a(e,a,-2)}=\frac{1-X/p}{1-X}.
\tag{29}
\]
Writing \(c=\Re X\), \(s_X=\Im X\), for \(a\le a_0\) we have
\(c\le-1/3\), \(0\le s_X\le1\). Thus
\[
\begin{split}
 K\{|1-X/p_d|^2-|1-X/p_0|^2\}
 &=1-\frac K2-2Cc+(\sqrt2K-2D)s_X\\
 &>\frac5{84}>0.
\end{split}
\tag{30}
\]
For the bound use \(K<11/6\), \(K>17/10\), \(C>3/20\),
\(\sqrt2<10/7\), and \(2D=11\sqrt2/6\).
The lower bound is
\[
 \frac{11}{10}-\frac{55}{21}+\frac{13}{14}\frac{17}{10}
                       =\frac5{84}.
\]
It follows that \((R_d-R_0)'(a)>0\) on the entire interval.

The exact later-point main theorem already proves
\(R_d(a_0)<M(a_0)=R_0(a_0)\); see
[its Section 2](research_mixed_cap_later_point_main_contour.md).
Therefore
\[
 R_d(a)-R_0(a)\le R_d(a_0)-R_0(a_0)<0.
\tag{31}
\]
Combining (28)--(31) proves the first assertion of the theorem,
with a uniform gap on the compact interval. This argument proves
the needed action ordering without claiming a sign for
\((R_d-M)'(a)\).

## 5. The complete finite contour and its nonzero coefficient

The departure-envelope theorem already supplies an exact complete
contour for every real \(a\in[1/2,7/10]\). Its source is the literal
interpolant
\[
 \mathscr A_N(e,a,w)
       =D_N(e)^{-1}C_N(e,w)\Pi_N(a+e)/\Pi_N(a),
\tag{32}
\]
with all original reciprocal zeros and carriers. At each fixed base
it retains the same half-grid cuts, the lower and upper physical
sectors, and all six weighted cotangent currents. The uniform left
component, both tall horizontal aliases, the short upper-end
currents, and both long-right estimates pay all those remainders
strictly relative to \(M(a)\). Their exact density is \(+N\).

Its unweighted main contour consists of the paid left join, the
auxiliary-real curve to \(e_d\), the vertical segment to the actual
critical height, the horizontal segment through \(e_*(a)\), and
the paid right join. The endpoint packet is already proved on a
fixed neighborhood of the complete rectangle
\([23/100,49/100]+i[-3/50,0]\), and separately along the early curve
and left join. No extra western source or an unproved tube is
introduced here.

The new strict inequality \(R_d<M\) pays the whole early curve
and both endpoints of its following vertical segment.
Original vertical convexity pays that entire segment. On the
horizontal segment, strict horizontal concavity gives the unique
maximum \(M(a)\) at the original nondegenerate saddle.
Thus every fixed part of this exact contour away from the saddle
has a uniform exponential gap, after a finite compact cover.
All original physical, weighted, and unweighted pieces are included.

The original row symbol there is
\[
 N^{-3/2}A(e,w)
       \sqrt{\frac{\sin\pi(a+e)}{\sin\pi a}}\,
                 e^{N\Psi(e,a,w)}(1+O_{\rm hol}(N^{-1})).
\tag{33}
\]
The \(+N\) cycle density and the horizontal Gaussian factor
\(N^{-1/2}\) give exactly \(N^{-1}\), with coefficient (6).
Every factor in (6) is nonzero on the retained critical chart.

Hold each base contour and each integer cut fixed before complex
continuation. The complete endpoint source cover, all zero-safe
physical remainder estimates, and all strict contour gaps persist
on a fixed complex neighborhood after shrinking. A finite cover
of the real interval gives the neighborhood in (5). On overlaps
the normalized expansions agree because they represent the same
exact finite polynomial with the same original analytic action
and Gaussian branch. This proves (5), including both parities.
Cauchy's formula on smaller fixed neighborhoods proves the stated
normalized mixed derivatives.

The theorem supplies a genuine nonzero cap coefficient along the
earlier real incoming interval and some fixed complex neighborhood.
It does not certify that this neighborhood reaches the given
negative-depth starting point, nor does it pay an incoming contour
joining that point to the already paid real interval. Those
source-domain and following-action comparisons remain separate.

