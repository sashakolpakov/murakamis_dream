# Joint main profiles on the lower left outgoing interval

Private research deduction, 8 November 2026. The two incident
conditional phases, with the original shared Fourier allocation,
have a strict joint supporting bound on the lower left interval.
The original main indices can first be clipped upward to \(1/6\).
The proof uses a horizontal Hessian bridge followed by a direct
positive derivative in the shared real coordinate.

This is a theorem about the specified original phase profiles.
The author extension in Section 6 also pays the central first/next
real low and half faces. It is not yet a complete finite-source
estimate for the lower left remainder. Physical tails, last rows,
aliases and the first incoming corner remain separate.
No numerical evaluation or change to a frozen source is used.

## 1. Actual source, allocations and domain

Keep the ordinary-next references of
[the complete lower plateau](research_mixed_next_complete_lower_plateau.md):
\[
(a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
(\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),\quad\beta=0,1.
\tag{1}
\]
The two conditional vertices are ordinary. Put \(P=[.22,.45]\),
\(A=\Re a_*\), \(\alpha=\Re y_*\), and fix all imaginary parts
at their actual reference values. The original bounds include
\[
\begin{gathered}
.24<\alpha<.36,\quad -.072<h_a<0,\quad
-.102<h_s,h_y<-.001,\\
-.108\le h_t\le.068,\qquad |h_z|\le.108 .
\end{gathered}
\tag{2}
\]
If \(\beta=1\), both \(h_t,h_z\) are negative. Use
\[
a=x+ih_a,\quad x\in P,\qquad
y=q+ih_y,\quad 0\le q\le1/5,\qquad
z=u+ih_z,\quad u\in P.
\tag{3}
\]
The original finite factors are
\[
U_{0,N}(w,X),\quad
C_{1,N}(X,Y)=\sum_{j<N}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
\quad
C_{\beta,N}(Y,Z)=\sum_{j<N}
\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
\tag{4}
\]
where \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\),
\(Z=e^{-2\pi iz}\). The exact unselected density contains
\(U_0C_1d_N(Y)C_\beta\), with outgoing allocation
\(|d_N(Z)|^{\beta/2}\). Its first integration has the original
factor \(+N\). Neither finite sum in (4) is truncated here.

With the original primitive \(g''(v)=\pi\cot\pi v-\pi i\), define
\[
\begin{split}
Q_\gamma(v;b,c)&=g(v+b)+g(v+c)-(2+\gamma)g(v)
                 -g(b)-g(c)+2\pi ibv,\\
F_1(s;a,y)&=Q_1(s;a,y)-\tfrac12g(y),\\
F_2(t;y,z)&=Q_\beta(t;y,z)-\tfrac12g(y)-\tfrac\beta2g(z),\\
\mathcal H(s,t;a,y,z)&=F_1(s;a,y)+F_2(t;y,z).
\end{split}
\tag{5}
\]
Thus the two shared halfweights give exactly \(-g(y)\).
The chirps in (5) remain present.

Let \(B_U(x)\) be the complete cap plane from
[the central-prefix theorem, equation (4)](research_mixed_next_lower_right_shoulder_central_prefix.md).
The original marginal cancellation is
\[
B_U(x)+\text{the two conditional affine planes}
\le\Lambda_{123}(z).
\tag{6}
\]
The negative cap quadratic can be dropped. The same source gives
the actual conditional index equations and
\(\kappa=1/2500000\). The individual old conditional Hessian
bound is \(-\Re F_i''\succeq2\kappa I\), for both outer real
coordinates in \(P\), the first index at least \(1/8\), and the
next index at least \(3/20\) if \(\beta=0\), or \(1/8\) if
\(\beta=1\). The source domains, including the half-index limit,
are traced in
[the next-block proof, Section 2](research_mixed_next_lower_right_shoulder_next_block.md).

## 2. The horizontal bridge to \(q=1/5\)

