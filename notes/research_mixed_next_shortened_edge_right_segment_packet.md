# The shortened second edge on the actual right horizontal segments

Private written finite-source theorem, 8 November 2026. The complete
shortened-edge packet extends from the actual cubic graph along each
right horizontal segment at its original fixed angular height.
Every original physical row of that shortened edge, both Fourier
denominators, and all external caps are retained. No numerical
evaluation or change to a frozen source is used.

The first complete-end edge remains eligible separately. Neither
statement estimates the complete inner trace or the remaining outer
observation.

## 1. Parameter set and exact finite statement

Use the actual positive outer family and selected cubic branch:
\[
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\quad0\le K\le1/2\},
 \qquad t_*(u)=a_*(u)-iH(u).
 \tag{1}
\]
The [cubic theorem](research_mixed_next_inner_three_cubic_continuation.md)
and [upper terminal-region theorem](research_mixed_next_shortened_edge_upper_terminal_regions.md)
give, uniformly on this compact family,
\[
 0<a_*(u)<\pi/2,\qquad 1/2<H(u)<1,\qquad
 H(u)>K .
 \tag{2}
\]
Choose once and for all a real number
\[
        \max_{\mathcal U_+}a_*(u)<a_R<\pi/2,
\]
and define the compact right-segment family
\[
 \mathcal S_R=
 \{(a-iH(u),u):u\in\mathcal U_+,\quad a_*(u)\le a\le a_R\}.
 \tag{3}
\]
The first angular height in (3) is the original \(H(u)\), held
fixed while its real part increases. The points after the initial
point are not asserted to solve the coupled cubic equation.

Keep the original Newton normalization and exact shortened cutoff:
\[
 \begin{gathered}
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 c_\nu=2\cos((2\nu+1)\pi/N),\\
 e_j(\xi)=S_j^{-2}\prod_{\nu<j}(c_\nu-\xi),\qquad
 U_N=\lfloor N/2\rfloor-1,\\
 K_N^{<}(t,u)=\sum_{j=0}^{U_N}
                     e_j(-2\cos t)e_j(-2\cos u).
 \end{gathered}
 \tag{4}
\]
This is the unchanged second edge licensed by
[the exact outer annihilator](research_mixed_next_outer_exact_low_edge_reduction.md).
In particular the odd middle row is still absent for that exact
algebraic reason. No omitted radical row is restored here.

**Theorem.** There are fixed independent complex neighborhoods
\(\mathcal O'\), \(\mathcal O\) of \(\mathcal S_R\), with
\(\overline{\mathcal O'}\subset\mathcal O\), on which
\[
 \boxed{\qquad
 K_N^{<}(t,u)=
 N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})).
 \qquad}
 \tag{5}
\]
The estimate holds for all sufficiently large levels, uniformly
at both parities. The original
holomorphic coefficient is nonzero and equals
\[
 a_e(t,u)=
 \frac{\sqrt{2\pi}}
 {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}} .
 \tag{6}
\]
The saddle, phase, and square root retain their original
normalizations. More precisely, for
\[
 E_N(t,u)=N^{3/2}e^{-N\psi(t,u)}K_N^{<}(t,u)-a_e(t,u),
 \tag{7}
\]
every fixed pair \(r,s\ge0\) satisfies
\[
       \sup_{\mathcal O'}
       |\partial_t^r\partial_u^sE_N(t,u)|
                         \le C_{r,s}/N .
 \tag{8}
\]
The derivatives are taken after the displayed exponential
normalization.

## 2. All algebraic and branch guards on the larger family

Put
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=\frac{AB}{D_0}.
 \tag{9}
\]
At fixed \(H=H(u)\), direct trigonometric identities give
\[
 \Re A=\frac{1+\cos a\cosh H}{2},\qquad
 \Im A=\frac{\sin a\sinh H}{2},\qquad
 |A|=\frac{\cosh H+\cos a}{2}.
 \tag{10}
\]
As \(a\) increases to \(a_R<\pi/2\), the first and third
expressions decrease and the second increases. The original
starting guards therefore imply
\[
 \frac12<\Re A<1,\qquad
 \Im A>\frac14,\qquad |A|<\frac{127}{144}<1 .
 \tag{11}
\]
The remaining upper imaginary guard also persists:
\[
 \Im A<\frac12\sinh1<\frac58 .
 \tag{12}
\]
For a written elementary witness,
\[
 \sinh1
 <1+\frac{1/6}{1-1/20}
   =\frac{67}{57}<\frac54.
\]
The series estimate bounds the positive terms beginning with the
cubic term by a geometric series; later ratios are strictly
smaller than \(1/20\).

