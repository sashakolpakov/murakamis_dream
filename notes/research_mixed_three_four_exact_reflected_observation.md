# Exact reflection of the remaining ordinary three/four observation

Research deduction, 7 November 2026. The complete product on the
remaining half-circle has an exact reflected representation in the
original half-band cardinal basis. Reflection changes both prescribed
boundary vectors. It does not identify this product with the already
estimated first-half source, or supply a smaller-action estimate.
No numerical evaluation is used.

## 1. Two identities of the whole finite functions

Use the original conventions
\[
 D=N-1,\qquad r=e^{-2\pi i/N},\qquad q=e^{\pi i/N},\qquad
 \kappa=q^{D^2/2},\qquad A_n=JM^n,\qquad N\ge2.
 \tag{1}
\]
Here \(J\) is coefficient reversal, \(v(w)\) is the full Newton
evaluation column, and \(h(a)\) is the original cardinal column
\[
 h_b(a)=\frac{\sin\pi N(a-b/N)}{N\sin\pi(a-b/N)},
                 \qquad 0\le b<N.
 \tag{2}
\]
All apparent singularities are removable. At even levels these
functions are antiperiodic, and their products remain periodic.
The identities \(M^T=JMJ\), \(\overline M=M^{-1}\), and
\(MJM=\kappa M^*\) retain their original scalars. In particular
\[
                         JM^*=M^{-1}J.
 \tag{3}
\]

Let \(X=e^{-2\pi ia}\). The literal cap and terminal functions
of [the ordinary pair](research_mixed_three_four_ordinary_pair_target.md)
satisfy, for every complex \(a,w\),
\[
\begin{split}
 U_{0,N}(w,X)
   &=e^{-\pi iDa}\,h(a)^T A_2v(w),\\
 V_{1,N}(w,X)
   &=\frac{e^{\pi iDa}}{\kappa^2N}\,
                    h(a)^TM^*M^3v(w).
\end{split}
 \tag{4}
\]
These are identities of the entire finite sources, not replacements
by arbitrary continuations through their physical values.

For the first identity, use
[the exact contraction](research_mixed_wire_exact_contraction.md),
equations (10), (13)--(14). Write
\[
 S=D_0M,\qquad
 (D_0)_{bb}=\frac{\kappa^{-1}(-q)^{-b}}{P_b},\qquad
 b(w)=Sv(w).
\]
Its literal first-cap identity is
\[
 (B_3b(w))_b=\kappa P_b U_{0,N}(w,r^b).
\]
On the other hand
\[
 B_3b=S^{-T}A_3v=D_0^{-1}M^{-T}JM^3v
                    =D_0^{-1}JM^2v.
\]
All \(P_b\) in this range are nonzero. Thus
\[
 U_{0,N}(w,r^b)=(-q)^b(A_2v(w))_b.
 \tag{5}
\]
The exact terminal dictionary in
[Gram transport](research_mixed_terminal_gram_shift.md), equation (2),
is
\[
 V_{1,N}(w,r^b)=\frac{(-q)^{-b}}{\kappa^2N}
                           (M^*M^3v(w))_b.
 \tag{6}
\]

The positive-degree polynomial \(U_0\) and negative-degree
polynomial \(V_1\) have respective bands \([0,D]\) and
\([-D,0]\) in \(X\). Therefore \(e^{\pi iDa}U_0\) and
\(e^{-\pi iDa}V_1\) belong to the same original half-band space
as (2). At its physical nodes,
\[
 e^{\pi iDb/N}(-q)^b=1,
 \qquad e^{-\pi iDb/N}(-q)^{-b}=1.
 \tag{7}
\]
Equations (5)--(7) and uniqueness in that fixed \(N\)-dimensional
space prove (4) for all complex \(a\), at both parities. They
are polynomial identities in the ordinary color, so every fixed
ordinary derivative is retained as well.

## 2. The reflected complete product and open contour