For the present actual phases only, the old Hessian domain has
the following simple extension. If \(v,w\) have real parts in
\([1/6,1/2)\), imaginary parts of modulus at most \(.108\), and
their sum is in the original regular strip, then
\[
V(v,w)=g(v+w)-g(v)-g(w)
\]
has strictly negative definite real horizontal Hessian.
Indeed, writing
\(\cot\pi v=a+ib,\ \cot\pi w=c+id\), one has \(a,c>0\)
and \(|b|,|d|<1\). The latter follows from the exact criterion
\[
|\Im\cot\pi(x+ih)|<1
\quad\Longleftrightarrow\quad
\cos(2\pi x)<e^{-2\pi|h|}.
\tag{7}
\]
Here \(\cos(2\pi x)\le1/2\), whereas
\[
.216\pi<\frac23+\frac2{81}<\log2.
\]
The last bound is the first two positive terms of
\(\log2=2\operatorname{arctanh}(1/3)\).
The determinant identity from
[horizontal support, equation (6)](research_mixed_horizontal_zero_mode_support.md)
now reads
\[
\det(-\Re V''/\pi)
=\frac{(a+c)^2-(cb-ad)^2}{(a+c)^2+(b+d)^2}>0.
\tag{8}
\]
It also equals \(ac-(a+c)\Re\cot\pi(v+w)\), so both
diagonal entries are positive. At an individual half face the
continuous limiting assertion is positive semidefiniteness.
All sums used below stay strictly below real part one.

The allocated decompositions are exactly
\[
\begin{split}
F_1&=V(s,a)+V(s,y)-g(s)-\tfrac12g(y)+2\pi ias,\\
F_2&=V(t,y)+V(t,z)-\beta g(t)
                  -\tfrac12g(y)-\tfrac\beta2g(z)+2\pi iyt.
\end{split}
\tag{9}
\]
The extra own terms add nonnegative negative-Hessian diagonals;
the chirps have purely imaginary horizontal Hessians.
Consequently both phases remain horizontally concave when all
their individual real coordinates lie in \([1/6,1/2]\).

Take target \(q=1/5\), with \(s_R,t_R\in[1/6,1/2]\),
and connect each phase's actual reference to its target by a
straight horizontal segment. Until the shared coordinate reaches
\(.22\), that segment stays in the old strictly positive domain.
Its initial fraction is
\[
L=\frac{\alpha-.22}{\alpha-.20}.
\]
For the remainder, (8)--(9) give semidefinite concavity.
The exact Taylor integral and both original index equations give
the joint deficit
\[
2\kappa L^2(\alpha-.20)^2
=2\kappa(\alpha-.22)^2
>\frac1{3125000000}>10^{-10}.
\tag{10}
\]
The outside linear terms cancel by (6). Hence
\[
B_U(x)+\Re\mathcal H(s,t;a,.20+ih_y,z)
<\Lambda_{123}(z)-10^{-10}.
\tag{11}
\]
Only the original fixed index heights \(h_s,h_t\) are used in
this bridge. It does not calibrate a real-index cut at height zero.

## 3. The original low main strips clip upward to \(1/6\)

The following force inequalities hold for every \(0\le q\le1/5\);
the same proofs permit \(q\le.22\).

First let \(s=v+ih_s\), \(11/100\le v\le1/6\), and allow
the first incoming real part in \([.1,.5]\), at any nonpositive
incoming height. Put \(r_s=e^{2\pi h_s}\in(1/2,1)\),
\(R=e^{2\pi h_y}\in(1/2,1)\), and \(T=e^{-2\pi\Im a}\ge1\).
The exact first force is
\[
e^{\Re Q_{1,s}}
=\frac{|T-r_se^{-2\pi i(x+v)}|
        |1-Rr_se^{-2\pi i(q+v)}|}
       {|1-r_se^{-2\pi iv}|^3}.
\tag{12}
\]
Write \(c=\cos(2\pi v)\), \(d=\cos(2\pi(v+.1))\).
The first numerator squared is at least \(5/4-d>1\):
the incoming cosine is at most \(d<1/4\), and both radial
minima occur at \(T=1,r_s=1/2\). The second numerator modulus
is at least \(\sin(2\pi v)\). Before its angle reaches
\(\pi/2\), radial minimization gives this bound; afterwards
the cosine is nonpositive and its modulus is at least one.

