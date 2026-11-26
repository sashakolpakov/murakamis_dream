# The physical terminal complement on the added ordinary three/four interval

Research deduction, 7 November 2026. This note extends the original
physical-complement reductions to the incoming interval \([9/20,1/2]\)
at its actual attached height. It proves a coupled gap for both true
transform ends. Every remaining lower-half transform row reduces to
the same real faces and alias anchors already under consideration.
No new face, partial Newton estimate, or numerical evaluation is used.

The strict gaps for the four real families charged in the saved-face
protocol are not assumed here. The result identifies precisely how
those comparisons control the physical complement.

## 1. Original source and calibrated first factor

Use the actual ordinary pair and notation of
[the right extension](research_mixed_three_four_private_left_right_extension.md),
equations (1)--(6):
\[
\begin{gathered}
 a_*=A+ic,\quad .278<A<.391,\quad -.072<c<.021,\qquad
 a=x+ic,\quad b=9/20\le x\le1/2,\\
 M=\Re\{T_0(a_*)+P_1(a_*)\},\quad
 p=\Re P_1'(a_*),\quad \kappa_*=\frac1{2500000},\\
 B_U(x)=\Re T_0(a_*)-p(x-A)-\kappa_*(x-A)^2 .
\end{gathered}
\tag{1}
\]
The complete original \(U_{0,N}\), including its ordinary-color
derivatives, has upper rate \(B_U(x)\). The shared critical equation
is \(T_0'+P_1'=0\). There is no retained \(d_N\) in this pair.

The exact square source is
\[
 V_{1,N}(w,X)=
 \sum_{i,j=0}^{N-1}\frac{X^{-i}p_i(X)}{P_i^2}\,
       \frac{p_j(r^i)\mathcal H_N(w,r^{-j})}{P_j^2},
 \qquad X=e^{-2\pi ia}.
\tag{2}
\]
Here \(\mathcal H_N\) is the entire original endpoint polynomial.
The identity \(P_jp_i(r^j)=P_ip_j(r^i)\) makes (2) identical to
the triangular source; its products vanish when \(i+j\ge N\).
No partial Newton sum replaces \(\mathcal H_N\).

The reduced phase is
\[
 \Phi(a;t,e)=S(e)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
             -\frac{\pi i}{2}(e-e^2)+2\pi iat .
\tag{3}
\]
All actions and lifts are original. Write
\[
 E_c=[.27,.49]+i[-.055,.04],\qquad
 T_c=[.15,.5]+i[-.12,.12].
\tag{4}
\]
The [new joint curvature theorem](research_mixed_three_four_right_strip_joint_curvature.md),
Proposition 2, makes \(\Re\Phi\) horizontally concave on
\(x\in[b,.5]\), \(t\in T_c\), \(e\in E_c\). In particular its
real part is convex in each index height when the other coordinates
are fixed. The continuous numerator corner \(a+t=1\) is included.

## 2. Both true transform ends retain an absolute coupled gap

**Lemma 1.** There is a fixed \(\delta>0\) such that the sum of
the absolute outer coefficients times the complete coherent cap
values, restricted to \(i/N\le\delta\) or \(i/N\ge1-\delta\),
has upper rate \(217/250\), uniformly on (1). Each tail multiplied
by the whole first cap consequently satisfies
\[
 |U_{0,N}(w_L,X)|\,
 \sum_{i/N\ {\rm in\ the\ stated\ tail}}
  \left|\frac{X^{-i}p_i(X)}{P_i^2}\right|
              |\mathcal U_{1,N}(w_R,r^i)|
 \le C N^B e^{N(M-1/10)} .
\tag{5}
\]
The assertion includes both parities and fixed ordinary-color
derivatives on smaller fixed disks.

*Proof.* Repeat the original
[terminal-transform tail proof](research_mixed_terminal_transform_tails.md),
Lemma 2, on the enlarged compact incoming rectangle. Its external
upper rate is
\[
 \chi_1(t,a)=
 \int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds-2J(t)-2\pi ct .
\tag{6}
\]
This is continuous in \((t,a)\), including its integrated
real-height zeros, and
\[
 \chi_1(0,a)=0,\qquad
 \chi_1(1,a)=2\pi(-c)_+\le .24\pi<132/175 .
\tag{7}
\]
The uniform zero-safe finite product estimate used there does not
restrict the incoming real part to \(x\le.45\). It applies on this
enlarged compact annulus with the same arbitrary rate tolerance.

