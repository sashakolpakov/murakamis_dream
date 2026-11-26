# A moving contour boundary for the ordinary three-four pair

Research deduction, 7 November 2026. The original fixed transform
cut at \(t=3/20\) need not remain fixed when the incoming coordinate
moves to the right. Moving it to \(t=3/5-x\) gives a strict decrease
of the coupled real action. This pays the boundary that was not
settled by the fixed saved-data comparison.

The argument below concerns the actual ordinary \((3,4)\) source.
It retains both ordinary boundary colors and the original critical
point. Together with the existing estimates, it controls the full
product of its two factors on \(9/20\le x\le1/2\), at the critical
height. The rest of the incoming circle, height transitions and
the estimates needed for attachment remain separate problems.
No new phase, root or source evaluation is used.

## 1. Source, reference and the choice of boundary

Use the exact source and primitive of
[the ordinary-pair deduction](research_mixed_three_four_ordinary_pair_target.md):
\[
 Z_{34,N}(w_L,w_R)=\kappa_N^3N^2
 \oint U_{0,N}(w_L,X)V_{1,N}(w_R,X)\frac{dX}{2\pi iX}.
 \tag{1}
\]
Both ordinary colors are near their complete value \(-2\).
Write the actual critical coordinates as
\[
 a_*=A+ic,\qquad t_*=T+ih,\qquad e_*=E+iv,
\]
with the rectangles in
[the endpoint theorem](research_mixed_open_word_endpoint_rectangles.md).
In particular
\[
 .278<A<.391,\quad -.072<c<.021,\quad
 -.108<h<-.020,\quad -.051<v<-.019.
 \tag{2}
\]
Let \(M=\Re\{T_0(a_*)+P_1(a_*)\}\), \(p=\Re P_1'(a_*)\),
and \(\kappa_*=1/2500000\).
The original stationary equation cancels the two incoming
marginals. The complete first factor has upper rate
\[
 B_U(x)=\Re T_0(a_*)-p(x-A)-\kappa_*(x-A)^2,
 \qquad p>-7/20.
 \tag{3}
\]
These are the already proved full-factor bounds, not a replacement
of that factor by its main summand.

The reduced terminal phase is
\[
 \Phi(a;t,e)=S(e)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
              -\frac{\pi i}{2}(e-e^2)+2\pi iat,
 \quad g'(z)=\log(1-e^{-2\pi iz}).
 \tag{4}
\]
Here \(S\) is the action of the complete ordinary endpoint
coefficient, with its original branch.
Keep the original private rectangle
\[
 E_c=[.27,.49]+i[-.055,.04]
\]
and the transform heights \([-.12,.12]\).
For \(b=9/20\le x\le1/2\), put
\[
 a=x+ic,\qquad s(x)=3/5-x.
 \tag{5}
\]
Thus \(1/10\le s(x)\le3/20\) and \(s(b)=3/20\).
The new central transform interval is \([s(x),1/2]\).

## 2. Increasing the real transform coordinate on the added rectangle

**Lemma 1.** Uniformly for
\[
 b\le x\le1/2,\quad .1\le u=\Re t\le.15,\quad
 |\Im t|\le.12,\quad e\in E_c,
\]
the original phase satisfies
\[
                      \partial_u\Re\Phi(a;t,e)>1/60.
 \tag{6}
\]

*Proof.* Set
\[
 R=e^{-2\pi c},\qquad r=e^{2\pi\Im t},\qquad
 k=e^{2\pi\Im e}.
\]
Keeping the chirp \(2\pi iat\), differentiation gives exactly
\[
 e^{2\partial_u\Re\Phi}
 =\frac{|R-r e^{-2\pi i(x+u)}|^2
             |1-kr e^{-2\pi i(\Re e+u)}|^2}
             {|1-r e^{-2\pi iu}|^6}.
 \tag{7}
\]
The ranges imply
\[
 R>4/5,\quad k>7/10,\quad 7/15<r<15/7,
\]
and
\[
 \cos2\pi(x+u)<-7/12,\quad
 \cos2\pi(\Re e+u)<-3/5,\quad
 \cos2\pi u>7/12.
 \tag{8}
\]
Consequently the right side of (7) is greater than \(AB/D^3\),
where
\[
 A=r^2+\frac{14}{15}r+\frac{16}{25},\quad
 B=\frac{49}{100}r^2+\frac{21}{25}r+1,\quad
 D=r^2-\frac76r+1>0.
 \tag{9}
\]

For \(7/15\le r\le7/6\), \(D\le1\),
\[
 A-D\ge31/50,\qquad
 B-D=r(301/150-51r/100)>0.
\]
It follows that \(AB/D^3>81/50\).
For \(7/6\le r\le15/7\), both \(A-2D\) and \(B-8D/5\)
are concave quadratics. Their respective endpoint values are
\[
 (109/100,\ 1284/1225),\qquad
 (3769/3600,\ 101/980).
\]
They are positive. Also \(D\le303/98\), so
\[
 \frac{AB}{D^3}>\frac{16}{5D}\ge\frac{1568}{1515}.
 \tag{10}
\]
Since \(\log(1+y)>y/(1+y)\) for \(y>0\), (7)--(10) give
\[
 \partial_u\Re\Phi>
 \tfrac12\log(1568/1515)>53/3136>1/60.
\]

For completeness all the scalar guards in (8) are elementary.
The lower incoming-radius bound follows from
\(e^{-.042\pi}>1-.042\pi>4/5\).
The positive-series bounds
\[
 e^z\le1+z+\frac{z^2}{2(1-z/3)},\qquad
 e^z\le1+z+\frac{z^2}{2}+\frac{z^3}{6(1-z/4)}
\]
give \(e^{.11\pi}<10/7\) and \(e^{.24\pi}<15/7\)
by using \(z=7/20\) and \(z=19/25\), respectively.
Reciprocation gives the lower bound for \(r\).
The exact value
\(\sin^2(\pi/5)=(5-\sqrt5)/8\) gives
\(\sin(\pi/5)>7/12\).
The angles \(x+u\) lie in \([.55,.65]\), so this proves the
first cosine bound. The angles \(\Re e+u\) lie in \([.37,.64]\);
their cosine is at most \(-\cos(.28\pi)=-\sin(.22\pi)<-3/5\).
The last inequality follows from
\(\sin(.22\pi)>\sin(.66)>.66-.66^3/6>3/5\).
No primitive or critical point has been evaluated. \(\square\)

## 3. Convexity along the vertical sides

**Lemma 2.** On the added rectangle of Lemma 1, the real part
of \(\Phi\) is strictly convex separately in each of
\(\Im t\) and \(\Im e\), with all other real coordinates fixed.

*Proof.* Put \(C(z)=\Re\cot(\pi z)\).
Since \(g''=\pi\cot(\pi z)-\pi i\), direct differentiation gives
\[
 -\pi^{-1}\Re\Phi_{tt}=3C(t)-C(a+t)-C(e+t).
 \tag{11}
\]
Here \(C(a+t)<0\) and \(C(e+t)\le\cot(.37\pi)<1/2\).
Also \(C(t)>1\). Indeed, for
\(\theta=2\pi\Re t\in[.2\pi,.3\pi]\),
\[
 \sin\theta+\cos\theta
 \ge\sin(.2\pi)+\cos(.2\pi)>7/12+4/5>4/3
 >\cosh(2\pi\Im t).
\]
The first inequality follows from concavity and equal endpoint
values of the sine-plus-cosine function.
Thus (11) exceeds \(5/2\).

For the other coordinate,
\[
 -\Re\Phi_{ee}=-\Re S''(e)+\pi C(e)-\pi C(e+t).
 \tag{12}
\]
The original endpoint Schur argument gives \(-\Re S''(e)>0\).
If \(\Re(e+t)\ge1/2\), the remaining signs suffice.
Otherwise let \(p_e=\cot(\pi\Re e)\), so \(0<p_e<1\).
Since \(\cos(2\pi\Re e)<0\) and \(\cosh(.11\pi)<16/15\),
\[
 C(e)>\frac{15}{16}p_e.
\]
Put \(d=\tan(\pi/10)>3/10\). Because \(\Re t\ge1/10\),
the cotangent addition formula gives
\[
 C(e+t)\le\cot\pi(\Re e+.1)
   =\frac{p_e-d}{1+p_ed}
   \le p_e-d<\frac7{10}p_e.
\]
This proves positivity in (12).
Holomorphicity changes the sign of the second derivative when
the imaginary coordinate varies, proving the two convexity
statements. The added rectangle meets no primitive singularity.
\(\square\)

These are separate convexity statements. No full joint concavity
on the enlarged rectangle is needed: Lemma 1 reduces its
horizontal pieces to the previously controlled boundary \(u=.15\).

## 4. The new real boundary has a decreasing coupled action

**Lemma 3.** For every fixed \(e\in E_c\), the function
\[
 H_e(x)=B_U(x)+\Re\Phi(x+ic;s(x),e)
 \tag{13}
\]
satisfies \(H_e'(x)<-1/20\) on \([b,1/2]\).
The same is true after any original private sampling penalty,
which is constant in \(x\), is subtracted.

*Proof.* The exact derivative along this real boundary is
\[
 \Phi_a-\Phi_t
   =3g'(t)-g'(a)-g'(e+t)+2\pi i(t-a).
\]
With \(t=s(x)\) real, its real part is
\[
 3\log(2\sin\pi t)
 -\log|e^{-2\pi c}-e^{-2\pi ix}|
 -\log|1-e^{-2\pi i(e+t)}|.
 \tag{14}
\]
The first term is negative because \(t\le.15<1/6\).
The first modulus is greater than \(3/2\): its square is
greater than \(R^2+R+1>61/25>9/4\).
The second modulus is greater than one, since
\(.37\le\Re(e+t)\le.64\) has negative cosine.
Thus (14) is less than \(-\log(3/2)\).
Together with (3) and \(x>A\), this proves
\[
 H_e'(x)<7/20-\log(3/2)<-1/20.
\]
For the last strict inequality,
\(e^{2/5}\le1+2/5+(2/5)^2/[2(1-(2/5)/3)]
=97/65<3/2\). \(\square\)

At \(x=b\), the new boundary is exactly the old real transform
cut. Its entire private main profile, its two real corners and
its private alias endpoints have their original strict calibrated
gaps. The completed old plateau comparisons give at least
\(1/20000\) for the real face. Lemma 3 preserves that gap and
adds \((x-b)/20\). It also transports the original alias penalties
without any change of sign or normalization.

## 5. Exact decomposition of the remaining physical sums

The contour change must be made in the finite source, not just in
its phase. The following partition keeps every term.

The central two-index interpolant is literally
\[
 \widehat{\mathcal J}_N(a,t,e,w)=
 e^{2\pi iNat}\Pi_N(a+t)\Pi_N(e+t)
 E_N(a)E_N(t)^3E_N(e)\Delta_N(e)^{-1}\mathcal C_N(e,w).
 \tag{14a}
\]
Here \(\Pi_N\) is the original canonical factorial, \(E_N\) its
reciprocal, and \(\mathcal C_N\) the complete ordinary endpoint
coefficient. No partial Newton sum is substituted for it.
At every retained physical pair (14a) is the corresponding exact
source summand. The new strip has
\(\Re(a+t)\in[.55,.65]\) and \(\Re(e+t)\in[.37,.64]\).
Thus its canonical branches continue without crossing a pole;
its original row power and both residue coefficients are unchanged.

First remove both true transform-end intervals using
[the physical-complement theorem](research_mixed_three_four_right_strip_physical_complement.md),
Lemma 1. Their products with the whole first factor already have
a fixed gap. Choose the lower endpoint interval shorter than
\(1/10\).

For the remaining rows, separate the private indices into their
central interval \([.27,.49]\) and its two complements. Interpret
every cut by the original half-grid convention.

1. For central private indices and physical transform coordinate
   below \(s(x)\), use the original exact private residue identity.
   The real transform derivative is greater than \(\log(3/2)\),
   as in Lemma 2 of the physical-complement theorem. Transport to
   \(t=s(x)\). Lemma 3 controls that real face, its private
   corners and private aliases; separate height convexity controls
   their joining segments.
2. For central private indices and transform coordinate in
   \([s(x),.5]\), use the original two-index interpolation and
   residue identities. Its new portion has
   \(\Re t\in[s(x),.15]\). All factorial denominators stay away
   from their zeros there. Lemma 1 transports its main horizontal
   integrals, private-face integrals and penalized horizontal
   aliases to the corresponding old point at \(\Re t=.15\).
   Both separate height convexities from Lemma 2 control the
   joining segments. The moving real transform face itself is
   paid by Lemma 3. The old part \([.15,.5]\) uses the existing
   main, face and alias estimates, including
   [the correlated-radius private-right bound](research_mixed_three_four_private_right_correlated_radius.md).
3. For private indices outside \([.27,.49]\) and physical
   transform coordinate below \(.15\), keep the transform
   coordinate real. The lower private sector first increases
   to \(t=.15\), then to \(e=.27\). The upper private sector
   first decreases to \(e=.49\), then increases to \(t=.15\).
   These are the exact whole-endpoint upper rates in
   equations (11)--(13) of the physical-complement theorem.
   The two resulting old real corners at the current incoming
   \(x\) are paid by the completed saved comparison.
4. For private indices outside that interval and transform
   coordinate in \([.15,.5)\), keep the original private-tail
   transform contour unchanged. Its faces, corners and aliases
   are already paid. In particular no extension of its complex
   private-tail lemma below \(.15\) is assumed.
5. The remaining upper physical sector with transform coordinate
   at least \(1/2\), after the true-end removal, uses
   [the upper-transform theorem](research_mixed_three_four_upper_transform_half_face.md).
   Its coupled rate decreases on the added incoming interval.

This partition is disjoint after the same half-grid choices are
made in adjacent pieces. More explicitly, let
\[
 L_N(x)=\lceil Ns(x)\rceil,\qquad
 M_N=\lceil N/2\rceil-1.
\]
The central transform rows are \(L_N(x)\le i\le M_N\);
their contour boundaries are
\((L_N(x)-1/2)/N\) and \((M_N+1/2)/N\).
Their private central indices satisfy
\(j/N\le.49+O(N^{-1})\), so \(i+j<N\) for all sufficiently
large \(N\). A jump of \(L_N\) transfers one complete physical
row between two exact pieces. It introduces no additional
incoming contour or term. We differentiate only the limiting
phase bound (13), not the discontinuous integer \(L_N\).
These cuts are at distance \(O(N^{-1})\) from (5).
On the new central rectangle all source symbols and
derivatives are uniformly regular, so these discrepancies have
rate \(o(1)\). At the old upper numerator corner use the already
proved zero-safe continuation; that issue has not moved.
The original residue coefficients, infinite sampling corrections,
and the entire Newton endpoint sums are retained.

## 6. Consequence for the complete product

**Theorem 4.** For the actual ordinary \((3,4)\) reference there
exist \(\gamma>0\), a fixed neighborhood of both complete
ordinary colors, and constants \(C,B\), such that
\[
 \left|U_{0,N}(w_L,e^{-2\pi i(x+ic)})
        V_{1,N}(w_R,e^{-2\pi i(x+ic)})\right|
       \le C N^B e^{N(M-\gamma)}
       \quad(9/20\le x\le1/2).
 \tag{15}
\]
This holds for all sufficiently large integer \(N\), at both
parities, and after any prescribed fixed ordinary-color derivatives
on a smaller neighborhood.

*Proof.* On the old central rectangle the main horizontal integral
has a strict gap by
[joint curvature](research_mixed_three_four_right_strip_joint_curvature.md).
The private-left face, the real right-transform face and all
horizontal aliases have their proved gaps in
[the original right extension](research_mixed_three_four_private_left_right_extension.md).
All four old real corners are paid by the completed
[saved comparison](research_mixed_three_four_right_strip_saved_faces_outcome.md).
The correlated-radius proof pays the private-right face.
Lemma 3 pays the moving real left-transform boundary.
Lemmas 1--2 and the exact partition in Section 5 therefore bound
every remaining physical sector and every retained contour piece.
There are finitely many types of pieces, each with a fixed
strict rate gap. Take \(\gamma\) smaller than their minimum and
allocate the arbitrary finite-source rate tolerances within the
remaining margin. Polynomial numbers of terms and contour factors
only alter \(C N^B\).

All endpoint packets and finite interpolants are holomorphic in
the original ordinary colors. The strict comparisons persist on
sufficiently small fixed color disks, uniformly on the compact
incoming interval. Cauchy's formula gives the asserted fixed
derivatives. None of these operations changes (1). \(\square\)

The failed fixed-cost tests remain recorded exactly as they were.
Equation (15) uses a smaller analytic cost for one face and a
different, explicitly justified contour boundary for the other.
It does not assert a whole-circle ordinary-pair asymptotic or a
new knot family.
