# An actual return-sector majorant need not have an increasing open profile

Private derivation, 1 November 2026. No repository changes.

This report concerns the absolute coefficient majorant of a fixed-polynomial Conway computation. The cubic return tensor is the exact tensor of the moving Casimir quotient. The inputs are the original positive complete pure-leaf polynomials. The conclusion is an obstruction to an induction invariant proposed for this majorant, not a lower bound for the signed deformed tangle, a knot example, or a statement about a classical main-meridian factor.

The exact quotient and return identities are in [the contracted return calculation](/private/tmp/md-fixed-newton-return-gates-and-contracted-tensor.md). The original positive coefficients and their complete actions are in `notes/actual_pure_conway_auxiliary_color_leaf.md`, `notes/actual_positive_newton_multiplication.md`, and `notes/actual_conway_isolated_three_leaf_long_twist_volume.md`.

## 1. Fixed-frame coefficients, including the return factor

Set
\[
N\ge2,\quad d=N-1,\quad M=\lfloor d/2\rfloor,
\quad S_n=\prod_{r=1}^n2\sin(\pi r/N),\quad S_0=1.
\]
The complete Newton basis is
\[
e_n(\omega)=S_n^{-2}\prod_{j=0}^{n-1}(c_j-\omega),
\qquad c_j=2\cos((2j+1)\pi/N).
\]
Keep this polynomial basis fixed while changing the relation to
\[
P_s=P_0+\Delta_s,\qquad
P_0=\mathsf T_N+2,\qquad
\Delta_s=2\cos(2\pi s)-2.
\tag{1}
\]
The degree-\(<N\) coefficient functional remains
\(\phi_s(F)=(-1)^dN^2[\omega^d]F\), and
\(\phi_s(e_i e_j)=\delta_{i+j,d}\). Thus the coefficient of \(e_r\) in a product is computed by the cubic tensor with third index \(d-r\).

Write \(\mu_0(i,j;r)\) for the original positive multiplication coefficient. It is supported on
\[
i+j<N,\qquad \max(i,j)\le r\le i+j.
\]
The exact additional coefficient in the moving quotient is
\[
\mu_{\mathrm{ret},s}(i,j;r)
=-\Delta_s(-1)^{i+j-r}\Lambda_{ijr},
\tag{2}
\]
where, with \(h=i+j-N\),
\[
\Lambda_{ijr}
=\frac{S_hS_r}
 {S_iS_jS_{h-r}S_{N-i+r}S_{N-j+r}}>0,
\qquad 0\le r\le h.
\tag{3}
\]
All factorial indices in (3) lie between zero and \(d\) on this support. In particular \(i,j\ge r+1\). The old and return supports are disjoint. The return factor in these fixed coordinates is \(\Delta_s\), which vanishes at integer \(s\); it is different from the \(\sin(2\pi s)\) factor in a moving-Newton-coordinate formula.

For a fixed \(s\notin\mathbb Z\), the scalar \(|\Delta_s|\) has zero exponential rate. The estimates below can also be read as statements about the tensor after division by this scalar. No lower estimate is asserted uniformly through its zeros.

## 2. The literal pure-leaf and two-leaf inputs

Use the original complete pure leaf
\[
h_N=\sum_{j=0}^{M}a_{N,j}e_j,
\qquad a_{N,j}=\frac{N^2S_{2j}}{S_j^4}>0.
\tag{4}
\]
There is no half-twist in (4). Let
\[
A_{2,N}=h_Nh_N=\sum_{i=0}^{d}A_{N,i}e_i,
\qquad
A_{N,i}=\sum_{u,v\le M}
a_{N,u}a_{N,v}\mu_0(u,v;i)\ge0.
\tag{5}
\]
The first product is exactly unchanged by (1): every pair of leaf indices satisfies \(u+v\le2M<N\), so its polynomial degree is less than \(N\). Its coefficients have no return term. At even levels its top coefficient can vanish; this does not affect any of the interior indices used below.

