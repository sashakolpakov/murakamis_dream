# A bound on the left end of the internal wire period

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

This note estimates the mixed source on the segment
\(0\le\Re x\le7/100\), at the imaginary height of the geometric
critical point. The outer Newton index is kept real and is summed
over its original finite range. Only the complete-meridian trace
angle is moved. Thus the proof needs three two-dimensional phase
bounds, with no outer-wire lattice corrections.

## 1. Statement and notation

Use the exact mixed source from
[the local packet theorem](research_internal_pair_three_mixed_packet.md):
\[
 W_{3,N}(x,u)
    =\phi_N[R^3\mathbf B_N(x)K_N(\,\cdot\,,u)].
 \tag{1}
\]
Here \(\mathbf B_N(x)\) is the full Fourier interpolation of the
Newton basis, \(K_N\) is the original edge kernel, and \(\phi_N\)
is the trace including the first derivatives at repeated roots.
The analytic representative of \(\mathbf B_N(x)\) at the physical
values and their first derivatives is
\[
 B_N(x,t)=
 \frac{N}{
  G_N(N(1/2-x+t/(2\pi))-1/2)
  G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{2}
\]
The equality at these full jets, rather than an off-spectrum
polynomial identity, is what is used in (1).

Let \((x_*,y_*,t_*)\) be the selected critical point of the local
packet theorem. Put
\[
 Y=\Im x_*,\qquad
 M=\Re\{b(x_*,t_*)+b(y_*,t_*)+b(y_*,0)
                       +3it_*^2/(4\pi)-it_*\}.
 \tag{3}
\]
The same cubic enclosure as in that theorem fixes these constants.
For orientation, \(Y\simeq0.0908105744\) and \(M\simeq1.2637824383\).
Define
\[
 A=\frac7{100},\quad h=\frac{13}{20},\quad T=\frac{39}{20},
 \qquad \alpha=\frac1{32},\quad\beta=\frac{15}{32}.
 \tag{4}
\]

**Theorem 1.** There are constants \(C,p,\rho>0\), independent of
\(N\) and \(a\), such that for all sufficiently large integer levels,
\[
 \boxed{\qquad
 \sup_{\substack{0\le a\le A\\ |u|\le\rho}}
       |W_{3,N}(a+iY,u)|
       \le C N^p e^{N(M-1/200)}.
 \qquad}
 \tag{5}
\]
Both level parities are included. The estimate is for the original
full trace, not for one term of a formal asymptotic expansion.

## 2. Reduction to the right endpoint

The factorial phase is
\[
 b(x,t)=-J(1/2-x+t/(2\pi))
        -J(1/2-x-t/(2\pi))-2J(x),
 \qquad J'(z)=\Log(2\sin\pi z).
 \tag{6}
\]
Its normalization and continuations are those of the local packet
theorem. For \(x=a+iY\), \(0\le a\le A\), and
\(t=\tau-iv\), \(|\tau|\le T\), \(0\le v\le h\), the two
shifted factorial arguments in (6) have positive real parts.
The argument \(x\) has fixed positive imaginary part, including
when \(a=0\), so it encounters no zero or branch cut.

**Lemma 2.** Throughout this rectangle,
\[
              \partial_a\Re b(a+iY,t)>0.
 \tag{7}
\]

*Proof.* Put \(C_x=\cos(2\pi x)\), \(K=\cos t\). Differentiation
of (6) gives
\[
 \partial_a\Re b(x,t)=
                 \log\frac{|C_x+K|}{|1-C_x|}.
 \tag{8}
\]
The denominator does not vanish because \(Y>0\). The difference
of the two squared moduli is
\[
 \mathcal D=|K|^2-1+
                      2\Re\{C_x(1+\overline K)\}.
 \tag{9}
\]
Write \(s=\sinh v\). The following strict inequalities are
certified from the algebraic enclosure of \(Y\):
\[
 \begin{gathered}
 \cos(2\pi a)\ge9/10,\qquad
 0\le\sin(2\pi a)\le9/20,\\
 \cosh(2\pi Y)>8/7,\qquad
 \sinh(2\pi Y)<5/8,\\
 \cos\tau>-2/5,\qquad \cosh v<5/4.
 \end{gathered}
 \tag{10}
\]
The first two follow from their endpoint values at \(A\);
the last two follow from \(T,h\).
In particular \(1+\cos\tau\cosh v>1/2\), so it is legitimate
to use the positive lower bound on
\(\cos(2\pi a)\cosh(2\pi Y)\) in (9).
Since \(|K|^2-1=s^2-\sin^2\tau\), we obtain
\[
 \begin{split}
 \mathcal D
 &\ge s^2-1+\frac{72}{35}
                \left(1-\frac25\sqrt{1+s^2}\right)-\frac9{16}s\\
 &\ge \frac{41}{175}+\frac{103}{175}s^2-\frac9{16}s\\
 &\ge \frac{1843727}{18457600}>0.
 \end{split}
 \tag{11}
\]
The second line uses \(\sqrt{1+s^2}\le1+s^2/2\), and the
last line is the exact minimum of the quadratic on the real line.
Equation (8) proves the claim. \(\square\)

Thus every retained contour bound is reduced to \(x=A+iY\).
This includes both folded angular connectors, without choosing
different maximizing values of \(a\) on different parts of a
contour.

For real \(t\in[0,\pi]\), the continued factorial rate also obeys
\[
 \partial_t\Re b(a+iY,t)
    =\frac1{2\pi}
       \log\frac{|\cos(\pi(a+iY)+t/2)|}
                     {|\cos(\pi(a+iY)-t/2)|}\le0.
 \tag{12}
\]
At \(a=0\) equality is allowed. At \(a>0\) the inequality is
strict, since the difference of the squared numerator and
denominator is \(-\sin(2\pi a)\sin t\).
Beyond the positive-real-part factorial strip this uses the
continued lower branch, as in the
[uniform factorial estimate](research_uniform_factorial_and_boundary_decay.md).
There is no reset of a principal dilogarithm. Equations (7) and
(12) consequently imply the two bounds needed on physical rows:
\[
 \begin{split}
 \Re b(a+iY,t)&\le\Re b(A+iY,0)
                                      &&(-\pi\le t\le\pi),\\
 \Re b(a+iY,t)&\le\Re b(A+iY,T)
                                      &&(T\le|t|\le\pi).
 \end{split}
 \tag{13}
\]

## 3. Three certified rectangles

For a real outer-wire coordinate \(y\), define
\[
 F_x(y,t)=b(x,t)+b(y,t)+b(y,0)
                         +\frac{3it^2}{4\pi}-it.
 \tag{14}
\]
The outward certificate proves
\[
 \begin{array}{ll}
 \Re F_{A+iY}(y,\tau-ih)\le M-1/100,
       &\alpha\le y\le\beta,\quad -T\le\tau\le T,\\
 \Re F_{A+iY}(y,T-iv)\le M-1/100,
       &\alpha\le y\le\beta,\quad 0\le v\le h,\\
 \Re F_{A+iY}(y,-T-iv)\le M-1/100,
       &\alpha\le y\le\beta,\quad 0\le v\le h.
 \end{array}
 \tag{15}
\]
These are interval bounds on full rectangles, not estimates at a
grid of sample points. The argument of the fixed factor \(B_N(x,t)\)
stays in its ordinary factorial strip. The moving outer-wire
factorials use the upper or lower side determined by
\(\Im t\); the reciprocal-factorial estimate includes the
points where their arguments reach zero.

The same certificate verifies the physical tail estimates
\[
 \begin{split}
 \Re b(A+iY,0)+2g(\alpha)&<M-1/100,\\
 \Re b(A+iY,T)+\psi(T,0)&<M-1/100,
 \end{split}
 \qquad g(y)=J(2y)-4J(y).
 \tag{16}
\]
The two rates on the left are approximately \(0.867013\) and
\(1.215889\). The comparison uses their rigorous enclosures.
The estimate involving \(\psi(T,0)\) is the summandwise
[real outer-angle bound](research_terminal_real_angle_tail.md),
which applies because \(\pi/2<T<2\pi/3\). It does not use a
complex asymptotic for a bare edge kernel.

## 4. Applying the bounds to the finite source

First retain only the original outer-wire indices with
\(\alpha\le j/N\le\beta\). The low-index complete Hermite
bounds give rate \(g(j/N)\) for each outer Newton factor.
Since \(g(1/2-y)=g(y)\), their omitted low-index product has
rate at most \(2g(\alpha)\). The high-index physical values
and first normals are polynomially bounded. Equation (13)
bounds the additional fixed interpolation factor, with
polynomial cost for its derivatives. Hence the first line
of (16) removes the entire discarded outer-wire sum before
any contour is introduced.

This derivative bound is uniform in \(a\): on real trace angles,
the arguments of the fixed factor have imaginary parts bounded
away from zero by \(Y\). Uniform factorial estimates and Cauchy
disks of radius \(O(1/N)\) therefore give polynomial derivative
cost. At the physical angles near zero the even Taylor expansion
handles the change from angular to spectral derivatives. No
simple-root formula is substituted for a repeated-root trace.

Next remove the physical trace rows with \(|t|\ge T_N\), where
\(T_N=T+O(N^{-1})\), \(T_N\ge T\), is an angular midpoint.
The retained outer kernel has the real-interval upper rate
\(\psi(T,0)\); its spectral derivative has the same rate by
Markov's inequality, since it is a degree-at-most-\(N-1\)
polynomial. The second line of (13) bounds the fixed factor
and its derivatives. The second inequality in (16) therefore
controls every removed row, including its first normal.

For the remaining source, apply the exact trace contour to
the even holomorphic function
\[
 f_N(t)=B_N(a+iY,t)
          \sum_{\alpha\le j/N\le\beta}
                   e_j(-2\cos t)e_j(-2).
 \tag{17}
\]
Use the horizontal segment at height \(-h\), with endpoints
\(\pm T_N-ih\). The full rational trace kernel on this segment
is bounded by a constant times \(e^{-Nh}\). This is exactly
the modulus of the unit-charge factor \(e^{-iNt}\) already
included in (14). In the finite outer sum each \(j/N\) is
real, so the first rectangle in (15) bounds each summand;
summing at most \(N\) terms costs only a power of \(N\).

The upper half of the angular endpoint contribution is folded
by \(t\mapsto-t\). The two lower connectors are
\(t=\pm T_N-iv\), \(0\le v\le h\). Their exact weight satisfies
\[
                       \frac1{4\cosh^2(Nv/2)}\le e^{-Nv}.
 \tag{18}
\]
The other two rectangles in (15) thus bound the full endpoint
contribution. The outer wire has never been replaced by an
integral; there are no wire endpoint terms or wire aliases to
estimate. At \(v=0\) the weight in (18) is regular, so no
separate small-height decomposition is required.

The strict bounds persist for the \(O(1/N)\) midpoint displacement.
All phase rates are uniformly continuous on the compact rectangles,
including their moving-zero faces, and the finite reciprocal-factorial
bounds are uniform there. The inequalities in (10) have strict
margins, so the monotonicity proof also persists for the slightly
enlarged angular interval.

Finally, take a sufficiently small fixed complex disk in \(u\).
For retained \(y\in[\alpha,\beta]\), the parent arguments
\(1/2-y\pm u/(2\pi)\) stay in the positive strip, so the phase
perturbation in (14) tends uniformly to zero as \(u\to0\).
For the discarded finite sums, the full interval Newton bounds
and polynomial continuation in the parent variable cost at most
\(e^{N|\Im u|}\). The real outer-angle argument applies uniformly
to the parent factors before that continuation. Shrinking the
disk, and allowing for midpoint displacement, leaves the common
gap \(1/200\). The trace prefactors, finite sums, and contour
lengths have only polynomial cost. This proves (5).
\(\square\)

## 5. Reproduction and scope

Run

~~~sh
python3 experiments/certify_internal_pair_three_low_wire_complement.py
~~~

The [checker](../experiments/certify_internal_pair_three_low_wire_complement.py)
uses the already enclosed cubic root and the audited Arb rectangle
engine. It checks all six inequalities in (10), the exact rational
minimum in (11), both physical tail bounds, and the three contour
rectangles. The
[saved certificate](../repro/results/research-internal-pair-three-low-wire-complement.json)
records 897 visited boxes: 633 for the horizontal rectangle, 175
for the positive connector, and 89 for the negative connector.

The theorem removes the displayed left-hand segment from the
full internal-wire period at the geometric exponential rate.
It supplies no estimate for the other portions of that period.
