# Cancellation is needed at the middle boundary color as well

Private phase and finite-source deduction, 8 November 2026.
The inner action at outgoing angle \(\pi/2\) exceeds the proposed
outer observation budget. Consequently an absolute bound on the
physical inner values cannot close the outer estimate even after
the small outgoing angles have been removed. This is a statement
about an absolute majorant, not a lower bound for the signed outer
sum. No numerical evaluation is used.

## 1. The original action and the comparison to be proved

Keep the original phase, its additive constant, and its selected
critical point from
[the cubic continuation](research_mixed_next_inner_three_cubic_continuation.md):
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,
 \qquad S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u).
 \tag{1}
\]
Write \(t_*(\pi/2)=a_*-iH\), where
\(0<a_*<\pi/2\) and \(1/2<H<1\). The budget in the original
outer Casimir observation is
\[
                       B_f=\frac{77}{50}+\frac{\pi}{50}.
 \tag{2}
\]

**Proposition.** With these original normalizations,
\[
                         s(\pi/2)>B_f+\frac1{50}.
 \tag{3}
\]

The action is that of the inner sum; (3) does not compare a knot
volume with \(B_f\).

## 2. The height gain of the second edge

For \(t=\pi/2-ih\), \(0\le h\le1\), put
\[
 c=\cos(t/2),\qquad C=1/\sqrt2,\qquad
 A=c^2=\frac{1+i\sinh h}{2},\qquad
 D=A+C^2-AC^2=\frac{3+i\sinh h}{4}.
 \tag{4}
\]
The principal roots and returns here are exactly those of
[the positive-horizontal phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md).
In particular,
\[
              \psi_{tt}(t,\pi/2)=-\frac{C}{2\pi c\sqrt D}.
 \tag{5}
\]

We give a uniform real-part bound rather than a Taylor expansion
with an unspecified remainder. The written bound \(\cosh1<8/5\)
in that phase theorem implies
\[
 |c|^2=\frac{\cosh h}{2}<\frac45<1,
 \qquad |D|^2=\frac{8+\cosh^2h}{16}<\frac{33}{50}<1.
 \tag{6}
\]
Moreover
\[
 0\le\arg c=\arctan(\tanh(h/2))<\pi/6.
 \tag{7}
\]
Indeed \(\tanh(h/2)\le\tanh(1/2)<1/2<1/\sqrt3\).
Since \(D=(1+A)/2\), with \(A\) in the first quadrant,
\(0\le\arg\sqrt D\le\arg c\). It follows that
\[
 0\le\arg(c\sqrt D)<\pi/3,
 \qquad
 \Re\frac{C}{c\sqrt D}>
             \frac12 C>\frac13.
 \tag{8}
\]
All inequalities include \(h=0\), where the relevant real parts
are strictly positive.

