# Restoring both full edges on the right closing path

Private written deduction, 9 November 2026. The two traced edge
deletions have the required exponential gap on the proposed right
hyperbola. The proof extends the domain of the incoming deletion
using the existing physical-row formula. It does not estimate the
remaining trace with both edges shortened.

## 1. The exact differences

Use the notation and original algebra of
[the integer-crossing deletion theorem](research_all_integer_crossing_edge_deletions.md).
For \(N\ge3\), put \(D=N-1\), \(m=\lfloor N/2\rfloor\),
\(U=m-1\), and
\[
 \mathcal K_N(w,x)=\sum_{j=0}^{D}e_j(w)e_j(x),\qquad
 \mathcal K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x).
\]
Here \(e_j\) are the original Newton polynomials. With the original
trace \(\phi_N\), crossing \(R_N\), and \(z_u=-2\cos u\), define
\[
\begin{aligned}
 Q_{n,N}(w,u)&=\phi_N[R_N^n\mathcal K_N(w,x)\mathcal K_N(x,z_u)],\\
 Q_{n,N}^{<}(w,u)&=\phi_N[R_N^n\mathcal K_N(w,x)\mathcal K_N^<(x,z_u)],\\
 Q_{n,N}^{<<}(w,u)&=\phi_N[R_N^n\mathcal K_N^<(w,x)\mathcal K_N^<(x,z_u)].
\end{aligned}
\tag{1}
\]
Thus \(\Delta^{\rm out}=Q-Q^<\) and
\(\Delta^{\rm in}=Q^<-Q^{<<}\). These are differences of exact
finite traces, including the derivatives at double roots and the
additional simple root at odd levels.

Write \(\psi(u,0)=\Psi_{1/2}(-2\cos u)\) for the calibrated
complete-edge action, where
\[
 \Psi_x(z)=\int_0^x
 2\operatorname{arsinh}\left(\frac{\sqrt{2-z}}2\cot(\pi s)\right)\,ds .
\tag{2}
\]
The branches are principal on \(\mathbb C\setminus[2,\infty)\),
and \(\psi(0,0)=2b_2\), with \(b_2<7/12\).

**Lemma 1.** Uniformly for
\[
 |\Re u|\le2\pi/3,\qquad |\Im u|=K\le7/10,\qquad w\in[-2,2],
\tag{3}
\]
and every signed integer \(n\),
\[
\begin{aligned}
 |\Delta^{\rm in}_{n,N}(w,u)|
   &\le CN^A e^{N\Re\psi(u,0)}
    \le CN^A e^{N(2b_2+K^2/(4\pi))},\\
 |Q_{n,N}(w,u)-Q_{n,N}^{<<}(w,u)|
   &\le CN^A e^{N E(K)},\qquad
 E(K)=2b_2+K/2+K^2/(4\pi).
\end{aligned}
\tag{4}
\]
The constants are independent of \(n\). Every fixed ordinary
incoming derivative satisfies the same estimates with a changed
polynomial factor.

*Proof.* On (3),
\[
 \Re z_u=-2\cos(\Re u)\cosh(\Im u)
       \le\cosh(7/10)<13/10<2 .
\tag{5}
\]
Its spectral image is therefore a fixed compact subset of
\(\Re z<2\). The quantitative physical-row estimate, equation (6)
of the [slit-plane theorem](research_mixed_next_first_short_edge_slit_plane_bound.md),
applies uniformly to every original physical row:
\[
 |F_{a,N}(z_u)|\le CN^A e^{N\Re\Psi_{a/N}(z_u)}
                 \le CN^A e^{N\Re\Psi_{1/2}(z_u)}.
\tag{6}
\]
The second inequality follows from the positive real part of
the principal integrand in (2).

The radical part of the incoming deletion is exactly
\[
 \sum_{r=0}^{m-1}e_{D-r}(w)
       \sum_{a=0}^r b_{ra}R_N(c_a)^nF_{a,N}(z_u),
 \qquad |b_{ra}|\le2 .
\tag{7}
\]
The deletion theorem proves \(|e_{D-r}(w)|\le\sqrt{N-1}\)
on the entire real incoming interval. Also
\(|R_N(c_a)^n|=1\), for either sign of \(n\). Consequently
(6) bounds (7) at the first rate in (4).

At odd levels retain, in addition, the original term
\[
 e_m(w)\left[
  \sum_{a=0}^{m-1}d_{ma}R_N(c_a)^nF_{a,N}(z_u)
        +R_N(-2)^n\mathcal K_N^<(-2,z_u)\right].
\tag{8}
\]
Here \(|e_m(w)|\le1\), \(|d_{ma}|\le2\), and the original
cardinal interpolation of the last shortened kernel has a
polynomially bounded absolute coefficient sum. Applying (6)
to that interpolation proves the same bound for (8).
No row or simple-node contribution has been removed.

