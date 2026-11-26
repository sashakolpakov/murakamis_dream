# Incoming row estimates on a horizontal complex contour

Research deduction, 7 November 2026. The finite numerator estimate
on the real incoming arc also has a quantitative version at a fixed
complex height. This is useful when moving the entire incoming
contour, since a theorem on the unit circle alone does not control
its displaced horizontal part.

The result concerns the original individual rows and their positive
norms. A cancellation estimate for the sum of those rows is a
separate hypothesis. No numerical evaluation is used.

## 1. Products on a fixed circle

For \(N\ge2\), write
\[
 r=e^{-2\pi i/N},\qquad
 X(x,h)=e^{-2\pi i(x+ih)},\qquad
 p_j(X)=\prod_{k=1}^j(1-r^kX).
 \tag{1}
\]
Fix \(\eta\in(0,1/2)\), \(d_1\ge0\), and a set of indices
\(\mathcal J\subset\{0,\ldots,N-1\}\) satisfying
\[
             d_1+j/N\le1/2-\eta\quad(j\in\mathcal J).
 \tag{2}
\]
The incoming real part ranges over \(x=1/2+d\),
\(0\le d\le d_1\). The height \(h\) is fixed during transport.
Set \(\rho=e^{2\pi h}>0\) and
\[
 \kappa(\rho,\eta)
   =\frac{2\pi\rho}{(1+\rho)^2}
                  \frac{\sin(2\pi\eta)}{1/2-\eta}>0.
 \tag{3}
\]
All factors in (1) are nonzero on this range. In particular (2)
keeps them a fixed angular distance from the first numerator zero
when \(\rho=1\).

**Proposition 1.** For every fixed integer \(m\), every
\(j\in\mathcal J\), and \(0\le d_0\le d_1'\le d_1\),
\[
\begin{split}
&\frac{
 |X(1/2+d_1',h)^{-mj}p_j(X(1/2+d_1',h))|}
 {|X(1/2+d_0,h)^{-mj}p_j(X(1/2+d_0,h))|}\\
&\quad\le
 \exp\left\{-\frac{\kappa(\rho,\eta)}2
 \left[j\big((d_1')^2-d_0^2\big)
       +\frac{j(j+1)}N(d_1'-d_0)\right]\right\}.
\end{split}
\tag{4}
\]
For \(j=0\), this is equality. The estimate is uniform over
any fixed compact range of heights after replacing \(\kappa\)
by its positive minimum there.

*Proof.* The modulus of \(X^{-mj}\) is independent of \(x\).
For one factor, put \(u=d+k/N\). Then
\[
 f_\rho(u)=\log|1+\rho e^{-2\pi iu}|,
 \qquad
 f_\rho'(u)=
 \frac{-2\pi\rho\sin(2\pi u)}
                 {1+\rho^2+2\rho\cos(2\pi u)}.
 \tag{5}
\]
On \(0\le u\le1/2-\eta\), the denominator is positive
and at most \((1+\rho)^2\). Concavity of sine on
\([0,\pi]\) bounds its graph below the chord from zero to
\(2\pi(1/2-\eta)\):
\[
 \sin(2\pi u)\ge
            \frac{\sin(2\pi\eta)}{1/2-\eta}\,u .
 \tag{6}
\]
Consequently
\[
 \partial_d\log|p_j(X(1/2+d,h))|
 \le-\kappa(\rho,\eta)
                 \left(jd+\frac{j(j+1)}{2N}\right).
 \tag{7}
\]
Integrating (7) from \(d_0\) to \(d_1'\) proves (4).
The argument retains every original factor and does not
approximate the product by an integral. \(\square\)

In particular, if \(|h|\le H_*\), a convenient common constant is
\[
 \kappa_*=
 \frac{2\pi e^{2\pi H_*}}{(1+e^{2\pi H_*})^2}
             \frac{\sin(2\pi\eta)}{1/2-\eta}.
 \tag{8}
\]
Indeed \(\rho/(1+\rho)^2\) is unchanged by
\(\rho\mapsto\rho^{-1}\) and decreases for \(\rho\ge1\).
Thus (8) is the minimum of (3) on the stated height range.
Neither \(H_*\) nor \(\eta\) is chosen by a numerical test.

## 2. Positive norms and the original two factors

Assume \(\mathcal J\) is nonempty; all sums below are zero
when it is empty. Let \(z_j\) be the actual row at \(x=1/2+d_0\), including
any factor independent of \(x\). Its row at \(x=1/2+d_1'\)
equals \(D_jz_j\), where \(D_j\) is the exact quotient
appearing before the modulus in (4). For any fixed positive
diagonal weights \(w_j\),
\[
 \sum_{j\in\mathcal J}w_j|D_jz_j|^2
 \le \big(\max_{j\in\mathcal J}|D_j|\big)^2
                         \sum_{j\in\mathcal J}w_j|z_j|^2 .
 \tag{9}
\]
If all retained indices satisfy \(j\ge\alpha N\), with
\(\alpha>0\), (4) implies the simpler bound
\[
 \max_j|D_j|
 \le \exp\left\{-\frac{N\kappa_*}{2}
       \left[\alpha\big((d_1')^2-d_0^2\big)
                    +\alpha^2(d_1'-d_0)\right]\right\}.
 \tag{10}
\]
The same factor bounds the sum of absolute row values.
Weighted Cauchy--Schwarz therefore transports any established
positive norm bound to a linear observation, with its usual
dual norm. It does not compare that observation with its
possibly cancelling value at the initial coordinate.

In the exact cap and conditional factors,
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
               H_N(w,r^{-j})\,p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
               X^{-j}p_j(X)p_j(Y)/P_j^3,\qquad
 P_j=(r;r)_j,
\end{split}
\tag{11}
\]
take \(m=0\) and \(m=1\), respectively. The complete
endpoint coefficient \(H_N\), the outgoing parameter \(Y\),
and all denominators are unchanged. Thus (4) applies to
each retained row on a displaced horizontal incoming contour,
at every level and both parities. It also applies to a
coherently contracted group whose only remaining incoming
dependence is that same numerator and carrier.

Unlike the real-height-zero formula in
[the earlier contraction theorem](research_incoming_finite_row_contraction.md),
the phase of \(D_j\) need not be a linear function of \(j\).
Only its modulus is bounded here. Treating this diagonal
map as a positive map on complex observations would discard
that phase.

## 3. Consequence for a contour deformation

The [local corner identity](research_mixed_half_face_local_corner_cancellation.md)
and the exact Laurent integral permit replacing an incoming
vertical segment followed by a real segment by a displaced
horizontal segment followed by a new vertical segment.
Proposition 1 supplies an exact estimate for the physical rows
in (2) on the new horizontal segment. A bound on their initial
sum of absolute values, or on an appropriate positive norm,
then propagates with the loss in (10).

The established geometric bound at the initial point is a
bound on the complete signed source. It does not automatically
supply either of those stronger initial hypotheses. Moreover
(2) excludes rows approaching or passing the moving numerator
wall. Those rows, the remaining contour contributions from
the internal sums, and the new far vertical segment need
their own estimates. The proposition does not establish the
complete shifted-contour bound or any new filling theorem.
