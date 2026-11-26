# A uniform retained-vertex bound when either Fourier height moves

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This estimate permits a complex outgoing Fourier parameter in the
first attachment. One wire stays at height \(Y_*=(\log2)/(2\pi)\);
the other height may move in either direction by \(1/200\).
The estimate concerns the original finite vertex with the larger
corner \(L=\lfloor N/40\rfloor\) deleted. It bounds the sum of
absolute values of its summands, so it also applies to every subset
of the real summation indices.

## 1. The global real envelope

Write this retained vertex as \(\widetilde V_N^{(40)}\). Its
finite formula is equation (2) of
[the global modulus proof](research_three_vertex_global_wire_bound.md),
with \(L=\lfloor N/40\rfloor\). Put
\[
 x=\xi+i(Y_*+v),\quad y=\eta+iY_*,\quad |v|\le1/200,
 \qquad r=\tfrac12e^{-2\pi v}.
 \tag{1}
\]
Then \(12/25<r<13/25\). For \(0<r<1\), define
\[
 \ell_r(s)=\int_{-s/2}^{s/2}\log|1-r e^{2\pi iu}|\,du.
\]
Minimizing the denominator interval over each real wire phase gives
the real envelope
\[
 \begin{split}
 \mathscr E_r(s,t)={}&-\tfrac12\log(r/2)+\mathcal J(s+t)
                    +s\log r+t\log(1/2)-\ell_r(s)-\ell_{1/2}(t),\\
 \mathcal D_{40}={}&\{s,t\ge0:s+t\le1,\ \max(s,t)\ge1/40\}.
 \end{split}
 \tag{2}
\]
The cardinal factors are included in the first term. Uniform endpoint
factorial bounds give a polynomial times \(e^{N\mathscr E_r}\)
for each original summand. The denominator estimates are uniform
because both radii stay strictly below one.

**Theorem 1.** For all real \(\xi,\eta\) and \(|v|\le1/200\),
\[
 |\widetilde V_N^{(40)}(x,y)|\le CN^a e^{6466N/10000}.
 \tag{3}
\]
More precisely, its maximum summand envelope satisfies
\[
 E(v):=\max_{\mathcal D_{40}}\mathscr E_r
       \le 2c+15v^2<646507/10^6<6466/10000,
 \qquad c=2\mathcal J(5/6).
 \tag{4}
\]
The same statement holds with the two wires interchanged, at both
parities and with every fixed wire derivative at polynomial cost.

## 2. Locating the maximum throughout the radius interval

