# Horizontal contraction of the complete conditional source

Research deduction, 8 November 2026. The original conditional critical
action decreases strictly as the incoming real coordinate moves right,
at every incoming height in the displaced rectangle. The complete
finite-source theorem on that rectangle makes this an actual
contraction of the original conditional polynomial, including all its
physical rows and contour currents. No cap estimate, outgoing affine
comparison, or numerical evaluation is used.

## 1. Original parameters and derivative

Keep the parameter rectangle
\[
 \mathcal D=\left\{a=x+ih:
 \frac12\le x\le\frac7{10},\ -\frac9{125}\le h\le0;\quad
 y=z+iH:\frac{11}{50}\le z\le\frac9{20},\
                       0\le H\le\frac1{100}\right\}.
 \tag{1}
\]
The original phase and selected critical value are
\[
 \begin{split}
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\\
 Q_t(t_*;a,y)&=0,\qquad
 \Theta(a,y)=Q(t_*;a,y),\\
 X&=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 v=e^{2\pi it_*},\qquad w=\frac{v-X}{1-X}.
 \end{split}
 \tag{2}
\]
These are the exact logarithmic lifts and additive constants of
[the negative-height branch theorem](research_mixed_conditional_negative_height_branch.md).
That theorem gives a simple holomorphic selected root, with
\[
 \Re X<0,\quad \Im X\ge0,\quad
 \Im Y<0,\quad \Im v>0,\qquad
                 v(v-X)(v-Y)=X(v-1)^3 .
 \tag{3}
\]
The original incoming carrier has not been dropped. Stationarity gives
\[
 \Theta_a=g'(a+t_*)-g'(a)+2\pi it_*,
                   \qquad e^{\Theta_a}=w.
 \tag{4}
\]
The upper-half-plane lemma and logarithmic argument in
[height-action monotonicity, Sections 2--3](research_mixed_conditional_height_action_monotonicity.md)
prove \(\Im w>0\) throughout (1), with
\(\Im\Theta_a=\Arg w\in(0,\pi)\).

## 2. A unit-circle exclusion for the actual multiplier

**Lemma 1.** Throughout \(\mathcal D\),
\[
                         0<|w|<1.
 \tag{5}
\]

*Proof.* The value zero is excluded by \(v\ne X\). Suppose \(|w|=1\),
and write
\[
 X=A+iB,\quad A<0,\ B\ge0,\qquad
 w=c+is,\quad s>0,\qquad d=2(1-c)>0.
 \tag{6}
\]
The sign of \(s\) is the previously proved upper-half-plane property.
The identity \(v=X+(1-X)w\) gives
\[
 P:=|v|^2=1+(|X|^2-A)d+2Bs>1.
 \tag{7}
\]
On the unit circle, \((w-1)^2/w=-d\). Substitution into the exact
critical equation in (3), without division by a possible zero, gives
\[
       Y=v+dX(1-X)\left(1-\frac1v\right).
 \tag{8}
\]
Here \(v\ne0\), also by the original equation.

Put
\[
 X(1-X)=C+iD,\qquad
 C=A-A^2+B^2,\qquad D=B(1-2A)\ge0.
 \tag{9}
\]
Equation (7) implies
\[
                  P+dC=1+2Bs+2B^2d>0.
 \tag{10}
\]
Write \(v=r+it\), where \(t>0\). Since \(P>1\),
\(r\le |v|=\sqrt P<P\). Taking imaginary parts of (8) therefore gives
\[
 \Im Y=\frac{t}{P}(P+dC)+\frac{dD}{P}(P-r)>0,
 \tag{11}
\]
contradicting \(\Im Y<0\). Thus the actual multiplier cannot meet
the unit circle.

The rectangle (1) is connected and the selected root is continuous.
At the point \(X=-1,\ Y=-i\), corresponding to
\(a=1/2,\ y=1/4\), the original critical point is \(t_*=1/4\):
indeed its original logarithmic derivative is zero, and \(v=i\).
There \(w=(1+i)/2\) has modulus less than one. The unit-circle
exclusion proves (5) on all of (1). \(\square\)

