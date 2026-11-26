# Joint coercivity for the original three- and four-crossing phases

Research proof, 4 November 2026. Frozen manuscripts and previous
source artifacts are unchanged.

The two original unsummed phases have one common positive Hessian
form. It gives a length-independent bound after arbitrary wire
identifications, including the complex Schur complement that
eliminates the indices. This is a local assembly result. It does not
locate the critical point of an arbitrary mixed word, estimate its
complementary integration cycle, or identify a knot invariant.

## 1. Original phases and a common chamber

Use the exact phases of the
[three-crossing source](research_traced_three_vertex_endpoint.md) and
[full four-crossing source](research_power_four_finite_source.md).
Write
\[
 \begin{split}
 g(z)&=J(z)+\frac{i\pi}{2}(z-z^2),\qquad J'(z)=\Log(2\sin\pi z),\\
 X&=e^{2\pi ix},\quad Y=e^{2\pi iy},\quad
 I_X(s)=\frac{\operatorname{Li}_2(Xe^{-2\pi is})-
                   \operatorname{Li}_2(X)}{2\pi i},\\
 F_3(s,t;x,y)&=g(s+t)+2\pi i(sx+ty)-I_X(s)-I_Y(t),\\
 F_4(s,t;x,y)&=F_3(s,t;x,y)-g(s)-g(t),\\
 \mathcal F_n&=F_n-\pi i(x+y),\qquad n=3,4.
 \end{split}
 \tag{1}
\]
The logarithms are continued from the original sine strips and disk
product interpolants. In particular the affine cardinal term is
retained, although it does not enter the Hessian.

Take the closed convex complex rectangles
\[
 \begin{split}
 \mathcal W&=[17/100,1/5]+i[7/100,9/100],\\
 \mathcal B&=[1/4,9/20]+i[-11/200,3/200].
 \end{split}
 \tag{2}
\]
Throughout \((s,t;x,y)\in\mathcal B^2\times\mathcal W^2\),
\[
 \begin{gathered}
 1/2\le\Re(s+t)\le9/10,\quad
 1/20\le\Re(s-x),\Re(t-y)\le7/25,\\
 11/200\le\Im(x-s),\Im(y-t)\le29/200,\qquad
 |Xe^{-2\pi is}|,|Ye^{-2\pi it}|<3/4.
 \end{gathered}
 \tag{3}
\]
All three sine arguments needed by (1) remain in \(0<\Re z<1\),
and all disk-product endpoints are strictly inside the unit disk.
The exact finite interpolants and their full original lattice values
are regular on a neighborhood of this chamber, at both parities.
No interpolation or boundary normal is replaced by a value-only
representative.

## 2. The exact positive form

