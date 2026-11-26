# Raw-row stationarity and two fixed rows for minimum transport

Research deduction, 5 November 2026. The complete right-row envelope
has a unique real optimizing row. For the specified hybrid minimum
flow, its directional derivative can be bounded using only rows
\(1/5\) and \(2/5\), while retaining every outer coordinate, reference
height and Fourier branch. This proves no sign for the resulting
whole derivative. A separate exact example explains why coherent
stationarity cannot simply be substituted for real-row stationarity.

## 1. Original branches and the available stationarity

Fix a real right target at \(1/2\), and write its other target
\(z=y+ih\). Let \(\alpha\) be the type-four indicator at \(z\),
\(\epsilon\) the own-factorial indicator, and \(d=1\) when \(z\)
is the first argument. The physical triples are
\[
 (\epsilon,\alpha,d)\in
 \{(0,0,0),(1,1,0),(0,0,1),(0,1,1),(1,0,1),(1,1,1)\}.
 \tag{1}
\]
Use the original normalized primitive
\(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\).
For a permitted selection \(0\le\sigma\le\alpha\), set
\[
\begin{split}
 Q(s,z)&=g(s+1/2)+g(s+z)-(2+\epsilon)g(s)
                    +2\pi i\{dz+(1-d)/2\}s,\\
 F_q(s,z)&=Q(s,z)
       -\left(1+\frac{\alpha-q}{2}\right)g(z)
                           +\pi i(\sigma-q)z,
                  \qquad q\in\{0,\sigma\}.
\end{split}                                                   \tag{2}
\]
Constants independent of \(s,z\) have zero real part and are suppressed.
These are the actual allocated branches on the typed hybrid heights:
unselected type four has \(h\le0\); selected type four has \(h\ge0\).
For a selected endpoint \(q=0\) is the factorial Fourier alternative
with its half-wrap penalty, and \(q=1\) is the forcing alternative.
The real right endpoint's Fourier upper rate is zero and its selected
monomial has modulus one. Thus no original halfweight is removed.