Taking real parts in the exact exponential identity (4) uses no
logarithmic choice:
\[
                  \Re\Theta_a=\log|w|<0.
 \tag{12}
\]
Compactness consequently gives a fixed \(\kappa>0\) such that
\[
                 \Re\Theta_a\le-\kappa
                         \qquad ((a,y)\in\mathcal D).
 \tag{13}
\]
No numerical value of \(\kappa\) is asserted. In particular, at fixed
incoming height and fixed \(y\),
\[
 \Re\Theta(x_2+ih,y)
 \le\Re\Theta(x_1+ih,y)-\kappa(x_2-x_1),
 \qquad \frac12\le x_1\le x_2\le\frac7{10}.
 \tag{14}
\]
Together with the earlier height theorem this gives two distinct
directions: the action increases when the incoming coordinate moves
down, and decreases when it moves right.

## 3. Contraction of the literal finite polynomial

Keep the original function
\[
 \begin{gathered}
 r_N=e^{-2\pi i/N},\quad P_j=(r_N;r_N)_j,\quad
 p_j(X)=(r_NX;r_N)_j,\\
 C_{1,N}(X,Y)
       =\sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \end{gathered}
 \tag{15}
\]
The entire displaced-rectangle conclusion in Section 6 of
[the complete conditional source theorem](research_mixed_conditional_nonnegative_height_complete_source.md)
proves, on a fixed open complex neighborhood of (1),
\[
 C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})
 =N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                       (1+\varepsilon_N(a,y)),
 \qquad \mathcal B\ne0,\quad
              \varepsilon_N=O_{\rm hol}(N^{-1}).
 \tag{16}
\]
Both parities and all fixed normalized mixed derivatives are included.
This theorem retains the complete physical sum, both half-index
parities, the original \(+N\) residue density, all six weighted
currents, and both unweighted joins. In particular (16) is not a
continuation of only a local critical contribution.

For sufficiently large \(N\), (16) is nonzero on a smaller fixed
neighborhood of (1). Its exact logarithmic derivative satisfies
\[
 \partial_a\log C_{1,N}
     =N\Theta_a+\frac{\mathcal B_a}{\mathcal B}
                  +\frac{\partial_a\varepsilon_N}{1+\varepsilon_N}
     =N\Theta_a+O(1)
 \tag{17}
\]
uniformly there. The \(O(1)\) bound follows from the nonzero
holomorphic symbol and the normalized derivative assertion in (16).
It is independent of the level parity. Combining (13) and (17),
and increasing the lower level threshold once, proves the following
finite-source statement.

**Theorem 2.** Uniformly for all parameters in (1), all sufficiently
large \(N\), and \(1/2\le x_1\le x_2\le7/10\),
\[
 \boxed{\quad
 \left|C_{1,N}(e^{-2\pi i(x_2+ih)},Y)\right|
 \le
 e^{-\kappa N(x_2-x_1)/2}
 \left|C_{1,N}(e^{-2\pi i(x_1+ih)},Y)\right|.
 \quad}
 \tag{18}
\]
Indeed \(\partial_x\log|C_{1,N}|\le-\kappa N/2\), and integration
along this fixed horizontal segment proves (18). There is no
polynomial prefactor in this ratio. Nonvanishing in the preceding
paragraph licenses the logarithmic derivative, including at both
endpoints.

The normalized expansion (16) continues to give every fixed mixed
derivative. For example, for each fixed pair \(j,k\), (14) and
holomorphic differentiation give
\[
 \left|\partial_a^j\partial_y^k C_{1,N}
       (e^{-2\pi i(x_2+ih)},e^{-2\pi iy})\right|
 \le C_{j,k}N^{j+k-1}
 e^{N[\Re\Theta(x_1+ih,y)-\kappa(x_2-x_1)]}.
 \tag{19}
\]
The derivatives in (19) mean derivatives of the displayed composed
function in \(a,y\). They are not derivatives of a moving cut or
of a modulus allocation. An arbitrarily small fixed parameter
enlargement is permitted after spending a prescribed rate tolerance.

Any finite factor independent of \(a\) may be multiplied into both
sides of (18), even when that factor vanishes. In particular the
original selected weight \(d_N(Y)Y^{-N}\), the complete next factor
\(C_{\beta,N}(Y,Z)\), and the original outgoing modulus halfweight
remain unchanged in this comparison. No division by them occurs.
The cap \(U_{0,N}(w,X)\) does depend on \(a\); its horizontal
transport is a separate source question. Thus (18) alone does not
assert contraction of the complete cap--conditional product or
settle its following affine comparison.