Set
\[
 F_N(a;w_L,w_R)=U_{0,N}(w_L,e^{-2\pi ia})
                         V_{1,N}(w_R,e^{-2\pi ia}).
\]
The two exponential factors in (4) cancel exactly:
\[
 F_N(a;w_L,w_R)=\frac1{\kappa^2N}
   [h(a)^TA_2v(w_L)]\,[h(a)^TM^*M^3v(w_R)].
 \tag{8}
\]
Evenness of the cardinal function in (2) gives
\(h(D/N-a)=Jh(a)\), with no additional parity factor. Thus
\[
 \boxed{\quad
 F_N(D/N-a;w_L,w_R)=\frac1{\kappa^2N}
   [h(a)^TM^2v(w_L)]\,[h(a)^TM^{-1}A_3v(w_R)].
 \quad}
 \tag{9}
\]
In multiplicative coordinates the reflection is
\(X\mapsto r^{-1}X^{-1}\), rather than \(X\mapsto X^{-1}\).
The exact displacement \(1/N\) has not been discarded.

Let \(\gamma_+\) be any original complementary path from
\(1/2+ic\) to \(1\), as in
[the first-half assembly](research_mixed_three_four_first_half_assembly.md).
Let \(\widetilde\gamma_+\) be its reflected path with orientation
reversed. Its endpoints are
\[
                  -1/N,\qquad 1/2-1/N-ic.
\]
Changing variables in the exact open contour gives
\[
\begin{split}
 I_{+,N}(w_L,w_R)
  =\kappa N\int_{\widetilde\gamma_+}
   [h(a)^TM^2v(w_L)]\,[h(a)^TM^{-1}A_3v(w_R)]\,da.
\end{split}
 \tag{10}
\]
Both changes of orientation are accounted for. Equation (10)
holds for the full open contour, not only for a root sum. There
is no omitted alias, endpoint forcing, selection factor, or
ordinary normal: all matrices and both prescribed boundary columns
are the full original ones.

As a normalization check, integrating (8) over a complete period
uses \(N\int hh^T=I\) and gives
\[
 \kappa^3N^2\int_0^1F_N(a)\,da
   =\kappa v(w_L)^TA_2M^*M^3v(w_R)
   =v(w_L)^TA_3A_4v(w_R).
 \tag{11}
\]
The last equality is precisely \(MJM=\kappa M^*\). Thus the
original \(\kappa^3N^2\) contour normalization is unchanged.

## 3. What the identity does and does not simplify

The reflected interval lies near the first real half-period and
has opposite incoming height. Its prescribed factors, however,
are \(h^TM^2v\) and \(h^TM^{-1}A_3v\). They are not the
original first-half \(U_0,V_1\) pair in (4). A bound for
\(U_0V_1\) cannot therefore be substituted into (10). Existing
inverse-crossing formulas with prepared Fourier endpoint vectors
also retain a different observation and do not supply that bound.

There is a simple exact exclusion of a scalar reflection into
the same family, uniformly in the two ordinary colors. The literal
support at the final physical incoming node gives
\[
 F_N(D/N;w_L,w_R)=U_{1,N}(w_R,1),
 \tag{12}
\]
which is independent of \(w_L\). At incoming zero, the
coefficients of the highest Newton polynomial \(e_D\) are
\[
 [e_D]U_{0,N}(w,1)=(-q)^{-D},\qquad
 [e_D]V_{1,N}(w,1)=\frac{(-q)^{-D}}N.
 \tag{13}
\]
Indeed the first coefficient comes only from private index \(D\),
where \((r^{-D};r)_D=P_D=N\). In the terminal source only
transform index zero can have ordinary degree \(D\); its cap
coefficient is the first one divided by \(P_D=N\).
Both numbers in (13) are nonzero. Hence \(F_N(0;w_L,w_R)\)
has degree \(D\) in each color. Neither it nor its color-swapped
version is a scalar multiple, independent of colors, of (12).
This rules out that simple pointwise reflection shortcut. It
does not rule out another exact transformed observation or a
useful estimate for the specific pair in (10).

Equations (9)--(10) are the proved reduction. A strict comparison
of the reflected signed integral with the original ordinary
action remains open; no smaller exponential rate or new
ordinary-pair asymptotic is inferred here.
