# Complete incoming end pieces on the selected left contour

Private research deduction, 8 November 2026. The larger preceding-factor
allowance pays two entire incoming paths, without decomposing their
conditional sums or assuming termination. The initial path has the
explicit fixed length \(1/32\). No mathematical numerical evaluation,
saved-data arithmetic, or frozen-source edit is used.

## 1. Original factors and the conclusion

Retain an actual complete word in the original powers \(3,4\), beginning
\(343\), of length at least five. Use its original ordinary-next reference,
fixed heights, and action \(\mathcal P_0^+\). Put
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
 \tag{1}
\]
The complete first factors are
\[
 U_{0,N}(w,X)=\sum_{j=0}^{D}H_N(w,r^{-j})\,p_j(X)/P_j,\qquad
 C_{1,N}(X,Y)=\sum_{j=0}^{D}
                  X^{-j}p_j(X)p_j(Y)/P_j^3 .
 \tag{2}
\]
Every \(H_N\) remains the original coherent coefficient. On the selected
left contour write
\[
 y=q+i/100,\quad 0\le q\le11/50,\quad
 z=u+i\Im z_*,\quad 3/10\le u\le39/100,\qquad
 R=|Y|=e^{\pi/50},\quad B_f=77/50+\pi/50 .
 \tag{3}
\]
The actual outgoing coordinate is in the interior of this real interval.
There is no outgoing halfweight for this next own-three factor.

Let the two positively oriented real incoming paths be
\[
 I_{\rm in}=[0,1/32],\qquad I_{\rm far}=[7/10,1],
 \qquad
 F_N^I(w,Y)=N\int_I
       U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da .
 \tag{4}
\]

**Theorem 1.** Uniformly on (3), for every real ordinary color
\(-2\le w\le2\), and at all sufficiently large integer levels of either
parity, each \(I=I_{\rm in},I_{\rm far}\) satisfies
\[
 \begin{split}
 &\sup_{a\in I}
 \left|U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)
                     d_N(Y)Y^{-N}C_{0,N}(Y,Z)\right|\\
 &\hspace{15mm}\le CN^B
       e^{N\{\Lambda_{123}(z)-1/2000\}},\\
 &\left|F_N^I(w,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z)\right|
       \le CN^{B'}e^{N\{\Lambda_{123}(z)-1/2000\}} .
 \end{split}
 \tag{5}
\]
The full forced polynomial \(d_N\), all finite indices in both first
factors and the next factor, every numerator zero, and both true ends
are retained. In particular these are bounds for complete incoming
path contributions, not only for physical-index subsets.

## 2. A disk bound on an explicit initial interval

Use the original zero-safe quotient bounds (7), (12), and (16) of
[the complete real initial source](research_mixed_transformed_real_initial_interval.md).
With
\[
 J'(t)=\log(2|\sin\pi t|),\quad J(0)=0,\quad
 L(x)=-2J((1-x)/2),\quad A(x)=L(x)-J(x),
 \tag{6}
\]
they give, for every prescribed positive tolerance \(\tau\),
\[
 \sup_{|Y|\le1}
 |U_{0,N}(w,e^{-2\pi ix})C_{1,N}(e^{-2\pi ix},Y)|
 \le C_\tau N^{B_\tau}
       e^{N\{101/125+2A(x)+7/15+\tau\}},
 \qquad 0\le x\le1/10 .
 \tag{7}
\]
Here \(\tau\) is the sum of the finitely many source tolerances.
This source uses the positive norm of the complete \(H_N\)'s and the
complete conditional sum on the outgoing disk. It includes \(x=0\)
by the exact identity \(p_j(1)=P_j\); it does not continue a regular
factorial symbol through a zero.

Since \(J(1/2)=0\) and \(\log(2\sin\pi t)\le\log2\),
\[
 L(x)=2\int_{(1-x)/2}^{1/2}\log(2\sin\pi t)\,dt
                                  \le x\log2 .
 \tag{8}
\]
Concavity of sine gives \(\sin(\pi t)\ge2t\) for
\(0\le t\le1/2\), hence
\[
 J(x)\ge x\log(4x)-x,\qquad
 A(x)\le x\{1-\log(2x)\}.
 \tag{9}
\]
The right side is increasing for \(0<x\le1/32\), and has continuous
limit zero at \(x=0\). The elementary witness
\[
 e^{7/10}>
 1+\frac7{10}+\frac{49}{200}+\frac{343}{6000}
       =\frac{12013}{6000}>2
 \tag{10}
\]
therefore yields
\[
 A(x)\le\frac{1+\log16}{32}<\frac{19}{160},
 \qquad 0\le x\le1/32 .
 \tag{11}
\]
Consequently the rate in (7), before \(\tau\), is less than
\[
 \frac{101}{125}+\frac{19}{80}+\frac7{15}
       =\frac{9073}{6000}
       =\frac{77}{50}-\frac{167}{6000}.
 \tag{12}
\]
Choose the total tolerance smaller than \(167/12000\). This proves the
complete disk bound
\[
 \sup_{\substack{x\in I_{\rm in}\\ |Y|\le1\\ -2\le w\le2}}
 |U_{0,N}(w,e^{-2\pi ix})C_{1,N}(e^{-2\pi ix},Y)|
                                    \le CN^B e^{77N/50}.
 \tag{13}
\]
Its original all-real-color and endpoint scopes are unchanged.