The [complete right-row theorem](research_mixed_complex_right_row_reduction.md)
and [fixed bracket](research_mixed_right_boundary_row_bracket.md) give
\[
 \mathcal R(z)=\max_{q\in\{0,\sigma\}} E_q(z),\qquad
 E_q(z)=\max_{0<u<1/2}\Re F_q(u,z),\qquad
                  1/5<u_*(z)<2/5.                           \tag{3}
\]
All branches have the same unique row \(u_*\), because their differences
are independent of \(u\). The row second derivative is at most
\(-2\pi\). For any differentiable target motion with velocity \(\zeta\),
the ordinary real implicit-function theorem and envelope differentiation
give
\[
 \frac{d}{dt}E_q(z(t))
  =\Re\{K_q(u_*,z)\zeta\},\qquad
 K_q=g'(u+z)-\left(1+\frac{\alpha-q}{2}\right)g'(z)
               +2\pi i d u+\pi i(\sigma-q).                 \tag{4}
\]
There is no \(u_*'\) term, since \(\Re F_{q,s}=0\).
At a Fourier tie, the one-sided directional derivative of \(\mathcal R\)
is the largest derivative of its active branches. Unique row
stationarity does not imply a unique Fourier branch.

## 2. The minimum-flow derivative needs only two fixed rows

Keep the original hybrid contour. There are no collar or early
coordinates in this assertion: all nonright real coordinates are at
least \(.12\), all right coordinates have already been fixed at \(.5\),
and a common current minimum \(t\in[.12,.22]\) is raised.
Let
\[
 R(y)=
 \begin{cases}1,&.12\le y\le.45,\\
 400(.5-y)^2,&.45\le y\le.5.
 \end{cases}                                                \tag{5}
\]
An unselected row affected by the moving minimum has height derivative
\(k=cR(y)/.12\), where \(c=\Im r\), \(|c|\le.057\).
Its actual height satisfies \(|h|\le.057R(y)\).
Selected rows have fixed height \(.014R(y)\); their height derivative
is zero. A selected row that itself moves has \(R(t)=1\), so this
remains true. At a one-sided switching time the following assertions
apply to the corresponding literal height velocities.

**Theorem 1.** Consider the contribution (4) of any affected raw edge.

1. If its A coordinate itself moves, then \(y=t\), its velocity is
   \(1+ik\) with \(|k|\le19/40\), and
   \[
    \Re\{K_q(u_*,z)(1+ik)\}\ge
       \min_{u\in\{1/5,2/5\}}\Re\{K_q(u,z)(1+ik)\}.
    \tag{6}
   \]
2. If only its height moves, the velocity is \(ik\). For \(k\ne0\)
   its contribution is monotone in the row. The minimizing endpoint is
   \[
   \begin{array}{c|cc}
       &k>0&k<0\\ \hline
    d=0&1/5&2/5\\
    d=1&2/5&1/5
   \end{array}                                               \tag{7}
   \]
   and the value there bounds the value at \(u_*\) from below.
   If \(k=0\), the contribution vanishes.

Every Fourier branch is retained in these statements. The estimates
can be summed over the physical edges of a whole minimum-flow derivative,
with all shared outer variables and height coefficients unchanged.
They introduce no independent split of those coefficients and no
additional source tolerance.

*Moving-real proof.* The only row-dependent part of (4) is
\(\Re[(g'(z+u)+2\pi i d u)(1+ik)]\). Its second derivative in \(u\) is
\[
          -\pi^2\Re\{(1+ik)\csc^2\pi(z+u)\}.                \tag{8}
\]
Here \(.32\le y+u\le.62\). Write
\(\tau=\cot\pi(y+u)\tanh\pi h\). The elementary scalar bounds
\[
 |\cot\pi(y+u)|\le\cot(8\pi/25)<2/3,\qquad
 \pi|h|<9/50,\qquad |\tau|<3/25
 \tag{9}
\]
follow from monotonicity of cotangent, its reflection about \(1/2\),
\(|h|\le.057\), and \(\pi<22/7\).
Factoring the sine as
\(\sin\pi(y+u)\cosh\pi h\,(1+i\tau)\), the numerator of the
real part in (8) is
\[
 1-\tau^2+2k\tau
 \ge1-(3/25)^2-2(19/40)(3/25)=2179/2500>0.                \tag{10}
\]
Its denominator is positive. The row contribution is strictly concave,
so its minimum on the closed bracket is at an endpoint. This proves (6).

*Height-only proof.* Differentiating its row contribution once gives
\[
 \frac{d}{du}\Re\{K_q(u,z)ik\}
       =\pi k\{1-2d-\Im\cot\pi(z+u)\}.                     \tag{11}
\]
We claim \(|\Im\cot\pi(z+u)|<1\) on the actual height domain.
Put \(v=y+u\in[.32,.9]\). The exact criterion is
\[
 |\Im\cot\pi(v+ih)|<1
       \quad\Longleftrightarrow\quad
          \cos(2\pi v)<e^{-2\pi|h|}.                       \tag{12}
\]
For \(v\le.75\) its left side on the right of (12) is nonpositive.
Otherwise set \(a=1-v\in[.1,.25)\). The inequality
\(-\log\cos(2\pi a)\ge2\pi^2a^2\) follows by integrating
\(\tan x\ge x\) on \([0,\pi/2)\). It suffices that \(|h|<\pi a^2\).
If \(y\le.45\), then \(a\ge.15\) and
\(.057<\pi(.15)^2\). If \(y=.5-\delta\), \(0\le\delta\le.05\), then
\[
 |h|\le22.8\delta^2,\qquad a\ge.1+\delta,\qquad
 \frac{22.8\delta^2}{(.1+\delta)^2}\le\frac{38}{15}<\pi.
 \tag{13}
\]
Both cases prove (12). Equation (11) now has the signs in (7).
Notice that (12) does not assert a positive real cotangent for the
shifted argument \(z+u\).

At tied minima, a row height changes once if its cyclic neighborhood
meets the moving set; repeated copies in a minimum do not multiply
its velocity. A raw RA or AR edge has only one A endpoint. Count its
one derivative once. Parallel edges in a two-cycle have separate rows
and are each retained. A one-cycle is either wholly raw-right or has
no right boundary, so creates no omitted mixed edge. These observations
justify the stated cyclic scope of (6)--(7). They do not prove that
the resulting sum is positive.

## 3. The real Schur complement and the missing imaginary equation

There is a useful local Hessian identity, but it has a different
meaning from eliminating a complex critical point. At a real optimizing
row write
\[
 F_{ss}=-a+ib,\qquad F_{sz}=-c+id,\qquad F_{zz}=-e+if,
                       \qquad a>0.                         \tag{14}
\]
Here \(d\) in (14) denotes a matrix entry only, not the orientation
indicator. Real maximization of \(\Re F(u,x+ih)\) gives
\[
 E_{xx}=-e+c^2/a,\qquad E_{hh}=e+d^2/a,\qquad
                         E_{xh}=-f+cd/a.                   \tag{15}
\]
On the established typed polygons
\(\Re\cot\pi z\ge0,\ |\Im\cot\pi z|<1/2\), the
[closed-cotangent triangle forms](research_mixed_closed_cotangent_roots.md)
apply with the real inner cotangent \(\cot\pi u>0\).
The nonlinear part of (2) is
\(V(s,z)+V(s,.5)-\epsilon g(s)-(\alpha-q)g(z)/2\),
with \(V(s,z)=g(s+z)-g(s)-g(z)\).
The remaining coefficients are nonnegative, and the chirp has zero
real Hessian. Thus \(\begin{pmatrix}a&c\\c&e\end{pmatrix}>0\);
(15) proves real concavity and height convexity there.
No positivity outside that established cotangent domain is inferred.

The original inner derivative at the raw optimizer has only zero
real part. Its remaining normal force is exactly
\[
 \Im Q_s=
 \Arg(1-e^{-2\pi i(u_*+z)})
 +(1+\epsilon)\pi u_*-\epsilon\pi/2
                         +d\pi(2y-1).                     \tag{16}
\]
The argument is the original regular-strip logarithm. When \(z=y\)
is real, (16) becomes
\[
 \Im Q_s=\epsilon\pi u_*+
            \pi\{(1-\epsilon)/2-y+d(2y-1)\}.               \tag{17}
\]
For \(\epsilon=0\), it is \(+\pi(.5-y)\) in the second-argument
orientation and its negative in the first-argument orientation,
independently of the row. Fourier additions do not change \(Q_s\).
An imaginary inner motion therefore contributes a generally nonzero
term. It cannot be discarded using the real stationarity in (4).

## 4. A minimal counterexample to automatic derivative comparison

Take \(\epsilon=\alpha=\sigma=0\), a real A coordinate \(y\), and
the other endpoint \(1/2\). At \(y=1/2\), the original coherent root
and the real maximizing row both equal \(s=u=1/4\). The original
zero lift follows directly from the regular logarithms. At that point
\[
 F_{ss}=-4\pi,\qquad F_{sy}=-\pi\pm i\pi,\qquad
                         \Re F_{yy}=-\pi,                 \tag{18}
\]
where the sign records the two orientations.
The raw real maximum has second derivative \(-3\pi/4\), by (15).
In contrast the coherent phase eliminates the complex stationary root:
\[
 \Re\left(F_{yy}-\frac{F_{sy}^2}{F_{ss}}\right)=-\pi.
 \tag{19}
\]
Let \(\Delta(y)\) be the raw maximum minus the real part of that
original coherent phase. Both its value and first derivative vanish
at \(1/2\), while
\[
 \Delta''(1/2)=\pi/4,\qquad
 \Delta'(y)=\frac{\pi}{4}(y-1/2)+O((y-1/2)^2)<0
                         \quad\text{just left of }1/2.     \tag{20}
\]
All functions here are smooth on a neighborhood of the displayed
regular point. Thus raw derivatives need not dominate coherent
derivatives, even though all relevant triangle forms are positive.
This is not an obstruction to the low-minimum flow on \([.12,.22]\),
nor a failure of a finite conditional sum. The remaining task is the
sign of its actual whole derivative after the valid reduction (6)--(7).

## 5. Signs of the unselected vertical marginals

**Corollary 2.** Let the A endpoint be unselected on the same hybrid
domain, with \(y\in[.12,.5]\). For either physical own-factorial
indicator, every row \(u\in[1/5,2/5]\), and the two orientations, put
\[
 K^{(d)}=g'(z+u)-(1+\alpha/2)g'(z)+2\pi i d u.
 \tag{21}
\]
Then
\[
 \Im K^{(0)}<0<\Im K^{(1)}.
 \tag{22}
\]
For \(h\le0\), there is also the uniform bound
\[
 \Im K^{(1)}
 \ge\pi\{u-\alpha(.5-y)/2\}\ge\pi/100.
 \tag{23}
\]
Here \(\alpha=1\) permits only nonpositive unselected height.
The case \(h>0\) therefore has \(\alpha=0\).

To prove this, first extend the cotangent cone in (12) to the whole
interval \(v\in[y,y+u]\), not just its last point. The actual hybrid
height obeys
\[
 |h|\le .057 R(y)\rho_{\rm slow}(y).
 \tag{24}
\]
At \(y\in[.12,.22]\), its flat-profile upper bound satisfies the
exact identity
\[
 \frac{19}{16}y^2-\frac{19}{40}(y-.1)
                 =\frac{19}{16}(y-.2)^2\ge0.
 \tag{25}
\]
For \(y\in[.22,.25)\), use instead
\(.057<(19/16)(.22)^2\). Since \(19/16<\pi\), both estimates
give \(|h|<\pi y^2\), which proves the cone at the initial point
by the logarithmic cosine estimate used above. For \(y\ge.25\)
the initial cosine is nonpositive. The endpoint \(y+u\) is already
covered by the proof of Theorem 1. Finally, the maximum of
\(\cos(2\pi v)\) on this interval lies at one of its endpoints:
the interval is contained in \((0,1)\), where the only interior
turning point is the minimum at \(1/2\). This proves
\(|\Im\cot\pi(v+ih)|<1\) throughout the interval.

Use the original continuous argument
\(A(v)=\Arg(1-e^{-2\pi i(v+ih)})\). Its derivative is
\(A'(v)=\pi\{\Im\cot\pi(v+ih)-1\}\).
For \(h<0\), it lies strictly between \(-\pi\) and zero;
for \(h>0\), strictly between \(-2\pi\) and \(-\pi\).
At \(h=0\) it equals \(-\pi\) exactly. If \(h\le0\), radial
monotonicity of the argument in the lower disk also gives
\(0\le A(y)\le\pi(.5-y)\), including \(y=.5\).
Consequently
\[
 \Im K^{(d)}=A(y+u)-A(y)-\alpha A(y)/2+2\pi d u.
 \tag{26}
\]
For \(h\le0\), this proves the first strict sign in (22) and the
lower bound (23). For \(h>0\), use \(\alpha=0\) and the strict
two-sided bounds on \(A'\) to obtain both signs in (22).
The zero-height case follows from the displayed exact derivative;
no strict derivative inequality at zero height is assumed.

Thus the height-only rate \(-k\Im K^{(d)}\) is favorable for
negative \(k\) when the A endpoint is first, and for positive \(k\)
when it is second. The opposite orientations give a negative
contribution; \(k=0\) gives zero. This is a sign for one raw height
term, not a sign for a whole mixed minimum-flow derivative.

## Reproduction

    python3 experiments/check_mixed_raw_row_stationarity.py --precision 320

The checker verifies the original branch bookkeeping, derivative and
Schur identities, exact rational taper bounds, three scalar constants,
the half-endpoint example and the unselected vertical signs. It validates the completed row bracket
and cotangent-domain inputs. It performs no root cover, source-cell
recomputation, or test of a mixed minimum-flow sign.
