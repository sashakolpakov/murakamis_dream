# A common convex domain for the ordinary-boundary critical equations

Research lemma, 5 November 2026. The ordinary endpoint coefficients
change the leading action of an open word. Nevertheless the enlarged
action has a uniform positive negative Hessian on one explicit product
of rectangles, independently of the length and order of the word.
This supplies uniqueness and a quantitative local inverse wherever a
critical point in that product exists. Existence and the full finite
contour estimate are separate requirements.

## 1. The action and its variables

Fix a word \(3+\epsilon_1,\ldots,3+\epsilon_m\), where
\(m\ge1\) and each \(\epsilon_j\) is zero or one. Vertex \(j\)
has two complex leg coordinates \(s_j,t_j\). The left ordinary
boundary introduces a coordinate \(u_L\), and the right boundary
introduces \(u_R\). The private endpoint legs are \(s_1,t_m\);
all other leg coordinates are called internal here.

Use the primitive \(J\) satisfying
\(J'(z)=\operatorname{Log}(2\sin\pi z)\), with its continuation
from positive real sine on \(0<\Re z<1\). In particular
\(J''(z)=\pi\cot\pi z\). At the complete ordinary color the
exact leading action from
[the full boundary sum](research_mixed_complete_boundary_sum.md),
equations (11), (21)--(22), is
\[
\begin{split}
 \mathcal F_m={}&
 \sum_{j=1}^m\{J(s_j+t_j)-\epsilon_j[J(s_j)+J(t_j)]\}\\
 &+\sum_{j=1}^{m-1}\{J(t_j+s_{j+1})-2J(t_j)-2J(s_{j+1})\}\\
 &+B(s_1,u_L)+B(t_m,u_R)+i\pi Q_m,                         \tag{1}\\
 B(e,u)={}&-2J(1/2-u)-3J(u)-J(e-u),\\
 Q_m={}&\sum_{j<m}t_js_{j+1}-\sum_{j\le m}s_jt_j
       +s_1u_L+t_mu_R
       +\frac12\sum_{j\le m}\epsilon_j(s_j^2+t_j^2-s_j-t_j).
\end{split}
\]
The polynomial \(Q_m\) has real coefficients. Its contribution
to the Hermitian real part of the complex Hessian is therefore zero.
The endpoint terms in (1) are part of the order-\(N\) action;
they are not bounded prefactors multiplying the cyclic integrand.

Define the closed rectangles
\[
\begin{split}
 Q&=[.23,.45]+i[-.12,.12],\\
 E&=[.33,.47]+i[-.09,.08],\\
 U&=[.21,.25]+i[.01,.10].                                  \tag{2}
\end{split}
\]
Let \(\mathcal D_m\) be the product with \(s_1,t_m\in E\),
\(u_L,u_R\in U\), and every internal leg in \(Q\).
For \(m=1\) both vertex legs are private, so there are no
\(Q\)-coordinates. Every argument of \(J\) in (1) stays in
the regular strip on a neighborhood of \(\mathcal D_m\).
For example \(\Re(e-u)\in[.08,.26]\), endpoint vertex sums
have real part in \([.56,.92]\) for \(m\ge2\), and the sole
vertex sum for \(m=1\) lies in \([.66,.94]\).

## 2. The interior pair estimate

Write \(C(z)=\Re\cot\pi z\). For
\(V(z,w)=J(z+w)-J(z)-J(w)\), the real quadratic form of its
negative Hessian is
\[
 -\Re V''=
 \pi\{C(z)\,dz^2+C(w)\,dw^2-C(z+w)(dz+dw)^2\}.           \tag{3}
\]
On \(Q\),
\[
 C(x+iy)=\frac{\sin(2\pi x)}{\cosh(2\pi y)-\cos(2\pi x)}
                         >\frac9{70}>\frac18.              \tag{4}
\]
Indeed \(\cosh(.24\pi)<4/3\), and the sine is greater than
\(3/10\) throughout the real interval. The denominator is less
than \(7/3\).

If \(\Re(z+w)\ge1/2\), then \(C(z+w)\le0\), and (4)
gives \(-\Re V''>(\pi/8)I_2\). Otherwise both individual
real coordinates are at most \(.27\). On that smaller interval,
\(\sin(2\pi x)>4/5\) and \(\cos(2\pi x)>-1/2\), so
\(C(z),C(w)>24/55\). Also
\[
 0<C(z+w)\le\cot(.46\pi)=\tan(\pi/25)<1/7.
\]
Since \((dz+dw)^2\le2(dz^2+dw^2)\), (3) is then greater
than \((58\pi/385)I_2>(\pi/8)I_2\). Thus, in all cases,
\[
                  -\Re V''>(\pi/8)I_2\quad\text{on }Q^2.
                                                               \tag{5}
\]
This is the interior pair estimate used in the cyclic argument,
with its elementary scalar margins retained explicitly.

## 3. The endpoint supplies its own coercivity

For \((e,u)\in E\times U\), differentiating the endpoint
term in (1) gives
\[
 -\Re B''=a\,du^2+b(de-du)^2,\qquad
 a=\pi\Re(2\tan\pi u+3\cot\pi u),\quad
 b=\pi\Re\cot\pi(e-u).                                   \tag{6}
\]
The following uniform rational bounds are sufficient:
\[
                         a>3\pi,\qquad b>2\pi/15.          \tag{7}
\]
For the first, \(\sin(2\pi\Re u)>9/10\),
\(0\le\cos(2\pi\Re u)<1/4\), and
\(\cosh(2\pi\Im u)<5/4\). The formulas for real parts of
the tangent and cotangent consequently give
\(\Re\tan\pi u>3/5\) and \(\Re\cot\pi u>18/25\).
Thus \(a>(84/25)\pi>3\pi\).
For the second, \(\Re(e-u)\in[.08,.26]\) and
\(|\Im(e-u)|\le.19\). The sine on this interval exceeds
\(2/5\), while \(\cosh(.38\pi)<2\); the denominator in
(4) is less than three. This proves (7).

In coordinates \((u,e)\), the lower comparison matrix in (6)
is
\[
 \pi\begin{pmatrix}3+2/15&-2/15\\-2/15&2/15\end{pmatrix}.
                                                               \tag{8}
\]
It is positive definite. Its least eigenvalue is strictly greater
than its determinant divided by its trace, which is \(6\pi/49\).
Increasing either coefficient in (6) adds a positive semidefinite
matrix. Therefore
\[
                  -\Re B''>(6\pi/49)I_2.                  \tag{9}
\]

The endpoint vertex contributes
\(W(e,t)=J(e+t)-J(t)\), where \(t\in Q\) is its attached
internal leg. Since \(1/2<\Re(e+t)<1\),
\[
 -\Re W''=
 -\pi C(e+t)(de+dt)^2+\pi C(t)\,dt^2
                         \ge (\pi/8)\,dt^2.               \tag{10}
\]
There is no subtraction of \(J(e)\) in \(W\). Adding one
would change the original endpoint action.

## 4. All word lengths and the local endpoint equations

**Theorem 1.** On \(\mathcal D_m\), for every fixed word,
\[
                   -\Re\mathcal F_m''>(6\pi/49)I_{2m+2}.
                                                               \tag{11}
\]
The full holomorphic gradient is injective on this convex product.
Any critical point there is simple, and
\(\|(-\mathcal F_m'')^{-1}\|_2<49/(6\pi)\).

For \(m\ge2\), decompose (1) into the two endpoint terms
\(B\), the two endpoint vertices \(W\), all interior vertex
pairs \(V\), all shared pairs \(V\), and the additional terms
\(-\epsilon_j[J(s_j)+J(t_j)]\). This decomposition is exact:
every internal leg is incident to two pairs, while a private leg
has no unweighted own term outside its endpoint function \(B\).
The two endpoint functions supply (9) on their four coordinates.
Each internal leg receives two contributions of at least
\(\pi/8\), by (5) and (10). The extra type-four own terms are
positive because every leg has real part between zero and \(1/2\).
Since \(\pi/4>6\pi/49\), this proves (11).

For \(m=1\), use the two endpoint functions and the remaining
term \(J(s_1+t_1)\). The latter has a positive semidefinite
negative real Hessian because its summed real coordinate is in
\((1/2,1)\). The type-four own terms remain positive. Equation
(11) therefore holds in this case too.

For two points \(z,w\) in the product, pair the integral of
their Hessian along the segment with \(\overline{z-w}\).
Equation (11) gives
\[
 \Re\bigl[(z-w)^*(-\nabla\mathcal F_m(z)+
                         \nabla\mathcal F_m(w))\bigr]
                 >(6\pi/49)\|z-w\|_2^2
\]
when \(z\ne w\). This proves injectivity. The same accretive
matrix inequality and Cauchy--Schwarz prove the inverse-norm bound.
Holomorphy on a neighborhood of the product then gives the usual
local continuation of any critical point under small parameter changes.

There is an immediate local version needed for an endpoint update.
Fix its external leg \(b\in Q\), and solve for its private leg
\(e\in E\), attached leg \(t\in Q\), and endpoint coordinate
\(u\in U\). The action is the corresponding endpoint portion
of (1), including \(J(t+b)\) and all original own terms and
quadratic phases. The same proof, with \(db=0\) in its shared
pair, gives (11) in these three unknowns. Thus this local problem
has at most one zero in \(E\times Q\times U\), and a zero
has a nondegenerate Jacobian. This statement holds at either end.

The theorem does not show that those local zeros exist or that their
attached legs map into the prescribed typed disks. Those image bounds
would permit the all-length fixed-point construction. Nor does (11)
prove that the finite boundary coefficient has its selected asymptotic
on all of \(E\): the previously established complex neighborhoods
near real indices have unspecified size. A contour estimate on the
actual endpoint image is still required.

## 5. Reproduction

The small checker verifies the rational constants, the endpoint
two-by-two matrix, and the eleven strict trigonometric inequalities
used above with outward arithmetic. It performs no critical-root search
or parameter cover.

```sh
python3 experiments/check_mixed_open_word_hessian.py --precision 192
python3 experiments/check_mixed_open_word_hessian.py --precision 256 --input repro/results/research-mixed-open-word-hessian.json --output /tmp/research-mixed-open-word-hessian-review.json
```
