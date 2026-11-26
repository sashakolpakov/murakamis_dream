# The incoming left taper on the full lower boundary interval

Research proof, 8 November 2026. This extends the earlier left-taper
estimate from the following vertex's matched boundary coordinate to
every independent real coordinate in its required lower interval.
The extension changes the estimates for the physical outer rows and
raises the upper auxiliary contour. The original finite sum, all its
contour terms, and the full first cap remain in the calculation.
No numerical evaluation is used.

The result concerns an ordinary next vertex. It does not estimate
the incoming real segment before the taper, the next boundary contour
outside its central interval, or the remaining selected Fourier term.

## 1. The finite expression and its normalization

Use the ordinary-next references and allocations of
[the incoming-corner theorem](research_mixed_next_unselected_incoming_corner_union.md)
and [the right-tail theorem](research_mixed_next_unselected_incoming_right_tail.md).
Thus the three flags are \((0,1,\beta)\), \(\beta=0,1\), the
second and third vertices are ordinary, and
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3).
\]
Write \(A=\Re a_*\), \(h_a=\Im a_*\), \(h_s=\Im s_*\),
\(h_y=\Im y_*\), and \(\alpha=\Re y_*\). The original
reference enclosures give
\[
 .278\le A\le.391,\qquad -.072<h_a<0,\qquad
 -.102<h_s,h_y<-.001.
 \tag{1}
\]
Set \(P=[.22,.45]\). The independent boundary variables are
\[
 y=q+ih_y,\qquad z=u+i\Im z_*,\qquad q,u\in P.
 \tag{2}
\]
The incoming path and its moving real index cut are
\[
 a(x)=x+ih_a(x-.1)/.12,\qquad
 \sigma(x)=39/400+x/8,\qquad .1\le x\le.22 .
 \tag{3}
\]
These paths and all index cuts are held fixed when differentiating
outside parameters.

For \(r=e^{-2\pi i/N}\), let \(P_j=(r;r)_j\) and
\(p_j(X)=(rX;r)_j\), with \(P_0=p_0=1\). The complete factors are
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{k=0}^{N-1}H_N(w,r^{-k})p_k(X)/P_k,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
                 X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{N-1}
                 Y^{-j}p_j(Y)p_j(Z)/P_j^{2+\beta}.
\end{split}
\tag{4}
\]
The original Fourier weight \(d_N\) is the degree-at-most-\(N-1\)
polynomial satisfying \(d_N(r^b)=P_b^{-1}\).
Put \(X=e^{-2\pi ia(x)}\), \(Y=e^{-2\pi iy}\), and
\(Z=e^{-2\pi iz}\).

The bare conditional phase and its allocated version are
\[
\begin{split}
 Q(v;a,y)&=g(a+v)+g(y+v)-3g(v)-g(a)-g(y)+2\pi iav,\\
 F(v;a,y)&=Q(v;a,y)-\tfrac12g(y),\\
 p_L&=Q_a(s_*;a_*,y_*),\\
 p&=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\},\\
 A_*&=\Re\{T_0(a_*)+F(s_*;a_*,y_*)\},\qquad
 \kappa_0=1/2500000 .
