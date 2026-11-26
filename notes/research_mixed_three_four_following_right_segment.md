# The right horizontal segment on the actual following family

Research deduction, 7 November 2026. This proves a complete-source gap on
the horizontal interval from \(9/20\) to \(1/2\), at the actual incoming
reference height of the following family. It does not replace the fixed
complementary contour by a contour at that new height.

## 1. Actual references and the claim

Use the actual half-chain and notation of the
[following plateau theorem](research_mixed_three_four_following_plateau_source.md).
For \(c\in K=O_3,O_4,A_3,A_4\), write
\[
 a_*=A+ih_a,\qquad (p_*,q_*)=F_4(a_*,c),\qquad h_p=\Im p_*,
 \qquad \mathscr P(c)=T_0(a_*)+Q(p_*;a_*,q_*),                 \tag{1}
\]
where the last equality is the stationary absolute pre-Gram action and
\[
 Q(t;a,z)=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat.              \tag{2}
\]
Every primitive and lift is the original one. In particular
\[
 \begin{gathered}
 .278\le A\le.391,\quad -.072\le h_a\le.021,\\
 .24\le\Re p_*,\Re q_*\le.36,\quad
 -.102\le h_p,\Im q_*\le-.001.                              \tag{3}
 \end{gathered}
\]
These are actual correlated references, not arbitrary points of their
containing rectangles.

Put \(\kappa=1/2500000\). The
[complete upper-target cap theorem](research_mixed_cap_upper_target_completion.md)
applies to this own-three cap with its actual following type-four input.
It gives the whole cap plane on \(x\in[.22,.5]\),
\[
 B_U(x)=\Re T_0(a_*)+\Re T_0'(a_*)(x-A)-\kappa(x-A)^2.         \tag{4}
\]
For complete left color, the stationary marginal cancellation is
\(T_0'(a_*)+Q_a(p_*;a_*,q_*)=0\).

**Theorem.** There is a constant \(\delta_R>0\), uniform on the actual
compact families \(K\), such that for every fixed ordinary-color
derivative order
\[
 \left|\partial_w^k
  \{U_{0,N}(w,e^{-2\pi i(x+ih_a)})
                  C_{1,N}(e^{-2\pi i(x+ih_a)},e^{-2\pi iq_*})\}\right|
 \le C_kN^{B_k}e^{N(\Re\mathscr P(c)-\delta_R)},
 \quad .45\le x\le.5,\quad w\in[-2,2].                     \tag{5}
\]
Both parities and the entire conditional finite sum are included.
For each fixed base \(c_0\in K\), the same exponential conclusion holds
for
\[
 N\int_{.45+i\Im a(c_0)}^{.5+i\Im a(c_0)}
       U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},e^{-2\pi iq(c)})\,da
                                                                    \tag{6}
\]
after multiplication by \(e^{-N\mathscr P(c)}\), with all fixed
ordinary/\(c\) derivatives on a fixed neighborhood of \(c_0\).
A small complete-color disk is also allowed. The contour in (6) is
fixed at its base point; no derivative of a reference-varying path is
asserted.

## 2. Main profiles and the moving real cut

Keep the actual index height \(h_p\), and put
\[
       s(x)=\frac{23}{40}-x\in[3/40,1/8].                    \tag{7}
\]
The new real cut starts at the certified ordinary cut \(1/8\) when
\(x=.45\). For \(t=u+ih_p\), \(u\in[s(x),1/2]\), one has
\(x+u\ge23/40\). Let
\(C(v)=\Re\cot\pi v\). At fixed heights, the negative real Hessian
of (2) in the real variables \((x,u)\), divided by \(\pi\), is
\[
 \begin{pmatrix}C(a)&0\\0&3C(t)-C(q_*+t)\end{pmatrix}
       -C(a+t)\begin{pmatrix}1&1\\1&1\end{pmatrix}.          \tag{8}
\]
Here \(C(a)\ge0\) and \(C(a+t)\le0\). Also
\(3C(t)>C(q_*+t)\). Indeed the latter cotangent is nonpositive
if \(u\ge.26\). Otherwise \(3/40\le u\le.26\), and
\[
 \sin(2\pi u)>9/20,\quad \cos(2\pi u)>-1/10,
 \quad \cosh(.204\pi)<5/4
\]
give \(C(t)>1/3\), whereas a positive \(C(q_*+t)\) is strictly
less than \(\cot(\pi/4)=1\), since
\(\Re(q_*+t)\ge.315>1/4\). Thus (8) is positive semidefinite.
The elementary trigonometric bounds follow from the quadratic cosine
bound and the cubic sine bound, with \(3.14<\pi<22/7\);
the hyperbolic bound follows by its even power series at \(13/20\).

