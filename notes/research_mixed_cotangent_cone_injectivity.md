# A cotangent-cone criterion for the open-word Hessian

Research lemma and obstruction, 5 November 2026. The extra type-four
own terms do not by themselves permit unrestricted heights after
dropping the internal pair-sum condition. A separate cotangent condition
does give a sufficient Hessian criterion without that condition. The
localized source point satisfies it; membership of the positive
geometric inverse remains open. No root cover or new source estimate
is used here.

## 1. The exact pair form

Use the original primitive \(J''(z)=\pi\cot\pi z\) and the
original open-word action in
[the Hessian theorem](research_mixed_open_word_hessian.md).
For two legs \(z,w\) with \(0<\Re z,\Re w<1/2\), put
\[
 p=\cot\pi z=P+iv,\qquad q=\cot\pi w=Q+iw_0,\qquad
 c=\Re\cot\pi(z+w).
 \tag{1}
\]
Then \(P,Q>0\). The negative real Hessian of
\(V(z,w)=J(z+w)-J(z)-J(w)\), divided by \(\pi\), is
\[
 M=\begin{pmatrix}P&0\\0&Q\end{pmatrix}
                  -c\begin{pmatrix}1&1\\1&1\end{pmatrix}.
 \tag{2}
\]
The cotangent addition identity gives
\[
\begin{split}
 c&=\frac{PQ(P+Q)+P w_0^2+Qv^2-(P+Q)}
                {(P+Q)^2+(v+w_0)^2},\\
 \det M
  &=\frac{(P+Q)^2-(P w_0-Qv)^2}
                {(P+Q)^2+(v+w_0)^2}.
\end{split}
\tag{3}
\]
There is no zero denominator because \(P+Q>0\).

**Lemma 1.** If \(|v|,|w_0|<1\), then \(M\) is positive
definite, whether or not \(\Re(z+w)>1/2\).

Indeed \(|P w_0-Qv|<P+Q\), so its determinant is positive.
The identity \(\det M=PQ-c(P+Q)>0\) also gives
\(c<PQ/(P+Q)<\min(P,Q)\). Thus both diagonal entries
are positive. This proves the lemma.

For clarity, the exact single-leg condition is
\[
 |\Im\cot\pi(x+iy)|<1
 \quad\Longleftrightarrow\quad
 \cos(2\pi x)<e^{-2\pi|y|},
 \qquad 0<x<1/2.
 \tag{4}
\]
Its proof is the positive-denominator formula
\[
 |\Im\cot\pi(x+iy)|
   =\frac{\sinh(2\pi|y|)}
          {\cosh(2\pi y)-\cos(2\pi x)}.
 \tag{5}
\]
The set in (4) is not being asserted convex.

## 2. What this gives for the full open word

Let every leg satisfy (4), let
\(0<\Re u_L<\Re s_1<1/2\) and
\(0<\Re u_R<\Re t_m<1/2\), and retain the original action
and logarithms. At an endpoint of type three also require its
vertex sum to have real part greater than \(1/2\).
For \(m=1\), impose this last condition only when the single
vertex is type three.

**Lemma 2.** Under these hypotheses,
\(-\Re\mathcal F_m''\) is positive definite for every word
length. No internal vertex-sum or shared-wire-sum lower bound
is needed.