The original lower bound \(|A|>85/144\) is not imported.
Instead (11) gives the sufficient strict bound \(|A|>1/2\).
The outgoing parameter is unchanged, so its original identities
and guards remain
\[
 \Re B\ge\frac12,\qquad \Im B\ge0,\qquad
 |B|<\frac{15}{14},\qquad
 \Re(1/B)>\frac{14}{15},\qquad |1/B-1|\le1 .
 \tag{13}
\]
In particular
\[
 \Re(1/W)>
       \frac{10368}{16129}-\frac1{15}>0,\qquad
 \Im(1/W)<0 .
 \tag{14}
\]
Here \(\Re(1/A)>(1/2)(144/127)^2\) and
\(\Im(1/A)<0\). Thus \(W\) lies in the first quadrant.
The same source argument for its upper modulus still applies:
writing \(1/A=x-iy\), one has \(x>3/5\), \(y>0\), and
\[
 |1/W|\ge |1/A|-\frac1{15}
       >\frac{144}{127}-\frac1{15}>1 .
 \tag{15}
\]
For its lower modulus the replacement lower \(A\)-guard gives
\[
              |1/W|\le|1/A|+|1/B-1|<2+1=3.
 \tag{16}
\]
Consequently
\[
       \frac13<|W|<1,\qquad
 y_*=\pi^{-1}\arctan\sqrt W,\qquad
             0<\Re y_*<1/4,\quad\Im y_*>0 .
 \tag{17}
\]
Every strict assertion is uniform on the compact set (3).

Keep the original regular-strip phase
\[
 \begin{split}
 b(y,z)&=-J(1/2-y+z/(2\pi))
         -J(1/2-y-z/(2\pi))-2J(y),\\
 F(y;t,u)&=b(y,t)+b(y,u),\qquad
                    J'(w)=\Log(2\sin\pi w).
 \end{split}
 \tag{18}
\]
At the saddle (17), all shifted real factorial arguments are
strictly between zero and one, with a uniform margin. The exact
exponential equation is the original one:
\[
 e^{F_y}-1
  =-\frac{(z^2+1)(D_0z^2-AB)}{z^4},
                  \qquad z=\tan(\pi y).
 \tag{19}
\]
Thus \(e^{F_y(y_*)}=1\). The family (3) is connected: it is the
continuous image of \(\mathcal U_+\times[0,1]\), with the last
coordinate interpolating \(a_*(u)\) and \(a_R\). Along each such
segment \(F_y(y_*)\) is continuous, lies in \(2\pi i\mathbb Z\),
and starts at the adopted zero lift. Hence
\[
            F_y(y_*;t,u)=0,\qquad \psi(t,u)=F(y_*;t,u)
 \tag{20}
\]
uses that same logarithmic charge.

The additive constant is also unchanged. The original closed
edge derivative form in
[the endpoint-gap theorem, Lemma 1](research_mixed_next_shortened_edge_endpoint_gap.md)
is holomorphic on a neighborhood of the whole independent box
\[
 0\le\Re t,\Re u\le\pi/2,\quad
 -1\le\Im t\le0,\quad-1/2\le\Im u\le0 .
 \tag{21}
\]
The critical value in (20) agrees with that calibrated edge phase
on the already proved independent neighborhood of the actual
cubic graph. Both are holomorphic on a connected neighborhood
of (3), using (17) and the regular factorial arguments in (18).
Analytic continuation therefore identifies them throughout that
neighborhood. No primitive or phase constant is reset.

## 3. The complete source hypotheses persist

We verify the complete contour inputs, rather than inferring
a finite packet merely from the continued stationary point.
The auxiliary cuts below may be chosen afresh uniformly for
the compact family (3); their exact half-grid rules and the
finite source (4) are unchanged.

