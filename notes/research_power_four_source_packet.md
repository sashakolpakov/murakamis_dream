# A full original power-four packet at the alternating reference

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The exact symmetric two-index source permits a direct contour proof
for the full original power-four vertex near the validated alternating
three/four reference. The real-index complement, every index side and
every alias are retained. No corner is deleted.

## 1. Statement and original normalization

Use \(V_{4,N}(x,y)=h(x)^TJM^4h(y)\) and the notation of the
[exact finite-source theorem](research_power_four_finite_source.md).
Let \(x_0=x_{34}\), \(K=e^{2\pi ix_0}\),
\(Z_0=2K/(1-K)\), and \(z_0=\Log Z_0/(2\pi i)\).
For \(X=e^{2\pi ix}\), \(Y=e^{2\pi iy}\), put
\[
 \begin{split}
 F(s,t;x,y)&=J(s+t)-J(s)-J(t)-i\pi st
                +s\Log X+t\Log Y-I_X(s)-I_Y(t),\\
 I_X(s)&=\frac{\operatorname{Li}_2(Xe^{-2\pi is})
                            -\operatorname{Li}_2(X)}{2\pi i}.
 \end{split}
 \tag{1}
\]
The sine primitive \(J\) and logarithms retain the original
interpolation branches. Near \((x_0,x_0)\), let
\((S(x,y),T(x,y))\) be the holomorphic critical branch with
\(S(x_0,x_0)=T(x_0,x_0)=z_0\), and write
\[
 \Phi_4(x,y)=F(S,T;x,y)-\pi i(x+y),\qquad
 H_4(x,y)=F''_{s,t}(S,T;x,y).
 \tag{2}
\]

**Theorem 1.** There is a fixed complex neighborhood of
\((x_0,x_0)\) on which the full original kernel satisfies
\[
 V_{4,N}(x,y)=\kappa^2 N^{-1/2}a_4(x,y)e^{N\Phi_4(x,y)}
                                      \{1+O(N^{-1})\}
 \tag{3}
\]
along both level parities. The coefficient is holomorphic and
nonzero. Explicitly, with \(U=e^{-2\pi iS}\), \(V=e^{-2\pi iT}\),
\[
 a_4(x,y)=\frac{2\pi e^{\pi i(x+y)}}{\sqrt{\det(-H_4)}}
 \frac{\sqrt{\sin\pi(S+T)/(2\sin\pi S\sin\pi T)}}
      {\sqrt{(1-X)(1-XU)(1-Y)(1-YV)}}.
 \tag{4}
\]
The roots in the second fraction are inherited from the exact
factorial and denominator expansions. The determinant root is
the Gaussian branch in the accretive matrix domain. The normalized
error and every fixed wire derivative are uniform after shrinking
the neighborhood. Moreover \(\Phi_4\) equals the selected original
power-four angular action \(\Xi_4\), with its absolute constant.

This is a local parameter theorem for a full original vertex kernel.
It does not yet assemble arbitrary mixed words or their complete
boundary sources.

## 2. A whole-rectangle Hessian bound

Set
\[
 A=\frac15,\quad B=\frac{21}{50},\quad
 h_-=-\frac{11}{200},\quad h_+=\frac3{200},\qquad
 \mathcal R=[A,B]+i[h_-,h_+].
 \tag{5}
\]
On a neighborhood of \(\mathcal R^2\), the three factorial
arguments \(s,t,s+t\) have real parts strictly between zero and
one. At the reference, \(|K|e^{2\pi h_+}<7/10\), so the
two exact denominator interpolants are nonzero as well.

**Lemma 2.** At \(X=Y=K\),
\[
                 -\Re F''_{s,t}\succ\frac14 I_2
                          \quad\hbox{on }\mathcal R^2.
 \tag{6}
\]
The same holds, with a slightly smaller constant, on a fixed
neighborhood in the two wire parameters.

*Proof.* Write \(p=\cot\pi s=a+ib\),
\(q=\cot\pi t=c+id\), and
\(C=\Re\cot\pi(s+t)\). Direct differentiation gives
\[
 -\Re F''/\pi=
       \operatorname{diag}(a,c)-C\begin{pmatrix}1&1\\1&1\end{pmatrix}
       +\operatorname{diag}\left(
       \frac{-2\Im(Xe^{-2\pi is})}{|1-Xe^{-2\pi is}|^2},
       \frac{-2\Im(Ye^{-2\pi it})}{|1-Ye^{-2\pi it}|^2}\right).
 \tag{7}
\]
The last diagonal is positive. Indeed
\(\pi/5<\arg K<2\pi/5\) and \(A\le\Re s,\Re t\le B\)
put the two rotated arguments strictly between \(-\pi\) and zero.