Put \(U=e^{-2\pi is}\), \(V=e^{-2\pi it}\), and set
\[
 \begin{split}
 a&=2\pi\Im\frac{UV}{1-UV},&
 d_x&=-2\pi\Im\frac{XU}{1-XU},&
 c_x&=2\pi\Im\frac X{1-X},\\
 d_y&=-2\pi\Im\frac{YV}{1-YV},&
 c_y&=2\pi\Im\frac Y{1-Y},&
 e_s&=\pi\Re\cot(\pi s),\quad e_t=\pi\Re\cot(\pi t).
 \end{split}
 \tag{4}
\]
The exact differentiation in the
[three-vertex joint Hessian](research_three_vertex_joint_concavity.md#1-the-original-unsummed-hessian)
gives, for real horizontal variations,
\[
 \begin{split}
 -\Re d^2\mathcal F_3={}&a(ds+dt)^2+d_x(ds-dx)^2+d_y(dt-dy)^2
                         +c_xdx^2+c_ydy^2,\\
 -\Re d^2\mathcal F_4={}&-\Re d^2\mathcal F_3+e_sds^2+e_tdt^2.
 \end{split}
 \tag{5}
\]
The second equality follows from \(g''(s)=\pi\cot\pi s-i\pi\).
It is an identity for the actual unsummed phases, not for absolute
values of their index sums.

**Theorem 1.** On the entire chamber (2),
\[
 -\Re\mathcal F_3''\succ I_4,\qquad
 -\Re\mathcal F_4''\succ I_4+\tfrac25\operatorname{diag}(1,1,0,0),
 \tag{6}
\]
with coordinate order \((s,t,x,y)\).

*Proof.* The phase sectors in (3) give \(a\ge0\); the equality
case at \(\Re(s+t)=1/2\) has \(UV<0\), so it is regular.
Each positive coefficient \(c,d,e\) has the form
\[
 Q(A,\theta)=\frac{\pi\sin\theta}{\cosh A-\cos\theta},
       \qquad A\ge0,\quad0<\theta<\pi.
 \tag{7}
\]
This decreases in \(A\). At fixed \(A\), its derivative in
\(\theta\) has the sign of \(\cosh A\cos\theta-1\), hence
it has no interior minimum. Thus endpoint inequalities suffice:
\[
 \begin{array}{c|c|c|c}
 & A\le&\theta\text{ interval}&\text{uniform lower bound}\\ \hline
 c_x,c_y&9\pi/50&[17\pi/50,2\pi/5]&10/3\\
 d_x,d_y&29\pi/100&[\pi/10,14\pi/25]&9/5\\
 e_s,e_t&11\pi/100&[\pi/2,9\pi/10]&2/5.
 \end{array}
 \tag{8}
\]
The six strict endpoint comparisons are recorded outward by the
focused checker. They are inequalities at explicit rational
multiples of \(\pi\), not a sample of the chamber.

Discard \(a\ge0\). Each \((s,x)\) or \((t,y)\) pair in (5)
strictly dominates the quadratic form with matrix
\[
 P=\begin{pmatrix}9/5&-9/5\\-9/5&9/5+10/3\end{pmatrix},
 \qquad (P-I)_{11}=4/5,\quad\det(P-I)=1/15>0.
 \tag{9}
\]
This proves both assertions of (6). \(\square\)

## 3. Shared wires and complex index elimination

Consider any fixed word \(n_1,\ldots,n_m\in\{3,4\}\), with
independent index pairs \((s_j,t_j)\) and wires \(x_0,\ldots,x_m\):
\[
 \mathcal G=\sum_{j=1}^m
       \mathcal F_{n_j}(s_j,t_j;x_{j-1},x_j).
 \tag{10}
\]
The same statement applies to cyclic wire identifications or to any
identification of these boundary variables. Let \(d_v\) be the number of boundary
incidences of a distinct free wire \(x_v\); a repeated boundary variable counts
again. Fixing some wires simply restricts the quadratic form.

**Corollary 2.** If every coordinate belongs to (2), then
\[
 -\Re d^2\mathcal G\succ
 \sum_j(ds_j^2+dt_j^2)+\sum_vd_vdx_v^2
            +\frac25\sum_{j:n_j=4}(ds_j^2+dt_j^2).
 \tag{11}
\]
In particular the coercivity constant does not deteriorate with the
word length. Every unpinned variable is covered. This statement is
obtained by pulling back and adding (6); it does not assert that an
arbitrary boundary-variable identification is an original knot realization.

The index elimination retains this bound in a useful precise sense.
Let a holomorphic index-critical branch be contained in the chamber,
and let \(\Phi\) be the resulting critical value as a function of
the remaining wires. Write \(K=-\mathcal G''\), partitioned into
indices \(i\) and wires \(w\). Then
\[
 -\Phi''=K_{ww}-K_{wi}K_{ii}^{-1}K_{iw},\qquad
 -\Re\Phi''\succ\operatorname{diag}(d_v).
 \tag{12}
\]
This is a complex Schur complement, not the Schur complement of the
real part. To prove the assertion, first note that the complex
symmetric \(K\) has Hermitian part equal to its entrywise real part.
It is strictly accretive by (11), so \(K_{ii}\) is invertible.
For any complex wire vector \(q\), put
\(p=-K_{ii}^{-1}K_{iw}q\). Then
\[
 \Re\{q^*(K_{ww}-K_{wi}K_{ii}^{-1}K_{iw})q\}
 =\Re\{(p,q)^*K(p,q)\}
 >\|p\|^2+\sum_vd_v|q_v|^2.
 \tag{13}
\]
This proves (12), including for real horizontal wire directions.
It also proves nondegeneracy and a nonzero local Gaussian determinant
whenever the original phase has a critical point in the chamber.

For fixed boundary wires, the full gradient has at most one zero in
the convex product chamber: integrate its Hessian on the straight
complex segment joining two proposed zeros, and pair with the
conjugate transpose of their difference. Inequality (11) rules out
a zero difference of gradients. On a horizontal plane through an
existing critical point it gives the ordinary quadratic maximum
bound, and hence a strict gap on any compact real face separated
from that point. Existence and the relation of those faces to the
original finite integration cycle are separate requirements.

## 4. Both actual reference branches lie strictly inside

Use the proved original alternating reference and its exact root
\(a\) from
[the three/four interface](research_three_four_source_interface.md#2-a-positive-alternating-reference-with-exact-periods):
\[
 p(a)=4a^4-6a^3+4a^2-2a+1=0,\qquad
 K=\frac1{1+2a-4a^2},\qquad x_0=\frac{\Log K}{2\pi i}.
 \tag{14}
\]
The rational expression for \(K\) is exactly the geometric wire
exponential. Indeed with
\(B=a^2(2a-1)^2/[2(a-1)]\) and \(k=a^2B/(a^2+B)\),
one has \(K+K^{-1}=2-4k\) identically. The inherited positive
branch has \(\Im K>0\), \(|K|<1\), selecting it rather than
its reciprocal.

The two diagonal index branches are
\[
 U_3=1-2a,\quad U_4=\frac{1-K}{2K},\qquad
 s_n=t_n=-\frac{\Log U_n}{2\pi i}.
 \tag{15}
\]
Both logarithms have imaginary part in \((-\pi,-\pi/2)\).
The exact stationary exponent identities are
\[
 U_3(1-U_3)=K^{-1}-1,\qquad
 K(1-U_4^2)=(1-U_4)(1-KU_4).
 \tag{16}
\]
Direct interval enclosures of the original sine-log gradients put
their imaginary parts in \((-\pi,\pi)\). Consequently their
actual lifts vanish. The same outward root enclosure gives
\[
 \begin{array}{c|c|c}
 &\Re&\Im\\ \hline
 x_0&(.18299,.18301)&(.07871,.07873)\\
 s_3=t_3&(.3535,.3537)&(-.0169,-.0167)\\
 s_4=t_4&(.2845,.2846)&(-.0425,-.0423).
 \end{array}
 \tag{17}
\]
Thus each index-critical branch exists on a neighborhood of the
same wire pair \((x_0,x_0)\) and lies strictly in (2).

There is also an exact unsummed stationarity assertion for alternating
words. The wire derivative of either critical phase at the reference
is
\[
 q_n=2\pi i s_n+\Log(1-KU_n)-\Log(1-K)-\pi i.
 \tag{18}
\]
Algebraically,
\((1-KU_3)(1-KU_4)-U_3U_4(1-K)^2\) vanishes modulo \(p(a)\).
Hence \(e^{q_3+q_4}=1\). The direct logarithmic strip enclosure
\(|\Im(q_3+q_4)|<\pi\) fixes \(q_3+q_4=0\).
Therefore every alternating even cyclic word is stationary at
constant wire \(x_0\), with each vertex using its own indices (15).
The same holds at every free wire of an alternating open word whose
boundary wires are fixed at \(x_0\). Corollary 2 gives its uniform
nondegeneracy and unique horizontal maximum in the chamber.

For a nonalternating word the wire gradients need not cancel at this
constant configuration. The coercivity theorem still applies wherever
its coordinates lie in (2), but it supplies neither its critical
location nor a nonzero coefficient of the full original source.
No absolute angular-action calibration is used in this note; in
particular the older homogeneous-three calibration box is not
silently extended to the new reference.

## 5. Reproduction and scope

Run `python3 experiments/check_mixed_three_four_joint_coercivity.py`.
The focused checker verifies the exact phase/Hessian algebra, rational
matrix minors, endpoint comparisons, inherited reference provenance,
and both original logarithmic lifts. It records the selected
coordinates and the unsummed wire-gradient cancellation.

The literal finite phases, cardinal factors and parity conventions
come from the original sources. The theorem preserves them rather
than changing to a positive operator metric. A whole-source theorem
for a mixed word still needs its actual boundary preparation,
critical-point location, all index and wire side/alias estimates,
and comparison with the complementary finite sum. The present
positive form is the common local estimate for that later assembly.
