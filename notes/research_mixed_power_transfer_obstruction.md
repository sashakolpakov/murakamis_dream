# The three/four inverse transfer does not extend by changing its exponent

Research deduction, 5 November 2026. The rational ordinary-block
transfer for powers three and four follows from their exceptional
exact factorial kernels. Replacing its exponent \(2+\epsilon\) by
\(n-1\) is not an extension to the original power-\(n\) source.
There are two separate obstructions below: an exact finite-kernel
calculation and a contradiction on the original large-power
geometric branch. No numerical computation is used.

## 1. The naive factorial kernel already fails at level two

Use the original matrices and common basis of
[the mixed Fourier contraction](research_mixed_wire_exact_contraction.md):
\[
 A_n=JM^n,\qquad B_n=S^{-T}A_nS^{-1}.
 \tag{1}
\]
This definition of \(B_n\) is meaningful for every integer \(n\);
only \(B_3,B_4\) have the simple factorial formulas proved there.
At \(N=2\), put \(q=i,\kappa=e^{\pi i/4}\). The exact original
crossing and basis matrix are
\[
 M=\kappa\begin{pmatrix}1&0\\-i&1\end{pmatrix},\qquad
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 S=\begin{pmatrix}1&0\\1/2&i/2\end{pmatrix}.
 \tag{2}
\]
The unit-circle Jordan block is retained. Direct multiplication gives,
for every integer \(n\),
\[
             B_n=-i\kappa^n
                     \begin{pmatrix}n-2&2\\2&0\end{pmatrix}.
 \tag{3}
\]
In particular \(B_3=\kappa\left(\begin{smallmatrix}1&2\\2&0\end{smallmatrix}\right)\)
and \(B_4=2i\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\),
as in the established formulas.

The natural extrapolation of those formulas would be
\[
 \widetilde B_{n,ij}
       =C_{n,N}\frac{P_{i+j}}{(P_iP_j)^{\,n-3}},
       \qquad i+j<N,
 \tag{4}
\]
with a scalar \(C_{n,N}\) allowed to vary. At \(N=2\), \(P_0=1,P_1=2\).
For \(n\ge3\), (3) has ratio \(B_{n,01}/B_{n,00}=2/(n-2)\);
(4) has ratio \(2^{4-n}\). Equality requires
\[
                         n-2=2^{n-3}.
 \tag{5}
\]
This holds at \(n=3,4\) and fails for every integer \(n\ge5\):
at five the right side already exceeds the left, and doubling
preserves the strict inequality at the next integer.
No scalar normalization repairs this discrepancy. In particular
the fifth power requires a different exact kernel or an additional
summation, rather than another copy of the four-type denominator.

This finite calculation alone would not rule out an independently
proved asymptotic phase identity. The next argument rules out the
proposed inverse critical equation on the same geometric chart.

## 2. The original large-power geometric limit contradicts that equation

Take one original degree-two vertex of positive power \(n\), with
both neighboring vertices complete and with the original unit charge.
The [isolated geometric theorem](research_isolated_internal_vertex_geometry.md),
Sections 1--2, supplies its unique positive branch. Write its angle as
\(\tau_n=2a_n-2ib_n\). Its original, lifted equations are
\[
 \begin{split}
 nb_n&=2\,\operatorname{artanh}
                 \frac{\sin a_n}{\cosh b_n},\\
 na_n+2\arctan\frac{\sinh b_n}{\cos a_n}&=\pi,
 \qquad 0<a_n<\pi/2,\quad b_n>0.
 \end{split}
 \tag{6}
\]
In particular \(a_n<\pi/n\), and, for \(n\ge3\),
\[
 0<b_n\le\frac2n\operatorname{artanh}\sin(\pi/n).
 \tag{7}
\]
It follows that \(\tau_n\to0\) as \(n\to+\infty\).
This varies the fixed filling power among geometric examples; it
does not replace a fixed power by one depending on the quantum level.

Set \(A_n^{\rm geom}=\cos^2(\tau_n/2)\). For an incident edge
whose other vertex is complete, its original wire cotangent is the
branch \(q_n\) near one satisfying
\[
                       q_n^2=(A_n^{\rm geom})^{-1}.
 \tag{8}
\]
The incidence coordinate change in
[the original inverse-log calculation](research_mixed_geometric_source_log_lifts.md),
Section 4, and
[the action calibration](research_mixed_geometric_action_calibration.md),
equations (4)--(7), is independent of the own crossing power.
In a neighborhood of the complete angle it is a regular algebraic
identity. Thus the own and outside inverse-leg exponentials are
\[
 U_n=\frac{-i}{2A_n^{\rm geom}(q_n+i)-i},\qquad
 L_n=\frac{-i}{2(q_n+i)-i}.
 \tag{9}
\]
The two own incidences agree by the symmetry and uniqueness of (6),
so \(V_n=U_n\). No global three/four localization is being assumed
for these new powers: (9) is used only near the complete angle,
where (7) places every sufficiently large \(n\).

Equations (7)--(9) imply
\[
 U_n,V_n,L_n\longrightarrow
       u_0=-\frac{1+2i}{5},\qquad
 |u_0|=\frac1{\sqrt5},\qquad |1-u_0|=\sqrt{\frac85}>1.
 \tag{10}
\]
The suggested exponent replacement would impose, in these same
inverse coordinates,
\[
      (1-U_nV_n)(1-U_nL_n)=L_n(1-U_n)^{\,n-1}.
 \tag{11}
\]
The modulus of the left side is bounded, and \(L_n\) tends to a
nonzero number. The modulus of the last factor on the right grows
exponentially in \(n\). More explicitly, for all sufficiently large
\(n\), one has \(|U_n|,|L_n|\le1\), \(|L_n|\ge1/3\), and
\(|1-U_n|>6/5\). Equation (11) would then require
\[
                       4\ge\frac13(6/5)^{n-1},
 \tag{12}
\]
which fails for every sufficiently large \(n\).

Consequently (11) is not the critical equation of the original
power-\(n\) geometric branch for all \(n\), even locally near the
complete large-power limit. A different inverse chart could lead
to another rational transfer, but it must be derived and calibrated
from the original source and lifted periods.

## 3. What remains exact for arbitrary powers

The [arbitrary-power compiler](research_arbitrary_power_source_compilation.md)
still gives \(A_n=JM^n\), retaining every first normal, and exact
internal-wire averaging after the full physical traces. In the
common basis (1), power insertion is exactly
\[
                     B_{n+1}=B_n(SMS^{-1}).
 \tag{13}
\]
It is matrix multiplication, rather than entrywise division by
\(P_iP_j\). The restored geometric angular phase retains its
original quadratic term \(in\tau^2/(4\pi)\) and unit-charge term.
Thus neither the source nor its geometric continuation is missing
an exact definition. What is absent is a justified replacement of
that complete operation by the proposed low-dimensional
three/four inverse recursion.

These obstructions concern that proposed extension only. They do
not contradict the existing all-power isolated-vertex theorem, a
future uniform theorem for composed short tangles, or the original
Kashaev volume identity.