For \(t\le\delta\le.001\), the entire coherent cap has upper rate
\(433/500+\Delta_\delta+\epsilon\), where
\(\Delta_\delta=\delta\log2-J(\delta)\to0\).
For \(t\ge1-\delta\), the exact support restricts its private
indices to \(j\le N-1-i\); the original whole-endpoint rate
\[
 \max_{0\le e\le1-t}
     \{\lambda(e)+J(e+t)-J(t)-J(e)\}
\]
tends uniformly to zero at \(t=1\). These facts are independent
of the incoming coordinate. Uniform continuity in (6) and the same
tolerance allocation therefore give \(217/250\), exactly as in the
cited proof. The complete private and Newton sums remain inside
each coherent \(\mathcal U_{1,N}(r^i)\).

For calibration, the original terminal theorem gives
\(\Re P_1(a_*)>107/100\), and the right-extension proof gives
\(p>-7/20\). Since \(0<x-A<111/500\),
\[
 \Re P_1(a_*)+p(x-A)
 >\frac{107}{100}-\frac7{20}\frac{111}{500}
 =\frac{9923}{10000}.
\tag{8}
\]
Thus \(M-B_U(x)-217/250>1243/10000>1/10\).
Spend the remaining fixed room on the first-cap upper tolerance
and ordinary-color neighborhoods. Polynomial row counts and
Cauchy estimates give (5). No incoming halfweight is divided out.
\(\square\)

## 3. The remaining small transform indices increase to their old cut

**Lemma 2.** For real \(0<t\le.15\), \(a\) as in (1), and
every \(e\in E_c\),
\[
                 \partial_t\Re\Phi(a;t,e)>\log(3/2).
\tag{9}
\]

*Proof.* The exact chirp-aware derivative is
\[
 e^{\partial_t\Re\Phi}=
 \frac{|e^{-2\pi c}-e^{-2\pi i(x+t)}|\,
       |1-e^{-2\pi i(e+t)}|}{(2\sin\pi t)^3}.
\tag{10}
\]
Put \(R=e^{-2\pi c}\). The bound \(c<.021\), together with
\(e^{-u}\ge1-u\) and \(\pi<22/7\), gives \(R>4/5\).
Also \(x+t\in(.45,.65]\), so its cosine is less than \(-1/2\).
Consequently
\[
 |R-e^{-2\pi i(x+t)}|^2>R^2+R+1>\frac{61}{25}>\frac94.
\]
The real part of \(e+t\) belongs to \([.27,.64]\), where its
cosine is negative; hence the second modulus in (10) is greater
than one, for every private height in (4).
Finally \(2\sin\pi t<1\), because \(t\le.15<1/6\).
This proves (9). \(\square\)

Remove \(i/N\le\delta\) first as the complete coherent rows
of Lemma 1. For each remaining physical \(t=i/N\in(\delta,.15)\),
apply exactly the private-index residue decomposition of
[the original small-transform theorem](research_mixed_terminal_four_left_strip.md),
Section 2. It retains the private shifted main, both joins,
both horizontal aliases and all vertical alias sides.
Equation (9) transports every point to \(t=.15\); the private
sampling penalty is unchanged. Only then use the height convexity
from (4) on that real transform face. Its required endpoint
comparisons are exactly the flattened \(t=.15\) face, its two
real corners, and its two private-alias families. No new anchor
is introduced.

For completeness, the same transport holds on the physical
private complement before its Newton sum is split. Its whole
endpoint upper rate is
\[
 \mathcal R(a;t,e)=Q_a(t)-2J(t)+\lambda(e)-J(e)+I_t(e),
\quad
 \begin{cases}
 Q_a(t)=\displaystyle\int_0^t
   \log|e^{-2\pi c}-e^{-2\pi i(x+s)}|\,ds,\\
 I_t(e)=\displaystyle\int_0^e\log|1-e^{-2\pi i(t+s)}|\,ds .
 \end{cases}
\tag{11}
\]
If \(0\le e\le.27\), then \(t\le t+e<.5\), and
\[
 e^{\mathcal R_t}=
 \frac{|e^{-2\pi c}-e^{-2\pi i(x+t)}|\,
               (2\sin\pi(t+e))}{(2\sin\pi t)^3}
 >\frac{3}{2}.
\tag{12}
\]
After transporting \(t\) to \(.15\), the original lower private
estimate transports \(e\) to \(.27\), with gain
\(13(.27-e)/100\). For \(e\ge.49\), the derivative of
\(\lambda(e)-J(e)+I_t(e)\) in \(e\) is below \(-1/2\):
the original bounds are \(\lambda'-J'<-6/5\) below \(.5\),
\(\lambda'-J'\le-\log4\) above it, and the additional
logarithm is at most \(\log2<7/10\).
Transport first to \(e=.49\), then apply (9).
Thus
\[
\begin{array}{ll}
 \mathcal R(a;t,e)\le\Re\Phi(a;.15,.27)
 -\log(3/2)(.15-t)-\frac{13}{100}(.27-e),
                                      &0\le e\le.27,\\[2mm]
 \mathcal R(a;t,e)\le\Re\Phi(a;.15,.49)
 -\log(3/2)(.15-t)-\frac12(e-.49),
                                      &.49\le e\le1 .
\end{array}
\tag{13}
\]
The order of \(\Phi\)'s arguments is \((a;t,e)\) throughout.
The inequalities extend through logarithmic zeros by integration;
the actual physical terms past \(i+j=N\) remain zero.