We prove the stronger radius statement \(12/25\le r\le13/25\).
Set \(p=s+t\). If \(p\le1/3\), the elementary bounds
\(\ell_r(s)\ge s\log(1-r)\),
\(\ell_{1/2}(t)\ge t\log(1/2)\) give
\[
 \mathscr E_r\le\log2+\mathcal J(p)-\tfrac12\log(2r)
                                      +s\log\frac r{1-r}.
 \tag{5}
\]
On \([1/40,1/3]\), the maximum of \(\mathcal J\) is at an
endpoint, since its derivative changes from negative to positive
only at \(1/6\). Both endpoint values are below \(-7/100\):
\[
 \mathcal J(1/40)\le{\log(\pi/20)-1\over40}<-7/100,
 \qquad \mathcal J(1/3)=-c/3<-7/100.
 \tag{6}
\]
For \(r\le1/2\), the last two terms in (5) are at most
\(-\tfrac12\log(24/25)<21/1000\). For \(r\ge1/2\), they
are at most
\[
 g(r)=-\tfrac12\log(2r)+\tfrac13\log\frac r{1-r}.
\]
Here \(g(1/2)=0\) and \(g'(r)<2/5\), so \(g(r)<1/125\).
Using \(\log2<347/500\), (5) is therefore below \(129/200=.645\).
At \(s=t=1/3\), the value at \(v=0\) is \(2c>.646\), its
height derivative is zero, and its height second derivative is
positive. It remains at least \(2c\) throughout the radius interval.
Thus no global maximum has \(p\le1/3\).

If \(1/3\le p\le1/2\), increase the smaller index, which is
at most \(1/4\). Its exponential derivative is
\[
 {2r_i\sin(\pi p)\over|1-r_i e^{\pi i s_i}|}>1,
             \qquad r_i\in[12/25,13/25].
 \tag{7}
\]
The ratio increases with \(r_i\). At \(r_i=12/25\), its
numerator is at least \((12/25)\sqrt3\); its denominator is
at most \(\sqrt{1+(12/25)^2-(24/25)\cos(\pi/4)}\), which is
strictly smaller. This feasible variation excludes this region too.

On \(p>1/2\), the negative index Hessian is
\[
 A=\operatorname{diag}(d_1,d_2)+k\mathbf1\mathbf1^T,
 \quad d_i={\pi r_i\sin(\pi s_i)\over1+r_i^2-2r_i\cos(\pi s_i)},
 \quad k=-\pi\cot(\pi p)>0.
 \tag{8}
\]
It is positive definite. The lower faces of \([.30,.37]^2\)
have inward positive derivatives and its upper faces inward negative
derivatives. It suffices to check
\[
 (24/25)^2\sin^2(67\pi/100)
       >1+(12/25)^2-(24/25)\cos(3\pi/10),
\]
\[
 (26/25)^2\sin^2(67\pi/100)
       <1+(13/25)^2-(26/25)\cos(37\pi/100).
 \tag{9}
\]
The monotonicities in (7) and the decrease of \(\sin(\pi p)\)
for \(p>1/2\) prove the full-face assertions. Hence this square
contains an interior stationary point. Strict concavity on the
convex region \(p>1/2\) makes it the unique global maximizer
there. The preceding exclusions show it is the unique maximizer
of (2) for every radius in the stated interval.

## 3. Bounding the change of its critical value

The maximizing point is smooth in the height. Put
\[
 q_i={2\pi(1-r_i\cos(\pi s_i))\over
                         1+r_i^2-2r_i\cos(\pi s_i)}.
\]
Differentiation before maximizing gives height second derivative
\(4d_1\) and mixed index-height derivative \(-q_1\).
The real Schur complement therefore gives
\[
                    E''(v)=4d_1+q_1^2(A^{-1})_{11}.
 \tag{10}
\]
Throughout the square just proved,
\[
        8/5<d_i<21/10,\qquad q_i<34/5,\qquad k>1.
 \tag{11}
\]
These are endpoint inequalities. Indeed \(d_i\) increases with
\(r_i\) and decreases with \(s_i\), whereas \(q_i\) decreases
with both. The derivative signs use
\(\cos(\pi s_i)<3/5<2r_i/(1+r_i^2)\).
Thus only \(d(.37,.48),d(.30,.52),q(.30,.48)\), and
\(-\pi\cot(3\pi/5)\) need be bounded.
Consequently
\[
 (A^{-1})_{11}={1\over d_1+kd_2/(d_2+k)}<{65\over144},
 \quad E''<{42\over5}+\left({34\over5}\right)^2{65\over144}<30.
 \tag{12}
\]
Since \(E(0)=2c,E'(0)=0\), integrating twice proves the first
inequality in (4), also for negative \(v\). The calibrated bound
\(c<161533/500000\) proves its strict numerical upper bound.
Summing at most \(N^2\) finite summands proves (3). Derivatives
cost only polynomial factors on a slightly larger radius interval;
the strict margin in (4) absorbs this enlargement. \(\square\)

The cutoff in this theorem is essential to this proof. At the smaller
cutoff \(N/50\), the low-axis envelope can rise above the required
central comparison when the height increases. The
[larger-corner error theorem](research_three_chain_fourier_corner_transfer.md#4-a-larger-deleted-corner-for-a-larger-source-domain)
justifies this change after contraction with the original boundaries.
No full first-attachment asymptotic on a \(.005\) disk follows from
(3) alone; the remaining coherent central estimates are separate.

## 4. Two moving heights at the central attachment contour

The angular remainder in the prepared-cap argument needs a bound
when the first height is already displaced. The same global
maximization proof gives the following useful extension.

**Proposition 2.** Delete the same \(N/40\) corner, and suppose
\[
 x=\xi+i(Y_*+v_1),\quad y=\eta+i(Y_*+v_2),\qquad
 -9/1000\le v_1\le0,\quad |v_2|\le1/200.
 \tag{13}
\]
Uniformly over both real phases, the sum of absolute values of
the retained summands is at most a polynomial times
\[
 \exp\{N(2c+19(v_1^2+v_2^2))\}
                     <\exp(1297N/2000).
 \tag{14}
\]
The assertion includes every real-index subset, both parities,
and every fixed wire derivative at polynomial cost.

*Proof.* The radii lie in the rectangle
\(r_1\in[1/2,53/100]\), \(r_2\in[12/25,13/25]\).
The height rectangle (13) is convex and contains the origin.
We must first justify a single smooth global maximum on it;
a Hessian bound at the origin alone would not suffice.

For \(p=s+t\le1/3\), the same denominator estimate as (5) gives
\[
 \mathscr E\le -\tfrac12\log(6/25)+\mathcal J(p)+p\log(53/47).
 \tag{15}
\]
The right side is convex in \(p\in[1/40,1/3]\), because
\(\mathcal J''(p)=\pi\cot(\pi p)>0\). At both endpoints
it is strictly below \(2c\), as verified by the scalar bounds
\[
 \begin{split}
 -\tfrac12\log(6/25)
   +{\log(\pi/20)-1+\log(53/47)\over40}&<2c,\\
 -\tfrac12\log(6/25)-c/3+\tfrac13\log(53/47)&<2c.
 \end{split}
 \tag{16}
\]
At \(s=t=1/3\), both height derivatives vanish at the origin
and the fixed-index height Hessian is positive diagonal. Its value
therefore remains at least \(2c\) throughout the radius rectangle.
This excludes (15). The smaller-index argument (7) still excludes
\(1/3\le p\le1/2\). The lower-face comparison in (9) is
unchanged; on the upper face replace \(13/25\) by \(53/100\).
The resulting strict inequality still holds. Thus the unique
global maximum remains in \([.30,.37]^2\).

On this larger radius rectangle, (11) remains valid: its only new
endpoint is \(d(.30,.53)<21/10\). Let
\(Q=\operatorname{diag}(q_1,q_2)\). The full height Hessian of
the optimized value is exactly
\[
 \nabla_v^2E=\operatorname{diag}(4d_1,4d_2)+QA^{-1}Q.
 \tag{17}
\]
Since \(A\succeq(8/5)I\), its operator norm satisfies
\[
 \|\nabla_v^2E\|
   <42/5+(34/5)^2(5/8)=373/10<38.
 \tag{18}
\]
The value and gradient at the origin are \(2c\) and zero.
Integrating along the segment from the origin to \(v\) proves
the first exponent in (14). Finally
\[
 2c+19\{(9/1000)^2+(1/200)^2\}
                 <648146/10^6<1297/2000.
 \tag{19}
\]
The original finite-product estimate proves all the stated
summand and derivative bounds as in Theorem 1. \(\square\)

For example, an angular remainder of rate \(1.26\) on this
input contour then has product rate below \(1.9085\). This
comparison does not supply that separate angular-remainder bound.

## 5. Reproduction

Run `python3 experiments/check_three_vertex_symmetric_height_bound.py`.
Its scalar bounds verify all endpoints in the written global
maximization proof, rather than sampling a maximum.
