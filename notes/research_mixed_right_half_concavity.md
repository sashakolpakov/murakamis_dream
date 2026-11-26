# Concavity of the interior row and angle problem on the right half-period

Research proof, 4 November 2026. This is a reduction of the exterior
estimate. It does not prove that the full exterior integral is smaller
than the geometric contribution.

## 1. The part of the finite-source envelope under consideration

Write
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \quad J(u)=\Re g(u),\quad
 I_h(u,y)=\int_0^u\log|1-e^{2\pi h-2\pi i(y+t)}|\,dt .
 \tag{1}
\]
The logarithm and dilogarithm have the original branches on
\(0<\Re z<1\). Consider one outer angle fixed at \(1/2\), with
height zero. The other angle is \(y\), its height is \(h\), and
\(u=j/N\) is the row fraction in the complete conditional finite sum.
The [right-half source reduction](research_mixed_right_half_source_reduction.md)
gives the product exponent
\[
 I_0(u,1/2)+I_h(u,y)-(2+\epsilon)J(u),
 \qquad \epsilon\in\{0,1\}.
 \tag{2}
\]
We shall work on
\[
 0<u<1/2,\qquad 13/100\le y\le1/2,\qquad
 |h|\le57/1000.                                                \tag{3}
\]
The exclusion of the other rows and angles is a separate task.
Throughout the interior of (3), \(0<u+y<1\), so
\[
 I_h(u,y)=\Re\{g(u+y+ih)-g(y+ih)\}.
 \tag{4}
\]
The identity extends continuously to the boundary, including the
integrable zero at \(u+y=1,h=0\).

Allow a real term \(\ell(u,y,h)\) that is affine in \((u,y)\)
for each fixed height and affine in \(h\) for each fixed \((u,y)\).
This includes the original factor \(-2\pi hu\), the real and
imaginary terms of a fixed complex supporting plane, and the
selected-alias factor. For \(q=0,1\), put
\[
 E_q(u,y;h)=I_0(u,1/2)+I_h(u,y)-(2+\epsilon)J(u)
                   -\frac q2\Re g(y+ih)+\ell(u,y,h).            \tag{5}
\]
The parameter \(q\) records which Fourier expression is being used;
it is independent of the own block type \(\epsilon\). The term
\(-\Re g\) is the reciprocal-factorial exponent.

## 2. A strict concavity theorem

**Theorem 1.** For every fixed height in (3), each function (5) is
strictly concave in \((u,y)\). For every fixed \((u,y)\) in the
interior, it is strictly convex in \(h\).

*Proof.* Set \(z=y+ih\) and
\[
 V(u,z)=g(u+z)-g(u)-g(z).
\]
Since \(g''(z)=\pi\cot(\pi z)-\pi i\), write
\[
 U=\cot(\pi u)>0,\qquad P+iQ=\cot(\pi z).
\]
Here \(P\ge0\), with equality only when \(y=1/2\).
Moreover \(|Q|<1\). Indeed
\[
 |Q|=\frac{\sinh(2\pi|h|)}
             {\cosh(2\pi h)-\cos(2\pi y)}<1
\]
follows from
\[
 \cos(13\pi/50)<e^{-57\pi/500}
       \le e^{-2\pi|h|}.
 \tag{6}
\]
The first inequality is an outward scalar comparison; the focused
checker below verifies it.

Put \(C=\Re\cot(\pi(u+z))\). The real negative Hessian of \(V\),
divided by \(\pi\), is
\[
 \begin{pmatrix}U-C&-C\\-C&P-C\end{pmatrix}.
\]
The cotangent addition formula gives, with
\(D=(U+P)^2+Q^2>0\),
\[
 U-C=\frac{(U+P)(U^2+1)}D>0,\qquad
 UP-(U+P)C=\frac{(U+P)^2-U^2Q^2}D>0.                           \tag{7}
\]
Thus this Hessian is positive definite, also when \(P=0\).