Throughout the rectangle \(a,c>6/25\). If
\(\Re(s+t)\ge1/2\), then \(C\le0\), and the first two
terms in (7) are bounded below by \((6/25)I_2\).
Otherwise both real indices belong to \([1/5,3/10]\). The
elementary trigonometric bounds recorded in the checker give
\[
 \frac23<a,c<\frac75,\qquad
 |b|/a,\ |d|/c<\gamma:=\frac{36}{95},\qquad
 \frac{|ad-bc|}{a+c}<\zeta:=\frac{252}{475}<1.
 \tag{8}
\]
For example, \(\sin(2\pi\Re s)\ge\sin(2\pi/5)>19/20\)
and \(\sinh(11\pi/100)<9/25\) give the ratio bound;
\(ac/(a+c)<7/10\) then gives the last bound.

The exact cotangent addition formula yields
\[
 \frac{ac}{a+c}-C
   =\frac{(a+c)^2-(ad-bc)^2}
          {(a+c)\{(a+c)^2+(b+d)^2\}}
   >\delta:=\frac{1-\zeta^2}{(14/5)(1+\gamma^2)}.
 \tag{9}
\]
If \(C\ge0\), the determinant of
\(D=\operatorname{diag}(a,c)-C\mathbf1\mathbf1^T\)
is greater than \((a+c)\delta\), while its trace is at most
\(a+c\). It is positive definite and
\(\lambda_{\min}(D)>\delta\). If \(C<0\), its lower
bound follows directly from its positive diagonal. The strict
scalar comparisons \(\pi\delta>1/4\) and
\(6\pi/25>1/4\) prove (6). Compactness gives the parameter
extension. \(\square\)

The exact stationary exponent equations are
\[
 e^{F_s}=\frac{X(1-UV)}{(1-U)(1-XU)},\qquad
 e^{F_t}=\frac{Y(1-UV)}{(1-V)(1-YV)}.
 \tag{10}
\]
At the reference, \(U=V=Z_0^{-1}\) satisfies both equations.
The checker encloses the actual logarithmic gradients in the
zero strip \(|\Im F_s|,|\Im F_t|<\pi\); their exponentials
are exactly one, so both gradients vanish. Also
\(.284<\Re z_0<.285\) and \(-.043<\Im z_0<-.042\).
Lemma 2 proves nondegeneracy and the asserted holomorphic critical
branch. It gives strict concavity on each horizontal real-index
plane and separate convexity in each imaginary index coordinate.

## 3. All complementary pieces of the original sum

The [real-complement theorem](research_power_four_real_complement.md)
proves, for the full original finite sum, an absolute upper rate
\(841/1000\) outside \([1/5,2/5]^2\). The complement of the
larger rectangle \([A,B]^2\) is a subset of that region, and
the theorem permits arbitrary subsets. At the reference the selected
full action satisfies
\[
                         \Re\Phi_4>\frac{4281}{5000}=.8562.
 \tag{11}
\]
Thus the entire real-index complement has a strict exponential gap,
including factorial ends and both level parities.

The [outward contour certificate](../repro/results/research-power-four-index-contours.json)
checks all sixteen products of sides of \(\partial\mathcal R\),
covering them by 183 exact rational rectangles at 256-bit precision.
With \(F_c=F(z_0,z_0;x_0,x_0)\), it proves
\[
 \begin{array}{ll}
 \Re(F_c-F)>1/200,&\text{if at least one side is vertical},\\
 \Re(F-F_c)<1/25,&\text{if both sides are horizontal}.
 \end{array}
 \tag{12}
\]
Each accepted box is a full interval or a derivative mean-value
enclosure, not a sampled inequality. The record retains the full
binary subdivision for independent replay. The bounds are strict,
so they persist on a fixed neighborhood in \((x,y)\), with slightly
smaller gaps, and under the actual \(O(N^{-1})\) half-grid shifts
of the vertical cuts.

When one coordinate is on a vertical side and the other has any
intermediate height, separate imaginary convexity from Lemma 2
reduces its upper bound to the two horizontal heights in (12).
Thus every vertical joining integral in the deformation to the
critical horizontal plane is strictly smaller. Also the maximum
principle in each complex index gives
\(\Re(F-F_c)<1/25\) on all of \(\mathcal R^2\).