Set \(f(h)=\Re\psi(\pi/2-ih,\pi/2)\). Equations (5)--(8) give
\[
                 f''(h)=-\Re\psi_{tt}(\pi/2-ih,\pi/2)
                                  >\frac1{6\pi}.
 \tag{9}
\]
The real phase has real first derivatives on the real square, so
\(f'(0)=0\). Integrating twice proves
\[
 \Re\psi(\pi/2-iH,\pi/2)
       >\psi(\pi/2,\pi/2)+\frac{H^2}{12\pi}
       >\frac{50}{63}+\frac{7H^2}{264}.
 \tag{10}
\]
The last step uses \(\pi<22/7\) and the original real-corner
bound in the action-floor theorem. The extra positive term is
the height gain that its earlier lower bound did not need.

## 3. Comparing the two-edge action with the outer budget

The adopted
[action-floor theorem, Section 1, equations (5)--(6)](research_mixed_next_inner_three_action_floor_and_top_rows.md)
proves, with the same first edge,
\[
 \Re\psi(\pi/2-iH,0)>\frac{239}{250}+\frac{7H^2}{72}.
 \tag{11}
\]
The horizontal maximum property in the phase theorem gives
\(s(\pi/2)\ge\Re\Phi(\pi/2-iH,\pi/2)\). The crossing and
original trace charge at that point have real part \(-H/4\).
Together with (10)--(11), this yields
\[
 s(\pi/2)>
 \frac{239}{250}+\frac{50}{63}+\frac{49H^2}{396}-\frac H4.
 \tag{12}
\]
The quadratic on the right decreases for \(0\le H\le1\):
its derivative is at most
\(49/198-1/4=-1/396\). Therefore
\[
 s(\pi/2)>
 \frac{239}{250}+\frac{50}{63}+\frac{49}{396}-\frac14
 =\frac{19}{12}+\frac{853}{63000}+\frac7{264}.
 \tag{13}
\]
Since \(B_f<561/350\), subtracting this upper bound from (13)
leaves
\[
 \frac7{264}-\frac{377}{63000}>\frac1{50}.
 \tag{14}
\]
For an explicit rational check of the final comparison,
\(7/264-1/50=43/6600\), and
\(43\cdot63000>377\cdot6600\).
This proves (3) without evaluating a critical root or a period.

## 4. A corresponding term in the original outer sum

Put \(m=\lfloor N/2\rfloor\), \(U=m-1\),
\(\theta=\pi/N\), and retain the exact outer nodes
\[
 c_j=2\cos((2j+1)\theta),\qquad
 u_j=\pi-(2j+1)\theta.
 \tag{15}
\]
The original outer observation of the inner polynomial is
\[
 \mathcal L_N(P)=\sum_{j=0}^U\beta_{j,N}P(c_j)Q_N(u_j),
 \qquad
 \beta_{j,N}=(-1)^{U+j}
 \frac{s_{2j+1}S_U^2}{S_{U-j}S_{U+j+1}}R_N(c_j)^3,
 \tag{16}
\]
where \(s_k=2\sin(k\theta)\),
\(S_k=\prod_{a=1}^ks_a\), and \(|R_N(c_j)|=1\).
These are the unchanged coefficients in
[the short-kernel operator transport](research_mixed_next_short_kernel_outer_operator_transport.md).

The reflection \(S_kS_{N-1-k}=N\) simplifies their moduli to
\[
 |\beta_{j,N}|=
 \begin{cases}
       \sin u_j,&N=2m,\\[1mm]
       \sin u_j\sin(u_j/2)/\cos^2(\theta/2),&N=2m+1.
 \end{cases}
 \tag{17}
\]
In the even case the denominator in (16) is \(N\) and
\(S_U^2=N/2\). In the odd case it is \(N/s_{m-j}\),
\(S_U^2=N/(4\cos^2(\theta/2))\), and
\((m-j)\theta=u_j/2\). These identities prove (17) at every
eligible node without a continuum replacement of its weight.

Choose
\[
                  j_N=\left\lceil\frac{N-2}{4}\right\rceil.
 \tag{18}
\]
For all sufficiently large levels, \(j_N\le U\) and
\(\pi/2-2\pi/N<u_{j_N}\le\pi/2\). Thus these are among
the actual double nodes of the
[physical-outgoing theorem](research_mixed_next_inner_three_physical_outgoing_packet.md).
That theorem and the continuity of its nonzero coefficient give
\[
 |Q_N(u_{j_N})|\ge cN^{-3/2}e^{N s(\pi/2)}.
 \tag{19}
\]
Here the bounded derivative of \(S\) near \(\pi/2\) changes
its exponent by at most a fixed constant when passing to the
nearby node. Formula (17) gives a level-independent positive lower
bound for \(|\beta_{j_N,N}|\). Hence
\[
 \sum_{j=0}^U|\beta_{j,N}Q_N(u_j)|
  \ge |\beta_{j_N,N}Q_N(u_{j_N})|
  \ge e^{N(B_f+1/100)}
 \tag{20}
\]
for sufficiently large levels of both parities. The strict reserve
in (3) absorbs the polynomial in (19). The same lower bound applies
to an absolute sum restricted to any fixed neighborhood of
\(\pi/2\). Restoring the original outside factor of modulus
\(1/N\) does not remove the exponential excess.

Thus cancellation at the middle color must be retained for the
constant outer mode as well. No lower bound for the signed sum
\(\mathcal L_N(1)\), no lower bound for the actual polynomial
insertion \(\mathcal L_N(H_N)\), and no failure of the desired
volume identity follows from (20). A uniform majorant for all
large outgoing angles at rate \(s(\pi/2)\) remains useful, but
cannot by itself meet the smaller budget \(B_f\).