If \(c\ge3/4\), the own squared modulus is at most \(1/2\),
whereas \(\sin(2\pi v)>\sin(11\pi/50)>3/5\). For the last
witness use \(11\pi/50>11/16\) and
\(11/16-(11/16)^3/6>3/5\). Thus (12) exceeds one.
If \(1/2\le c\le3/4\), the own square is at most \(2(1-c)\).
The elementary pentagon bounds give
\[
d<\frac{13}{16}c-\frac7{12}\sqrt{1-c^2},\qquad
\sqrt{1-c^2}>
\frac{219}{175}-\frac{138}{175}c.
\tag{13}
\]
The second line is the concavity chord between the lower
endpoint witnesses \(\sqrt3/2>6/7,\ \sqrt7/4>33/50\).
After multiplying the squared force inequality by positive
denominators, a sufficient polynomial is
\[
-16856+46781c-25963c^2>0.
\tag{14}
\]
It is concave, and its endpoint values are \(175/4\) and
\(58009/16\). This proves \(\Re Q_{1,s}>0\) on the whole
stated low strip.

For the next own-four main strip \(1/8\le t_R\le1/6\),
put \(r_t=e^{2\pi h_t}\le1\), \(B=R^{-1}\ge1\).
Its incoming folded modulus is at least its own modulus.
Its outgoing shifted cosine is negative, so the outgoing
modulus exceeds one. The own squared modulus is at most one.
Thus
\[
e^{\Re Q_{1,t}}
=\frac{|B-r_te^{-2\pi i(q+t_R)}|
        |1-R_zr_te^{-2\pi i(u+t_R)}|}
       {|1-r_te^{-2\pi it_R}|^3}>1.
\tag{15}
\]
Here \(R_z=e^{2\pi h_z}\).

For the next own-three strip \(3/20\le t_R\le1/6\),
one has \(r_t<8/5\) and \(R_z>1/2\). These follow from
the original height bounds and the elementary exponential
witnesses also used below. Since
\(\cos(2\pi t_R)<3/5\), the incoming radial expression is
increasing for \(B\ge1\), and is again at least the own
modulus. Moreover
\[
\cos(2\pi(u+t_R))<-2/3,\qquad
|1-R_zr_te^{-2\pi i(u+t_R)}|^2
>1+\frac{r_t^2}{4}+\frac{2r_t}{3}.
\]
The own square is at most \(1+r_t^2-r_t\), and their
difference exceeds
\[
r_t\left(\frac53-\frac34r_t\right)>0.
\tag{16}
\]
The angular bound follows from \(u+t_R\in[.37,37/60]\)
and the alternating cosine bound at \(5/6>.26\pi\).
Thus the own-three force is positive as well.

In all cases the allocation terms independent of the index
do not change its derivative. Each added low main strip is
therefore bounded by its endpoint at real index \(1/6\),
with the other index and every outside coordinate held fixed.

## 4. Joint transport from \(q=1/5\) down to zero

For \(s_R,t_R\in[1/6,1/2]\), put
\(r_s=e^{2\pi h_s}\in[1/2,1]\),
\(R=e^{2\pi h_y}\in[1/2,1]\), and
\(A_t=e^{-2\pi h_t}>13/20\). The last bound has the
explicit witness
\[
2\pi h_t\le17\pi/125<3/7,\qquad
e^{3/7}<1+\frac37+\frac{9/98}{1-1/7}
=\frac{43}{28}<\frac{20}{13}.
\tag{17}
\]
The opposite height bound gives \(R,R_z,r_s>1/2\)
using \(.216\pi<\log2\).

Differentiating the original phases, including the next chirp,
gives the exact identity
\[
\exp(\partial_q\Re\mathcal H)=
\frac{|1-Rr_se^{-2\pi i(q+s_R)}|
      |A_t-Re^{-2\pi i(q+t_R)}|}
     {|1-Re^{-2\pi iq}|^3}.
\tag{18}
\]
In particular the second folded factor in (18) cannot be
replaced by the first one's radial expression.

