# A two-wire real bound with cap radius (3/100)

Research proof, 4 November 2026. Frozen manuscripts and completed
source artifacts are unchanged.

This strengthens the real-period estimate for the actual L40 retained
vertex. Both input and output distances enter one global maximization;
their two losses are not added from separate one-wire estimates.

## 1. Exact source and theorem

Let
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 c=2\mathcal J(5/6),\qquad
 d_{03}(z)=\min\{\operatorname{dist}(z,\mathbb Z),3/100\}.
 \tag{1}
\]
The distance is on the real Fourier circle. Keep the original source
\(\widetilde V_N^{(40)}=h(x)^T(JM^3-E_{40})h(y)\), with
\(E_{40}=M^TP_{\lfloor N/40\rfloor}JM P_{\lfloor N/40\rfloor}M\).

**Theorem 1.** Uniformly for all real \(z,w\), at both level parities,
\[
 \sum_{\mathrm{retained}}|\mathrm{original\ summand}|
 \le CN^b\exp N\left[
 2c-\frac32\{d_{03}(z)^2+d_{03}(w)^2\}\right],
 \qquad x=x_h+z,\quad y=x_h+w.
 \tag{2}
\]
Every subset of real retained indices satisfies the same upper bound.
Every fixed wire derivative costs only a polynomial factor. No
nonzero leading coefficient or complex-height extension is inferred.

## 2. Global index exclusion

Put \(\xi=1/6+z\), \(\eta=1/6+w\), and define
\[
 f(u)=\log|1-\tfrac12e^{2\pi iu}|,\qquad
 I(s,\xi)=\int_0^s f(\xi-u)\,du .
 \tag{3}
\]
The original full-cardinal real envelope is
\[
 E(s,t,\xi,\eta)=\log2+\mathcal J(s+t)
                  -(s+t)\log2-I(s,\xi)-I(t,\eta).
 \tag{4}
\]
The finite retained indices lie in
\(s,t\ge0\), \(s+t\le1\), \(\max(s,t)\ge1/40\).
The [original global wire theorem](research_three_vertex_global_wire_bound.md)
proves that minimizing the two denominator intervals gives the unique
unweighted maximum at \(s=t=1/3\), with value \(2c\).
The original phase calibration and cardinal factors are retained in (4).

Maximize instead
\[
 P=E+\frac32\{d_{03}(\xi-1/6)^2+d_{03}(\eta-1/6)^2\}.
 \tag{5}
\]
The total added weight is at most \(27/10000=.0027\), and
the homogeneous point still has value \(2c\).

For \(1/40\le p=s+t\le1/3\), the original denominator
inequality \(I(s,\xi)\ge-s\log2\) gives
\[
 P\le\log2+\mathcal J(p)+\frac{27}{10000}
 \le\log2+\frac{\log(\pi/20)-1}{40}+\frac{27}{10000}<2c.
 \tag{6}
\]
Indeed \(\mathcal J\) has only a minimum at \(1/6\) in this
interval. The bound at \(p=1/40\) follows by integrating
\(\log(2\sin\pi u)\le\log(2\pi u)\), and the other endpoint
\(\mathcal J(1/3)=-c/3\) is smaller. The upper expression in
(6) is below \(.624573\).

For the remaining indices use
\[
                              Q=[13/50,2/5]^2.
 \tag{7}
\]
The unweighted envelope after minimizing both denominator intervals
has negative index Hessian
\[
 \operatorname{diag}(d_1,d_2)+k\mathbf1\mathbf1^T,
 \quad
 d_i=\frac{(\pi/2)\sin(\pi s_i)}{5/4-\cos(\pi s_i)},
 \quad k=-\pi\cot\pi(s+t).
 \tag{8}
\]
On (7), \(k>0\) and \(d_i>3/2\). The latter expression
decreases for \(s_i\in[.26,.40]\), and its value at \(.40\)
exceeds \(3/2\). The exact homogeneous critical pair is at
distance at least \(1/15\) from every face of (7).
Consequently the unweighted loss at each exit from (7) is strictly
greater than
\[
 \frac34\left(\frac1{15}\right)^2=\frac1{300}
                     >\frac{27}{10000},
 \qquad \frac1{300}-\frac{27}{10000}=\frac{19}{30000}.
 \tag{9}
\]
Strict concavity on \(s+t>1/2\) extends this loss beyond that
boundary. The already established smaller-index variation raises
every unweighted value with \(1/3\le s+t\le1/2\) to the
boundary \(s+t=1/2\), which lies outside (7). Explicitly, the
ratio giving that derivative is
\(\sin\pi(s+t)/|1-\tfrac12e^{\pi i s_i}|>1\) when
\(s_i\le1/4\); its squared numerator is at least \(3/4\)
and its squared denominator is at most \(5/4-\cos(\pi/4)<3/4\).
This comparison uses the unweighted majorant and the maximum total
weight; it does not assert that (5) increases with the wire phases fixed.
Thus every global maximum of (5) has \((s,t)\in Q\).

