# The complete first cap and the adjoining central sum

Research proof, 10 November 2026. Keep the original geometric heights,
and suppose that the private critical index of the second vertex has
nonpositive imaginary part. The complete first cap can then be
multiplied by the entire central part of the next finite sum and
bounded strictly below their original combined supporting plane.
The central interval starts at the original cut, \(3/20\) or \(1/8\),
and ends at \(1/2\). No interval between a former and a new cut is
left over.

The proof includes both horizontal Fourier corrections, their
vertical sides, and the endpoint integrals created when the principal
integral is moved. Together with the already proved low-index bound,
it leaves only the upper real-index tail of the second factor.
In the height-sign class where that entire tail is controlled, this
gives a bound for the complete first pair on the early interval.
It is an upper bound, not a new lower bound or a whole-word theorem.

## 1. Exact source and statement

Use an actual positive three/four open word of length at least three.
Its first two types are \(3+\alpha,3+\epsilon\), where
\(\alpha,\epsilon\in\{0,1\}\). Write the first two retained
geometric coordinates and the second private coordinate as
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad s_*=s_0+ih_0,
                         \qquad h_0\le0.
\tag{1}
\]
The second vertex is ordinary. The actual source bounds give
\[
 -.078<c<.021,\quad -.102<d<.068,\quad
 -.108\le h_0\le0,\qquad .246<a_0<.391 .
\tag{2}
\]
For first type three the stronger bounds \(c>-.072\),
\(a_0>.278\) hold. For first type four, \(c<-.020\).
If \(\epsilon=1\), both \(d\) and \(h_0\) are negative, so the
last condition of (1) is automatic. These are necessary bounds
on the same actual reference; independent points of the boxes
are not substituted for that reference.

Take
\[
 a=x+ic,\quad b=z+id,\qquad
 x\in[1/10,11/50],\quad z\in P=[11/50,9/20],
\tag{3}
\]
and retain
\[
\begin{gathered}
 r_N=e^{-2\pi i/N},\quad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\\
 P_j=(r_N;r_N)_j,\qquad
 R_{j,N}(a,b)=X^{-j}
       \frac{(r_NX;r_N)_j(r_NY;r_N)_j}{P_j^{\,2+\epsilon}},\\
 \ell_0=3/20,\qquad \ell_1=1/8,\qquad
 J_L=\lfloor N\ell_\epsilon\rfloor,\quad
 J_R=\lceil N/2\rceil-1 .
\end{gathered}
\tag{4}
\]
The central finite sum is precisely
\[
 C^{\rm mid}_{\epsilon,N}(X,Y)
                   =\sum_{j=J_L+1}^{J_R}R_{j,N}(a,b).
\tag{5}
\]
Let \(U_{\alpha,N}(w,X)\) and \(d_N\) be the original complete
cap and reciprocal-factorial interpolation polynomial. They are
the literal polynomials in the
[joint low- and half-index theorem](research_mixed_early_joint_low_tail.md),
not local asymptotic replacements.