We prove that (18) exceeds one by three rational ranges.
For \(0\le q\le1/10\), both shifted cosines are at most
\(1/2\). The two numerator squares are respectively at least
\(3/4\) and \(139/400\). The own square is at most \(9/20\),
using \(\cos(2\pi q)\ge\cos(\pi/5)>4/5\). Hence
\[
\frac34\frac{139}{400}>\left(\frac9{20}\right)^3.
\tag{19}
\]
For \(1/10\le q\le3/20\), both shifted cosines are
nonpositive. The numerator squares are at least \(1\) and
\(269/400\), while the own square is at most \(5/6\),
using \(\cos(3\pi/10)>7/12\). Therefore
\[
\frac{269}{400}>\left(\frac56\right)^3.
\tag{20}
\]
For \(3/20\le q\le1/5\), both shifted cosines are less
than \(-3/10\), whereas the own cosine exceeds \(3/10\).
Define
\[
D=1+R^2-\frac35R,\quad
U=1+\frac{R^2}{4}+\frac3{10}R,\quad
V=\frac{169}{400}+R^2+\frac{39}{100}R.
\tag{21}
\]
The own square is at most \(D\); the numerator squares
are at least \(U,V\). On \(1/2\le R\le1\),
\[
U>\frac{11}{10}D,\qquad V>\frac{10}{11}D^2.
\tag{22}
\]
For the first assertion the difference is
\((-10-85R^2+96R)/100\), concave with positive endpoint
values \(67/400,1/100\). For the second,
\[
(D^2)''=12R^2-\frac{36}{5}R+\frac{118}{25}
\ge\frac{103}{25}.
\]
Thus \(11V-10D^2\) is strictly concave. Its endpoint
values are \(207/400,27/80\), proving the assertion.
Equations (21)--(22) imply \(UV>D^3\).
This proves strict positive joint transport on all of \([0,1/5]\).

Combining (11), the clipping in Section 3, and (18)--(22) gives:

**Main-profile conclusion.** On (1)--(3), at the original
fixed heights, for
\[
11/100\le s_R\le1/2,\qquad
\begin{cases}
3/20\le t_R\le1/2,&\beta=0,\\
1/8\le t_R\le1/2,&\beta=1,
\end{cases}
\]
one has
\[
\boxed{\quad
B_U(x)+\Re\mathcal H(s,t;a,y,z)
<\Lambda_{123}(z)-10^{-10}.
\quad}
\tag{23}
\]
The \(q=0\) statement uses the continuous lower-half primitive
at the fixed nonzero height \(h_y\). This is not a replacement
of \(d_N\) by its factorial interpolation at the seam.

There is also a useful uncalibrated real-face version of the
transport lemma. In (18), either first main index may instead
be real with \(s_R\in[.11,.5]\), and either next main index
may instead be real with \(t_R\in[1/8,.5]\).
For \(q\in[.15,.2]\), the resulting squares are at least
\(1+R^2\), improving respectively \(U,V\).
For \(q\in[.1,.15]\), the first square is at least
\(1+R^2-R/2\ge1\), and the second exceeds one, so (20)
still holds. For \(q\in[0,.1]\), the first real-face
square exceeds \(9/25\), and the next real-face square
is at least \(1/2\). In combination with their main
counterparts \(3/4,139/400\), these also exceed the
own sixth-power bound \((9/20)^3\).
Thus the joint derivative is positive for these real-face
combinations too. No reference-plane calibration for those
faces at \(q=1/5\) is claimed.

## 5. What this does not yet prove

The finite factor \(U_0\) already has the complete all-real
cap plane \(B_U\) on the central first interval. The two
conditional phases in (23) are their actual regular-row
phases, with the original allocations. Nevertheless a bound
for these main profiles is not a bound for the full factors
(4). The following remain separate.

* The real lower and half cuts require a separate calibration.
  Section 6 below supplies it for the central first interval,
  using the original cuts \(1/8\) and \(3/20\) or \(1/8\).
  The bridge in Section 2 itself cannot be applied to a
  real cut by changing that height silently.
* Every conditional physical tail and last-row alternative,
  both weighted aliases, all vertical remainders and unweighted
  joins must have full source comparisons on the new domain.
  The last-row phase is different from (18).
* The initial and taper portions of the first incoming
  integral, and its right corner, need their own complete
  comparisons with the next factor retained.