For \(m\ge2\), use the exact decomposition from the
[pair-sum chamber proof](research_mixed_positive_geometry_action_route.md#1-a-convex-chamber-using-adjacent-leg-sums).
Every interior vertex pair \(V\) and every shared pair \(V\)
is positive definite by Lemma 1. The additional type-four
own terms have positive negative real Hessian.

At a type-three endpoint, the remaining vertex term is
\(W(e,t)=J(e+t)-J(t)\). The retained sum condition gives
\[
 -\Re d^2W
   =\pi\{-\Re\cot\pi(e+t)(de+dt)^2
                      +\Re\cot\pi t\,dt^2\}>0.
 \tag{6}
\]
At a type-four endpoint its own terms instead give
\[
 W(e,t)-J(e)-J(t)=V(e,t)-J(t),
 \tag{7}
\]
which is positive by Lemma 1 without a sum condition.
Each original endpoint function
\(B(e,u)=-2J(1/2-u)-3J(u)-J(e-u)\) has
\[
 -\Re d^2B
  =\pi\Re(2\tan\pi u+3\cot\pi u)\,du^2
                  +\pi\Re\cot\pi(e-u)(de-du)^2>0.
 \tag{8}
\]
This controls the endpoint coordinates with no artificial
\(-J(e)\) term. The original purely imaginary quadratic
polynomial has zero Hermitian real Hessian.

For \(m=1\), the two endpoint functions already control
all four variables. The remaining vertex term is \(V(s_1,t_1)\)
at type four, or \(J(s_1+t_1)\) at type three. The latter has
positive semidefinite negative real Hessian under the retained
sum condition. This also verifies the literal short-word case.

On any **convex** subdomain satisfying these hypotheses, integrating
the complex Hessian along a segment proves injectivity of the original
holomorphic gradient, exactly as in the cited chamber proof.
Pointwise positivity on a nonconvex union alone is not such an
injectivity statement.

One explicit open convex choice places every leg in
\[
       1/5<\Re z<1/2,\qquad |\Im z|<3/20,
 \tag{9}
\]
and retains the linear endpoint inequalities and the type-three
endpoint-sum inequalities above. To verify (4), use
\[
 \cos(2\pi\Re z)
  <\cos(2\pi/5)=\frac{\sqrt5-1}{4}<\frac13
  <e^{-1}<e^{-2\pi|\Im z|}.
 \tag{10}
\]
Here \(\sqrt5<7/3\), \(e<3\), and \(3\pi/10<1\)
suffice. The strict localized source rectangles
\[
 Q=[.23,.45]+i[-.12,.12],\qquad
 E=[.33,.47]+i[-.09,.08]
 \tag{11}
\]
lie inside (9), and their endpoint sums exceed \(1/2\).
Thus the source-side inclusion is immediate. The current geometric
inverse-leg theorems do **not** establish (9), (4), or another
common convex domain of this kind.

## 3. Why the extra type-four terms alone are insufficient

Consider the literal length-three word \((3,4,3)\). Set
\[
\begin{split}
 s_1=t_1=s_3=t_3&=2/5,\qquad u_L=u_R=1/5,\\
 s_2&=1/8+i/2,\qquad t_2=1/8-i/2.
\end{split}
\tag{12}
\]
Every leg has real part strictly between zero and \(1/2\).
Both endpoint vertex sums are \(4/5\), both shared-wire sums
have real part \(21/40>1/2\), and the endpoint ordering is
strict. The only omitted condition of the earlier chamber is
the middle type-four vertex sum, which equals \(1/4\).
All original \(J\) arguments remain in their regular strips.

Vary only the two middle legs by \(ds_2=dt_2=1\).
Put
\[
 C=\frac{\sin(\pi/4)}{\cosh\pi-\cos(\pi/4)},\qquad
 D=\frac{\sin(\pi/20)}{\cosh\pi+\cos(\pi/20)}.
 \tag{13}
\]
The original action gives exactly
\[
 \frac{-\Re d^2\mathcal F_3}{\pi}=6C-4+2D.
 \tag{14}
\]
Each middle leg has three negative own copies: two from its
shared edge and one from its type-four term. The middle
\(J(s_2+t_2)\) contributes \(-4\), and the two literal
shared-edge terms contribute \(2D\). No endpoint term varies.

Since \(\pi>3\),
\[
 \cosh\pi>1+\frac{3^2}{2}+\frac{3^4}{24}>8.
 \tag{15}
\]
Consequently \(0<C<1/7\) and \(0<D<1/8\), and (14) is
strictly less than
\[
                \frac67-4+\frac14=-\frac{81}{28}<0.
 \tag{16}
\]
Thus dropping only the type-four internal sum condition, while
leaving imaginary parts unrestricted, destroys the proposed
positive-Hessian criterion even for three vertices.

This is an exact counterexample to that **chamber criterion**.
The point in (12) is not asserted critical, geometrically positive,
or relevant to a finite-source cancellation. An indefinite Hessian
at this point also does not, by itself, prove that the full gradient
map is noninjective.
