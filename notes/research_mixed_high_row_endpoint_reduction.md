# Why the upper half of the summation range has no interior maximum

Research proof, 4 November 2026. The conclusion concerns a scalar bound
for the complete finite sum. A comparison with the geometric critical
value is a separate step.

## 1. The row variable and the statement

For a real height \(h\), define
\[
 I_h(u,y)=\int_0^u\log|1-e^{2\pi h-2\pi i(y+s)}|\,ds,
 \qquad J(u)=\int_0^u\log(2\sin\pi s)\,ds .                 \tag{1}
\]
The integrals exist at their logarithmic singularities and are continuous
in all the parameters used below. In the original finite sum, \(u=j/N\)
is the summation index divided by the level. Fix one outer angle at
\(1/2\) with height zero. Let \(y\) and \(h\) be the angle and height
of the other outer variable. The logarithmic upper bound for a row is
\[
 E_{\epsilon,c}(u;y,h)=I_0(u,1/2)+I_h(u,y)
                  -(2+\epsilon)J(u)-2\pi chu,                 \tag{2}
\]
where \(\epsilon=0,1\) distinguishes the two block types. The parameter
\(c=1\) when the other variable is the left argument, and \(c=0\)
when it is the right argument. This keeps the original reciprocal factor
in the finite sum. All Fourier half-weights and the outer supporting
plane are independent of \(u\), and can be added to (2) unchanged.

**Theorem 1.** If
\[
 13/100\le y\le1/2,\qquad |h|\le57/1000,
 \qquad \epsilon,c\in\{0,1\},                               \tag{3}
\]
then
\[
 \max_{1/2\le u\le1}E_{\epsilon,c}(u;y,h)
   =\max\{E_{\epsilon,c}(1/2;y,h),E_{\epsilon,c}(1;y,h)\}.
                                                                  \tag{4}
\]
More precisely, (2) decreases to a unique minimum and then increases
on this interval. In particular, the last summation indices cannot
produce an additional maximum in this part of parameter space.

The theorem is not a statement about \(y<13/100\). The reduction of
small outer angles proved for the lower summation indices does not
automatically apply to the upper indices.

## 2. An algebraic expression for the row derivative

