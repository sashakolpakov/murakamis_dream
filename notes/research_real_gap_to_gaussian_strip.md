# From a real angular gap to a Gaussian complex-strip bound

Research lemma, 2 November 2026.

The long-filling theorem asks for a bound quadratic in the
imaginary boundary angles. A whole-period estimate on real
angles, together with the local holomorphic asymptotic at
the complete angle, implies that bound. The only additional
input is a degree bound for the exact finite polynomial.

This note records the implication explicitly. The extension
away from the complete angle is an elementary application
of the maximum principle, equivalently a Poisson majorant.
It does not require an estimate for the coefficients of
the polynomial.

## 1. Hypotheses

For each \(N\), let
\[
 B_N(\mathbf t)=p_N(-2\cos t_1,\ldots,-2\cos t_r),
 \tag{1}
\]
where \(p_N\) is a polynomial of separate degrees
\(D_{j,N}\le d_jN\), for fixed \(d_j\ge0\).
Suppose there are constants \(c,C>0\), \(A\in\mathbb R\),
and \(M\in\mathbb R\), independent of \(N\), such that
\[
 |B_N(\mathbf x)|
 \le CN^A\exp N\left\{
    M-c\sum_{j=1}^r(1-\cos x_j)\right\}
 \qquad(\mathbf x\in\mathbb R^r).
 \tag{2}
\]
Suppose also that on a fixed complex neighborhood of zero,
\[
 B_N(\mathbf t)=\epsilon_N N^\alpha a(\mathbf t)
        e^{NF(\mathbf t)}(1+E_N(\mathbf t)),
 \qquad |\epsilon_N|=1,\quad
 \sup|E_N|\le C/N.
 \tag{3}
\]
Here \(a,F,E_N\) are holomorphic, the functions \(a,F\)
are independent of \(N\), and
\[
 \operatorname{Re}F(\mathbf0)=M,\qquad
 F'(\mathbf0)=0,\qquad
 -\operatorname{Re}F''(\mathbf0)\ \hbox{is positive definite}.
 \tag{4}
\]
In the intended applications, separate evenness gives
\(F'(\mathbf0)=0\) and a diagonal Hessian. Diagonality is
not needed for this lemma. A nonzero amplitude is needed
in the subsequent asymptotic theorem, but not for the
upper bound proved here.

**Theorem.** There are constants \(b,c_0,C_0,C_1>0\) and
\(A_1\in\mathbb R\) such that
\[
 \boxed{
 |B_N(\mathbf x+i\mathbf y)|
 \le C_1N^{A_1}
 \exp N\left\{
   M-c_0\sum_j(1-\cos x_j)+C_0\sum_j y_j^2
 \right\}}
 \tag{5}
\]
for all \(|x_j|\le\pi\), \(|y_j|\le b\), and all
sufficiently large \(N\). Thus the Gaussian strip
hypothesis of
[the complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md)
follows from (1)--(4).

## 2. An exact linear strip estimate

First, (1)--(2) alone imply, for every real \(\mathbf x,\mathbf y\),
\[
 \begin{split}
 |B_N(\mathbf x+i\mathbf y)|
 \le CN^A\exp N\left\{
  M-c\sum_j(1-e^{-|y_j|}\cos x_j)
                  +\sum_j d_j|y_j|\right\}.
 \end{split}
 \tag{6}
\]
To prove this, choose
\(\sigma_j=\operatorname{sgn}y_j\), with either sign
allowed if \(y_j=0\), and put
\[
 \zeta_j=e^{i\sigma_jt_j}.
 \]
Then \(|\zeta_j|=e^{-|y_j|}\le1\).
The Laurent polynomial for \(B_N\), expressed using these
variables, becomes an ordinary polynomial \(Q_N\) after
multiplication by \(\prod_j\zeta_j^{D_{j,N}}\).

Consider the holomorphic function on the closed polydisk
\[
 Q_N(\boldsymbol\zeta)
                 \exp\left(-Nc\sum_j\zeta_j\right).
 \tag{7}
\]
On its distinguished boundary, all \(|\zeta_j|=1\).
The monomial multiplier has modulus one, and the real
angles of \(B_N\) differ at most by signs. Equation (2)
therefore bounds the modulus of (7) by
\[
 CN^A e^{N(M-cr)}.
 \]
Apply the maximum modulus principle one coordinate at a
time. Restoring the exponential and the monomial gives
(6), because
\(\operatorname{Re}\zeta_j=e^{-|y_j|}\cos x_j\).
Zeros of \(B_N\) cause no problem in this proof; no
logarithm of that polynomial has been taken.

Since \(1-e^{-v}\le v\) for \(v\ge0\), a useful consequence is
\[
 |B_N(\mathbf x+i\mathbf y)|
 \le CN^A\exp N\left\{
 M-c\sum_j(1-\cos x_j)
                  +\sum_j(d_j+c)|y_j|\right\}.
 \tag{8}
\]
The linear imaginary cost in (8) is used only where a
fixed real gap is already available.

## 3. The local quadratic estimate

Write
\[
 F''(\mathbf0)=-\mathsf A+i\mathsf B,
 \]
with real symmetric matrices and \(\mathsf A\) positive
definite. Let \(a_*>0\) be its least eigenvalue. The real
part of the quadratic term at \(\mathbf t=\mathbf x+i\mathbf y\)
is
\[
 -\frac12\mathbf x^T\mathsf A\mathbf x
 +\frac12\mathbf y^T\mathsf A\mathbf y
                    -\mathbf x^T\mathsf B\mathbf y.
 \tag{9}
\]
Young's inequality bounds this above by
\[
 -\frac{a_*}{4}|\mathbf x|^2+
 \left(\frac{\|\mathsf A\|}{2}
             +\frac{\|\mathsf B\|^2}{a_*}\right)|\mathbf y|^2.
 \tag{10}
\]
After shrinking a fixed neighborhood of zero, the Taylor
remainder is at most
\((a_*/8)(|\mathbf x|^2+|\mathbf y|^2)\) in absolute value.
Consequently, for some \(C_2\),
\[
 \operatorname{Re}F(\mathbf x+i\mathbf y)
 \le M-\frac{a_*}{8}|\mathbf x|^2+C_2|\mathbf y|^2.
 \tag{11}
\]
The amplitude and relative error in (3) are uniformly
bounded on a smaller neighborhood. Since
\(1-\cos x_j\le x_j^2/2\), equations (3) and (11)
imply (5) there with any \(c_0\le a_*/4\),
after increasing the polynomial prefactor if necessary.

## 4. Combining the two regions

Choose a fixed \(\delta>0\) so that the local estimate
applies whenever \(|x_j|\le\delta\) and
\(|y_j|\le\delta\). On the complementary real set,
at least one \(|x_j|\ge\delta\), and hence
\[
 c\sum_j(1-\cos x_j)\ge
             \gamma:=c(1-\cos\delta)>0.
 \tag{12}
\]
Choose \(b\le\delta\) sufficiently small that
\[
 b\sum_j(d_j+c)\le\gamma/2.
 \tag{13}
\]
Equation (8) then gives
\[
 |B_N(\mathbf x+i\mathbf y)|
        \le CN^A e^{N(M-\gamma/2)}
 \tag{14}
\]
on this complement, for \(|y_j|\le b\).
Since \(\sum_j(1-\cos x_j)\le2r\), any
\[
 0<c_0\le\min\{a_*/4,\ \gamma/(4r)\}
 \]
makes (14) no larger than the right-hand side of (5).
Combine this with the local bound. Taking
\(A_1\ge\max(A,\alpha)\) and increasing constants
completes the proof.

## 5. Application to the adjacent pair

The exact adjacent-pair boundary polynomial has degree
at most \(N-1\) in \(-2\cos u\). The local stationary
action in the
[complete boundary theorem](research_adjacent_two_crossing_boundary_theorem.md)
has
\[
 F''(0)=-\frac{\sqrt7+3i}{8\pi},
 \tag{15}
\]
as proved in
[the adjacent-pair calculation](research_adjacent_two_crossing_pair.md).
Its real part is strictly negative.

The boundary theorem supplies both the local expansion
(3) and the whole-real-period bound (2). No additional
contour theorem is needed merely to replace a linear
imaginary-angle cost by a quadratic one. The theorem above
supplies precisely that step.

This implication requires both full-source inputs.
An expansion of an isolated saddle and a real
estimate for only part of the source do not satisfy
(2)--(3).