The next multiplication is the open three-leaf computation
\[
A_{3,N}^{(s)}=A_{2,N}\mathbin{\cdot_s}h_N.
\]
It is not closed by \(\phi_s\); its output is the coefficient indexed by \(r\). The absolute majorant for its return coefficient is
\[
B_{N,r}(s)=|\Delta_s|
 \sum_{\substack{0\le i\le d,\ 0\le j\le M\\i+j\ge N+r}}
 A_{N,i}a_{N,j}\Lambda_{ijr}.
\tag{6}
\]
The signed coefficient uses \((-1)^{i+j-r}\) inside this sum. Formula (6) does not move those signs into a positive trace or discard the specified output index. It is precisely the triangle-inequality majorant of that sector.

These fixed complete input polynomials are sufficient to test an induction claim based only on their coefficient profiles. Uniform nonzero diagonal factors at the original leaves do not change the displayed exponential profiles. Identifying an entire varying-color tangle with a particular such modified circuit still requires its actual typed source; no such identification is silently used here.

## 3. The two old profiles

Let
\[
J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
g(a)=J(2a)-4J(a),\quad 0\le a\le1/2.
\tag{7}
\]
The pure leaf has the uniform closed coefficient rate \(g\). The old gate action is
\[
m(u,v,x)=J(u+v)+J(x)-J(u)-J(v)
-J(x-u)-J(x-v)-J(u+v-x).
\tag{8}
\]
Define the original two-leaf coefficient profile
\[
f_2(x)=\max\{g(u)+g(v)+m(u,v,x):
0\le u,v\le1/2,\ \max(u,v)\le x\le u+v\le1\}.
\tag{9}
\]
This is the profile of the positive coefficients (5). Its strict interior maximizers and derivatives follow from the actual two-leaf gate equations. If \(B=\cot(\pi x)\) and
\[
X=\frac{B+\sqrt{B^2+2}}2,
\qquad f_2'(x)=2\log(2X^2),
\tag{10}
\]
then \(X\) decreases strictly with \(x\). Consequently \(f_2\) is strictly concave, increases up to \(x=1/2\), and decreases strictly afterward. Its endpoints are \(f_2(0)=f_2(1)=0\). The leaf profile \(g\) is strictly concave and is uniquely maximized at \(1/4\).