First, the full-box endpoint theorem applies through (21):
\[
             \Re\psi(t,u)-\frac{H+K}{2}>\frac1{25}.
 \tag{22}
\]
In particular \(\Re\psi>1/25\). The real physical rate is
zero at the left endpoint. Joint continuity of the original
integrated logarithms therefore gives a fixed left interval
with a strict deficit. At the right endpoint the exact rate
is \((H+K)/2\), so the same continuity gives a fixed paid
right interval. The original zero-safe midpoint numerator
bound and sine-factorial bound turn both into estimates for
their entire positive finite row sums, with polynomial cost.
They include the exact zero row, the terminal shortened row,
all numerator zeros, and both parities.

Next, the cosine signs needed for every first-quarter comparison
remain valid:
\[
 \Re\cos t>0,\quad\Im\cos t>0,\qquad
             \Re\cos u,\Im\cos u\ge0 .
 \tag{23}
\]
The original identity
\[
 F_{yy}=-\pi\left\{
 \frac{2\sin(2\pi y)}{\cos(2\pi y)+\cos t}
 +\frac{2\sin(2\pi y)}{\cos(2\pi y)+\cos u}
 +4\cot(\pi y)\right\}
 \tag{24}
\]
therefore has \(\Re F_{yy}<0\) on the entire upper first
quarter, exactly as in the first-quarter source proof.
Choose fixed cuts
\[
        0<\alpha<\min_{\mathcal S_R}\Re y_*,
        \qquad
        \max_{\mathcal S_R}\Re y_*<\beta<1/4 .
 \tag{25}
\]
Decrease \(\alpha\) into the paid left endpoint interval.
The horizontal through \(y_*\) has its unique strict maximum
there, and its endpoints have uniform gaps. Its two local
descending germs remain the horizontal left and right ones.
The original lower reflected comparison is valid through the
quarter face: the \(t\)-cosine has a uniformly positive real
part, supplying the strict argument reserve, while the outgoing
leg has a nonnegative real part. These are precisely the
ingredients of Sections 3--4 of
[the complete lower continuation](research_mixed_next_shortened_edge_lower_continuation.md).

All upper terminal-region comparisons also persist. From
(11) one still has
\[
 |\cos t|^2<\frac94,\qquad |\cos u|<\frac87,
 \tag{26}
\]
and the angular heights retain \(H<1\), \(K\le1/2\).
Thus the original force is less than \(9/10\) along either
upper numerator-zero cut, by the exact inequalities in
[upper terminal regions, Section 3](research_mixed_next_shortened_edge_upper_terminal_regions.md).
The height ordering \(H>1/2\ge K\) is retained directly from
(2), not from a new cubic assertion at the moved angle.

For clarity these facts verify every hypothesis of the adopted
upper-continuation topology. The unchanged sidewise envelope is
continuous and subharmonic, with upward derivative jump \(2\pi\)
on each cut and no endpoint atom. Away from cuts it is harmonic;
the strict horizontal cut decrease excludes local minima there.
The bottom has inward descent except on a real outgoing cut,
where the same horizontal decrease applies. The left-side rate
increases from zero. The right-side rate decreases to height
\(K/(2\pi)\) and then increases: after its cut the outgoing leg
has vertical derivative at least \(\pi\), whereas a still
un-crossed \(t\) leg has derivative greater than \(-\pi\).
The large-height rate is still
\[
 2\pi\sigma-\frac{(\Re t)H+(\Re u)K}{2\pi}+o(1)
                           \longrightarrow+\infty .
 \tag{27}
\]
All of these are original branch identities whose proofs use
(2),(22)--(26), and not the coupled cubic equation.
The only regular stationary point is (17), by (19); it is
nondegenerate by (24).

The planar lemma and path construction in
[upper continuation, Sections 1--5](research_mixed_next_shortened_edge_upper_continuation.md)
now apply to this compact family. The left descending component
is identified by the paid left real interval and the first-quarter
horizontal and convex vertical joining segment. The other component
reaches the paid right side. This gives a strict upper path from
\(\beta+i\Im y_*\) to the right external cap. A finite parameter
cover supplies uniformly bounded lengths, positive distances from
height zero and the two wire sides, and a uniform positive action
gap. No continuous global choice of paths is required.

## 4. Exact finite assembly and independent continuation

Use the literal canonical product
\[
 \begin{split}
 B_N(y,z)&=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y;t,u)&=B_N(y,t)B_N(y,u),
 \end{split}