Using (4), the nonlinear part of (5) is
\[
 \Re V(u,z)+J(1/2+u)-J(1/2)
            -(1+\epsilon)J(u)-\frac q2\Re g(z).               \tag{8}
\]
The extra second derivative in \(u\) is
\[
 \pi\{\cot(\pi(1/2+u))-(1+\epsilon)\cot(\pi u)\}<0.
\]
The extra second derivative in \(y\) is \(-q\pi P/2\le0\).
There are no new mixed derivatives. Equation (7) proves strict
joint concavity.

For height convexity, the \(z\)-dependent part of (5) is the real
part of a holomorphic function. Its second \(h\)-derivative is
the negative of its second \(y\)-derivative. The remaining terms
are independent of \(h\), or affine in \(h\); the affine term
\(\ell\) also has zero second \(y\)-derivative. Consequently
\[
                         (E_q)_{hh}=-(E_q)_{yy}>0.             \tag{9}
\]
This proves the second assertion. \(\square\)

## 3. Keeping the actual two Fourier expressions

Let \(\beta\in\{0,1\}\) indicate whether the other leg has a Fourier
weight. Its actual upper exponent is
\(\max\{-\Re g(y+ih),2\pi h_+\}\), where \(h_+=\max(h,0)\).
After allocating half of this weight to the block, the complete
envelope on (3) is
\[
 \mathcal E(u,y;h)
 =I_0(u,1/2)+I_h(u,y)-(2+\epsilon)J(u)+\ell(u,y,h)
       +\frac\beta2\max\{-\Re g(y+ih),2\pi h_+\}.              \tag{10}
\]
It is the maximum of \(E_\beta\) and \(E_0+\beta\pi h_+\).
Each of these is convex in height, so (10) is convex in height.
For any closed interval \([h_{\min},h_{\max}]\subset[-.057,.057]\),
\[
 \sup_{\substack{0\le u\le1/2\\13/100\le y\le1/2\\
                  h_{\min}\le h\le h_{\max}}}\mathcal E(u,y;h)
 =
 \max_{h\in\{h_{\min},h_{\max}\}}\ 
 \sup_{\substack{0\le u\le1/2\\13/100\le y\le1/2}}
                         \mathcal E(u,y;h).                  \tag{11}
\]
This reduction does not discard the Fourier forcing term or an
intermediate height. In an application, the Fourier-envelope estimate
must of course be available on the chosen height interval; the actual
negative heights and the selected height \(+.014\) lie in the already
proved interval.

The maximum of two concave functions need not be concave. Accordingly,
at each endpoint height we maximize the two expressions separately:
\[
 \sup\mathcal E=\max\{\sup E_\beta,\ \sup(E_0+\beta\pi h_+)\}.
 \tag{12}
\]
No assumption about which Fourier expression is larger at a trial
point is needed.

## 4. A practical upper certificate

For either expression in (12), choose any interior trial point
\(p=(p_u,p_y)\). Concavity proves, on the entire rectangle
\(D=[0,1/2]\times[13/100,1/2]\),
\[
 E_q(v;h)\le E_q(p;h)+\nabla E_q(p;h)\cdot(v-p).
 \tag{13}
\]
The boundary values follow by continuity. In particular, an upper
bound for the right side is
\[
 E_q(p;h)
 +|\,\partial_uE_q(p;h)\,|\max\{p_u,1/2-p_u\}
 +|\,\partial_yE_q(p;h)\,|
                     \max\{p_y-13/100,1/2-p_y\}.              \tag{14}
\]
A numerical optimizer can propose \(p\); an outward evaluation of
the value and the two derivatives makes (14) a certificate. No
numerical assertion of convergence or stationarity is a premise.
The same bound is uniform over a reference-parameter cell when the
supporting-plane coefficients and the quantities in (14) are enclosed
over that whole cell.

This replaces a grid over the two source variables by a value and
gradient estimate. Reference parameters still require their own
cover, and the rows and angles outside \(D\), as well as right angles
different from \(1/2\), still require separate estimates. Nothing
here establishes a global exterior gap or a new knot volume theorem.

## 5. Reproduction

    python3 experiments/check_mixed_right_half_concavity.py

The checker verifies (7), the Hessian decomposition, and the strict
scalar inequality (6). The passage from these identities to (11)--(14)
is the written concavity argument above.