On the old rectangle \(x\in[.22,.45]\), \(u\in[1/8,.5]\), the
[original zero-mode support](research_mixed_horizontal_zero_mode_support.md)
and [own-four left extension](research_mixed_four_left_cut_extension.md)
give negative real Hessian at least
\(\mu I\), \(\mu=1/1250000\), for the allocated phase. Removing
its outgoing halfweight changes only a constant here. Adding (4)
does not weaken concavity. Along the straight segment from the actual
critical pair \((A,\Re p_*)\) to any \(x\ge.45,u\in[1/8,.5]\),
the old part supplies the loss
\[
 \frac\mu2(.45-A)^2\ge\frac\mu2(.059)^2>10^{-9}.              \tag{9}
\]
The rest of that segment is concave by (8). Both first derivatives
vanish at the reference, by (1). Hence the entire old-width main
rectangle on the right is below \(\Re\mathscr P(c)-10^{-9}\).

For the additional strip \(s(x)\le u\le1/8\), set
\(r=e^{2\pi h_p}\in(1/2,1)\). In the real part of \(Q_t\), absorb
the incoming chirp into the first factor:
\[
 e^{\Re Q_t}=
 \frac{|e^{-2\pi h_a}-r e^{-2\pi i(x+u)}|
       |1-e^{2\pi\Im q_*}r e^{-2\pi i(\Re q_*+u)}|}
      {|1-r e^{-2\pi iu}|^3}.                              \tag{10}
\]
Here \(e^{-2\pi h_a}>7/8\),
\(x+u\in[23/40,5/8]\), and
\(\Re q_*+u\in[.315,.485]\). Both numerator factors exceed one.
Since \(\cos(2\pi u)\ge\sqrt2/2>7/10\), convexity in
\(r\in[1/2,1]\) gives
\(|1-r e^{-2\pi iu}|^2\le3/5\).
Consequently \(\Re Q_t>\log(5/3)>0\). Increasing \(u\) to
\(1/8\) pays all the additional main points by (9).