## 4. The central transform interval and both private physical tails

Keep each physical private \(j\) and its complete
\(\mathcal H_N(w,r^{-j})\), interpolating only \(t\):
\[
 \mathcal B_{j,N}(a,t,w)=
 e^{2\pi iNat}\Pi_N(a+t)E_N(a)E_N(t)^2
                  \frac{p_j(e^{-2\pi it})\mathcal H_N(w,r^{-j})}{P_j^2}.
\tag{14}
\]
It agrees exactly with (2) at every physical transform index.
The polynomial \(p_j\) is not replaced by a factorial ratio
across its support wall.

The [original private-tail theorem](research_mixed_terminal_four_private_tails.md)
gives the upper rate
\[
 \Re G_a(t)+R(e,t),\qquad
 G_a(t)=g(a+t)-g(a)-2g(t)+2\pi iat,\quad
 R(e,t)=\lambda(e)-J(e)+I_t(e).
\tag{15}
\]
Its complete uniform estimates and the following two inequalities
are independent of \(a\):
\[
 \begin{array}{ll}
 R(e,t)\le R(.27,t)-\frac{13}{100}(.27-e),&0\le e\le.27,\\
 R(e,t)\le R(.49,t)-\frac1{30}(e-.49),&.49\le e\le1.
 \end{array}
\tag{16}
\]
At a real cut \(e_0=.27,.49\), the exact original-rate equality is
\[
             \Re G_a(t)+R(e_0,t)=\Re\Phi(a;t,e_0).
\tag{17}
\]
These statements therefore apply on the added incoming interval.

The only new finite chart issue is the numerator \(a+t=1\)
at \(x=t_R=.5\). The numerator continuation and quarter-level
shift in Section 5 of the right-extension note give its
zero-safe upper packet, including a fixed neighborhood and the
\(O(N^{-1})\) half-grid shifts. All denominators in (14) remain
regular. No new reciprocal or logarithmic branch is introduced.

Apply the original one-index transform residue identity to (14),
with constant-mode coefficient \(+N\), main height \(h\), and
alias heights \(\pm.12\). First use (16)--(17) at every point.
On both transform cuts, height convexity from (4) bounds all joins
and alias half-sides by their existing endpoints.
Thus these two whole physical-private sectors require precisely
the two private main faces, four real corners and transform-alias
faces already listed in the reduced-current criterion.

The entire finite passage preserves arbitrary small rate
tolerances, ordinary-color Cauchy estimates, both parities,
and the original polynomial factors. Half-grid discrepancies are
handled after transport to the regular anchors; the possible
incoming numerator corner uses the preceding zero-safe bound.

## 5. Exact source consequence and remaining comparison

Let \(\mathscr A(x)\) be the maximum of the original eight
flattened real-face rates and twelve penalized alias-anchor rates
on the added incoming interval. Keep all actual reference heights
and original alias penalties. If
\[
                     B_U(x)+\mathscr A(x)\le M-\gamma
                     \qquad(b\le x\le1/2)
\tag{18}
\]
for some uniform \(\gamma>0\), then all lower-half transform
physical rows outside the central two-index rectangle, multiplied
by the complete first cap, satisfy
\[
              C N^B e^{N(M-\gamma')},
              \qquad 0<\gamma'<\min\{\gamma,1/10\}.
\tag{19}
\]
This is the literal finite-source consequence of Lemmas 1--2 and
(14)--(17), with every private/Newton index retained.

For the central rectangle itself, the new joint-curvature theorem
already pays its main component. Its other retained currents use
the same endpoints in (18), with height convexity supplying every
join. The right-extension note already establishes the needed
gaps for four real families and all twelve aliases; its remaining
four real families have the precise charges recorded in Section 8
and in the frozen saved-face protocol. No outcome of that
comparison is inferred here.

The upper transform triangle \(i/N\ge1/2\) is a distinct sector.
Its entropy reduction and coupled \(Q\)-transport are treated in
[the upper-transform half-face note](research_mixed_three_four_upper_transform_half_face.md).
This note does not replace its complete physical majorant by a
coherent terminal bound. It also does not move the incoming height
or estimate the far half-circle. The original one-circle scalar
\(\kappa_N^3N^2\) stays unchanged.