\]
with exactly the factorial normalization in
[the joined-contour theorem, equation (2)](research_mixed_next_shortened_edge_joined_contour.md).
Keep its same midpoint cut rules:
\[
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\quad
 \beta_N=(\lfloor N\beta\rfloor+1/2)/N,\quad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N .
 \tag{28}
\]
Here \(1/3<\gamma<1/2\) lies strictly inside the new uniformly paid
right endpoint interval. Choose the fixed external cap height \(h_c>0\)
small enough for both endpoint collars and
\(h_c<\min_{\mathcal S_R}\Im y_*/2\).
The \(O(N^{-1})\) shifts in (28) preserve all strict gaps.

The exact joined identity contains the Gaussian integral, the two
complete continuation integrals
\[
 N\int_{\Upsilon_+}\frac{T_N(y;t,u)}{1-e^{2\pi iNy}}\,dy,
 \qquad
 N\int_{\Upsilon_-}\frac{T_N(y;t,u)}{e^{2\pi iNy}-1}\,dy,
 \tag{29}
\]
both external caps, and both physical endpoint groups. The canonical
source is holomorphic throughout the open wire half-strip, including
its reciprocal-factorial zeros. Its upper bounds keep both reflection
terms. Thus the joined identity and all path replacements are
unchanged exact Cauchy identities.

The upper path supplied in Section 3 pays the first integral in
(29), with its entire denominator. The complete lower path from
the lower-continuation theorem still pays the second one. Indeed
its proof uses just the signs in (23), the first-quarter reflected
reserve, the original deep-height sine primitive, and (22).
Its deep line has the same bound
\[
 \mathfrak F(x-i;t,u)-2\pi
 \le\frac{(\Re t)H+(\Re u)K}{2\pi}+\frac1{50}
                 <\Re\psi(t,u)-\frac1{50}.
 \tag{30}
\]
The quarter descent and right external descent are monotone for
the same lower logarithmic lift. All lower frequencies are retained
through the exact second denominator in (29).

The first-quarter Gaussian integral has its original coefficient
(6), from the regular factorial expansion and (24). Its powers are
exactly \(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\). Every other piece
of the exact finite source has a uniform exponential gap. This
proves (5) on (3), with an exponential error separate from the
Gaussian's algebraic relative error.

Finally apply the independent-neighborhood argument of
[upper continuation, Section 7](research_mixed_next_shortened_edge_upper_continuation.md)
to the present compact family. Formula (17) gives compatible
holomorphic saddle and action branches on a fixed neighborhood.
The regular Gaussian root is fixed by \(\Re(-F_{yy})>0\).
Every saved remote path has a strict compact source gap, which
persists under a small independent perturbation of both angular
variables by continuity of the original sidewise envelope.
The omitted physical intervals use the uniform reciprocal-factorial
upper bound, including moving zeros, and the own-factorial shift
\[
       N[J(x+1/(2N))-J(x)]=O(1+\log N)
                    \qquad(0\le x\le1/2).
 \tag{31}
\]
The zero row stays exactly one. Hence the absolute endpoint
estimates persist as well, without extrapolating a relative
symbol across a zero.

Choose a finite cover, shrink the resulting independent neighborhood,
and move the local Gaussian contour through the nearby saddle with
short paid endpoint connectors. These steps yield (5) uniformly on
\(\mathcal O\). The normalized error (7) is holomorphic and bounded
by \(C/N\) there. Cauchy's formula on the smaller fixed neighborhood
proves (8). No derivative of a chosen contour is used.

## 5. Separate complete-end input and remaining trace

For the same right segments,
\[
 0<\Re t<\pi/2,\qquad -1<\Im t<0,\qquad
                         |\cos(t/2)|^2=|A|<1 .
 \tag{32}
\]
Thus the already proved
[free complete-end theorem, Theorem 1](research_pair_free_boundary_kernel.md)
continues to supply the packet for the full \(K_N(t,0)\) on a
neighborhood of this compact first-angle set. That theorem retains
its own full Newton source. The current note does not truncate it.

The result proved here is the complete shortened second-edge packet
on the actual right horizontal segments, with independent complex
control before a later integration in \(t\). It does not assert
the corresponding packet for all radical rows of the second edge.
Nor does it supply the remaining inner angular contour, its
aliases or endpoint currents, the outer observation estimate,
or noncancellation of the original transfer.