## 3. Both wire phases and the exact joint Hessian

For indices in (7), both minimizing interval centers lie in
\[
                     s/2,t/2\in W=[13/100,1/5].
 \tag{10}
\]
The interval integral \(I(s,\xi)\) increases with circular
distance from \(s/2\) up to distance \(1/2\). Each input phase
outside \(W\) may therefore be projected toward its own center
to the first endpoint of \(W\), decreasing its denominator integral.
The clipped weight is unchanged along this projection, since
\([1/6-.03,1/6+.03]\) lies strictly inside \(W\). Apply the
same argument separately to the other wire. Hence every maximum
lies in the full rectangle \(Q\times W^2\).

There put
\[
 D_x=-f'(\xi-s)>0,\quad D_y=-f'(\eta-t)>0,\quad
 C_x=f'(\xi)>3,\quad C_y=f'(\eta)>3.
 \tag{11}
\]
The first two signs follow from
\(s-\xi,t-\eta\in[.06,.27]\subset(0,1/2)\).
For the other two, use
\[
 f'(u)=\frac{\pi\sin(2\pi u)}{5/4-\cos(2\pi u)}.
 \tag{12}
\]
It decreases on \([.13,.20]\), and its value at \(.20\)
exceeds 3. This is twice the endpoint value of \(d_i\) used in
(8), so the two required endpoint inequalities are the same.

On each smooth part of the clipped weights, the exact negative
Hessian of (5) is the quadratic form
\[
 \begin{split}
 -d^2P={}&k(ds+dt)^2+D_x(ds-d\xi)^2+D_y(dt-d\eta)^2\\
       &+(C_x-\omega_x)d\xi^2+(C_y-\omega_y)d\eta^2,
                  \qquad \omega_x,\omega_y\in\{0,3\}.
 \end{split}
 \tag{13}
\]
Here \(\omega=3\) on a quadratic segment and zero on a constant
segment. Every coefficient needed for positive definiteness is
strictly positive. At each clipping face the first derivative
jumps down. Thus \(P\) is strictly concave on \(Q\times W^2\),
including all intersections of clipping faces.

The homogeneous point
\((s,t,\xi,\eta)=(1/3,1/3,1/6,1/6)\) is inside the
quadratic region and is an exact stationary point: the unweighted
gradient vanishes and both added gradients are zero. Its value is
\(2c\). The global exclusions and strict concavity therefore prove
\(\max P=2c\). Subtracting the two weights gives the exponent in (2).

Finally the original finite product estimates, including both
factorial endpoints, differ from (4) by at most \(O(\log N)\)
uniformly over all retained rows and both real Fourier phases.
Every denominator stays bounded away from zero at radius \(1/2\).
The literal cardinal factors and finite products have fixed derivatives
bounded by powers of \(N\) times their moduli. Summing the at most
\(N^2\) actual terms proves (2), with its subset, derivative, and
parity assertions. \(\square\)

## 4. Reproduction and scope

The [focused checker](../experiments/check_three_vertex_two_wire_large_cap_bound.py)
and [record](../repro/results/research-three-vertex-two-wire-large-cap-bound.json)
verify the endpoint inequalities, exact joint Hessian identity,
global exclusion budget and clipping intervals. No numerical
maximization or new root certificate is needed.

```sh
python3 experiments/check_three_vertex_two_wire_large_cap_bound.py --precision 192
```

Both wires in this theorem have exactly the homogeneous imaginary
height. A complex-height bound must use its own joint argument;
it cannot be obtained by simply adding a separate height cost to (2).
The result strengthens the real envelopes in source preparation,
but does not establish any unverified entrance attachment.
