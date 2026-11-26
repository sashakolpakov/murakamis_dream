# A selected six-leaf counterexample to return tangent domination

Private exact proof, 1 November 2026. No repository source is changed.

The four tangent inequalities proposed in /private/tmp/md-source-selected-cubic-tangent-domain.md are false. They fail at the genuine strict complete optimizer of a six-leaf all-turn tree, not merely at a point satisfying necessary derivative inequalities. The original optimizer has no high internal edge. This note first proves that general high-edge exclusion and then gives the exact counterexample with a certified negative tangent margin.

## 1. High internal edges are absent at the complete optimum

Consider the same finite trivalent tree as in the restricted clamping theorem: every internal edge carries a physical turn, every external effective leaf has its original positive profile \(g+c_\ell\), and the original all-complete source has a strict maximizing state.

Cut an internal edge with covariant label \(x\). Each side is an unturned product \(A\) or \(B\) with \(L/A\) children. The two ordinary output labels are both \(1-x\), because the covariant contraction includes the physical turn. Optimizing the two disjoint sides with this label fixed gives the exact action
\[
\mathcal F_{\mathrm{edge}}(x)
   =f_A(1-x)+f_B(1-x).
\tag{1}
\]
Every absolute branch constant is retained in these profiles; there is no extra edge action.

For \(x>1/2\), both outputs lie in \((0,1/2)\). The unturned-product theorem gives
\[
f_A'(1-x)\ge f_{hh}'(1-x)>0,\qquad
f_B'(1-x)\ge f_{hh}'(1-x)>0.
\]
Consequently
\[
\mathcal F_{\mathrm{edge}}'(x)
 =-f_A'(1-x)-f_B'(1-x)<0.
\tag{2}
\]
This contradicts stationarity at a strict complete maximum. Thus every internal label is at most \(1/2\); external labels are already in the leaf interval \((0,1/2)\).

At \(x=1/2\), stationarity forces both \(f_A'(1/2)\) and \(f_B'(1/2)\) to vanish. The strict form of the product derivative theorem says this can happen only if each product has two \(L\) children. Thus an internal equality \(x=1/2\) is possible only for the tree consisting of two cubic vertices and four effective \(L\) leaves. In every larger such tree all internal labels are strictly below \(1/2\).

## 2. The literal six-leaf source and its strict state

Let \(A_j=h_{j,1}h_{j,2}\), \(j=1,2,3\), be three ordinary two-leaf products, with six distinct leaves. Consider the original positive source of
\[
C\bigl((T A_1)(T A_2)(T A_3)\bigr).
\tag{3}
\]
One may associate the last two factors to obtain the prescribed closure of two \(A\)-type expressions. Its covariant tree has a central cubic vertex joined by three physical turn edges to three outer cubic vertices. Each outer vertex has two effective \(L\) leaves. Thus this is an actual strict construction in the all-turn trivalent class.

Set
\[
a=\frac1\pi\arctan(2\sqrt3),\qquad
B=\cot(\pi a)=\frac1{2\sqrt3}.
\tag{4}
\]
Give each of the three internal edges label \(a\), and each of the six external leaves label \(1/3\). Since
\[
\frac13<a<\frac5{12}<\frac12,
\tag{5}
\]
every complete cubic inequality is strict. The central vertex has labels \((a,a,a)\). Each outer vertex has labels \((1/3,1/3,a)\). Their pair sums are less than one and their total sums exceed one. The upper inequality \(a<5/12\) follows from
\[
\frac1{2\sqrt3}>2-\sqrt3
\quad\Longleftrightarrow\quad 7>4\sqrt3,
\]
which follows by squaring \(49>48\).

For the complete cubic action
\[
t(x,y,z)=\sum_{\mathrm{pairs}}J(x+y)
 -J(x)-J(y)-J(z)-J(x+y+z-1),
\qquad J(u)=\int_0^u\log(2\sin\pi v)\,dv,
\tag{6}
\]
write \(A=\cot\pi x\), \(B_1=\cot\pi y\), \(C=\cot\pi z\). On the positive domain with all labels at most \(1/2\),
\[
D=1-AB_1-AC-B_1C>0,\qquad
\partial_x t=\log\frac{(A+B_1)(A+C)}D.
\tag{7}
\]
This follows by expanding \(\sin\pi(x+y+z)\); the other two derivatives are obtained cyclically.