For \(0<a<\pi\) and real \(k\),
\[
 \Re\tan((a+ik)/2)=\frac{\sin a}{\cos a+\cosh k}>0 .
\]
Its principal inverse hyperbolic sine also has positive real
part. Hence the original derivative
\(\psi_u=-\pi^{-1}\operatorname{arsinh}(\tan(u/2))\)
shows that \(\Re\psi(a+ik,0)\) decreases as \(a\) increases.
The derivative agrees with (2) by continuation from the central
strip; (5) keeps the entire continuation inside its original
domain. Evenness and conjugation handle the other signs.
On the imaginary axis the existing bound is
\(\psi(iK,0)\le2b_2+K^2/(4\pi)\).
This proves the second incoming inequality.

The outgoing deletion theorem already allows every real outgoing
angle and bounds it by \(CN^A e^{N E(K)}\). Adding it proves
the second line of (4). Finally the exact differences have
ordinary degree at most \(D\) in \(w\), independently of \(n\).
The real-interval Markov inequality proves the derivative
assertion. \(\square\)

## 2. Comparison with the original closing rate

Let \(u_g=\beta_g-iK_g\) be the actual geometric closing point,
and put
\[
 M_g=\Re\{2S(u_g)+iu_g^2/\pi-iu_g\}.
\]
The established height and rate bounds are
\(17/30<K_g<7/10\) and \(M_g>321/100\).
Use the proposed right path
\[
 u(\beta)=\beta-iK(\beta),\qquad
 K(\beta)=\frac{\pi K_g}{2\beta},\qquad
                       \pi/2\le\beta\le2\pi/3 .
\tag{9}
\]
The outer crossing and trace charge have combined rate
\[
 c_{\rm out}(u)=(2\beta/\pi-1)K .
\]
Define the available rate for one inner factor by
\[
 B(u)=\frac{M_g-c_{\rm out}(u)}2 .
\tag{10}
\]
The cancellation of the linear height terms in the following
comparison is exact:
\[
\begin{aligned}
 2E(K)+c_{\rm out}(u)
 &=4b_2+\frac{K^2}{2\pi}+\frac{2\beta K}{\pi}\\
 &=4b_2+\frac{K^2}{2\pi}+K_g\\
 &<\frac73+\frac{49}{600}+\frac7{10}
   =\frac{623}{200}.
\end{aligned}
\tag{11}
\]
We used only \(b_2<7/12\), \(\pi>3\), and \(K\le K_g<7/10\).
As \(M_g>642/200\), equations (10)--(11) give
\[
                         E(K)<B(u)-\frac{19}{400}.
\tag{12}
\]

**Corollary 2.** There is a fixed complex neighborhood of
\([-2,2]\) on which, uniformly on (9), at both parities and
for every signed integer \(n\),
\[
 |Q_{n,N}(w,u)-Q_{n,N}^{<<}(w,u)|
                  \le C e^{N(B(u)-1/25)}.
\tag{13}
\]
Every fixed ordinary incoming derivative satisfies (13) on a
smaller fixed neighborhood.

*Proof.* Apply polynomial continuation from \([-2,2]\) using a
filled Bernstein ellipse of parameter \(\exp(1/400)\).
The degree bound \(D<N\) costs at most \(N/400\) in the
exponent; its finite coefficient count costs a polynomial.
Absorb all polynomial factors using a further \(1/400\).
The remaining margin \(19/400-2/400=17/400\) exceeds \(1/25\).
Cauchy's formula on smaller ellipses proves the derivative claim.
\(\square\)

This gives the required restoration estimate for each inner
factor at \(n=3\). It does not bound \(Q_{3,N}^{<<}\).
For example, once that shortened trace has an upper bound
\(C e^{N(B(u)+\varepsilon)}\) with a fixed
\(\varepsilon<1/25\), the cross terms formed with (13) are
exponentially smaller after the outer factor is attached.
Without such an estimate, the restoration bound alone does
not control the original product or its closing integral.

## Source bindings

- Exact full-trace deletions, including the odd term and all-real
  incoming bounds:
  [integer-crossing deletion theorem](research_all_integer_crossing_edge_deletions.md),
  f7abba0175c558ee9ca7f94799f9cd4d58adc249fea3f6b8c425e55a8136da66.
- Quantitative physical-row profiles and cardinal interpolation:
  [slit-plane theorem](research_mixed_next_first_short_edge_slit_plane_bound.md),
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Actual height localization:
  [geometric height theorem](research_mixed_symmetric_closing_height_below_seven_tenths.md),
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
- The original closing normalization and \(M_g>321/100\):
  [far-right connection theorem](research_mixed_symmetric_closing_right_far_connection.md),
  dd3322925c80e58eaf22af936e5653945532f1b6de6b4044c047d92348211835.