Use exactly that theorem's phases
\[
\begin{split}
 \Xi_\alpha(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea
                         -\alpha g(e)-\tfrac\alpha2g(a),\\
 F_{\alpha\epsilon}(s;a,b)
 &=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias\\
 &\hspace{5mm}-(1+\alpha/2)g(a)-(1+\epsilon/2)g(b).
\end{split}
\tag{6}
\]
Here \(J'(t)=\Log(2\sin\pi t)\), \(J(0)=0\),
\(g(t)=J(t)+i\pi(t-t^2)/2\), and \(S\) is the original
complete-end action. All logarithmic lifts and the additive
normalization of \(S\) are fixed in that source.
Write \(L_\alpha=\operatorname{stat}_e\Xi_\alpha\),
\(\phi_{\alpha\epsilon}=\operatorname{stat}_s F_{\alpha\epsilon}\),
and \(\kappa=1/2500000\). Define
\[
\begin{split}
 \Gamma(z)&=\Re L_\alpha(a_*)+
          \Re\phi_{\alpha\epsilon}(a_*,b_*)\\
 &\quad+\Re\partial_b\phi_{\alpha\epsilon}(a_*,b_*)(z-b_0)
                                      -\kappa(z-b_0)^2,\\
 \gamma_*&=\kappa(a_0-11/50)^2>0.
\end{split}
\tag{7}
\]
The original critical equations cancel the two first-coordinate
marginals. Also \(\gamma_*<1/2000\), since \(a_0<.391<.45\).
The gap is uniformly positive on the containing actual-reference
domains: \(\gamma_*>\kappa(13/500)^2\).

**Theorem 1.** Under (1)--(3), for every \(\tau>0\), both
level parities satisfy
\[
\begin{split}
 &|U_{\alpha,N}(w,X)|\,|d_N(X)|^\alpha
      |d_N(Y)|^{\epsilon/2}
      |C^{\rm mid}_{\epsilon,N}(X,Y)|\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
                  \exp N\{\Gamma(z)-\gamma_*+\tau\}.
\end{split}
\tag{8}
\]
The bound is uniform on (3) and on a sufficiently small fixed
complex neighborhood of the ordinary color \(w=-2\). Every fixed
ordinary-color derivative of the cap obeys the same rate on a
smaller neighborhood. No selected first-coordinate monomial is
included.

## 2. Transport of the complete cap with a nonpositive private height

Let \(e\) range over the original cap rectangle
\[
 E_c=[.27,.49]+i[-.055,.04],
\]
and put \(s=v+i\eta\), \(\ell_\epsilon\le v\le1/2\),
\(\eta\le0\). Fix \(e,v,\eta,c,d,z\) while varying \(x\).
With \(r=e^{2\pi c}\), differentiation of (6) gives
\[
 \partial_x\Re(\Xi_\alpha+F_{\alpha\epsilon})
 =\log\frac{|1-e^{2\pi\Im e}r e^{-2\pi i(\Re e+x)}|\,
              |e^{-2\pi\eta}-r e^{-2\pi i(v+x)}|}
                    {|1-r e^{-2\pi ix}|^{2+\alpha}} .
\tag{9}
\]
The factor \(e^{-2\pi\eta}\) retains the ordinary incoming
chirp; dropping it would change the comparison.

The proof of Lemma 1 in the joint low- and half-index theorem
applies throughout the continuous interval
\(\ell_\epsilon\le v\le1/2\). For \(x\le.16\), all these
angles satisfy \(\cos(2\pi(v+x))<1/6\); for \(x\ge.16\),
they satisfy \(\cos(2\pi(v+x))<-9/50\).
Those are exactly the two inequalities used there.
For \(q\ge1\), the squared second numerator
\[
 q^2+r^2-2qr\cos(2\pi(v+x))
\]
increases with \(q\), because \(r<23/20\) and the cosine
is less than \(1/6\). Therefore (9) is at least its real-index
value \(\eta=0\). It is positive everywhere. If
\(\alpha=0\) and \(.16\le x\le.22\), it exceeds \(18/125\).
This includes the original main line, both real cuts, and
every nonpositive ordinary index height.

The [complete fixed-height cap envelope](research_mixed_cap_early_fixed_height_full_source.md)
contains its five private contour profiles, the possible right-cut
allowance \(\Delta<1/200\), and its true-end profile. Each
private profile plus \(\Re F_{\alpha\epsilon}\) increases
with \(x\) by (9). Its Fourier penalty is independent of \(x\).
The possible allowance occurs only when \(\alpha=0,c>0,x<.16\).
Transport from \(.16\) to \(.22\) saves more than
\((.22-.16)18/125=27/3125>1/200\), so it pays that allowance.
Taking the maxima over the unchanged private intervals preserves
the comparison.

For the true-end profile the derivative instead is
\[
 \log\frac{|e^{-2\pi\eta}-r e^{-2\pi i(v+x)}|}
                    {|1-r e^{-2\pi ix}|^{1+\alpha}} .
\tag{10}
\]
The numerator at \(\eta=0\) exceeds the single denominator:
\[
             x<v+x<1-x,\qquad 0<x<1/2 .
\]
Indeed \(v>0\) and \(v+2x\le.94<1\). Increasing
\(e^{-2\pi\eta}\) only increases the numerator.
Thus (10) is positive for \(\alpha=0\), and exceeds
\(-\log2\) for \(\alpha=1\), where \(r<1\).
The total unfavorable transport in the latter case is less than
\((3/25)\log2<21/250\).
At \(x=.22\) the original bare cap plane exceeds \(79/100\),
whereas the type-four true-end rate is below \(123/200\).
The reserve \(7/40\) exceeds the transport cost by \(91/1000\).
The convex outgoing halfweight comparison is unchanged.
These are precisely the true-end comparisons of the joint
low- and half-index proof. Hence that profile is retained as well.

## 3. Calibration of the main line and its downward joins

At \(x=.22\), the
[complete cap plane](research_mixed_first_cap_plateau_completion.md)
bounds every retained cap profile. The
[half-index contour theorem](research_mixed_half_index_contour.md)
and, for own type four, its
[original left-cut extension](research_mixed_four_left_cut_extension.md)
bound the whole ordinary main line
\([\ell_\epsilon,1/2]+ih_0\) by its original allocated plane
with the same quadratic coefficient \(\kappa\).
Their sum is exactly
\[
                    \Gamma(z)-2\kappa(a_0-.22)^2.
\tag{11}
\]
No reference height or marginal has been reset.

Transport (9)--(10) proves the same bound for the complete cap
times every main-line rate at (3). At either real cut, the
ordinary zero-mode join from height zero to \(h_0\le0\)
can be treated in the same way. At \(x=.22\), its original
vertical convexity bounds it by its real-cut or main-line rate.
Both original real cuts are below the ordinary plane by \(1/2000\).
The joint transport applies pointwise on this entire downward
join, so (11) bounds it as well. This uses convexity only on
the old plateau domain where it is proved; it does not infer
an early-domain Hessian bound from the fixed-height transport.

At the early targets, the two real cuts themselves, including
every cap profile, have the joint bound
\(\Gamma(z)-1/2000\), by the low- and half-index theorem.
These rates will also bound the vertical Fourier corrections.

## 4. Argument bounds for the original lower cut

Write
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,
\]
so \(Q_\epsilon-F_{\alpha\epsilon}\) is independent of \(s\).
For \(0<t<1\) and finite \(y\), the original radial argument
\(A(t,y)=\arg(1-e^{2\pi y-2\pi it})\) satisfies
\[
 \pi\min(1-2t,0)\le A(t,y)
                   \le\pi\max(1-2t,0).
\tag{12}
\]
It is the argument on the original logarithmic lift. In particular
\[
 \Im Q_{\epsilon,s}
 =A(v+x,y+c)+A(v+z,y+d)
                     -(2+\epsilon)A(v,y)+2\pi x.
\tag{13}
\]
All individual real arguments remain strictly between zero and one
for \(1/8\le v\le1/2\) and (3).

**Lemma 2.** On that domain, for every finite \(y\),
\[
 -\frac{11\pi}{5}<\Im Q_{\epsilon,s}<\frac{53\pi}{50}.
\tag{14}
\]
For \(y\ge0\), the actual bound \(c>-.078\) improves the
lower inequality to
\[
                    \Im Q_{\epsilon,s}>-\frac{77\pi}{40}.
\tag{15}
\]

*Proof.* For the upper bound, drop the nonpositive own term
in (13). The remaining quantity, divided by \(\pi\), is at most
\[
 \max(1-2v,2x)+(1-2v-2z)_+
                              \le3/4+31/100=53/50.
\]
For the lower bound it suffices to take \(\epsilon=1\).
According to whether the two shifted arguments are above or
below \(1/2\), (12) gives the following four expressions:
\[
 -1+2v-2z,\quad
 -2+4v+2x-2z,\quad
 -2+4v,\quad
 -3+6v+2x .
\tag{16}
\]
Their lower bounds are respectively \(-33/20,-11/5,-3/2,-41/20\).
The own argument is strictly below its upper bound at finite
radius when \(v<1/2\). At \(v=1/2\), the shifted arguments
give strictness directly. This proves (14).

For (15), first take \(v\ge1/5\). The four bounds (16)
are then at least \(-19/10>-77/40\).
It remains to take \(1/8\le v\le1/5\), where
\(0<v+x<1/2\).

If \(y+c\ge0\), the radius in the first shifted argument
is at least one. Monotonicity of that argument in its radius
gives
\[
                    A(v+x,y+c)\ge\pi(1/2-v-x).
\]
Together with (12), the lower expressions in (13) are now
\[
 -3/2+3v+x-2z\quad\hbox{or}\quad -5/2+5v+x,
\]
depending on whether \(v+z\ge1/2\). Their minima are
\(-77/40\) and \(-71/40\), respectively.

If \(0\le y<-c\), then \(0\le y<.078\).
The unshifted radius \(R=e^{2\pi y}\) satisfies
\[
 1\le R<e^{1/2}<5/3.
\]
The last elementary bound is proved by the positive factorial
series in the
[own-four index-barrier proof](research_mixed_first_attached_four_upper_index_barrier.md).
At a fixed \(y\ge0\), \(A(v,y)\) decreases with \(v\), since
\(\partial_v A=\pi\Im\cot\pi(v+iy)-\pi<0\).
At \(v=1/8\), if \(R\le\sqrt2\) this argument is at most
\(\pi/2\). Otherwise it equals
\[
 \pi/2+\arctan(1-\sqrt2/R)<\pi/2+\pi/10=3\pi/5.
\]
Indeed \(1-\sqrt2/R<1-3\sqrt2/5<4/25<\pi/10\).
Thus the own argument in (13) is below \(3\pi/5\).
The first shifted argument is nonnegative, the second is at
least \(-3\pi/10\), and the chirp is at least \(\pi/5\).
The resulting lower bound is \(-19\pi/10>-77\pi/40\).
This proves (15), including zero heights. \(\square\)

## 5. All Fourier corrections are paid

Take the lower and upper index heights to be \(-1/5\) and \(4\).
The outer halfweight allocations are constant in the index height,
so Lemma 2 applies to \(F_{\alpha\epsilon}\) without alteration.
Because \(\partial_y\Re F=-\Im Q_s\), (14) gives
\[
 \Re F(v-i/5)-2\pi/5
   \le\Re F(v+ih_0)-\frac{47\pi}{250}.
\tag{17}
\]
Here \(h_0\le0\), and the downward length is at most \(1/5\).
For the upper side, integrate the lower bound of (14) from
\(h_0\) to zero and then (15) from zero to \(4\).
After subtracting the upper Fourier penalty \(8\pi\), the
extra rate is strictly less than
\[
 \frac{11}{5}\frac{27}{250}\pi+
             4\frac{77}{40}\pi-8\pi=-\frac{39\pi}{625}.
\tag{18}
\]
Thus both horizontal corrections are below the main-line
rate at the same real private index. Multiplication by any
of the unchanged cap profiles preserves these comparisons.

At either real cut, the upper vertical correction has derivative
\[
 \partial_y\{\Re F(v+iy)-2\pi y\}
                                    <-3\pi/40,\quad y\ge0.
\]
The lower one has derivative
\[
 \partial_y\{\Re F(v+iy)+2\pi y\}
                                    >47\pi/50,\quad y\le0.
\tag{19}
\]
They are therefore bounded by their own real-cut rates, which
were jointly calibrated in Section 3. No convexity on the tall
upper strip is assumed.

## 6. Exact interpolation and completion of the finite central sum

The interpolation is the original one. More explicitly, let \(G_N\)
be the convergent gamma product in Section 1 of
[the exact factorial theorem](exact_factorial_interpolation_and_complex_contours.md).
For the negative root \(r_N\), take its marked version
\[
 \widehat P_N(t)=
       e^{-i\pi t(t+1)/(2N)+i\pi t/2}G_N(t).
\]
It satisfies the exact difference equation and lattice values
\[
 \widehat P_N(t+1)=(1-r_N^{\,t+1})\widehat P_N(t),
                  \qquad \widehat P_N(j)=P_j.
\]
The interpolant of the literal row (4) is consequently
\[
 \mathcal I_N(s;a,b)=e^{2\pi iNas}
 \frac{\widehat P_N(N(s+a))\widehat P_N(N(s+b))}
 {\widehat P_N(Na)\widehat P_N(Nb)\widehat P_N(Ns)^{2+\epsilon}}.
\tag{20}
\]
No interpolating periodic factor or independent logarithmic
normalization has been inserted.

Use the half-grid cuts
\[
 \ell_N=(J_L+1/2)/N,\qquad u_N=(J_R+1/2)/N.
\]
The original cotangent residue formula on
\([\ell_N,u_N]+i[-1/5,4]\) encloses exactly the rows (5).
The regular factorial arguments have real parts in compact
subintervals of \((0,1)\): their smallest limiting real part
is \(1/10\), and the largest shifted one is \(19/20\).
The exact factorial theorem permits every fixed compact
imaginary-height interval. The rectangle therefore introduces
no factorial zero or pole, and its uniform symbol has precisely
phase (6) after the original halfweights are allocated.

The constant cotangent modes combine to \(+N\) times the
central real integral. Move this integral to height \(h_0\),
retaining both downward endpoint integrals. Sections 2--3
bound the main integral and those joins with the complete cap.
The nonconstant modes give both horizontal corrections and
the four vertical half-sides; Section 5 bounds all of them.
Their physical residue signs and original scalar coefficients
remain unchanged. Triangle inequalities are used only after
this exact finite decomposition.

For \(\alpha=1\) or \(\epsilon=1\), the corresponding outer
height is negative. The original unselected Fourier estimate
therefore supplies the allocated rate \(-\Re g/2\) for each
halfweight. Each first-coordinate halfweight occurs once in
each adjoining factor, giving the full power \(\alpha\) in (8).
No Fourier value is divided out.

The common strict bound (11), the real-cut deficit \(1/2000\),
and the margins (17)--(19) leave the gap \(\gamma_*\) in (8).
Half-grid displacements, finite contour lengths and regular
symbols contribute polynomial factors and one prescribed
arbitrarily small rate tolerance. These observations apply
at both level parities, including the half-grid upper cut
at odd level.

The complete cap envelope holds over the entire real ordinary-color
interval. Its contour term has a favorable angular loss and its
true-end term has a uniform bound there. Discarding the favorable
loss gives the same estimate for all those colors. The cap has
degree less than \(N\), so the interval Bernstein--Walsh bound
extends it to a fixed complex neighborhood of \(-2\) with an
arbitrarily small extra rate tolerance. Cauchy's formula gives
the stated fixed color derivatives. This also handles zeros
of color-independent factors without division. Theorem 1 follows.

## 7. When the entire first pair is controlled

The original finite sum splits into exactly the low block
\(0\le j\le J_L\), the central block (5), and the high block
\(\lceil N/2\rceil\le j<N\). The low block is already bounded
by the joint low-row theorem with deficit \(1/2000\).

If, in addition to (1), \(c\ge0\) and \(d\le0\), the
[all-angle high-row theorem](research_mixed_all_angle_high_row_sign_class.md)
pays the complete high block with the same deficit.
The first type is then three. Consequently the literal full
ordinary factor \(C_{\epsilon,N}=\sum_{j=0}^{N-1}R_{j,N}\) satisfies
\[
 |U_{0,N}(w,X)C_{\epsilon,N}(X,Y)|\,|d_N(Y)|^{\epsilon/2}
 \le C_\tau N^{A_\tau}
                  e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{21}
\]
There is no missing finite-index range in this corollary.
It has the same parity and ordinary-color scope as (8).
For an adjoining type four, the conditions \(h_0<0,d<0\)
are automatic, so only the first attached height condition
\(c\ge0\) is additional. No claim about how many actual words
satisfy that condition is made.

Without these height signs, Theorem 1 and the low-row theorem
still remove all central and lower contributions, but the full
high physical tail must be bounded separately. Positive private
index height, a selected first Fourier monomial, movement of the
outer heights, and later outer-contour joins are also outside
this theorem. Neither (8) nor (21) supplies a lower bound for
the whole knot invariant or proves short-partial-filling stability.

## Direct source versions

The proof uses written inequalities and the original finite
interpolation. No new mathematical numerical evaluation, saved-value
arithmetic, test, compilation, or frozen-source edit was performed.

| Source | SHA-256 |
|---|---|
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_half_index_contour.md | ed8d13779e734803090f778d01ddc334469cbfb7a35154ba48d6eb462c28c57e |
| research_mixed_four_left_cut_extension.md | b8a496417f6c6b619508d2ad644eaef47d7fd4408d412bc28a3e92b09d98b96b |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_first_attached_four_upper_index_barrier.md | 863353130161d320a666d2da944eb5da5ef79bc3bbeac60ea1d651db24ea8f06 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