Set
\[
F_3=\max_{0\le y\le1/2}\{f_2(1-y)+g(y)\}>0.
\tag{11}
\]
This is the old complete closing action of the isolated three-leaf source. Its known value is \(2v_8/\pi\), but no numerical value is needed. Strict concavity gives a unique maximizer \(y_0\in(1/4,1/2)\), with \(x_0=1-y_0>1/2\). For example, the derivative of the objective is positive at \(y=1/4\), because \(f_2'(3/4)<0\), and tends to \(-\infty\) at \(y=1/2\). The original explicit solution is \(y_0=\arctan(2)/\pi\).

## 4. The return profile and its endpoint

Write \(b=r/N\), \(x=i/N\), and \(y=j/N\). The closed limiting return domain is
\[
\mathcal R_b=\{0\le x\le1,\ 0\le y\le1/2,
\ x,y\ge b,\ x+y\ge1+b\}.
\tag{12}
\]
The return entropy is
\[
\mathscr R(x,y,1-b)
=J(a)+J(c)+J(b)+J(a+c+b)
-J(a+c)-J(a+b)-J(c+b),
\tag{13}
\]
where \(a=1-x\), \(c=1-y\). These complementary variables are nonnegative and their sum is at most one. The exact negative-volume identity is
\[
\mathscr R(x,y,1-b)
=-\pi^2\int_0^a\int_0^c\int_0^b
       \csc^2(\pi(u+v+w))\,dw\,dv\,du\le0.
\tag{14}
\]
Endpoint values are obtained by continuity. In particular the entropy is identically zero when \(b=0\).

The absolute return envelope is therefore
\[
E_{\mathrm{ret}}(b)
=\max_{(x,y)\in\mathcal R_b}
 \{f_2(x)+g(y)+\mathscr R(x,y,1-b)\}.
\tag{15}
\]
Uniform factorial estimates give this as an upper coefficient rate in (6). The positive coefficients in (4)--(5), and ordinary integer rounding in their strict fibers, give the matching lower rates at the interior test points used below. The equality face \(i+j=N+r\) is a genuine finite support face, not a deleted root zero.

At \(b=0\), every feasible pair has \(x\ge1-y\ge1/2\). Since \(f_2\) decreases strictly on \((1/2,1)\), replacing \(x\) by \(1-y\) cannot decrease the objective, and strictly increases it unless \(x+y=1\). Hence
\[
E_{\mathrm{ret}}(0)=F_3,
\tag{16}
\]
with the unique maximizing pair \((x_0,y_0)\).

This endpoint rate is present at finite level. Choose \(j/N\to y_0\) and \(i=N-j\), so \(i+j=N\). At output \(r=0\), (3) simplifies exactly to
\[
\Lambda_{ij0}=\frac1{S_i^2S_j^2}
=\frac1{N^2(2\sin(\pi i/N))^2}.
\tag{17}
\]
Thus this factor is polynomial at the selected interior point. The two-leaf coefficient at \(i\) and the leaf coefficient at \(j\) have total rate \(f_2(x_0)+g(y_0)=F_3\). One positive summand in (6) gives the lower rate, while (15) gives the upper rate. Therefore, for each fixed \(s\notin\mathbb Z\),
\[
\lim_{N\to\infty}\frac1N\log B_{N,0}(s)=F_3
\tag{18}
\]
at both parities. The known positive two-leaf fiber has a strict saddle at \(x_0\), so its integer approximation is unaffected by choosing \(i=N-j\).

For every \(b>0\) with nonempty \(\mathcal R_b\), the smaller compact set \(x+y\ge1+b\) excludes that unique maximizing pair. Equations (14)--(16) imply
\[
E_{\mathrm{ret}}(b)
\le\max_{\mathcal R_b}[f_2(x)+g(y)]<F_3.
\tag{19}
\]
On the other hand, for sufficiently small \(b>0\), choose \(x=x_0+b\), \(y=y_0\). This is feasible, with \(x+y=1+b\), and its action tends to \(F_3\). Consequently
\[
\lim_{b\downarrow0}E_{\mathrm{ret}}(b)=F_3.
\tag{20}
\]
Compatible finite indices use \(i+j=N+r\); the strictly interior two-leaf fiber and the closed factorial estimate again give the corresponding lower rate. Nothing here divides by \(\Delta_s\) at a zero or assigns a lower rate to a vanishing term.

## 5. The enlarged absolute profile is not nondecreasing

Let \(f_3(b)\) be the old all-positive coefficient profile for \(A_{2,N}\cdot_0h_N\) at output \(b\). Its domain is the old gate domain \(\max(x,y)\le b\le x+y\le1\), so continuity of the compact action gives
\[
f_3(b)\longrightarrow0\quad(b\downarrow0).
\tag{21}
\]
At output zero this is also immediate from the exact coefficient \(N^6\).

The triangle-inequality profile allowing both the old and return root sectors is
\[
\widehat f_3(b)=\max\{f_3(b),E_{\mathrm{ret}}(b)\}.
\tag{22}
\]
Equations (16), (19)--(21) show that
\[
\widehat f_3(0)=F_3,
\qquad
\widehat f_3(b)<F_3
\quad\text{for every sufficiently small }b>0.
\tag{23}
\]
Thus the increasing lower-half profile property of the old unturned completed source does not extend to this absolute return-permitting profile. The obstruction already uses the literal open three-leaf multiplication and all its fixed output constraints; it is not an arbitrary choice of boundary weights.

The sum in (6) is an absolute majorant. Its lower bound (18) cannot be transferred to the signed coefficient in (2). In particular this argument neither disproves a relative exponential bound for the actual deformed source nor compares a returned knot invariant with volume. It shows that proving such a bound requires an induction invariant that retains more cancellation or boundary information than (22).

## 6. The restricted high-forest replacement that remains valid

There is a separate useful classical replacement lemma. Its graph hypothesis is essential: use an actual trivalent covariant tree with a physical turn on every internal edge. With cubic tensors lowered by \(\phi\), these edges identify equal labels. An unturned internal product edge instead identifies complementary labels. Resolving a higher-valence multiplication hub introduces such edges, so the following argument does not apply across an arbitrary hub.

In the equal-edge tree, an old cubic vertex has at most one incidence with label strictly above \(1/2\); an interior return vertex has at least two. All-low external labels exclude high boundary edges. A connected high-edge component containing returns is therefore a tree with return vertices internally and old vertices at its leaves. Boundary ties are handled by passage to the closed support, rather than by an incorrect strict-degree count at a tied point.

Suppose this is the only return component, and every terminal old vertex together with the subtree outside the component is a genuine return-free unturned completed branch of type A with pure effective-L leaves. Write its old coefficient profile as \(f_A\). The previously proved product-profile inequality implies
\[
f_A'(a)\ge f_2'(a)\ge0\quad(0<a\le1/2).
\tag{24}
\]
Here the branch output is \(a=1-x\), where \(x\) is its incident high cubic label. This is a statement about a whole genuine branch, not an old cell with its other labels artificially fixed.

For a returned state satisfying these hypotheses, change every high edge in this component to \(1/2\). Keep its other, low boundary labels fixed. Reoptimize each terminal A branch at output \(1/2\); (24) shows that its action cannot decrease. Replace every return vertex by an old vertex. Its new labels are either \((1/2,1/2,u)\), with \(0\le u\le1/2\), or \((1/2,1/2,1/2)\). They satisfy all old support inequalities. Their old entropy is nonnegative, whereas the replaced return entropy is nonpositive.

The resulting state is a feasible old state with at least as much action. At least one of its old vertices lies on the old boundary, since two incident labels sum to one. The actual old complete action has a unique strict maximizer. Compactness of the original closed wire polytope therefore supplies a positive gap between its maximum and this boundary stratum. Under the stated branch hypotheses, the whole returned family has that strict gap.

This proof does not justify iteration across several high components whose terminal branches themselves contain returns. Equation (23) shows why replacing (24) by monotonicity of an absolute return-permitting profile cannot repair that step in general. Nor does (24) automatically cover an odd-leaf plateau majorant; that requires a separate source/profile statement. These are the precise remaining hypotheses of the clamping lemma.

## 7. A local tangent shortcut also fails

For clarity, the old cubic action is
\[
t(x,y,z)=J(x+y)+J(y+z)+J(z+x)
-J(x)-J(y)-J(z)-J(x+y+z-1).
\]
At the strict symmetric point \(x=y=z=1/2-\varepsilon\), its value tends to zero and each partial derivative equals
\[
\lambda_\varepsilon
=\log\frac{\sin^2(2\pi\varepsilon)}
                 {\cos(\pi\varepsilon)\cos(3\pi\varepsilon)}
\longrightarrow-\infty.
\tag{25}
\]
The old supporting plane evaluated at the return corner \((1,1,1)\) is
\(t+3(1/2+\varepsilon)\lambda_\varepsilon\), which tends to \(-\infty\). The return entropy at that corner is zero. Thus no theorem asserting domination of every return cell by every strict old local supporting plane is possible. This local point is not asserted to be a complete stationary vertex of a specified closed tree. A valid universal comparison must use the global stationary constraints or a genuine whole-cluster replacement.
