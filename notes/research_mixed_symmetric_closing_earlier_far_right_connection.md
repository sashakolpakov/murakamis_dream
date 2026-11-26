# Extending the controlled far-right path to angle \(4\pi/5\)

Private written deduction, 9 November 2026. The sharp complete-column
norm improves the starting angle of the far-right estimate from
\(19\pi/20\) to \(4\pi/5\). Unlike the earlier all-real incoming
estimate, this improvement is asserted on fixed neighborhoods of
the complete incoming colors. Those neighborhoods suffice for
the current closing calculation.

Use exactly the full finite functions in
[the far-right connection theorem](research_mixed_symmetric_closing_right_far_connection.md):
\[
\begin{aligned}
 Q_N(w,u)&=\mathbf e(-2\cos u)^T J_NM_N^3\mathbf e(w),\\
 F_N(u;\mathbf w)&=Q_N(w_L,u)Q_N(w_R,u),\\
 G_N(u;\mathbf w)&=\sin u\,F_N(u;\mathbf w)e^{iNu^2/\pi},\\
 W_N(u)&=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2},
              \qquad \eta_N=(-1)^{N-1}.
\end{aligned}
\tag{1}
\]
The original right endpoint is
\[
 a_N=\pi-\frac{2\pi\lfloor N/400\rfloor}{N}
       \ge\pi-\pi/200,
\]
and \(h_c\in(0,1/1000]\) is the fixed positive height chosen in
the original closing identity. Consider the oriented path with
successive vertices
\[
 \Gamma_N:\quad
 4\pi/5-i/100,\quad a_N-i/100,\quad a_N-ih_c .
\tag{2}
\]
Let \(M_g\) retain the original geometric closing rate.

**Theorem.** On sufficiently small fixed complex neighborhoods of
\(w_L=w_R=-2\), at both level parities and all sufficiently large
\(N\),
\[
 \frac{N^2}{\pi}\int_{\Gamma_N}
       |G_N(u;\mathbf w)W_N(u)|\,|du|
                \le C e^{N(M_g-1/50)}.
\tag{3}
\]
Every fixed mixed ordinary incoming derivative satisfies the same
bound on smaller fixed neighborhoods. Equation (3) also bounds
the signed original current, whose additional crossing scalar
has modulus one.

*Proof.* The [complete-column theorem](research_mixed_symmetric_closing_complete_column_norm.md)
gives, for each fixed \(\tau>0\), a fixed incoming disk on which
\[
 \|M_N^3\mathbf e(w)\|_2
       \le C_\tau N^A e^{N(\sigma+\tau)},\qquad
 \sigma=b_2+\lambda_*<\frac7{12}+\frac{175}{216}
                         =\frac{301}{216}.
\tag{4}
\]
The complete Newton-vector bound, which includes every index,
gives
\[
 \|\mathbf e(-2\cos(a-ih))\|_2
       \le CN^B e^{N(m_0(a)+h)}.
\tag{5}
\]
Here the real-period maximum \(m_0\) has derivative
\[
 m_0'(a)=-\pi^{-1}\operatorname{arsinh}(\sin(a/2)),
             \qquad m_0(\pi)=0.
\tag{6}
\]
The positive series proves
\(\sinh(9/10)>9/10+(9/10)^3/6>1\).
Consequently \(\operatorname{arsinh}1<9/10\), and integration
of (6) yields
\[
 m_0(a)\le\frac9{10}\frac{\pi-a}{\pi}
                  \le\frac9{50}\qquad(4\pi/5\le a\le\pi).
\tag{7}
\]

Apply Cauchy--Schwarz to the exact evaluation in (1).
Reversal \(J_N\) preserves the Euclidean norm. The two inner
factors together have rate at most
\(2\sigma+2\tau+9/25+2h\).
The original crossing contributes \(2ah/\pi\), and the
complete sampling factor contributes \(-h\):
\[
 |W_N(a-ih)|
 \le e^{-Nh}(1-e^{-Nh_c})^{-2}\le C e^{-Nh}
                \qquad(h_c\le h\le1/100).
\tag{8}
\]
Thus the full rate on (2), before \(\tau\) and polynomial
allowances, is less than
\[
 \frac{301}{108}+\frac9{25}
                +(1+2a/\pi)h
 \le \frac{301}{108}+\frac9{25}+\frac3{100}
 =\frac{8578}{2700}.
\tag{9}
\]
The established geometric floor is
\[
 M_g>\frac{321}{100}=\frac{8667}{2700}.
\]
The remaining margin is greater than \(89/2700\).
Choose \(\tau=1/1000\) in each column bound and absorb the
polynomial factors, bounded path length, sine, and original
\(N^2/\pi\) using a further \(1/1000\) of exponential rate.
The total spent is \(3/1000\), and
\[
 \frac{89}{2700}-\frac3{1000}>\frac1{50},
\]
since \(89000>62100\). This proves (3). Cauchy's formula
on smaller incoming disks applies to the pointwise integrand
bound before integration and proves the derivative statement.
\(\square\)

The remaining original right current can now be deformed into
a path from \(\pi/2-iK_g\) to \(4\pi/5-i/100\), followed by
(2). This uses holomorphy of the complete integrand below the
real axis; its sampling poles lie on the real line. The
intermediate path still needs an estimate. In particular (3)
does not bridge the region between the proposed hyperbola
ending at real angle \(2\pi/3\) and the start of (2).

## Source bindings

- Complete column and arbitrary small ordinary incoming-disk allowance:
  [complete-column norm](research_mixed_symmetric_closing_complete_column_norm.md),
  4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519.
- Full complex Newton vector:
  [left-far vector estimate](research_mixed_symmetric_closing_left_far_connection.md),
  d02646e7422138c265de9ed1e16749590a8cb2f808b9cf15f30e584627aa6184.
- Exact real maximum and its derivative:
  [real-period theorem](research_three_crossing_real_period_newton_bound.md),
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.
- Original finite current, endpoints, fixed height, and geometric floor:
  [far-right connection theorem](research_mixed_symmetric_closing_right_far_connection.md),
  dd3322925c80e58eaf22af936e5653945532f1b6de6b4044c047d92348211835.