\end{split}
\tag{5}
\]
Here \(g'(v)=\log(1-e^{-2\pi iv})\) has the original lift;
\(T_0\) is the original first-cap action. In particular,
\(T_0'(a_*)+p_L=0\). The cap supporting plane is
\[
 B_U(x)=\Re T_0(a_*)-\Re p_L(x-A)-\kappa_0(x-A)^2.
 \tag{6}
\]
The third vertex's original plane \(B_3(q,u)\) and the original
next action \(\Lambda_{123}(z)\) satisfy
\[
 A_*+p(q-\alpha)+B_3(q,u)\le\Lambda_{123}(z).
 \tag{7}
\]
Their full definitions, including all outgoing halfweights, are in
[paired localization, Section 2](research_mixed_next_low_cardinal_paired_localization.md).
No action constant is changed here.

**Theorem.** Uniformly over (1)--(3), both level parities, and
every real ordinary color \(w\in[-2,2]\),
\[
\begin{split}
 &|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{\beta,N}(Y,Z)|
                                      |d_N(Z)|^{\beta/2}\\
 &\hspace{15mm}\le
 C N^B\exp\{N(\Lambda_{123}(z)-10^{-10})\}.
\end{split}
\tag{8}
\]
The same estimate, with a different polynomial prefactor, holds
after integration over the taper with its original measure
\(N a'(x)\,dx\). Fixed real-color derivatives have polynomial cost.
At the actual output \(z_*\), on sufficiently small fixed
complete-color and output neighborhoods, the unweighted integral
normalized by the original next action has every fixed normalized
mixed derivative bounded with gap \(10^{-11}\).

The local statement removes the outgoing halfweight using its
nonzero packet at the actual output, exactly as in the right-tail
theorem. It does not divide by that weight on the independent
interval at a possible zero.

## 2. The low rows and the moving real cut

The incoming derivative of a regular first-cap profile coupled to
\(Q(v;a(x),y)\) is independent of \(y\). The profilewise derivative
estimates of
[the calibrated moving-cut proof](research_mixed_three_four_following_left_moving_cut.md),
Sections 3--4, therefore remain available. We check the only new
input to its moving-cut argument: the index force.

Write \(B=e^{-2\pi\Im a(x)}\ge1\) and \(R=e^{2\pi h_y}>1/2\).
The latter follows from \(.204\pi<2/3<\log2\). At a real
index \(v\),
\[
 e^{\Re Q_v(v;a(x),y)}
 =\frac{|B-e^{-2\pi i(x+v)}|\,|1-Re^{-2\pi i(q+v)}|}
             {(2\sin\pi v)^3}.
 \tag{9}
\]
For \(.11\le v\le1/8\), the first shifted coordinate is in
\([.21,.345]\), with cosine less than \(1/4\).
Its modulus is greater than \(11/10\), even with the weaker
bound \(B\ge5/6\) used in the original proof.
The second shifted coordinate is in \([.33,.575]\).
Its cosine is less than \(-4/9\), since
\(\sin(4\pi/25)>\sin(1/2)>23/48>4/9\).
Consequently its squared modulus exceeds
\[
 1+\tfrac14+\tfrac49=\tfrac{61}{36}>(13/10)^2.
\]
Since \(2\sin(\pi/8)<4/5\), (9) gives
\[
 e^{\Re Q_v}>\frac{(11/10)(13/10)}{(4/5)^3}
              =\frac{715}{256}>\frac{11}{4}>e.
 \tag{10}
\]
On the part \(x\ge.18\), \(v=\sigma(x)\ge.12\), the first
modulus exceeds \(8/5\). Thus
\[
 e^{\Re Q_v}>\frac{(8/5)(13/10)}{(4/5)^3}
              =\frac{65}{16}>4,\qquad \Re Q_v>4/3.
 \tag{11}
\]
These are precisely the two force bounds required in the old
moving-cut proof. Its inequalities for the incoming derivative,
including its true-cap-end alternative, are unchanged. In
particular, each retained cap profile \(\Psi_0(e,a)\) satisfies
\[
 \frac d{dx}\Re\{\Psi_0(e,a(x))+Q(\sigma(x);a(x),y)\}>2/75.
 \tag{12}
\]
The same assertion holds in the integrated one-sided sense for
the cap's explicit end profile.

At \(x=.22\), the cut is exactly \(1/8\). The original
[type-four left-row certificate](research_mixed_four_left_cut_support.md)
covers every independent target in \(P^2\), at the actual
reference heights. Adding (6), its two incoming marginals cancel.
It follows, before maximizing the cap profiles, that
\[
 \mathcal E_U(x)+\Re F(\sigma(x);a(x),y)
 \le A_*+p(q-\alpha)-1/2000
                 -(2/75)(.22-x).
 \tag{13}
\]
Here \(\mathcal E_U\) is the full cap-rate envelope of the
earlier left-taper proof, including its real cuts, physical tails
and explicit end alternative. Its inactive private Fourier terms
are bounded by the same profiles. All these bounds hold for
every real color by
[the real-color extension](research_mixed_three_four_following_left_real_colors.md),
Section 1.

Every lower physical row is bounded by the moving cut. To see this
on the enlarged \(q\)-interval, the first-modulus comparison in
[the preceding lower-row proof](research_mixed_four_upper_rows_following_domains.md),
Section 6, still gives
\(|B-e^{-2\pi i(x+v)}|>2\sin\pi v\) for \(0<v\le.15\).
For \(.03\le v\le.15\), \(q+v\in[.25,.60]\), so the
second modulus is at least one and (9) is greater than
\((2\sin\pi v)^{-2}>1\).
For \(0<v<.03\), both numerator moduli exceed \(1/2\):
the first shifted coordinate lies in \((.1,.25)\);
the second in \((.22,.48)\), where either its cosine is
nonpositive or its sine exceeds \(1/2\).
The denominator is less than \((1/5)^3\), since
\(2\pi(.03)<1/5\). Thus (9) is greater than \(125/4\).
The real rate increases from its continuous value zero at \(v=0\).
The usual zero-safe finite-product upper bound now applies to
all \(j<\lceil N\sigma(x)\rceil\), retaining the exact zero row.

## 3. Every upper physical row reduces to the half row or last row

We prove the needed endpoint comparison on the larger domain
\[
 .1\le x\le.22,\qquad .22\le q\le.45,\qquad
 5/8\le R_a\le1,\quad 0<R_y\le1,\quad
 0\le\lambda\le-\log R_a.
 \tag{14}
\]
Put \(f_R(t)=\log|1-Re^{-2\pi it}|\) and
\(J(t)=\int_0^t\log(2\sin\pi v)\,dv\).
The reflected row rate, after subtracting the last-row rate, is
\[
 \mathscr F(v)=
 -\int_{x-v}^x f_{R_a}(t)\,dt
 -\int_{q-v}^q f_{R_y}(t)\,dt+3J(v)-\lambda v .
 \tag{15}
\]
This is the exact reflection of the physical row \(1-v\);
the incoming carrier is the retained term \(-\lambda v\).
For \(0<v\le1/5\), the minimum-integral-arc argument of
[the preceding upper-row theorem](research_mixed_four_upper_rows_following_domains.md),
Section 2, applies unchanged: \(v\le q\le1/2\). It gives
\[
 \mathscr F(v)\le v\{\log(4\pi v)-1\}-\lambda v<0.
 \tag{16}
\]

For \(1/5\le v\le1/2\), set \(S(v)=2\sin\pi v\) and
\(T=R_a^{-1}\le8/5\). Since \(e^{-\lambda}\ge R_a\),
\[
 e^{\mathscr F'(v)}
 \ge\frac{S(v)^3}
 {|T-e^{-2\pi i(x-v)}|\,|1-R_y e^{-2\pi i(q-v)}|}.
 \tag{17}
\]
The following four intervals prove that this ratio exceeds one.
The squared first modulus is increasing in \(T\ge1\).
The squared second modulus is at most
\(\max(1,4\sin^2\pi(q-v))\).

* If \(1/5\le v\le11/50\), then \(|x-v|\le.12\),
  \(|q-v|\le1/4\). The two squared moduli are at most
  \(223/175\) and \(2\), respectively, whereas
  \(S(v)^6>(11/8)^3>446/175\).
  Here \(\cos(6\pi/25)>5/7\).
* If \(11/50\le v\le1/4\), then \(|x-v|\le.15\),
  \(|q-v|\le.23\). The squared moduli are at most
  \(303/175\) and \(2\), whereas
  \(S(v)^6>(5/4)^6>606/175\).
  We used \(\cos(3\pi/10)>4/7\) and
  \(\sin(11\pi/50)>5/8\).
* If \(1/4\le v\le7/20\), then \(|x-v|\le1/4\),
  \(|q-v|\le1/5\). The squared moduli are at most
  \(89/25\) and \(3/2\), whereas \(S(v)^6\ge8>267/50\).
* If \(7/20\le v\le1/2\), the moduli are at most \(13/5\)
  and \(2\), whereas
  \(S(v)^3>(7/4)^3>26/5\).

These are rational comparisons with elementary trigonometric
witnesses. For example,
\[
\begin{split}
 \cos(6\pi/25)&>1-(132/175)^2/2=21913/30625>5/7,\\
 \cos(3\pi/10)^2&=(5-\sqrt5)/8>11/32>16/49,\\
 \sin(11\pi/50)&>\sin(11/16)>
       11/16-(11/16)^3/6=15565/24576>5/8,\\
 \cos(3\pi/20)&>1-(33/70)^2/2>7/8 .
\end{split}
\tag{18}
\]
Also \(S(1/5)^2=(5-\sqrt5)/2>11/8\).
At numerator zeros the derivative has an integrable logarithmic
singularity. Integration on the complementary intervals shows
that \(\mathscr F\) is strictly increasing on \([1/5,1/2]\).
Together with (16) and \(\mathscr F(0)=0\), this proves the
endpoint comparison for every upper physical row.

For (3), the radius hypothesis holds because
\(e^{2\pi|h_a|}<8/5\), as proved in the preceding row theorem.
The zero-safe finite consequence bounds the complete upper sum
by the two endpoint rates, with an arbitrarily small fixed rate
tolerance and a polynomial prefactor. This includes the even
half row, the first odd row above one half, and all revived rows.

The half-row branch is paid by the original independent-\(P^2\)
[half-row certificate](research_mixed_half_row_support_completion.md)
at \(x=.22\), followed by the old positive incoming transport.
That transport is independent of \(y\). The last-row branch
uses the full cap disk bound and the exact last-row carrier:
\[
 b_0+c_{\rm b}+2\pi|\Im a(x)|
 <\frac{11099}{7000}<\frac{2383}{1500},
 \quad b_0=101/125,\quad c_{\rm b}<13/40 .
 \tag{19}
\]
The disk estimate and rational reserve are recorded in the
right-tail theorem, Section 5. The original marginal calculation
in [the low-block theorem, Section 2](research_mixed_conditional_lower_output_low_block.md)
pays any such prefix ceiling on all of (2), with gap greater
than \(1/50\), after the remaining weight and third kernel
are included. It applies here to a pointwise bound; it does
not require that the bound was originally obtained for low rows.

## 4. The complete main contour

Use private height \(h_s\) for the middle index. On the added
segment \(\sigma(x)\le v\le.15\), set
\(\rho=e^{2\pi h_s}\in(1/2,1)\). The exact force is
\[
 e^{\Re Q_v(v+ih_s;a(x),y)}
 =\frac{|B-\rho e^{-2\pi i(x+v)}|\,
              |1-\rho R e^{-2\pi i(q+v)}|}
             {|1-\rho e^{-2\pi iv}|^3}.
 \tag{20}
\]
The squared numerators exceed
\[
 N_1=25/36+\rho^2-5\rho/12,\qquad
 N_2=1+\rho^2/4+4\rho/9.
\]
The squared denominator modulus is less than
\(D=1+\rho^2-47\rho/40\), since
\(\cos(.3\pi)>47/80\), as in the old main-contour proof.
Now
\[
 N_1-D\ge53/720,\qquad
 N_2-D=\rho(4/9+47/40-3\rho/4)>0,\qquad D\le33/40.
 \tag{21}
\]
Thus the main profile strictly increases up to \(v=.15\).

For \(.15\le v\le.5\), the profilewise incoming derivative
and the true-cap-end derivative in
[the complete left-taper proof, Section 3](research_mixed_three_four_following_left_taper_source.md)
are independent of \(y\). They transport every profile to
\(x=.22\) before taking its maximum. At that endpoint, the
full three-variable horizontal supporting inequality for \(F\),
as stated in the corner theorem, applies to
\((.22,v,q)\in P\times[1/8,.5]\times P\) at the actual
heights \(h_a,h_s,h_y\).
Adding the full cap plane (6) cancels the incoming marginal.
The remaining deficit is at least
\[
 \delta_L=\kappa_0(A-.22)^2
 \ge\frac{841}{625000000000}>10^{-9}.
 \tag{22}
\]
Only the cap's quadratic deficit is used in this bound.
No extra quadratic constant is inferred from strict concavity.
Equations (20)--(22) pay the entire main contour relative to
\(A_*+p(q-\alpha)\), with the allocation \(-g(y)/2\) retained.

The same incoming transport at the real index \(v=.5\)
starts from the completed half-row certificate at \(x=.22\).
It therefore pays this real cut with its separate \(1/2000\)
deficit. Equation (13) pays the other real cut.

## 5. Curvature on the enlarged target interval

Write
\[
 C(v+i\eta)=\Re\cot\pi(v+i\eta)
    =\frac{\sin2\pi v}{\cosh2\pi\eta-\cos2\pi v}.
\]
For every \(x\in[.1,.22]\), \(q\in P\), every incoming
height, the fixed outgoing height in (1), and
\(.11\le v\le.5,\ |\eta|\le.12\), we have
\[
 -\Re Q_{vv}(v+i\eta;a(x),y)>\pi/84.
 \tag{23}
\]
Here is an explicit extension of the curvature proof in
the moving-cut note. We retain its bound
\(\cosh(2\pi\eta)<4/3\). A shifted positive cotangent is
bounded above by its real-height value; a shifted coordinate
at least \(1/2\) has nonpositive real cotangent.

On \([.11,7/40]\), the own sine exceeds \(5/8\), its cosine
exceeds \(9/20\), and hence \(3C(v+i\eta)>225/106\).
The two shifted cotangents are less than \(4/3\) and \(2/3\).
The difference exceeds \(13/106>1/84\).
The outgoing bound uses
\(\cot(.33\pi)=\tan(.17\pi)<2/3\):
\(.17\pi<11/20\) and
\(\tan t\le t/(1-t^2/2)\le440/679<2/3\).
The own cosine bound follows from
\(\cos(.35\pi)=\sin(.15\pi)>
15/32-(15/32)^3/6>9/20\).

On \([7/40,1/4]\), the old bounds \(3C>9/5\),
\(C(a+v+i\eta)<1\), and \(C(y+v+i\eta)<7/12\)
remain valid. On \([1/4,7/20]\), the own sine exceeds
\(4/5\), its denominator is less than \(7/3\), and the two
shifted cotangents are at most \(7/12\) and \(1/10\).
Thus the difference exceeds \(36/35-7/12-1/10>1/84\).
Here \(\cot(.47\pi)=\tan(.03\pi)<1/10\).

On \([7/20,2/5]\), the outgoing cotangent is nonpositive,
the incoming one is less than \(\cot(.45\pi)<1/6\), and
the own term satisfies \(3C>9/14\). Their difference is
greater than \(10/21\).
Finally, on \([2/5,1/2]\), the incoming cotangent is
nonpositive and the own one nonnegative.
The outgoing real coordinate belongs to \([.62,.95]\);
its sine is less than \(-3/10\). Its height has modulus
at most \(.222\), so the old bound
\(\cosh(2\pi\cdot.222)<11/5\) gives an outgoing cotangent
less than \(-3/32\). This proves (23) throughout.

In particular each real phase profile is convex in private
height on this strip. This statement is made before maximizing
or eliminating a private variable.

## 6. Both Fourier remainders and all connecting sides

Let \(\mathcal J(v,\eta)=\Im Q_v(v+i\eta;a(x),y)\).
The original logarithmic argument inequalities give
\[
 \mathcal J(v,\eta)<9\pi/10\quad(\eta\le0),\qquad
 \mathcal J(v,\eta)>-197\pi/100\quad(\eta\ge h_s).
 \tag{24}
\]
For the first bound, at \(\eta\le-.12\) the two numerator
radii are less than \(\sqrt2/2\) and \(1/2\).
Their argument magnitudes are at most \(\pi/4,\pi/6\).
The own argument is nonnegative and \(2x\le.44\), giving
\(\mathcal J/\pi<257/300<9/10\).
Curvature (23) transports this upper bound from \(-.12\)
through zero.

For the second bound, at \(\eta\ge.12\) both shifted heights
are nonnegative. Use the same four original argument cases
as in the earlier left-taper proof. Depending on whether
\(x+v\) and \(q+v\) are less than \(1/2\), their lower bounds
for \(\mathcal J/\pi\) are, respectively,
\[
\begin{array}{c|c}
 x+v<1/2,\ q+v<1/2&-2+4v+x-q\\
 x+v\ge1/2,\ q+v<1/2&-3/2+3v-q\\
 x+v<1/2,\ q+v\ge1/2&-3/2+3v+x-2q\\
 x+v\ge1/2,\ q+v\ge1/2&-1+2v-2q .
\end{array}
\tag{25}
\]
With \(v\ge.11,x\ge.1,q\le.45\), these are bounded below
by \(-191/100,-162/100,-197/100,-168/100\).
All finite-height inequalities have a strict reserve.
Equation (23) transports the bound down from \(.12\)
through \(h_s\).

Keep the lower auxiliary height \(-1/5\), and replace the
old upper height \(5/4\) by the fixed height \(8\).
The corresponding Fourier penalties are \(2\pi/5\) and \(16\pi\).
Integrating (24) from the main height gives
\[
\begin{split}
 \Re Q(v-i/5)-2\pi/5
     &<\Re Q(v+ih_s)-11\pi/50,\\
 \Re Q(v+8i)-16\pi
     &<\Re Q(v+ih_s)-1953\pi/50000
      <\Re Q(v+ih_s)-1/10.
\end{split}
\tag{26}
\]
For the second inequality,
\((197/100)(8+51/500)-16=-1953/50000\).
These comparisons are pointwise in every retained cap profile.

The weighted upper connecting sides have height derivative
\(-\mathcal J-2\pi<-3\pi/100\); the lower sides have
\(-\mathcal J+2\pi>11\pi/10\).
They are bounded by their real-cut endpoints.
The two unweighted sides between \(h_s\) and zero are
convex by (23), and therefore bounded by their real and
main-height endpoints. Every endpoint has already been paid.

## 7. Assemble the literal finite source

Put \(L_N(x)=\lceil N\sigma(x)\rceil\), \(M_N=\lceil N/2\rceil\).
Partition the actual indices into \(j<L_N\), \(L_N\le j<M_N\),
and \(M_N\le j<N\). Sections 2--3 bound the two physical
outer groups. On the middle group use the original canonical
interpolant
\[
 e^{2\pi iNav}
 \frac{\Pi_N(a+v)\Pi_N(y+v)}
      {\Pi_N(a)\Pi_N(y)\Pi_N(v)^3}
 \tag{27}
\]
and half-grid real cuts \((L_N-1/2)/N,(M_N-1/2)/N\).
Its exact finite-contour decomposition retains the original
\(+N\) main density, both horizontal Fourier remainders,
four weighted vertical pieces, and two unweighted joins.
Raising a finite auxiliary height changes none of its residues.
All real arguments stay in fixed regular strips:
\[
 .21\le\Re(a+v)\le.72,\qquad
 .33\le\Re(y+v)\le.95,\qquad .11\le\Re v\le.5.
 \tag{28}
\]
The original factorial interpolation is uniform on every fixed
compact imaginary interval, so the height \(8\) is allowed.
Half-grid displacements cost a vanishing rate tolerance.
No moving numerator zeros are deleted from the physical groups.

The full cap envelope used throughout includes its own contour
terms, physical end rows, and coherent coefficient polynomial.
The all-real-color theorem preserves each of those upper bounds.
Thus (13), (19), (22) and (26) bound every part of the finite
sum (4).

Finally the original lower-strip weight and third-factor bounds give
\[
\begin{split}
 |d_N(Y)|^{1/2}
   &\le C_\tau N^{B_\tau}e^{N(-\Re g(y)/2+\tau)},\\
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)|^{1/2}|d_N(Z)|^{\beta/2}
   &\le C_\tau N^{B_\tau}e^{N(B_3(q,u)+\tau)} .
\end{split}
\tag{29}
\]
Both the factorial and forcing alternatives of \(d_N\) are
retained in the first inequality. Their use is valid because
\(-\Re g(y)>0\) on the actual compact lower interval.
The allocation in \(F\) and (7) now put every main/cut/current
term below \(\Lambda_{123}(z)\) by (22).
The last-row branch instead uses the larger separate reserve
following (19).
Choose all finite-product tolerances inside the strict reserve
between (22) and \(10^{-10}\). This proves (8).

The measure and bounded path length cost only polynomial factors.
Markov's inequality applies to the exact color polynomial.
All strict source bounds persist on small fixed complex
neighborhoods at the actual outside parameters, so Cauchy's
formula gives the stated fixed normalized derivatives.
The outgoing nonzero packet removes the halfweight locally,
with the original absolute action and a reduced gap \(10^{-11}\).

Together with the right-tail theorem this controls the left taper
and the full incoming right tail on the lower interval.
The incoming real segment \(0\le a\le.1\) remains separate.
Neither these estimates nor the local central Gaussian alone
complete the next transfer or the finite-exceptions theorem.