## 3. The final real arc and continuation to the prescribed height

The complete coherent cap theorem,
[Section 4, equation (22)](research_mixed_next_coherent_cap_far_arc.md),
already proves
\[
 \sup_{\substack{a\in I_{\rm far}\\ |Y|\le1\\ -2\le w\le2}}
 |U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)|
                                    \le CN^B e^{153N/100}.
 \tag{14}
\]
Only this disk-source assertion is used; its later selected comparison,
whose angular domain is different, is not being extended here.

For fixed \(a,w\), the product in (13) or (14) is a polynomial in \(Y\)
of degree at most \(D\). The reciprocal-polynomial maximum principle
therefore gives, on \(|Y|=R\),
\[
 \begin{split}
 |U_{0,N}C_{1,N}|
   &\le CN^B e^{77N/50}R^D\le CN^B e^{NB_f}
                                      &&(a\in I_{\rm in}),\\
 |U_{0,N}C_{1,N}|
   &\le CN^B e^{153N/100}R^D
       \le CN^B e^{N(B_f-1/100)}
                                      &&(a\in I_{\rm far}).
 \end{split}
 \tag{15}
\]
This is an exact finite-polynomial continuation. It does not assume
that the unit-disk bound itself persists outside that disk.

Apply Theorem 1 of
[the selected-left filter-correction theorem](research_mixed_next_three_selected_left_filter_correction.md),
at its frozen hash
\(\texttt{3122492d2d2dbf11a7f04f140525aa0873aefdf1ad2930371c166acf173a83dc}\).
Its preceding-factor allowance is exactly \(B_f\), and its complete
next-kernel conclusion retains both alternatives of the forced weight.
Equation (15) satisfies its hypothesis at every incoming point.
This proves the first estimate in (5). Integration over either bounded
path and its original coefficient \(+N\) proves the second.
No first conditional contour, alias, or connecting side has been
dropped: the whole finite first source was bounded before attachment.

## 4. Exact consequence for the old filtered top remainder

Let \(F_N\) be the original complete prefix, \(F_N^{\rm mid}\) its
unchanged old filtered version, and
\[
 E_N^{\rm filt}=F_N-F_N^{\rm mid},\qquad
 F_N^{\rm rest}=F_N-F_N^{I_{\rm in}}-F_N^{I_{\rm far}}.
 \tag{16}
\]
The prefix's original incoming decomposition contains the two real
paths (4), with those orientations. All its other paths and joins
remain in \(F_N^{\rm rest}\); no new incoming vertical side is introduced.
Define, only on the fixed top contour,
\[
 K_N^{\rm mid}(y)=
       \frac{NF_N^{\rm mid}(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},
 \qquad
 K_N^{\rm rest}(y)=
       \frac{NF_N^{\rm rest}(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N}.
 \tag{17}
\]
The exact identity is
\[
 K_N^{\rm mid}-K_N^{\rm rest}
  =-\frac{N\big(F_N^{I_{\rm in}}+F_N^{I_{\rm far}}-E_N^{\rm filt}\big)
                  d_N(Y)Y^{-N}C_{0,N}(Y,Z)}
                 {1-Y^{-N}} .
 \tag{18}
\]
The denominator is bounded below by \(1/2\) for all sufficiently large
\(N\), since \(|Y|=e^{\pi/50}>1\). The two path terms are paid by (5).
The entire correction \(E_N^{\rm filt}\) is paid by Section 4 of the
cited filter-correction theorem. Thus (18) is pointwise bounded by
\(CN^B e^{N\{\Lambda_{123}(z)-1/2000\}}\).
Both original coefficients \(N\), in the incoming integral (4) and
the meromorphic density (17), remain; they cost polynomial factors.

In particular the increasing top interval \([s,11/50]+i/100\) in the
remaining signed chain may be written with \(K_N^{\rm rest}\), with
an exponentially smaller additive error. Its preceding minus sign
in that chain is unchanged. This statement neither deletes the
remaining first paths nor asserts that their contributions are small.
No separate filter is applied to an incoming path contribution.

The two paths in (4) are fixed and independent of outside parameters.
The proven estimates also apply to fixed subintervals of either path.
No new outside-parameter derivative assertion, full first-prefix
estimate, or complete Fourier-coefficient conclusion is needed here.
The rest of the initial real path, the incoming taper, the central
first path, the right horizontal path, and the combined incoming
corner remain separate source obligations on the selected left contour.