Put
\[
 H=|h|,\quad R=e^{2\pi h},\quad
 t=-\cot\pi u\quad(1/2<u<1),
\]
so \(t\) increases from zero to infinity. Write
\[
 \begin{split}
 a&=2\cosh(2\pi H)-2\cos(2\pi y),\\
 b&=4\sin(2\pi y),\\
 d&=2\cosh(2\pi H)+2\cos(2\pi y),\\
 P(t)&=at^2-bt+d,\qquad Q_\epsilon(t)=t^2P(t)(1+t^2)^\epsilon.
 \end{split}                                                    \tag{5}
\]
Away from a zero in the numerator of the logarithm, direct
differentiation of (1) gives
\[
 \exp(2E'_{\epsilon,c}(u))
  =\frac{Q_\epsilon(t)}{D_{h,c}},
 \qquad D_{h,c}=2^{2+2\epsilon}R^{2c-1}.                       \tag{6}
\]
For completeness, the squared modulus from the other angle is
\[
 |1-Re^{-2\pi i(y+u)}|^2
 =\frac{R\{at^2-bt+d\}}{1+t^2}.
\]
The squared modulus from the half-period angle is
\(4t^2/(1+t^2)\), whereas
\((2\sin\pi u)^{4+2\epsilon}
 =2^{4+2\epsilon}/(1+t^2)^{2+\epsilon}\).
These identities prove (6), including its power of \(R\).
Both possible thresholds satisfy
\[
 D_{h,c}\ge D_-(H):=2^{2+2\epsilon}e^{-2\pi H}>0.              \tag{7}
\]

## 3. A compact inequality and the large-\(t\) argument

The following compact inequality is verified with outward interval
arithmetic by the accompanying program:
\[
 \boxed{\quad Q_\epsilon(t)<D_-(H)
       \quad\hbox{or}\quad Q_\epsilon'(t)>0\quad}              \tag{8}
\]
for \(0<t\le\cot\pi y\), throughout (3). To make the domain compact
without a variable boundary, set \(t=w\cot\pi y\), \(0\le w\le1\).
The interval calculation covers the entire rectangular box
\[
 (y,H,w)\in[13/100,1/2]\times[0,57/1000]\times[0,1].            \tag{9}
\]
It accepts a cell only if its full interval enclosure proves the first
strict inequality in (8), or proves strict positivity of
\(Q_\epsilon'(t)/(2t)\). The latter expression extends polynomially
to \(t=0\). Its formulas are
\[
 \begin{split}
 B_0(t)&=2at^2-\tfrac32bt+d,\\
 B_1(t)&=B_0(t)(1+t^2)+t^2P(t).
 \end{split}                                                    \tag{10}
\]
At \(t=0\), the first inequality in (8) always holds. Thus positivity
of \(B_\epsilon\) is only used to infer positivity of
\(Q_\epsilon'\) for \(t>0\).

There is an elementary proof beyond this compact interval. Indeed,
\[
 P(t)=(2\cosh(2\pi H)-2)(1+t^2)
              +4(\sin\pi y\,t-\cos\pi y)^2.                  \tag{11}
\]
For \(t>\cot\pi y\), this expression is positive and strictly
increasing. It follows that \(Q_\epsilon'(t)>0\) there.
This also treats \(y=1/2\), when \(\cot\pi y=0\). At the common
boundary \(t=\cot\pi y\), a possible zero of (11) has
\(Q_\epsilon=0<D_-\); any point with \(Q_\epsilon\ge D_-\)
is already covered by (8).

Combining (8) and (11), we have proved
\[
 t>0,\ Q_\epsilon(t)\ge D_-(H)
       \quad\Longrightarrow\quad Q_\epsilon'(t)>0.           \tag{12}
\]
Since \(Q_\epsilon(0)=0\), and \(Q_\epsilon(t)\to+\infty\),
each level \(D\ge D_-\) is crossed exactly once. To see uniqueness
without assuming global monotonicity of \(Q_\epsilon\), note that
its derivative is strictly positive wherever its value is at least
\(D_-\). After an upward crossing it therefore cannot return to
that level. Existence follows from continuity. Applying this to
\(D=D_{h,c}\) in (6) proves the decrease and increase asserted in
Theorem 1.

If \(h=0\), the factor at \(u=1-y\) may vanish. There
\(Q_\epsilon=0\) and the logarithmic derivative tends to
\(-\infty\) from both sides. This point lies before the unique
level crossing. Continuity of the integrals in (1) shows that it
does not interrupt their decrease or introduce a maximum. The
endpoints \(u=1/2,1\) follow by continuity as well. This proves
(4).

## 4. The retained last-row value and the finite sum

Integration over a complete period gives
\[
 I_h(1,y)=2\pi h_+,\qquad I_0(1,1/2)=J(1)=0,
 \qquad h_+=\max(h,0).
\]
For \(R<1\), the first identity follows by integrating the convergent
Fourier series of \(\log|1-Re^{-2\pi is}|\). For \(R>1\), factor
out \(R\) and apply the same argument to \(R^{-1}\). The value at
\(R=1\) follows by integration of the logarithmic singularity.
Consequently the endpoint in (4) is explicitly
\[
                    E_{\epsilon,c}(1;y,h)=2\pi(h_+-ch).       \tag{13}
\]
It must still carry its actual Fourier half-weight and supporting-plane
terms. Replacing the upper indices by this endpoint does not mean
deleting the last rows.

The uniform finite-product bound in the
[whole-period source estimate](research_mixed_boundary_strip_bounds.md)
bounds each original row by a polynomial factor times the exponential
of (2), with its independent factors restored. There are at most \(N\)
rows. Equation (4) therefore bounds the absolute sum of all rows with
\(j/N\ge1/2\) by the larger of the two retained endpoint exponents,
up to a polynomial factor and the already allowed arbitrarily small
Fourier rate error. It applies at both parities and both orientations.
No cancellation between rows is used.

## 5. Reproduction

Run
```sh
python3 experiments/certify_mixed_high_row_endpoint_reduction.py
```
The script checks the algebra in (6), (10), and (11), and subdivides
(9) along its three coordinates in cyclic order. Every accepted box
proves one of the strict inequalities used in (8). Its output records
all subdivision addresses. Prefix disjointness and the exact equality
of their dyadic volumes to one establish complete coverage, separately
for each \(\epsilon\). The saved record binds the proof and script
contents by their hashes. This is a certificate for Theorem 1; it is
not a certificate for a geometric gap or a knot volume theorem.