At the central vertex, all three cotangents equal \(1/(2\sqrt3)\). Thus \(D=3/4\), and
\[
\partial_x t(a,a,a)
 =\partial_y t(a,a,a)
 =\partial_z t(a,a,a)=\log(4/9).
\tag{8}
\]
At an outer vertex the two leaf cotangents are \(1/\sqrt3\), the internal-edge cotangent is \(1/(2\sqrt3)\), and \(D=1/3\). Equation (7) gives
\[
\partial_{\mathrm{leaf}}t=\log3,\qquad
\partial_{\mathrm{internal}}t=\log(9/4).
\tag{9}
\]
The original leaf derivative is
\[
g'(1/3)=2\log\cot(\pi/3)=-\log3.
\tag{10}
\]
Hence (9) cancels (10) at each physical leaf, while (8) cancels the internal derivative in (9) across each turn edge. The whole state is stationary. Strict concavity of the retained complete gate action and the original leaf action, or equivalently the existing strict-source uniqueness theorem, makes it the unique complete maximizer of (3).

This verifies the source selection directly. No arbitrary external profile or numerical optimizer is used.

## 3. The branch inequalities hold with equality

For a two-leaf product, put
\[
X_2(B)=\frac{B+\sqrt{B^2+2}}2,\qquad
f_{hh}'(x)=2\log(2X_2(\cot\pi x)^2).
\tag{11}
\]
At (4),
\[
X_2(B)=\frac{\sqrt3}{2},\qquad
f_{hh}'(a)=\log(9/4).
\tag{12}
\]
Consequently the central vertex satisfies every proposed source-selected restriction exactly:
\[
\partial_x t(a,a,a)+f_{hh}'(a)=0,
\]
and likewise for the other two coordinates. It also has \(a<1/2\), so the high-edge exclusion of Section 1 adds no further restriction to this example.

## 4. A certified negative tangent at the return corner

Let the old tangent plane at this central state be
\[
L(u)=t(a,a,a)+\log(4/9)\bigl(u_1+u_2+u_3-3a\bigr).
\tag{13}
\]
The point \(u=(1,1,1)\) is a feasible corner of the closed return domain, and its return action is zero. We prove
\[
\boxed{\quad L(1,1,1)<-\frac{11}{40}<0.\quad}
\tag{14}
\]

First, the old prism formula expresses \(\pi t(a,a,a)\) as the sum of three positively oriented ideal tetrahedron volumes. The positive parameters are \(p=q=w=1-2a\) and \(r=3a-1\); they satisfy the original strict prism conditions by (5). Every ideal tetrahedron has volume at most the regular ideal tetrahedron volume \(v_3\), by concavity of its volume on the angle simplex. Thus
\[
t(a,a,a)\le\frac{3v_3}{\pi}.
\tag{15}
\]
An elementary Fourier estimate gives the convenient rational bound \(v_3<9/8\). In fact,
\[
v_3=\frac{3\sqrt3}{4}
 \sum_{k=0}^{\infty}
 \left(\frac1{(3k+1)^2}-\frac1{(3k+2)^2}\right).
\tag{16}
\]
For \(k\ge1\), the difference in parentheses is less than \(2/(3k+1)^3\), and
\[
\sum_{k=1}^{\infty}\frac1{(3k+1)^3}
 \le\frac1{64}+\int_1^\infty\frac{dt}{(3t+1)^3}
 =\frac5{192}.
\]
Therefore the series in (16) is less than \(3/4+5/96=77/96\). Using \(\sqrt3<7/4\) gives
\[
v_3<\frac{21}{16}\frac{77}{96}
 =\frac{539}{512}<\frac98.
\tag{17}
\]
Since \(\pi>3\), (15)–(17) imply \(t(a,a,a)<9/8\).

Second, \(a<5/12\) gives \(3(1-a)>7/4\). Also
\[
\log(3/2)
 =\log\frac{1+1/5}{1-1/5}
 =2\left(\frac15+\frac1{3\cdot5^3}+\cdots\right)>\frac25,
\]
so \(\log(9/4)>4/5\). Combining these estimates with (13),
\[
L(1,1,1)
 =t(a,a,a)-3(1-a)\log(9/4)
 <\frac98-\frac74\frac45=-\frac{11}{40}.
\]
This proves (14) without numerical quadrature. By continuity, tangent domination also fails at interior return points sufficiently close to \((1,1,1)\), where the return action tends to zero.

## 5. What this rules out

The complete optimum does have all internal labels at most \(1/2\), and genuine branch pressures impose the selected derivative inequalities. Neither fact repairs the local tangent comparison. The counterexample is a literal strict source with explicit stationary labels and exact derivative cancellations.

This does not contradict the one-return-cluster clamping theorem. That theorem reoptimizes whole terminal branches and compares actual feasible actions. The tangent attempt instead charges a distant return state to fixed first derivatives at the original optimum; it can fail even when the reoptimized whole-sector comparison is true.

No whole-contraction lower bound or violation of the original geometric maximum follows. The conclusion is that a global return estimate must retain more than these local old tangent planes, even in the trivalent all-turn class.