* The original Fourier polynomial must keep its forcing,
  with a uniform bound through the lower seam. The
  [Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
  supplies its factorial branch on fixed compact subsets of
  \(0<\Re y<1/2,\Im y<0\). It does not by itself provide
  the required whole-source seam estimate at the full
  original depth.

Consequently (23) is not asserted as a finite bound for
\(F_{34,N}d_NC_{\beta,N}\), for either complete Fourier
coefficient, or for the signed four-piece remainder.
No conditional root continuation, nonzero packet, or
additional knot-family theorem is inferred.

## 6. Author extension: the central real low and half faces

This section adds no source premise. It combines the original
real-cut deficits on the old face \(q=.22\), recorded in
[the ordinary source assembly, Sections 1--2](research_mixed_three_row_source_assembly.md),
with direct profile comparisons. All first incoming targets
remain \(x\in P\), at their fixed negative height.
Specifically, [own four, Theorem 1](research_mixed_four_left_cut_support.md)
gives the \(1/8\) deficit \(1/2000\) on all independent
targets in \(P^2\); [the completed own-three certificate](research_mixed_three_left_cut_symmetry_completion.md)
gives the same deficit at \(3/20\); and
[the half-row theorem](research_mixed_half_row_support_completion.md)
gives it at \(1/2\). The actual references (1) belong to
their ordinary source domains. These already proved
theorems are used without evaluating or replaying any record.

First, the main-profile conclusion (23) also holds on
\(1/5\le q\le.22\). Repeat Section 2 with this value of \(q\):
the initial old-domain fraction is
\((\alpha-.22)/(\alpha-q)\), and the same deficit (10)
remains. At \(q=.22\) use the old domain throughout.
The low-main clippings of Section 3 still apply.

### 6.1. An upper clipping for the first main

At the fixed first index height \(h_s\), the first main profile
strictly decreases on \(5/12\le s_R\le1/2\), for all
\(0\le q\le.22\). To prove this let \(r=e^{2\pi h_s}\in[1/2,1]\).
The old incoming height gives \(T=e^{-2\pi h_a}<8/5\).
For \(x\in P\), the incoming shifted cosine exceeds \(-2/3\),
whereas the own cosine is less than \(-6/7\). Indeed
\[
x+s_R\in[191/300,19/20],\qquad
\cos(41\pi/150)<2/3,\qquad \sqrt3/2>6/7.
\]
For the middle witness, \(41\pi/150>17/20\), and the
alternating cosine upper bound at \(17/20\) is less than \(2/3\).
Put
\[
D_r=1+r^2+\frac{12}{7}r.
\]
The first incoming numerator square is at most
\(64/25+r^2+32r/15\), the outgoing modulus is at most \(1+r\),
and the own square is at least \(D_r\).
For \(r\ge1/2\),
\[
\begin{split}
D_r-\tfrac75(1+r)
 &=r^2+\tfrac{11}{35}r-\tfrac25\ge\tfrac1{140}>0,\\
\tfrac{49}{25}D_r-
       (\tfrac{64}{25}+r^2+\tfrac{32}{15}r)
 &=-\tfrac35+\tfrac{24}{25}r^2+\tfrac{92}{75}r
   \ge\tfrac{19}{75}>0.
\end{split}
\tag{24}
\]
Thus the squared force in (12) is strictly less than
\((49/25)(1+r)^2/D_r^2<1\), proving the clipping.
Combined with Section 3, every first main index may now be
compared upward in value to an index in \([1/6,5/12]\).

### 6.2. The next real cuts with the first main retained

Keep the first main at an index in \([1/6,5/12]\), and take
the next index real, either its original low cut
\[
\ell_\beta^0=
\begin{cases}3/20,&\beta=0,\\1/8,&\beta=1,\end{cases}
\]
or \(1/2\). For \(q\le1/5\), the positive joint derivative
was already proved after (23). For \(1/5\le q\le.22\), put
\(c=\cos(2\pi q)>9/50\). The first shifted cosine is at most
\(-13/20\), and the next shifted cosine is at most \(-c\).
The first claim follows because
\[
q+s_R\in[11/30,191/300],\qquad
\cos(41\pi/150)>\cos(43/50)>13/20;
\]
the last inequality follows from the alternating cosine
lower bound through degree six. For the second claim, on
the interval \(q+t_R\in[q+1/8,q+1/2]\) the maximum cosine
occurs at an endpoint, and
\(\cos(2\pi(q+1/8))\le-\cos(2\pi q)\) when \(q\ge3/16\).
Also \(c>9/50\) follows from
\(\sin(3\pi/50)>\sin(3/16)>9/50\).

Consequently the own square and the two numerator squares
in (18) are bounded by
\[
D=1+R^2-\frac9{25}R,\qquad
U=1+\frac{R^2}{4}+\frac{13}{20}R,\qquad
V=1+R^2+\frac9{25}R,
\tag{25}
\]
respectively, with the own square at most \(D\).
For \(1/2\le R\le1\),
\[
U>\frac{23}{20}D,\qquad V>\frac{20}{23}D^2.
\tag{26}
\]
The first difference is concave with endpoint values
\(157/1000,7/500\). For the second, \(23V-20D^2\) is
strictly concave: \((D^2)''=12R^2-(108/25)R+2662/625\)
is increasing and greater than five. Its endpoint values
are \(1249/125,61/125\). Thus (26) proves \(UV>D^3\).

The joint q derivative is therefore positive all the way
to the old face \(q=.22\). At that face the original next
real-cut deficit is \(1/2000\); the complete cap plane
and the original first main plane retain that deficit.
The upward/downward first-main clippings and positive
joint q transport pay the same real next face for every
\(0\le q\le.22\), with the first main otherwise unrestricted.

### 6.3. The first real low cut

Take the first index real at \(s_R=1/8\). The next index
may be on its original main, its real low cut or its real
half cut. Clip a next main upward to \(1/6\) when needed.
For \(q\le1/5\), use the real-face variant after (23).
For \(1/5\le q\le.22\), the first shifted cosine is less
than \(-9/20\), since
\(q+1/8\in[13/40,69/200]\) and
\(\sin(3\pi/20)>9/20\). The next shifted cosine is at most
\(-\cos(2\pi q)<-9/50\). Its folded radius is at least
\(13/20\), including either real next face.

With \(D\) as in (25), sufficient numerator squares are
\[
U=1+R^2+\frac9{10}R,\qquad
V=\frac{169}{400}+R^2+\frac{117}{500}R .
\tag{27}
\]
The following two inequalities prove \(UV>D^3\):
\[
U>\frac7{20}(4+R)D,\qquad
7(4+R)V>20D^2.
\tag{28}
\]
For the first, the difference is
\[
-\frac25+\frac{527}{500}R-\frac{137}{500}R^2-\frac7{20}R^3,
\]
strictly concave with positive endpoint values
\(59/4000,3/100\). For the second, the difference is
\[
-\frac{817}{100}+\frac{47819}{2000}R
 -\frac{6477}{500}R^2+\frac{107}{5}R^3-20R^4.
\tag{29}
\]
Its second derivative is decreasing on \([1/2,1]\)
and is already \(-5427/250<0\) at \(1/2\).
Its endpoint values are \(1577/800,8371/2000\).
This proves (28) by concavity.

The original first real-cut certificate at \(q=.22\)
has deficit \(1/2000\) after the cap plane is attached.
The next main or real-face estimate is below its own
original affine plane there. Positive joint transport
therefore pays these combinations on all \(0\le q\le.22\).

### 6.4. The first real half face

For the remaining first face \(s_R=1/2\), retain its
whole vertical segment \(s=1/2+i\sigma\),
\(h_s\le\sigma\le0\). All radial arguments in
\(1+e^{2\pi\sigma}X\) and \(1+e^{2\pi\sigma}Y\)
have modulus at most one. On the original logarithmic lift,
\[
\Arg(1+\rho e^{-2\pi ix})\ge-\pi x
\quad(0\le\rho\le1,\ 0\le x<1/2).
\]
The own factor \(1+e^{2\pi\sigma}\) is positive real.
Keeping the incoming chirp gives
\[
\Im Q_{1,s}(1/2+i\sigma;a,y)
\ge-\pi x-\pi q+2\pi x
=\pi(x-q)\ge0.
\tag{30}
\]
Hence \(\partial_\sigma\Re Q_1=-\Im Q_{1,s}\le0\).
Its real half value is at most its value at the original
negative main height. The allocation is index independent,
and the entire next profile stays attached. Sections 2--4
pay this comparison when the next index is on its main;
Section 6.2 pays it when the next index is a real cut.
No new plane at a changed index height has been assumed.

**Extended profile conclusion.** For \(0\le q\le.22\),
the sum of the complete cap plane and the two allocated
profiles is below \(\Lambda_{123}(z)-10^{-10}\) when each
conditional profile is either on its original retained main
or at its original real low or half cut. The first incoming
coordinate remains in \(P+ih_a\), and the outgoing coordinate
remains in its independent original plateau.
For comparisons using an old real-cut certificate, the
larger deficit \(1/2000\) may be weakened to this common value.

This conclusion still concerns profiles only. It does not
pay every physical row by their endpoint profiles on the
new q domain, or prove the alias and vertical-current
comparisons there. In particular the last-row alternatives,
the noncentral first incoming pieces and the full-depth
seam source remain separate obligations.