For the real cut \(t=s(x)\), its coupled derivative is exactly
\[
 \frac d{dx}\{B_U(x)+\Re Q(s(x);x+ih_a,q_*)\}
 =B_U'(x)+3\log(2\sin\pi s(x))
 -\log|e^{-2\pi h_a}-e^{-2\pi ix}|
 -\log|1-e^{-2\pi i(q_*+s(x))}|.                           \tag{11}
\]
The actual first-cap private height is at most .037, so its marginal
formula gives
\[
 \Re T_0'(a_*)=
 \log\frac{|1-e^{-2\pi i(e_*+a_*)}|}{|1-e^{-2\pi ia_*}|}
 <\log(5/2)<1.                                             \tag{12}
\]
Indeed the denominator exceeds one, \(\Re a_*>1/4\), while
\(\Im(e_*+a_*)\le.058\) and \(e^{.116\pi}<3/2\).
Thus \(B_U'<1\). Further,
\(2\sin(\pi/8)<4/5\), the first modulus in (11) exceeds
\(9/5\), and the second exceeds one. Using
\(3\log(4/5)<-3/5\) and \(\log(9/5)>1/2\), (11) is
strictly less than \(-1/10\).
At \(x=.45\), the
[ordinary \(1/8\)-row certificate](research_mixed_four_left_cut_support.md),
after removing the nonzero fixed outgoing halfweight and adding (4),
gives a deficit \(1/2000\). It therefore pays the moving real cut
throughout the new interval.

Every lower physical row is included. For \(0<u\le s(x)\le1/8\),
formula (10) with \(r=1\) has first factor greater than \(7/8\),
second factor greater than \(9/10\), and denominator less than
\(3/5\). Thus its real derivative is positive. Its rate is continuous
at \(u=0\), where the exact row is one. The zero-safe physical-product
upper bound and monotonicity pay all these rows by the moving real cut.

## 3. The half row, the aliases and the revived upper rows

On the real half row,
\[
 \frac d{dx}\{B_U(x)+\Re Q(1/2;x+ih_a,q_*)\}
 =B_U'(x)+\log\frac{|1+R e^{-2\pi ix}|}{|1-R e^{-2\pi ix}|},
 \qquad R=e^{2\pi h_a}.                                    \tag{13}
\]
The original height bounds give \(3/5<R<8/7\), hence
\(R+R^{-1}\le34/15\). Since \(-\cos2\pi x\ge19/20\), the
squared ratio is at most \(11/125\). Combining with (12), the
right-hand side of (13) is less than
\(\tfrac12\log(11/20)<0\).
The [ordinary half-row certificate](research_mixed_half_row_support_completion.md)
at \(x=.45,z=q_*\) therefore transports its \(1/2000\) deficit
through the full right interval.

Retain the original tall horizontal aliases at heights \(-1/5\)
and \(5/4\). For every \(u\in[s(x),.5]\) and every real index
height, the original argument strip for \(g'\) yields
\[
             -\frac{17\pi}{10}<\Im Q_t<\frac{137\pi}{100}.
                                                                    \tag{14}
\]
For clarity, \(\Arg(1-e^{-2\pi iv})\) lies between zero and
\(\pi(1-2\Re v)\) when \(0<\Re v<1\), with their order reversed
on the right half. The lower bound in (14) follows from
\[
 -2+4u+\min(0,1-2\Re q_*-2u)\ge-17/10;
\]
the upper bound follows from
\(2x+\max(0,1-2\Re q_*-2u)\le137/100\).
Consequently the lower and upper weighted horizontal profiles,
relative to the main at height \(h_p\), gain at least
\[
       \frac{63\pi}{500},\qquad \frac{126\pi}{625},          \tag{15}
\]
respectively. These are the estimates
\(2\pi/5-(137\pi/100)(1/5)\) and
\(2\pi(5/4)-(17\pi/10)(5/4+.102)\).

The same bounds make the weighted vertical alias profiles strictly
increase toward height zero below the real axis, and strictly decrease
above it. The unweighted joins from height zero to \(h_p\) are convex
in index height at both real cuts. At \(u=s(x)\le1/8\),
\(C(a+t)<0\) and the bounds used in (8) give
\(3C(t)>C(q_*+t)\) throughout \(h_p\le\Im t\le0\).
At \(u=1/2\), \(C(t)=0\) and both shifted cotangents are nonpositive.
At the corner \(x=u=1/2\), the original left-limit lift gives
\(\Re g(1+i\eta)=\pi\max(\eta,0)\). Thus the height derivative
has a nonnegative jump when \(a+t\) crosses its real numerator zero;
convexity persists there as well.
Thus each such join is bounded by its paid real and main endpoints.
No vertical current or join is deleted.

The [upper-row endpoint comparison](research_mixed_transformed_upper_rows.md),
whose endpoint-reduction lemma is independent of its later old-private
calibration, applies on the whole square \([.22,.5]^2\).
It reduces every revived physical \(u\ge1/2\) to the half or last
rate. The former was just paid. For the latter use the full-cap disk
bound and the independent
[following-domain last-row bound](research_mixed_four_upper_rows_following_domains.md):
their sum is less than \(5/3\). The
[two following-remainder gaps](research_mixed_three_four_following_remainder_gaps.md)
give \(\Re\mathscr P(c)>7/4\), so the last branch has a gap
greater than \(1/12\). The cap plane and the disk bound are used on
their respective branches, not interchanged.

## 4. Literal finite contours and scope

The exact index interpolant is
\[
 \mathcal T_N(t;a,z)=e^{2\pi iNat}
 \frac{\Pi_N(a+t)\Pi_N(z+t)}
      {\Pi_N(a)\Pi_N(t)^3\Pi_N(z)},                         \tag{16}
\]
which equals \(X^{-j}p_j(X)p_j(Y)/P_j^3\) at \(t=j/N\).
Take
\[
 L_N(x)=\lceil Ns(x)\rceil,\quad M_N=\lceil N/2\rceil,
 \quad \sigma_-=(L_N-1/2)/N,\quad \sigma_+=(M_N-1/2)/N.      \tag{17}
\]
The physical pieces are \(0\le j<L_N\), \(L_N\le j<M_N\),
and \(M_N\le j<N\). Apply the original finite fixed-contour
identity only to the middle piece, retaining its main, both tall
horizontal aliases, both vertical aliases and both zero-mode joins.
All denominator arguments remain in their original regular strips.
The numerator \(a+t\) can meet real part one at the upper corner;
use the original zero-safe upper continuation there, as in the
[exact right-strip source audit](research_mixed_transformed_right_strip.md).
This is not a zero-free asymptotic across a numerator zero.
The half-grid displacement is \(O(1/N)\); compact continuity of
the upper rates, including their logarithmic endpoints, absorbs it
into one arbitrarily small rate tolerance. The finite contour stays
at the two specified heights; its uniform factorial estimates are
on a fixed compact set. No infinite-height limit is needed.
In particular there is no new support assumption or physical
truncation of revived rows.

Equations (9), (11), (13)--(15) and the last-row comparison pay every
one of these original groups. Choose the total source tolerance
smaller than a fixed fraction of the smallest displayed gap. This
proves (5). The all-real ordinary cap bounds and Markov are applied
before the finite summations, as in the plateau theorem.

For (6), fix \(c_0\) and its contours (17). Every displayed source
profile and zero-safe finite-product upper rate has a compact
parameter neighborhood with a smaller gap. The whole cap's
integer-weighted polynomial extension supplies its required complex
neighborhood, as in the plateau theorem. The exact normalized
sources, the reference action and \(q(c)\) are holomorphic there.
Compactness of \(K\) gives a finite cover and uniform constants;
Cauchy gives the fixed normalized derivatives. No division by
\(C_{1,N}\) or by \(U_{0,N}\) occurs.

The endpoint of (6) is \(1/2+i\Im a(c_0)\), whereas the certified
complementary source begins at \(1/2+ih_{\rm pair}\). A connector
between those points is not included in this theorem. Convexity in
incoming height of individual regular profiles can be useful for
that connector only after the same individual profiles have been
bounded at both endpoint heights. A whole-source bound for the
fixed complementary path does not supply that missing premise.