Take each real cut at a midpoint between consecutive index nodes.
The exact lattice kernel is \(N\pi\cot(\pi Ns)\), with residue
one at every enclosed node. On the upper and lower horizontal sides,
subtract its respective constant limits \(-i\pi N\) and
\(i\pi N\). The remaining kernels are bounded by a polynomial
times \(e^{-2\pi N h_+}\) and \(e^{-2\pi N|h_-|}\).
On a vertical midpoint side, the cotangent is bounded by one in
modulus. Applying this identity in both indices writes the exact
central lattice sum as its zero Fourier term plus vertical currents
and terms containing at least one of the two decaying horizontal
kernels. By (12), every latter term has a strict gap, because
\[
                     2\pi h_+-\frac1{25}>\frac1{20}.
 \tag{13}
\]
The lower horizontal gap is larger. Tensor products with vertical
sides are controlled by the first line of (12). No alias or side
is omitted. The zero Fourier term has its original coefficient
\(N^2\) times the ordinary two-dimensional index integral.

## 4. The selected coefficient and the absolute phase

On the whole index rectangle the exact interpolation of a summand
in the symmetric finite source has the uniform symbol
\[
 T_N(s,t)=N^{-1/2}g(s,t;X,Y)e^{NF(s,t;x,y)}
                                     \{1+O(N^{-1})\},
 \qquad
 g=\frac{\sqrt{\sin\pi(s+t)/(2\sin\pi s\sin\pi t)}}
          {\sqrt{(1-X)(1-Xe^{-2\pi is})(1-Y)(1-Ye^{-2\pi it})}}.
 \tag{14}
\]
This follows directly from the three exact sine-factorial
interpolants and the two exact denominator interpolants. It matches
the original summands on the lattice before any approximation.
All factors in (14) are nonzero on a fixed neighborhood.

Move the zero Fourier integral to heights \(\Im S,\Im T\).
Every joining side has already been bounded. Lemma 2 makes its
critical point the unique maximum on this real two-plane; ordinary
holomorphic stationary phase gives
\[
 N^2\int T_N(s,t)\,ds\,dt
  =N^{1/2}\frac{2\pi g(S,T)}{\sqrt{\det(-H_4)}}
                          e^{NF(S,T)}\{1+O(N^{-1})\}.
 \tag{15}
\]
The strict complementary gaps justify extending the Gaussian
locally and give a relative error of order \(N^{-1}\).
Multiplication by the original outside factor
\[
 \kappa^2Nc_xc_y
 =\kappa^2N^{-1}e^{-N\pi i(x+y)}e^{\pi i(x+y)}
                                      (1-X^N)(1-Y^N)
 \tag{16}
\]
proves precisely (3)--(4). All contours and gaps persist on a fixed
complex parameter neighborhood; Cauchy's formula proves the stated
fixed derivatives of the normalized error.

For the action identification, let \(W\) be the selected simple
root of
\[
 XYW^2+(X+Y)W+1-XY=0,
 \qquad
 U=\frac{1-X}{1+X(W+1)},\quad
 V=\frac{1-Y}{1+Y(W+1)}.
 \tag{17}
\]
Direct substitution gives (10). The zero lifts at the reference
select the same branch, and the two wire derivatives satisfy
\[
 e^{(\Phi_4)_x}=-\frac{X^2+WX+1}{(X-1)^2},\qquad
 e^{(\Phi_4)_y}=-\frac{Y^2+WY+1}{(Y-1)^2}.
 \tag{18}
\]
Their actual logarithmic lifts equal the original angular ones:
at the reference they are exactly the expressions checked in the
[exterior phase proof](research_exterior_crossing_phase.md), and
then equality continues locally. Thus \(d\Phi_4=d\Xi_4\).

The additive constant is also zero. Use the same connected
diagonal crescent and marked continuation from Section 5 of that
proof. There \(S=T=z=\Log(2K/(1-K))/(2\pi i)\), and all
three factorial arguments \(z,z,2z\) remain in their regular
strips. The index equations keep their zero lifts by connectedness.
The angular primitive and its logarithmic equation are holomorphic
there by the cited cut-exclusion proof. On its specified approach
to \(K=-1\), \(z\to1/2\), \(I_{-1}(1/2)=-i\pi/8\),
and (1) gives \(F\to i\pi\). The outside phase
\(-\pi i(x+y)\to-i\pi\), so \(\Phi_4\to0\), just as
\(\Xi_4\to0\). The constant vanishes, completing the proof.

Reproduce the contour bounds with
`python3 experiments/certify_power_four_index_contours.py` and the
independent real-complement bounds with
`python3 experiments/check_power_four_real_complement.py`.
Their scopes distinguish the finite inequalities from the written
all-level contour and coefficient argument.
